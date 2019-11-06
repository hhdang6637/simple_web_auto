#!/bin/bash

Xvfb :1 -screen 0 1600x1200x24+32 > /tmp/Xvfb.log 2>&1 &
x11vnc -display :1 &
