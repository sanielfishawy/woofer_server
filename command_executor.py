import requests

def post_command(command):
    r = requests.post('http://localhost:80' + command['path'], data = {'key':'value'})
