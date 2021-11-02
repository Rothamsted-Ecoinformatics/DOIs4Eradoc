'''
Created on 30 May 2017

@author: ostlerr
'''
from datacite import schema41
import sys
import getpass
from EraConnect import getDbConnection, getDataCiteClient
eraCon = getDbConnection()
cursor = eraCon.cursor()

#http://mysql1.rothamsted.ac.uk/phpmyadmin/import.php#PMAURL-3:sql.php?db=eradoc&table=Rs&server=1&target=&token=c9827285e632afa8d396e0e56dfd465c

bookId = 7
#try:
cursor.execute("select Rs.RUID, Rs.RTitle, Books.year, Rs.LID - Rs.FID as nofPages, Rs.RAuthors, Rs.BID, Books.bookTitle, Rs.FID, Rs.LID from Rs inner join Books on Rs.BID = Books.bookid where Rs.RUID = 39931 and Rs.needsDOI = 1");
data = cursor.fetchall()
for row in data:
    # Open a file named for the ID and collection.
    rId = row[0]
    rTitle = row[1]
    
    year = row[2]
    nofPages = row[3]
    authors = row[4]
    bookId = row[5]
    bookTitle = row[6]
    fid = row[7]
    lid = row[8]
    bookDoi = "10.23637/ERADOC-1-" + str(bookId)
    doi = "10.23637/ERADOC-1-" + str(rId)
    pages = str(nofPages) + " pages"
    abstract = "Scanned PDF of "+rTitle+ ", part of " + bookTitle;
    rTitle = rTitle + ", " + bookTitle
    curContents = eraCon.cursor()    
    curContents.execute("select RTitle, FID, RAuthors from Rs where bid = "+ str(bookId) +" order by FID");
    dataContents = curContents.fetchall()
    print(rTitle)
    
    subjects = [
            {'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41331872', 'subject' : 'rothamsted research'}
        ] 
    if rTitle.lower().find("yield") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_10176', 'subject' : 'crop yield'})
    if rTitle.lower().find("weather") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_4780', 'subject' : 'meteorological observations'})
#             {'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_10795', 'subject' : 'fertilizer application'},
#             {'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_8373', 'subject' : 'wheat'},
#             {'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_7156', 'subject' : 'soil'},
#             {'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_6662', 'subject' : 'crop rotation'},
#             {'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_8679', 'subject' : 'agricultural research'},
#             {'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_211', 'subject' : 'agronomy'},
#             {'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_823', 'subject' : 'barley'},
#             {'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_2784', 'subject' : 'fallowing'},
#             {'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_2810', 'subject' : 'farmyard manure'},
#             {'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_5195', 'subject' : 'nitrogen fertilizers'},
#             {'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41332378', 'subject' : 'rothamsted classical experiments'},
#   
    if rTitle.lower().find("broadbalk") > -1 :
        subjects.append(
#            {'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41331872', 'subject' : 'broadbalk long-term experiment'})
            {'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q7137747', 'subject' : 'park grass long-term experiment'})
#             {'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41530393', 'subject' : 'rothamsted long-term experiments'},
#             {'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41523123', 'subject' : 'hoosfield alternate wheat and fallow long-term experiment'},
#             {'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41528375', 'subject' : 'exhaustion land long-term experiment'},
#             {'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41528075', 'subject' : 'broadbalk wilderness experiment'},
#             {'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41528232', 'subject' : 'geescroft wilderness experiments'},
#             {'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41530125', 'subject' : 'agdell long-term experiment'},
#             {'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41528611', 'subject' : 'barnfield long-term experiment'},
#             {'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41528458', 'subject' : 'Garden clover long-term experiment'}
    if rTitle.lower().find("mangolds") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_4576', 'subject' : 'mangolds'})
    if (rTitle.lower().find("residu") > -1 and rTitle.lower().find("value") > -1) or rTitle.lower().find("long-term effects") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_24408', 'subject' : 'residual effects'})
    if rTitle.lower().find("botanical composition") > -1 or rTitle.lower().find("composition") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_15945', 'subject' : 'botanical composition'})
    if rTitle.lower().find("hay") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_3508', 'subject' : 'hay'})
    if rTitle.lower().find("oats") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_5287', 'subject' : 'oats'})
    if rTitle.lower().find("swedes") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_6713', 'subject' : 'swedes'})
    if rTitle.lower().find("green manuring") > -1 or rTitle.lower().find("green manures") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_3375', 'subject' : 'green manures'})
    if rTitle.lower().find("soil management") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_7176', 'subject' : 'soil management'})
    if rTitle.lower().find("potatoes") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_13551', 'subject' : 'potatoes'})
    if rTitle.lower().find("plant nutrition") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_16379', 'subject' : 'plant nutrition'})
    if rTitle.lower().find("entomology") > -1 or rTitle.lower().find("entomological") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_2588', 'subject' : 'entomology'})
    if rTitle.lower().find("mycology") > -1 or rTitle.lower().find("mycological") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_5019', 'subject' : 'mycology'})
    if rTitle.lower().find("stubble cleaning") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_7472', 'subject' : 'stubble cleaning'})
    if rTitle.lower().find("efficiency of labour") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_4130', 'subject' : 'labour efficiency'})
    if rTitle.lower().find("tractor") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_7847', 'subject' : 'tractors'})
    if rTitle.lower().find("apicultur") > -1 or rTitle.lower().find(" bee") > -1 or rTitle.lower().find("honey") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_529', 'subject' : 'apiculture'})
    if rTitle.lower().find("soil acidity") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_34901', 'subject' : 'soil acidity'})                 
    if rTitle.lower().find("soil") > -1 and rTitle.lower().find("cultivation") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_7771', 'subject' : 'soil cultivation'})
    if rTitle.lower().find("woburn") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41530491', 'subject' : 'woburn experimental farm'})
    if rTitle.lower().find("costs of Ploughing") > -1 or rTitle.lower().find("valuation") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_6202', 'subject' : 'production costs'})
    if rTitle.lower().find("insecticides") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_3887', 'subject' : 'insecticides'})
    if rTitle.lower().find("leadon") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q26471046', 'subject' : 'leadon court farm'})
    if rTitle.lower().find("liming") > -1 or rTitle.lower().find(" lime") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_25206', 'subject' : 'liming'})
    if rTitle.lower().find("basic slag") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_837', 'subject' : 'basic slag'})
    if rTitle.lower().find("potash") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_6138', 'subject' : 'potash fertilizers'})
    if rTitle.lower().find("pest") > -1 and rTitle.lower().find("control") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_5726', 'subject' : 'pest control'})
    if rTitle.lower().find("disease") > -1 and rTitle.lower().find("control") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_2327', 'subject' : 'disease control'})
    if rTitle.lower().find("leguminous") > -1 or rTitle.lower().find("legumes") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_4255', 'subject' : 'legumes'})
    if rTitle.lower().find("soil micro-organisms") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_36167', 'subject' : 'soil microorganisms'})
    if rTitle.lower().find("malting barley") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_25485', 'subject' : 'malting barley'})
    if rTitle.lower().find("sewage") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_7008', 'subject' : 'sewage'})
    if rTitle.lower().find("resistance") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_2328', 'subject' : 'disease resistance'})
    if rTitle.lower().find("lucerne") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_4693', 'subject' : 'lucerne'})
    if rTitle.lower().find("cellulose") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_1423', 'subject' : 'cellulose'})
    if rTitle.lower().find("sugar beet") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_7499', 'subject' : 'sugarbeet'})
    if rTitle.lower().find("grassland") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_3366', 'subject' : 'grasslands'})
    if rTitle.lower().find("geolog") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_3232', 'subject' : 'geology'})
    if rTitle.lower().find("fungus") > -1 and rTitle.lower().find("disease") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_11042', 'subject' : 'fungal diseases'})
    if rTitle.lower().find("bacteria") > -1 and rTitle.lower().find("disease") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_770', 'subject' : 'bacterial diseases'})
    if rTitle.lower().find("virus") > -1 and rTitle.lower().find("disease") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_8260', 'subject' : 'viral diseases'})
    if rTitle.lower().find("survey") > -1 and rTitle.lower().find("pest") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_32767', 'subject' : 'pest surveys'})
    if rTitle.lower().find("survey") > -1 and rTitle.lower().find("disease") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_28665', 'subject' : 'disease surveys'})
    if rTitle.lower().find("fodder crops") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_2829', 'subject' : 'fodder crops'})
    if rTitle.lower().find("soil") > -1 and rTitle.lower().find("chemi") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_7161', 'subject' : 'soil chemistry'})
    if rTitle.lower().find("effluent") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_24455', 'subject' : 'effluents'})
    if rTitle.lower().find("husbandry") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_8532', 'subject' : 'animal husbandry'})
    if ((rTitle.lower().find("minor") > -1 or rTitle.lower().find("small") > -1) and rTitle.lower().find("elements") > -1) or (rTitle.lower().find("micro") > -1 and rTitle.lower().find("nutrient") > -1):
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_28665', 'subject' : 'micronutrients'})
    if rTitle.lower().find("crop") > -1 and rTitle.lower().find("forecasting") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_8486', 'subject' : 'yield forecasting'})
    if rTitle.lower().find("kale") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_4070', 'subject' : 'kales'})
    if rTitle.lower().find("beans") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_331566', 'subject' : 'beans'})
    if rTitle.lower().find("maize") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_12332', 'subject' : 'maize'})
    if rTitle.lower().find("soya") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_14477', 'subject' : 'soybeans'})
    if rTitle.lower().find("pyrethr") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_6383', 'subject' : 'pyrethrins'})
    if rTitle.lower().find("earthworms") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_29109', 'subject' : 'earthworms'})
    if rTitle.lower().find("slugs") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_7111', 'subject' : 'slugs'})   
    if rTitle.lower().find("take-all") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_24640', 'subject' : 'take all fungus'})
    if rTitle.lower().find("survey") > -1 and rTitle.lower().find("soil") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_16551', 'subject' : 'soil surveys'})
    if rTitle.lower().find("forest nurseries") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_34830', 'subject' : 'forest nurseries'})
    if rTitle.lower().find("eelworm") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_5112', 'subject' : 'eelworms'})
    if rTitle.lower().find("yellow") >-1 and rTitle.lower().find("virus") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'GACS', 'schemeURI' : 'http://id.agrisemantics.org/gacs', 'valueURI' : 'http://id.agrisemantics.org/gacs/C25917', 'subject' : 'beet yellows virus group'})
    if rTitle.lower().find("ddt") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_33467', 'subject' : 'DDT'})
    if rTitle.lower().find("tropical soils") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_7978', 'subject' : 'tropical soils'})
    if rTitle.lower().find("nutrient uptake") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_5273', 'subject' : 'nutrient uptake'})
    if rTitle.lower().find("clay minerals") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_15836', 'subject' : 'clay minerals'})
    if rTitle.lower().find("nematode") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_5112', 'subject' : 'nematodes'})
    if rTitle.lower().find("aphid") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_30757', 'subject' : 'aphids'})
    if rTitle.lower().find("dispersal") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'GACS', 'schemeURI' : 'http://id.agrisemantics.org/gacs', 'valueURI' : 'http://id.agrisemantics.org/gacs/C16929', 'subject' : 'dispersal behaviour'})
    if rTitle.lower().find("soil structure") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_7196', 'subject' : 'soil structure'})
    if rTitle.lower().find("thiaminase") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_34132', 'subject' : 'thiaminase'})
    if rTitle.lower().find("seed dressing") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_26820', 'subject' : 'seed dressing'})
    if rTitle.lower().find("simazine") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_31491', 'subject' : 'simazine'})
    if rTitle.lower().find("dunholme field station") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41594347', 'subject' : 'Dunholme field station'})
    if rTitle.lower().find("woburn") > -1 and rTitle.lower().find("green") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41619215', 'subject' : 'Woburn green manuring experiment'})
    if rTitle.lower().find("woburn") > -1 and rTitle.lower().find("organic") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41619109', 'subject' : 'Woburn organic manuring experiment'})
    if rTitle.lower().find("broom") > -1 and rTitle.lower().find("barn") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41619546', 'subject' : 'Broom''s barn research centre'})
    if rTitle.lower().find("market") > -1 and rTitle.lower().find("garden") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41618401', 'subject' : 'Woburn market garden experiment'})
    if rTitle.lower().find("wild oat") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'GACS', 'schemeURI' : 'http://id.agrisemantics.org/gacs', 'valueURI' : 'http://id.agrisemantics.org/gacs/C11835', 'subject' : 'wild oats'})
    if rTitle.lower().find("saxmundham") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41621379', 'subject' : 'saxmundham experimental station'})
    if rTitle.lower().find("Heterodera rostochiensis") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_31040', 'subject' : 'Heterodera rostochiensis'}) # Potato cyst nematode same as Globodera
    if rTitle.lower().find("sticky") > -1 and rTitle.lower().find("traps") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_37305', 'subject' : 'sticky traps'})
    if rTitle.lower().find("rothamsted") > -1 and rTitle.lower().find("ley") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41621981', 'subject' : 'Rothamsted ley-arable rotation experiment'})
    if rTitle.lower().find("soil ph") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_34901', 'subject' : 'soil pH'})
    if rTitle.lower().find("chalk") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_4342', 'subject' : 'chalk'})
    if rTitle.lower().find("migrant") > -1 and rTitle.lower().find("pest") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_32927', 'subject' : 'migratory pests'})
    if rTitle.lower().find("lepidoptera") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_4268', 'subject' : 'Lepidoptera'})
    if rTitle.lower().find("population") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_6111', 'subject' : 'population dynamics'})
    if rTitle.lower().find("light traps") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_4324', 'subject' : 'Light traps'})
    if rTitle.lower().find("red clover") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_7917', 'subject' : 'Red clover'})
    if rTitle.lower().find("ditylenchus dipsaci") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_30986', 'subject' : 'Ditylenchus dipsaci'})
    if rTitle.lower().find("neuroptera") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_30986', 'subject' : 'Neuroptera'})    
    if rTitle.lower().find("phenology") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_5774', 'subject' : 'phenology'})    
    if rTitle.lower().find("phosphorous") > -1 or rTitle.lower().find(" p ") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_5804', 'subject' : 'phosphorous'})    
    if rTitle.lower().find("nitrogen") > -1 or rTitle.lower().find(" n ") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_5192', 'subject' : 'nitrogen'})    
    if rTitle.lower().find("potassium") > -1 or rTitle.lower().find(" k ") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_6139', 'subject' : 'potassium'})
    if rTitle.lower().find("longidorus leptocephalus") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'NCBITAXON', 'schemeURI' : 'http://purl.bioontology.org/ontology/NCBITAXON', 'valueURI' : 'http://purl.bioontology.org/ontology/NCBITAXON/286745', 'subject' : 'Longidorus leptocephalus'})    
    if rTitle.lower().find("nitrogen fix") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_5196', 'subject' : 'Nitrogen fixation'})    
    if rTitle.lower().find("rhizosphere") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_6569', 'subject' : 'rhiszosphere'})    
    if rTitle.lower().find("vesicular") > -1 and rTitle.lower().find("arbuscular ") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_24415', 'subject' : 'Vesicular arbuscular mycorrhizae'})    
    if rTitle.lower().find("superphosphate") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_7521', 'subject' : 'superphosphate'})    
    if rTitle.lower().find("formalin") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_34833', 'subject' : 'formalin'})    
    if rTitle.lower().find("magnesium") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_4517', 'subject' : 'magnesium'})    
    if rTitle.lower().find("sodium") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_7145', 'subject' : 'sodium'})    
    if rTitle.lower().find("water use") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_36790', 'subject' : 'water use efficiency'})    
    if rTitle.lower().find("nutrient balance") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_35711', 'subject' : 'nutrient balance (plants)'})    
    if rTitle.lower().find("conifers") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_330325', 'subject' : 'conifers'})    
    if rTitle.lower().find("stackyard") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'wikidata', 'schemeURI' : 'http://www.wikidata.org/entity', 'valueURI' : 'http://www.wikidata.org/entity/Q41627647', 'subject' : 'Stackyard experimental field'})
    if rTitle.lower().find("NPK fertilizers") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_5250', 'subject' : 'NPK fertilizers'})    
    if rTitle.lower().find("soil organic matter") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_35657', 'subject' : 'soil organic matter'})    
    if rTitle.lower().find("nitrogen balance") > -1 :
        subjects.append({'lang' : 'en', 'subjectScheme' : 'GACS', 'schemeURI' : 'http://id.agrisemantics.org/gacs', 'valueURI' : 'http://id.agrisemantics.org/gacs/C8736', 'subject' : 'nitrogen balance'})
    if rTitle.lower().find("honey") > -1 and rTitle.lower().find("bees") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_3654', 'subject' : 'honey bees'})    
    if rTitle.lower().find("poisoning") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_6051', 'subject' : 'poisoning'})    
    if rTitle.lower().find("rhizobium") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_6563', 'subject' : 'rhizobium'})    
    if rTitle.lower().find("leys") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_16189', 'subject' : 'leys'})    
    if rTitle.lower().find("inoculation") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_3879', 'subject' : 'inoculation'})    
    # new
    if rTitle.lower().find("weed") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_8347', 'subject' : 'weeds'})    
    if rTitle.lower().find("irrigation") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_3954', 'subject' : 'irrigation'})    
    if rTitle.lower().find("quinone") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_6412', 'subject' : 'quinones'})    
    if rTitle.lower().find("pollination") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_6073', 'subject' : 'pollination'})    
    if rTitle.lower().find("root rot") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_16033', 'subject' : 'root rots'})    
    if rTitle.lower().find("soil fumigation") > -1:
        subjects.append({'lang' : 'en', 'subjectScheme' : 'AGROVOC', 'schemeURI' : 'http://aims.fao.org/standards/agrovoc', 'valueURI' : 'http://aims.fao.org/aos/agrovoc/c_6073', 'subject' : 'soil fumigation'})    
    
        
    #make subjects unique
    subjectsu = list({v['subject']:v for v in subjects}.values())
    data = {
        'identifier' : {
            'identifier' : doi,
            'identifierType' : 'DOI'
        },
        'creators' : [
            {'creatorName' : authors}
        ],
        'titles' : [
            {'title' : rTitle}
        ],
        'publisher' : 'Lawes Agricultural Trust',
        'publicationYear' : year,
        'resourceType': {'resourceTypeGeneral' : 'Text'},
        'subjects' : subjectsu,
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
        'language' : 'en',        
        'version' : '1.0',
        'sizes' : [
            pages
        ],
        'formats' : [
            'appplication/PDF'
        ],
        'rightsList' : [
            {'rightsURI' : 'http://creativecommons.org/licenses/by/4.0', 'rights' : 'This work is licensed under a Creative Commons Attribution 4.0 International License'},
            {'rights' : '@Copyright Lawes Agricultural Trust Ltd'}
        ],
        'descriptions' : [
            {'lang' : 'en', 'descriptionType' : 'Abstract', 'description' : abstract}
        ],
        'geoLocations' : [
            {'geoLocationPlace' : 'Rothamsted Research, Harpenden, UK'}
        ],
        'relatedIdentifiers' : [
            {'relatedIdentifier' : bookDoi, 'relatedIdentifierType' : 'DOI', 'relationType' : 'IsPartOf'}
        ],
        'fundingReferences' : [
            {'funderName' : 'Biotechnology and Biological Sciences Research Council', 
            'funderIdentifier' : {
                'funderIdentifier' : 'http://dx.doi.org/10.13039/501100000268', 'funderIdentifierType' : 'Crossref Funder ID'
            }},
            {'funderName' : 'Lawes Agricultural Trust'}
        ]
    }
   
    assert schema41.validate(data)
    #print(schema40.validate(data))
    doc = schema41.tostring(data)
    print(doc)
    
    try:
        prefix = ""
        d = getDataCiteClient()
        d.metadata_post(schema41.tostring(data))
        print("do url")
        iyear = int(year)-1
        doiurl = "http://www.era.rothamsted.ac.uk/eradoc/article/ResReport"+ str(iyear) + "-" + str(fid) + "-" + str(lid)
        print(doiurl)
        d.doi_post(doi,doiurl)
        xname = "D:/doi_out/ERADOC-1-" + str(rId) + ".xml"
        jname = "D:/doi_out/ERADOC-1-" + str(rId) + ".json"
        fxname = open(xname,'w+')
        fxname.write(doc)
        fxname.close()
#         fjname = open(jname,'w+')
#         fjname.write(data)
#         fjname.close()
        sql = "insert into RaDOIs (addedBy, RUID, DOI, version) values ('" + getpass.getuser() + "'," + str(rId) + ",'https://doi.org/" + doi + "',1)"
        print (sql)
        curIns = eraCon.cursor()
        curIns.execute(sql)
        eraCon.commit()
        print('done')
    except:
        print("Unexpected error:", sys.exc_info()[0])

    #print(datacite.schema41.validate(fin))
    # Set metadata for DOI
    
#finally:
#db.close()