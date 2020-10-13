from flask import request
import json
from common.config import app
from service import user_service
from service import processing_service


@app.route("/api/user", methods=["POST"])
def register_user():
    request_payload = json.loads(request.data)
    return user_service.register_user(request_payload)


@app.route("/api/user/<id>", methods=["GET"])
def get_user(id):
    return user_service.get_user_info(id)


@app.route("/api/user/<id>/event", methods=["PUT"])
def register_user_event(id):
    request_payload = json.loads(request.data)
    return user_service.create_event(id, request_payload)


@app.route("/api/user/<id>/finalize", methods=["PUT"])
def compute_user_working_hours(id):
    return processing_service.compute_working_hours(id)


@app.route("/api/user/status", methods=["GET"])
def get_processing_users_nr():
    return processing_service.get_processing_users_nr()


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

