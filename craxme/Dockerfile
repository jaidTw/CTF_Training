FROM ubuntu:16.04
MAINTAINER JaidTw
RUN apt update
RUN apt install -y libc6 libncurses5 libstdc++6
RUN apt install -y socat sudo
RUN useradd -U -m craxme
COPY ./craxme /home/craxme/craxme
COPY ./craxme.c /home/craxme/craxme.c
COPY ./flag /home/craxme/flag
COPY ./craxflag /home/craxme/craxflag
COPY ./realflag /home/craxme/realflag
RUN chown root:craxme /home/craxme/*
RUN chown root:root /home/craxme
RUN chmod 750 /home/craxme/craxme && chmod 740 /home/craxme/flag /home/craxme/craxflag /home/craxme/realflag

CMD sudo -u craxme socat tcp-l:5577,fork exec:/home/craxme/craxme
EXPOSE 5577
