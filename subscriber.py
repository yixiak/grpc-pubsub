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

def subscribe(theme_index):
    channel = grpc.insecure_channel('localhost:50051')
    client = pubsub_pb2_grpc.pubsubStub(channel)
    
    request = pubsub_pb2.theme(theme_index=theme_index)
    response = client.subscribe(request)
    
    if response and response.theme_index==theme_index:
        print(f"Subscribe to {theme_index} successfully")
    else:
        print(f"Failed to subscribe to {theme_index}")
        
def getTheme():
    channel = grpc.insecure_channel('localhost:50051')
    client = pubsub_pb2_grpc.pubsubStub(channel)
    request = pubsub_pb2.Request()
    
    response = client.getTheme(request)
    if response:
        print(f"get the theme list: {response}")
    else:
        print(f"Failed")