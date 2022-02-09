import pynetbox
from getpass import getpass

base_url = 'https://netbox.bowdoin.edu/'
token = getpass()

nb = pynetbox.api(
    base_url,
    token=token
)

devices = nb.dcim.devices.all()

for device in devices:
    print(device.name)

