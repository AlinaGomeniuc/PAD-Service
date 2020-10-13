from model.user import User
from model.event import Event
from flask import abort
from common import user_service_helper
from common.constants import Statuses
from service.processing_service import ProcessingService
from jobs import timeout_job


class UserService:
    @staticmethod
    def register_user(request_payload):
        if not ProcessingService.are_processing_resources_available():
            abort(404, description="Unavailable service resources")

        user = User(name=request_payload['name'],
                    surname=request_payload['surname'],
                    status=Statuses.Building.name)
        user.save()
        timeout_job.end_user_session(user, session_time=5)
        return user.to_json()

    @staticmethod
    def get_user_info(id):
        try:
            user = User.objects.get(pk=id)
        except:
            abort(404, description="User does not exist")

        return user.to_json()

    @staticmethod
    def create_event(id, request_payload):
        try:
            user = User.objects.get(pk=id)
        except:
            abort(404, description="User does not exist")

        if user_service_helper.is_session_user_timed_out(user):
            abort(404, description="User session timed out")

        event_type = request_payload['type']
        status = user_service_helper.define_event_status(event_type)
        event = Event(type=event_type,
                      status=status,
                      timestamp=request_payload['timestamp'])
        User.objects(id=id).update_one(push__events=event)
        user.reload()
        return user.to_json()


