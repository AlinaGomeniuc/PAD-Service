def sort_items(data, field):
    return sorted(data, key=lambda d: d[field])


def define_event_status(event_type):
    if event_type in ["START", "STOP_BREAK"]:
        return "online"
    else:
        return "offline"


def is_session_user_timed_out(user):
    return user.status == "Timed_out"

