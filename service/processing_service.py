from common import processing_job
from flask import jsonify, abort
from model.user import User
from common.constants import Statuses, LIMIT


class ProcessingService:

    @staticmethod
    def compute_working_hours(id):
        try:
            user = User.objects.get(pk=id)
        except:
            abort(404, description="User does not exist")

        user.modify(status=Statuses.Processing.name)
        processing_job.process_user_events(user)
        return user.to_json()

    @staticmethod
    def get_processing_users_nr():
        count = User.objects.filter(status__in=["Processing", "Building"]).count()
        return jsonify({"count": count})

    @staticmethod
    def are_processing_resources_available():
        current_processing_nr = ProcessingService.get_processing_users_nr()
        return current_processing_nr.json["count"] < LIMIT
