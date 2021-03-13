import xml.etree.ElementTree as ET

import re
import random
class directwhat1:
    
    tree1=ET.parse('D:\\evakya\\xml\\directwhat1.xml')
    root=tree1.getroot()
    def genwhat1tags(self):
        verblst=[]
        noundict=[]
        for i in directwhat1.root:
            if i.tag=="AUXV":
                aux=i.attrib['TYPE']
            if i.tag=="QTAG":
                qtag=i.attrib['TYPE']
            if i.tag=="SNOUN":
                if i.attrib['TYPE']=="personified":
                

                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                noundict.append(dh[1])

                                #print(type5.noundict)
                    snname=random.choice(noundict)    
            if i.tag=="PRESENTVERB":
                vclass=i.attrib['VCLASS']
                #print("directq.vclass",directq.vclass)
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if vclass==dh[0]:
                            verblst.append(dh[1])
                    verb=random.choice(verblst)
                    #print("directq.verb",directq.verb)

                with open("D:\\evakya\\dataset\\tense.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        #print(dh)
                        if verb==dh[1]:
                            presentverb=dh[0]
                
                return(qtag,aux,snname,presentverb)
          
##    def gensent(self):
##        qmark="?"
##        qtag,aux,snname,pv=p5.genwhat1tags()
####        print("aux",aux)
####        print("qtag",qtag)
####        print("snoun",snname)
####        print("verb",pv)
##        sent=qtag+" "+aux+" "+snname+" "+pv+qmark
##        print(sent)
##        return(sent)


class directwhat2:
    tree1=ET.parse('D:\\evakya\\xml\\directwhat2.xml')
    root=tree1.getroot()
    def genwhat2tags(self):
        noundict=[]
        verblst=[]
        for i in directwhat2.root:
            if i.tag=="AUXV":
                aux=i.attrib['TYPE']
            if i.tag=="QTAG":
                qtag=i.attrib['TYPE']
            if i.tag=="SNOUN":
                if i.attrib['TYPE']=="personified":
                

                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                noundict.append(dh[1])

                                #print(type5.noundict)
                    snname=random.choice(noundict)    
            if i.tag=="PRESENTVERB":
                vclass=i.attrib['VCLASS']
                #print("directq.vclass",directq.vclass)
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if vclass==dh[0]:
                            verblst.append(dh[1])
                    verb=random.choice(verblst)
                    #print("directq.verb",directq.verb)

                with open("D:\\evakya\\dataset\\tense.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        #print(dh)
                        if verb==dh[1]:
                            presentverb=dh[0]
                
                return(qtag,aux,snname,presentverb)
      
    def gensent(self):
        qmark="?"
        
        qtag,aux,snname,pv=p6.genwhat2tags()
        sent=qtag+" "+aux+" "+snname+" "+pv+qmark
        taggedsent=qtag+"<w>"+aux+"<w>"+snname+"<w>"+pv+"<m>"
        
        nopunct=""
        punctuations = '?'
        mylist=[]
        for char in sent:
            if char not in punctuations:
                nopunct = nopunct + char
             
        category="questionmark"
        level=1
        #print(sent)    
        return(sent,taggedsent,nopunct,category,level)             
    
        
for i in range(1,3):        
    p6=directwhat2()
    sent,taggedsent,nopunct,category,level=p6.gensent()
    print("sen6",sent)
    ##    print(sent,taggedsent,nopunct,category,level)
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
    level=1                

    #-----------------------------insert into database------------------------------------------------------------------------------------------------------------------   

    mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))
    mydb.commit() 


##
##p7=directwhat1()
##qtag,aux,snname,pv=p7.genwhat1tags()
##qmark="?"
##sent=qtag+" "+aux+" "+snname+" "+pv+qmark
##print("sent7",sent)
##taggedsent=qtag+"<w>"+aux+"<w>"+snname+"<w>"+pv+"<m>"
##nopunct=""
##punctuations = '?'
##mylist=[]
##for char in sent:
##    if char not in punctuations:
##        nopunct = nopunct + char
##     
##category="questionmark"
##level=1
##import mysql.connector
##
##mydb = mysql.connector.connect(
##        host="localhost",
##        user="root",
##        passwd="rohith@123",
##        database="pythonlogin"
##)
##mycursor = mydb.cursor()
##
##mycursor.execute("select max(exerciseid) from sentencedb")  
##rows = mycursor.fetchall()
##for row in rows:
##        id1=0
##        id1=row[0]
##        #####print("id1:",row[0])
##id2=id1+1
##                
##nopunct=""
##punctuations = '?'
##mylist=[]
##for char in sent:
##    if char not in punctuations:
##        nopunct = nopunct + char
##     
##category="questionmark"
##level=1
###print(sent,taggedsent,nopunct,category,level) 
###-----------------------------insert into database------------------------------------------------------------------------------------------------------------------   
##
##mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))
##mydb.commit() 
##        
