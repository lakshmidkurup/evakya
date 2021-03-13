import xml.etree.ElementTree as ET
import random
import re
class directq:
        
    snname=""
    adj1=""
    noundict=[]
    tree = ET.parse('D:\\evakya\\xml\\qwherestay.xml')
    tree1 = ET.parse('D:\\evakya\\xml\\qwherework.xml')
    root=tree.getroot()
    vclass=""

    def genqtag(self):
        for i in directq.root:
            if i.tag=="QTAG":
                qtag=i.attrib['TYPE']
                #print(qtag)
        return(qtag)

    def genaux(self):
        for i in directq.root:
            if i.tag=="AUX":
                aux=i.attrib['TYPE']
        #print(aux)
        return(aux)

    def gensnoun(self):
        for i in directq.root:
            if i.tag=="SNOUN":
                if i.attrib['TYPE']=="personified":
                

                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                directq.noundict.append(dh[1])

                                #print(type5.noundict)
                    directq.snname=random.choice(directq.noundict)
                    
        #print(directq.snname)
        return(directq.snname)
        
    def genverb(self):
        verblst=[]
        for i in directq.root:
            if i.tag=="PRESENTVERB":
                directq.vclass=i.attrib['VCLASS']
                #print("directq.vclass",directq.vclass)
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if directq.vclass==dh[0]:
                            verblst.append(dh[1])
                    directq.verb=random.choice(verblst)
                    #print("directq.verb",directq.verb)

                with open("D:\\evakya\\dataset\\tense.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        #print(dh)
                        if directq.verb==dh[1]:
                            presentverb=dh[0]

                    
        #print("preverb",presentverb)
        return(presentverb)
    
    def gensent(self):
        
        qmark="?"
        qtag=p1.genqtag()
        aux=p1.genaux()
        snoun=p1.gensnoun()
        verb=p1.genverb()
        sent=qtag.capitalize()+" "+aux+" "+snoun+" "+verb+qmark
        taggedsent=qtag.capitalize()+"<w>"+aux+"<w>"+snoun+"<w>"+verb+"<m>"
        nopunct=""
        punctuations = '?'
        mylist=[]
        for char in sent:
            if char not in punctuations:
                nopunct = nopunct + char
             
        category="questionmark"
        level=1
        print(sent,taggedsent,nopunct,category,level)    
                     
        return(sent,taggedsent,nopunct,category,level)
        
       
    

p1=directq()
sent,taggedsent,nopunct,category,level=p1.gensent()

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
                

#-----------------------------insert into database------------------------------------------------------------------------------------------------------------------   

mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))
mydb.commit()
sent1="How"+" "+"does"+" "+"Mary"+" "+"read"+"?"
taggedsent1="How"+"<w>"+"does"+"<w>"+"Mary"+"<w>"+"read"+"<m>"
nopunct1="How"+" "+"does"+" "+"Mary"+" "+"read"
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
                

#-----------------------------insert into database------------------------------------------------------------------------------------------------------------------   

mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct1,sent1,taggedsent1,category,level,1))
mydb.commit()
                        
#------------------------
sent2="Why "+" "+"is"+" "+"Mary"+" "+"late"+"?"
taggedsent2="Why"+"<w>"+"is"+"<w>"+"Mary"+"<w>"+"late"+"<m>"
nopunct2="Why"+" "+"is"+" "+"Mary"+" "+"late"
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
                

#-----------------------------insert into database------------------------------------------------------------------------------------------------------------------   

mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct2,sent2,taggedsent2,category,level,1))
mydb.commit()
    
##print(sent)
##print(sent1)
##print(sent2)
