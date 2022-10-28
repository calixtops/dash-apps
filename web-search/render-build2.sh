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

cd /opt/render/project/src/web-search # Make sure we return to where we were

/opt/render/project/src/.venv/bin/python -m pip install -r /opt/render/project/src/web-search/requirements.txt	
