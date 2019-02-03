from scheduling.blueprints.api.models import RoomSchema

room_schema = RoomSchema()


def room_serializer(content):
    serialized = room_schema.dump(content, many=True).data
    return serialized
