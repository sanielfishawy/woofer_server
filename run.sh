#!/bin/bash

SERVER_DIR=/home/pi/dev/woofer_server
cd $SERVER_DIR

source ./venv/bin/activate
export WOOFER_OUTPUT_DEVICE=headphones
export WOOFER_SPEAKER_TYPE=woofer

/home/pi/dev/woofer_server/venv/bin/python server.py

