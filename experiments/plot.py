#!/usr/bin/env python3

import matplotlib.pyplot as plt

from parse import print_data
from parse import print_mean_data
from parse import get_network_traffic
from parse import get_network_traffic_reduction_by_requests
from parse import get_network_traffic_reduction_by_size
from parse import get_data_staleness_by_requests
from parse import get_data_staleness_by_size
from parse import get_memory_usage

def plot_network_traffic():
    fine_grained_network_data = get_network_traffic('fine-grained', '*')
    fine_grained_ttls, fine_grained_network_requests = zip(*fine_grained_network_data)
    full_page_network_data = get_network_traffic('full-page', '*')
    full_page_ttls, full_page_network_requests = zip(*full_page_network_data)
    
    plt.plot(fine_grained_ttls, fine_grained_network_requests, 'r')
    plt.plot(full_page_ttls, full_page_network_requests, 'b')
    plt.xscale('log')
    plt.xticks([0.1, 0.2, 0.5, 1, 2, 5, 10, 20], [0.1, 0.2, 0.5, 1, 2, 5, 10, 20])
    plt.axis([0.1, 20, 0, 4000])
    plt.show()

def plot_network_traffic_reduction_by_requests():
    ttls = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]
    fine_grained_network_traffic_reduction = get_network_traffic_reduction_by_requests('fine-grained', '*')
    full_page_network_traffic_reduction = get_network_traffic_reduction_by_requests('full-page', '*')

    plt.plot(ttls, fine_grained_network_traffic_reduction, 'r', label='Fine-grained caching')
    plt.plot(ttls, full_page_network_traffic_reduction, 'b', label='Full-page caching')
    plt.xscale('log')
    plt.xticks([0.1, 0.2, 0.5, 1, 2, 5, 10, 20], [0.1, 0.2, 0.5, 1, 2, 5, 10, 20])
    plt.axis([0.1, 20, 0, 1])
    plt.suptitle('Network Traffic Reduction by Number of Requests')
    plt.xlabel('TTL (s)')
    plt.ylabel('Network Traffic Reduction')
    plt.legend()
    plt.show()
    # plt.savefig('network_traffic_reduction_by_requests.png', bbox_inches='tight')

def plot_network_traffic_reduction_by_size():
    ttls = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]
    fine_grained_network_traffic_reduction = get_network_traffic_reduction_by_size('fine-grained', '*')
    full_page_network_traffic_reduction = get_network_traffic_reduction_by_size('full-page', '*')

    plt.plot(ttls, fine_grained_network_traffic_reduction, 'r', label='Fine-grained caching')
    plt.plot(ttls, full_page_network_traffic_reduction, 'b', label='Full-page caching')
    plt.xscale('log')
    plt.xticks([0.1, 0.2, 0.5, 1, 2, 5, 10, 20], [0.1, 0.2, 0.5, 1, 2, 5, 10, 20])
    plt.axis([0.1, 20, 0, 1])
    plt.suptitle('Network Traffic Reduction by Size')
    plt.xlabel('TTL (s)')
    plt.ylabel('Network Traffic Reduction')
    plt.legend()
    plt.show()
    # plt.savefig('plot_network_traffic_reduction_by_size.png', bbox_inches='tight')

def plot_data_staleness_by_requests():
    ttls = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]
    fine_grained_data_staleness = get_data_staleness_by_requests('fine-grained', '*')
    full_page_data_staleness = get_data_staleness_by_requests('full-page', '*')

    plt.plot(ttls, fine_grained_data_staleness, 'r', label='Fine-grained caching')
    plt.plot(ttls, full_page_data_staleness, 'b', label='Full-page caching')
    plt.xscale('log')
    plt.xticks([0.1, 0.2, 0.5, 1, 2, 5, 10, 20], [0.1, 0.2, 0.5, 1, 2, 5, 10, 20])
    # plt.axis([0.1, 20, 0, 1])
    plt.suptitle('Data Staleness by Requests')
    plt.xlabel('TTL (s)')
    plt.ylabel('Data Staleness')
    plt.legend()
    plt.show()
    # plt.savefig('plot_data_staleness_by_requests.png', bbox_inches='tight')

def plot_data_staleness_by_size():
    ttls = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]
    fine_grained_data_staleness = get_data_staleness_by_size('fine-grained', '*')
    full_page_data_staleness = get_data_staleness_by_size('full-page', '*')

    plt.plot(ttls, fine_grained_data_staleness, 'r', label='Fine-grained caching')
    plt.plot(ttls, full_page_data_staleness, 'b', label='Full-page caching')
    plt.xscale('log')
    plt.xticks([0.1, 0.2, 0.5, 1, 2, 5, 10, 20], [0.1, 0.2, 0.5, 1, 2, 5, 10, 20])
    # plt.axis([0.1, 20, 0, 1])
    plt.suptitle('Data Staleness by Size')
    plt.xlabel('TTL (s)')
    plt.ylabel('Data Staleness')
    plt.legend()
    plt.show()
    # plt.savefig('plot_data_staleness_by_size.png', bbox_inches='tight')

def plot_memory_usage():
    ttls = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]
    fine_grained_get_memory_usage = get_memory_usage('fine-grained', '*')
    full_page_get_memory_usage = get_memory_usage('full-page', '*')

    plt.plot(ttls, fine_grained_get_memory_usage, 'r', label='Fine-grained caching')
    plt.plot(ttls, full_page_get_memory_usage, 'b', label='Full-page caching')
    plt.xscale('log')
    plt.xticks([0.1, 0.2, 0.5, 1, 2, 5, 10, 20], [0.1, 0.2, 0.5, 1, 2, 5, 10, 20])
    # plt.axis([0.1, 20, 0, 1])
    plt.suptitle('Memory Usage')
    plt.xlabel('TTL (s)')
    plt.ylabel('Memory Usage (bytes)')
    plt.legend()
    plt.show()
    # plt.savefig('plot_memory_usage.png', bbox_inches='tight')

if __name__=="__main__":
    # plot_network_traffic_reduction_by_size()
    # plot_data_staleness_by_requests()
    plot_memory_usage()
    # print_mean_data("fine-grained", "*")