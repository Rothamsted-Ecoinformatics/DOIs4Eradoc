'''
Created on 30th June 2017

@author: Richard Ostler
'''
import pymysql
import configparser
from PyPDF2 import PdfFileReader, PdfFileMerger
from FrontPager import FrontPage
from EradocData import EraDocumentData
from Bookmark import BookmarkData
from PdfMerger import bookmarksData

def getBookmarks(eraCursor, bookId):
    eraCursor.execute("select Rs.FID, Rs.Rtitle from Rs inner join Books on Rs.BID = Books.BookID where Rs.BID="+bookId+" order by Rs.BID,Rs.FID");
    bookmarks = [BookmarkData(row[0],row[1]) for row in eraCursor.fetchall()]
    return dict([(b.pageNumber, b.title) for b in bookmarks])

if __name__ == '__main__':
    
    bookId = input("Enter book ID: ")
    bookDir = input("Enter book directory (e.g. V:\\ResReport1938\\PDF): ")
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    # ERA database
    erahost = config['ERA_DATABASE']['host']
    erauser = config['ERA_DATABASE']['user']
    erapwd= config['ERA_DATABASE']['password']
    eradb = config['ERA_DATABASE']['db']
    
    eraCon = pymysql.connect(host=erahost,user=erauser,password=erapwd,db=eradb)
    
    eraCursor = eraCon.cursor()
    
    eraCursor.execute("select Books.bookid,booktitle,year,count(*) as nofPages from Books inner join Pages on Books.bookid = Pages.bookid where Books.bookid = "+bookId+" group by Books.bookid,booktitle,year order by year limit 1 ");
    data = eraCursor.fetchone()
    title = data[1]
    year = data[2]
    nofPages = data[3]
    docData = EraDocumentData(bookId,title,year,nofPages)
    
    # TODO: find somewhere more sensible to put these files?
    fpFileName = "D:\\"+bookId+"-fp.pdf"
    fpDoc = FrontPage(fpFileName, docData)
    fpDoc.createDocument()
    fpDoc.savePDF()
    
    # Get the list of book marks into a list then convert to a dictionary (not sure how to do this directly
    bookmarksData = getBookmarks(eraCursor, bookId)
    
    # Set-up the PDF file merger then add the covering page created earlier.
    merger = PdfFileMerger()
    merger.append(PdfFileReader(open("D:\\"+bookId+"-fp.pdf","rb")))
    
    # Use a query to get the pages for the book...
    eraCursor.execute("select Folders.FolderName, Pages.PagePDFName, Pages.PageVisibleName from Books inner join Folders on Books.BookFolderID = Folders.FolderID inner join Pages on Folders.FolderID = Pages.FolderID where Books.bookId = " + bookId + " order by Pages.Ordering")
    pages = eraCursor.fetchall()
    for pageRow in pages:
        
        thisPage = pageRow[2]
        # tests whether or not the current page should be bookmarked
        bookmark = bookmarksData.get(int(thisPage))  
        if (bookmark):
            merger.addBookmark(bookmark + "....."+str(thisPage), thisPage)
        merger.append(PdfFileReader(open("V:\\"+pageRow[0]+"\\PDF\\"+pageRow[1],"rb")))
        
    # TODO: Change this but for now dump the final merged PDF book to D:
    merger.write("d:\\book"+bookId+".pdf")
    merger.close()