#!/bin/bash

set -euo pipefail

duration=60

if [ ! -d results ]; then
    mkdir -p results
fi

# TODO only run if git repo is up to date

kubectl delete -f ../release/kubernetes-manifests-full-page.yaml &> /dev/null || true
kubectl delete -f ../release/kubernetes-manifests-fine-grained.yaml &> /dev/null || true
kubectl delete -f ../release/loadgenerator.yaml &> /dev/null || true

for experiment in full-page fine-grained; do
    if grep 'end' results/${experiment}-times.txt; then
        echo "Seems that ${experiment} is already finished, skipping..."
        continue
    fi

    echo "Will run experiment for ${experiment}"

    echo "Deploying Online Boutique"
    kubectl apply -f ../release/kubernetes-manifests-${experiment}.yaml

    echo "Sleeping a minute while containers creating..."
    sleep 60

    while kubectl get pods --no-headers | grep -v 'Running'; do
        echo 'Not everything is Running yet'
        sleep 2
    done

    start=$(date +"%s")
    echo "Starting experiment at ${start} in UTC epoch time, that is, $(date) for humans"
    echo "start ${start}" > results/${experiment}-times.txt

    echo "Sleeping a minute to not miss load ramp-up period..."
    sleep 60

    echo "Deploying load generator"
    kubectl apply -f ../release/loadgenerator.yaml

    echo "Sleeping for ${duration} seconds"
    sleep ${duration}

    echo "Actually done, saving load generator logs before removing it..."
    kubectl logs $(kubectl get pods | grep loadgenerator | cut -d ' ' -f 1) > results/${experiment}-loadgenerator.log

    echo "Storing Pod status"
    kubectl get pods > results/${experiment}-podstatus.log

    echo "Removing load generator"
    kubectl delete -f ../release/loadgenerator.yaml

    echo "Sleeping for an additional minute to not miss ramp-down period..."
    sleep 60

    end=$(date +"%s")
    echo "Experiment ended at ${end} in UTC epoch time"
    echo "end ${end}" >> results/${experiment}-times.txt

    echo "Storing cache and memory CSV files for the components with caching enabled"
    if [ ${experiment} == "full-page" ]; then
        kubectl exec $(kubectl get pods | grep frontend | cut -d ' ' -f 1) -c caching-http-reverse-proxy cat data.csv > results/${experiment}-frontend-caching.csv
        kubectl exec $(kubectl get pods | grep frontend | cut -d ' ' -f 1) -c caching-http-reverse-proxy cat memory-data.csv > results/${experiment}-frontend-memory.csv
    elif [ ${experiment} == "fine-grained" ]; then
        for component in frontend recommendation checkout; do
            kubectl exec $(kubectl get pods | grep ${component} | cut -d ' ' -f 1) -c caching-grpc-reverse-proxy cat data.csv > results/${experiment}-${component}-caching.csv
            kubectl exec $(kubectl get pods | grep ${component} | cut -d ' ' -f 1) -c caching-grpc-reverse-proxy cat memory-data.csv > results/${experiment}-${component}-memory.csv
        done
    fi

    echo "Sleeping for 20 seconds"
    sleep 20

    echo "Removing Online Boutique"
    kubectl delete -f ../release/kubernetes-manifests-${experiment}.yaml

    echo "Sleeping 2 minutes before moving on..."
    sleep 120
done