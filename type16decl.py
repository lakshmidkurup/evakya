import xml.etree.ElementTree as ET
import random
import re
import datetime
class type16decl:
    sent=""
    snname=""
    adj1=""
    noundict=[]
    vbz=""
    onoun=""
    verb=""
    title=["Dr.","Prof."]
    title1=random.choice(title)
    opronoun=""
    onounlist=[]
    eml=[]
    verbtype=""
    det="the"
##    tree1 = ET.parse('D:\\evakya\\dataset\\declarative.xml')
##    tree1 = ET.parse('D:\\evakya\\dataset\\declnegative.xml')
    str1='D:\\evakya\\xml\\declarative.xml'
    str2='D:\\evakya\\xml\\declnegative.xml'
    str3=random.choice([str1,str2])
    tree=ET.parse(str3)
    
    
    
    def generatesubject(self):
        
        root = type16decl.tree.getroot()
        
        for i in root[0][0]:
            #print(i.tag)
            if i.tag=="SNOUN":
                
                if i.attrib['TYPE']=="personified":
                

                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                type16decl.noundict.append(dh[1])

                                #print(type5.noundict)
                        type16decl.snname=random.choice(type16decl.noundict)
                        
                    return(type16decl.snname)
                
    def generatesubjectpronoun(self):
        root = type16decl.tree.getroot()
        
        for i in root[0][0]:
            #print(i.tag)
            if i.tag=="SNOUN":
                
                if i.attrib['TYPE']=="personified":
                

                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                if type16decl.snname==dh[1]:
                                    type16decl.opronoun=dh[3]
                                    type16decl.subjpronoun=dh[2]
                    return(type16decl.subjpronoun,type16decl.opronoun) 
    def gensubarticle(self):
        
        root = type16decl.tree.getroot()
        for i in root[0][0]:  # SARTICLE
            #print(i.tag,i.attrib)
            if i.tag=="SARTICLE":
                #print("hi")
#-----------------------------ARTICLE--------------------------------------------------------------------------------------------------------
                
                pattern = '^[aeiou]'
                test_string = type16decl.adj1
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
        #tree = ET.parse('D:\\evakya\\dataset\\type16declintwon.xml')
        #tree = ET.parse('D:\\evakya\\dataset\\type16decl1cook.xml')
        #tree = ET.parse('D:\\evakya\\dataset\\type16declmorever.xml')
        adjectivelst=[]
        root = type16decl.tree.getroot()
        for i in root[0][0][3]:  # OADJECTIVEPHRASE
            #print(i.tag,i.attrib)
            if i.tag=="SCNOUN":
                cnounlist=[]
                with open("D:\\evakya\\dataset\\cnoun.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if type16decl.snname==dh[1]:
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
                    
                    type16decl.adj1=random.choice(adjectivelst)

            adjphrase=type16decl.adj1+" "+cnoun        
            return(adjphrase)
        
    def genverbphrase(self):
        #tree = ET.parse('D:\\evakya\\dataset\\type16declintwon.xml')
        #tree = ET.parse('D:\\evakya\\dataset\\type16decl1cook.xml')
        verblst2=[]
        root = type16decl.tree.getroot()
        
        for i in root[0][1]: # VERBPHRASE
            type16decl.verbtype=i.attrib["VERBTYPE"]
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
            type16decl.vbz=i.attrib['VERBBE']
            type16decl.verb=str(random.choice(verblst2))
            
           
            vp=type16decl.vbz+" "+type16decl.verb
        return(vp)
    
    def getobjnounphrase(self):
        #tree = ET.parse('D:\\evakya\\dataset\\type16declintwon.xml')
        #tree = ET.parse('D:\\evakya\\dataset\\type16decl1cook.xml')
        #tree = ET.parse('D:\\evakya\\dataset\\type16declmorever.xml')
        type16decl.onounlist=[]
        root = type16decl.tree.getroot()
        #---reteieve the class of the verb
        with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
            for word in nd:                        
                dh=word.split(':')
                if type16decl.verb==dh[1]:
                    verbclass=dh[0]
                    #print(verbclass)
        for i in root[0][2]:  # ONOUN
            if i.tag=="ONOUN":
                
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if verbclass==dh[0]:
                           
                            type16decl.onounlist.append(dh[1])
                            
                type16decl.onoun=random.choice(type16decl.onounlist)
                #print(type16decl.onoun)                       
            
        for i in root[0][2]:  # ONOUN
            if i.tag=="ONOUN":
                if type16decl.verbtype=="negative":
##                    type16decl.subjpronoun,type16decl.opronoun=p1.generatesubjectpronoun()
                    i.attrib['DET']=type16decl.opronoun
                else:
                    i.attrib['DET']=type16decl.det
                    
        ophrase=i.attrib['DET']+" "+type16decl.onoun
        return(ophrase)
    
    
    def type16declsentence(self):

    
        snname=p1.generatesubject()
        type16decl.subjpronoun,type16decl.opronoun=p1.generatesubjectpronoun()
        title1=random.choice(['Dr.','Prof.'])
        snname1=title1+" "+snname
        adjphrase=p1.generateadjectivephrase()
        article=p1.gensubarticle()
        vp=p1.genverbphrase()
        ophrase=p1.getobjnounphrase()     
      
       
        s=" "
        comma=","
        period="."
        
        type1=snname1
        type2=article,adjphrase,vp,ophrase
        text1=type1  #----Dr.Mary
        text2=s.join(type2)#---an old lady
       
       
        correctans=snname1+" "+vp+" "+ophrase+period        
        print("level 1.",correctans)
        #--------------------unpunctuate-----------------------------------------------------------------
        punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        #--------------------------------tag unpunctuated text--------------------------------------------
        #Dr.John has lost his books.
           
        mylist=nopunct.split(" ")
        taglst=[]
        for i, element in enumerate(mylist):
                previous_element = mylist[i-1] if i > 0 else None
                current_element = element
                next_element = mylist[i+1] if i < len(mylist)-1 else None
                print(previous_element, current_element, next_element)
                title1=title1[:-1]
                if current_element==title1 and next_element==type16decl.snname:
                        taglst.append(current_element)
                        taglst.append("<m>")
                        print("taglst",taglst)
                if current_element==type16decl.snname and next_element==type16decl.vbz:
                        taglst.append(current_element)
                        taglst.append("<w>")
                if current_element==type16decl.vbz and next_element==type16decl.verb:
                        taglst.append(current_element)
                        taglst.append("<w>")        
                if (current_element==type16decl.verb and next_element==type16decl.opronoun): 
                        taglst.append(current_element)
                        taglst.append("<w>")
                if(current_element==type16decl.verb and next_element=="the"):
                        taglst.append(current_element)
                        taglst.append("<w>")
                if(current_element=="the" and next_element==type16decl.onoun):
                        taglst.append(current_element)
                        taglst.append("<w>")
                        
                if (current_element==type16decl.opronoun and next_element==type16decl.onoun) or (current_element==type16decl.opronoun and next_element==type16decl.onoun):   
                        taglst.append(current_element)
                        taglst.append("<w>")
                if next_element==None:
                        taglst.append(current_element)
                        taglst.append("<m>")
                   
           
        taggedsent="".join(taglst)
        category="fullstop"
        level="2"
        print(correctans,nopunct,taggedsent,category,level)
       

        return(correctans,nopunct,taggedsent,category,level)


for i in range(1,6):
        p1=type16decl()
        correctans,nopunct,taggedsent,category,level=p1.type16declsentence()
        print("correctans",correctans)
        category="fullstop"
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
       
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,correctans,taggedsent,category,level,1))
        #mycursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (1, 'abc', id2,correctans,0,0,0,0,0,datetime.datetime.now(),category,level,0))

        mydb.commit()


##p1=type16decl()
##correctans,nopunct,taggedsent,category,level=p1.type16declsentence()
