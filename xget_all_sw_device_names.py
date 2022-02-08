import requests
from getpass import getpass
from pprint import pprint
import json

# https://netbox.bowdoin.edu/api/docs/

base_url = 'https://netbox.bowdoin.edu/'
uri = 'api/dcim/devices/?limit=2000'
url = base_url + uri
token = getpass()

headers = {'Authorization': "Token " + token}

r = requests.get(url, headers=headers)

output = json.loads(r.text)
devices = output['results']

for each in devices:
    device_role = each['device_role']
    display = device_role['display']
    if 'Access Switch' in display:
        print(each['name'])
        # print(display)
