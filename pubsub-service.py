# Copyright (c) 2023 yixiak
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import asyncio
import logging
import subprocess

import grpc
import pubsub_pb2
import pubsub_pb2_grpc
from concurrent import futures

class pubsubServicer(pubsub_pb2_grpc.pubsubServicer):
    def __init__(self):
        # stores the lists of a topic's subscribers
        self.subscribers = {}
        
        # the list of theme created
        self.themeList=[]
    
    def getTheme(self, request, context):
        response=pubsub_pb2.themeList(theme_index=[i for i in self.themeList])
        
        return response

    def subscribe(self, request, context):
        """ 
            subsciber subscribe the theme
            two themes will be the same if successful
        """
        
        theme_index = request.theme_index
        # there is no such a theme
        # return -1 for fail
        if theme_index not in self.subscribers:
            response = pubsub_pb2.theme(theme_index=-1)
            
        # add this client into subscribers list
        else:
            self.subscribers[theme_index].append(context)
            response = pubsub_pb2.theme(theme_index=theme_index)
        return response

    def createTheme(self, request, context):
        """publisher create a theme
        two themes will be the same if successful
        """
        print("enter createTheme")
        theme = request.theme_index
        self.themeList.append(theme)
        self.subscribers[theme]=[]
        return pubsub_pb2.theme(theme_index=theme)
        
        pass

    def publish(self, request, context):
        """publisher publish a message to server
        """
        theme = request.theme_index.theme_index
        message = request.text
        
        if theme in self.subscribers:
            for subscriber in self.subscribers[theme]:
                subscriber.send(request)
                
        return pubsub_pb2.theme(theme_index=theme)
        
def server():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    
    pubsub_pb2_grpc.add_pubsubServicer_to_server(pubsubServicer(),server)
    server.add_insecure_port("localhost:50052")
    server.start()
    server.wait_for_termination()

if __name__=="__main__":
    server()