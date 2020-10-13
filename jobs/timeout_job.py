import time
from common.constants import Statuses
import threading


def process_events(user, session_time):
    time.sleep(session_time)
    user.modify(status=Statuses.Timed_out.name)


def end_user_session(user, session_time=30):
    processing_thread = threading.Thread(target=process_events, args=(user, session_time,))
    processing_thread.start()