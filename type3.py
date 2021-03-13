import xml.etree.ElementTree as ET
import random
import re

class type3:
    sname=""
    noundict=[]
    oadj1=""
    oadj2=""
    cordconj=""
    oarticle=""
    oarticle2=""
    onoun=""

    def generatesubject(self):    
        
        tree = ET.parse('D:\\evakya\\xml\\itemseperatortype3a.xml')
        root = tree.getroot()
        
        for i in root[0]:
            
            if i.tag=="SNOUN":
                
                if i.attrib['TYPE']=="personified":
                
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                type3.noundict.append(dh[1])

                                #print(type3.noundict)
                        type3.snname=random.choice(type3.noundict)
                        
                    return(type3.snname)
            
    def generateadjectivephrase(self):
        tree = ET.parse('D:\\evakya\\xml\\itemseperatortype3a.xml')
        root = tree.getroot()
        for i in root[0][2]:  # OADJECTIVEPHRASE
            #print(i.tag,i.attrib)
            if i.tag=="SCNOUN":
                cnounlist=[]
                with open("D:\\evakya\\dataset\\cnoun.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if type3.snname==dh[1]:
                            cnounlist=dh[2:5]
                                        
                                        #print(snname1,cnounlist)
                            cnoun=random.choice(cnounlist)
                            #print("cnoun",cnoun)   
                

        for i in root[0][2]:      
            if i.tag=="SADJECTIVE":
                if i.attrib['TYPE']=="personified":
                    adjectivelst=[]
                    with open("D:\\evakya\\dataset\\adjectives.txt") as nd:
                        for word in nd:                        
                            dh=word.split(':')
                            if i.attrib['TYPE']== dh[0]:
                                adjectivelst.append(dh[1])
                    #print("adjectivelst",adjectivelst)
                    
                    type3.adj1=random.choice(adjectivelst)

            adjphrase=type3.adj1+" "+cnoun        
            return(type3.adj1,cnoun)

    def gensubarticle(self):
        tree = ET.parse('D:\\evakya\\xml\\itemseperatortype3a.xml')
        root = tree.getroot()
        for i in root[0]:  # SARTICLE
            #print(i.tag,i.attrib)
            if i.tag=="SARTICLE":
                #print("hi")
#-----------------------------ARTICLE--------------------------------------------------------------------------------------------------------
                
                pattern = '^[aeiou]'
                test_string = type3.adj1
                #print("test",test_string)
                result = re.match(pattern, test_string)

                if result:
                  #print("Search successful.")
                  article="an"
                else:
                  #print("Search unsuccessful.")
                  article="a"

                return(article)

    def genverbphrase(self):
        tree=tree = ET.parse('D:\\evakya\\xml\\itemseperatortype3a.xml')
        root = tree.getroot()
        helpingverbs=["could","will","would","might"]
        for i in root[1]: # VERBPHRASE
            if i.tag=="HELPINGVERB":
                 i.attrib['NAME']=random.choice(helpingverbs)
                 type3.hverb=i.attrib['NAME']
        for i in root[1]: # VERBPHRASE
            if i.tag=="VERB":
                 type3.verb=i.attrib['VNAME']
                 #print(verb)        
        vp=type3.hverb+" "+type3.verb
        return(type3.hverb,type3.verb)
    def getobadjphrase1(self):
        tree = ET.parse('D:\\evakya\\xml\\itemseperatortype3a.xml')
        root = tree.getroot()
               
        for i in root[2]:  # OARTICLE
            #print(i.tag,i.attrib)
            if i.tag=="OARTICLE":
                #print("hi")
    #-----------------------------OARTICLE--------------------------------------------------------------------------------------------------------
                pattern = '^[aeiou]'
                test_string = type3.oadj1
                #print("test",test_string)
                result = re.match(pattern, test_string)

                if result:
                  #print("Search successful.")
                  type3.oarticle="an"
                 # print(oarticle)
                else:
                  #print("Search unsuccessful.")
                  type3.oarticle="a"
                  #print(oarticle)
        
            if i.tag=="ONOUN":
                onounlist=[]
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if i.attrib['CLASS']==dh[0]:
                            onounlist.append(dh[1])
                type3.onoun=random.choice(onounlist)            
                                        
                                     
                #print("0noun",onoun)  
        for i in root[2][2]:  # OADJECTIVE
            #print(i.tag,i.attrib)
            if i.tag=="OADJECTIVE":


                 
                oadjectivelst=[]
                with open("D:\\evakya\\dataset\\adjectives.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        #print(i.attrib['CLASS'])
                        if i.attrib['CLASS']== dh[0]:
                            oadjectivelst.append(dh[1])
                #print("oadjectivelst",oadjectivelst)
                
                type3.oadj1=random.choice(oadjectivelst)
                #print(type3.oadj1)
                
                    
                oadjphrase=type3.oarticle+" "+type3.oadj1+" "+type3.onoun        
            #return(oadjphrase)


            return(type3.oarticle,type3.oadj1,type3.onoun)
        
    def getobadjphrase2(self):
        tree = ET.parse('D:\\evakya\\xml\\itemseperatortype3a.xml')
        root = tree.getroot()
               
        for i in root[4]:  # OARTICLE
            #print(i.tag,i.attrib)
            if i.tag=="OARTICLE":
                #print("hi")
#-----------------------------OARTICLE--------------------------------------------------------------------------------------------------------
                pattern = '^[aeiou]'
                test_string = type3.oadj1
                #print("test",test_string)
                result = re.match(pattern, test_string)

                if result:
                  #print("Search successful.")
                  type3.oarticle2="an"
                 # print(oarticle)
                else:
                  #print("Search unsuccessful.")
                  type3.oarticle2="a"
                  #print(oarticle)
        
            if i.tag=="ONOUN":
                onounlist=[]
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if i.attrib['CLASS']==dh[0]:
                            onounlist.append(dh[1])
                            
                onoun2=random.choice(onounlist)            
                                        
                                     
                #print("0noun",type3.onoun)  
        for i in root[4][2]:  # OADJECTIVE
            #print(i.tag,i.attrib)
            if i.tag=="OADJECTIVE":


                 
                oadjectivelst=[]
                with open("D:\\evakya\\dataset\\adjectives.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        #print(i.attrib['CLASS'])
                        if i.attrib['CLASS']== dh[0]:
                            oadjectivelst.append(dh[1])
                #print("oadjectivelst",oadjectivelst)
                oadjectivelst.remove(type3.oadj1)
                type3.oadj2=random.choice(oadjectivelst)
                
                #print(type3.oadj1)
                
                    
                oadjphrase2=type3.oarticle2+" "+type3.oadj2+" "+onoun2      
            #return(oadjphrase)


            return(type3.oarticle2,type3.oadj2,onoun2)        
                                                 

    def gencordconj(self):
        tree = ET.parse('D:\\evakya\\xml\\itemseperatortype3a.xml')
        root = tree.getroot()
        for i in root:  # COORDCONJ
            #print(i.tag,i.attrib)
            if i.tag=="CONJ":
                type3.cordconj=i.attrib['TYPE']
                #print(cordconj)
                return(type3.cordconj)

    def type3sentence(self):
        
        snname=p1.generatesubject()
        with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                
            for word in nd:
                dh=word.split(':')
                
                if snname==dh[1]:
                    sex=dh[4]
        if sex=="M":
            title=['Mr.','Capt.','Major.','Bro.']
        elif sex=="F":
            title=['Mrs.','Miss.','Sr.']
        
        snname1=random.choice(title)+" "+snname
        adj,cnoun=p1.generateadjectivephrase()
        article=p1.gensubarticle()
        hverb,verb=p1.genverbphrase()
        oarticle,oadj,onoun=p1.getobadjphrase1()
        oarticle2,oadj2,onoun2=p1.getobadjphrase2()
        cordconj=p1.gencordconj()
        
        

        
        #------------------------------------if coordinate conj is "and"------------------------------------------------------------------------------
        if type3.cordconj=="and":
            s=" "
            comma=","
            period="."
            text2=snname1+comma+" "+article+" "+adj+" "+cnoun+comma+" "
            type2=hverb,verb,oarticle,oadj,onoun,cordconj,oarticle2,oadj2,onoun2
            text1=text2+s.join(type2)+period
            #print("text1",text1)
        correctans=text1
        #--------------------unpunctuate-----------------------------------------------------------------
        punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        #--------------------------------tag unpunctuated text--------------------------------------------
        #Dr.James a clever orator would open a heavy cage and a red cage
##        print("correctans",correctans)
##        print("nopunct",nopunct)   
        title=['Mr','Capt','Major','Bro','Mrs','Miss','Sr']   
        mylist=nopunct.split(" ")
        
        
        taglst=[]
        
        #Dr. James a clever orator would open a heavy cage and a red cage
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            #print(previous_element, current_element, next_element)
            
            if current_element in title and next_element==snname:
                taglst.append(current_element)
                taglst.append("<m>")
               
            if current_element in snname and next_element==article:
                taglst.append(current_element)
                taglst.append("<m>")

                   
            if current_element ==article and next_element==adj:
                taglst.append(current_element)
                taglst.append("<w>")
                
            if current_element ==adj and next_element==cnoun:
                taglst.append(current_element)
                taglst.append("<w>")
               
          
            if current_element ==cnoun and next_element==hverb:
                taglst.append(current_element)
                taglst.append("<m>")
            if current_element == hverb and next_element==verb:
               
                taglst.append(current_element)
                taglst.append("<w>")
            if current_element == verb and next_element==oarticle:
                taglst.append(current_element)
                taglst.append("<w>")                                    
               
            if (current_element ==oarticle) and (next_element ==oadj):
                taglst.append(current_element)
                taglst.append("<w>")  
             
            if (current_element ==oadj2) and (next_element == onoun2):
                taglst.append(current_element)
                taglst.append("<w>")
            if (current_element ==oadj) and (next_element == onoun):
                taglst.append(current_element)
                taglst.append("<w>")
            if (current_element ==onoun) and next_element==cordconj:
                taglst.append(current_element)
                taglst.append("<w>")    
            if (current_element ==oarticle2) and (next_element == oadj2):
                taglst.append(current_element)
                taglst.append("<w>")       
            if current_element ==cordconj and (next_element==oarticle2):
                taglst.append(current_element)
                taglst.append("<w>")
            if next_element==None:
                taglst.append(current_element)
                taglst.append("<m>")    
        taggedsent="".join(taglst)
        category="comma"
        level="2"
        print(taggedsent)
       

        return(correctans,nopunct,taggedsent,category,level)


for i in range(1,6):
        p1=type3()
        correctans,nopunct,taggedsent,category,level=p1.type3sentence()
        print("correctans",taggedsent)
        print(correctans)
        
        category="comma"
        level=2
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
       
        #mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,correctans,taggedsent,category,level,1))
        mydb.commit()



        
##p1=type3()
##p1.type3sentence()
