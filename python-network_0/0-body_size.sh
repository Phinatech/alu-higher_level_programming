#!/bin/bash
# Getting a url via cURl and outputing the content length
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f 2
