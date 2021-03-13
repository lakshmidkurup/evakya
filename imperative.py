import xml.etree.ElementTree as ET
import random
import re
class type17:
    sname=""
    noundict=[]
    onounlist=[]
    eclass=""
    verb=""
    verbclass=""

    str1='D:\\evakya\\xml\\imppos.xml'
    str2='D:\\evakya\\xml\\impneg.xml'
    str3='D:\\evakya\\xml\\impneutral.xml'
    str4=random.choice([str1,str2,str3])
    tree=ET.parse(str4)
##    tree=ET.parse('D:\\evakya\\dataset\\impnumeric.xml')
##    tree=ET.parse('D:\\evakya\\dataset\\impmarry.xml')
    root = tree.getroot()
    def genverb(self):
        root = type17.tree.getroot()
        
        verblst=[]
        for i in root:
            #print(i.tag,i.attrib)
            if i.tag=="VERB":
                type17.eclass=i.attrib['ECLASS']
                
                if i.attrib['ECLASS']=="positive" or i.attrib['ECLASS']=="negative" or i.attrib['ECLASS']=="neutral" or i.attrib['ECLASS']=="numeric" or i.attrib['ECLASS']=="marryclass":
                    
                
                    with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                        for word in nd:                        
                            dh=word.split(':')
                        #print(dh)
                            if i.attrib['ECLASS']==dh[2]:
                                verblst.append(dh[1])
                    type17.verb=random.choice(verblst)
                    #print("verbis",type17.verb)
                    with open("D:\\evakya\\dataset\\tense.txt") as nd:
                        for word in nd:                        
                            dh=word.split(':')
                        #print(dh)
                            if type17.verb==dh[1]:
                                presentverb=dh[0]

        #print(presentverb)
        return(presentverb)
        
   
    def gendet(self):#----Avoid "the" for personified nouns
        root = type17.tree.getroot()       
        for i in root:
            
            #print(i.tag,i.attrib)
            if i.tag=="DET":
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        #print(dh)
                        if type17.verb==dh[1]:
                            type17.verbclass=dh[0]
##                    print("verbclass",type17.verbclass)
                if type17.verbclass=="personified":
                    det=" "
                else:    
                    det="the"
                #print(det)
                return(det)
           
    def genobjnoun(self):
        root=type17.tree.getroot()
        with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
            for word in nd:                        
                dh=word.split(':')
                if type17.verb==dh[1]:
                    verbclass=dh[0]
                    #print(verbclass)
        type17.onoun=""
        for i in root:  # ONOUN
            if i.tag=="ONOUN":
                
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if verbclass==dh[0]:
                           
                            type17.onounlist.append(dh[1])                            
        type17.onoun=random.choice(type17.onounlist)
        #print(type17.onoun)
        return(type17.onoun)
    def gensent(self):
        
        period="."
        verb=p1.genverb()
        onoun=""
        onoun=p1.genobjnoun()
        det=p1.gendet()
        if type17.eclass in ["positive","negative","neutral"]:
            sent=verb.capitalize()+" "+det+" "+onoun+period
            correctans=re.sub(' +', ' ', sent) 
            
        #--------------------unpunctuate-----------------------------------------------------------------
        punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        #--------------------------------tag unpunctuated text--------------------------------------------
        #Meet Alice,Win the match
           
        mylist=nopunct.split(" ")
        taglst=[]
        for i, element in enumerate(mylist):
                previous_element = mylist[i-1] if i > 0 else None
                current_element = element
                next_element = mylist[i+1] if i < len(mylist)-1 else None
                #print(previous_element, current_element, next_element)
                
                verb1=verb.capitalize() 
                if (current_element==verb1 and next_element==det) or (current_element==verb1 and next_element==onoun):
                        taglst.append(current_element)
                        taglst.append("<w>")        
                if (current_element==det and next_element==onoun):
                        taglst.append(current_element)
                        taglst.append("<w>")
               
    
                if next_element==None:
                        taglst.append(current_element)
                        taglst.append("<m>")
                   
           
        taggedsent="".join(taglst)
        category="fullstop"
        level="3"
        #print(correctans,nopunct,taggedsent,category,level)
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
                #print("id1:",row[0])
        id2=id1+1
                    #-----------------------------insert into database------------------------------------------------------------------------------------------------------------------   
        #mycursor.execute("insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category) values ( %d, %s, %s, %s, %s )")
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s,%s )', (id2,nopunct,correctans,taggedsent,category,level,1))
        mydb.commit()
        print(correctans,level)
        return(correctans,nopunct,taggedsent,category,level)
    



for i in range(0,3):
            
    p1=type17()
    p1.gensent()
    
    
#correctans,nopunct,taggedsent,category,level=p1.gensent()
