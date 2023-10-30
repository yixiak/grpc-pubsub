# Copyright (c) 2023 yixiak
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import asyncio
import logging
import subprocess

import queue
import grpc
import pubsub_pb2
import pubsub_pb2_grpc
from concurrent import futures

logging.basicConfig(level=logging.INFO)

class pubsubServicer(pubsub_pb2_grpc.pubsubServicer):
    def __init__(self):
        # stores the lists of a topic's subscribers
        self.subscribers = {}
        
        # the list of theme created
        self.themeList=[]
        
        # store the message list of each theme
        self.message={}
    
    def getTheme(self, request, context):
        response=pubsub_pb2.themeList(theme_index=[i for i in self.themeList])
        
        return response

    def subscribe(self, request, context):
        """ 
            subsciber subscribe the theme
            two themes will be the same if successful
        """
        logging.info('enter subscribe')
        theme_index = request.theme_index
        # there is no such a theme
        # return -1 for fail
        if theme_index not in self.themeList:
            response =pubsub_pb2.sub(theme_index=pubsub_pb2.theme(theme_index=-1),text=message)
            logging.info('there is no such theme')
        # add this client into subscribers list
        else:
            if self.message[theme_index].empty():
                response = pubsub_pb2.sub(theme_index=pubsub_pb2.theme(theme_index=-1),text=message)
            else:
                message=self.message[theme_index].get()
                response = pubsub_pb2.sub(theme_index=pubsub_pb2.theme(theme_index=theme_index),text=message)
        return response

    def createTheme(self, request, context):
        """publisher create a theme
        two themes will be the same if successful
        """
        logging.info("enter createTheme")
        theme = request.theme_index
        self.themeList.append(theme)
        self.subscribers[theme]=[]
        self.message[theme]=queue.Queue()
        return pubsub_pb2.theme(theme_index=theme)
        
        pass

    def publish(self, request, context):
        """publisher publish a message to server
        """
        logging.info("enter publish")
        theme = request.theme_index.theme_index
        message = request.text
        
        if theme in self.message:
            self.message[theme].put(message)
            logging.info(f"add message {message} into theme {theme}")
                
        return pubsub_pb2.theme(theme_index=theme)
        
def server():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    
    pubsub_pb2_grpc.add_pubsubServicer_to_server(pubsubServicer(),server)
    server.add_insecure_port("localhost:50052")
    server.start()
    server.wait_for_termination()

if __name__=="__main__":
    server()