from service.user_service import UserService
from model.user import User
from model.event import Event
from flask import abort
import json
from common import user_service_helper
from common.constants import Statuses


class UserServiceImpl(UserService):
    def register_user(self, request_payload):
        user = User(name=request_payload['name'],
                    surname=request_payload['surname'],
                    status=Statuses.Building.name)
        user.save()
        return user.to_json()

    def create_event(self, id, request_payload):
        try:
            user = User.objects.get(pk=id)
        except:
            abort(404, description="User does not exist")

        event_type = request_payload['type']
        status = user_service_helper.define_event_status(event_type)
        event = Event(type=event_type,
                      status=status,
                      timestamp=request_payload['timestamp'])
        User.objects(id=id).update_one(push__events=event)
        user.reload()
        return user.to_json()

    def compute_user_working_hours(self, id):
        try:
            user = User.objects.get(pk=id)
        except:
            abort(404, description="User does not exist")

        user.modify(status=Statuses.Processing.name)
        events = user_service_helper.sort_items(json.loads(user.to_json())["events"], "timestamp")
        working_hours = user_service_helper.compute_working_hours(events)
        user.modify(worked_hours=working_hours)
        return user.to_json()
