import xml.etree.ElementTree as ET
import random
import re
import csv


class type12work:
    noundict=[]
    snname=""
    eclass=""
    verbclass=""
    verb=""
    pro=""
    onoun=""
    verb1=""
    objname=""
    addlst1=[]
   
    tree = ET.parse('D:\\evakya\\xml\\type12work.xml')

    root = tree.getroot()
    def generatesubject(self):
                      
        for i in type12work.root[0]:
            if i.tag=="SNOUN":
                if i.attrib['TYPE']=="personified":
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                type12work.noundict.append(dh[1])
                                
                                ##print(type5.noundict)
                        type12work.snname=random.choice(type12work.noundict)
                      
                    ##print(type12work.snname)    
                    return(type12work.snname)
    def genpro(self):    
             
        for i in type12work.root[1]:
            if i.tag=="SPRO":
            
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if type12work.snname == dh[1] and dh[0]=="personified":
                            type12work.pro=dh[3]
                           # #print(type12work.pro)
                    return(type12work.pro)
    def genverb(self):
        verblst=[]
       
        for i in type12work.root[0]:
            if i.tag=="VERB":
                type12work.eclass=i.attrib['ECLASS']
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        if type12work.eclass==dh[2]:
                            verblst.append(dh[1])
                            ##print(verblst)
                type12work.verb=random.choice(verblst)
                with open("D:\\evakya\\dataset\\tense.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if type12work.verb==dh[1]:
                            presentverb=dh[0]

                type12work.verb1=presentverb+"s"
                ##print(type12work.verb1)
                
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        if type12work.verb==dh[1]:
                            type12work.verbclass=dh[0]
                            ##print(type12work.verbclass)
        return(type12work.verb1,type12work.verbclass) 

    def genprepphrase(self):
        
        vclst=[]
        olst=[]
        for i in type12work.root[0]:
            if i.tag=="ONOUNP":
                if type12work.verb=="work" or "join":
                    with open("D:\\evakya\\dataset\\preposition.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if type12work.verb==dh[1]:
                                prep=dh[0]
                
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if type12work.eclass==dh[2]:
                            vclst.append(dh[0])
                            
                vc=random.choice(vclst)
                ##print(vc)
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if vc==dh[0]:
                            olst.append(dh[1])
                    type12work.onoun=random.choice(olst)
                    ##print(type12work.onoun)
                pattern = '^[aeiou]'
                result = re.match(pattern, type12work.onoun)
               
                if result:
                    art="an"
                else:
            
                    art="a"
        ##print(prep,art,type12work.onoun)              
        return(prep,art,type12work.onoun)
        
    def genaddress(self):
        addlst=[]
        for i in type12work.root[2]:
        
            
            if i.tag=="ADDRESS":
                import csv
                addlst=[]
                comma=","
                period="."
                ##print("aa",type12work.objname)
                with open('D:\\evakya\\dataset\\address.csv', mode='r') as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    line_count = 0
                    for row in csv_reader:
                        
                        if row['TYPE']=="4":
                            s=" "
                            
                            addlst.append(row["LOCATION"]+comma+s+row["CITY"]+comma+s+row["STATE"]+comma+s+row["PINCODE"])
                            
                   
                    sent1=random.choice(addlst)
                    print("add",sent1)
                    return(sent1)

   
    def gensub1(self):
        import csv
        addlst1=[]
        period="."
        for i in type12work.root[1]:
            if i.tag=="NOUNPHRASE":
                
                if type12work.eclass=="oaddress":
                    i.attrib['DET']="the"
                    i.attrib['VBZ']="is"
                    subname=i.attrib['SNAME']
                    i.attrib['PREP']="of"
                    i.attrib['OTYPE']=type12work.onoun
                    with open('D:\\evakya\\dataset\\address.csv', mode='r') as csv_file:
                        csv_reader = csv.DictReader(csv_file)
                        line_count = 0
                        for row in csv_reader:
                            if row['TYPE']=="4":
                            
                                type12work.addlst1.append(row["NAME"])
                    ##print(addlst1)
                    type12work.objname=random.choice(type12work.addlst1)
                           
                    i.attrib['ONAME']=type12work.objname
        period="."
        sub1=i.attrib['DET'].capitalize()+" "+subname+" "+i.attrib['PREP']+" "+i.attrib['DET']+" "+type12work.onoun+" "+i.attrib['VBZ']+" "+i.attrib['ONAME']
        det1=i.attrib['DET'].capitalize()
        det=i.attrib['DET']
        prep=i.attrib['PREP']
        onoun=type12work.onoun
        vbz=i.attrib['VBZ']
        oname=i.attrib['ONAME']
        return(sub1,det1,subname,prep,det,onoun,vbz,oname)
    def gensub2(self):
        import csv
        addlst2=[]
        period="."
        for i in type12work.root[2]:
            ##print(i.tag)
            if i.tag=="SNOUN":
                i.attrib['DET']="the"
                deter=i.attrib['DET'].capitalize()

                sname2=i.attrib['SNAME']
                
            if i.tag=="VERB":     
                i.attrib['VBZ']="is"
                vbz=i.attrib['VBZ']
        add=p1.genaddress()             
        quotes="\""
        sub2=deter+" "+sname2+" "+vbz+" "+'"'+add+'"'
        



        return(sub2,deter,sname2,vbz,add)
        
                    
        
    def gensen(self):
        
       
        if type12work.root.tag=="SENTENCE" and type12work.root.attrib['NO']=="5":
           
            snname=p1.generatesubject()
            verb,vclass=p1.genverb()
            prep,art,onoun=p1.genprepphrase()
            
            address=p1.genaddress()
            
            sub1,det1,subname,prep1,det,onoun,vbz,oname=p1.gensub1()
            pattern='[.]["]' #-----if a period followed by a quotes,replace y quotes
##            sub11=re.sub(pattern,"\"",sub1)
##
            sub2,deter,sname2,vbz,add=p1.gensub2()
            sub21=re.sub(pattern,"\"",sub2)
            period ="."
##            comma=","

            sent1=snname+" "+verb+" "+prep+" "+art+" "+onoun+period
            sent1=sent1.replace("  "," ")
            correctans=sent1+" "+sub1+period+" "+sub2+period
            print("correctans",correctans)
            
             #--------------------unpunctuate-----------------------------------------------------------------
            punctuations= '''""!()[]{};:'\,<>?@#$%^&*_~'''
           
            nopunct=""
            nopunct2=""
            nopunct3=""
            
            #print("sub1",sub2)
            for char in sub2:
                if char not in punctuations:
                    nopunct3 = nopunct3 + char
                
            for char in sent1:
                punctuation="."
                if char not in punctuation:
                    nopunct = nopunct + char
            for char in sub1:
                if char not in punctuations:
                    nopunct2= nopunct2+char    
            nopunct2=nopunct2.replace("Pvt.","Pvt")
            nopunct2=nopunct2.replace("Ltd.","Ltd")
            nopunct2=nopunct2.replace("Software.","Software")
            sent=nopunct+" "+nopunct2+" "+nopunct3
            nopunct=sent
            print("sent",sent)
            taglst=[]
            mylist=sent.split(" ")
            art=["a","an"]
            objname=type12work.objname.replace("Software.","Software")
            objname=type12work.objname.replace("Pvt.","Pvt")
            objname=objname.replace("Ltd.","Ltd")
            onamelst=objname.split(" ")
            #print("onamelst",onamelst)
            with open('D:\\evakya\\dataset\\address.csv', mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                landmarkl=[]
                cityl=[]
                statel=[]
                pincodel=[]
                locationl=[]
                for row in csv_reader:
                    if row['TYPE']=="4":
                        landmarkl.append(row['Landmark'])
                        locationl.append(row['LOCATION'])
                        cityl.append(row['CITY'])
                        statel.append(row['STATE'])
                        pincodel.append(row['PINCODE'])
                #print("statel",statel)        
                new_landmark = []
                for item in landmarkl:
                    new_landmark.extend(item.split())
                #print("newland",new_landmark)        
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            print(previous_element, current_element, next_element)
            
            if current_element in snname and next_element==verb:
                taglst.append(current_element)
                taglst.append("<w>")
                   
            if current_element ==verb and next_element==prep:
                taglst.append(current_element)
                taglst.append("<w>")
            if current_element ==verb and next_element in art:
                taglst.append(current_element)
                taglst.append("<w>")    
            if current_element ==prep and next_element in art:
                taglst.append(current_element)
                taglst.append("<w>")    
            if current_element in art and next_element==onoun:
                taglst.append(current_element)
                taglst.append("<w>")
            if current_element ==onoun and next_element==det.capitalize():
                taglst.append(current_element)
                taglst.append("<m>")
            if current_element ==det.capitalize() and next_element=="name":
                taglst.append(current_element)
                taglst.append("<w>")
            if current_element =="name" and next_element=="of":
                taglst.append(current_element)
                taglst.append("<w>")
            if current_element =="of" and next_element==det:
                taglst.append(current_element)
                taglst.append("<w>")

            if current_element ==det and next_element==onoun:
                taglst.append(current_element)
                taglst.append("<w>")
            if current_element ==onoun and next_element==vbz:
                taglst.append(current_element)
                taglst.append("<w>")
            if current_element == vbz and next_element in onamelst:
                taglst.append(current_element)
                taglst.append("<w>")

            if (current_element in onamelst) and (next_element in onamelst):
                taglst.append(current_element)
                taglst.append("<w>")
            if (current_element in onamelst) and (next_element ==det.capitalize()):
                taglst.append(current_element)
                taglst.append("<m>")
            if (current_element ==det.capitalize()) and (next_element =="address"):
                taglst.append(current_element)
                taglst.append("<w>")    
            if (current_element =="address") and (next_element ==vbz):
                taglst.append(current_element)
                taglst.append("<w>")
            if (current_element ==vbz) and (next_element in locationl):
                taglst.append(current_element)
                taglst.append("<w>")
           
            if (current_element in locationl) and (next_element in cityl):
                taglst.append(current_element)
                taglst.append("<m>")     
            if (current_element in cityl) and (next_element in statel):
                taglst.append(current_element)
                taglst.append("<m>")
            if (current_element in statel) and (next_element in pincodel):
                taglst.append(current_element)
                taglst.append("<m>")
            if (current_element in pincodel) and (next_element==None):
                taglst.append(current_element)
                taglst.append("<m>")    
                
        taggedsent="".join(taglst)
        taggedsent=taggedsent.replace("Pvt<w>Ltd<m>","Pvt<w>Ltd<m>")
        taggedsent=taggedsent.replace("BMC","B<w>M<w>C")
        taggedsent=taggedsent.replace("Pvt","Pvt.")
        taggedsent=taggedsent.replace("Ltd","Ltd.")
        category="comma"
        level="10"
        nopunct=nopunct.replace("Pvt","Pvt.")
        nopunct=nopunct.replace("Ltd","Ltd.")
        print(taggedsent)        
        return(correctans,nopunct,taggedsent,category,level)
for i in range(1,3):
        p1=type12work()
        correctans,nopunct,taggedsent,category,level=p1.gensen()
        print(nopunct)
        #print(taggedsent)
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
                ###print("id1:",row[0])
        id2=id1+1
                
        
        #-----------------------------insert into database------------------------------------------------------------------------------------------------------------------   
       
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,correctans,taggedsent,category,level,1))
        mydb.commit()

