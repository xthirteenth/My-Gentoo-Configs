#!/bin/bash

# Получаем текущую громкость через wpctl
volume_line=$(wpctl get-volume @DEFAULT_AUDIO_SINK@)
volume=$(echo "$volume_line" | awk '{print int($2 * 100)}')
mute=$(echo "$volume_line" | grep -q MUTED && echo "yes" || echo "no")

if [ "$mute" = "yes" ]; then
  echo "| 󰖁"
else
  echo "| 󰕾 : ${volume}%"
fi
