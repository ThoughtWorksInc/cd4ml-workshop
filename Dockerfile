FROM eu.gcr.io/continuous-intelligence/gocd-agent-docker-dind-dvc:v19.9.0

USER root

RUN mkdir -p /app/continuous-intelligence/{src,data}

COPY start.sh /app/continuous-intelligence
COPY src /app/continuous-intelligence/src
COPY data/decision_tree /app/continuous-intelligence/data/decision_tree

RUN chmod +x /app/continuous-intelligence/start.sh

EXPOSE 5005

CMD ["/app/continuous-intelligence/start.sh"]
