import docker


def containers_clean():
    client = docker.from_env()
    containers = client.containers.list()
    for c in containers:
        c.kill()


if __name__ == '__main__':
    containers_clean()
