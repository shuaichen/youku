from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import UINT32,BOOL,BUFFER
from playground.asyncio_lib.testing import TestLoopEx
from playground.network.testing import MockTransportToStorageStream
from playground.network.testing import MockTransportToProtocol
from Packet import RequestPicture,Picture,Answer,Result
import playground
import asyncio
from playground.network.common import StackingProtocol, StackingTransport, StackingProtocolFactory
from PassThrough import PassThrough1, PassThrough2

class EchoClientProtocol(asyncio.Protocol):
	def __init__(self):
		
		self.transport=None
	def connection_made(self,transport):
		print("connection_made echo")
		self.transport=transport
		self.status=0
		self._deserializer=PacketType.Deserializer()
		packet1=RequestPicture()
		packet1.id=1
		self.transport.write(packet1.__serialize__())
		print("done sending in connection_made")
		
	def data_received(self,data):
		print("data received echo client")
		self._deserializer.update(data)
		for pkt in self._deserializer.nextPackets():
			
			if isinstance(pkt,Picture):
				packet3=Answer()
				packet3.id=pkt.id
				packet3.answer=1234
				self.status+=1
				self.transport.write(packet3.__serialize__())
			elif isinstance(pkt,Result):

				self.status+=1
				print ("The code you input is",pkt.result)
			
			else:
				print ("This is a wrong packet!")
	def connection_lost(self,exc):
		print ("Echo Client Connection lost because{}".format(exc))		
		self.transport=None

if __name__=="__main__":
        f = StackingProtocolFactory(lambda: PassThrough1(), lambda: PassThrough2())
        ptConnector = playground.Connector(protocolStack=f)
        playground.setConnector("passthrough", ptConnector)

        loop=asyncio.get_event_loop()
        loop.set_debug(enabled=True)
        coro=playground.getConnector('passthrough').create_playground_connection(lambda:EchoClientProtocol(),"20174.1.1.1",800)
         
        loop.run_until_complete(coro)
        loop.run_forever()
        loop.close()


