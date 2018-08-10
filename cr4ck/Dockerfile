FROM ubuntu:16.04
MAINTAINER JaidTw
RUN apt update
RUN apt install -y libc6 libncurses5 libstdc++6
RUN apt install -y socat sudo
RUN useradd -U -m cr4ck
COPY ./cr4ck /home/cr4ck/cr4ck
COPY ./cr4ck.c /home/cr4ck/cr4ck.c
COPY ./flag /home/cr4ck/flag
RUN chown root:cr4ck /home/cr4ck/*
RUN chown root:root /home/cr4ck
RUN chmod 750 /home/cr4ck/cr4ck && chmod 740 /home/cr4ck/flag

CMD sudo -u cr4ck socat tcp-l:5576,fork exec:/home/cr4ck/cr4ck
EXPOSE 5576
