# COVERTOVERT
Open source implementation of "network" covert channels.

## Installation

Install docker (and optionally compose V2 plugin - not the docker-compose!) and VSCode on your sytstem. Run the docker containers as non-root users.

To start server and client containers:
```
docker compose up -d
```

To stop server and client containers:
```
docker compose down
```

Note that, if you orchestrate your containers using docker compose, the containers will have hostnames ("client" and "server") and DNS will be able to resolve them...

In one terminal, attach to the server container
```
docker exec -it server bash
```
In another terminal, attach to the client container
```
docker exec -it client bash
```

The local "code" folder is mapped to the "/app" folder in containers and the local "examples" folder is mapped to the "/examples" folder in the container. You can develop your code on your local folders on your own host machine, they will be immediately synchronized with the "/app" folder on containers. The volumes are created in read-write mode, so changes can be made both on the host or on the containers. You can run your code on the containers...