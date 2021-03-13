import xml.etree.ElementTree as ET
import random
import re

class inter1:
    tree = ET.parse('D:\\evakya\\xml\\inter1.xml')
    def gensent(self):
        
        root = inter1.tree.getroot()
        
        for i in root:
            if i.tag=="INTN":
                intn=i.attrib['NAME']
                quot='"'
                
                exclm="!"
                sent=quot+intn+exclm+quot
                taggedsent=quot+"<w>"+intn+"<m>"+quot+"<w>"
                nopunct=quot+intn+quot
                print(sent,taggedsent,nopunct)
                return(sent,taggedsent,nopunct)

class inter2:
    tree = ET.parse('D:\\evakya\\xml\\inter2.xml')
    def gensent(self):
        
        root = inter2.tree.getroot()
        
        for i in root:
            if i.tag=="INTN":
                intn=i.attrib['NAME']
                quot='"'
                exclm="!"
                sent=quot+intn+exclm+quot
                taggedsent=quot+"<w>"+intn+"<m>"+quot+"<w>"
                nopunct=quot+intn+quot
                print(sent,taggedsent,nopunct)
                return(sent,taggedsent,nopunct)
class inter3:
    tree = ET.parse('D:\\evakya\\xml\\inter3.xml')
    def gensent(self):
        
        root = inter3.tree.getroot()
        intn3=[]
        for i in root:
            if i.tag=="INTN":
                intn=i.attrib['NAME']
                intn3=intn.split(" ")  
                quot='"'
                exclm="!"
                sent=quot+intn+exclm+quot
                taggedsent=quot+"<w>"+intn3[0]+"<w>"+intn3[1]+"<m>"+quot+"<w>"
                nopunct=quot+intn+quot
                print(sent,taggedsent,nopunct)
                return(sent,taggedsent,nopunct)

class inter4:
    tree = ET.parse('D:\\evakya\\xml\\inter4.xml')
    def gensent(self):
        
        root = inter4.tree.getroot()
        
        for i in root:
            if i.tag=="ITAG":
##                print(i.attrib)
                pro=i.attrib['PRO']
                intn=i.attrib['INTN']
                quot='"'
                exclm="!"
                sent=quot+intn+" "+pro.capitalize()+exclm+quot
                taggedsent=quot+"<w>"+intn+"<w>"+pro.capitalize()+"<m>"+quot+"<w>"
                nopunct=quot+intn+" "+pro.capitalize()+quot
                print(sent,taggedsent,nopunct)
                return(sent,taggedsent,nopunct) 
class inter5:
    tree = ET.parse('D:\\evakya\\xml\\inter5.xml')
    def gensent(self):
        
        root = inter5.tree.getroot()
        
        for i in root:
            if i.tag=="ITAG":
                ppro=i.attrib['PPRO']
                verb=i.attrib['VERB']
                intn=i.attrib['INTN']
                quot='"'
                exclm="!"
                comma=","
                sent=quot+ppro+" "+verb+" "+intn+exclm+quot
                taggedsent=quot+"<w>"+ppro+"<w>"+verb+"<w>"+intn+"<m>"+quot+"<w>"
                nopunct=quot+ppro+" "+verb+" "+intn+quot
                print(sent,taggedsent,nopunct)
                return(sent,taggedsent,nopunct)             
class inter6:
    tree = ET.parse('D:\\evakya\\xml\\inter6.xml')
    def gensent(self):
        
        root = inter6.tree.getroot()
         
        for i in root:
            if i.tag=="INTN":
                ppro=i.attrib['NAME']
                verb=i.attrib['VERB']
                intn=i.attrib['INTN']
                quot='"'
                exclm="!"
                sent=quot+intn+exclm+quot
                taggedsent=quot+"<w>"+intn+"<m>"+exclm+quot+"<w>"
                nopunct=quot+intn+quot+"<w>"
                print(sent)
                return(sent)       
#-------------------------------------------
p1=inter1()
sent,taggedsent,nopunct=p1.gensent()
level=4
category="exclamation"
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

mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))

mydb.commit() 
#---------------------------------
p2=inter2()
sent,taggedsent,nopunct=p2.gensent()
level=4
category="exclamation"
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

mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))

mydb.commit() 
#-------------------------------------------------------------
p3=inter3()
sent,taggedsent,nopunct=p3.gensent()
level=4
category="exclamation"
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

mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))

mydb.commit()
#------------------------------------------------------------
p4=inter4()
sent,taggedsent,nopunct=p4.gensent()
level=4
category="exclamation"
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

mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))

mydb.commit() 

#------------------------------------------------------
p5=inter5()
sent,taggedsent,nopunct=p5.gensent()
level=4
category="exclamation"
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

mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))

mydb.commit() 
mycursor.execute('delete from sentencedb where exerciseid>=121')
mydb.commit()
##p6=inter6()
##p6.gensent()
