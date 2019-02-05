from scheduling.blueprints.api.schemas import RoomSchema, ScheduleSchema

room_schema = RoomSchema()


def room_serializer(content):
    serialized = room_schema.dump(content, many=True).data
    return serialized


schedule_schema = ScheduleSchema()


def schedule_serializer(content):
    serialized = schedule_schema.dump(content, many=True).data
    return serialized
