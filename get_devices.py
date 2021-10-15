import requests
from getpass import getpass
from pprint import pprint
import json

base_url = 'https://netbox.bowdoin.edu/api/'
uri = 'ipam/ip-addresses'
url = base_url + uri
token = getpass()
# params = { 'name': "junos-dev-ex4200" }

headers = {'Authorization': "Token " + token}

# r = requests.get(url, params=params, headers=headers)
r = requests.get(url, headers=headers)

output = json.loads(r.text)
results = output['results']

devices = []

for k, v in enumerate(results):
    devices.append(v)

for each in devices:
    print(each)
    print(type(each))