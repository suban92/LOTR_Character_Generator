# install pip3, pytest and flask-testing and test service-1
sudo update -y
sudo upgrade -y
sudo apt install -y python3-pip
sudo pip3 install --upgrade pip



cd ./service-1
pip3 install -r requirements.txt
python3 -m pytest --cov application > test_results-1.txt
mv test_results-1.txt ..
cd ..



# test servcie-2
cd ./service-2
python3 -m pytest --cov application > test_results-2.txt
mv test_results-2.txt ..
cd ..



# test servcie-3
cd ./service-3
python3 -m pytest --cov application > test_results-3.txt
mv test_results-3.txt ..
cd ..



# test servcie-4
cd ./service-4
python3 -m pytest --cov application > test_results-4.txt
mv test_results-4.txt ..
cd ..



# test servcie-5
cd ./service-5
python3 -m pytest --cov application > test_results-5.txt
mv test_results-5.txt ..
cd ..

echo test_results-1 > test_results_total 
echo test_results-2 >> test_results_total
echo test_results-3 >> test_results_total
echo test_results-4 >> test_results_total
echo test_results-5 >> test_results_total
cat test_results_total