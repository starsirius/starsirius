#!/bin/bash

echo "\n########################"
echo "Installing virtualenv..."
echo "########################"
sudo pip install virtualenv

echo "\n############################"
echo "Creating virtualenv..."
echo "############################"
virtualenv starenv

echo "\n########################"
echo "Activating virtualenv..."
echo "########################"
source starenv/bin/activate
if test $? != 0; then
   echo "> Can't activate virtualenv. Abort."
   exit 1
fi

echo "\n####################################"
echo "Installing required site-packages..."
echo "####################################"
pip install -r requirements.txt

echo "\n##############################"
echo "Installing applcation..."
echo "##############################"
cd src/star && python setup.py develop

