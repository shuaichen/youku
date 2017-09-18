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

class EchoServerProtocol(asyncio.Protocol):
	def connection_made(self,transport):
		print ("Echo Server Connected to Client")
		self.transport=transport
		self.status=0
		self._deserializer=PacketType.Deserializer()
	def data_received(self,data):
		self._deserializer.update(data)
		for pkt in self._deserializer.nextPackets():
			
			if isinstance(pkt,RequestPicture):
				packet2=Picture()
				packet2.id=pkt.id
				packet2.picture=b"1.png"
				self.status+=1
				self.transport.write(packet2.__serialize__())
			elif isinstance(pkt,Answer):
				packet4=Result()
				packet4.id=pkt.id
				if pkt.answer==1234:
					packet4.result=True
					
				else:
					packet4.result=False
					
				self.status+=1
				self.transport.write(packet4.__serialize__())

			else:
				print ("This is a wrong packet")
	def connection_lost(self,exc):
		print ("Echo Server Connection Lost because {}".format(exc))
		self.transport=None

if __name__=="__main__":
        f = StackingProtocolFactory(lambda: PassThrough1(), lambda: PassThrough2())
        ptConnector = playground.Connector(protocolStack=f)
        playground.setConnector("passthrough", ptConnector)

        loop=asyncio.get_event_loop()
        loop.set_debug(enabled=True)
        coro=playground.getConnector('passthrough').create_playground_server(lambda:EchoServerProtocol(),800)
        loop.run_until_complete(coro)
        loop.run_forever()
        loop.close()
