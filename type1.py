import xml.dom.minidom
from xml.dom.minidom import Node
import random
import re
##from compound import comp
##from compound2 import comp
##from compound3 import comp
class type1:
    doc = xml.dom.minidom.parse("D:\\evakya\\xml\\type11.xml")

    noundict=[]
    snname1=""
    adjective1=""
    article=""
    cnoun=""
    adverb=""
    verbt=""
    objnoun1=""
    vt=""
    oclass=""
    sennum=3
    def generatesubject(self):
        for node in type1.doc.getElementsByTagName("SENTENCE"):
            senno=node.getAttribute("NO")
            sennotype=node.getAttribute("TYPE")
            ms=node.getElementsByTagName("SUBJECTNOUNPHRASE")
            for i in ms:
                sn=i.getElementsByTagName("SNOUN")
                for i in sn:#Noun Type
                    snname=i.getAttribute("NAME")
                    snst=i.getAttribute("TYPE")
                    ######print("sennum",type1.sennum)
                    if senno==str(type1.sennum) and sennotype=="1":
                        ######print("sennum",type1.sennum)
                        if snst=="personified":
                            with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                                for word in nd:
                                    dh=word.split(':')
                                    
                                    if snst==dh[0]:
                                        type1.noundict.append(dh[1])
                                        ######print(type1.noundict)
                                        
                                snname=random.choice(type1.noundict)
                                
                        return(snname)

    def generateadjectivesforsubject(self):
        for node in type1.doc.getElementsByTagName("SENTENCE"):
            senno=node.getAttribute("NO")
            sennotype=node.getAttribute("TYPE")
            ms=node.getElementsByTagName("SUBJECTNOUNPHRASE")
            
            for i in ms:#Noun Type
                sn=i.getElementsByTagName("SNOUN")
                sadjphrase=i.getElementsByTagName("SADJECTIVEPHRASE")
                for i in sn:#Noun Type
                    snname=i.getAttribute("NAME")
                    snst=i.getAttribute("TYPE")
                    for i in sadjphrase:
                        sadj=i.getElementsByTagName("SADJECTIVE")
                        for i in sadj:
                            sadj1=i.getAttribute("NAME")
                            if sadj1=="x":
                        
                                if senno==str(type1.sennum) and sennotype=="1":
                                    if snst=="personified":
                                        adjectivelst=[]
                                        with open("D:\\evakya\\dataset\\adjectives.txt") as nd:
                                            for word in nd:
                                            
                                                dh=word.split(':')
                                                if snst == dh[0]:
                                                    ######print("abc",dh[1])
                                            
                                                    adjectivelst.append(dh[1])
                                        ######print("adjectivelst",adjectivelst)
                                        
                                    adj1=random.choice(adjectivelst)
                                    adj2l=[]
                                    adj2l.append(adj1)
                                    ######print("adj2l",adj2l)
                                    adj2=random.choice([x for x in adjectivelst if x not in adj2l])
                                    ######print("adj1",adj1)
                                    ######print("adj2",adj2)
                                    return(adj1)
                        
    def generatesubjphrase(self):
        for node in type1.doc.getElementsByTagName("SENTENCE"):
            senno=node.getAttribute("NO")
            sennotype=node.getAttribute("TYPE")
            ms=node.getElementsByTagName("SUBJECTNOUNPHRASE")
            for i in ms:#Noun Type
                sn=i.getElementsByTagName("SNOUN")
                sadjphrase=i.getElementsByTagName("SADJECTIVEPHRASE")
                sarticle=i.getElementsByTagName("SARTICLE")
                for i in sn:
                    snname=i.getAttribute("NAME")
                    snst=i.getAttribute("TYPE")
                    if senno==str(type1.sennum) and sennotype=="1":
                        #####print("senmum",type1.sennum)
                        if snst=="personified":
                            nounlist=[]
                            cnounlist=[]
                            snname1=type1.generatesubject(self)
                            adjective1=type1.generateadjectivesforsubject(self)
                            ######print("adjective1",adjective1)
                            with open("D:\\evakya\\dataset\\cnoun.txt") as nd:
                                for word in nd:
                                    dh=word.split(':')
                                    if snname1==dh[1]:
                                        cnounlist=dh[2:5]
                                        
                                        ######print(snname1,cnounlist)
                                cnoun=random.choice(cnounlist)
                                ######print("cnoun",cnoun)   
    #--------------Rules for subject article-----------------------                            
                                
                        pattern = '^[aeiou]'
                        test_string = adjective1
                        result = re.match(pattern, test_string)

                        if result:
                          ######print("Search successful.")
                          article="an"
                        else:
                          ######print("Search unsuccessful.")
                          article="a"
                        return (snname1,adjective1,article,cnoun)
                    
    
        
    def generateverbphrase(self):
        for node in type1.doc.getElementsByTagName("SENTENCE"):
            senno=node.getAttribute("NO")
            sennotype=node.getAttribute("TYPE")
            vp = node.getElementsByTagName("VERBPHRASE")
            auxverb=[]
            adverblst=[]
            moadvlst=[]
            if senno==str(type1.sennum) and sennotype=="1":
                for i in vp:
                   aux=i.getElementsByTagName("AUXVERB")
                   mainverb=i.getElementsByTagName("VERBWORDMAIN")
                   adv=i.getElementsByTagName("ADVERB")
                   modadv=i.getElementsByTagName("MODIFYINGOADVERB")
                   for i in mainverb:
                       vt=i.getAttribute("TYPE")
                       vtense=i.getAttribute("TENSE")
                       ######print("vtense",vtense)
#--------------------Rules for auxtype--------------------------------------------------------------
                       if vtense=="PRESENT":
                           verb=vt+"s"
                           #print("verb",verb)
                           
                       elif vtense=="PAST" and not type1.vt.endswith("e") :
                           verb=vt+"ed"
                       else:
                           verb=vt+"d"
                           ######print("vt",vt)
                       for i in aux:
                           auxtype=i.getAttribute("TYPE")
                           if vtense=="PRESENT":
                               aux=""
                               auxverb=aux
                           elif vtense=="PAST":
                               seq=[]
                               seq-["had","hadn't"]
                               auxverb=random.choice(seq)
                           auxv=auxverb
                   #print(verb,auxv)                                                    
                   return(verb,auxv)


    def generateobjectphrase(self):
        for node in type1.doc.getElementsByTagName("SENTENCE"):
            senno=node.getAttribute("NO")
            sennotype=node.getAttribute("TYPE")
            onoun = node.getElementsByTagName("ONOUN")
            oarticle=node.getElementsByTagName("OARTICLE")
            oadjp=node.getElementsByTagName("OBJECTNOUNPHRASE")
            
           
            if senno==str(type1.sennum) and sennotype=="1":
                for i in oadjp:
                    for i in onoun:
                        oname= i.getAttribute("NAME")
                        oclass=i.getAttribute("CLASS")
                        if oname=="x":
                            objnoun=type1.generateobject(self)
                            oartname=type1.generateobjarticle(self)
                            oadjp,oobjpn=type1.generateobjadjphrase(self)
                            

                            return(objnoun,oartname,oadjp,oobjpn)

    def generateobject(self):
        for node in type1.doc.getElementsByTagName("SENTENCE"):
            senno=node.getAttribute("NO")
            sennotype=node.getAttribute("TYPE")
            onoun = node.getElementsByTagName("ONOUN")
            objectlst=[]
            if senno==str(type1.sennum) and sennotype=="1":
                for i in onoun:
                    oname= i.getAttribute("NAME")
                    type1.oclass=i.getAttribute("CLASS")
                    if oname=="x":
                        
                        f=open("D:\\evakya\\dataset\\noundict.txt")
                        
                        for line in f:
                            dh=line.split(":") 
                           
                            if dh[0]== type1.oclass:
                                objectlst.append(dh[1])
                                ######print("objectlst",objectlst)
                        type1.objnoun1=random.choice(objectlst)
                        return(type1.objnoun1)
                        
        
    def generateobjarticle(self):
        for node in type1.doc.getElementsByTagName("SENTENCE"):
            senno=node.getAttribute("NO")
            sennotype=node.getAttribute("TYPE")
            onoun = node.getElementsByTagName("ONOUN")
            oarticle=node.getElementsByTagName("OARTICLE")
            oadjphrase=node.getElementsByTagName("OADJECTIVEPHRASE")
            if senno==str(type1.sennum) and sennotype=="1":
                for i in onoun:
                    objname=i.getAttribute("NAME")
                    objclass=i.getAttribute("CLASS")
                    for i in oarticle:
                        oartname=i.getAttribute("NAME")
                        
      # -------------------------------------------Rules for OBJARTICLE--------------------------
      #If noun is singular, look at the vowel,add "a" and "an", if indefenite article2

                        if oartname=="x":
                            if objclass==type1.oclass:
                                
                                pattern = '^[aeiou]'
                                test_string = type1.objnoun1
                                result = re.match(pattern, test_string)

                                if result:
                                  ######print("Search successful.")
                                  oartname="an"
                                else:
                                  ######print("Search unsuccessful.")
                                  oartname="a"
                            
                                return(oartname)
                    
        
    def generateobjadjphrase(self):
        for node in type1.doc.getElementsByTagName("SENTENCE"):
            senno=node.getAttribute("NO")
            sennotype=node.getAttribute("TYPE")
            onoun = node.getElementsByTagName("ONOUN")
            oarticle=node.getElementsByTagName("OARTICLE")
            oadjphrase=node.getElementsByTagName("OADJECTIVEPHRASE")
            if senno==str(type1.sennum)  and sennotype=="1":
                oadjlst=[]
                for i in oadjphrase:
                    oadjp=i.getElementsByTagName("OADJECTIVE")
                    
                    oobjp=i.getElementsByTagName("ONOUN")
                    for i in oadjp:
                        oadjpn=i.getAttribute("NAME")
                        ######print(oadjpn)
                        for i in oobjp:
                            oobjpn=i.getAttribute("NAME")
                            oobjpc=i.getAttribute("CLASS")
                            oobjpc==type1.oclass
                            oobjpn=type1.objnoun1
                            if oadjpn=="x":
                                f=open("D:\\evakya\\dataset\\adjectives.txt")
                                ######print("hi")
                                for line in f:
                                    dh=line.split(':')
          #--------------------------------------------Rule for adjectivelist based on object class--------------------------------                          
                                    oobjpc=type1.oclass
                                    if dh[0] == type1.oclass:
                                        oadjlst.append(dh[1])
                                        
                                oadjp=random.choice(oadjlst)        
                                return(oadjp,oobjpn)
        
        
    def generateadverbphrase(self):
        for node in type1.doc.getElementsByTagName("SENTENCE"):
            senno=node.getAttribute("NO")
            sennotype=node.getAttribute("TYPE")
            oadjphrase=node.getElementsByTagName("OADVERBPHRASE")
            verb,auxv=p1.generateverbphrase()
            if senno==str(type1.sennum) and sennotype=="1":
                for i in oadjphrase:
                    omadv=i.getElementsByTagName("MODIFYINGOADVERB")
                    
                    oadv=i.getElementsByTagName("OADVERB")
                    #-----------------------------Rules for ADVERB------------------------------------------------------                               
                    for i in oadv:
                       ######print("adv",adv)
                       oadvt=i.getAttribute("TYPE")
                       
                       adverblst=[]
                       if oadvt=="x":
                          f=open("D:\\evakya\\dataset\\adverb.txt")
                          for line in f:
                              dh=line.split(":") 
                              ######print("dh",dh[0])
                              if dh[0] == verb:
                                 adverblst.append(dh[1])
                                 ######print("adverblst",adverblst)
                          oadvt=random.choice(adverblst)
                         #--------------------------RUles Modifying ADVERB---------------------------------------------
                          for i in omadv:
                            moadvt=i.getAttribute("TYPE")
                            moadvlst=[]
                            if moadvt=="x":
                                f=open("D:\\evakya\\dataset\\adverb.txt")
                                for line in f:
                                    dh=line.split(":") 
                                    
                                    if dh[0]== oadvt:
                                      moadvlst.append(dh[1])
                                      ######print("moadvlst",moadvlst)
                                      moadvt=random.choice(moadvlst)

                                return(verb,auxv,oadvt,moadvt)
                
                
    def coordnateconj(self):
        for node in type1.doc.getElementsByTagName("SENTENCE"):
            senno=node.getAttribute("NO")
            sennotype=node.getAttribute("TYPE")
            conj=i.getElementsByTagName("COORDCONJ")
            #####print(conj)
                
            if senno==str(type1.sennum) and sennotype=="2":
                
                for i in conj:
                    conjname=i.getAttribute("NAME")
                    return(conjname)
                    
        
    def type1sentence(self):
        
                            
        snname1,adjective1,article,cnoun=p1.generatesubjphrase()
        title=["Dr.","Prof."]
        snname5=random.choice(title)+" "+snname1
        ######print(snname5)
        
        objnoun,oartname,oadjp,oobjpn=p1.generateobjectphrase()
        verb,auxv,oadvt,moadvt=p1.generateadverbphrase()
        s=" "
        type1=snname1,article,adjective1,cnoun,verb,oartname,oadjp,objnoun
        type11=snname1,article,adjective1,cnoun,auxv,verb,oartname,oadjp,objnoun
        type111=snname1,article,adjective1,cnoun,auxv,verb,oartname,oadjp,objnoun,moadvt,oadvt
        type1111=snname5+","+" "+article+" "+adjective1+" "+cnoun+","+" "+verb+" "+oartname+" "+oadjp+" "+objnoun+" "+moadvt+" "+oadvt+"."
        text1=s.join(type1)
        text2=s.join(type11)
        text3=s.join(type111)
        correctans=type1111
        #print(text1)
        #print(text2)
        #print(text3)
        #print(correctans)
       

       
        #--------------------unpunctuate-----------------------------------------------------------------
        punctuations = '''!.()[]{};:'"\,<>/?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        
        ######print(nopunct)
        mylist=nopunct.split(" ")
        
        taglst=[]
        #####print("mylst",mylist)
        title1=['Dr','Prof']
        
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            #####print(previous_element, current_element, next_element)
            if current_element in title1 and next_element==snname1:
                    taglst.append(current_element)
                    taglst.append("<m>")
            if current_element==snname1 and next_element==article:
                    taglst.append(current_element)
                    taglst.append("<m>")
                    
            if current_element==article  and next_element==adjective1:
                taglst.append(current_element)
                taglst.append("<w>")
            if current_element ==adjective1 and next_element==cnoun:
                    taglst.append(current_element)
                    taglst.append("<w>")
                    #----,verb,oartname,oadjp,objnoun,moadvt,oadvt
            if current_element ==cnoun and next_element ==verb:
                    taglst.append(current_element)
                    taglst.append("<m>")
            if current_element ==verb and next_element ==oartname:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element ==oartname and next_element ==oadjp:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element ==oadjp and next_element ==objnoun:
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element ==objnoun and next_element ==moadvt:
                    taglst.append(current_element)
                    taglst.append("<w>")        
               
            
            if current_element ==moadvt and next_element ==oadvt:
                    taglst.append(current_element)
                    taglst.append("<w>")
           
            if current_element ==oadvt and next_element ==None  :
                    taglst.append(current_element)
                    taglst.append("<m>")        
            taggedsent="".join(taglst)
            category="comma"
            level="5"
        #print(taggedsent)    
        ######print(correctans,nopunct,taggedsent,category,level)      
        return(correctans,nopunct,taggedsent,category,level)          
for i in range(1,6):
        p1=type1()
#p1.type1sentence()
        correctans,nopunct,taggedsent,category,level=p1.type1sentence()
        #print("correctans",taggedsent)
        category="comma"
        level=5
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



