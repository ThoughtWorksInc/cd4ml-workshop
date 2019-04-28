FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev git vim nano \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --no-cache-dir --upgrade pip

RUN mkdir -p /app/continuous-intelligence \
  && git clone https://github.com/ThoughtWorksInc/continuous-intelligence-workshop.git /app/continuous-intelligence \
  && mkdir /app/continuous-intelligence/data \
  && cd /app/continuous-intelligence \
  && pip3 install --no-cache-dir -r requirements.txt

COPY data /app/continuous-intelligence/data

RUN rm /app/continuous-intelligence/data/splitter/*.csv

CMD ["/app/continuous-intelligence/start.sh"]
