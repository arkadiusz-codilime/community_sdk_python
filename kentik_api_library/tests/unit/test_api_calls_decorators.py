from unittest.mock import MagicMock

from kentik_api.api_calls.api_call_decorators import get, post, put, delete, payload_type
from kentik_api.api_calls.api_call import APICall, APICallMethods


def test_get_decorator__adds_query_method_get_to_api_call():
    # GIVEN
    mock = MagicMock()
    decorated = get(mock)
    mock.return_value = APICall("dummy_url")

    # WHEN
    decorated_result = decorated()

    # THEN
    assert decorated_result.method.value is APICallMethods.GET.value

def test_post_decorator__adds_query_method_get_to_api_call():
    # GIVEN
    mock = MagicMock()
    decorated = post(mock)
    mock.return_value = APICall("dummy_url")

    # WHEN
    decorated_result = decorated()

    # THEN
    assert decorated_result.method.value is APICallMethods.POST.value

def test_put_decorator__adds_query_method_get_to_api_call():
    # GIVEN
    mock = MagicMock()
    decorated = put(mock)
    mock.return_value = APICall("dummy_url")

    # WHEN
    decorated_result = decorated()

    # THEN
    assert decorated_result.method.value is APICallMethods.PUT.value

def test_delete_decorator__adds_query_method_get_to_api_call():
    # GIVEN
    mock = MagicMock()
    decorated = delete(mock)
    mock.return_value = APICall("dummy_url")

    # WHEN
    decorated_result = decorated()

    # THEN
    assert decorated_result.method.value is APICallMethods.DELETE.value
