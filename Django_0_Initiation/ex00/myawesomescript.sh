#!/bin/sh

if [ $# -eq 1 ]; then
curl --silent "$1" | grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*"

else
echo "Wrong argument given need to pass a bitly adress."

fi
