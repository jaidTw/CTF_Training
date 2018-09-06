FROM ubuntu:16.04
MAINTAINER JaidTw
RUN apt update
RUN apt install -y libc6 libncurses5 libstdc++6
RUN apt install -y socat sudo
RUN useradd -U -m simplerop
COPY ./simplerop_revenge /home/simplerop/simplerop_revenge
COPY ./simplerop_revenge.c /home/simplerop/simplerop_revenge.c
COPY ./flag /home/simplerop/flag
RUN chown root:simplerop /home/simplerop/*
RUN chown root:root /home/simplerop
RUN chmod 750 /home/simplerop/simplerop_revenge && chmod 740 /home/simplerop/flag /home/simplerop/simplerop_revenge.c

CMD sudo -u simplerop socat tcp-l:8000,fork exec:/home/simplerop/simplerop_revenge
EXPOSE 8000
