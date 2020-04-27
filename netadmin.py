import argparse
import os,sys
import netaddr
from netaddr import *
import urllib3


class netadmin:
    """A simple python script/tool designed for IP Management
        a) Abstract:
                    getipdetails(<input_ip>,<options: deep|fast>) : Return the subnet details, region, provider, whoisinfo, ASN
                    getipdetails(<input_subnet) : Return all IP addresses
                    decompress(<list_of_ips_and_subnets>): Return a list with subnets and IP's expanded.
                    Sample Usecase : Security scanners containing mix of IP's and subnets to be expanded to be used as filters in splunk
                    compress (<list_of_ips>) : Input a list of NON-SEQUENTIAL IP's, compress them to the closest subnets and
                         return a list with IP's and possible subnets which can be carved out from the same. Also generate
                         a subnet to possibly include all the IP's so that a sequential allocation can be provided to avoid
                         holes/gaps.

        b) Reference or inputs:
                         https://ip-ranges.amazonaws.com/ip-ranges.json
                         https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_20200420.json
                         https://docs.cloud.oracle.com/en-us/iaas/tools/public_ip_ranges.json
                         https://stat.ripe.net/data/bgp-updates/data.json
        """

    def __init__(self):
        """Initialize all variables here"""
        print("Inside constructor, initialize variables here..")


    def build_inventory(self,url):
        """ Helper method: Input: URL | Output: Hash Table """
        http = urllib3.PoolManager()
        request = http.request('GET','https://ip-ranges.amazonaws.com/ip-ranges.json')
        print (request)

    def expand(self,infile):
        print(infile)
        try:
            with open(infile,'r') as f:
                input = f.readlines()

            for line in input:
                ip_list = list(line.strip())
                print(len(ip_list))
                print(ip_list)

        finally:
            f.close()

def main():

    cli = argparse.ArgumentParser('netadmin')
    cli.add_argument("--input_type",type=str,help="Input type should be of type text/json")
    cli.add_argument("--input_file",type=str,help="Input file with IP/Subnets")
    args = cli.parse_args()

    netadm  = netadmin()
    netadm.expand(args.input_file)

    if len(sys.argv) == 0:
        print ("Insufficient arguments supplied, exiting! Run -h")
        exit(0)

if __name__ == "__main__":
    main()

#netadmin

