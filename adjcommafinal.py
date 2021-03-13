import xml.etree.ElementTree as ET
import random
import re
#from adjcommafinal2 import acomma2 as ac2
class acomma:
##    tree = ET.parse('D:\\phd\\renewed\\adjcomma.xml') #--The question, Alice answered is difficult and intelligent.
##    tree = ET.parse('D:\\phd\\renewed\\adjcomma3.xml') #--The novel, Mary read is short, interesting and selective.
    tree2 = ET.parse('D:\\evakya\\xml\\adjcomma4.xml') #----The poem, Alice wrote is lovely, fascinating, short and precise.
##    tree = ET.parse('D:\\phd\\renewed\\adjcommap2.xml')#-The job, John got is demanding and ambitious.
##    tree = ET.parse('D:\\phd\\renewed\\adjcommap3.xml')#---The position, Mary achieved is exceptional, high-grade and excellent.
##    tree = ET.parse('D:\\phd\\renewed\\adjcommap4.xml')#The second-prize, Alice secured is exceptional, high-grade and excellent.
##    tree = ET.parse('D:\\phd\\renewed\\adjcomman2.xml')#-The leg, Mary hurt is fractured and sprained.
##    tree = ET.parse('D:\\phd\\renewed\\adjcomman3.xml')#The books, Alice lost are precious, expensive and valuable.
    tree1 = ET.parse('D:\\evakya\\xml\\adjcomman4.xml')#The books, John lost are precious, expensive, valuable and worthy.
    treelst=[]
    treelst.append(tree1)
    treelst.append(tree2)
    tree=random.choice(treelst)
    root=tree.getroot()
    verb=""
    verbclass=""
    adlst=[]
    vbz=""
    onoun=""
    def gensnoun(self):
        noundict=[]
        for i in acomma.root:
            if i.tag=="DET":
                det="The"
            if i.tag=="SNOUN":
                if i.attrib['TYPE']=="personified":
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                noundict.append(dh[1])
                snname=random.choice(noundict)
                return(snname)
               
    def genverb(self):
        for i in acomma.root:
            if i.tag=="VERB":
                verblst=[]
                acomma.eclass=i.attrib["ECLASS"]
                
                
                ##print("vclass",abbr.vclass)
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        ##print(dh)
                        if acomma.eclass==dh[2]:
                            verblst.append(dh[1])
                acomma.verb=random.choice(verblst)
               
                #print(acomma.verb)
               
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        ##print(dh)
                        if acomma.verb==dh[1]:
                            acomma.verbclass=dh[0]
                   
                #print(acomma.verbclass)            
                return(acomma.verb)

    
    def genadj(self):
        for i in acomma.root:
            if i.tag=="ADJLST":
               acomma.adlst=[]
                
               with open("D:\\evakya\\dataset\\adjectives.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        ##print(dh)
                        if acomma.verbclass==dh[0]:

                           acomma.adlst.append(dh[1])
            adj=[]               
            adj=acomma.adlst           
            comma=","
            if i.tag=="ADJLST":
                res=""
                if i.attrib['MINCOUNT']=="4" and i.attrib['MAXCOUNT']=="4":
                    
                    res=adj[0]+comma+" "+adj[1]+comma+" "+adj[2]+" "+"and"+" "+adj[3]
                elif i.attrib['MINCOUNT']=="3" and i.attrib['MAXCOUNT']=="4":
                    res=adj[0]+comma+" "+adj[1]+" "+"and"+" "+adj[2]
                elif i.attrib['MINCOUNT']=="2" and i.attrib['MAXCOUNT']=="4":
                    res=adj[0]+" "+"and"+" "+adj[1]
               
            
             
        #print(res)
        return(res)
             
    def gendet(self):
       
        for i in acomma.root:
            ##print(i.attrib)
            if i.tag=="DET":
               det=i.attrib['NAME']
               #print(det)
               return(det)
               
##    def genadjlst(self):
##       
##        for i in acomma.root:
##            #print(i.attrib)
##            if i.tag=="ADJLST":
##                #print(i.attrib)
##               
##                with open("D:\\phd\\renewed\\adjectives.txt") as nd:
##                    for word in nd:
##                        dh=word.split(':')
##                        #print(dh)
##                        if acomma.verbclass==dh[0]:
##                           acomma.adlst.append(dh[1])
##            comma=","
##            if i.attrib['MINCOUNT']=="4" and i.attrib['MAXCOUNT']=="4":
##                
##                res=adj[0]+comma+" "+adj[1]+comma+" "+adj[2]+comma+" "+"and"+" "+adj[3]
##            elif i.attrib['MINCOUNT']=="3" and i.attrib['MAXCOUNT']=="4":
##                res=adj[0]+comma+" "+adj[1]+comma+" "+"and"+" "+adj[2]
##            elif i.attrib['MINCOUNT']=="2" and i.attrib['MAXCOUNT']=="4":
##                res=adj[0]+comma+" "+"and"+adj[1]
##           
##                        
##            #print(res)
##            return(res)
##            
    def genonoun(self):
        for i in acomma.root:      
            if i.tag=="ONOUN":
                           
                onounlst=[]
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if acomma.verbclass==dh[0]:
                            onounlst.append(dh[1])

        acomma.onoun=random.choice(onounlst)
        if acomma.verbclass=="personified":
            acomma.onoun="person"
        #print("acomma.onoun",acomma.onoun)
        return(acomma.onoun)
    def genvbz(self):
        for i in acomma.root:
            if i.tag=="ONOUN":
                #print("onounssss",acomma.onoun)
              
                if acomma.onoun.endswith("s"):
                    vbz="are"
                    return(vbz)
                else:
                    vbz="is"
                    return(vbz)            
        
    def gensent(self):
        det=p1.gendet()
        sname=p1.gensnoun()
        verb=p1.genverb()
        onoun=p1.genonoun()
        res=""
        res=p1.genadj()
        vbz=p1.genvbz()
        comma=","
        period="."        
        correctans=det+" "+acomma.onoun+comma+" "+sname+" "+verb+" "+vbz+" "+res+period
        #print("sname",sname)
        
            
       
        #--------------------unpunctuate-----------------------------------------------------------------
        punctuations = '''!()[]{};:'"\,<>/?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        nopunct1=nopunct.replace(".","")
        #print(nopunct)
        mylist=nopunct1.split(" ")
        
        taglst=[]
        conj="and"
        print("mylst",mylist)
        
        #mylist=['The', 'ankle', 'Mary', 'hurt', 'is', 'fractured', 'sprained', 'twisted', 'and', 'limpy.']
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            print(previous_element, current_element, next_element)
            if current_element in det and next_element==onoun:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element==onoun and next_element==sname:
                    taglst.append(current_element)
                    taglst.append("<m>")
                    
            if current_element==sname  and next_element==verb:
                taglst.append(current_element)
                taglst.append("<w>")
            if current_element ==verb and next_element==vbz:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element ==vbz and next_element in acomma.adlst:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element in acomma.adlst and next_element in acomma.adlst:
                    taglst.append(current_element)
                    taglst.append("<m>")
            if current_element in acomma.adlst and next_element ==conj:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element ==conj and next_element in acomma.adlst:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element in acomma.adlst and next_element ==None:
                    taglst.append(current_element)
                    taglst.append("<m>")
                    
            taggedsent="".join(taglst)
            category="comma"
            level="9"
            
           
        return(correctans,nopunct,taggedsent,category,level)          
for i in range(1,3):
        p1=acomma()
        correctans,nopunct,taggedsent,category,level=p1.gensent()
        print("correctans",taggedsent)
        category="comma"
        level=9
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
        mydb.commit()

##p1=acomma()
##p1.gensent()
