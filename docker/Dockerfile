FROM ubuntu:22.04

RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl git htop man unzip vim wget && \
  apt-get install -y python3 && \
  apt-get install -y python3-pip && \
  apt-get install -y python3-dev && \
  apt-get install -y libpcap-dev && \
  apt-get install -y net-tools && \
  apt-get install -y dnsutils && \
  apt-get install -y inetutils-ping && \
  apt-get install -y iproute2 && \
  pip3 install scapy && \
  pip3 install sphinx sphinx_rtd_theme && \
  rm -rf /var/lib/apt/lists/*

ENV HOME /root

WORKDIR /root

COPY README.md README.md

CMD ["sleep", "infinity"]