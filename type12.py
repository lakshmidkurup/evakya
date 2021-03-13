import xml.etree.ElementTree as ET
import random
import re


class type12address:
    noundict=[]
    snname=""
    eclass=""
    verbclass=""
    verb=""
    pro=""
    verb1=""
    presentverb=""
    addlst=[]
    tree = ET.parse('D:\\evakya\\xml\\type12address.xml')
####    tree = ET.parse('D:\\phd\\renxmlewed\\type12address3.xml')
####    tree = ET.parse('D:\\phd\\renewed\\type12address.xml')
##    tree1='D:\\phd\\renewed\\type12address2.xml'
##    tree2='D:\\phd\\renewed\\type12address3.xml'
##    tree3='D:\\phd\\renewed\\type12address.xml'    
##    treelst=[tree1,tree2,tree3]    
##    tree4=random.choice(treelst)
##    tree=ET.parse(tree3)
    root = tree.getroot()
    def generatesubject(self):
                      
        for i in type12address.root[0]:
            if i.tag=="SNOUN":
                if i.attrib['TYPE']=="personified":
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                type12address.noundict.append(dh[1])
                                
                                ##print(type5.noundict)
                        type12address.snname=random.choice(type12address.noundict)
                      
                    ##print(type12address.snname)    
                    return(type12address.snname)
    def genpro(self):    
             
        for i in type12address.root[1]:
            if i.tag=="SPRO":
               
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        
                        if type12address.snname==dh[1]:
                           type12address.pro=dh[3]
                                
                    return(type12address.pro)
    def genverb(self):
        verblst=[]
       
        for i in type12address.root[0]:
            if i.tag=="VERB":
                type12address.eclass=i.attrib['ECLASS']
##                #print("eclass",type12address.eclass)
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        if type12address.eclass==dh[2]:
                            verblst.append(dh[1])
                type12address.verb=random.choice(verblst)
                #print("verb",type12address.verb)
                with open("D:\\evakya\\dataset\\tense.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        if type12address.verb==dh[1]:
                            type12address.presentverb=dh[0]
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        if type12address.verb==dh[1]:
                            type12address.verbclass=dh[0]
##                            #print("vc",type12address.verbclass)
        return(type12address.verb,type12address.verbclass) 

    def genprepphrase(self):
        
        vclst=[]
        olst=[]
        for i in type12address.root[0]:
            if i.tag=="ONOUN":
                with open("D:\\evakya\\dataset\\preposition.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        if type12address.verb==dh[1]:
                            prep=dh[0]
##                            ##print("prep",prep)
                type12address.verb1=type12address.presentverb+"s"            
                if type12address.verb1.endswith("s"):
                    art="a"
                    ##print(art)
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if type12address.eclass==dh[2]:
                            vclst.append(dh[0])
                            
                vc=random.choice(vclst)
                ##print(vc)
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if vc==dh[0]:
                            olst.append(dh[1])
                    onoun=random.choice(olst)
##                    #print(onoun)
                            
                return(prep,art,onoun)
        
    def genaddress(self):
        
        #<ADDRESS NAME="x" FLATNO="x" WING="x" SOCIETYNAME="x" ROAD="x" STREET="x" LOCATION="x" CITY="x" STATE="x" PINCODE="x"/>
        for i in type12address.root[1]:
        
            
            if i.tag=="ADDRESS":
                import csv
                addlst=[]
                comma=","
                period="."

                with open('D:\\evakya\\dataset\\address.csv', mode='r') as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    line_count = 0
                    for row in csv_reader:
                        if row['TYPE']=="1":
                            s=" "
                            type12address.addlst.append(row["NAME"]+comma+s+row["FLATNO"]+comma+s+row["WING"]+comma+s+row["SOCIETYNAME"]+comma+s+row["ROAD"]+comma+s+row["LOCATION"]+comma+s+row["CITY"]+comma+s+row["STATE"]+comma+s+row["PINCODE"]+period)
                            s.join(type12address.addlst)
                    sent=random.choice(type12address.addlst)
                    #print(sent)
                    return(sent)

   
    def genaddress2(self):
        
         #<ADDRESS FLATNO="x" ROAD="x" STREET="x" LOCATION="x" CITY="x" STATE="x" PINCODE="x" />
        for i in type12address.root[1]:
        
            
            if i.tag=="ADDRESS":
                import csv
                addlst=[]
                comma=","
                period="."

                with open('D:\\evakya\\dataset\\address.csv', mode='r') as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    line_count = 0
                    for row in csv_reader:
                        if row['TYPE']=="3":
                            s=""
                            addlst.append(row["FLATNO"]+comma+row["ROAD"]+comma+row["STREET"]+comma+row["LOCATION"]+comma+row["CITY"]+comma+row["STATE"]+comma+row["PINCODE"]+period)
                    ##print(addlst)
                    sent=random.choice(addlst)
                    ##print(row[")
                    return(sent)
    def genaddress1(self):
        
        #<ADDRESS BNAME="x" FLATNO="x" LANDMARK="x" ROAD="x" LOCATION="x" CITY="x" STATE="x" PINCODE="x" />
        for i in type12address.root[1]:
        
            
            if i.tag=="ADDRESS":
                import csv
               
                comma=","
                period="."

                with open('D:\\evakya\\dataset\\address.csv', mode='r') as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    line_count = 0
                    for row in csv_reader:
                        if row['TYPE']=="2":
                            s=""
                            addlst.append(row["BuildingName"]+comma+row["FLATNO"]+comma+row["Landmark"]+comma+row["ROAD"]+comma+row["LOCATION"]+comma+row["CITY"]+comma+row["STATE"]+comma+row["PINCODE"]+period)
                    #print(type12address.addlst)
                    sent=random.choice(type12address.addlst)
                    #print(sent)
                    return(sent)
    def genvbz(self):
        
        for i in type12address.root[1]:
            if i.tag=="NOUN":
                if type12address.eclass=="address":
                    vbz="is"
        
        return(vbz)
        
            
        
    def gensen(self):
        
       
        if type12address.root.tag=="SENTENCE" and type12address.root.attrib['NO']=="1":
           
            snname=p1.generatesubject()
            verb,vclass=p1.genverb()
            prep,art,onoun=p1.genprepphrase()
            address=p1.genaddress()
            pro=p1.genpro()
            vbz=p1.genvbz()
            period="."
            comma=","
            sent1=snname+" "+type12address.verb1+" "+prep+" "+art+" "+onoun+period
            sent2=pro.capitalize()+" "+type12address.eclass+" "+vbz+" "+address       
            text1=sent1+" "+sent2
            correctans=text1
            print("correctans",correctans)
        #--------------------unpunctuate-----------------------------------------------------------------
        punctuations = '''!()[]{};:'"\,<>.?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        #--------------------------------tag unpunctuated text--------------------------------------------
##John stays in a flat. His address is c/o Late Esmail Bagani,Y/2/122,B-Wing,Sarayu Society,Satghara Road,Badartala,Basirhat,Kolkata,700044.

        #print("correctans",correctans)
        #print("nopunct",nopunct)   
        adword=['address']   
        mylist=nopunct.split(" ")
        taglst=[]
        addtag=[]
       
        import csv
        with open('D:\\evakya\\dataset\\address.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            title=[]
            name=[]
            
            name2=[]
            itemlst=["C/O","Mr.","Mrs.","Late."]
            for row in csv_reader:
                if row['TYPE']=="1":
                     personname=row["NAME"]
                     persondetails=personname.split(" ")
                     print(persondetails)
                     if "C/O" in persondetails:
                         addtag.append("C/O")
                     
                     extra_pdet="Late."
                     title=["Mr.","Mrs."]
                     
                     for item in persondetails:
                        if item not in itemlst:
                            name.append(item)
                            
                     for i in name:
                         if len(i)==2:
                             name1=i
                             name1=name1.replace(".","")
                         else:
                             name2.append(i)
            #--------------------unpunctuate-----------------------------------------------------------------
                     title1=["Mrs","Mr"]
                     #print("title1",name2)
                     flatno=row["FLATNO"]
                     wing=row["WING"]
                     societyname=row["SOCIETYNAME"]
                     society=[]
                     societyname=societyname.replace(".","")
                     societyname=societyname.split(" ")
                     
                     for i in societyname:
                         society.append(i)
                         
                     roadl=[]
                     road=row["ROAD"]
                    
                     road=road.split(" ")
                
                     for i in road:
                         roadl.append(i)
                     
                     
                     location=row["LOCATION"]
                     city=row["CITY"]
                     city=city.split(" ")
                     cityl=[]
                     for i in city:
                         
                         cityl.append(i)
                     state=row["STATE"]
                     state=state.split(" ")
                     statel=[]
                     for i in state:
                         
                         statel.append(i)
                     pincode=row["PINCODE"]    
                     #print("society name",society)   
        #print("statel",statel)            
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            ##print(previous_element, current_element, next_element)
            #print(snname)
            if current_element in snname and next_element==type12address.verb1:
                taglst.append(current_element)
                taglst.append("<w>")
                   
            if current_element ==type12address.verb1 and next_element==prep:
                taglst.append(current_element)
                taglst.append("<w>")
              
            if current_element == prep and next_element==art:
                taglst.append(current_element)
                taglst.append("<w>")

            if current_element ==art and next_element==onoun:
                taglst.append(current_element)
                taglst.append("<w>")

            if current_element == onoun and next_element==pro.capitalize():               
                taglst.append(current_element)
                taglst.append("<m>")#-------------------------------------------------------------------------------------fullstop----------------

            if current_element == pro.capitalize() and next_element in adword:
                taglst.append(current_element)
                taglst.append("<w>")                                                   

            if (current_element in adword) and (next_element ==vbz):
                taglst.append(current_element)
                taglst.append("<w>")  

            if (current_element ==vbz) and next_element=="C/O":
                taglst.append(current_element)
                taglst.append("<w>")
            if (current_element =="C/O") and next_element =="Late":
                taglst.append(current_element)
                taglst.append("<w>")
            if (current_element =="Late") and next_element  in title1:
                taglst.append(current_element)
                taglst.append("<m>")    
            if (current_element in addtag) and next_element in title1:
                taglst.append(current_element)
                taglst.append("<w>")

            if (current_element==extra_pdet) and next_element in title1:
                taglst.append(current_element)
                taglst.append("<m>")

                   
            if (current_element in title1) and next_element ==name1:
                taglst.append(current_element)
                taglst.append("<m>")#--------------------------------------------------------------------fullstop-------
            if (current_element in title1) and next_element in name2:
                taglst.append(current_element)
                taglst.append("<m>")    
           
            if (current_element in name2) and next_element==name1:
                taglst.append(current_element)
                taglst.append("<w>")   
            if (current_element == name1) and next_element in name2:
                taglst.append(current_element)
                taglst.append("<m>")
            if (current_element in name2) and next_element in name2:
                taglst.append(current_element)
                taglst.append("<w>")#---------------------------------------------------------------------comma----------    
            if (current_element in name2) and (next_element==flatno):
                taglst.append(current_element)
                taglst.append("<m>")
            
            if current_element == flatno and (next_element == wing):
                taglst.append(current_element)
                taglst.append("<m>")    
            
            if (current_element == wing) and (next_element in society):
                taglst.append(current_element)
                taglst.append("<m>")
            if (current_element in society) and (next_element in society):
                taglst.append(current_element)
                taglst.append("<w>")    
            if (current_element in society) and (next_element in roadl):
                taglst.append(current_element)
                taglst.append("<m>")
            if (current_element in roadl) and (next_element in roadl):
                taglst.append(current_element)
                taglst.append("<w>")               
            if (current_element in roadl) and (next_element in location):
                taglst.append(current_element)
                taglst.append("<m>")
            if (current_element in location) and (next_element in cityl):
                taglst.append(current_element)
                taglst.append("<m>")
            if (current_element in cityl) and (next_element in state):
                taglst.append(current_element)
                taglst.append("<m>")
            if (current_element in cityl) and (next_element in cityl):
                taglst.append(current_element)
                taglst.append("<w>")
            if (current_element in statel) and (next_element in statel):
                taglst.append(current_element)
                taglst.append("<w>")    
            if (current_element in statel) and (next_element in pincode):
                taglst.append(current_element)
                taglst.append("<m>")
            if (current_element in pincode) and next_element==None:
                taglst.append(current_element)
                taglst.append("<m>")
            
        taggedsent="".join(taglst)
        taggedsent=taggedsent.replace("<m><w>","<m>")
        taggedsent=taggedsent.replace("<w><m>","<m>")
        taggedsent=taggedsent.replace("Co<w>","Co<m>")
        #taggedsent=taggedsent.replace("Ltd","Ltd.")
        category="comma"
        level="10"
        print(taggedsent)
        return(correctans,nopunct,taggedsent,category,level)
for i in range(1,3):
        p1=type12address()
        correctans,nopunct,taggedsent,category,level=p1.gensen()
        print("correctans",correctans)
        category="comma"
        level=10
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
