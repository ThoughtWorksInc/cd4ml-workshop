FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev wget unzip \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN mkdir -p /app/continuous-intelligence
ADD requirements.txt /app/continuous-intelligence/requirements.txt
ADD run_decisiontree_pipeline.sh /app/continuous-intelligence/run_decisiontree_pipeline.sh
ADD src /app/continuous-intelligence/src
ADD start.sh /app/continuous-intelligence/start.sh

RUN cd /app/continuous-intelligence && pip install -r requirements.txt
RUN cd /app/continuous-intelligence && sh run_decisiontree_pipeline.sh
RUN chmod +x /app/continuous-intelligence/start.sh

CMD ["/app/continuous-intelligence/start.sh"]
