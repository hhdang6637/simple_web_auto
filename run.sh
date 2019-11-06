#!/bin/bash

sudo docker run \
--rm \
-it   --name=firefox   -p 5900:5900    --shm-size 1g test_selenium_fb

