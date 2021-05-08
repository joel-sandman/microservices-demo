#!/bin/bash

set -euo pipefail

duration=600

if [ ! -d results ]; then
    mkdir -p results
fi

kubectl delete -f ../release/kubernetes-manifests-full-page.yaml &> /dev/null || true
kubectl delete -f ../release/kubernetes-manifests-fine-grained.yaml &> /dev/null || true
kubectl delete -f ../release/loadgenerator.yaml &> /dev/null || true

for repetition in {1..5}; do
    for methodology in full-page fine-grained; do
        for ttl in 0 0.1 0.2 0.5 1 2 5 10 20; do
            if grep 'end' results/${repetition}-${methodology}-${ttl}-times.txt; then
                echo "Seems that ${repetition}-${methodology}-${ttl} is already finished, skipping..."
                continue
            fi

            echo "Will run experiment for ${repetition}-${methodology}-${ttl}"

            echo "Deploying Online Boutique"
            kubectl apply -f ../release/kubernetes-manifests-${methodology}-${ttl}.yaml

            echo "Sleeping 30 seconds while containers creating..."
            sleep 30

            while kubectl get pods --no-headers | grep -v 'Running'; do
                echo 'Not everything is Running yet'
                sleep 2
            done

            start=$(date +"%s")
            echo "Starting experiment at ${start} in UTC epoch time, that is, $(date) for humans"
            echo "start ${start}" > results/${repetition}-${methodology}-${ttl}-times.txt

            echo "Sleeping a minute to not miss load ramp-up period..."
            sleep 60

            echo "Deploying load generator"
            kubectl apply -f ../release/loadgenerator.yaml

            echo "Sleeping for ${duration} seconds"
            sleep ${duration}

            echo "Actually done, saving load generator logs before removing it..."
            kubectl logs $(kubectl get pods | grep loadgenerator | cut -d ' ' -f 1) > results/${repetition}-${methodology}-${ttl}-loadgenerator.log

            echo "Storing Pod status"
            kubectl get pods > results/${repetition}-${methodology}-${ttl}-podstatus.log

            echo "Removing load generator"
            kubectl delete -f ../release/loadgenerator.yaml

            echo "Sleeping for an additional minute to not miss ramp-down period..."
            sleep 60

            end=$(date +"%s")
            echo "Experiment ended at ${end} in UTC epoch time"
            echo "end ${end}" >> results/${repetition}-${methodology}-${ttl}-times.txt

            echo "Storing cache and memory CSV files for the components with caching enabled"
            if [ ${methodology} == "full-page" ]; then
                kubectl exec $(kubectl get pods | grep frontend | cut -d ' ' -f 1) -c caching-http-reverse-proxy cat data.csv > results/${repetition}-${methodology}-${ttl}-frontend-caching.csv
                kubectl exec $(kubectl get pods | grep frontend | cut -d ' ' -f 1) -c caching-http-reverse-proxy cat memory-data.csv > results/${repetition}-${methodology}-${ttl}-frontend-memory.csv
            elif [ ${methodology} == "fine-grained" ]; then
                for component in frontend recommendation checkout; do
                    kubectl exec $(kubectl get pods | grep ${component} | cut -d ' ' -f 1) -c caching-grpc-reverse-proxy cat data.csv > results/${repetition}-${methodology}-${ttl}-${component}-caching.csv
                    kubectl exec $(kubectl get pods | grep ${component} | cut -d ' ' -f 1) -c caching-grpc-reverse-proxy cat memory-data.csv > results/${repetition}-${methodology}-${ttl}-${component}-memory.csv
                done
            fi

            echo "Sleeping for 20 seconds"
            sleep 20

            echo "Removing Online Boutique"
            kubectl delete -f ../release/kubernetes-manifests-${methodology}-${ttl}.yaml

            echo "Sleeping 2 minutes before moving on..."
            sleep 120
        done
    done
done