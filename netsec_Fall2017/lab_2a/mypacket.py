from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import *
from playground.network.packet.fieldtypes.attributes import *


class RequestToConnect(PacketType):
    DEFINITION_IDENTIFIER = "RequestToConnect"
    DEFINITION_VERSION = "1.0"


class NameRequest(PacketType):
    DEFINITION_IDENTIFIER = "NameRequest"
    DEFINITION_VERSION = "1.0"
    FIELDS = [
        ("ID", UINT32),
        ("question", STRING)
    ]


class AnswerNameRequest(PacketType):
    DEFINITION_IDENTIFIER = "AnswerNameRequest"
    DEFINITION_VERSION = "1.0"
    FIELDS = [
        ("ID", UINT32),
        ("name", STRING)
    ]


class Result(PacketType):
    DEFINITION_IDENTIFIER = "result"
    DEFINITION_VERSION = "1.0"
    FIELDS = [
        ("result", BOOL)
    ]


class PEEPPacket(PacketType):
    DEFINITION_IDENTIFIER = "PEEP.Packet"
    DEFINITION_VERSION = "1.0"

    FIELDS = [
        ("Type", UINT8),
        ("SequenceNumber", UINT32({Optional: True})),
        ("Checksum", UINT16),
        ("Acknowledgement", UINT32({Optional: True})),
        ("Data", BUFFER({Optional: True}))
    ]