# open folder
cd [FOLDER_NAME]

# create network
docker network create --driver bridge [NETWORK_NAME] 

# build containers
sudo docker-compose build

# run containers
sudo docker-compose up

# in a new terminal, execute bash in container (repeat for each peer)
docker exec -it [CONTAINER_NAME] bash

# run peers (repeat for each peer)
python3 peer[#].py

# when prompted, enter valid port number for running peer
ex: 5001

# when prompted, enter peer number you want to communicate with
ex: 2

# when prompted, enter peer's port number to communicate with them
ex: 5002

# to exit messaging enter:
--exit


