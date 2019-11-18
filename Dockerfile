FROM ubuntu:16.04

RUN apt-get update
RUN apt install python3 python3-pip firefox xvfb bash x11vnc browser-plugin-freshplayer-pepperflash -y
RUN pip3 install selenium

COPY geckodriver-v0.26.0-linux64.tar.gz /opt
RUN tar -xvf /opt/geckodriver-v0.26.0-linux64.tar.gz -C /opt

ENV PATH=/opt:$PATH
ENV DISPLAY=:1

RUN apt install -y htop psmisc

RUN useradd jenkins

RUN apt-get install -y sudo
RUN usermod -aG sudo jenkins
RUN echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN echo "jenkins:jenkins" | chpasswd
RUN mkdir /home/jenkins

RUN chown jenkins:jenkins -R /home/jenkins
USER jenkins
WORKDIR /home/jenkins
COPY cmd.sh /home/jenkins

ENTRYPOINT /home/jenkins/cmd.sh; /bin/bash
