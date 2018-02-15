'''
Created on 2 Nov 2017

@author: ostlerr
'''
from datacite import schema40
import sys
import json
from EraConnect import getDataCiteClient    

##########################################################
#                                                        #
# EDIT THESE!!!                                          #
#                                                        #
##########################################################
model = 'rothamsted-sift-model'
url = 'https://www.rothamsted.ac.uk/'+model
filename = 'BROADBALK-WHEAT-YIELD-OA.json'

jsonData = json.load(open('D:/Code/python/workspace/DOIs4Eradoc/dataCiteJson/'+filename))
doi = jsonData['identifier']['identifier']
print(doi)
assert schema40.validate(jsonData)    
doc = schema40.tostring(jsonData)
print(doc)

# try:
#     d = getDataCiteClient()
#     d.metadata_post(doc)    
#     d.doi_post(doi, url)
#     xname = "D:/doi_out/"+ model + ".xml"
#     fxname = open(xname,'w+')
#     fxname.write(doc)
#     fxname.close()
#     print('done')
# except:
#     print("Unexpected error:", sys.exc_info()[0])
