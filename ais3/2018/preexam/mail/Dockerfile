FROM ubuntu:16.04
MAINTAINER JaidTw
RUN apt update
RUN apt install -y libc6 libncurses5 libstdc++6
RUN apt install -y socat sudo
RUN useradd -U -m mail_
COPY ./mail /home/mail_/mail
COPY ./flag.txt /home/mail_/flag.txt
RUN chown root:mail_ /home/mail_/*
RUN chown root:root /home/mail_
RUN chmod 750 /home/mail_/mail && chmod 740 /home/mail_/flag.txt

CMD cd /home/mail_
CMD cd /home/mail_; sudo -u mail_ socat tcp-l:5572,fork exec:/home/mail_/mail
EXPOSE 5572
