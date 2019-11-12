#!/bin/bash

docker run --rm -it --name=selenium -p 5900:5900 -v $PWD:/root/$(basename $PWD) test_selenium_fb