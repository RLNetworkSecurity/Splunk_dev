#! /usr/bin/env python
"""
Splunk Sample Script to query splunk api with the latest TOR IP list
filter query splunk indexes and/or source_types
Author: RLNetworkSecurity - RLNetworkSecurity.co.uk
"""

import splunklib
import splunklib.client as client
import splunklib.results as results
from urllib.request import urlopen
import re
from datetime import datetime

TOR_URL = "https://check.torproject.org/torbulkexitlist"


def get_tor_exit_list(tor_url):
    page = urlopen(tor_url)
    data = page.read().decode("utf-8")
    tor_ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', data)
    return(tor_ip)

def splunk_connection(splunk_query):

    HOST = "10.0.0.252"
    PORT = 8089
    USERNAME = "Splunk"
    PASSWORD = "Changeme"
    #Credentials as inputs
    #USERNAME = input('Enter Splunk username: ')
    #PASSWORD = input('Enter Splunk Credentials: ')

    c = client.connect(host=HOST, port=PORT,
                         username=USERNAME,
                         password=PASSWORD)

    c_result = splunklib.results.ResultsReader(
        c.jobs.export(splunk_query))

    for result in c_result:
        if isinstance(result, results.Message):
            print('%s: %s' % (result.type, result.message))
        elif isinstance(result, dict):
            print(result)
        else:
            print("Complete.")

def main():

    SEARCH_TIME = input('Enter Query Time Range example earliest=-24h: ')
    SEARCH_INDEX = input('Enter index for all *: ')
    SEARCH_SOURCETYPE = input('Enter Sourcetype for all *: ')

    tor_ip_list = get_tor_exit_list(TOR_URL)

    for tor_ip in tor_ip_list:

        QUERY = "search * " + SEARCH_TIME + " index=" + SEARCH_INDEX + " " + tor_ip
        result = splunk_connection(QUERY)
        if result = 'None':
            Complete
        elif
            print(result)

if __name__ == "__main__":
    main()
