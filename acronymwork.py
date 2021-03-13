import xml.etree.ElementTree as ET
import random
import re
from abbreviation import abbr
from abbreviation import acrstate

class acronymwork:
    vclass=""
    verb=""
    stype=""
    tree = ET.parse('D:\\evakya\\xml\\acronym.xml')
    snname=""
    onoun=""
    noundict=[]
    onounlst=[]
    root=tree.getroot()
    def generatesubject(self):
                
        for i in acronymwork.root:
            #print("snoun",i.tag)
            if i.tag=="SNOUN":
                
                if i.attrib['TYPE']=="personified":
                

                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                acronymwork.noundict.append(dh[1])

                            
                    acronymwork.snname=random.choice(acronymwork.noundict)
                        
                    return(acronymwork.snname)
    def genverb(self):
        for i in acronymwork.root:
            verblst=[]
            if i.tag=="VERB":
                acronymwork.vclass=i.attrib["VCLASS"]
##                #print("vclass",abbr.vclass)
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        ##print(dh)
                        if acronymwork.vclass==dh[0]:
                            verblst.append(dh[1])
                verb=random.choice(verblst)
                #print("verb",verb)
                with open("D:\\evakya\\dataset\\preposition.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                    
                        if verb==dh[1]:
                            prep=dh[0]
                    return(verb,prep)

    def genonoun(self):
        for i in acronymwork.root:
            #print("onoun",i.tag)
            acronymwork.onoun=""
            if i.tag=="ONOUN":
                with open("D:\\evakya\\dataset\\abbreviations.txt") as nd:
                
                     for word in nd:
                        dh=word.split(':')
                        ##print(dh)
                        if acronymwork.vclass==dh[0]:
                           
                            acronymwork.onounlst.append(dh[1])
                            
            acronymwork.onoun=random.choice(acronymwork.onounlst)
            print("onoun",acronymwork.onoun)
            
            return(acronymwork.onoun)                       
            
    def acronymperiod(self):
        

        
        verb,prep=p1.genverb()
        snname=p1.generatesubject()
        #print("snname",snname)
        onoun=p1.genonoun()
        with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                
            for word in nd:
                dh=word.split(':')
                
                if snname==dh[1]:
                    sex=dh[4]
        #print("sex",sex)
        if sex=="M":
            title=['Mr.','Capt.','Major.','Bro.']
        elif sex=="F":
            title=['Mrs.','Miss.','Sr.']
        fullstop="."
        snname1=""
        snname1=random.choice(title)+" "+snname
        result=snname1+" "+verb+" "+prep+" "+onoun+fullstop
        result = result.strip() 
        while '  ' in result:
            result = result.replace('  ', ' ')
        
               
        correctans=result     
       
        #--------------------unpunctuate-----------------------------------------------------------------
        punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        #--------------------------------tag unpunctuated text--------------------------------------------
        #Dr.John works in TCS.
        title=['Mr','Capt','Major','Bro','Mrs','Miss','Sr']   
        mylist=nopunct.split(" ")
        taglst=[]
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            #print(previous_element, current_element, next_element)
            
            if current_element in title and next_element==snname:
                taglst.append(current_element)
                taglst.append("<m>")
               
            if current_element==snname and next_element==verb:
                taglst.append(current_element)
                taglst.append("<w>")
            if(current_element==verb and next_element==onoun):
                taglst.append(current_element)
                taglst.append("<w>")
            if(current_element==verb and next_element==prep):
                taglst.append(current_element)
                taglst.append("<w>")
            if(current_element==prep and next_element==onoun):
                taglst.append(current_element)
                taglst.append("<w>")
            if(current_element==onoun and next_element==None):
                res='<w>'.join(onoun[i:i + 1] for i in range(0, len(onoun), 1))
                taglst.append(res)
                taglst.append("<m>")
        taggedsent="".join(taglst)
        category="fullstop"
        level="5"
        #print(correctans,nopunct,taggedsent,category,level)
       
        print(taggedsent)
        return(correctans,nopunct,taggedsent,category,level)


for i in range(1,3):
        p1=acronymwork()
        correctans,nopunct,taggedsent,category,level=p1.acronymperiod()
        
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
                print("id1:",row[0])
        id2=id1+1
                

        #-----------------------------insert into database------------------------------------------------------------------------------------------------------------------   
       
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,correctans,taggedsent,category,level,1))
        mydb.commit()

