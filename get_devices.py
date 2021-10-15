import requests
from getpass import getpass
from pprint import pprint
import json

base_url = 'https://netbox.bowdoin.edu/api/'
uri = 'ipam/ip-addresses/?limit=0'
url = base_url + uri
token = getpass()
# params = { 'name': "junos-dev-ex4200" }

headers = {'Authorization': "Token " + token}

# r = requests.get(url, params=params, headers=headers)
r = requests.get(url, headers=headers)

output = json.loads(r.text)
devices = output['results']

addresses = []

for each in devices:
    cidr = each['address']
    ipv4_addr = (cidr.split("/", 1)[0])
    addresses.append(ipv4_addr)

for address in addresses:
    print(address)
