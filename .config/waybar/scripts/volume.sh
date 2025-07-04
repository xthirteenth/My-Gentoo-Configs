#!/bin/bash

# Получаем текущую громкость через pactl
volume=$(pactl get-sink-volume @DEFAULT_SINK@ | awk '{print $5}' | tr -d '%')

# Проверка, отключён ли звук
mute=$(pactl get-sink-mute @DEFAULT_SINK@ | awk '{print $2}')

if [ "$mute" = "yes" ]; then
    echo "| 󰖁"
else
    echo "| 󰕾 : ${volume}%"
fi