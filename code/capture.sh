#!/bin/sh

# Put interface to monitor mode
sudo airmon-ng check kill
sudo airmon-ng start $1

# Capture packets on channels
sudo iwconfig channel 1
tshark -i $1 -I -Y dns -a duration:300

sudo iwconfig channel 2
tshark -i $1 -I -Y dns -a duration:300
