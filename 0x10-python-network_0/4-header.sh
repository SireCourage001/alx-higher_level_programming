#!/bin/bash
#Bash script takes a url as first argument, sends get request to the url with header variable 'X-School-User-Id' with value 98, displays the body of response
curl -sH "X-HolbertonSchool-User-Id: 98" "${1}"
