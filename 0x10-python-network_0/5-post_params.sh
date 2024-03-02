#!/bin/bash
# sends a post request to a server with given data and displays the response body
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "${1}"

