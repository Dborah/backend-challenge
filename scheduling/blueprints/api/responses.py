# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import abort


def resp_data_invalid():
    pass


def resp_does_not_exist(resource, msg):
    """
    Response 404 Not Found

    :return:
    """
    if not resource:
        abort(http_status_code=404, message=f"{msg} does not exist.")


def resp_already_exists(msg):
    """
    Response 400

    :return:
    """
    resp = jsonify({
        'message': f'{msg} already exists.'
    })
    resp.status_code = 400
    return resp


def resp_created_successfully(msg):
    """
    Response 201
    Feature successfully created

    :return:
    """
    resp = jsonify({
        'message': f'New {msg} created successfully.'
    })
    resp.status_code = 201
    return resp


def resp_update_successfully(msg):
    """
    Response 200
    Feature successfully update

    :return:
    """
    resp = jsonify({
        'message': f'{msg} updated successfully.'
    })
    resp.status_code = 201
    return resp


def resp_delete_successfully(msg):
    """
    Response 202
    Feature successfully delete

    :return:
    """
    resp = jsonify({
        'message': f'{msg} delete successfully.'
    })
    resp.status_code = 202
    return resp


def resp_room_linked_to_schedule():
    """
    Response 400

    :return:
    """
    pass
