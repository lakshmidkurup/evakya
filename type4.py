import xml.etree.ElementTree as ET
import random
import re

class type4:
    sname=""
    noundict=[]
    oadj1=""
    oadj2=""
    cordconj=""
    oarticle=""
    oarticle2=""
    oarticle3=""
    onoun=""
    onoun2=""
    onoun3=""

    def generatesubject(self):    
        
        tree = ET.parse('D:\\evakya\\xml\\itemseperatortype4a.xml')
        root = tree.getroot()
        
        for i in root[0]:
            
            if i.tag=="SNOUN":
                
                if i.attrib['TYPE']=="personified":
                
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                type4.noundict.append(dh[1])

                                ###print(type4.noundict)
                        type4.snname=random.choice(type4.noundict)
                        
                    return(type4.snname)
            
    def generateadjectivephrase(self):
        tree = ET.parse('D:\\evakya\\xml\\itemseperatortype4a.xml')
        root = tree.getroot()
        for i in root[0][2]:  # OADJECTIVEPHRASE
            ###print(i.tag,i.attrib)
            if i.tag=="SCNOUN":
                cnounlist=[]
                with open("D:\\evakya\\dataset\\cnoun.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        ###print(dh)
                        if type4.snname==dh[1]:
                            cnounlist=dh[2:5]
                                        
                                        ###print(snname1,cnounlist)
                            cnoun=random.choice(cnounlist)
                            ###print("cnoun",cnoun)   
                

        for i in root[0][2]:      
            if i.tag=="SADJECTIVE":
                if i.attrib['TYPE']=="personified":
                    adjectivelst=[]
                    with open("D:\\evakya\\dataset\\adjectives.txt") as nd:
                        for word in nd:                        
                            dh=word.split(':')
                            if i.attrib['TYPE']== dh[0]:
                                adjectivelst.append(dh[1])
                    ###print("adjectivelst",adjectivelst)
                    
                    type4.adj1=random.choice(adjectivelst)

            adjphrase=type4.adj1+" "+cnoun        
            return(type4.adj1,cnoun)

    def gensubarticle(self):
        tree = ET.parse('D:\\evakya\\xml\\itemseperatortype4a.xml')
        root = tree.getroot()
        for i in root[0]:  # SARTICLE
            ###print(i.tag,i.attrib)
            if i.tag=="SARTICLE":
               
#-----------------------------ARTICLE--------------------------------------------------------------------------------------------------------
                
                pattern = '^[aeiou]'
                test_string = type4.adj1
                ###print("test",test_string)
                result = re.match(pattern, test_string)

                if result:
                  ###print("Search successful.")
                  article="an"
                else:
                  ###print("Search unsuccessful.")
                  article="a"

                return(article)

    def genverbphrase(self):
        tree=tree = ET.parse('D:\\evakya\\xml\\itemseperatortype4a.xml')
        root = tree.getroot()
        helpingverbs=["could","will","would","might"]
        for i in root[1]: # VERBPHRASE
            if i.tag=="HELPINGVERB":
                 i.attrib['NAME']=random.choice(helpingverbs)
                 type4.hverb=i.attrib['NAME']
        for i in root[1]: # VERBPHRASE
            if i.tag=="VERB":
                 type4.verb=i.attrib['VNAME']
                 ###print(verb)        
        vp=type4.hverb+" "+type4.verb
        return(type4.hverb,type4.verb)
    def getobjphrase1(self):
        tree = ET.parse('D:\\evakya\\xml\\itemseperatortype4a.xml')
        root = tree.getroot()
        for i in root[2]:
            ###print(i.tag,i.attrib)
            
            if i.tag=="ONOUN":
                onounlist=[]
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        ###print(dh)
                        if i.attrib['CLASS']==dh[0]:
                            onounlist.append(dh[1])
                type4.onoun=random.choice(onounlist)
            if i.tag=="OARTICLE":
                
    #-----------------------------OARTICLE--------------------------------------------------------------------------------------------------------
                pattern = '^[aeiou]'
                test_string = type4.onoun
                ##print("test",test_string)
                result = re.match(pattern, test_string)

                if result:
                  ###print("Search successful.")
                  type4.oarticle="an"
                 # ##print(oarticle)
                else:
                  ###print("Search unsuccessful.")
                  type4.oarticle="a"
                  ###print(oarticle)

                
        return(type4.onoun, type4.oarticle)
    def getobjphrase2(self):
    
        tree = ET.parse('D:\\evakya\\xml\\itemseperatortype4a.xml')
        root = tree.getroot()
               
        for i in root[3]:  # OARTICLE
##            ##print(i.tag,i.attrib)     
            if i.tag=="ONOUN":
                onounlist=[]
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        ###print(dh)
                        if i.attrib['CLASS']==dh[0]:
                            onounlist.append(dh[1])
                
            
                m1=[]
                m1.append(type4.onoun)
                
                onounlist=list(set(onounlist) - set(m1))
                
                type4.onoun2=random.choice(onounlist)
##                ##print("onoun",str(type4.onoun2))

            if i.tag=="OARTICLE":
                ###print("hi")
#-----------------------------OARTICLE--------------------------------------------------------------------------------------------------------
                pattern = '^[aeiou]'
                test_string = type4.onoun2
                ###print("test",test_string)
                result = re.match(pattern, test_string)

                if result:
                  ###print("Search successful.")
                  type4.oarticle2="an"
                 # ##print(oarticle)
                else:
                  ###print("Search unsuccessful.")
                  type4.oarticle2="a"
                  ###print(oarticle)        

            

                
        return(type4.onoun2,type4.oarticle2)

    def getobjphrase3(self):
        tree = ET.parse('D:\\evakya\\xml\\itemseperatortype4a.xml')
        root = tree.getroot()
               
        for i in root[4]:  # OARTICLE
            ##print("phrase3",i.tag,i.attrib)
            if i.tag=="ONOUN":
                onounlist=[]
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        ###print(dh)
                        if i.attrib['CLASS']==dh[0]:
                            onounlist.append(dh[1])
                                    
                m1=[]
                m1.append(type4.onoun)                     
                m2=[]
                m2.append(type4.onoun2)
                
                onounlist=list(set(onounlist) - set(m1))
                onounlist=list(set(onounlist) - set(m2))
                
                type4.onoun3=random.choice(onounlist)
       
            if i.tag=="OARTICLE":    
                pattern = '^[aeiou]'
                test_string = type4.onoun3
                ###print("test",test_string)
                result = re.match(pattern, test_string)

                if result:
                  ###print("Search successful.")
                  type4.oarticle3="an"
                 # ##print(oarticle)
                else:
                  ###print("Search unsuccessful.")
                  type4.oarticle3="a"
                  ###print(oarticle3)        

        ##print("o3",type4.onoun3,type4.oarticle3)
        return(type4.onoun3,type4.oarticle3)

    def gencordconj(self):
        tree = ET.parse('D:\\evakya\\xml\\itemseperatortype4a.xml')
        root = tree.getroot()
        for i in root:  # COORDCONJ
            ###print(i.tag,i.attrib)
            if i.tag=="CONJ":
                type4.cordconj=i.attrib['TYPE']
                ###print(cordconj)
                return(type4.cordconj)
    def type4sentence(self):
          
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
        title=["Dr.","Prof."]
       
        adj,cnoun=p1.generateadjectivephrase()
        article=p1.gensubarticle()
        hverb,verb=p1.genverbphrase()
        onoun1,oarticle1=p1.getobjphrase1()
        onoun2,oarticle2=p1.getobjphrase2()
        onoun3,oarticle3=p1.getobjphrase3()
        cordconj=p1.gencordconj()
               
        #------------------------------------if coordinate conj is "and"------------------------------------------------------------------------------
        if type4.cordconj=="and":
            s=" "
            comma=","
            period="."
            text2=snname1+comma+" "+article+" "+adj+" "+cnoun+comma+" "
            type2=hverb,verb,oarticle1,onoun1
            type3=oarticle2,onoun2,cordconj,oarticle3,onoun3
            text1=text2+s.join(type2)+comma+" "+s.join(type3)+period
            text4=text2+hverb+" "+verb+" "+oarticle1+" "+onoun1+" "+cordconj+" "+oarticle2+" "+onoun2+period
            #print("text1",text4)
        correctans=text1
        #--------------------unpunctuate--------------------------------------------------------------------------------------------------------------------
        punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        #--------------------------------tag unpunctuated text------------------------------------------------------------------------------------------------
        #Dr.James a clever orator would open a heavy cage and a red cage
        ##print("correctans",correctans)
        ##print("nopunct",nopunct)   
        title=['Mr','Capt','Major','Bro','Mrs','Miss','Sr']   
        mylist=nopunct.split(" ")
        
        
        taglst=[]
        
      #Major. John, an adorable orator, would open a box ,a cage and a book.
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            ##print(previous_element, current_element, next_element)
            
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
            if current_element == verb and next_element==oarticle1:
                taglst.append(current_element)
                taglst.append("<w>")
               
            if (current_element ==oarticle1) and (next_element ==onoun1):
                taglst.append(current_element)
                taglst.append("<w>")
            if (current_element ==onoun1) and (next_element ==oarticle2):
                taglst.append(current_element)
                taglst.append("<m>")    
            if (current_element ==oarticle2) and (next_element == onoun2):
                taglst.append(current_element)
                taglst.append("<w>")    
            if (current_element ==onoun2) and (next_element == cordconj):
                taglst.append(current_element)
                taglst.append("<w>")
        
            if current_element ==cordconj and (next_element==oarticle3):
                taglst.append(current_element)
                taglst.append("<w>")
            if current_element ==oarticle3 and (next_element==onoun3):
                taglst.append(current_element)
                taglst.append("<w>")    
            if next_element==None:
                taglst.append(current_element)
                taglst.append("<m>")    
        taggedsent="".join(taglst)
        category="comma"
        level="1"
        print(taggedsent)
       
        ##print("correctans",correctans,nopunct,taggedsent,category,level)
        return(correctans,nopunct,taggedsent,category,level)        
    def type42sentence(self):
        

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
        title=["Dr.","Prof."]
       
        adj,cnoun=p1.generateadjectivephrase()
        article=p1.gensubarticle()
        hverb,verb=p1.genverbphrase()
        onoun1,oarticle1=p1.getobjphrase1()
        onoun2,oarticle2=p1.getobjphrase2()
        onoun3,oarticle3=p1.getobjphrase3()
        cordconj=p1.gencordconj()
               
        #------------------------------------if coordinate conj is "and"------------------------------------------------------------------------------
        if type4.cordconj=="and":
            s=" "
            comma=","
            period="."
            text2=snname1+comma+" "+article+" "+adj+" "+cnoun+comma+" "
            type2=hverb,verb,oarticle1,onoun1
            type3=oarticle2,onoun2,cordconj,oarticle3,onoun3
            text1=text2+s.join(type2)+s.join(type3)+period
            text4=text2+hverb+" "+verb+" "+oarticle1+" "+onoun1+" "+cordconj+" "+oarticle2+" "+onoun2+period
            #print("text4",text4)
        correctans=text4
        #--------------------unpunctuate--------------------------------------------------------------------------------------------------------------------
        punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        #--------------------------------tag unpunctuated text------------------------------------------------------------------------------------------------
        #Dr.James a clever orator would open a heavy cage and a red cage
        ##print("correctans",correctans)
        ##print("nopunct",nopunct)   
        title=['Mr','Capt','Major','Bro','Mrs','Miss','Sr']   
        mylist=nopunct.split(" ")       
        taglst=[]
        
        #Major. John, an adorable orator, would open a box ,a cage and a book.
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            ##print(previous_element, current_element, next_element)
            
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
            if current_element == verb and next_element==oarticle1:
                taglst.append(current_element)
                taglst.append("<w>")
               
            if (current_element ==oarticle1) and (next_element ==onoun1):
                taglst.append(current_element)
                taglst.append("<w>")
            if (current_element ==onoun1) and (next_element ==cordconj):
                taglst.append(current_element)
                taglst.append("<w>")    
            if current_element ==cordconj and (next_element==oarticle2):
                taglst.append(current_element)
                taglst.append("<w>")
            if current_element ==oarticle2 and (next_element==onoun2):
                taglst.append(current_element)
                taglst.append("<w>")
                 
            if next_element==None:
                taglst.append(current_element)
                taglst.append("<m>")    
        taggedsent="".join(taglst)
        category="comma"
        level="1"
        print(taggedsent)
       
        ##print("correctans",correctans,nopunct,taggedsent,category,level)
        return(correctans,nopunct,taggedsent,category,level)


for i in range(1,3):
        p1=type4()
        correctans,nopunct,taggedsent,category,level=p1.type42sentence()
       
        category="comma"
        level=1
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
        
    


for i in range(1,4):
        p1=type4()
        correctans,nopunct,taggedsent,category,level=p1.type4sentence()
       
        category="comma"
        level=1
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


