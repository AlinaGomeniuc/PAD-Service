from jobs import processing_job
from flask import jsonify, abort
from model.user import User
from common.constants import Statuses, LIMIT
from common import user_service_helper


def compute_working_hours(id):
    try:
        user = User.objects.get(pk=id)
    except:
        abort(404, description="User does not exist")

    if user_service_helper.check_user_status(user, "Timed_out"):
        abort(404, description="User session timed out")

    user.modify(status=Statuses.Processing.name)
    processing_job.process_user_events(user)
    return user.to_json()


def get_processing_users_nr():
    count = User.objects.filter(status__in=["Processing", "Building"]).count()
    return jsonify({"count": count})


def are_processing_resources_available():
    current_processing_nr = get_processing_users_nr()
    return current_processing_nr.json["count"] < LIMIT
