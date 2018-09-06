FROM ubuntu:16.04
MAINTAINER JaidTw
RUN apt update
RUN apt install -y libc6 libncurses5 libstdc++6
RUN apt install -y socat sudo
RUN useradd -U -m callme
COPY ./callme /home/callme/callme
COPY ./flag /home/callme/flag
RUN chown root:callme /home/callme/*
RUN chown root:root /home/callme
RUN chmod 750 /home/callme/callme && chmod 740 /home/callme/flag

CMD sudo -u callme socat tcp-l:8000,fork exec:/home/callme/callme
EXPOSE 8000
