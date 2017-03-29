#!/bin/sh

cd `dirname "$0"`

FILES="requirements.txt server.py"

sync_rpi() {
  TARGET=$1
  DEST_PATH="/root/httprelay/"
  rsync -v $FILES $TARGET:$DEST_PATH
  #ssh $TARGET -t 'sudo pip install cherrypy'
}


# sync_ubuntu() {
#   TARGET=$1
#   DEST_PATH="/home/ju/simpleplayer"
#   rsync -v $FILES $TARGET:$DEST_PATH
#  # ssh $TARGET pip install cherrypy
#  # ssh $TARGET sudo reboot
# }

sync_rpi $1




