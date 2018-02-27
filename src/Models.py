'''
Created on 2 Nov 2017

@author: ostlerr
'''
from datacite import schema40
import sys
import json
from EraConnect import getDataCiteClient    

url = input('Enter URL: ')
filepath = 'D:\Code\python\workspace\DOIs4Eradoc\dataCiteJson' #input('Enter filepath:')
filename = input('Enter filename: ')
#MODEL-MANUAL-ROTHC-WIN-VERSION-2014.json
jsonData = json.load(open(filepath+'/'+filename))
doi = jsonData['identifier']['identifier']
print(doi)
assert schema40.validate(jsonData)    
doc = schema40.tostring(jsonData)
print(doc)

try:
    d = getDataCiteClient()
    d.metadata_post(doc)    
    d.doi_post(doi, url)
    xname = "D:/doi_out/"+ filename + ".xml"
    fxname = open(xname,'w+')
    fxname.write(doc)
    fxname.close()
    print('done')
except:
    print("Unexpected error:", sys.exc_info()[0])
