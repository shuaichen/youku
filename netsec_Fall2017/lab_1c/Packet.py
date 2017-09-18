from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import UINT32,BOOL,BUFFER

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
		
