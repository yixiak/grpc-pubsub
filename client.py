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

logging.basicConfig(level=logging.INFO)
def subscribe(stub, theme_index):
    request = pubsub_pb2.theme(theme_index=theme_index)
    response = stub.subscribe(request)
    
    if response and response.theme_index.theme_index==theme_index:
        logging.info(f"Subscribe to {theme_index} successfully")
        logging.info(f"theme {theme_index}: {response.text}")
    else:
        logging.info(f"Failed to subscribe to {theme_index}")
        
def getTheme(stub):

    request = pubsub_pb2.Request()
    
    response = stub.getTheme(request)
    if response:
        logging.info(f"get the theme list: {response}")
    else:
        logging.info(f"Failed")

def createTheme(stub,theme):
    request = pubsub_pb2.theme(theme_index=theme)
    response = stub.createTheme(request)
    
    if response:
        logging.info(f"create theme {theme} successfully")
    

def publish(stub,theme,text):
    pub = pubsub_pb2.pub(theme_index=pubsub_pb2.theme(theme_index=theme),text=text)
    response = stub.publish(pub)
    if response:
        logging.info(f"publish to {theme} successfully")

def run():
    with grpc.insecure_channel("localhost:50052") as channel:
        stub = pubsub_pb2_grpc.pubsubStub(channel)
        createTheme(stub,1)
        time.sleep(5)
        publish(stub,1,"hello")
        subscribe(stub,1)
        
run()