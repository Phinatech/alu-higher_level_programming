#!/bin/bash
# Make post request via cURL
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
