from flask import jsonify
from flask_restful import abort


def resp_data_invalid():
    pass


def resp_already_exists(msg):
    """Response 400"""
    response = jsonify({
        'message': f'{msg} already exists.'
    })
    response.status_code = 400
    return response


def resp_unavailable():
    """Response 400"""
    response = jsonify({
        'message': f'Room Unavailable for this Period.'
    })
    response.status_code = 400
    return response


def resp_room_linked_to_schedule(msg):
    """Response 401"""
    response = jsonify({
        'message': f'This room {msg} has been reserved for one or more meetings. '
        f'Please choose another one or try updating it. Or removed to Schedule'
    })
    response.status_code = 401
    return response


def resp_not_allowed():
    """Response 405 Not Allowed"""
    response = jsonify({
        "message": "The method is not allowed for the requested URL."
    })
    response.status_code = 405
    return response


def resp_does_not_exist(resource, msg):
    """Response 404 Not Found"""
    if not resource:
        abort(http_status_code=404, message=f"{msg} does not exist.")


def resp_successful(data):
    """ Response 200"""
    response = jsonify(data)
    response.status_code = 200
    return response


def resp_created_successfully(msg):
    """Response 201"""
    response = jsonify({
        'message': f'New {msg} created successfully.'
    })
    response.status_code = 201
    return response


def resp_update_successfully(msg):
    """Response 201"""
    response = jsonify({
        'message': f'{msg} updated successfully.'
    })
    response.status_code = 201
    return response


def resp_delete_successfully(msg):
    """Response 200"""
    response = jsonify({
        'message': f'{msg} delete successfully.'
    })
    response.status_code = 200
    return response


def resp_not_meeting(msg):
    """Response """
    messages = {
        'room': 'No meetings scheduled in this room.',
        'date': 'No meeting scheduled on this date.',
        'meeting': 'No meeting scheduled in this period in this room.'
    }
    response = jsonify({
        'message': messages[msg]
    })
    response.status_code = 200
    return response
