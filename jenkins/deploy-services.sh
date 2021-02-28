# ssh to the swarm manager to execute commands
ssh 10.154.0.12

sudo rm -rf LOTR_Character_Generator

# clone the project repository  
git clone https://github.com/Dwalker0357/LOTR_Character_Generator


git checkout jenkins 


# cd into the project repositroy
cd LOTR_Character_Generator


# remove any previous services 
sudo docker stack rm lotr


#log into dockerhub account
sudo docker login


# Deploy our services in swarm as a stack with the name lotr
sudo docker stack deploy --compose-file docker-compose.yaml lotr
