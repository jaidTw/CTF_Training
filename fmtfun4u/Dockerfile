FROM ubuntu:16.04
MAINTAINER JaidTw
RUN apt update
RUN apt install -y libc6 libncurses5 libstdc++6
RUN apt install -y socat sudo
RUN useradd -U -m fmtfun4u
COPY ./fmtfun4u /home/fmtfun4u/fmtfun4u
COPY ./fmtfun4u.c /home/fmtfun4u/fmtfun4u.c
COPY ./flag /home/fmtfun4u/flag
RUN chown root:fmtfun4u /home/fmtfun4u/*
RUN chown root:root /home/fmtfun4u
RUN chmod 750 /home/fmtfun4u/fmtfun4u && chmod 740 /home/fmtfun4u/flag

CMD sudo -u fmtfun4u socat tcp-l:8000,fork exec:/home/fmtfun4u/fmtfun4u
EXPOSE 8000
