FROM ubuntu:bionic

RUN apt update
RUN apt -y install python3-pip
RUN apt -y install telnet
RUN apt-get update -y
RUN apt-get install -y python3-dev
RUN apt-get install -y libpq-dev build-essential
RUN DEBIAN_FRONTEND="noninteractive" TZ=America/New_York apt-get -y install tzdata
RUN apt-get install -y postgresql postgresql-contrib

WORKDIR /usr/src/crawler

EXPOSE 6023

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
CMD ["./start.sh"]