import requests
from getpass import getpass
from pprint import pprint
import json

# https://netbox.bowdoin.edu/api/docs/

base_url = 'https://netbox.bowdoin.edu/'
uri = 'api/dcim/devices/?limit=0'
url = base_url + uri
token = getpass()
# params = { 'name': "junos-dev-ex4200" }

headers = {'Authorization': "Token " + token}

# r = requests.get(url, params=params, headers=headers)
r = requests.get(url, headers=headers)

output = json.loads(r.text)
devices = output['results']

devices_names = []
for each in devices:
    device = each['name']
    names = (device.split(":"))
    devices_names.append(names[0])
    #print(names[0])

device_name = (list(set(devices_names)))
device_name.sort()

for those in device_name:
    if "-sw-" in those:
        continue
    print(those)
