#!/bin/bash
#BAsh script that DEL request to the server passed as the first arg and displays the body of the response.
curl -s -X DELETE "${1}"

