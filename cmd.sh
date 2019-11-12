#!/bin/bash

Xvfb :1 -screen 0 800x600x16 > /tmp/Xvfb.log 2>&1 &
x11vnc -shared -forever -display :1 &
