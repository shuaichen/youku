import playground
from playground.network.common import StackingProtocol, StackingTransport, StackingProtocolFactory

class PassThrough1(StackingProtocol):
    def __init__(self):
        super().__init__()
        print("pass through constructor 1")


    def connection_made(self,transport):
        print("connection made")
        self.transport=transport
        higherTransport=StackingTransport(self.transport)
        self.higherProtocol().connection_made(higherTransport)
        print('PassThrough1 connection is made')

    def data_received(self,data):
        self.data=data
        self.higherProtocol().data_received(data)
        print('Passthrough1 pass data up')

    def connection_lost(self,exc):
        self.higherProtocol().connection_lost(exc)
        print('Passthrough1 lost the connection')
        

class PassThrough2(StackingProtocol):

    

    def connection_made(self,transport):

        self.transport=transport
        higherTransport=StackingTransport(self.transport)
        self.higherProtocol().connection_made(higherTransport)
        print('PassThrough2 connection is made')

    def data_received(self,data):
        self.data=data
        self.higherProtocol().data_received(data)
        print('Passthrough2 pass data up')

    def connection_lost(self,exc):
        self.higherProtocol().connection_lost(exc)
        print('Passthrough2 lost the connection')
        


