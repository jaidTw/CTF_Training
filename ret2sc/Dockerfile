FROM ubuntu:16.04
MAINTAINER JaidTw
RUN apt update
RUN apt install -y libc6 libncurses5 libstdc++6
RUN apt install -y socat sudo
RUN useradd -U -m ret2sc
COPY ./ret2sc /home/ret2sc/ret2sc
COPY ./ret2sc.c /home/ret2sc/ret2sc.c
COPY ./flag /home/ret2sc/flag
RUN chown root:ret2sc /home/ret2sc/*
RUN chown root:root /home/ret2sc
RUN chmod 750 /home/ret2sc/ret2sc && chmod 740 /home/ret2sc/flag

CMD sudo -u ret2sc socat tcp-l:8000,fork exec:/home/ret2sc/ret2sc
EXPOSE 8000
