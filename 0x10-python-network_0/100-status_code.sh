#!/bin/bash
# Script that only shows the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
