#!/usr/bin/env python3

import glob
import pandas as pd
from statistics import mean

def normalize_timestamps(df):
    df['timestamp'] = df['timestamp'] - df['timestamp'][0]
    return df

def get_network_traffic(methodology, service):
    requests_vs_ttl = []
    for ttl in [0, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20]:
        network_traffic_requests = []
        for source in glob.glob('results/?-' + methodology + '-' + str(ttl) + '-' + service + '-caching.csv'):
            df = pd.read_csv(source)
            number_of_requests = len(df)
            cached_network_traffic = df.loc[df['source'] == 'cache']
            number_of_cached_responses = len(cached_network_traffic)
            number_of_non_cached_requests = number_of_requests - number_of_cached_responses
            network_traffic_requests.append(number_of_non_cached_requests)
        requests_vs_ttl.append((ttl, mean(network_traffic_requests)))
    return requests_vs_ttl

def get_network_traffic_reduction_by_requests(methodology, service):
    network_traffic_reduction_by_requests = []
    for ttl in [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]:
        network_traffic_reduction = []
        for source in glob.glob('results/?-' + methodology + '-' + str(ttl) + '-' + service + '-caching.csv'):
            df = pd.read_csv(source)
            number_of_requests = len(df)
            cached_network_traffic = df.loc[df['source'] == 'cache']
            number_of_cached_responses = len(cached_network_traffic)
            network_traffic_reduction.append(number_of_cached_responses/number_of_requests)
        network_traffic_reduction_by_requests.append(mean(network_traffic_reduction))
    return network_traffic_reduction_by_requests

def get_network_traffic_reduction_by_size(methodology, service):
    network_traffic_reduction_by_size = []
    for ttl in [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]:
        network_traffic_reduction = []
        for source in glob.glob('results/?-' + methodology + '-' + str(ttl) + '-' + service + '-caching.csv'):
            df = pd.read_csv(source)
            total_size_of_all_network_traffic = df['size'].sum()
            cached_network_traffic = df.loc[df['source'] == 'cache']
            total_size_of_cached_network_traffic = cached_network_traffic['size'].sum()
            network_traffic_reduction.append(total_size_of_cached_network_traffic/total_size_of_all_network_traffic)
        network_traffic_reduction_by_size.append(mean(network_traffic_reduction))
    return network_traffic_reduction_by_size

def get_data_staleness_by_requests(methodology, service):
    data_staleness_by_requests = []
    for ttl in [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]:
        data_staleness = []
        for source in glob.glob('results/?-' + methodology + '-' + str(ttl) + '-' + service + '-caching.csv'):
            df = pd.read_csv(source)
            number_of_requests = len(df)
            stale_responses = df.loc[df['info'] == 'stale']
            number_of_stale_responses = len(stale_responses)
            data_staleness.append(number_of_stale_responses/number_of_requests)
        data_staleness_by_requests.append(mean(data_staleness))
    return data_staleness_by_requests

def get_data_staleness_by_size(methodology, service):
    data_staleness_by_size = []
    for ttl in [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]:
        data_staleness = []
        for source in glob.glob('results/?-' + methodology + '-' + str(ttl) + '-' + service + '-caching.csv'):
            df = pd.read_csv(source)
            total_size_of_all_network_traffic = df['size'].sum()
            stale_responses = df.loc[df['info'] == 'stale']
            total_size_of_stale_responses = stale_responses['size'].sum()
            data_staleness.append(total_size_of_stale_responses/total_size_of_all_network_traffic)
        data_staleness_by_size.append(mean(data_staleness))
    return data_staleness_by_size

def get_memory_usage(methodology, service):
    mean_memory_usage = []
    for ttl in [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]:
        memory_usage = []
        for source in glob.glob('results/?-' + methodology + '-' + str(ttl) + '-' + service + '-memory.csv'):
            df = pd.read_csv(source)
            start_index = df['items'].ne(0).idxmax()
            sizes = df.iloc[start_index:,2].tolist()
            while len(sizes) < 300:
                sizes.append(60)
            sizes = sizes[:300]
            corrected_sizes = [x-60 for x in sizes]
            memory_usage.append(mean(corrected_sizes))
        mean_memory_usage.append(mean(memory_usage))
    return mean_memory_usage

def print_data(methodology, service):
    for ttl in [0, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20]:
        for source in glob.glob('results/?-' + methodology + '-' + str(ttl) + '-' + service + '-caching.csv'):
            df = pd.read_csv(source)
            print("Data for " + service + " service with " + methodology + " caching and a TTL of " + str(ttl) + " seconds")

            number_of_requests = len(df)
            print("Requests: " + str(number_of_requests))
            total_size_of_all_network_traffic = df['size'].sum()
            print("Size of all network traffic: " + str(total_size_of_all_network_traffic) + " bytes")
            print("")

            cached_network_traffic = df.loc[df['source'] == 'cache']
            number_of_cached_responses = len(cached_network_traffic)
            print("Cached responses: " + str(number_of_cached_responses))
            total_size_of_cached_network_traffic = cached_network_traffic['size'].sum()
            print("Size of cached network traffic: " + str(total_size_of_cached_network_traffic))
            print("")

            if ttl > 0:
                print("Request reduction: " + str(number_of_cached_responses/number_of_requests))
                print("Network traffic reduction: " + str(total_size_of_cached_network_traffic/total_size_of_all_network_traffic))
                print("")

            fresh_responses = df.loc[df['info'] == 'fresh']
            number_of_fresh_responses = len(fresh_responses)
            print("Fresh responses: " + str(number_of_fresh_responses))
            total_size_of_fresh_responses = fresh_responses['size'].sum()
            print("Size of fresh responses: " + str(total_size_of_fresh_responses))
            if ttl > 0 and number_of_cached_responses > 0:
                print("Percentage fresh of cached: " + str(number_of_fresh_responses/number_of_cached_responses))
            print("")

            stale_responses = df.loc[df['info'] == 'stale']
            number_of_stale_responses = len(stale_responses)
            print("Stale responses: " + str(number_of_stale_responses))
            total_size_of_stale_responses = stale_responses['size'].sum()
            print("Size of stale responses: " + str(total_size_of_stale_responses))
            if ttl > 0 and number_of_cached_responses > 0:
                print("Percentage stale of cached: " + str(number_of_stale_responses/number_of_cached_responses))
                print("Percentage stale of total: " + str(number_of_stale_responses/number_of_requests))
            print("")

            print("")

def print_mean_data(methodology, service):
    for ttl in [0, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20]:
        print("Data for " + service + " service with " + methodology + " caching and a TTL of " + str(ttl) + " seconds")
        number_of_requests = []
        total_size_of_all_network_traffic = []
        number_of_cached_responses = []
        total_size_of_cached_network_traffic = []
        request_reduction = []
        network_traffic_reduction = []
        number_of_fresh_responses = []
        total_size_of_fresh_responses = []
        percentage_fresh_of_cached = []
        number_of_stale_responses = []
        total_size_of_stale_responses = []
        percentage_stale_of_cached = []
        percentage_stale_of_total = []
        percentage_stale_of_total_size = []
        i = 0
        for source in glob.glob('results/?-' + methodology + '-' + str(ttl) + '-' + service + '-caching.csv'):
            df = pd.read_csv(source)

            number_of_requests.append(len(df))
            total_size_of_all_network_traffic.append(df['size'].sum())

            cached_network_traffic = df.loc[df['source'] == 'cache']
            number_of_cached_responses.append(len(cached_network_traffic))
            total_size_of_cached_network_traffic.append(cached_network_traffic['size'].sum())

            if ttl > 0:
                request_reduction.append(number_of_cached_responses[i]/number_of_requests[i])
                network_traffic_reduction.append(total_size_of_cached_network_traffic[i]/total_size_of_all_network_traffic[i])

            fresh_responses = df.loc[df['info'] == 'fresh']
            number_of_fresh_responses.append(len(fresh_responses))
            total_size_of_fresh_responses.append(fresh_responses['size'].sum())
            if ttl > 0 and number_of_cached_responses[i] > 0:
                percentage_fresh_of_cached.append(number_of_fresh_responses[i]/number_of_cached_responses[i])

            stale_responses = df.loc[df['info'] == 'stale']
            number_of_stale_responses.append(len(stale_responses))
            total_size_of_stale_responses.append(stale_responses['size'].sum())
            if ttl > 0 and number_of_cached_responses[i] > 0:
                percentage_stale_of_cached.append(number_of_stale_responses[i]/number_of_cached_responses[i])
                percentage_stale_of_total.append(number_of_stale_responses[i]/number_of_requests[i])
                percentage_stale_of_total_size.append(total_size_of_stale_responses[i]/total_size_of_all_network_traffic[i])
            i += 1

        print("Requests: " + str(mean(number_of_requests)))
        print("Size of all network traffic: " + str(mean(total_size_of_all_network_traffic)) + " bytes")
        print("")

        print("Cached responses: " + str(mean(number_of_cached_responses)))
        print("Size of cached network traffic: " + str(mean(total_size_of_cached_network_traffic)))
        print("")

        if ttl > 0:
            print("Request reduction: " + str(mean(request_reduction)))
            print("Network traffic reduction: " + str(mean(network_traffic_reduction)))
            print("")

        print("Fresh responses: " + str(mean(number_of_fresh_responses)))
        print("Size of fresh responses: " + str(mean(total_size_of_fresh_responses)))
        if ttl > 0:
            print("Percentage fresh of cached: " + str(mean(percentage_fresh_of_cached)))
        print("")

        print("Stale responses: " + str(mean(number_of_stale_responses)))
        print("Size of stale responses: " + str(mean(total_size_of_stale_responses)))
        if ttl > 0:
            print("Percentage stale of cached: " + str(mean(percentage_stale_of_cached)))
            print("Percentage stale of total: " + str(mean(percentage_stale_of_total)))
            print("Percentage stale of total size: " + str(mean(percentage_stale_of_total_size)))
        print("")

        print("")