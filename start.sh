#!/bin/sh
echo "\nDownloading...\n\n\n"
rm robot.py
wget -O - https://raw.githubusercontent.com/trzaszcs/robo-kura/master/robot.py | python
