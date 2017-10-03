from playground.network.common import *
from mypacket import *


class PassThroughc1(StackingProtocol):
    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        higherTransport = StackingTransport(self.transport)
        self.higherProtocol().connection_made(higherTransport)

    def data_received(self, data):
        self.higherProtocol().data_received(data)

    def connection_lost(self, exc):
        self.higherProtocol().connection_lost()
        self.transport = None


#
class PassThroughs1(StackingProtocol):
    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        higherTransport = StackingTransport(self.transport)
        self.higherProtocol().connection_made(higherTransport)

    def data_received(self, data):
        self.higherProtocol().data_received(data)

    def connection_lost(self, exc):
        self.higherProtocol().connection_lost()
        self.transport = None


#
# state machine for client
# 0: initial state
# 1: SYN sent, wait for SYN-ACK
# 2: SYN-ACK received, sent ACK
class PassThroughc2(StackingProtocol):
    def __init__(self):
        self.transport = None
        self._deserializer = PacketType.Deserializer()
        self.handshake = False
        self.seq = 0
        self.state = 0

    def connection_made(self, transport):
        self.transport = transport
        SYN = PEEPPacket()
        SYN.SequenceNumber = self.seq
        self.seq = self.seq + 1
        SYN.Type = 0  # SYN - TYPE 0
        SYN.Checksum = SYN.calculateChecksum()
        print("client: SYN sent")
        SYNbyte = SYN.__serialize__()
        self.transport.write(SYNbyte)

    def data_received(self, data):
        self._deserializer.update(data)
        for pkt in self._deserializer.nextPackets():
            if isinstance(pkt, PEEPPacket):
                if pkt.Type == 1 and self.state == 0:
                    print("SYN-ACK received")
                    if pkt.verifyChecksum():
                        ACK = PEEPPacket()
                        ACK.Type = 2  # ACK -  TYPE 2

                        self.seq = self.seq + 1
                        ACK.updateSeqAcknumber(seq=self.seq, ack=pkt.SequenceNumber + 1)
                        print("client: ACK sent")
                        ACK.Checksum = ACK.calculateChecksum()
                        self.transport.write(ACK.__serialize__())
                        self.state = 1
                        self.handshake = True
                        print("ACK sent, handshake done")
                        print("------------------------------")
                        print("upper level start here")
                        if self.handshake == True:
                            higherTransport = StackingTransport(self.transport)
                            self.higherProtocol().connection_made(higherTransport)

                            # if pkt.Type == 3:
                            #     RIP_ACK = PEEPPacket()
                            #     RIP_ACK.Type = 4
                            #     RIP_ACK.calculateChecksum()
                            #     print("client: RIP-ACK sent")
                            #     self.transport.write(RIP_ACK.__serialize__())
        if self.handshake == True:
            self.higherProtocol().data_received(data)

    def connection_lost(self, exc):
        self.higherProtocol().connection_lost()
        self.transport = None


#
# state machine for server
# 0: initial state, wait for SYN
# 1: received SYN, sent SYN-ACK, wait for ACK
# 2: ACK received, finished handshake
class PassThroughs2(StackingProtocol):
    def __init__(self):
        self.transport = None
        self._deserializer = PacketType.Deserializer()
        self.handshake = False
        self.seq = 0
        self.state = 0

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        self._deserializer.update(data)
        for pkt in self._deserializer.nextPackets():
            if isinstance(pkt, PEEPPacket):
                if pkt.Type == 0 and self.state == 0:
                    if pkt.verifyChecksum():
                        print("received SYN")
                        SYN_ACK = PEEPPacket()
                        SYN_ACK.Type = 1
                        self.seq = self.seq + 1
                        SYN_ACK.updateSeqAcknumber(seq=self.seq, ack=pkt.SequenceNumber + 1)
                        SYN_ACK.Checksum = SYN_ACK.calculateChecksum()
                        print("server: SYN-ACK sent")
                        self.transport.write(SYN_ACK.__serialize__())
                        self.state = 1
                        
                if pkt.Type == 2 and self.state ==1:
                    if pkt.verifyChecksum():
                        self.handshake = True
                        print("got ACK, handshake done")
                        print("------------------------------")
                        print("upper level start here")
                        higherTransport = StackingTransport(self.transport)
                        self.higherProtocol().connection_made(higherTransport)

                        # if pkt.Type == 3:
                        #     RIP_ACK = PEEPPacket()
                        #     RIP_ACK.Type = 4
                        #     RIP_ACK.calculateChecksum()
                        #     print("server: RIP-ACK sent")
                        #     self.transport.write(RIP_ACK.__serialize__())

        if self.handshake == True:
            self.higherProtocol().data_received(data)

    def connection_lost(self, exc):
        self.higherProtocol().connection_lost()
        self.transport = None
