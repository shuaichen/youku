from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import UINT32,STRING,BUFFER,BOOL

class RequestPicture(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.shuaichenwu.RequestPicure"
    DEFINITION_VERSION = "1.0"
    FIELDS = []

class Picture(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.shuaichenwu.Picture"
    DEFINITION_VERSION="1.0"
    FIELDS = [
      ("id",UINT32),
      ("picture",BUFFER)
    ]
class Answer(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.shuaichenwu.Answer"
    DEFINITION_VERSION = "1.0"
    FIELDS = [
      ("id",UINT32),
      ("answer",UINT32)
    ]

class Result(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.shuaichenwu.Result"
    DEFINITION_VERSION = "1.0"
    FIELDS = [
      ("id",UINT32),
      ("result",BOOL)
    ]

def  unittest():
 
    packet1=RequestPicture()
    packetBytes = packet1.__serialize__()
    packet1x = PacketType.Deserialize(packetBytes)
    if packet1x == packet1:
        print("These two packets of first packet are the same!")

    packet2=Picture()
    packet2Bytes = packet2.__serialize__()
    packet2.id=1
    packet2.picture=b"1.png"
    packet2x = PacketType.Deserialize(packet2Bytes)
    if packet2x == packet2:
        print("These two packets of second packet are the same!")

    packet3=Answer()
    packet3Bytes = packet3.__serialize__()
    packet3.id=1
    packet3.answer=1234
    packet3x = PacketType.Deserialize(packet3Bytes)
    if packet3x == packet3:
        print("These two packets of third packet are the same!")

    packet4=Result()
    packet4Bytes = packet4.__serialize__()
    packet4.id=1
    packet4.result=True
    packet4x = PacketType.Deserialize(packet4Bytes)
    if packet4x == packet4:
        print("These two packets of fourth packet are the same!")

    deserializer = PacketType.Deserializer()
    pktBytes = packet1.__serialize__() + packet2.__serialize__() + packet3.__serialize__() + packet4.__serialize__()
    deserializer.update(pktBytes)
    for packet in deserializer.nextPackets():
        print("got a packet!")
        if packet == packet1: print("It’s packet 1!")
        elif packet == packet2: print("It’s packet 2!")
        elif packet == packet3: print("It’s packet 3!") 
        elif pakcet == packet4: print("It’s packet 4!")


def main():
    unittest()

if __name__ == "__main__":
    main()









