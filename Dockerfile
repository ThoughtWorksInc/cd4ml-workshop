FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev wget unzip \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN mkdir -p /app && wget -O /app/data-lab.zip https://github.com/ThoughtWorksInc/continuous-intelligence-workshop/archive/master.zip
RUN cd /app && unzip ./data-lab.zip && rm data-lab.zip
RUN cd /app/continuous-intelligence-workshop-master && pip install -r requirements.txt
RUN cd /app/continuous-intelligence-workshop-master && sh run_decisiontree_pipeline.sh
RUN chmod +x /app/continuous-intelligence-workshop-master/start.sh

CMD ["/app/continuous-intelligence-workshop-master/start.sh"]
