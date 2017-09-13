from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import UINT32,STRING,BUFFER,BOOL

class RequestPicture(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.shuaichenwu.RequestPicture"
    DEFINITION_VERSION = "1.0"
    FIELDS = [
        ("id",UNIT32)
    ]

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
    assert packet1x == packet1
       

    packet2=Picture()
    packet2Bytes = packet2.__serialize__()
    packet2.id=1
    packet2.picture=b"1.png"
    packet2x = PacketType.Deserialize(packet2Bytes)
    assert packet2x == packet2
       

    packet3=Answer()
    packet3Bytes = packet3.__serialize__()
    packet3.id=1
    packet3.answer=1234
    packet3x = PacketType.Deserialize(packet3Bytes)
    assert packet3x == packet3
        

    packet4=Result()
    packet4Bytes = packet4.__serialize__()
    packet4.id=1
    packet4.result=True
    packet4x = PacketType.Deserialize(packet4Bytes)
    assert packet4x == packet4
       

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









