
import xml.etree.ElementTree as ET
import random
import re


class comp:
    
    sname=""
    noundict=[]
    adj1=""
    oadj1=""
    hverb=""
    verb=""
    verb1=""
    treelst=[]
    cordconj=""
    tree = ET.parse('D:\\evakya\\xml\\type2andtaste.xml')
    
    def generatesubject(self):    
        
        #tree = ET.parse('D:\\evakya\\xml\\type2andtaste.xml')
        root = comp.tree.getroot()
        for i in root[0][0]:
            if i.tag=="SNOUN":
                if i.attrib['TYPE']=="personified":
                
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                comp.noundict.append(dh[1])

                                ##print(comp.noundict)
                        comp.snname=random.choice(comp.noundict)
                        
                return(comp.snname)
            
    def generateadjectivephrase(self):
        #tree = ET.parse('D:\\evakya\\xml\\type2andtaste.xml')
        root = comp.tree.getroot()
        for i in root[0][0][2]:  # SADJECTIVEPHRASE
            ###print(i.tag,i.attrib)
            if i.tag=="SCNOUN":
                cnounlist=[]
                with open("D:\\evakya\\dataset\\cnoun.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        ###print(dh)
                        if comp.snname==dh[1]:
                            cnounlist=dh[2:5]
                                        
                                        ###print(snname1,cnounlist)
                            cnoun=random.choice(cnounlist)
                            ###print("cnoun",cnoun)   
                

        for i in root[0][0][2]:      
            if i.tag=="SADJECTIVE":
                if i.attrib['TYPE']=="personified":
                    adjectivelst=[]
                    with open("D:\\evakya\\dataset\\adjectives.txt") as nd:
                        for word in nd:                        
                            dh=word.split(':')
                            if i.attrib['TYPE']== dh[0]:
                                adjectivelst.append(dh[1])
                    ###print("adjectivelst",adjectivelst)
                    
                    comp.adj1=random.choice(adjectivelst)

            adjphrase=comp.adj1+" "+cnoun        
            return(adjphrase,comp.adj1,cnoun )

    def gensubarticle(self):
        #tree = ET.parse('D:\\evakya\\xml\\type2andtaste.xml')
        root = comp.tree.getroot()
        for i in root[0][0]:  # SARTICLE
            ###print(i.tag,i.attrib)
            if i.tag=="SARTICLE":
                ###print("hi")
#-----------------------------ARTICLE--------------------------------------------------------------------------------------------------------
                
                pattern = '^[aeiou]'
                test_string = comp.adj1
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
        #tree=tree = ET.parse('D:\\evakya\\xml\\type2andtaste.xml')
        root = comp.tree.getroot()
        helpingverbs=["could","will","would","might"]
        for i in root[0][1]: # VERBPHRASE
            if i.tag=="HELPINGVERB":
                 i.attrib['NAME']=random.choice(helpingverbs)
                 comp.hverb=i.attrib['NAME']
        for i in root[0][1]: # VERBPHRASE
            if i.tag=="VERB":
                 comp.verb=i.attrib['VNAME']
        f=open("D:\\evakya\\dataset\\tense.txt")                        
        for line in f:
            dh=line.split(":")
            if comp.verb==dh[0]:
                comp.verb1=dh[1]
                ##print("comp.verb1",comp.verb1)        
        vp=comp.verb1
        return(vp)

    def getobjnoun(self):
        #tree = ET.parse('D:\\evakya\\xml\\type2andtaste.xml')
        root = comp.tree.getroot()
        for i in root[0][2]: # VERBPHRASE
            if i.tag=="ONOUN":
                onounlst=[]
                f=open("D:\\evakya\\dataset\\noundict.txt")                        
                for line in f:
                    dh=line.split(":")
                    if i.attrib['CLASS'] == dh[0]:
                                                
                        onounlst.append(dh[1])
                        ###print(onounlst)
                        i.attrib['NAME']=random.choice(onounlst)
                        onoun=i.attrib['NAME']
                        return(onoun)
                       
    def getobadjphrase(self):
        #tree = ET.parse('D:\\evakya\\xml\\type2andtaste.xml')
        root = comp.tree.getroot()
        for i in root[0][2][2]:  # OADJECTIVEPHRASE
            ###print(i.tag,i.attrib)
            if i.tag=="ONOUN":
                onounlist=[]
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        ###print(dh)
                        if i.attrib['CLASS']==dh[0]:
                            onounlist.append(dh[1])
                onoun=random.choice(onounlist)            
                                        
                                     
                ###print("0noun",onoun)  
        for i in root[0][2][2]:  # SADJECTIVEPHRASE
            ###print(i.tag,i.attrib)
            if i.tag=="OADJECTIVE":
                
                oadjectivelst=[]
                with open("D:\\evakya\\dataset\\adjectives.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        ###print(i.attrib['CLASS'])
                        if i.attrib['CLASS']== dh[0]:
                            oadjectivelst.append(dh[1])
                ###print("oadjectivelst",oadjectivelst)
                
                comp.oadj1=random.choice(oadjectivelst)
                ###print(oadj1)
                
                    
            oadjphrase=comp.oadj1+" "+onoun        
            return(oadjphrase,comp.oadj1,onoun )

    def genobjarticle(self):
        #tree = ET.parse('D:\\evakya\\xml\\type2andtaste.xml')
        root = comp.tree.getroot()
        for i in root[0][2]:  # OARTICLE
            ###print(i.tag,i.attrib)
            if i.tag=="OARTICLE":
                ###print("hi")
#-----------------------------OARTICLE--------------------------------------------------------------------------------------------------------
                pattern = '^[aeiou]'
                test_string = comp.oadj1
                ###print("test",test_string)
                result = re.match(pattern, test_string)

                if result:
                  ###print("Search successful.")
                  oarticle="an"
                else:
                  ###print("Search unsuccessful.")
                  oarticle="a"

                return(oarticle)        
                                                 

    def gencordconj(self):
        #tree = ET.parse('D:\\evakya\\xml\\type2andtaste.xml')
        root = comp.tree.getroot()
        for i in root:  # COORDCONJ
            ###print(i.tag,i.attrib)
            if i.tag=="COORDCONJ":
                comp.cordconj=i.attrib['NAME']
                ###print(cordconj)
                return(comp.cordconj)
                
            
    def genneghelpingverb(self):
        #tree = ET.parse('D:\\evakya\\xml\\type2andtaste.xml')
        root = comp.tree.getroot()
        for i in root[2]:  # neg help
            ###print(i.tag,i.attrib)
            if i.tag=="NEGHELPINGVERB":
                
                nhverb=[comp.hverb+" "+"not"]

                return(nhverb)

                
    def gencoverb(self):
        #tree = ET.parse('D:\\evakya\\xml\\type2andtaste.xml')
        root = comp.tree.getroot()
        for i in root[2]:  # Corelated verb
            ###print(i.tag,i.attrib)
            if i.tag=="COVERB":
                cverb=i.attrib['VNAME']
        f=open("D:\\evakya\\dataset\\tense.txt")                        
        for line in f:
            dh=line.split(":")
            if cverb==dh[0]:
                cverb2=dh[1]
                ##print("compc.verb1",cverb2)          
                return(cverb2)
               
    def genpronoun(self):
        #tree = ET.parse('D:\\evakya\\xml\\type2andtaste.xml')
        root = comp.tree.getroot()
        proclass=""
        for i in root[2]:
            ###print(i.tag,i.attrib)
            if i.tag=="PRONOUN":
                proclass=i.attrib['CLASS']
                if proclass=="openable" or proclass=="drawable" or proclass=="drinkable":
                    pro="it"
               
                    
                    return(pro)
    def type2sentence(self):
        
                            
##        #tree = ET.parse('D:\\evakya\\xml\\type2andtaste.xml')
##        root = comp.tree.getroot()
    ##        ##print(ET.tostring(root, encoding='utf8').decode('utf8'))
        ###print(snname5)
    
        
        snname=p1.generatesubject()
        title=["Dr.","Prof."]
        snname1=random.choice(title)+" "+snname
        adjphrase,comp.adj1,cnoun =p1.generateadjectivephrase()
        article=p1.gensubarticle()
        #article="the"
        vp=p1.genverbphrase()
        onoun=p1.getobjnoun()
        oadjphrase,comp.oadj1,onoun=p1.getobadjphrase()
        #oarticle=p1.genobjarticle()
        oarticle="the"
        cordconj=p1.gencordconj()
        nhverb=p1.genneghelpingverb()
        cverb=p1.gencoverb()
        pro=p1.genpronoun()
        comma=","
        if comp.cordconj=="but":
            s=" "
            type2=snname1+comma+s+article+s+adjphrase+comma+s+vp+comma+s+oarticle+s+oadjphrase+comma+s+cordconj+s+nhverb+s+cverb+s+pro+"."
            correctans=type2
            ##print("text1",correctans)
        elif comp.cordconj=="and":
            s=" "
            type2=snname1+comma+s+article+s+adjphrase+comma+s+vp+s+oarticle+s+oadjphrase+s+cordconj+s+cverb+s+pro+"."
            #print(snname1,article,adjphrase,vp,oarticle,oadjphrase,cordconj,cverb,pro)
            correctans=type2
            ##print("text1",correctans)

       
        #--------------------unpunctuate-----------------------------------------------------------------
        punctuations = '''!.()[]{};:'"\,<>/?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        
        ####print(nopunct)
        mylist=nopunct.split(" ")
        
        taglst=[]
        #print("mylst",mylist)
        title1=['Dr','Prof']
        #Dr.John an adorable orator tasted a hot coffee and gulped it
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            ###print(previous_element, current_element, next_element)
            if current_element in title1 and next_element==snname:
                    taglst.append(current_element)
                    taglst.append("<m>")
            if current_element==snname and next_element==article:
                    taglst.append(current_element)
                    taglst.append("<m>")
                    
            if current_element==article  and next_element==comp.adj1:
                taglst.append(current_element)
                taglst.append("<w>")
            if current_element ==comp.adj1 and next_element==cnoun:
                    taglst.append(current_element)
                    taglst.append("<w>")
                    #----,verb,oartname,oadjp,objnoun,moadvt,oadvt
            if current_element ==cnoun and next_element ==vp:
                    taglst.append(current_element)
                    taglst.append("<m>")
            if current_element ==vp and next_element ==oarticle:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element ==oarticle and next_element ==comp.oadj1:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element ==comp.oadj1 and next_element ==onoun:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element ==onoun and next_element ==cordconj:
                    taglst.append(current_element)
                    taglst.append("<w>")        
               
            
            if current_element ==cordconj and next_element ==cverb:
                    taglst.append(current_element)
                    taglst.append("<w>")
           
            if current_element ==cverb and next_element == pro  :
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element ==pro and next_element == None  :
                    taglst.append(current_element)
                    taglst.append("<m>")            
            taggedsent="".join(taglst)
            category="comma"
            level="6"
        #print(taggedsent)    
        ####print(correctans,nopunct,taggedsent,category,level)      
        return(correctans,nopunct,taggedsent,category,level)          
for i in range(1,3):
        p1=comp()
        correctans,nopunct,taggedsent,category,level=p1.type2sentence()
        print("correctans",correctans)
        category="comma"
        level=6
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
       
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,correctans,taggedsent,category,level,1))
        mydb.commit()        
