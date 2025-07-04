#!/bin/bash

# Путь к датчику температуры (замени на свой путь hwmon)
TEMP_PATH="/sys/class/hwmon/hwmon5/temp1_input"

if [ -f "$TEMP_PATH" ]; then
  # Читаем температуру и переводим в градусы Цельсия (делим на 1000)
  temp=$(cat "$TEMP_PATH")
  temp_c=$((temp / 1000))
  echo "|  : ${temp_c} "
else
  echo "CPU: N/A"
fi
