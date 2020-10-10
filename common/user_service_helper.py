def sort_items(data, field):
    return sorted(data, key=lambda d: d[field])


def define_event_status(event_type):
    if event_type in ["START", "STOP_BREAK"]:
        return "online"
    else:
        return "offline"

