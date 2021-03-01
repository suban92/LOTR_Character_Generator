#!/bin/bash
ssh 35.197.224.58 << EOF 

sudo rm LOTR_Character_Generator -rf

git clone https://github.com/Dwalker0357/LOTR_Character_Generator

cd LOTR_Character_Generator

sudo docker-compose down --rmi local

sudo docker-compose up -d
EOF