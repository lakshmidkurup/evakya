import xml.etree.ElementTree as ET
import random
import re

class type10comma:
    tree = ET.parse('D:\\evakya\\xml\\type10comma.xml')
    verb=""
    vclass=""
    eclass=""
    onoun=""
    verbclass=""
    snoun=""
    rskey=['Rs.']
    def gennoun(self):
        nounlst=[]
        pro=[]
        root=type10comma.tree.getroot()
        for i in root:
            if i.tag=="SNOUN" and i.attrib['TYPE']=="personified":
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        ##print(dh)
                        if dh[0]=="personified":
                            nounlst.append(dh[1])
                            pro.append(dh[2])

        type10comma.snoun=random.choice(nounlst)
        return(type10comma.snoun)

    def genverb(self):
    #<VERB TYPE="paid" ECLASS="numeric"  />
        verblst=[]
        root=type10comma.tree.getroot()
        for i in root:
            if i.tag=="VERB":
                type10comma.vclass=i.attrib['VCLASS']
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        if type10comma.vclass==dh[0]:
                            verblst.append(dh[1])
##        #print("vl",verblst)
        type10comma.verb=random.choice(verblst)    
        return(type10comma.verb,type10comma.vclass)
    def gennounamount(self):
        #<AMT HOW="x" />
        root=type10comma.tree.getroot()
        for i in root:
            noundict=[]
            if i.tag=="AMT":
                type10comma.eclass=i.attrib['ECLASS']     
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:                    
                    for word in nd:
                        dh=word.split(':')
                        if type10comma.vclass==dh[0]:
                            noundict.append(dh[1])
                            type10comma.onoun=random.choice(noundict)
                            
                with open("D:\\evakya\\dataset\\pricelist.txt") as nd:                    
                    for word in nd:
                        dh=word.split(':')
                        if type10comma.onoun==dh[0]:
                            pricelist=dh[1]
                    ##print(pricelist)
                    return(type10comma.onoun,pricelist)
    
    def genobjphrase(self):
        
        root=type10comma.tree.getroot()
        for i in root[3]:
            ##print(i.tag)
            if i.tag=="PREP":
                prep=i.attrib['TYPE']
                prep="for"
                ##print(prep)
            if i.tag=="PRO":
                    ##print(i.tag)
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:                    
                        for word in nd:
                            dh=word.split(':')
                            ##print(type10comma.snoun)
                            if dh[0]=="personified":
                                if type10comma.snoun==dh[1]:
                                
                                    pro=dh[3]
                                    ##print(pro)

            if i.tag=="ADJ":
                adj=[]
                with open("D:\\evakya\\dataset\\adjectives.txt") as nd:                    
                    for word in nd:
                        dh=word.split(':')
                        if type10comma.vclass==dh[0]:
                            adj.append(dh[1])
                adj1=random.choice(adj)
                
                ##print(adj1)
        
        ##print(ophrase)
        return(prep,pro,adj1)    

                                
    def gen10sent(self):
        type10comma.snoun=p1.gennoun()
        snname=type10comma.snoun
        verb,vclass=p1.genverb()
        
        onoun,amount=p1.gennounamount()
        adj=[]
        prep,pro,adj1=p1.genobjphrase()
        period="."
        if type10comma.verb=="paid":
            ophrase=prep+" "+pro+" "+adj1+" "+type10comma.onoun
            sent=type10comma.snoun+" "+verb+" "+amount+" "+ophrase+period
            correctans=sent
           
        else:
            sent=type10comma.snoun+" "+verb+" "+pro+" "+adj1+" "+type10comma.onoun+" "+prep+" "+amount+period
            correctans=sent
            
       
        #--------------------unpunctuate-----------------------------------------------------------------
        punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        #--------------------------------tag unpunctuated text--------------------------------------------
        #Mary bought her adorable bicycle for Rs. 4,300.
        #James paid Rs. 3,500 for his adorable furniture.        
##        #print("correctans",correctans)
##        #print("nopunct",nopunct)
        rskeyword=['Rs']
##        #print("prep",prep)
            
        amount1=re.findall("\d+", nopunct)
        if len(amount1[0])>3:
            number1=amount1[0]
            number=""
        else:
            number=amount1[0]
            number1=""
        #print("nuber",number)  
        onoun=type10comma.onoun
        mylist=nopunct.split(" ")
        taglst=[]
        #print("mylst",mylist)
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            ##print(previous_element, current_element, next_element)

            if current_element in snname and next_element==type10comma.verb:
                    taglst.append(current_element)
                    taglst.append("<w>")

            if current_element ==type10comma.verb and next_element==pro:
                    taglst.append(current_element)
                    taglst.append("<w>")        
            if current_element ==pro and next_element==adj1:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element ==adj1 and next_element==onoun:
                    taglst.append(current_element)
                    taglst.append("<w>")        
            if current_element ==type10comma.verb and next_element==rskeyword[0]:
                    taglst.append(current_element)
                    taglst.append("<w>")
                  
            if current_element ==onoun and next_element==prep:
                    taglst.append(current_element)
                    taglst.append("<w>")
                  
            if current_element ==prep and next_element==rskeyword[0]:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element ==rskeyword[0] and next_element== number or next_element==number1:
                    taglst.append(current_element)
                    taglst.append("<m>")      #=---------------------fullstop mandatory
            if current_element ==number and next_element==prep:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element==number1 and next_element==prep:
    
                    res = number1[:1] + "<m>" + number1[1:]
                   
                    
                    taglst.append(res)
                    taglst.append("<w>")
            if current_element ==prep and next_element==pro:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element==onoun and next_element==None:
                    
                   
                    taglst.append(current_element)
                    taglst.append("<m>")  
            if current_element==number and next_element==None:
                                        
                    taglst.append(current_element)
                    taglst.append("<m>")     
            if current_element==number1 and next_element==None:
                    
                    res = number1[:1] + "<m>" + number1[1:]
                    taglst.append(res)
                    taglst.append("<m>")
                     
            taggedsent="".join(taglst)
            category="comma"
            level="3"
            
           
        ##print(taggedsent)
        return(correctans,nopunct,taggedsent,category,level)            
for i in range(1,6):
        p1=type10comma()
        correctans,nopunct,taggedsent,category,level=p1.gen10sent()
        #print("correctans",taggedsent)
        category="comma"
        level=3
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


                    
##p1=type10comma()
##p1.gen10sent()
