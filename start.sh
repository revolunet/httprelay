#!/bin/bash

DIR=$(dirname $0)
cd $DIR

screen -AdmS server -t home
screen -S server -X screen -t init sh -c 'python server.py ; exec bash'