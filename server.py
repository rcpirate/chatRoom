# -*- coding: utf-8 -*- 

from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet import reactor

from settings import *
from controller import dispath

FACTORY = None

class ChatProtocol(Protocol):
    
    def __init__(self,factory):
        self.factory = factory
        
    def connectionMade(self):
        print self.transport.getHost()
        pass
    
    def dataReceived(self, data):
        dispath(self,data)
        print data
    
    def connectionLost(self, reason):
        print '...connectionLost'
    

class ProtocolFactory(Factory):
    
    protocols = 0
    
    def __init__(self):
        pass
    
    def buildProtocol(self):
        
        if PROTOCOLS <= self.protocol:
            print 'protocols is over !!!'
            return
        
        self.protocols += 1
        
        return ChatProtocol(self)


def start(port):
    FACTORY = ProtocolFactory()
    reactor.listenTCP(8193,FACTORY)
    reactor.listenTCP(port,FACTORY)
    reactor.run()
