#!/usr/bin/env bash
# exit on error
set -o errexit



STORAGE_DIR=/opt/render/project/.render
echo "Pasta base"
echo $PWD
echo "----------"
echo "...Downloading Chrome"
mkdir -p $STORAGE_DIR/chrome
cd $STORAGE_DIR/chrome
wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
rm ./google-chrome-stable_current_amd64.deb
echo "Pasta base"
echo $PWD
echo "----------"


cd /opt/render/project/src/web-search # Make sure we return to where we were
echo "Pasta Final"
echo $PWD
echo $(ls)
echo "----------"
pip install -r /opt/render/project/src/web-search/requirements.txt	






