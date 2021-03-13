import xml.etree.ElementTree as ET
import random
import re

        
class declneutral:
        tree = ET.parse('D:\\evakya\\xml\\declneutral.xml')
        noundict=[]
        snname=""
        verb=""
        eml=[]
        em=""
        verb=""
        onounlist=[]
        onoun=""
        adj=""
        sent=""
        no_punct=""
        article=""
        taggedsent=""
        id2=""
        category="fullstop"
      
        def gensnoun(self):
                root = declneutral.tree.getroot()
    
                for i in root:
                ###print(i.tag)
                        if i.tag=="SNOUN":
            
                                if i.attrib['TYPE']=="personified":
            
                                        with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                                                for word in nd:
                                                        dh=word.split(':')
                                                        if i.attrib['TYPE'] == dh[0]:
                                                            declneutral.noundict.append(dh[1])

                                                    ###print(type5.noundict)
                                declneutral.snname=random.choice(declneutral.noundict)
                                ###print(declneutral.snname)
                                return(declneutral.snname)
                            
        def genverb(self):
                root = declneutral.tree.getroot()

                verblst=[]
                for i in root:
                ###print(i.tag,i.attrib)
                        if i.tag=="VERB":
                                if i.attrib['ECLASS']=="neutral":

                                        with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                                                for word in nd:                        
                                                        dh=word.split(':')
                                                                ###print(dh)
                                                        if i.attrib['ECLASS']==dh[2]:
                                                                verblst.append(dh[1])
                                                declneutral.verb=random.choice(verblst)
                                                             

                print("verb",declneutral.verb)
                return(declneutral.verb)

    

        def genobjnoun(self):
                root=declneutral.tree.getroot()
                declneutral.onounlist=[]
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                        for word in nd:                        
                                dh=word.split(':')
                                if declneutral.verb==dh[1]:
                                        verbclass=dh[0]
                                        
##                                      print(verbclass)
                for i in root:  # ONOUN
                        if i.tag=="ONOUN":
                    
                                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                    
                                        for word in nd:
                                                dh=word.split(':')
                                                ###print(dh)
                                                if verbclass==dh[0]:
                               
                                                        declneutral.onounlist.append(dh[1])
##                                #print("list",  declneutral.onounlist)
                                
                                declneutral.onoun=random.choice(declneutral.onounlist)
                                print("onoun is:",declneutral.onoun)
                    
                    
        
                                with open("D:\\evakya\\dataset\\adjectives.txt") as nd:
                                        adjlst=[]
                                        for word in nd:
                                                dh=word.split(':')
                                                ###print(dh)
                                                if verbclass==dh[0]:
                                               
                                                        adjlst.append(dh[1])
                                        
                        
                declneutral.adj=random.choice(adjlst)
                #print("adj is",declneutral.adj)

                pattern = '^[aeiou]'
                test_string = declneutral.adj
                #print("test",test_string)
                result = re.match(pattern, test_string)

                if result:
                        ###print("Search successful.")
                        declneutral.article="an"
                else:
                        ###print("Search unsuccessful.")
                        declneutral.article="a"    
                nadj=declneutral.article+" "+declneutral.adj
                nobjnoun=declneutral.onoun

                return(declneutral.article,declneutral.adj,nobjnoun)
        def declneutralsentence(self):
                
        
                snoun=p1.gensnoun()
                declneutral.verb=p1.genverb()
                art,nadj,nobjnoun=p1.genobjnoun()
                #print(snoun,declneutral.verb,nadj,nobjnoun)
                period="."
                correctans=snoun+" "+declneutral.verb+" "+art+" "+nadj+" "+nobjnoun+period
            
                #--------------------unpunctuate-----------------------------------------------------------------
                punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
                declneutral.no_punct = ""
                for char in correctans:
                        if char not in punctuations:
                                declneutral.no_punct = declneutral.no_punct + char
                nopunct=declneutral.no_punct 
               
                #-------------------tag unpunctuated text--------------------------------------------

                #['John', 'read', 'a', 'fascinating', 'nonfictional', 'book']
                mylist=nopunct.split(" ")
               
                taglst=[]
                for i, element in enumerate(mylist):
                        previous_element = mylist[i-1] if i > 0 else None
                        current_element = element
                        next_element = mylist[i+1] if i < len(mylist)-1 else None
                        #print(previous_element, current_element, next_element)
                        if current_element==snoun and next_element==declneutral.verb:
                                taglst.append(current_element)
                                taglst.append("<w>")
                        if (current_element==declneutral.verb and next_element==declneutral.article):
                                taglst.append(current_element)
                                taglst.append("<w>")
                        if current_element==declneutral.article and next_element==declneutral.adj:   
                                taglst.append(current_element)
                                taglst.append("<w>")
                        if current_element==declneutral.adj and next_element==nobjnoun:   
                                taglst.append(current_element)
                                taglst.append("<w>")
                        if next_element==None:
                                taglst.append(current_element)
                                taglst.append("<m>")
                           
                   
                taggedsent="".join(taglst)
                category="fullstop"
                level="1"
                #print(correctans,nopunct,taggedsent,category,level)
       

                return(correctans,nopunct,taggedsent,category,level)
        def sqlinsert(self):
                correctans,nopunct,taggedsent,category,level=p1.declneutralsentence()
                #print(correctans,nopunct,taggedsent,category,level)
                category="fullstop"
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
                        print("id1:",row[0])
                declneutral.id2=id1+1
                        
                
        #-----------------------------insert into database------------------------------------------------------------------------------------------------------------------   
                #mycursor.execute("insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category) values ( %d, %s, %s, %s, %s )")
                mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s,%s, %s, %s, %s, %s, %s )', (declneutral.id2,nopunct,correctans,taggedsent,category,level,1))
                mydb.commit()
        
 
for i in range(1,6):
        p1=declneutral()  
        correctans,nopunct,taggedsent,category,level=p1.declneutralsentence()
        print(correctans)
        category="fullstop"
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
                print("id1:",row[0])
        declneutral.id2=id1+1
                
        
       #-----------------------------insert into database------------------------------------------------------------------------------------------------------------------   
        #mycursor.execute("insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category) values ( %d, %s, %s, %s, %s )")
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s,%s, %s, %s, %s, %s, %s )', (declneutral.id2,nopunct,correctans,taggedsent,category,level,1))
        mydb.commit()


