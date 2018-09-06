FROM ubuntu:14.04
MAINTAINER JaidTw
RUN apt update
RUN apt install -y libc6 libncurses5 libstdc++6
RUN apt install -y socat sudo
RUN useradd -U -m justfmt
COPY ./justfmt /home/justfmt/justfmt
COPY ./flag.txt /home/justfmt/flag.txt
RUN chown root:justfmt /home/justfmt/*
RUN chown root:root /home/justfmt
RUN chmod 750 /home/justfmt/justfmt && chmod 740 /home/justfmt/flag.txt

CMD cd /home/justfmt; sudo -u justfmt socat tcp-l:8000,fork exec:/home/justfmt/justfmt
EXPOSE 8000
