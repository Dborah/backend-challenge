from flask import jsonify


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
    """Response 202"""
    response = jsonify({
        'message': f'{msg} delete successfully.'
    })
    response.status_code = 202
    return response


def resp_not_meeting(msg):
    """Response 200"""
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
