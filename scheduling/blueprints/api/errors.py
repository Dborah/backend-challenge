from flask import jsonify
from flask_restful import abort


def error_data_invalid():
    pass


def error_already_exists(msg):
    """Response 400"""
    response = jsonify({
        'error': f'{msg} already exists.'
    })
    response.status_code = 400
    return response


def error_unavailable():
    """Response 400"""
    response = jsonify({
        'error': f'Room Unavailable for this Period.'
    })
    response.status_code = 400
    return response


def error_room_linked_to_schedule(msg):
    """Response 401"""
    response = jsonify({
        'error': f'This room {msg} has been reserved for one or more meetings. '
        f'Please choose another one or try updating it. Or removed to Schedule'
    })
    response.status_code = 401
    return response


def error_not_allowed():
    """Response 405 Not Allowed"""
    response = jsonify({
        "error": "The method is not allowed for the requested URL."
    })
    response.status_code = 405
    return response


def error_does_not_exist(resource, msg):
    """Response 404 Not Found"""
    if not resource:
        abort(http_status_code=404, error=f"{msg} does not exist.")
