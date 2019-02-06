from marshmallow import fields, Schema


class RoomSchema(Schema):
    id = fields.Integer(dump_only=True)
    room_number = fields.Integer(dump_only=True)


class ScheduleSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.Integer(dump_only=True)
    date = fields.String(dump_only=True)
    room_id = fields.Integer(dump_only=True)
    room_number = fields.String(dump_only=True)
