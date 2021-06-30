#! /usr/bin/env python
"""
Splunk Sample Script output windows defender alerts in dictionary
"""

import splunklib
import splunklib.client as client
import splunklib.results as results
from datetime import datetime

HOST = "10.0.0.252"
PORT = 8089
USERNAME = "Splunk"
PASSWORD = "Changeme"

#Credentials as inputs
#USERNAME = input('Enter Splunk username: ')
#PASSWORD = input('Enter Splunk Credentials: ')

#QUERY_BUILD_AS_INPUTS
SEARCH_TIME = input('Enter Query Time Range example earliest=-24h: ')
SEARCH_STRING = "index=windefender Severity_Name!=null Severity_Name=* Computer=* Threat_Name=* Category_Name=* | table Detection_Time,Detection_User,Computer,Severity_Name,Category_Name,Threat_Name,Action_Name,Additional_Actions_String,Source_Name"

if __name__ == '__main__':
    c = client.connect(host=HOST, port=PORT,
                         username=USERNAME,
                         password=PASSWORD)

    QUERY = "search * " + SEARCH_TIME + " " + SEARCH_STRING
    print(QUERY)
    #"search * earliest=-24h@h index=* 10.0.0 | top index"

    c_result = splunklib.results.ResultsReader(
        c.jobs.export(QUERY))

    for result in c_result:
        if isinstance(result, results.Message):
            print('%s: %s' % (result.type, result.message))
        elif isinstance(result, dict):
            print(result)
        else:
            print("Complete.")
