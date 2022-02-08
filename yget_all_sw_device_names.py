import requests
from getpass import getpass
from pprint import pprint
import json

# https://netbox.bowdoin.edu/api/docs/

base_url = 'https://netbox.bowdoin.edu/'
uri = 'api/dcim/devices/?limit=0'
url = base_url + uri
token = getpass()

headers = {'Authorization': "Token " + token}

r = requests.get(url, headers=headers)

output = json.loads(r.text)
devices = output['results']

pprint(output)