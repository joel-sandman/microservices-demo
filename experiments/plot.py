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
    
    plt.plot(fine_grained_ttls, fine_grained_network_requests, 'b-.')
    plt.plot(full_page_ttls, full_page_network_requests, 'r--')
    plt.xscale('log')
    plt.xticks([0.1, 0.2, 0.5, 1, 2, 5, 10, 20], [0.1, 0.2, 0.5, 1, 2, 5, 10, 20])
    plt.axis([0.1, 20, 0, 4000])
    plt.show()

def plot_network_traffic_reduction_by_requests():
    ttls = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]
    fine_grained_network_traffic_reduction = get_network_traffic_reduction_by_requests('fine-grained', '*')
    full_page_network_traffic_reduction = get_network_traffic_reduction_by_requests('full-page', '*')

    plt.plot(ttls, fine_grained_network_traffic_reduction, 'b-.', label='Fine-grained caching')
    plt.plot(ttls, full_page_network_traffic_reduction, 'r--', label='Full-page caching')
    plt.plot(ttls, [0]*len(ttls), 'g-', label='No caching')
    plt.xscale('log')
    plt.xticks(ttls, ttls)
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

    plt.plot(ttls, fine_grained_network_traffic_reduction, 'b-.', label='Fine-grained caching')
    plt.plot(ttls, full_page_network_traffic_reduction, 'r--', label='Full-page caching')
    plt.plot(ttls, [0]*len(ttls), 'g-', label='No caching')
    plt.xscale('log')
    plt.xticks(ttls, ttls)
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

    plt.plot(ttls, fine_grained_data_staleness, 'b-.', label='Fine-grained caching')
    plt.plot(ttls, full_page_data_staleness, 'r--', label='Full-page caching')
    plt.plot(ttls, [0]*len(ttls), 'g-', label='No caching')
    plt.xscale('log')
    plt.xticks(ttls, ttls)
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

    plt.plot(ttls, fine_grained_data_staleness, 'b-.', label='Fine-grained caching')
    plt.plot(ttls, full_page_data_staleness, 'r--', label='Full-page caching')
    plt.plot(ttls, [0]*len(ttls), 'g-', label='No caching')
    plt.xscale('log')
    plt.xticks(ttls, ttls)
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

    plt.plot(ttls, fine_grained_get_memory_usage, 'b-.', label='Fine-grained caching')
    plt.plot(ttls, full_page_get_memory_usage, 'r--', label='Full-page caching')
    plt.plot(ttls, [0]*len(ttls), 'g-', label='No caching')
    plt.xscale('log')
    plt.xticks(ttls, ttls)
    plt.suptitle('Memory Usage')
    plt.xlabel('TTL (s)')
    plt.ylabel('Memory Usage (bytes)')
    plt.legend()
    plt.show()
    # plt.savefig('plot_memory_usage.png', bbox_inches='tight')

def plot_network_traffic_reduction_divided_by_data_staleness():
    ttls = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]
    fine_grained_network_traffic_reduction = get_network_traffic_reduction_by_size('fine-grained', '*')
    full_page_network_traffic_reduction = get_network_traffic_reduction_by_size('full-page', '*')
    fine_grained_data_staleness = get_data_staleness_by_size('fine-grained', '*')
    full_page_data_staleness = get_data_staleness_by_size('full-page', '*')

    fine_grained_quotient = [i / j for i, j in zip(fine_grained_network_traffic_reduction, fine_grained_data_staleness)]
    full_page_quotient = [i / j for i, j in zip(full_page_network_traffic_reduction, full_page_data_staleness)]

    print(full_page_quotient)
    plt.plot(ttls, fine_grained_quotient, 'b-.', label='Fine-grained caching')
    plt.plot(ttls, full_page_quotient, 'r--', label='Full-page caching')
    # plt.plot(ttls, [1]*len(ttls), 'g-', label='No caching')
    plt.xscale('log')
    plt.xticks(ttls, ttls)
    plt.suptitle('Network Traffic Reduction / Date Staleness')
    plt.xlabel('TTL (s)')
    plt.ylabel('Network Traffic Reduction / Date Staleness')
    plt.legend()
    plt.show()
    # plt.savefig('plot_memory_usage.png', bbox_inches='tight')

def plot_network_traffic_reduction_for_ttl():
    methodology = ['fine-grained']
    fine_grained_network_traffic_reduction = get_network_traffic_reduction_by_requests('fine-grained', '*')
    full_page_network_traffic_reduction = get_network_traffic_reduction_by_requests('full-page', '*')

    plt.bar(0, fine_grained_network_traffic_reduction[4], color='blue', label='Fine-grained caching')
    plt.bar(1, full_page_network_traffic_reduction[4], color='red', label='Full-page caching')
    plt.bar(2, 0, color='green', label='No caching')
    plt.xticks([0, 1, 2], ['Fine-grained', 'Full-page', 'No cache'])
    plt.suptitle('Network Traffic Reduction for TTL = 2 seconds')
    plt.xlabel('Methodology')
    plt.ylabel('Network Traffic Reduction')
    plt.legend()
    plt.show()
    # plt.savefig('network_traffic_reduction_by_requests.png', bbox_inches='tight')


if __name__=="__main__":
    # plot_network_traffic_reduction_by_requests()
    # plot_network_traffic_reduction_by_size()
    # plot_data_staleness_by_requests()
    # plot_data_staleness_by_size()
    # plot_memory_usage()
    # plot_network_traffic_reduction_divided_by_data_staleness()
    # plot_network_traffic_reduction_for_ttl()
    # print_mean_data("full-page", "*")