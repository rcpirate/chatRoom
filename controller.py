# -*- coding: utf-8 -*- 
'''
Created on 2014年7月28日
@author: rcpirate
控制中心
'''
from message import data_parse

#线程数量
controllers = []


def dispath(chatProtocol,data):
    '''数据分发
    主要根据任务量来分发给子线程处理
    '''
    data_parse(data)
    pass

class Controller(object):
    
    def __init__(self):
        pass
    
    


