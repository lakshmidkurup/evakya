import xml.etree.ElementTree as ET
import random
import re
class introcomma:
    
    snname=""

    tree='D:\\evakya\\xml\\introductorycomma.xml'
    tree=ET.parse(tree)
    root=tree.getroot()
    verblst=[]
    verb=""
    objclass=""
    
    def genclause1(self):
        # <CLAUSE1 INTRO="while" SNOUn="x" vbz="was" VERBING="x" ECLASS="neutral"/>
        
        for i in introcomma.root[0] :
            if i.tag=="INTRO":
                intro=i.attrib['WORD']
            if i.tag=="SNOUN":
                if i.attrib['TYPE']=="personified":
                    noundict=[]
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                noundict.append(dh[1])

                                ##print(comp.noundict)
                    sname=random.choice(noundict)    
                
            if i.tag=="VERB":
               vbz=i.attrib['VBZ']
               verblst=[]
               eclass=i.attrib["ECLASS"]
               
               with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                   for word in nd:
                       dh=word.split(':')
                        
                       if eclass==dh[2]:
                           
                           introcomma.verblst.append(dh[1])
                   print(introcomma.verblst)
                   introcomma.verblst.remove("met")
                    
                   introcomma.verb=random.choice(introcomma.verblst)
                   
                   
               with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                   for word in nd:
                       dh=word.split(':')
                        
                       if introcomma.verb==dh[1]:
                           introcomma.objclass=dh[0]
                           
                          
                   
                   print("a",introcomma.objclass,introcomma.verb)    
                   
               f=open("D:\\evakya\\dataset\\tense.txt")                        
               for line in f:
                    dh=line.split(":")
                
                    if introcomma.verb==dh[1]:
                        verb1=dh[0]
               if verb1.endswith("e"):
                   verb1=verb1[:-1]
                #print("comp.verb1",comp.verb1)
            
               fp=open("D:\\evakya\\dataset\\noundict.txt")
               
               for line in fp:
                    dh=line.split(":")
                    if introcomma.objclass==dh[0]:
                        onoun=dh[1]
                    
               pattern = '^[aeiou]'
               test_string = onoun
                ##print("test",test_string)
               result = re.match(pattern, test_string)

               if result:
                  ##print("Search successful.")
                  article="an"
               else:
                  ##print("Search unsuccessful.")
                  article="a"     
        verbing=verb1+"ing"     
        print(intro,sname,vbz,verbing,article,onoun)
        return(intro,sname,vbz,verbing,article,onoun)

    def genclause2(self):
        #<CLAUSE2 PRO="I" VERB="x" ONOUN="x" ECLASS="neutral"/>
        for i in introcomma.root:
            if i.tag=="CLAUSE2":
              
                pro=i.attrib['PRO']
                print("verb2",introcomma.verblst)
                introcomma.verblst.remove(introcomma.verb)
                
                verb2=random.choice(introcomma.verblst)
                
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                   for word in nd:
                       dh=word.split(':')
                        
                       if verb2==dh[1]:
                           objclass1=dh[0]
                fd=open("D:\\evakya\\dataset\\noundict.txt")
               
                for line in fd:
                    dh=line.split(":")
                    if objclass1==dh[0]:
                        onoun=dh[1]          
                pattern = '^[aeiou]'
                test_string = onoun
                ##print("test",test_string)
                result = re.match(pattern, test_string)

                if result:
                  ##print("Search successful.")
                  article="an"
                else:
                  ##print("Search unsuccessful.")
                  article="a"
         
                   
                 

                
                print(pro,verb2,article,onoun)
                return(pro,verb2,article,onoun)

    def gensent(self):
        intro,sname,vbz,verbing,article,onoun1=p1.genclause1()
        pro,verb2,article,onoun2=p1.genclause2()
        clause2=pro,verb2,article,onoun2
        s=" "
        correctans=intro.capitalize()+" "+sname+" "+vbz+" "+verbing+" "+article+" "+onoun1+","+" "+s.join(clause2)+"."
        
        print(correctans)
        #--------------------unpunctuate-----------------------------------------------------------------
        punctuations = '''!.()[]{};:'"\,<>/?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        
        ###print(nopunct)
        mylist=nopunct.split(" ")
        
        taglst=[]
        print("mylst",mylist)
        title1=['Dr','Prof']
        #While James was drinking a coffee,I read a story
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            ##print(previous_element, current_element, next_element)
            if current_element ==intro.capitalize() and next_element==sname:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element==sname and next_element==vbz:
                    taglst.append(current_element)
                    taglst.append("<w>")
                    
            if current_element==vbz  and next_element==verbing:
                taglst.append(current_element)
                taglst.append("<w>")
            if current_element ==verbing and next_element==article:
                    taglst.append(current_element)
                    taglst.append("<w>")
                    
            if current_element ==article and next_element ==onoun1:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element ==onoun1 and next_element ==pro:
                    taglst.append(current_element)
                    taglst.append("<m>")
            if current_element ==pro and next_element ==verb2:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element ==verb2 and next_element ==article:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element ==article and next_element ==onoun2:
                    taglst.append(current_element)
                    taglst.append("<w>")        
               
            
            if current_element ==onoun2 and next_element ==None:
                    taglst.append(current_element)
                    taglst.append("<m>")
           
                     
            taggedsent="".join(taglst)
            category="comma"
            level="7"
        print(taggedsent)    
        ###print(correctans,nopunct,taggedsent,category,level)      
        return(correctans,nopunct,taggedsent,category,level)          
for i in range(1,6):
        p1=introcomma()
        correctans,nopunct,taggedsent,category,level=p1.gensent()
        print("correctans",taggedsent)
        category="comma"
        level=7
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


    
     
    
