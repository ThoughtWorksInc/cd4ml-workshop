#!/usr/bin/env bash
set -xe

IMAGE_VERSION=${GO_PIPELINE_LABEL:-latest}
PROJECT_ID=${GCLOUD_PROJECT_ID:-continuous-intelligence}
echo "Deploying image version: $IMAGE_VERSION"

cat kubernetes/web.yml | sed "s/\(image: \).*$/\1us.gcr.io\/$PROJECT_ID\/ci-workshop-app:$IMAGE_VERSION/" | kubectl apply -f - --namespace default
