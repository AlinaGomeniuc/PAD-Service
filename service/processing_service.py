from jobs import processing_job
from flask import jsonify, abort
from model.user import User
from common.constants import Statuses, LOW_PRIORITY_LIMIT, HIGH_PRIORITY_LIMIT
from common import user_service_helper
from mongoengine.errors import ValidationError, DoesNotExist


def compute_working_hours(id):
    user = None
    try:
        user = User.objects.get(pk=id)
    except (ValidationError, DoesNotExist):
        abort(404, description="User does not exist")

    if user_service_helper.check_user_status(user, "Timed_out"):
        abort(404, description="User session timed out")

    user.modify(status=Statuses.Processing.name)
    processing_job.process_user_events(user)
    return user.to_json()


def get_processing_users_nr():
    count = User.objects.filter(status__in=["Processing", "Building"]).count()
    return jsonify({"count": count})


def are_processing_resources_available(priority_type):
    current_processing_nr = get_processing_users_nr()
    if priority_type == "low":
        return current_processing_nr.json["count"] < LOW_PRIORITY_LIMIT
    elif priority_type == "high":
        return current_processing_nr.json["count"] < LOW_PRIORITY_LIMIT + HIGH_PRIORITY_LIMIT
