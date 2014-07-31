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
        
        if PROTOCOLS <= self.protocols:
            print 'protocols is over !!!'
            return
        
        self.protocols += 1
        
        return ChatProtocol(self)



def start(port):
    FACTORY = ProtocolFactory()
    reactor.listenTCP(port,FACTORY)
    reactor.run()