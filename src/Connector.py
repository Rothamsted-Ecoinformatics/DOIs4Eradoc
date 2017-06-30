'''
Created on 30 May 2017

@author: ostlerr
'''
import pymysql
import configparser
from datacite import DataCiteMDSClient, schema40


config = configparser.ConfigParser()
config.read('config.ini')
# ERA database
erahost = config['ERA_DATABASE']['host']
erauser = config['ERA_DATABASE']['user']
erapwd= config['ERA_DATABASE']['password']
eradb = config['ERA_DATABASE']['db']
eraCon = pymysql.connect(host=erahost,user=erauser,password=erapwd,db=eradb)

cursor = eraCon.cursor()



#try:
cursor.execute("select Books.bookid,booktitle,year,count(*) as nofPages from Books inner join Pages on Books.bookid = Pages.bookid where collectionID = 1 group by Books.bookid,booktitle,year order by year limit 1 ");
data = cursor.fetchall()
for row in data:
    # Open a file named for the ID and collection.
    bookId = row[0]
    bookTitle = row[1]
    year = row[2]
    nofPages = row[3]
    fname = "D:/doi_out/1-" + str(bookId) + ".xml"
    print (fname)
    f = open(fname, "w+")
#     data = {
#         'identifier': {
#             'identifier': '10.23637/ERADOC.1.' + str(bookId),
#             'identifierType':'DOI'
#         },
#         'creators': [
#             {'creatorName': 'Rothamsted Experimental Station'}
#         ],
#         'titles': [
#             {'title': bookTitle}
#         ],
#         'publisher': 'Lawes Agricultural Trust',
#         'publicationYear': year,
#         'resourceType': {
#             'resourceTypeGeneral': 'Text'
#         },
#         'subjects': [{
#             'subject': 'crop yield',
#             {
#                 'subjectScheme':'AGROVOC',
#                 'schemeURI':'http://aims.fao.org/standards/agrovoc',
#                 'valueURI':'http://aims.fao.org/aos/agrovoc/c_10176'
#             }  
#         }]
#     }
    # Validate dictionary
    #assert schema40.validate(data)

    doc = schema40.tostring(data)

    #f.write(doc)
    f.write("<resource xmlns=\"http://datacite.org/schema/kernel-3\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://datacite.org/schema/kernel-3 http://schema.datacite.org/meta/kernel-3/metadata.xsd\">\n")
    f.write("<identifier identifierType=\"DOI\">10.23637/ERADOC.1." + str(bookId) + "</identifier>")
    f.write("<creators>")
    f.write("<creatorName>Rothamsted Experimental Station</creatorName>")
    f.write("</creators>")
    f.write("<titles>")
    f.write("<title>"+bookTitle+"</title>")
    f.write("</titles>")
    f.write("<publisher>Lawes Agricultural Trust</publisher>")
    f.write("<publicationYear>"+year+"</publicationYear>")
    f.write("<resourceType resourceTypeGeneral=\"Text\">Text</resourceType>")
    f.write("<subjects>")
    f.write("<subject xml:lang=\"en-us\" subjectScheme=\"AGROVOC\" schemeURI=\"http://aims.fao.org/standards/agrovoc\" valueURI=\"http://aims.fao.org/aos/agrovoc/c_10176\">crop yield</subject>")
    f.write("<subject xml:lang=\"en-us\" subjectScheme=\"AGROVOC\" schemeURI=\"http://aims.fao.org/standards/agrovoc\" valueURI=\"http://aims.fao.org/aos/agrovoc/c_4780\">meteorological observations</subject>")
    f.write("<subject xml:lang=\"en-us\" subjectScheme=\"AGROVOC\" schemeURI=\"http://aims.fao.org/standards/agrovoc\" valueURI=\"http://aims.fao.org/aos/agrovoc/c_10795\">fertilizer application</subject>")
    f.write("<subject xml:lang=\"en-us\" subjectScheme=\"AGROVOC\" schemeURI=\"http://aims.fao.org/standards/agrovoc\" valueURI=\"http://aims.fao.org/aos/agrovoc/c_8373\">wheat</subject>")
    f.write("<subject xml:lang=\"en-us\" subjectScheme=\"AGROVOC\" schemeURI=\"http://aims.fao.org/standards/agrovoc\" valueURI=\"http://aims.fao.org/aos/agrovoc/c_7156\">soil</subject>")
    f.write("<subject xml:lang=\"en-us\" subjectScheme=\"AGROVOC\" schemeURI=\"http://aims.fao.org/standards/agrovoc\" valueURI=\"http://aims.fao.org/aos/agrovoc/c_8679\">agricultural research</subject>")
    f.write("<subject xml:lang=\"en-us\" subjectScheme=\"AGROVOC\" schemeURI=\"http://aims.fao.org/standards/agrovoc\" valueURI=\"http://aims.fao.org/aos/agrovoc/c_211\">agronomy</subject>")
    f.write("<subject xml:lang=\"en-us\" subjectScheme=\"AGROVOC\" schemeURI=\"http://aims.fao.org/standards/agrovoc\" valueURI=\"http://aims.fao.org/aos/agrovoc/c_823\">barley</subject>")
    f.write("<subject xml:lang=\"en-us\">rothamsted</subject>")
    f.write("<subject xml:lang=\"en-us\">park Grass</subject>")
    f.write("<subject xml:lang=\"en-us\">broadbalk</subject>")
    f.write("<subject xml:lang=\"en-us\">classical experiments</subject>")
    f.write("<subject xml:lang=\"en-us\">long-term experiments</subject>")
    f.write("<subject xml:lang=\"en-us\">high field</subject>")
    f.write("<subject xml:lang=\"en-us\">alternate wheat and fallow</subject>")
    f.write("<subject xml:lang=\"en-us\">exhaustion land</subject>")
    f.write("<subject xml:lang=\"en-us\">wilderness experiments</subject>")
    f.write("<subject xml:lang=\"en-us\">garden clover</subject>")
    f.write("</subjects>")
    f.write("<contributors>")
    f.write("<contributor contributorType=\"Distributor\"><contributorName>Rothamsted Research</contributorName></contributor>")
    f.write("<contributor contributorType=\"HostingInstitution\"><contributorName>Rothamsted Research</contributorName></contributor>")
    f.write("<contributor contributorType=\"RightsHolder\"><contributorName>Lawes Agricultural Trust</contributorName></contributor>")
    f.write("<contributor contributorType=\"DataCurator\"><contributorName>E-RA Curator Team</contributorName><affiliation>Rothamsted Research</affiliation></contributor>")
    f.write("<contributor contributorType=\"ContactPerson\"><contributorName>E-RA Curator Team</contributorName><affiliation>Rothamsted Research</affiliation></contributor>")
    f.write("</contributors>")
    f.write("<dates>")
    f.write("<date dateType=\"available\">2017-01-01</date>")
    f.write("</dates>")
    f.write("<language>en-us</language>")
    f.write("<size>"+str(nofPages)+"</size>")
    f.write("<format>PDF</format>")
    f.write("<version>1.0</version>")
    f.write("<rightsList>")
    f.write("<rights rightsURI=\"http://creativecommons.org/licenses/by/4.0\">This work is licensed under a Creative Commons Attribution 4.0 International License</rights>")
    f.write("<rights>Copyright Lawes Agricultural Trust</rights>")
    f.write("</rightsList>")
    f.write("<description xml:lang=\"en-us\" descriptionType=\"Abstract\">Scanned and searchable PDF of "+bookTitle+".</description>")
    f.write("<geoLocations>")
    f.write("<geoLocation><geoLocationPlace>Rothamsted, Harpenden, UK</geoLocationPlace></geoLocation>")
    f.write("<geoLocation><geoLocationPlace>Woburn, UK</geoLocationPlace></geoLocation>")
    f.write("</geoLocations>")
    f.write("<fundingReferences>")
    f.write("<fundingReference>")
    f.write("<funderName>Biotechnology and Biological Sciences Research Council</funderName>")
    f.write("<funderIdentifier funderIdentifierType=\"Crossref Funder ID\">http://dx.doi.org/10.13039/501100000268</funderIdentifer>")
    f.write("</fundingReference>")
    f.write("<fundingReference>")
    f.write("<funderName>Lawes Agricultural Trust</funderName>")
    f.write("</fundingReference>")
    f.write("<fundingReferencess>")
    f.write("</resource>")
    
    f.close()
    fin = open(fname, "r")
    d = DataCiteMDSClient(
        username='',
        password='',
        prefix='',
        test_mode=True
    )

    # Set metadata for DOI
    d.metadata_post(fin)
#finally:
db.close()