#!/bin/bash

Xvfb :1 -screen 0 800x600x16 > /tmp/Xvfb_$$.log 2>&1 &
x11vnc -shared -forever -display :1 > /tmp/x11vnc_$$.log 2>&1 &
