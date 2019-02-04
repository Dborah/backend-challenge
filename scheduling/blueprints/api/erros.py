from flask_restful import abort


def error_404(query, _id):
    if query is None:
        abort(404, message=f"Room {_id}, doesn't exist")

