#!/bin/bash
# Script that hack the nasa
curl -sX PUT -L -d "user_id=98" -H "origin:HolbertonSchool" 0.0.0.0:5000/catch_me
