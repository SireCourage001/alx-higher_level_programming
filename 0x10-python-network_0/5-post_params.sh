#!/bin/bash
# sends a post request to a server with given data and displays the response body
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"

