from flask import jsonify
from flask_restful import abort


def resp_data_invalid():
    pass


def resp_does_not_exist(resource, msg):
    """Response 404 Not Found"""
    if not resource:
        abort(http_status_code=404, message=f"{msg} does not exist.")


def resp_already_exists(msg):
    """Response 400"""
    resp = jsonify({
        'message': f'{msg} already exists.'
    })
    resp.status_code = 400
    return resp


def resp_room_linked_to_schedule(msg):
    """Response 401"""
    resp = jsonify({
        'message': f'This room {msg} has been reserved for one or more meetings. '
        f'Please choose another one or try updating it. Or removed to Schedule'
    })
    resp.status_code = 401
    return resp


def resp_created_successfully(msg):
    """Response 201"""
    resp = jsonify({
        'message': f'New {msg} created successfully.'
    })
    resp.status_code = 201
    return resp


def resp_update_successfully(msg):
    """Response 201"""
    resp = jsonify({
        'message': f'{msg} updated successfully.'
    })
    resp.status_code = 201
    return resp


def resp_delete_successfully(msg):
    """Response 202"""
    resp = jsonify({
        'message': f'{msg} delete successfully.'
    })
    resp.status_code = 202
    return resp


def resp_successful(resource):
    """ Response 200"""
    resp = jsonify(resource)
    resp.status_code = 200
    return resp



