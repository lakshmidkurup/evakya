import xml.etree.ElementTree as ET
import random
import re
import datetime
import time


class type11date:
    sname=""
    noundict=[]
    tree = ET.parse('D:\\evakya\\xml\\type11date.xml')
    eclass=""
    verbclass=""
    onoun=""
    
    def prep(self):
        root = type11date.tree.getroot()
        for i in root:
            if i.tag=="PREP":
                prep=i.attrib['NAME']
                return(prep)
        
    def gendate(self):
        root=type11date.tree.getroot()
        for i in root:
            if i.tag=="DATE":
##                today = datetime.date.today()
##                y=today.year
##                m=today.month
##                d=today.day
##                x = datetime.datetime(y, m, d)
##                    
##                tdate=x.strftime("%B %d, %Y")
                t = (2021, 2, 17, 17, 3, 38, 1, 48, 0)
                t = time.mktime(t)
                tdate=time.strftime("%B %d, %Y", time.gmtime(t))
                
                return(tdate)

    
    def generatesubject(self):    
        
        
        root = type11date.tree.getroot()       
        for i in root:
            if i.tag=="SNOUN":
                if i.attrib['TYPE']=="personified":
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                type11date.noundict.append(dh[1])
                                ##print(type5.noundict)
                        type11date.snname=random.choice(type11date.noundict)
                        
                    return(type11date.snname)
    def genverb(self):
        verblst=[]
        root=type11date.tree.getroot()
        for i in root:
            if i.tag=="VERB":
                type11date.eclass=i.attrib['ECLASS']
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        if type11date.eclass==dh[2]:
                            verblst.append(dh[1])
                verb=random.choice(verblst)
                
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        if verb==dh[1]:
                            type11date.verbclass=dh[0]
        return(verb,type11date.verbclass)               
       
    def genonoun(self):
        onounlst=[]
        root=type11date.tree.getroot()
        for i in root:
            if i.tag=="ONOUN":
                art=i.attrib['ART']
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:                    
                    for word in nd:
                        dh=word.split(':')
                        if type11date.verbclass==dh[0]:
                            onounlst.append(dh[1])
                    type11date.onoun=random.choice(onounlst)
                    return(art,type11date.onoun)


    def type11sent(self):
        prep=p1.prep()
        tdate=p1.gendate()
        snoun=p1.generatesubject()
        verb,vclass=p1.genverb()
        art,onoun=p1.genonoun()
        period="."
        sent=snoun+" "+verb+" "+art+" "+onoun+" "+prep+" "+tdate+period
        ##print(sent)
        correctans=sent
        #--------------------unpunctuate-----------------------------------------------------------------
        punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        #James won a race on February 17, 2021.
        mylist=nopunct.split(" ")
        taglst=[]
        weekdays =["Monday", "Tuesday", "Wednesday", "Thursday", 
                         "Friday", "Saturday", "Sunday"]
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        year=['2021','2020','2021']
        #t = [2, 7, 17, 3, 38, 1, 48, 0)
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            ##print(previous_element, current_element, next_element)

            if current_element ==snoun and next_element==verb:
                    taglst.append(current_element)
                    taglst.append("<w>")

            if current_element ==verb and next_element==art:
                    taglst.append(current_element)
                    taglst.append("<w>")

            if current_element ==art and next_element==onoun:
                    taglst.append(current_element)
                    taglst.append("<w>")
                    
            if current_element ==onoun and next_element==prep:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element ==prep and next_element in months:
                    taglst.append(current_element)
                    taglst.append("<w>")         
            #------------------------------comma
            if current_element in months and next_element.isdigit():
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element.isdigit() and next_element in year:
                    
                    
                    taglst.append(current_element)
                    taglst.append("<m>") #------------------------------comma
            if current_element in year and next_element==None:
                    
                    
                    taglst.append(current_element)
                    taglst.append("<m>")   #-----------------------------Fullstop     
            taggedsent="".join(taglst)
            category="comma"
            level="4"
            
           
        #print(taggedsent)
        return(correctans,nopunct,taggedsent,category,level) 
    def genbornsentmonthdate(self):
        snoun=p1.generatesubject()
        tree = ET.parse('D:\\evakya\\xml\\type11borndate.xml')
        root=tree.getroot()
        for i in root:
            #print(i.tag)
            if i.tag=="VERB":
                verb=i.attrib['NAME']
                verbtobe=i.attrib['VERBTOBE']
        for i in root:
             
            if i.tag=="PREP":
                prep=i.attrib['NAME']
                #print(prep)
        for i in root:
                
            if i.tag=="DATE":
                t = (2021, 2, 17, 17, 3, 38, 1, 48, 0)
                t = time.mktime(t)
                tdate=time.strftime("%B, %d", time.gmtime(t))
        period="."
        sent=snoun+" "+verbtobe+" "+verb+" "+prep+" "+tdate+period
        #print("genbornsentmonthdate",sent)
        correctans=sent
        #--------------------unpunctuate-----------------------------------------------------------------
        punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        #John was born on February, 17.
        mylist=nopunct.split(" ")
        taglst=[]
       
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        weekdays =["Monday", "Tuesday", "Wednesday", "Thursday", 
                         "Friday", "Saturday", "Sunday"]
        
        #t = [2, 7, 17, 3, 38, 1, 48, 0)
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            #print(previous_element, current_element, next_element)

            if current_element ==snoun and next_element==verbtobe:
                    taglst.append(current_element)
                    taglst.append("<w>")

            if current_element ==verbtobe and next_element==verb:
                    taglst.append(current_element)
                    taglst.append("<w>")

            if current_element ==verb and next_element==prep:
                    taglst.append(current_element)
                    taglst.append("<w>")
                    
            if current_element ==prep and next_element in months:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element in months and next_element.isdigit():
                    taglst.append(current_element)
                    taglst.append("<m>")
            if current_element.isdigit() and next_element==None:
                    
                    
                    taglst.append(current_element)
                    taglst.append("<m>") #------------------------------fullstop
             
            taggedsent="".join(taglst)
            category="comma"
            level="4"
            
           
        #print(taggedsent)
        return(correctans,nopunct,taggedsent,category,level) 
    def genbornsent(self):
        snoun=p1.generatesubject()
        tree = ET.parse('D:\\evakya\\xml\\type11borndate.xml')
        root=tree.getroot()
        for i in root:
            #print(i.tag)
            if i.tag=="VERB":
                verb=i.attrib['NAME']
                verbtobe=i.attrib['VERBTOBE']
        for i in root:
             
            if i.tag=="PREP":
                prep=i.attrib['NAME']
                #print(prep)
        for i in root:
                
            if i.tag=="DATE":
                t = (2021, 2, 17, 17, 3, 38, 1, 48, 0)
                t = time.mktime(t)
                tdate=time.strftime("%A, %B %d, %Y", time.gmtime(t))
        period="."
        sent=snoun+" "+verbtobe+" "+verb+" "+prep+" "+tdate+period
        #print(sent)
        correctans=sent
        #--------------------unpunctuate-----------------------------------------------------------------
        punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        #James was born on Tuesday, February 17, 2021.
        mylist=nopunct.split(" ")
        taglst=[]
        weekdays =["Monday", "Tuesday", "Wednesday", "Thursday", 
                         "Friday", "Saturday", "Sunday"]
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        year=['2021','2020','2021']
        #t = [2, 7, 17, 3, 38, 1, 48, 0)
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            #print(previous_element, current_element, next_element)

            if current_element ==snoun and next_element==verbtobe:
                    taglst.append(current_element)
                    taglst.append("<w>")

            if current_element ==verbtobe and next_element==verb:
                    taglst.append(current_element)
                    taglst.append("<w>")

            if current_element ==verb and next_element==prep:
                    taglst.append(current_element)
                    taglst.append("<w>")
                    

            if current_element ==prep and next_element in weekdays:
                    taglst.append(current_element)
                    taglst.append("<w>")         
            if current_element in weekdays and next_element in months:
                    taglst.append(current_element)
                    taglst.append("<m>") #------------------------------comma
            if current_element in months and next_element.isdigit():
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element.isdigit() and next_element in year:
                    
                    
                    taglst.append(current_element)
                    taglst.append("<m>") #------------------------------comma
            if current_element in year and next_element==None:
                    
                    
                    taglst.append(current_element)
                    taglst.append("<m>")   #-----------------------------Fullstop     
            taggedsent="".join(taglst)
            category="comma"
            level="4"
            
           
        #print(taggedsent)
        return(correctans,nopunct,taggedsent,category,level)            
    def genbornnocomma(self):
        snoun=p1.generatesubject()
        tree = ET.parse('D:\\evakya\\xml\\type11borndate.xml')
        root=tree.getroot()
        for i in root:
            #print(i.tag)
            if i.tag=="VERB":
                verb=i.attrib['NAME']
                verbtobe=i.attrib['VERBTOBE']
        for i in root:
             
            if i.tag=="PREP":
                prep=i.attrib['NAME']
                #print(prep)
        for i in root:
                
            if i.tag=="DATE":
                t = (2021, 2, 17, 17, 3, 38, 1, 48, 0)
                t = time.mktime(t)
                tdate=time.strftime("%d %B %Y", time.gmtime(t))
        period="."
        sent=snoun+" "+verbtobe+" "+verb+" "+prep+" "+tdate+period
        #print(sent)
        correctans=sent
        
        #--------------------unpunctuate-----------------------------------------------------------------
        punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        #James was born on Tuesday, February 17, 2021.
        mylist=nopunct.split(" ")
        taglst=[]
        weekdays =["Monday", "Tuesday", "Wednesday", "Thursday", 
                         "Friday", "Saturday", "Sunday"]
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        year=['2021','2020','2021']
        #t = [2, 7, 17, 3, 38, 1, 48, 0)
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            #print(previous_element, current_element, next_element)

            if current_element ==snoun and next_element==verbtobe:
                    taglst.append(current_element)
                    taglst.append("<w>")

            if current_element ==verbtobe and next_element==verb:
                    taglst.append(current_element)
                    taglst.append("<w>")

            if current_element ==verb and next_element==prep:
                    taglst.append(current_element)
                    taglst.append("<w>")
                    

            if current_element ==prep and next_element.isdigit():
                    taglst.append(current_element)
                    taglst.append("<w>")         
            if current_element.isdigit() and next_element in months:
                    taglst.append(current_element)
                    taglst.append("<w>") 
            if current_element in months and next_element in year:
                    taglst.append(current_element)
                    taglst.append("<w>")
            
            if current_element in year and next_element==None:
                    
                    
                    taglst.append(current_element)
                    taglst.append("<m>")   #-----------------------------Fullstop     
            taggedsent="".join(taglst)
            category="comma"
            level="4"
            
           
        #print(taggedsent)
        return(correctans,nopunct,taggedsent,category,level)
#----------Mary got a job on February 17, 2021---------------------------------------------------
for i in range(1,3):
        p1=type11date()
        correctans,nopunct,taggedsent,category,level=p1.type11sent()
        #print("correctans",taggedsent)
        category="comma"
        level=4
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
#-----------------------------Mary was born on February, 17--------------------------------------
for i in range(1,2):
    
        p1=type11date()
        correctans,nopunct,taggedsent,category,level=p1.genbornsent()
        #print("correctans",taggedsent)
        category="comma"
        level=4
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
#-----------------------------Mary was born on Tuesday, February 17, 2021-------------------------------------
for i in range(1,2):
    
        p1=type11date()
        correctans,nopunct,taggedsent,category,level=p1.genbornsent()
        #print("correctans",taggedsent)
        category="comma"
        level=4
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
#-------------------------------------------Alice was born on 17 February 2021-------------------------------------------------------------
for i in range(1,2):
        p1=type11date()
        correctans,nopunct,taggedsent,category,level=p1.genbornnocomma()
        #print("correctans",taggedsent)
        category="comma"
        level=4
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
       
        #mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,correctans,taggedsent,category,level,1))
        mydb.commit() 


for i in range(1,2):
        p1=type11date()
        correctans,nopunct,taggedsent,category,level=p1.genbornsentmonthdate()
        #print("correctans",taggedsent)
        category="comma"
        level=4
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
