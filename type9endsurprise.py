import xml.etree.ElementTree as ET
import random
import re

class type9end:
    tree = ET.parse('D:\\evakya\\xml\\type9endsurprise.xml')
    conj=""
    noundict=[]
    snname=""
    spronoun=""
    verb=""
    verb1=""
    helpverb=""
    eml=[]
    em=""
    onounlst=[]
    onoun=""
    verbclass=""
    det=""
    def genconj(self):
        root = type9end.tree.getroot()
        
        for i in root:
            #print(i.tag)
            if i.tag=="CONJ":
                conj=i.attrib['NAME']
                #print(conj)
                return(conj)

    def gensnoun(self):
        root = type9end.tree.getroot()      
        for i in root:
            #print(i.tag)
            if i.tag=="SNOUN" and i.attrib['CHOICE']=="1" and i.attrib['TYPE']=="personified":
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if i.attrib['TYPE'] == dh[0]:
                            type9end.noundict.append(dh[1])
                            #print(type9end.noundict)
                type9end.snname=random.choice(type9end.noundict)
##                print(type9end.snname)
         
            if i.tag=="SNOUN" and i.attrib['CHOICE']=="1" and i.attrib['TYPE']=="personified":
                
                if type9end.snname in ["Mary","Alice"]:
                    type9end.spronoun="she"
                elif type9end.snname in ["James","John"]:
                    type9end.spronoun="he"    
                else:
                    type9end.spronoun="it"
                    
                            
        from random import choice
        a=choice((type9end.snname,type9end.spronoun))       
        #print(a)
        return(a)
    
    def genverb(self):
##        import nltk
##        from nltk.stem import PorterStemmer
        root = type9end.tree.getroot()
        verblst=[]
        
        for i in root:
            #print(i.tag)
            if i.tag=="VERB" and i.attrib['ECLASS']=="neutral":
                type9end.verbclass=i.attrib['ECLASS']
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if i.attrib['ECLASS']==dh[2]:
                            verblst.append(dh[1])
                    type9end.verb=random.choice(verblst)
                    #print(type9end.verb)
      
                hverb=i.attrib['HVERB']
                neg=i.attrib['NEGATION']
                hverbs=hverb+" "+neg
                hverbs1=hverb+"'nt"
        from random import choice
        type9end.helpverb=choice((hverbs,hverbs1))
        with open("D:\\evakya\\dataset\\tense.txt") as nd:
            for word in nd:
                dh=word.split(':')
                if type9end.verb==dh[1]:
                    type9end.verb1=dh[0]
        
##        ps =PorterStemmer()
##        type9end.verb1=ps.stem(type9end.verb)
    
        vp=type9end.helpverb+" "+type9end.verb1
        #print(vp)
        return(type9end.helpverb,type9end.verb1)
    def geninterjection(self):
       
        root = type9end.tree.getroot()
        for i in root:
           #print(i.tag,i.attrib)
           if i.tag=="INTERJECTION":
               with open("D:\\evakya\\dataset\\interjections.txt") as nd:
                   for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if i.attrib['EMOTION']==dh[1]:
                            type9end.eml.append(dh[2])
                            
        type9end.em=random.choice(type9end.eml)
        #print(type9end.em)
        return(type9end.em)
        
    def genobjnoun(self):
        root = type9end.tree.getroot()
        with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
            for word in nd:                        
                dh=word.split(':')
               # print(dh)
                if type9end.verb==dh[1]:
                    verbclass=dh[0]
                   
        for i in root:  # ONOUN
            if i.tag=="ONOUN":
                type9end.onounlst=[]
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        
                        if verbclass==dh[0]:
                            print("verbclass",verbclass)
                            type9end.onounlst.append(dh[1])
                           
                type9end.onoun=random.choice(type9end.onounlst)
                #print(type9end.onoun)
                
                if type9end.verbclass=="neutral":
                    i.attrib['DET']="the"
                    type9end.det=i.attrib['DET']
        return(type9end.det,type9end.onoun)       
    def type9endsentence(self):
        p1=type9end()
        conj=p1.genconj()
        snoun=p1.gensnoun()
        helpverb,verb=p1.genverb()
        interjn=p1.geninterjection()
        det,objnoun=p1.genobjnoun()
        excl="!"
        comma=","
        questionmark="!"
        period="."
        if helpverb=="could not":
            hv=helpverb.split(" ")
            helpingverb=hv[0]+" "+hv[1]
            npuncthverb=hv[0]+"<w>"+hv[1]
        else:
            helpingverb=helpverb
            npuncthverb=helpverb
        #print(helpingverb)
        sent=conj+comma+" "+snoun+" "+helpingverb+" "+verb+" "+det+" "+objnoun+comma+" "+interjn+questionmark
        taggedsent=conj+"<m>"+snoun+"<w>"+npuncthverb+"<w>"+verb+"<w>"+det+"<w>"+objnoun+"<m>"+interjn+"<m>"
        nopunct=conj+" "+snoun+" "+helpingverb+" "+verb+" "+det+" "+objnoun+" "+interjn
        #print(sent,taggedsent,nopunct)
        return(sent,taggedsent,nopunct)

for i in range(0,5):        
    p1=type9end()
    sent,taggedsent,nopunct=p1.type9endsentence()
    
#------------------- -unpunctuate-----------------------------------------------------------------
    punctuations = '''!()[]{};:'"\,<>.?@#$%^&*_~'''
    nopunct=""
    for char in sent:
        if char not in punctuations:
            nopunct = nopunct + char
  
    import mysql.connector
    
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="rohith@123",
            database="pythonlogin"
    )
    mycursor = mydb.cursor()

    mycursor.execute("select max(exerciseid) from sentencedb")  
    rows = mycursor.fetchall()
    for row in rows:
            id1=0
            id1=row[0]
            #####print("id1:",row[0])
    id2=id1+1
    category="exclamation"
    level=3
    
    mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))
    mydb.commit() 
