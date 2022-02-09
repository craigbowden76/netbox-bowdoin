import pynetbox
from getpass import getpass

base_url = 'https://netbox.bowdoin.edu/'
token = getpass()

nb = pynetbox.api(
    base_url,
    token=token
)

# devices = nb.dcim.devices.all()

types = [t.id for t in nb.dcim.device_types.filter(model__ic="3560")]
for dev in nb.dcim.devices.filter(device_type_id=types):
    print(dev)

# for stack in nb.dcim.virtual_chassis.filter():
#     master = str(stack.master)
#     print(master.split(':')[0])
