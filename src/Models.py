'''
Created on 2 Nov 2017

@author: ostlerr
'''
from datacite import schema40
import sys
import getpass
from EraConnect import getDbConnection, getDataCiteClient

doi = "10.23637/model-SIFT-1-0"
    
    subjects = [
            {'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_7156', 'subject' : 'soil'},
            {'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41331872', 'subject' : 'rothamsted research'},
            {'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41332378', 'subject' : 'rothamsted classical experiments'},
            {'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41530393', 'subject' : 'rothamsted long-term experiments'}
            
        ]
    
        
    if len(issn) > 0: 
        altId.append({'relatedIdentifier' : issn, 'alternateIdentifierType' : 'ISBN'})
        
    locations = []
    data = {
        'identifier' : {
            'identifier' : doi,
            'identifierType' : 'DOI'
        },
        'creators' : [
            {'Creator' : {
                'creatorName' : 'Dr Simon Pulley',
                'givenName': 'Simon',
                'familyName': 'Pully',
                'affiliation': 'Sustainable Agriculture Sciences Department, Rothamsted Research, North Wyke, Okehampton EX20 2SB, UK'
            }},
            {'Creator' : {
                'creatorName' : 'Prof. Adrian L. Collins',
                'givenName': 'Adrian L',
                'familyName': 'Collins',
                'nameIdentifier': {
                    'nameIdentifierScheme': 'ORCID',
                    'schemeURI': 'http://orcid.org/0000-0001-8790-8473'
                },
                'affiliation': 'Sustainable Agriculture Sciences Department, Rothamsted Research, North Wyke, Okehampton EX20 2SB, UK'
            }}
        ],
        'titles' : [
            {'title' : 'SIFT: SedIment Fingerprinting Tool'}
        ],
        'publisher' : 'Rothamsted Research',
        'publicationYear' : '2018',
        'resourceType': {'resourceTypeGeneral' : 'Model'},
        'subjects' : subjects,
        'contributors' : [
            {'contributorType' : 'Distributor', 'contributorName' : 'Rothamsted Research'},
            {'contributorType' : 'HostingInstitution', 'contributorName' : 'Rothamsted Research'},
            {'contributorType' : 'RightsHolder', 'contributorName' : 'Lawes Agricultural Trust'},
            {'contributorType' : 'DataCurator', 'contributorName' : 'E-RA Curator Team'},
            {'contributorType' : 'ContactPerson', 'contributorName' : 'E-RA Curator Team'}
        ],
        'dates' : [
            {'date' : year, 'dateType' : 'Created'}
        ],
        'alternateIdentifiers': altId, 
        'language' : 'en',        
        'version' : '1.0',
        'formats' : [
            'R Shiny application'
        ],
        'rightsList' : [
            {'rightsURI' : 'https://www.apache.org/licenses/LICENSE-2.0', 'rights' : 'This work is licensed under Apache 2.0 Software Licence'},
            {'rights' : '@Copyright Rothamsted Research Ltd 2018'}
        ],
        'descriptions' : [
            {'lang' : 'en', 'descriptionType' : 'Abstract', 'description' : 'A comprehensive software tool with a user-friendly GUI to walk any researcher or catchment manager through every step of a sediment source fingerprinting data analysis procedure. The tool is programmed using R and uses Shiny by RStudio for the user interface.'},
        ],
        'fundingReferences' : [
            {'funderName' : 'Biotechnology and Biological Sciences Research Council', 
            'funderIdentifier' : {
                'funderIdentifier' : 'http://dx.doi.org/10.13039/501100000268', 'funderIdentifierType' : 'Crossref Funder ID'
            }},
            {'funderName' : 'Lawes Agricultural Trust'}
        ]
    }
    print(schema40.tostring(data))
    assert schema40.validate(data)
    
    doc = schema40.tostring(data)
    print(doc)
    
    try:
        d = getDataCiteClient()
        d.metadata_post(schema40.tostring(data))
        d.doi_post(doi, "http://www.era.rothamsted.ac.uk/eradoc/book/"+str(bookId))
        xname = "D:/doi_out/ERADOC-1-" + str(bookId1) + ".xml"
        jname = "D:/doi_out/ERADOC-1-" + str(bookId1) + ".json"
        fxname = open(xname,'w+')
        fxname.write(doc)
        fxname.close()
        
        sql = "insert into BookDOIs (addedBy, bookID, DOI, Version) values ('" + getpass.getuser() + "'," + str(bookId) + ",'https://doi.org/" + doi + "',1)"
        print (sql)
        curIns = eraCon.cursor()
        curIns.execute("insert into BookDOIs (addedBy, bookID, DOI, Version) values ('" + getpass.getuser() + "'," + str(bookId) + ",'https://doi.org/" + doi + "',1)")
        eraCon.commit()
        print('done')
    except:
        print("Unexpected error:", sys.exc_info()[0])

#finally:
#db.close()