#!/usr/bin/env bash
# exit on error
set -o errexit

apt install chromium-chromedriver
pip install -r requirements.txt	

