# -*-cod:utf-8 -*-

from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet import reactor

from settings import *
from controller import dispatch

class ChatProtocol(Protocol):
    
    def __init__(self,factory):
        self.factory = factory
        
    def connectionMade(self):
        pass
    
    def dataReceived(self, data):
        print data
    
    def connectionLost(self, reason):
        print '...connectionLost'
    

class ProtocolFactory(Factory):
    
    def __init__(self):
        pass
    
    def buildProtocol(self,addr):
        
        if MAX_PROTOCOLS <= self.protocols:
            print 'protocols is over !!!'
            return
        
        return ChatProtocol(self)



def start(port):
    FACTORY = ProtocolFactory()
    reactor.listenTCP(port,FACTORY)
    reactor.run()
    
    
if __name__ == '__main__':
    start(8192)
    
    
    