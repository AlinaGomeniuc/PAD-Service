import time
from common.constants import Statuses, SESSION_TIME
import threading
from common import user_service_helper


def process_events(user, session_time):
    time.sleep(session_time)
    if user_service_helper.check_user_status(user, "Building"):
        user.modify(status=Statuses.Timed_out.name)


def end_user_session(user, session_time=SESSION_TIME):
    processing_thread = threading.Thread(target=process_events, args=(user, session_time,))
    processing_thread.start()