from flask import request
import json
from common.config import app
from service.user_service import UserService
from service.processing_service import ProcessingService


@app.route("/api/user", methods=["POST"])
def register_user():
    request_payload = json.loads(request.data)
    return UserService.register_user(request_payload)


@app.route("/api/user/<id>", methods=["GET"])
def get_user(id):
    return UserService.get_user_info(id)


@app.route("/api/user/<id>/event", methods=["PUT"])
def register_user_event(id):
    request_payload = json.loads(request.data)
    return UserService.create_event(id, request_payload)


@app.route("/api/user/<id>/finalize", methods=["PUT"])
def compute_user_working_hours(id):
    return ProcessingService.compute_working_hours(id)


@app.route("/api/user/status", methods=["GET"])
def get_processing_users_nr():
    return ProcessingService.get_processing_users_nr()


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

