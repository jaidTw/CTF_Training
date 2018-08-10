FROM ubuntu:16.04
MAINTAINER JaidTw
RUN apt update
RUN apt install -y libc6 libncurses5 libstdc++6
RUN apt install -y socat sudo
RUN useradd -U -m calc
COPY ./calc /home/calc/calc
COPY ./flag.txt /home/calc/flag.txt
RUN chown root:calc /home/calc/*
RUN chown root:root /home/calc
RUN chmod 750 /home/calc/calc && chmod 740 /home/calc/flag.txt

CMD cd /home/calc; sudo -u calc socat tcp-l:5571,fork exec:/home/calc/calc
EXPOSE 5571
