#!/bin/sh

DIR="$HOME/Pictures/Screenshots"
mkdir -p "$DIR"

FILE="$DIR/screenshot_$(date +%Y-%m-%d_%H-%M-%S).png"

slurp | grim -g - "$FILE" && notify-send "Screenshot Save" "$FILE"
