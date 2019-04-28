#!/usr/bin/env bash
set -xe

IMAGE_VERSION=${GO_PIPELINE_LABEL:-latest}
PROJECT_ID=${GCLOUD_PROJECT_ID:-continuous-intelligence}
TENANT_NAMESPACE=${TENANT:-admin}
FLUENTD_HOST=${FLUENTD_HOST:-""}
FLUENTD_PORT=${FLUENTD_PORT:-""}
echo "Deploying image version: $IMAGE_VERSION"

cat kubernetes/web.yml \
  | sed "s/\\\$tenant\\\$/$TENANT_NAMESPACE/" \
  | sed "s/\\\$fluentd_host\\\$/$FLUENTD_HOST/" \
  | sed "s/\\\$fluentd_port\\\$/$FLUENTD_PORT/" \
  | sed "s/\(image: \).*$/\1eu.gcr.io\/$PROJECT_ID\/ci-workshop-app:$TENANT_NAMESPACE.$IMAGE_VERSION/" \
  | kubectl apply -f -

echo "Access your application at: http://$TENANT_NAMESPACE.app.cd4ml.net"
