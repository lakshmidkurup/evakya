import xml.etree.ElementTree as ET
import random
import mysql.connector
class rhetorical:#---I would like to know--readable
    
    tree1=ET.parse('D:\\evakya\\xml\\rhetorical.xml')
    root=tree1.getroot()
    def genclause(self):
        for i in rhetorical.root:
            noundict=[]
            if i.tag=="CLAUSE":
                verb1=i.attrib['VERB']
                if i.attrib['TYPE']=="personified":
                
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                noundict.append(dh[1])

                                #print(type5.noundict)
                        snname=random.choice(noundict)
                            
        return(snname,verb1)
        
    def gensent(self):
        sname,verb1=rhetorical.genclause(self)
        for i in rhetorical.root:
            if i.tag=="RHETORICAL":
                qtag=i.attrib['QTAG']
                verb=i.attrib['VERB']
        qmark="?"
        quot='"'
        period="."
        sent=quot+qtag+" "+verb+qmark+" "+quot+" "+sname+" "+verb1+period
        taggedsent=quot+qtag+"<w>"+verb+"<m>"+quot+sname+"<w>"+verb1+"<m>"
        category="questionmark"
        level=4
        punctuations = '''!()[]{};:.\,<>/?@#$%^&*_~'''
        nopunct=""
        for char in sent:
            if char not in punctuations:
                nopunct = nopunct + char
        print(sent,taggedsent,nopunct,category,level)                     
        return(sent,taggedsent,nopunct,category,level)
class rhetorical2:#---I would like to know--readable
    
    tree1=ET.parse('D:\\evakya\\xml\\rhetorical2.xml')
    root=tree1.getroot()
    def gensent(self):
        p1=rhetorical()
        sname,verb1=p1.genclause()
        for i in rhetorical2.root:
            if i.tag=="RHETORICAL":
                qtag=i.attrib['QTAG']
                pro=i.attrib['PRO']
                adj=i.attrib['ADJ']
                qmark="?"
                quot='"'
                period="."       
                sent=quot+qtag+" "+pro+" "+adj+qmark+" "+quot+" "+sname+" "+verb1+period
                
                taggedsent=quot+qtag+"<w>"+pro+"<w>"+adj+"<m>"+quot+sname+"<w>"+verb1+"<m>"
            category="questionmark"
            level=4
            punctuations = '''!()[]{};:.\,<>/?@#$%^&*_~'''
            nopunct=""
            for char in sent:
                if char not in punctuations:
                    nopunct = nopunct + char
            print(sent,taggedsent,nopunct,category,level)                     
            return(sent,taggedsent,nopunct,category,level)
            

class rhetorical3:#---I would like to know--readable
    
    tree1=ET.parse('D:\\evakya\\xml\\rhetorical3.xml')
    root=tree1.getroot()
    def gensent(self):
        p1=rhetorical()
        sname,verb=p1.genclause()
        for i in rhetorical3.root:
            if i.tag=="RHETORICAL":
                qtag=i.attrib['QTAG']
                neg=i.attrib['NEG']
               
        qmark="?"
        quot='"'
             
               
        sent=sname+" "+verb+" "+quot+qtag+" "+neg+qmark+" "+quot
        taggedsent=sname+"<w>"+verb+"<w>"+quot+qtag+"<w>"+neg+"<m>"+quot
        
        category="questionmark"
        level=4
        punctuations = '''!()[]{};:.\,<>/?@#$%^&*_~'''
        nopunct=""
        for char in sent:
            if char not in punctuations:
                nopunct = nopunct + char
        print(sent,taggedsent,nopunct,category,level)                     
        return(sent,taggedsent,nopunct,category,level)

class rhetorical4:#---I would like to know--readable
    
   
    def gensent(self):
        tree2=ET.parse('D:\\evakya\\xml\\rhetorical4.xml')
        root=tree2.getroot()
        for i in root:
            noundict=[]
            if i.tag=="EXCLAMATION":
                exsent=i.attrib['EXSENT']
            if i.tag=="CLAUSE":
                verb1=i.attrib['VERB']
                if i.attrib['TYPE']=="personified":
            
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                noundict.append(dh[1])

                                #print(type5.noundict)
                    snname=random.choice(noundict)
            if i.tag=="RHETORICAL":
                qtag=i.attrib['QTAG']
                pro=i.attrib['PRO']
                verb=i.attrib['VERB']
        #exsent1=[]
        exsent1=exsent.split(" ")
        #print("exsent1",exsent1)
        qmark="?"
        quot='"'
      
        category="questionmark"
        level=4        
        sent=quot+exsent+"!"+quot+" "+snname+" "+verb1+"."+" "+quot+qtag+" "+pro+" "+verb+"?"+" "+quot
        taggedsent=quot+exsent1[0]+"<w>"+exsent1[1]+"<w>"+exsent1[2]+"!"+quot+snname+"<w>"+verb1+"<m>"+quot+qtag+"<w>"+pro+"<w>"+verb+"<m>"+quot
        
        punctuations = '''()[]{};:.\,<>/?@#$%^&*_~'''
        nopunct=""
        for char in sent:
            if char not in punctuations:
                nopunct = nopunct + char
        
        print(sent,taggedsent,nopunct,category,level)                     
        return(sent,taggedsent,nopunct,category,level)

class rhetorical5:#---I would like to know--readable
    
   
    def gensent(self):
        tree3=ET.parse('D:\\evakya\\xml\\rhetorical5.xml')
        root=tree3.getroot()
        for i in root:
            noundict=[]
            
            if i.tag=="QTAG2":
                qtag2=i.attrib['QTAG']
                pro2=i.attrib['PRO']
                verb2=i.attrib['VERB']
                
            if i.tag=="RHETORICAL":
                qtag=i.attrib['QTAG']
                pro=i.attrib['PRO']
                verb=i.attrib['VERB']
        
        qmark="?"
        quot='"'
      
        category="questionmark"
        level=5
        sent=qtag+" "+pro+" "+verb+","+" "+quot+qtag2+" "+pro2+" "+verb2+"?"+quot
        taggedsent=qtag+"<w>"+pro+"<w>"+verb+"<m>"+quot+qtag2+"<w>"+pro2+"<w>"+verb2+"<m>"+quot
        #sent=quot+exsent+"!"+quot+" "+snname+" "+verb1+"."+" "+quot+qtag+" "+pro+" "+verb+"?"+quot
        #taggedsent=quot+exsent1[0]+"<w>"+exsent1[1]+"<w>"+exsent1[2]+"<m>"+quot+snname+"<w>"+verb1+"<m>"+quot+qtag+"<w>"+pro+"<w>"+verb+"<m>"+quot
        
        punctuations = '''()[]{\,<>/?@#$%^&*_~'''
        nopunct=""
        for char in sent:
            if char not in punctuations:
                nopunct = nopunct + char
        
        print(sent,taggedsent,nopunct,category,level)                     
        return(sent,taggedsent,nopunct,category,level)    
for i in range(0,1):
    p1=rhetorical()
    sent,taggedsent,nopunct,category,level=p1.gensent()
    level=5
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
    
    mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))
    mydb.commit() 
for i in range(0,1):
    p1=rhetorical2()
    sent,taggedsent,nopunct,category,level=p1.gensent()
    level=5
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
    
    mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))
    mydb.commit() 
for i in range(0,1):
    p1=rhetorical3()
    sent,taggedsent,nopunct,category,level=p1.gensent()
    level=5
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
    
    mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))
    mydb.commit() 
for i in range(0,1):
    p1=rhetorical4()
    sent,taggedsent,nopunct,category,level=p1.gensent()
    level=5
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
    
    mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))
    mydb.commit() 
        
for i in range(0,1):
    p1=rhetorical5()
    sent,taggedsent,nopunct,category,level=p1.gensent()
    level=5
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
    
    mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))
    mydb.commit() 
