FROM ubuntu:14.04
MAINTAINER JaidTw
RUN apt update
RUN apt install -y libc6 libncurses5 libstdc++6
RUN apt install -y socat sudo
RUN useradd -U -m magic
COPY ./Magic_World /home/magic/Magic_World
COPY ./flag.txt /home/magic/flag.txt
RUN chown root:magic /home/magic/*
RUN chown root:root /home/magic
RUN chmod 750 /home/magic/Magic_World && chmod 740 /home/magic/flag.txt

CMD cd /home/magic; sudo -u magic socat tcp-l:5575,fork exec:/home/magic/Magic_World
EXPOSE 5575
