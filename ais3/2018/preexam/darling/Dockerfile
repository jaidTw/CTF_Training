FROM ubuntu:16.04
MAINTAINER JaidTw
RUN apt update
RUN apt install -y libc6 libncurses5 libstdc++6
RUN apt install -y socat sudo
RUN useradd -U -m darling
COPY ./darling /home/darling/darling
COPY ./flag.txt /home/darling/flag.txt
RUN chown root:darling /home/darling/*
RUN chown root:root /home/darling
RUN chmod 750 /home/darling/darling && chmod 740 /home/darling/flag.txt

CMD cd /home/darling; sudo -u darling socat tcp-l:5573,fork exec:/home/darling/darling
EXPOSE 5573
