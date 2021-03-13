import xml.etree.ElementTree as ET
import random
import re
class quotpos:
    tree = ET.parse('D:\\evakya\\xml\\quotcommap.xml')
    root=tree.getroot()
##    <CLAUSE1 SNAME1="x" VERB="said" PREP="to" SNAME2="x" />
##    <CLAUSE2 XML="simplepositiveclass.xml" />
    def clause1(self):
        noundict=[]
        for i in quotpos.root:
            if i.tag=="CLAUSE1":
                if i.attrib['TYPE']=="personified":
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                noundict.append(dh[1])
                snname1=random.choice(noundict)
                noundict.remove(snname1)
                snname2=random.choice(noundict)
                verb=i.attrib['VERB']
                prep=i.attrib['PREP']
        clause1=snname1+" "+verb+" "+prep+" "+snname2
        punctuations = '''!.()[]{};:'\,<>/?@#$%^&*_~'''
        nopunct=""
        for char in clause1:
            if char not in punctuations:
                nopunct = nopunct + char
        
##        #print(nopunct)
        mylist=nopunct.split(" ")
        
        taglst=[]
        
       #Mary said to John.
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            ####print(previous_element, current_element, next_element)
            if current_element in snname1 and next_element==verb:
                    taglst.append(current_element)
                    taglst.append("<m>")
            if current_element==verb and next_element==prep:
                    taglst.append(current_element)
                    taglst.append("<w>")
                    taggedsent="".join(taglst)
            if current_element==prep and next_element==snname2:
                    taglst.append(current_element)
                    taglst.append("<w>")
                    taggedsent="".join(taglst)
            if current_element==snname2 and next_element==None:
                    taglst.append(current_element)
                    taglst.append("<m>")#----------------fullstop
                    taggedsent="".join(taglst)        
            taggedsent="".join(taglst)
##        #print(taggedsent)    
        ##print(clause1)
        return(clause1,taggedsent,nopunct)
    def clause2(self):
        for i in quotpos.root:
            if i.tag=="CLAUSE2":
                if i.attrib['XML']=="simplepositiveclass.xml":
                    from positivevc import positivec as p
                    sent,taggedsent,nopunct=p.gensent(self)
                
                    return(sent,taggedsent,nopunct)
    def gensentforquot(self):
        clause1,taggedsent1,nopunct1=p1.clause1()
        
        clause2,taggedsent2,nopunct2=p1.clause2()
        
        quot='"'
        comma=","
        period="."
        sent=clause2+" "+clause1+period
        correctans=sent
        taggedsent=taggedsent2+taggedsent1
        #punctuations = '''!.()[]{};:'\,<>/?@#$%^&*_~'''
        nopunct=nopunct2+" "+nopunct1
        category="comma"
        level="8"
        print(taggedsent)
        #print(correctans,nopunct,taggedsent,category,level)      
        return(correctans,nopunct,taggedsent,category,level)          
for i in range(1,4):
        p1=quotpos()
        correctans,nopunct,taggedsent,category,level=p1.gensentforquot()
        print("correctans",taggedsent)
        category="comma"
        level=8
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
                ######print("id1:",row[0])
        id2=id1+1
                

        #-----------------------------insert into database------------------------------------------------------------------------------------------------------------------   
       
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,correctans,taggedsent,category,level,1))
        mydb.commit() 


##class quotneg:
##    tree = ET.parse('D:\\phd\\renewed\\quotcomman.xml')
##    root=tree.getroot()
##    def gensent(self):
##        clause1,taggedsent1,nopunct1=p1.clause1()
##        for i in quotneg.root:
##            if i.tag=="CLAUSE2":
##                if i.attrib['XML']=="simplenegativeclass.xml":
##                    from negativevc import negativec as n
##                    clause2,taggedsent2,nopunct2=n.clause2()
##                
##     
##        period="."
##        sent=clause2+" "+clause1+period
##        correctans=sent
##        taggedsent=taggedsent2+taggedsent1
##        #punctuations = '''!.()[]{};:'\,<>/?@#$%^&*_~'''
##        nopunct=nopunct2+" "+nopunct1
##        category="comma"
##        level="7"
##        #print(correctans,nopunct,taggedsent,category,level)      
##        return(correctans,nopunct,taggedsent,category,level)          
##for i in range(1,4):
##        p2=quotneg()
##        correctans,nopunct,taggedsent,category,level=p2.gensent()
##        #print("correctans",taggedsent)
##        category="comma"
##        level=1
##        import mysql.connector
##
##        mydb = mysql.connector.connect(
##                host="localhost",
##                user="root",
##                passwd="rohith@123",
##                database="pythonlogin"
##        )
##        mycursor = mydb.cursor()
##
##        mycursor.execute("select max(exerciseid) from sentencedb")  
##        rows = mycursor.fetchall()
##        for row in rows:
##                id1=0
##                id1=row[0]
##                ######print("id1:",row[0])
##        id2=id1+1
##                
##
##        #-----------------------------insert into database------------------------------------------------------------------------------------------------------------------   
##       
##        #mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,correctans,taggedsent,category,level,1))
##        mydb.commit() 
##p1=quotpos()
##p1.gensentforquot()
##p2=quotneg()
##p2.gensent()
