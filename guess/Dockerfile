FROM ubuntu:16.04
MAINTAINER JaidTw
RUN apt update
RUN apt install -y libc6 libncurses5 libstdc++6
RUN apt install -y socat sudo
RUN useradd -U -m guess
COPY ./guess /home/guess/guess
RUN chown root:guess /home/guess/*
RUN chown root:root /home/guess
RUN chmod 750 /home/guess/guess

CMD sudo -u guess socat tcp-l:5568,fork exec:/home/guess/guess
EXPOSE 5568
