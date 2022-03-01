import docker

client = docker.from_env()
containers = client.containers.list()
for c in containers:
    c.kill()