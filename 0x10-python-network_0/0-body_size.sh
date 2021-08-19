#!/bin/bash
# Script that print body size of response
curl -sI "$1" | grep "Content-Length" | cut -d " " -f 2
