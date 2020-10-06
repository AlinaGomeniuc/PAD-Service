from datetime import datetime


def sort_items(data, field):
    return sorted(data, key=lambda d: d[field])


def compute_working_hours(events):
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


def define_event_status(event_type):
    if event_type in ["START", "STOP_BREAK"]:
        return "online"
    else:
        return "offline"

