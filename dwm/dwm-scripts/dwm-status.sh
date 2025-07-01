#!/bin/bash

while true; do
  date '+ %a %d %b  %R ' >/tmp/CurlTime.tmp
  sleep 60s
done &

while true; do
  LOCALTIME=$(echo $(</tmp/CurlTime.tmp))

  MEM=$(echo $(free -h --kilo | awk '/^Mem:/ {print $3 "/" $2}'))
  CPU=$(echo "CPU: "$((100 - $(vmstat 1 2 | tail -1 | awk '{print $15}')))"%")

  xsetroot -name "[ RAM: $MEM ][ $CPU ][ $LOCALTIME ]"
  sleep 5s
done
