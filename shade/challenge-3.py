#3: Listing flavors
from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')

print "\nAvailable flavors:"
flavors =  conn.list_flavors()
for flavor in flavors:
    print(flavor)
