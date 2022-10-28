#!/usr/bin/env bash
# exit on error
set -o errexit

wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -x google-chrome-stable_current_amd64.deb ./
apt-get install -f
pip install -r requirements.txt	

