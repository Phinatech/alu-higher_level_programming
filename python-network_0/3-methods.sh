#!/bin/bash
# display acceptable methods from url via cURL
curl -sI "$1" -X OPTIONS | grep "Allow" | cut -c 8-
