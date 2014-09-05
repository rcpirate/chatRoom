# -*-coding:utf-8 -*-
'''
针对恶意连接，如果发现连接过来发送的协议格式不正确就加入到，拒绝连接的列表中去
'''
from twisted.application import internet,service
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
        print 'ProtocolFactory is create ...'
    
    def buildProtocol(self,addr):
        
        if MAX_PROTOCOLS >= self.protocols:
            print 'protocols is over !!!'
            return
        
        return ChatProtocol(self)

def start_application(port):
    application = service.Application('chatRoom', 1, 1)
    factory = ProtocolFactory()
    tcpServer = internet.TCPServer(port,factory)
    tcpServer.setServerParent(service.IServiceCollection(application))

def start(port):
    FACTORY = ProtocolFactory()
    reactor.listenTCP(port,FACTORY)
    reactor.run()
    
    
if __name__ == '__main__':
    start(8192)
    
    
    