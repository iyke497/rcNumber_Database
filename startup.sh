#!/bin/bash

sudo apt update
sudo apt upgrade

sudo apt install python3.10-venv
sudo apt install git 

git config --global user.name "iyke497"
git config --global user.email "iyke497@gmail.com"

git clone https://github.com/iyke497/rcNumber_Database.git 
cd ./rcNumber_Database
mkdir csv_files

sudo chmod +x get_co_rc.sh 
sudo chmod +x rc_num_db.py

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

#Input the parameters for the start and stop in place here
./get_co_rc.sh $1 $2