import xml.etree.ElementTree as ET
import random
import re

class type9:
    sent=""
    snname=""
    adj1=""
    noundict=[]
    vbz=""
    helpingverbs=["could","will","would","might","can","may"]
    oadj1=""
    onoun=""
    oarticle=""
    coadv=""
    verb=""
    prep="to"
    converb=""
    subjpronoun=""
    opronoun=""
    onounlist=[]
    eml=[]
    verbtype=""
    #tree = ET.parse('D:\\phd\\renewed\\type9positive.xml')
    #
    def generatesubject(self):
        
        root = tree.getroot()
        
        for i in root[0][0]:
            if i.tag=="SNOUN":
                
                if i.attrib['TYPE']=="personified":
                

                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                type9.noundict.append(dh[1])

                                #print(type5.noundict)
                        type9.snname=random.choice(type9.noundict)
                    print(type9.snname)    
                    return(type9.snname)
                
    def generatesubjectpronoun(self):
        root = tree.getroot()
        
        for i in root[0][0]:
            #print(i.tag)
            if i.tag=="SNOUN":
                
                if i.attrib['TYPE']=="personified":
                

                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                if type9.snname==dh[1]:
                                    type9.opronoun=dh[3]
                                    type9.subjpronoun=dh[2]
                    return(type9.subjpronoun,type9.opronoun) 
    def gensubarticle(self):
        
        root = tree.getroot()
        for i in root[0][0]:  # SARTICLE
            #print(i.tag,i.attrib)
            if i.tag=="SARTICLE":
                #print("hi")
#-----------------------------ARTICLE--------------------------------------------------------------------------------------------------------
                
                pattern = '^[aeiou]'
                test_string = type9.adj1
                #print("test",test_string)
                result = re.match(pattern, test_string)

                if result:
                  #print("Search successful.")
                  article="an"
                else:
                  #print("Search unsuccessful.")
                  article="a"

                return(article)
            
    
    def generateadjectivephrase(self):
        #tree = ET.parse('D:\\phd\\renewed\\type9intwon.xml')
        #tree = ET.parse('D:\\phd\\renewed\\type91cook.xml')
        #tree = ET.parse('D:\\phd\\renewed\\type9morever.xml')
        root = tree.getroot()
        for i in root[0][0][3]:  # OADJECTIVEPHRASE
            #print(i.tag,i.attrib)
            if i.tag=="SCNOUN":
                cnounlist=[]
                with open("D:\\evakya\\dataset\\cnoun.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if type9.snname==dh[1]:
                            cnounlist=dh[2:5]
                                        
                            #print("snname",cnounlist)
                            cnoun=random.choice(cnounlist)
                            #print("cnoun",cnoun)   
                

        for i in root[0][0][3]:      
            if i.tag=="SADJECTIVE":
                if i.attrib['TYPE']=="personified":
                    adjectivelst=[]
                    with open("D:\\evakya\\dataset\\adjectives.txt") as nd:
                        for word in nd:                        
                            dh=word.split(':')
                            if i.attrib['TYPE']== dh[0]:
                                adjectivelst.append(dh[1])
                    #print("adjectivelst",adjectivelst)
                    
                    type9.adj1=random.choice(adjectivelst)

            adjphrase=type9.adj1+" "+cnoun        
            return(type9.adj1,cnoun)
        
    def genverbphrase(self):
        #tree = ET.parse('D:\\phd\\renewed\\type9intwon.xml')
        #tree = ET.parse('D:\\phd\\renewed\\type91cook.xml')
        verblst2=[]
        root = tree.getroot()
        
        for i in root[0][1]: # VERBPHRASE
            type9.verbtype=i.attrib["VERBTYPE"]
            #print(i.tag,i.attrib)
            if i.tag=="VERB":
                if i.attrib['VERBTYPE']=="positive" or i.attrib['VERBTYPE']=="negative" :
                    #print("hi")
                    with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                        for word in nd:                        
                            dh=word.split(':')
                            if i.attrib['VERBTYPE']==dh[2]:
                                verblst2.append(dh[1])
                            
                        #print(verblst2)            
            type9.vbz=i.attrib['VERBBE']
            type9.verb=str(random.choice(verblst2))
            
            
            vp=type9.vbz+" "+type9.verb
        return(type9.vbz,type9.verb)
    
    def getobjnounphrase(self):
        #tree = ET.parse('D:\\phd\\renewed\\type9intwon.xml')
        #tree = ET.parse('D:\\phd\\renewed\\type91cook.xml')
        #tree = ET.parse('D:\\phd\\renewed\\type9morever.xml')
        root = tree.getroot()
        #---reteieve the class of the verb
        with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
            for word in nd:                        
                dh=word.split(':')
                if type9.verb==dh[1]:
                    verbclass=dh[0]
                    #print(verbclass)
        for i in root[0][2]:  # ONOUN
            if i.tag=="ONOUN":
                
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if verbclass==dh[0]:
                           
                            type9.onounlist.append(dh[1])
                            
                type9.onoun=random.choice(type9.onounlist)
                #print(type9.onoun)                       
            
        for i in root[0][2]:  # ONOUN
            if i.tag=="ONOUN":
                if type9.verbtype=="negative":
##                    type9.subjpronoun,type9.opronoun=p1.generatesubjectpronoun()
                    i.attrib['DET']=type9.opronoun
                else:
                    i.attrib['DET']="the"
                    
        ophrase=i.attrib['DET']+" "+type9.onoun
        return(i.attrib['DET'],type9.onoun)
    
    def geninterjection(self):
        #tree = ET.parse('D:\\phd\\renewed\\type71read.xml')
        #tree = ET.parse('D:\\phd\\renewed\\type71cook.xml')
        root = tree.getroot()
        for i in root[1]:
            if i.tag=="TYPE":
                with open("D:\\evakya\\dataset\\interjections.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if i.attrib['EMOTION']==dh[1]:
                            type9.eml.append(dh[2])
                            
                type9.eml1=random.choice(type9.eml)
                
                i.attrib['NAME']=type9.eml1
        return(i.attrib['NAME'])           
               
    def type9sentence(self):

    
        snname=p1.generatesubject()
        type9.subjpronoun,type9.opronoun=p1.generatesubjectpronoun()
        title=["Dr.","Prof."]
        snname1=random.choice(title)+snname
        adjphrase=p1.generateadjectivephrase()
        article=p1.gensubarticle()
        vp=p1.genverbphrase()
        ophrase=p1.getobjnounphrase()     
        interjn=p1.geninterjection()
       
        s=" "
        comma=","
        period="."
        exclamation="!"
        type1=snname1
        type2=article,adjphrase,vp,ophrase
        text1=type1  #----Dr.Mary
        text2=s.join(type2)#---an old lady
        n = int(input("Enter the level: ")) 
        if n==1:
            sentence1=interjn+exclamation+type9.subjpronoun.capitalize()+" "+vp+" "+ophrase+period
            sentence2=interjn+comma+type9.subjpronoun+" "+vp+" "+ophrase+exclamation
            sentence3=interjn+exclamation+type9.subjpronoun.capitalize()+" "+vp+" "+ophrase+exclamation
            print("level 1.",sentence1)
            print("12.",sentence2)
            print("13.",sentence3)
            return(sentence1,sentence2,sentence3)
        elif n==2:
            sentence1=interjn+exclamation+type1+comma+text2+period
            sentence2=interjn+comma+type1+comma+text2+exclamation
            sentence3=interjn+exclamation+type1+comma+text2+exclamation
            print("level 2.",sentence1)
            print("22.",sentence2)
            print("23.",sentence3)
            return(sentence1,sentence2,sentence3)
      
        elif n==3:
            from type9whexcl import type9excl as tex
            tex.type9sentence(self)
        elif n==4:        
            from type9mid import type9mid as tem
            tem.type9midsentence(self)
        elif n==5:
            from type9endsurprise import type9end as te
            te.type9endsentence(self)
        elif n==6:
            sentence1=type9.subjpronoun.capitalize()+" "+vp+" "+ophrase+period+interjn+exclamation
            sentence2=interjn+comma+type9.subjpronoun+" "+vp+" "+ophrase+period+interjn+exclamation
            sentence3=type9.subjpronoun.capitalize()+" "+vp+" "+ophrase+exclamation+interjn+exclamation
            print("Interjection at the end of the sentence:Option1:",sentence1)
            print("option2:",sentence2)
            print("option3.",sentence3)
            return(sentence1,sentence2,sentence3)
        elif n==7:
            sentence1=type1+comma+text2+period+interjn+exclamation
            sentence2=type1+comma+text2+comma+interjn+exclamation
            sentence3=type1+comma+text2+exclamation+interjn+exclamation
            print("Exclamation At the end.")
            print("Option1",sentence1)
            print("Option 2.",sentence2)
            print("Option 3.",sentence3)
            return(sentence1,sentence2,sentence3)
        elif n==8:
            from type9ohmyg import type9ohmyg as toh
            toh.gentype9ohmyg(self)
        elif n==9:
            intlst=['Stop!','Wait!','Get Lost!','I said no!','Like it? I LOVE it!','Hey, you!',"Let's go!"]
            interjn=random.choice(intlst)
            print(interjn)
            return(interjn)
##p1=type9()
##p1.type9sentence()
for i in range(0,2):
        tree = ET.parse('D:\\evakya\\xml\\type9positive.xml')
        p1=type9()
        snname=p1.generatesubject()
        type9.subjpronoun,type9.opronoun=p1.generatesubjectpronoun()
        title=["Dr","Prof"]
        snname1=random.choice(title)+snname
        type9.adj1,cnoun =p1.generateadjectivephrase()
        article=p1.gensubarticle()
        type9.vbz,type9.verb=p1.genverbphrase()
        det,type9.onoun=p1.getobjnounphrase()     
        interjn=p1.geninterjection()       
        s=" "
        comma=","
        period="."
        exclamation="!"
##        sentence1=interjn+exclamation+random.choice(title)+"."+" "+snname+comma+" "+article+" "+type9.adj1+" "+cnoun+" "+type9.vbz+" "+type9.verb+" "+det+" "+type9.onoun+period
##        taggedsent1=interjn+"<m>"+random.choice(title)+"<m>"+snname+"<m>"+article+"<w>"+type9.adj1+"<w>"+cnoun+"<w>"+type9.vbz+"<w>"+type9.verb+"<w>"+det+"<w>"+type9.onoun+"<m>"
        sentence2=interjn+comma+" "+random.choice(title)+"."+" "+snname+comma+" "+article+" "+type9.adj1+" "+cnoun+comma+" "+type9.vbz+" "+type9.verb+" "+det+" "+type9.onoun+exclamation
        taggedsent2=interjn+"<c>"+random.choice(title)+"<m>"+snname+"<m>"+article+"<w>"+type9.adj1+"<w>"+cnoun+"<m>"+type9.vbz+"<w>"+type9.verb+"<w>"+det+"<w>"+type9.onoun+"<c>"
        
##        print("level 2.",sentence1,taggedsent1)
##        print("22.",sentence2,taggedsent2)
        punctuations = '''!()[]{};:'"\,<>.?@#$%^&*_~'''
        nopunct=""
        for char in sentence2:
            if char not in punctuations:
                nopunct = nopunct + char
        
        import mysql.connector
    
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="rohith@123",
                database="pythonlogin"
        )
        mycursor = mydb.cursor()
        level=2
        category="exclamation"
        mycursor.execute("select max(exerciseid) from sentencedb")  
        rows = mycursor.fetchall()
        for row in rows:
                id1=0
                id1=row[0]
                #####print("id1:",row[0])
        id2=id1+1
        
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sentence2,taggedsent2,category,level,1))
        mydb.commit() 

for i in range(0,2):
        tree = ET.parse('D:\\evakya\\xml\\type9negative.xml')
        p1=type9()
        snname=p1.generatesubject()
        type9.subjpronoun,type9.opronoun=p1.generatesubjectpronoun()
        title=["Dr","Prof"]
        snname1=random.choice(title)+snname
        type9.adj1,cnoun =p1.generateadjectivephrase()
        article=p1.gensubarticle()
        type9.vbz,type9.verb=p1.genverbphrase()
        onoun=""
        det,type9.onoun=p1.getobjnounphrase()     
        interjn=p1.geninterjection()       
        s=" "
        comma=","
        period="."
        exclamation="!"            
        sent1=interjn+exclamation+" "+random.choice(title)+"."+" "+snname+comma+" "+article+" "+type9.adj1+" "+cnoun+comma+" "+type9.vbz+" "+type9.verb+" "+det+" "+type9.onoun+period
        taggedsent1=interjn+"<c>"+random.choice(title)+"<m>"+snname+"<m>"+article+"<w>"+type9.adj1+"<w>"+cnoun+"<m>"+type9.vbz+"<w>"+type9.verb+"<w>"+det+"<w>"+type9.onoun+"<c>"
##        sent2=interjn+comma+" "+random.choice(title)+"."+" "+snname+comma+" "+article+" "+type9.adj1+" "+cnoun+" "+type9.vbz+" "+type9.verb+" "+det+" "+type9.onoun+exclamation
##        taggedsent2=interjn+"<m>"+random.choice(title)+"<m>"+snname+"<m>"+article+"<w>"+type9.adj1+"<w>"+cnoun+"<w>"+type9.vbz+"<w>"+type9.verb+"<w>"+det+"<w>"+type9.onoun+"<m>"
##        
       
        punctuations = '''!()[]{};:'"\,<>.?@#$%^&*_~'''
        nopunct=""
        for char in sent1:
            if char not in punctuations:
                nopunct = nopunct + char
        
        import mysql.connector
    
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="rohith@123",
                database="pythonlogin"
        )
        mycursor = mydb.cursor()
        level=2
        category="exclamation"
        mycursor.execute("select max(exerciseid) from sentencedb")  
        rows = mycursor.fetchall()
        for row in rows:
                id1=0
                id1=row[0]
                #####print("id1:",row[0])
        id2=id1+1
        
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent1,taggedsent1,category,level,1))
        mydb.commit() 

        
##        punctuations = '''!()[]{};:'"\,<>.?@#$%^&*_~'''
##        nopunct=""
##        for char in sent2:
##            if char not in punctuations:
##                nopunct = nopunct + char
##        
##        import mysql.connector
##    
##        mydb = mysql.connector.connect(
##                host="localhost",
##                user="root",
##                passwd="rohith@123",
##                database="pythonlogin"
##        )
##        mycursor = mydb.cursor()
##        level=2
##        category="exclamation"
##        mycursor.execute("select max(exerciseid) from sentencedb")  
##        rows = mycursor.fetchall()
##        for row in rows:
##                id1=0
##                id1=row[0]
##                #####print("id1:",row[0])
##        id2=id1+1
##        
##        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent2,taggedsent2,category,level,1))
##        mydb.commit() 

for i in range(0,1):
        tree = ET.parse('D:\\evakya\\xml\\type9positive.xml')
        p1=type9()
        snname=p1.generatesubject()
        type9.subjpronoun,type9.opronoun=p1.generatesubjectpronoun()
        title=["Dr","Prof"]
        snname1=random.choice(title)+snname
        type9.adj1,cnoun =p1.generateadjectivephrase()
        article=p1.gensubarticle()
        type9.vbz,type9.verb=p1.genverbphrase()
        det,type9.onoun=p1.getobjnounphrase()     
        interjn=p1.geninterjection()       
        s=" "
        comma=","
        period="."
        exclamation="!"
        level=2
        category="exclamation" 
        sent=interjn+exclamation+" "+random.choice(title)+"."+" "+snname+comma+" "+article+" "+type9.adj1+" "+cnoun+comma+" "+type9.vbz+" "+type9.verb+" "+det+" "+type9.onoun+period
        taggedsent=interjn+"<c>"+random.choice(title)+"<m>"+snname+"<m>"+article+"<w>"+type9.adj1+"<w>"+cnoun+"<m>"+type9.vbz+"<w>"+type9.verb+"<w>"+det+"<w>"+type9.onoun+"<c>"
        punctuations = '''!()[]{};:'"\,<>.?@#$%^&*_~'''
        nopunct=""
        for char in sent:
            if char not in punctuations:
                nopunct = nopunct + char
        
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

     
