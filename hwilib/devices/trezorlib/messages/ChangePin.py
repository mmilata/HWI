# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class ChangePin(p.MessageType):
    MESSAGE_WIRE_TYPE = 4

    def __init__(
        self,
        remove: bool = None,
    ) -> None:
        self.remove = remove

    @classmethod
    def get_fields(cls):
        return {
            1: ('remove', p.BoolType, 0),
        }
