#!/bin/bash

git.sh -i /var/www/.ssh/srv01 pull
python freifunkAPIupdater.py

git add freifunk.net.json
git commit -a -m "updated number of nodes"
git.sh -i /var/www/.ssh/srv01 push


