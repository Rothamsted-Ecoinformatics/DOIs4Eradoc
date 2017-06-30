'''
Created on 30th June 2017

@author: Richard Ostler

Used to create a covering page for eRADoc PDFs. Data is provided by the docData class.
'''

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph
from reportlab.lib.colors import forestgreen
 

class FrontPage(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, fpFileName, docData):
        self.c = canvas.Canvas(fpFileName, pagesize=letter)
        self.styles = getSampleStyleSheet()
        self.width, self.height = letter
        self.docData  = docData
  
    #----------------------------------------------------------------------
    def createDocument(self):
        """"""
        voffset = 40
 
        # add a logo and size it
        logo = Image("D:\\logo.png")
        logo.drawHeight = 20*mm
        logo.drawWidth = 66*mm
        logo.wrapOn(self.c, self.width, self.height)
        logo.drawOn(self.c, *self.coord(100, 60, mm))
 
        # insert document title
        p = Paragraph(self.docData.title, self.styles["title"])
        p.wrapOn(self.c, self.width-90, self.height)
        p.drawOn(self.c, *self.coord(20, voffset+45, mm))
        
        styleWrapped = self.styles["Normal"]
        styleWrapped.wordWrap = "CJK"
        # insert document metadata
        widthAdjust=100
        p = Paragraph("Thank you for using eRADoc, a platform to publish electronic copies of the Rothamsted documents.", self.styles["Normal"])
        p.wrapOn(self.c, self.width-widthAdjust, self.height)
        p.drawOn(self.c, *self.coord(20, voffset+60, mm))
        
        p = Paragraph("This work is licensed under a Creative Commons Attribution 4.0 International License, Copyright Lawes Agricultural Trust.", styleWrapped)
        p.wrapOn(self.c, self.width-widthAdjust, self.height)
        p.drawOn(self.c, *self.coord(20, voffset+67, mm))
        
        p = Paragraph("Created by: <b>Rothamsted Experimental Station</b>.", self.styles["Normal"])
        p.wrapOn(self.c, self.width-widthAdjust, self.height)
        p.drawOn(self.c, *self.coord(20, voffset+74, mm))
        
        p = Paragraph("Published by: <b>Lawes Agricultural Trust</b>.", self.styles["Normal"])
        p.wrapOn(self.c, self.width-widthAdjust, self.height)
        p.drawOn(self.c, *self.coord(20, voffset+81, mm))
        
        citeStyle = self.styles["Normal"]
        citeStyle.borderColor=forestgreen
        citeStyle.borderWidth=1
        citeStyle.borderPadding=5
        citeStyle.borderRadius=2
        p = Paragraph("<b>Please Cite</b>: <i>Rothamsted Experimental Station</i> (%s): %s. Lawes Agricultural Trust. DOI:" % (self.docData.year, self.docData.title), citeStyle)
        
        # TODO: Include links to related DOIs / Documents. Will need this for articles.
        p.wrapOn(self.c, self.width-widthAdjust, self.height)
        p.drawOn(self.c, *self.coord(20, voffset+102, mm))
 
    #----------------------------------------------------------------------
    def coord(self, x, y, unit=1):
        """
        # http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
        Helper class to help position flowables in Canvas objects
        """
        x, y = x * unit, self.height -  y * unit
        return x, y    
 
    #----------------------------------------------------------------------
    def createParagraph(self, ptext, x, y, style=None):
        """"""
        if not style:
            style = self.styles["Normal"]
        p = Paragraph(ptext, style=style)
        p.wrapOn(self.c, self.width, self.height)
        p.drawOn(self.c, *self.coord(x, y, mm))
 
    #----------------------------------------------------------------------
    def savePDF(self):
        """"""
        self.c.save()   