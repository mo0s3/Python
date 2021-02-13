#!/usr/bin/python3

import json
import sys
import requests

def check_abuseipdb(ip_addr, abuseipdb_key):

    """
    This function will query https://www.abuseipdb.com for the reputation of an IP address>

    The functiontakes two parameters:
    ip_addr (the IP address to query) and abuseipdb_key (your AbuseIPDB API key).

    More info: https://docs.abuseipdb.com/#introduction
    """

    url = 'https://api.abuseipdb.com/api/v2/check'

    query = {
        'ipAddress': ip_addr,
        'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',
        'Key': abuseipdb_key
    }

    response = requests.request(method='GET', url=url, headers=headers, params=query)
    decoded_response = json.loads(response.text)

    # print a formatted report from the response above
    print('\n')
    print('=' * 60)
    print("\t\tAbuse IP Database Report:\t\t")
    print('\n')

    print("IP Address: " + str(decoded_response['data']['ipAddress']))
    print("Abuse Score: " + str(decoded_response['data']['abuseConfidenceScore']))
    print("Country Code: " + str(decoded_response['data']['ipAddress']))
    print("Usage: " + str(decoded_response['data']['usageType']))
    print("ISP: " + str(decoded_response['data']['isp']))
    print("Domain: " + str(decoded_response['data']['domain']))
    print("Last Reported Abuse Date: " + str(decoded_response['data']['lastReportedAt']))
    print('=' * 60)
    print('\n')

if __name__ == "__main__":
    api_key = CHANGE ME # your abuseipdb key
    if len(sys.argv) > 1:
        if sys.argv[1] == '--ip':
            ip = str(sys.argv[2])
            check_abuseipdb(ip, api_key)
    else:
        print('\n')
        print('=' * 45)
        print("\t\tUsage Section")
        print('\n')
        print('--ip\t ip address to query')
        print('=' * 45)
        print('\n')