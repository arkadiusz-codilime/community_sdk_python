# Local application imports
from api_calls.api_call_decorators import get, post, put, delete, payload_type
from api_calls.api_call import APICall


@get
def get_device_labels() -> APICall:
    """Returns an array of device_labels objects
    that each contain information about an individual device_label."""
    return APICall("/deviceLabels")

@get
def get_device_label_info(device_label_id: int) -> APICall:
    """Returns a device_label object
    containing information about an individual device_label"""
    url_path = f"/deviceLabels/{device_label_id}"
    return APICall(url_path)

@post
@payload_type(dict)
def create_device_label() -> APICall:
    """Creates and returns a device_label object
    containing information about an individual device_label"""
    return APICall("/deviceLabels")

@put
@payload_type(dict)
def update_device_label(device_label_id: int) -> APICall:
    """Updates and returns a device_label object
    containing information about an individual device_label"""
    url_path = f"/deviceLabels/{device_label_id}"
    return APICall(url_path)

@delete
def delete_device_label(device_label_id: int) -> APICall:
    """Deletes a device_label."""
    url_path = f"/deviceLabels/{device_label_id}"
    return APICall(url_path)
