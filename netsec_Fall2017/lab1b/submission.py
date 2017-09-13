from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import BUFFER,UINT32,BOOL

class RequestPicture(PacketType):
	DEFINITION_IDENTIFIER="lab1b.sw.RequestPicture"
	DEFINITION_VERSION="1.0"
	
	FIELDS=[
		("id",UINT32)
		]

class Picture(PacketType):
	DEFINITION_IDENTIFIER="lab1b.sw.Picture"
	DEFINITION_VERSION="1.0"
	FIELDS=[
		("picture",BUFFER),
		("id",UINT32)
		]

class Answer(PacketType):
	DEFINITION_IDENTIFIER="lab1b.sw.Answer"
	DEFINITION_VERSION="1.0"
	FIELDS=[
		("answer",UINT32),
		("id",UINT32)
		]

class Result(PacketType):
	DEFINITION_IDENTIFIER="lab1b.sw.Result"
	DEFINITION_VERSION="1.0"
	FIELDS=[
			
		("result",BOOL),
		("id",UINT32)
		]

def basicUnitTest():
	packet1=RequestPicture()
	packet1.id=1
	packet1Bytes=packet1.__serialize__()
	packet1a=RequestPicture.Deserialize(packet1Bytes)
	assert packet1==packet1a
	
	packet2=Picture()
	packet2.picture=b"1.png"
	packet2.id=1
	packet2Bytes=packet2.__serialize__()
	packet2a=Picture.Deserialize(packet2Bytes)
	assert packet2==packet2a
	
	packet3=Answer()
	packet3.answer=1234
	packet3.id=1
	packet3Bytes=packet3.__serialize__()
	packet3a=Answer.Deserialize(packet3Bytes)
	assert packet3==packet3a
	
	packet4=Result()
	packet4.result=True
	packet4.id=1
	packet4Bytes=packet4.__serialize__()
	packet4a=Result.Deserialize(packet4Bytes)
	assert packet4==packet4a
	

	pktBytes=packet1.__serialize__()+packet2.__serialize__()+packet3.__serialize__()+packet4.__serialize__()
	deserializer=PacketType.Deserializer()
	deserializer.update(pktBytes)
	for packet in deserializer.nextPackets():
		print("got a packet!")
		if packet==packet1:print("It's packet 1!")
		elif packet==packet2:print("It's packet 2!")
		elif packet==packet3:print("It's packet 3!")
		elif packet==packet4:print("It's packet 4!")
		
	
	print ("Finish the test!")
	
if  __name__=="__main__":
	basicUnitTest()
	
	
