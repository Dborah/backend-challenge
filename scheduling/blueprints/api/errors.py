from flask_restful import abort


def error_404(query, _id, name):

    if query is None:
        # abort(404, message=f"Room {_id}, doesn't exist.")
        if name == 'room':
            abort(404, message=f"Room {_id}, doesn't exist.")
        else:
            abort(404, message=f"Scheduling {_id}, doesn't exist.")

