#!/bin/bash -ex
mongod --bind_ip_all &
sleep 5
python3 ./run.py
