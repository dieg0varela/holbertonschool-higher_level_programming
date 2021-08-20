#!/bin/bash
# Script that sends a json using curl
curl -sH "Content-Type: application/json" --data @"$2" "$1"
