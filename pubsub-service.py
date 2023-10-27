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

class pubsubServicer(pubsub_pb2_grpc.pubsubServicer):
    def __init__(self):
        # stores the lists of a topic's subscribers
        self.subscribers = {}
    
    def getTheme(self, request, context):
        themelist=pubsub_pb2.themeList()
        
        
        return pubsub_pb2.themeList()

    def subscribe(self, request, context):
        """subsciber subscribe the theme
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
        pass

    def publish(self, request, context):
        """publisher publish a message 
        """
        pass