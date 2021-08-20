#!/bin/bash
# Script that print the accepted methods of the server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
