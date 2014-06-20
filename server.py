#code:utf-8

from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet import reactor

from settings import *

from msg import Message

FACTORY = None

class ChatProtocol(Protocol):
    
    def __init__(self,factory):
        self.factory = factory
        print '__init__'
    
    def dataReceived(self, data):
        print '...dataReceived'
    
    def connectionLost(self, reason):
        print '...connectionLost'
    

class ProtocolFactory(Factory):
    
    protocols = 0
    
    def __init__(self):
        pass
    
    def buildProtocol(self):
        
        self.protocols += 1
        
        return ChatProtocol(self)


if __name__ == '__main__':
    
    FACTORY = ProtocolFactory()
    reactor.listenTCP(PORT,FACTORY)
    reactor.run()