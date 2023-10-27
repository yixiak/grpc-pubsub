# Copyright (c) 2023 yixiak
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import asyncio
import logging
import subprocess
import time

import grpc
import pubsub_pb2
import pubsub_pb2_grpc

def createTheme(stub,theme):
    request = pubsub_pb2.theme(theme_index=theme)
    response = stub.createTheme(request)
    
    if response:
        print(f"create theme {theme} successfully")
    

def publish(stub,theme,text):
    pub = pubsub_pb2.pub(theme_index=pubsub_pb2.theme(theme_index=theme),text=text)
    response = stub.publish(pub)
    if response:
        print(f"publish to {theme} successfully")

def run():
    with grpc.insecure_channel("localhost:50052") as channel:
        stub = pubsub_pb2_grpc.pubsubStub(channel)
        createTheme(stub,1)
        time.sleep(5)
        publish(stub,1,"hello")
        
run()