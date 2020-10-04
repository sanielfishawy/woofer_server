import requests
import urllib3
from .command_interpreter import Command
import logging

def post_command(command:Command):
    try:
        requests.post('http://localhost:80' + command.path, json=command.payload)
    except:
        logging.error('Connection error. Server probably not running.')
