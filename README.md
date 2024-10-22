# COVERTOVERT
Open source implementation of "network" covert channels.

## Installation

Install docker (and optionally compose V2 plugin - not the docker-compose!) and VSCode on your sytstem. Run the docker containers as non-root users.

To start sender and receiver containers:
```
docker compose up -d
```

To stop sender and receiver containers:
```
docker compose down
```

Note that, if you orchestrate your containers using docker compose, the containers will have hostnames ("sender" and "receiver") and DNS will be able to resolve them...

In one terminal, attach to the sender container
```
docker exec -it sender bash
```
In another terminal, attach to the receiver container
```
docker exec -it receiver bash
```

and you will be in your Ubuntu 22.04 Docker instance (python3.10.12 and scapy installed). After running the Ubuntu Docker, you can type "ip addr" or "ifconfig" to see your network configuration (work on eth0).

Docker extension of VSCode will be of great benefit to you.

Note that if you develop code in these Docker instances and you stop the machine, your code will be lost. That is why it is recommended to use Github to store your code and clone in the machine, and push your code to Github before shutting the Docker instances down. The other option is to work in the /app folder in the sender and receiver Docker instances which are mounted to the "code" directory of your own machine.

**IMPORTANT** Note that the "code" folder on your local machine are mounted to the "/app" folder (be careful it is in the root folder) in the sender and receiver Docker instances (read/write mode). You can use these folders (they are the same in fact) to develop your code. Other than the /app folder, this tool does not guarantee any persistent storage: if you exit the Docker instance, all data will be lost.

You can develop your code on your local folders ("code/sender" and "code/receiver") on your own host machine, they will be immediately synchronized with the "/app" folder on containers. The volumes are created in read-write mode, so changes can be made both on the host or on the containers. You can run your code on the containers.

Additionally, the local "examples" folder is mapped to the "/examples" folder in the containers. In that folder, there is a covert timing channel example including sender, receiver and base classes. In the second phase, you will implement a similar system, so it is recommended to look at the example for now.
