'''
Created on 2 Oct 2017
username:password https://mds.datacite.org/doi/10.5438/0012
@author: ostlerr
'''
from requests.auth import HTTPBasicAuth
import requests
req = requests.get("http://mds.datacite.org/metadata/10.23637/ecn-north-wyke-booklet-2015",auth=HTTPBasicAuth('BL.ROTHRES','R0th@msted1843'))
print(req)