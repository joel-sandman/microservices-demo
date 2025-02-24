#!/usr/bin/env python3

import matplotlib.pyplot as plt

from parse import print_data
from parse import print_mean_data
from parse import get_network_traffic_by_requests
from parse import get_network_traffic_by_size
from parse import get_network_traffic_reduction_by_requests
from parse import get_network_traffic_reduction_by_size
from parse import get_data_staleness_by_requests
from parse import get_data_staleness_by_size
from parse import get_memory_usage

def plot_network_traffic_by_requests():
    ttls = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]
    frontend = get_network_traffic_by_requests('fine-grained', 'frontend')
    checkout = get_network_traffic_by_requests('fine-grained', 'checkout')
    recommendation = get_network_traffic_by_requests('fine-grained', 'recommendation')
    fine_grained_network_requests = [frontend[i] + checkout[i] + recommendation[i] for i in range(len(frontend))]
    full_page_network_requests = get_network_traffic_by_requests('full-page', '*')

    print(fine_grained_network_requests)
    print(full_page_network_requests)

    plt.plot(ttls, fine_grained_network_requests[1:], '-.bd', label='Fine-grained caching')
    plt.plot(ttls, full_page_network_requests[1:], '--ro', label='Full-page caching')
    plt.xscale('log')
    plt.xticks(ttls, ttls)
    plt.xlabel('TTL (s)')
    plt.ylabel('Network Traffic (requests)')
    plt.legend()
    plt.show()
    # plt.savefig('plots/network_traffic_by_requests.svg', bbox_inches='tight')

def plot_network_traffic_by_size():
    ttls = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]
    frontend = get_network_traffic_by_size('fine-grained', 'frontend')
    checkout = get_network_traffic_by_size('fine-grained', 'checkout')
    recommendation = get_network_traffic_by_size('fine-grained', 'recommendation')
    fine_grained_network_size = [frontend[i] + checkout[i] + recommendation[i] for i in range(len(frontend))]
    full_page_network_size = get_network_traffic_by_size('full-page', '*')

    print(fine_grained_network_size)
    print(full_page_network_size)

    plt.plot(ttls, fine_grained_network_size[1:], '-.bd', label='Fine-grained caching')
    plt.plot(ttls, full_page_network_size[1:], '--ro', label='Full-page caching')
    plt.xscale('log')
    plt.xticks(ttls, ttls)
    plt.xlabel('TTL (s)')
    plt.ylabel('Network Traffic (MB)')
    plt.legend()
    plt.show()
    # plt.savefig('plots/network_traffic_by_size.svg', bbox_inches='tight')

def plot_network_traffic_reduction_by_requests():
    ttls = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]
    fine_grained_network_traffic_reduction = get_network_traffic_reduction_by_requests('fine-grained', '*')
    full_page_network_traffic_reduction = get_network_traffic_reduction_by_requests('full-page', '*')

    plt.plot(ttls, fine_grained_network_traffic_reduction, '-.bd', label='Fine-grained caching')
    plt.plot(ttls, full_page_network_traffic_reduction, '--ro', label='Full-page caching')
    plt.plot(ttls, [0]*len(ttls), '-gx', label='No caching')
    plt.xscale('log')
    plt.xticks(ttls, ttls)
    plt.xlabel('TTL (s)')
    plt.ylabel('Network Traffic Reduction (by requests)')
    plt.legend()
    plt.show()
    # plt.savefig('plots/network_traffic_reduction_by_requests.svg', bbox_inches='tight')

def plot_network_traffic_reduction_by_size():
    ttls = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]
    fine_grained_network_traffic_reduction = get_network_traffic_reduction_by_size('fine-grained', '*')
    full_page_network_traffic_reduction = get_network_traffic_reduction_by_size('full-page', '*')

    print(fine_grained_network_traffic_reduction)
    print(full_page_network_traffic_reduction)

    plt.plot(ttls, fine_grained_network_traffic_reduction, '-.bd', label='Fine-grained caching')
    plt.plot(ttls, full_page_network_traffic_reduction, '--ro', label='Full-page caching')
    plt.plot(ttls, [0]*len(ttls), '-gx', label='No caching')
    plt.xscale('log')
    plt.xticks(ttls, ttls)
    plt.xlabel('TTL (s)')
    plt.ylabel('Network Traffic Reduction (by size)')
    plt.legend()
    plt.show()
    # plt.savefig('plots/network_traffic_reduction_by_size.svg', bbox_inches='tight')

def plot_data_staleness_by_requests():
    ttls = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]
    fine_grained_data_staleness = get_data_staleness_by_requests('fine-grained', '*')
    full_page_data_staleness = get_data_staleness_by_requests('full-page', '*')

    plt.plot(ttls, fine_grained_data_staleness, '-.bd', label='Fine-grained caching')
    plt.plot(ttls, full_page_data_staleness, '--ro', label='Full-page caching')
    plt.plot(ttls, [0]*len(ttls), '-gx', label='No caching')
    plt.xscale('log')
    plt.xticks(ttls, ttls)
    plt.xlabel('TTL (s)')
    plt.ylabel('Data Staleness (by requests)')
    plt.legend()
    plt.show()
    # plt.savefig('plots/data_staleness_by_requests.svg', bbox_inches='tight')

def plot_data_staleness_by_size():
    ttls = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]
    fine_grained_data_staleness = get_data_staleness_by_size('fine-grained', '*')
    full_page_data_staleness = get_data_staleness_by_size('full-page', '*')

    print(fine_grained_data_staleness)
    print(full_page_data_staleness)

    plt.plot(ttls, fine_grained_data_staleness, '-.bd', label='Fine-grained caching')
    plt.plot(ttls, full_page_data_staleness, '--ro', label='Full-page caching')
    plt.plot(ttls, [0]*len(ttls), '-gx', label='No caching')
    plt.xscale('log')
    plt.xticks(ttls, ttls)
    plt.xlabel('TTL (s)')
    plt.ylabel('Data Staleness (by size)')
    plt.legend()
    plt.show()
    # plt.savefig('plots/data_staleness_by_size.svg', bbox_inches='tight')

def plot_memory_usage():
    ttls = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]
    frontend = get_memory_usage('fine-grained', 'frontend')
    checkout = get_memory_usage('fine-grained', 'checkout')
    recommendation = get_memory_usage('fine-grained', 'recommendation')
    fine_grained_memory_usage = [frontend[i] + checkout[i] + recommendation[i] for i in range(len(frontend))]
    full_page_memory_usage = get_memory_usage('full-page', '*')

    print(fine_grained_memory_usage)
    print(full_page_memory_usage)

    plt.plot(ttls, fine_grained_memory_usage, '-.bd', label='Fine-grained caching')
    plt.plot(ttls, full_page_memory_usage, '--ro', label='Full-page caching')
    plt.plot(ttls, [0]*len(ttls), '-gx', label='No caching')
    plt.xscale('log')
    plt.xticks(ttls, ttls)
    plt.xlabel('TTL (s)')
    plt.ylabel('Memory Usage (kB)')
    plt.legend()
    plt.show()
    # plt.savefig('plots/memory_usage.svg', bbox_inches='tight')

def plot_memory_usage_vs_network_traffic_reduction_by_size():
    ttls = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]

    frontend = get_memory_usage('fine-grained', 'frontend')
    checkout = get_memory_usage('fine-grained', 'checkout')
    recommendation = get_memory_usage('fine-grained', 'recommendation')
    fine_grained_memory_usage = [frontend[i] + checkout[i] + recommendation[i] for i in range(len(frontend))]
    full_page_memory_usage = get_memory_usage('full-page', '*')

    frontend = get_network_traffic_by_size('fine-grained', 'frontend')
    checkout = get_network_traffic_by_size('fine-grained', 'checkout')
    recommendation = get_network_traffic_by_size('fine-grained', 'recommendation')
    fine_grained_network_size = [frontend[i] + checkout[i] + recommendation[i] for i in range(len(frontend))]
    full_page_network_size = get_network_traffic_by_size('full-page', '*')

    fine_grained_network_reduction_size = [2.4621604 - size for size in fine_grained_network_size]
    full_page_network_reduction_size = [10.077961 - size for size in full_page_network_size]

    fine_grained_quotient = [i / j for i, j in zip(fine_grained_memory_usage, fine_grained_network_reduction_size[1:])]
    full_page_quotient = [i / j for i, j in zip(full_page_memory_usage, full_page_network_reduction_size[1:])]

    print(fine_grained_quotient)
    print(full_page_quotient)

def print_network_traffic_reduction_vs_data_staleness_by_requests():
    ttls = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]
    fine_grained_network_traffic_reduction = get_network_traffic_reduction_by_requests('fine-grained', '*')
    full_page_network_traffic_reduction = get_network_traffic_reduction_by_requests('full-page', '*')
    fine_grained_data_staleness = get_data_staleness_by_requests('fine-grained', '*')
    full_page_data_staleness = get_data_staleness_by_requests('full-page', '*')

    fine_grained_quotient = [i / j for i, j in zip(fine_grained_network_traffic_reduction, fine_grained_data_staleness)]
    full_page_quotient = [i / j for i, j in zip(full_page_network_traffic_reduction, full_page_data_staleness)]

    print(fine_grained_quotient)
    print(full_page_quotient)

def print_network_traffic_reduction_vs_data_staleness_by_size():
    ttls = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]
    fine_grained_network_traffic_reduction = get_network_traffic_reduction_by_size('fine-grained', '*')
    full_page_network_traffic_reduction = get_network_traffic_reduction_by_size('full-page', '*')
    fine_grained_data_staleness = get_data_staleness_by_size('fine-grained', '*')
    full_page_data_staleness = get_data_staleness_by_size('full-page', '*')

    fine_grained_quotient = [i / j for i, j in zip(fine_grained_network_traffic_reduction, fine_grained_data_staleness)]
    full_page_quotient = [i / j for i, j in zip(full_page_network_traffic_reduction, full_page_data_staleness)]

    print(fine_grained_quotient)
    print(full_page_quotient)

def plot_network_traffic_reduction_for_ttl():
    methodology = ['fine-grained']
    fine_grained_network_traffic_reduction = get_network_traffic_reduction_by_requests('fine-grained', '*')
    full_page_network_traffic_reduction = get_network_traffic_reduction_by_requests('full-page', '*')

    plt.bar(0, fine_grained_network_traffic_reduction[4], color='blue', label='Fine-grained caching')
    plt.bar(1, full_page_network_traffic_reduction[4], color='red', label='Full-page caching')
    plt.bar(2, 0, color='green', label='No caching')
    plt.xticks([0, 1, 2], ['Fine-grained', 'Full-page', 'No cache'])
    plt.xlabel('Methodology')
    plt.ylabel('Network Traffic Reduction')
    plt.legend()
    plt.show()
    # plt.savefig('plots/network_traffic_reduction_by_requests_for_ttl.svg', bbox_inches='tight')

if __name__=="__main__":
    # plot_network_traffic_by_requests()
    # plot_network_traffic_by_size()
    # plot_network_traffic_reduction_by_requests()
    # plot_network_traffic_reduction_by_size()
    # plot_data_staleness_by_requests()
    # plot_data_staleness_by_size()
    # plot_memory_usage()
    # plot_memory_usage_vs_network_traffic_reduction_by_size()
    # print_network_traffic_reduction_vs_data_staleness_by_requests()
    # print_network_traffic_reduction_vs_data_staleness_by_size()
    # plot_network_traffic_reduction_for_ttl()
    # print_mean_data("full-page", "*")