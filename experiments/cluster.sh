#!/bin/bash

set -euo pipefail

if ! minikube status | grep 'host: Running' > /dev/null; then
    echo "minikube does not seem to be running"
    # 4 CPU cores, 10 GiB RAM, and 32 GiB disk for Kubernetes 1.20.2
    minikube start --cpus 4 --memory 10240 --disk-size 32768 --driver virtualbox --kubernetes-version='v1.20.2'
fi