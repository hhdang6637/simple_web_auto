#!/bin/bash

docker run --rm -it --name=selenium -p 5900:5900 -v $PWD/selenium_fb.py:/root/selenium_fb.py test_selenium_fb