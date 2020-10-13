import threading
from common.user_service_helper import sort_items
from common.constants import Statuses, PROCESSING_TIME
from datetime import datetime
import time
import json


def compute_user_working_hours(user):
    events = sort_items(json.loads(user.to_json())["events"], "timestamp")
    prev_event = None
    default_value = datetime.strptime('0001-01-01 00:00', '%Y-%m-%d %H:%M')
    hours = default_value
    for event in events:
        if prev_event is not None and event["status"] == "offline" and prev_event["status"] == "online":
            hours += datetime.strptime(event["timestamp"], '%Y-%m-%d %H:%M') - \
                     datetime.strptime(prev_event["timestamp"], '%Y-%m-%d %H:%M')
        prev_event = event
    hours -= default_value
    return str(hours)


def process_events(user, process_time):
    time.sleep(process_time)
    working_hours = compute_user_working_hours(user)
    user.modify(worked_hours=working_hours)
    user.modify(status=Statuses.Processed.name)


def process_user_events(user, process_time=PROCESSING_TIME):
    processing_thread = threading.Thread(target=process_events, args=(user, process_time,))
    processing_thread.start()
