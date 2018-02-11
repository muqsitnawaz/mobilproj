#!/bin/sh

# Put interface to monitor mode
sudo airmon-ng check kill

sudo ifconfig $1 down
sudo iwconfig $1 mode monitor
sudo ifconfig $1 up

# Capture packets on channels
for i in `seq 1 11`; do
  sudo iwconfig $1 channel $i
  ts=`date "+%F-%T"`
  ts+="-channel"
  ts+=$i
  ts+=".pcapng"
  tshark -i $1 -I -a duration:10 -w $ts
  echo "Done capturing on channel"
done
