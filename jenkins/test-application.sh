# install pip3, pytest and flask-testing and test service-1
sudo update -y
sudo upgrade -y
sudo apt install -y python3-pip
sudo pip3 install --upgrade pip



cd ./service-1
pip3 install -r requirements.txt
python3 -m pytest --cov application
cd ..



# test servcie-2
cd ./service-2
python3 -m pytest --cov application
cd ..



# test servcie-3
cd ./service-3
python3 -m pytest --cov application
cd ..



# test servcie-4
cd ./service-4
python3 -m pytest --cov application
cd ..



# test servcie-5
cd ./service-5
python3 -m pytest --cov application
cd ..