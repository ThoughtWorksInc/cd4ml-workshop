#!/usr/bin/env bash
set -xe

TENANT_NAMESPACE=${TENANT:-admin}
cat kubernetes/web.yml | sed "s/\\\$tenant\\\$/$TENANT_NAMESPACE/" | kubectl delete -f -
