import xml.etree.ElementTree as ET
import random
import re


class type12address3:
    noundict=[]
    snname=""
    eclass=""
    verbclass=""
    verb=""
    pro=""
    verb1=""
    presentverb=""
    addlst=[]
    
    tree = ET.parse('D:\\evakya\\xml\\type12address3.xml')

   
    root = tree.getroot()
    def generatesubject(self):
                      
        for i in type12address3.root[0]:
            if i.tag=="SNOUN":
                if i.attrib['TYPE']=="personified":
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                type12address3.noundict.append(dh[1])
                                
                                #print(type5.noundict)
                        type12address3.snname=random.choice(type12address3.noundict)
                      
                    print(type12address3.snname)    
                    return(type12address3.snname)
    def genpro(self):    
             
        for i in type12address3.root[1]:
            if i.tag=="SPRO":
               
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        
                        if type12address3.snname==dh[1]:
                           type12address3.pro=dh[3]
                                
                    return(type12address3.pro)
    def genverb(self):
        verblst=[]
       
        for i in type12address3.root[0]:
            if i.tag=="VERB":
                type12address3.eclass=i.attrib['ECLASS']
##                print("eclass",type12address3.eclass)
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        if type12address3.eclass==dh[2]:
                            verblst.append(dh[1])
                type12address3.verb=random.choice(verblst)
                print("verb",type12address3.verb)
                with open("D:\\evakya\\dataset\\tense.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        if type12address3.verb==dh[1]:
                            type12address3.presentverb=dh[0]
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        if type12address3.verb==dh[1]:
                            type12address3.verbclass=dh[0]
##                            print("vc",type12address3.verbclass)
        return(type12address3.verb,type12address3.verbclass) 

    def genprepphrase(self):
        
        vclst=[]
        olst=[]
        for i in type12address3.root[0]:
            if i.tag=="ONOUN":
                with open("D:\\evakya\\dataset\\preposition.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        if type12address3.verb==dh[1]:
                            prep=dh[0]
##                            #print("prep",prep)
                type12address3.verb1=type12address3.presentverb+"s"            
                if type12address3.verb1.endswith("s"):
                    art="a"
                    #print(art)
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if type12address3.eclass==dh[2]:
                            vclst.append(dh[0])
                            
                vc=random.choice(vclst)
                #print(vc)
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if vc==dh[0]:
                            olst.append(dh[1])
                    onoun=random.choice(olst)
##                    print(onoun)
                            
                return(prep,art,onoun)
        
    

   
    def genaddress2(self):
        for i in type12address3.root[1]:
        
            
            if i.tag=="ADDRESS":
                import csv
               
                comma=","
                period="."

                with open('D:\\evakya\\dataset\\address.csv', mode='r') as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    line_count = 0
                    for row in csv_reader:
                        if row['TYPE']=="2":
                            s=" "
                            type12address3.addlst.append(row["BuildingName"]+comma+s+row["FLATNO"]+comma+s+row["Landmark"]+comma+s+row["ROAD"]+comma+s+row["LOCATION"]+comma+s+row["CITY"]+comma+s+row["STATE"]+comma+s+row["PINCODE"]+period)
                    print(type12address3.addlst)
                    sent=random.choice(type12address3.addlst)
                    #print(sent)
                    return(sent)
    def genvbz(self):
        
        for i in type12address3.root[1]:
            if i.tag=="NOUN":
                if type12address3.eclass=="address":
                    vbz="is"
        
        return(vbz)
        
            
        
    def gensen(self):
        
       
        if type12address3.root.tag=="SENTENCE" and type12address3.root.attrib['NO']=="3":
           
            snname=p1.generatesubject()
            verb,vclass=p1.genverb()
            prep,art,onoun=p1.genprepphrase()
            address=p1.genaddress2()
            pro=p1.genpro()
            vbz=p1.genvbz()
            period="."
            comma=","
            sent1=snname+" "+type12address3.verb1+" "+prep+" "+art+" "+onoun+period
            sent2=pro.capitalize()+" "+type12address3.eclass+" "+vbz+" "+address       
            text1=sent1+" "+sent2
            correctans=text1
            print(correctans)
            
        #--------------------unpunctuate-----------------------------------------------------------------
        punctuations = '''!()[]{};:'"\,<>.?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        #--------------------------------tag unpunctuated text--------------------------------------------
##John stays in a flat. His address is Daksha Bldng,13/19,Vallabh Bagh Lane,,Ghatkopar,Mumbai,Mumbai,400077.

        print("correctans",correctans)
        print("nopunct",nopunct)   
        adword=['address']   
        mylist=nopunct.split(" ")
        taglst=[]
        addtag=[]
 #["BuildingName"]+comma+row["FLATNO"]+comma+row["Landmark"]+comma+row["ROAD"]+comma+row["LOCATION"]+comma+row["CITY"]+comma+row["STATE"]+comma+row["PINCODE"]      
        import csv
        with open('D:\\evakya\\dataset\\address.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            title=[]
            name=[]
            
            name2=[]
            itemlst=["C/O","Mr.","Mrs.","Late"]
            for row in csv_reader:
                if row['TYPE']=="2":

                     bnamel=[]
                     roadl=[]
                     societyl=[]
                     landmarkl=[]
                     streetl=[]
                     statel=[]
                     locationl=[]
                     flatnol=[]
                     bname=row["BuildingName"]
                     flatno=row["FLATNO"]
                     landmark=row["Landmark"]
                     road=row["ROAD"]
                     location=row["LOCATION"]
                     city=row["CITY"]
                     state=row["STATE"]
                     pincode=row["PINCODE"]
                     societyname=row["SOCIETYNAME"]
                     flatno=flatno.split(" ")
                     for i in flatno:
                         flatnol.append(i)
                     bname=bname.split(" ")
                     for i in bname:
                         bnamel.append(i)
                    
                     landmark=landmark.replace(".","")
                     landmark = " ".join(landmark.split())
                     landmark=landmark.split(" ")
                     for i in landmark:
                         landmarkl.append(i)
                     
                    
                     road=road.replace(".","")
                     road=road.split(" ")
                
                     for i in road:
                         roadl.append(i)
                    
                     state=state.split(" ")    
                     for i in state:
                         statel.append(i)
                                             
                     city=city.split(" ")
                     cityl=[]
                     for i in city:
                         
                         cityl.append(i)
                     print("bname",bnamel)   
                    
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            print(previous_element, current_element, next_element)
            
            if current_element in snname and next_element==type12address3.verb1:
                taglst.append(current_element)
                taglst.append("<w>")
                   
            if current_element ==type12address3.verb1 and next_element==prep:
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

            if (current_element ==vbz) and next_element in bnamel:
                taglst.append(current_element)
                taglst.append("<w>")
            if (current_element in bnamel) and next_element in bnamel:
                taglst.append(current_element)
                taglst.append("<w>")
               
            if (current_element in bnamel) and next_element in flatnol:
                taglst.append(current_element)
                taglst.append("<m>")
              
            if (current_element in flatnol) and next_element in flatnol:
                taglst.append(current_element)
                taglst.append("<w>")
                
            if (current_element==flatnol[0]) and next_element ==landmarkl[0]:
                taglst.append(current_element)
                taglst.append("<m>")#--------------------------------------------
             
            if (current_element=="Opp" and next_element ==landmarkl[1]):
                taglst.append(current_element)
                taglst.append("<m>")
                
            if (current_element==landmarkl[1]) and next_element ==landmarkl[2]:
                taglst.append(current_element)
                taglst.append("<w>")
                
            if (current_element in landmarkl) and next_element in roadl:
                taglst.append(current_element)
                taglst.append("<m>")
                
            if (current_element in roadl) and next_element in roadl:
                taglst.append(current_element)
                taglst.append("<w>")#--------------------------------------------------------------------fullstop-------

            if (current_element in roadl) and next_element==location:
                taglst.append(current_element)
                taglst.append("<m>")    
           
            if (current_element ==location) and next_element==location:
                taglst.append(current_element)
                taglst.append("<w>")
                
            if (current_element == locationl) and next_element in cityl:
                taglst.append(current_element)
                taglst.append("<m>")
                
            if (current_element in cityl) and next_element in cityl:
                taglst.append(current_element)
                taglst.append("<w>")#---------------------------------------------------------------------comma----------
                
            if (current_element in cityl) and (next_element in statel):
                taglst.append(current_element)
                taglst.append("<m>")
            
            if current_element in statel and (next_element in statel):
                taglst.append(current_element)
                taglst.append("<w>")    
           
            if (current_element in statel) and (next_element == pincode):
                taglst.append(current_element)
                taglst.append("<m>")
          
            if (current_element in pincode) and next_element==None:
                taglst.append(current_element)
                taglst.append("<m>")    
        taggedsent="".join(taglst)
        #taggedsent=taggedsent.replace("Opp","Opp.")
        category="comma"
        level="10"
        print(taggedsent)
        return(correctans,nopunct,taggedsent,category,level)

for i in range(1,2):
        p1=type12address3()
        correctans,nopunct,taggedsent,category,level=p1.gensen()
        print(correctans)
        print(taggedsent)
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
                ##print("id1:",row[0])
        id2=id1+1
                
        
        #-----------------------------insert into database------------------------------------------------------------------------------------------------------------------   
       
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,correctans,taggedsent,category,level,1))
        mydb.commit()


