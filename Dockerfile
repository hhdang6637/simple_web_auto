FROM ubuntu:16.04

RUN sed -i 's/archive/vn\.archive/g' /etc/apt/sources.list
RUN apt-get update
RUN apt install python3 python3-pip firefox xvfb bash -y
RUN pip3 install selenium

COPY selenium_fb.py /root

COPY geckodriver-v0.24.0-linux64.tar.gz /opt
RUN tar -xvf /opt/geckodriver-v0.24.0-linux64.tar.gz -C /opt

ENV PATH=/opt:$PATH
ENV DISPLAY=:1

ENTRYPOINT Xvfb :1 >/tmp/xvfb.log 2>&1 & ; /bin/bash