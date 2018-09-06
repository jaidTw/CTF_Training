FROM ubuntu:16.04
MAINTAINER JaidTw
RUN apt update
RUN apt install -y libc6 libncurses5 libstdc++6
RUN apt install -y socat sudo
RUN useradd -U -m r3t2lib
COPY ./r3t2lib /home/r3t2lib/r3t2lib
COPY ./r3t2lib.c /home/r3t2lib/r3t2lib.c
COPY ./makefile /home/r3t2lib/makefile
COPY ./flag /home/r3t2lib/flag
RUN chown root:r3t2lib /home/r3t2lib/*
RUN chown root:root /home/r3t2lib
RUN chmod 750 /home/r3t2lib/r3t2lib && chmod 740 /home/r3t2lib/r3t2lib.c /home/r3t2lib/flag

CMD sudo -u r3t2lib socat tcp-l:8000,fork exec:/home/r3t2lib/r3t2lib
EXPOSE 8000
