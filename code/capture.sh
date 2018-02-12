#!/bin/sh

# Put interface to monitor mode
sudo airmon-ng check kill
sudo airmon-ng start $1

# Capture packets on channels
for i in `seq 1 11`; do
  sudo iwconfig wlp6s0mon channel $i
  ts=`date "+%F-%T"`
  ts+="-channel"
  ts+=$i
  ts+=".pcapng"
  tshark -i wlp6s0mon -I -a duration:120 -w $ts
  echo "Done capturing on channel"
done
