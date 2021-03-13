import xml.etree.ElementTree as ET
import random
import re
class type6:
    
    snname=""
    adj1=""
    noundict=[]
    hverb=""
    helpingverbs=["could","will","would","might","can","may"]
    oadj1=""
    onoun=""
    oarticle=""
    coadv=""
    verb=""
    treelst=[]
##    tree1 = 'D:\\evakya\\dataset\\type6hdraw.xml'
##    tree2 = 'D:\\evakya\\dataset\\type6morever.xml'
##        
##    treelst.append(tree1)
##    treelst.append(tree2)
    treec='D:\\evakya\\xml\\type6hdraw.xml'
    tree=ET.parse(treec)
    root=tree.getroot()
    
    def generatesubject(self):
        
        
        for i in type6.root[0][0]:
            ##print(i.tag)
            if i.tag=="SNOUN":
                
                if i.attrib['TYPE']=="personified":
                

                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                type6.noundict.append(dh[1])

                                ##print(type5.noundict)
                        type6.snname=random.choice(type6.noundict)
                        
                    return(type6.snname)


    def gensubarticle(self):
        #tree = ET.parse('D:\\evakya\\dataset\\type6.xml')
        
        for i in type6.root[0][0]:  # SARTICLE
            ##print(i.tag,i.attrib)
            if i.tag=="SARTICLE":
                ##print("hi")
#-----------------------------ARTICLE--------------------------------------------------------------------------------------------------------
                
                pattern = '^[aeiou]'
                test_string = type6.adj1
                ##print("test",test_string)
                result = re.match(pattern, test_string)

                if result:
                  ##print("Search successful.")
                  article="an"
                else:
                  ##print("Search unsuccessful.")
                  article="a"

                return(article)
            
    
    def generateadjectivephrase(self):
        
        for i in type6.root[0][0][2]:  # OADJECTIVEPHRASE
            ##print(i.tag,i.attrib)
            if i.tag=="SCNOUN":
                cnounlist=[]
                with open("D:\\evakya\\dataset\\cnoun.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        ##print(dh)
                        if type6.snname==dh[1]:
                            cnounlist=dh[2:5]
                                        
                            ##print("snname",cnounlist)
                            cnoun=random.choice(cnounlist)
                            ##print("cnoun",cnoun)   
                

        for i in type6.root[0][0][2]:      
            if i.tag=="SADJECTIVE":
                if i.attrib['TYPE']=="personified":
                    adjectivelst=[]
                    with open("D:\\evakya\\dataset\\adjectives.txt") as nd:
                        for word in nd:                        
                            dh=word.split(':')
                            if i.attrib['TYPE']== dh[0]:
                                adjectivelst.append(dh[1])
                    ##print("adjectivelst",adjectivelst)
                    
                    type6.adj1=random.choice(adjectivelst)

            #adjphrase=type6.adj1+" "+cnoun        
            return(type6.adj1,cnoun)
        
    def genverbphrase(self):
        
        for i in type6.root[0][1]: # VERBPHRASE
            if i.tag=="HELPINGVERB":
                i.attrib['NAME']=random.choice(type6.helpingverbs)
                type6.hverb=i.attrib['NAME']
        
            if i.tag=="VERB":
                type6.verb=i.attrib['VNAME']
                ##print(verb)        
        #vp=type6.hverb+" "+type6.verb
        return(type6.hverb,type6.verb)
    
    def getobadjphrase1(self):
       
               
        for i in type6.root[0][2]:  # OARTICLE
            ##print(i.tag,i.attrib)
            if i.tag=="OARTICLE":
                ##print("hi")
    #-----------------------------OARTICLE--------------------------------------------------------------------------------------------------------
                pattern = '^[aeiou]'
                test_string = type6.oadj1
                ##print("test",test_string)
                result = re.match(pattern, test_string)

                if result:
                  ##print("Search successful.")
                  type6.oarticle="an"
                 # #print(oarticle)
                else:
                  ##print("Search unsuccessful.")
                  type6.oarticle="a"
                  ##print(oarticle)
        
            if i.tag=="ONOUN":
                onounlist=[]
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        ##print(dh)
                        if i.attrib['CLASS']==dh[0]:
                            onounlist.append(dh[1])
                type6.onoun=random.choice(onounlist)            
                                        
                                     
                ##print("0noun",onoun)  
        for i in type6.root[0][2][2]:  # OADJECTIVE
            ##print(i.tag,i.attrib)
            if i.tag=="OADJECTIVE":
                oadjectivelst=[]
                with open("D:\\evakya\\dataset\\adjectives.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                       
                        if i.attrib['CLASS']== dh[0]:
                            oadjectivelst.append(dh[1])
               
                
                type6.oadj1=random.choice(oadjectivelst)
                ##print(type5.oadj1)                
                oadjphrase=type6.oarticle+" "+type6.oadj1+" "+type6.onoun        
            #return(oadjphrase)
            return(type6.oarticle,type6.oadj1,type6.onoun)
        

    def gencoverb(self):
        
        for i in type6.root[2]:  # Corelated verb
            ##print(i.tag,i.attrib)
            if i.tag=="COVERB":
                cverb=i.attrib['VNAME']
                return(cverb)
            
    def genpronoun(self):
       
        for i in type6.root[2]:
            ##print(i.tag,i.attrib)
            if i.tag=="PRONOUN":
                proclass=i.attrib['CLASS']
                if proclass=="openable" or proclass=="drawable" or proclass=="drinkable":
                    pro="it"


                return(pro)            

    def genperspronoun(self):
       
        for i in type6.root[2]:
            ##print(i.tag,i.attrib)
            if i.tag=="PERSPRONOUN":
                if  i.attrib['TYPE']=="personified":
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            ##print(dh[0])
                            if type6.snname in dh[1]:
                                perspro=dh[2]
                                #print(perspro)
                                return(perspro)



    def genconjadv(self):
        
       
        for i in type6.root:  # COORDCONJ
            ##print(i.tag,i.attrib)
            if i.tag=="COADV":
                type6.coadv=i.attrib['NAME']
                ##print(cordconj)
                return(type6.coadv)

            
    def genneghelpingverb(self):
       
        for i in type6.root[2]:  
            
            if i.tag=="NEGHELPINGVERB":
                type6.hverb=random.choice(type6.helpingverbs)
                neg="not"
            
                
                return(type6.hverb,neg)

    def type6sentence(self):

    
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
        oarticle1,adj1,onoun1=p1.getobadjphrase1()        
        pro=p1.genpronoun()
        cverb=p1.gencoverb()
        perspro=p1.genperspronoun()
       
        hverb,neg=p1.genneghelpingverb()
        cadvlst=["however","morever"]
        cadv=p1.genconjadv()
        cadv=random.choice(cadvlst)
        s=" "
        comma=","
        period="."
        semicolon=";"
        type1=snname1
        
        type2=article,adj,cnoun,hverb,verb,oarticle1,adj1,onoun1
        text1=type1
        text2=s.join(type2)
        #text3=s.join(type3)
        option=1
        #print(option)
        #option = int(input("Enter your option for semicolon rules : "))

        if option == 1:
            if cadv=="however": # Rule 1: When you use a conjunctive adverb, put a semicolon (;) before it and a comma (,) after it
                
                
                ##print(type1+comma+text2+comma+text3+questionmark)
                type3=perspro,hverb,neg,cverb,pro
                subclause=comma+" "+s.join(type3)+period
                sentence=type1+comma+" "+text2+semicolon+" "+cadv+subclause
                #print(sentence)
               
            elif cadv=="morever":
                type3m=perspro,type6.hverb,cverb,pro
                subclause=comma+" "+s.join(type3m)+period
                sentence=type1+comma+" "+text2+semicolon+" "+cadv+subclause
                #print(sentence)
               



        correctans=sentence
        #--------------------unpunctuate--------------------------------------------------------------------------------------------------------------------
        punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''
        nopunct=""
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        #print(nopunct)        
        #--------------------------------tag unpunctuated text------------------------------------------------------------------------------------------------
        #Mrs. Mary,an adorable lady can open a heavy book.However,she can not lift it.
        #Bro. James,an adorable man would open a small cage;however,he would not lift it.
        title=['Mr','Capt','Major','Bro','Mrs','Miss','Sr']   
        mylist=nopunct.split(" ")
        
        
        taglst=[]
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
            if current_element == verb and next_element==oarticle1:
                taglst.append(current_element)
                taglst.append("<w>")
               
            if (current_element ==oarticle1) and (next_element ==adj1):
                taglst.append(current_element)
                taglst.append("<w>")
            if (current_element ==adj1) and (next_element ==onoun1):
                taglst.append(current_element)
                taglst.append("<w>")    
            if (current_element ==onoun1) and (next_element == cadv):
                taglst.append(current_element)
                taglst.append("<m>")    
            if (current_element ==cadv) and (next_element == perspro):
                taglst.append(current_element)
                taglst.append("<m>")
        
            if (current_element ==perspro) and (next_element == hverb):
                taglst.append(current_element)
                taglst.append("<w>")
            if current_element ==hverb and (next_element==neg):
                taglst.append(current_element)
                taglst.append("<w>")
            if current_element ==hverb and (next_element==cverb):
                taglst.append(current_element)
                taglst.append("<w>")    
            if current_element ==neg and (next_element==cverb):
                taglst.append(current_element)
                taglst.append("<w>")
            if current_element ==cverb and (next_element==pro):
                taglst.append(current_element)
                taglst.append("<w>")    
            if next_element==None:
                taglst.append(current_element)
                taglst.append("<m>")    
        taggedsent="".join(taglst)
        category="comma"
        level="3"
        ###print(taggedsent)
       
        #print("correctans",correctans,nopunct,taggedsent,category,level)
        return(correctans,nopunct,taggedsent,category,level)
                
            
for i in range(1,6):
        p1=type6()
        correctans,nopunct,taggedsent,category,level=p1.type6sentence()
        print(correctans)
        print(taggedsent)
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

