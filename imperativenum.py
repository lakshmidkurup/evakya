import xml.etree.ElementTree as ET
import random
import re
class type17num:
    sname=""
    noundict=[]
    onounlist=[]
    eclass=""
    verb=""
    verbclass=""
    str1='D:\\evakya\\xml\\impposintn.xml'
    str2='D:\\evakya\\xml\\impnegintn.xml'
    str3='D:\\evakya\\xml\\impnumeric.xml'
    str4=random.choice([str1,str2,str3])
    tree=ET.parse(str4)
   ##    tree=ET.parse('D:\\evakya\\dataset\\impposintn.xml')
##    tree=ET.parse('D:\\evakya\\dataset\\impnegintn.xml')
##    tree=ET.parse('D:\\evakya\\dataset\\impnumeric.xml')
    root = tree.getroot()
    def genverb(self):
        root = type17num.tree.getroot()
        
        verblst=[]
        for i in root:
            ##print(i.tag,i.attrib)
            if i.tag=="VERB":
                type17num.eclass=i.attrib['ECLASS']
                if i.attrib['ECLASS']=="numeric" or i.attrib['ECLASS']=="interactionpositive" or i.attrib['ECLASS']=="interactionnegative":                   
                    with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                        for word in nd:                        
                            dh=word.split(':')
                        ##print(dh)
                            if i.attrib['ECLASS']==dh[2]:
                                verblst.append(dh[1])
                    type17num.verb=random.choice(verblst)
                    ##print("verbis",type17num.verb)
                    with open("D:\\evakya\\dataset\\tense.txt") as nd:
                        for word in nd:                        
                            dh=word.split(':')
                       
                            if type17num.verb==dh[1]:
                                presentverb=dh[0]

        ##print(presentverb)
        return(presentverb)
        
    def gendet(self):#----Avoid "the" for personified nouns
        root = type17num.tree.getroot()       
        for i in root:
            
            ##print(i.tag,i.attrib)
            if i.tag=="DET":
                
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        ##print(dh)
                        if type17num.verb==dh[1]:
                            type17num.verbclass=dh[0]
                    ##print("verbclass",type17num.verbclass)
                if type17num.verbclass=="personified":
                    det=str('')
                else:    
                    det="the"
        ##print("det is",det)
                
        return(det)
        
           
    def genobjnoun(self):
        root=type17num.tree.getroot()
        with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
            for word in nd:                        
                dh=word.split(':')
                if type17num.verb==dh[1]:
                    type17num.verbclass=dh[0]
            ##print(type17num.verbclass)
        for i in root:  # ONOUN
            if i.tag=="ONOUN":
                
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        ##print(dh)
                        if type17num.verbclass==dh[0]:
                           
                            type17num.onounlist.append(dh[1])                            
        type17num.onoun=random.choice(type17num.onounlist)
        ##print(type17num.onoun)
        return(type17num.onoun)
    def genprep(self):
        root = type17num.tree.getroot()


        for i in root:
            ##print(i.tag,i.attrib)
            if i.tag=="PREP":
                with open("D:\\evakya\\dataset\\preposition.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            ##print(dh)
                            if type17num.verb==dh[1]:
                                prep=dh[0]
                ##print(prep)
                return(prep)    
    def gensent(self):        
        period="."
        verb=p1.genverb()
        onoun=p1.genobjnoun()
        det=p1.gendet()
        prep=p1.genprep()       
        sent=verb.capitalize()+" "+prep+" "+det+" "+onoun+period
        correctans=re.sub(' +'," ",sent)
        
        #--------------------unpunctuate-----------------------------------------------------------------
        punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        #--------------------------------tag unpunctuated text--------------------------------------------
        #Pay for the furniture.
           
        mylist=nopunct.split(" ")
        ##print("mulist",mylist)
        taglst=[]
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            #print(previous_element, current_element, next_element)
            verb1=verb.capitalize()
            ##print("verb",verb1)
            if current_element==verb1 and next_element==onoun:
                taglst.append(current_element)
                taglst.append("<w>")
            if current_element==verb1 and next_element==det:
                taglst.append(current_element)
                taglst.append("<w>")    
            if current_element==verb1 and next_element==prep:
                taglst.append(current_element)
                taglst.append("<w>")
            if (current_element==prep and next_element==det) or (current_element==prep and next_element==onoun):
                taglst.append(current_element)
                taglst.append("<w>")
            if current_element==det and next_element==onoun:
                taglst.append(current_element)
                taglst.append("<w>")        
            
            if next_element==None:
                taglst.append(current_element)
                taglst.append("<m>")
               
           
        taggedsent="".join(taglst)
        category="fullstop"
        level="3"
        print(correctans,nopunct,taggedsent,category,level)
       

        return(correctans,nopunct,taggedsent,category,level)
for i in range(1,3):    
        p1=type17num()
        correctans,nopunct,taggedsent,category,level=p1.gensent()
        ##print("correctans",correctans)
        category="fullstop"
        level=3
        import mysql.connector

        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="rohith@123",
                database="pythonlogin"
        )
        mycursor = mydb.cursor()
        level=3
        mycursor.execute("select max(exerciseid) from sentencedb")
        rows = mycursor.fetchall()
        for row in rows:
                id1=0
                id1=row[0]
                #print("id1:",row[0])
        id2=id1+1
                
        
#-----------------------------insert into database-----------------------------------------------------------------------------------------------------------------------------------   
        #mycursor.execute("insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category) values ( %d, %s, %s, %s, %s )")
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s,%s )', (id2,nopunct,correctans,taggedsent,category,level,1))
        mydb.commit()




    
#correctans,nopunct,taggedsent,category,level=p1.gensent()
