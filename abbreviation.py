import xml.etree.ElementTree as ET
import random
import re

class abbr:
    vclass=""
    verb=""
    stype=""
    tree = ET.parse('D:\\evakya\\xml\\acronymstate.xml')
    root=tree.getroot()
    
    def gendet(self):

        for i in abbr.root:
            
            if i.tag=="DET":
                det=i.attrib['NAME']
            
            return(det)

    def gensnoun(self):
        for i in abbr.root:
           
            if i.tag=="SNOUN":
                abbr.stype=i.attrib['TYPE']
                abbrlst1=[]
                abbrlst2=[]
                abbr.stype=i.attrib['TYPE']
                if abbr.stype=="acronym" or abbr.stype=="state":
                    with open("D:\\evakya\\dataset\\abbreviations.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if abbr.stype==dh[0]:
                                abbrlst1.append(dh[1])
                                abbrlst2.append(dh[2])
##                    #print(abbrlst1)
##                    #print(abbrlst2)
                j=0
                j=random.randint(1,10)
                
                short=abbrlst1[j]
                expanded=abbrlst2[j]
                
                return(abbr.stype,short,expanded)
            
    def genverbphrase(self):
        for i in abbr.root[2]:
##            #print(i.tag)
            if i.tag=="VERB":
                abbr.vclass=i.attrib["VCLASS"]
##                #print("vclass",abbr.vclass)
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        ##print(dh)
                        if abbr.vclass==dh[0]:
                            abbr.verb=dh[1]
                            
                
        with open("D:\\evakya\\dataset\\preposition.txt") as nd:
            for word in nd:
                dh=word.split(':')
                if abbr.verb==dh[1]:
                    prep=dh[0]
##        #print("prep",prep)
        return(abbr.verb, prep)
    
    def gensent(self):
        period="."
        p1=abbr()
        verb,prep=p1.genverbphrase()
        a1,short,exp=p1.gensnoun()
        det=p1.gendet()
        subject="acronym"
        correctans=det+" "+a1+" "+short+" "+verb+"s"+" "+prep+" "+exp+period
        correctans = correctans.strip() 
        while '  ' in correctans:
            correctans = correctans.replace('  ', ' ')

       
        #--------------------unpunctuate-----------------------------------------------------------------
        punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        #--------------------------------tag unpunctuated text--------------------------------------------
        #print("nopunct",nopunct)
        #title=['Mr','Capt','Major','Bro','Mrs','Miss','Sr']   
        mylist=nopunct.split(" ")
        taglst=[]
        exp1=exp.split(" ")
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            #print(previous_element, current_element, next_element)
            
##            if current_element in title and next_element==snname:
##                taglst.append(current_element)
##                taglst.append("<m>")
            verb2=verb+"s"
            if(current_element==det and next_element==subject):
                taglst.append(current_element)
                taglst.append("<w>")
            if(current_element==subject and next_element==short):
                taglst.append(current_element)
                taglst.append("<w>")    
            if(current_element==short and next_element==verb2):
                res='<w>'.join(short[i:i + 1] for i in range(0, len(short), 1))
                taglst.append(res)
                
                taglst.append("<w>") 
            if(current_element==verb2 and next_element==prep):
                taglst.append(current_element)
                taglst.append("<w>")
            if(current_element==prep and next_element==exp1[0]):
                taglst.append(current_element)                     
                taglst.append("<w>")
            print("ëxp1",exp1,len(exp1))    
            if len(exp1)==2:               
                if(current_element==exp1[0] and (next_element==exp1[1])):
                    taglst.append(current_element)                 
                    taglst.append("<w>")
                if(current_element==exp1[1] and (next_element==exp1[:-1])):
                    taglst.append(current_element)                 
                    taglst.append("<m>")    
            if len(exp1)==3:               
                if(current_element==exp1[0] and (next_element==exp1[1])):
                    taglst.append(current_element)                 
                    taglst.append("<w>") 
                if(current_element==exp1[1] and (next_element==exp1[2])):
                    taglst.append(current_element)                 
                    taglst.append("<w>")
                if(current_element==exp1[2] and (next_element==None)):
                    taglst.append(current_element)
                    taglst.append("<m>")
               
            if len(exp1)==4:               
                if (current_element==exp1[0] and (next_element==exp1[1])):
                    taglst.append(current_element)
                    taglst.append("<w>") 
                if (current_element==exp1[1] and (next_element==exp1[2])):
                    taglst.append(current_element)                 
                    taglst.append("<w>")
                if (current_element==exp1[2] and (next_element==exp1[3])):
                    taglst.append(current_element)                 
                    taglst.append("<w>")
                    
                if (current_element==exp1[3] and (next_element==None)):
                    taglst.append(current_element)
                    taglst.append("<m>")
               
            if len(exp1)==5:               
                if (current_element==exp1[0] and (next_element==exp1[1])):
                    taglst.append(current_element)
                    taglst.append("<w>") 
                if (current_element==exp1[1] and (next_element==exp1[2])):
                    taglst.append(current_element)                 
                    taglst.append("<w>")
                if (current_element==exp1[2] and (next_element==exp1[3])):
                    taglst.append(current_element)                 
                    taglst.append("<w>")
                if (current_element==exp1[3] and (next_element==exp1[4])):
                    taglst.append(current_element)                 
                    taglst.append("<w>")    
                if (current_element==exp1[4] and (next_element==None)):
                    taglst.append(current_element)
                    taglst.append("<m>")
        taggedsent="".join(taglst)
        category="fullstop"
        level="5"
        print("sent1",taggedsent)
       

        return(correctans,nopunct,taggedsent,category,level)
for i in range(1,3):
        p1=abbr()
        correctans,nopunct,taggedsent,category,level=p1.gensent()
        
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
       
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,correctans,taggedsent,category,level,1))
        mydb.commit()


class acrstate:
    name=""
    type=""
    tree = ET.parse('D:\\evakya\\xml\\acronymstate.xml')
    root=tree.getroot()
    
        
    def gensnoun(self):
        abbrlst1=[]
        abbrlst2=[]
        for i in acrstate.root:
            
            if i.tag=="SNOUN":
                
                acrstate.stype=i.attrib['TYPE']
                acrstate.name=i.attrib['NAME']
                #print("name",acrstate.name)
               
                with open("D:\\evakya\\dataset\\abbreviations.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        
                        if dh[0]=="state":
                           
                            abbrlst1.append(dh[1])
                            abbrlst2.append(dh[2])
               
             
                j=0
                j=random.randint(1,10)
                
                short=abbrlst1[j]
                expanded=abbrlst2[j]
##                if len(exp1)==1:
##                    taglst.append(exp1[0])
##                    taglst.append("<m>")
##
##                elif len(exp1)>=1: 
##                    for i in exp1:
##                        res='<>'.join(short[i:i + 1] for i in range(0, len(exp1), 1))
##                        taglst.append(res)
                        
        ##print(acrstate.stype,acrstate.name,short,expanded)        
        return(acrstate.stype,acrstate.name,short,expanded)
    def gensent(self):
        period="."
        p1=abbr()
        verb,prep=p1.genverbphrase()
        a1,n1,short,exp=p2.gensnoun()
        det=p1.gendet()
        subject="acronym"
        correctans=det+" "+a1+" "+short+" "+verb+"s"+" "+prep+" "+exp+period
        correctans = correctans.strip() 
        while '  ' in correctans:
            correctans = correctans.replace('  ', ' ')

       
        #--------------------unpunctuate-----------------------------------------------------------------
        punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        #--------------------------------tag unpunctuated text--------------------------------------------
        #print("nopunct",nopunct)
        #title=['Mr','Capt','Major','Bro','Mrs','Miss','Sr']   
        mylist=nopunct.split(" ")
        taglst=[]
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            ##print(previous_element, current_element, next_element)
            
##            if current_element in title and next_element==snname:
##                taglst.append(current_element)
##                taglst.append("<m>")
            verb2=verb+"s"
            if(current_element==det and next_element==subject):
                taglst.append(current_element)
                taglst.append("<w>")
            if(current_element==subject and next_element==short):
                taglst.append(current_element)
                taglst.append("<w>")    
            if(current_element==verb2 and next_element==prep):
                taglst.append(current_element)
                taglst.append("<w>")
            if(current_element==prep and next_element==exp):
                taglst.append(current_element)
                taglst.append("<w>")
            if len(exp)==2:               
                if(current_element==exp[0] and (next_element==exp[1])):
                    taglst.append(current_element)                 
                    taglst.append("<w>")
                if(current_element==exp[1] and (next_element==exp[:-1])):
                    taglst.append(current_element)                 
                    taglst.append("<m>")    
            if len(exp)==3:               
                if(current_element==exp[0] and (next_element==exp[1])):
                    taglst.append(current_element)                 
                    taglst.append("<w>") 
                if(current_element==exp[1] and (next_element==exp[2])):
                    taglst.append(current_element)                 
                    taglst.append("<w>")
                if(current_element==exp[2] and (next_element==None)):
                    taglst.append(current_element)
                    taglst.append("<m>")
            if len(exp)==4:               
                if(current_element==exp[0] and (next_element==exp[1])):
                    taglst.append(current_element)                 
                    taglst.append("<w>") 
                if(current_element==exp[1] and (next_element==exp[2])):
                    taglst.append(current_element)                 
                    taglst.append("<w>")
                if(current_element==exp[2] and (next_element==exp[3])):
                    taglst.append(current_element)                 
                    taglst.append("<w>")
                if(current_element==exp[3] and (next_element==exp[4])):
                    taglst.append(current_element)                 
                    taglst.append("<w>")    
                if(current_element==exp[4] and (next_element==None)):
                    taglst.append(current_element)
                    taglst.append("<m>")
                    
            if(current_element==exp and next_element==None):
                taglst.append(current_element)
                taglst.append("<m>")
                
                
            if(current_element==short and next_element==verb2):
                
                res='<w>'.join(short[i:i + 1] for i in range(0, len(short), 1))
                taglst.append(res)
                taglst.append("<w>")
        taggedsent="".join(taglst)
        category="fullstop"
        level="5"
        #print(correctans,nopunct,taggedsent,category,level)
        print(taggedsent)
        
        return(correctans,nopunct,taggedsent,category,level)


for i in range(1,2):
        p2=acrstate()
        correctans,nopunct,taggedsent,category,level=p2.gensent()
        
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
       
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,correctans,taggedsent,category,level,1))
        mydb.commit()

