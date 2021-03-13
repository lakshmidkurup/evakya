import xml.etree.ElementTree as ET
import random
import re

class type5advqtag:
    tree = ET.parse('D:\\evakya\\xml\\type5quesadv.xml')
    tree1= ET.parse('D:\\evakya\\xml\\type5ntag.xml')
    ppro=["he","she","you","they"]
    ppro2="they"
    verb=""
    perspro=""
    verb1=""
    nsubtag=["Nobody","None of them","Neither-nor"]
    nsubtag1=""
    noundict=[]
    conj=""
    prep=""
    verbclass=""
    verbclass1=""
    vclass=""
    vclass1=""
    eclass=""
    eclass1=""
    onoun=""
    onoun1=""
    def genperspro(self):
        root = type5advqtag.tree.getroot()
        for i in root:
            if i.tag=="PPRO":
                type5advqtag.perspro=random.choice(type5advqtag.ppro)
                i.attrib["TYPE"]=type5advqtag.perspro
                ##print(i.attrib["TYPE"])
                return(type5advqtag.perspro)
                    
    def negadverb(self):
        root = type5advqtag.tree.getroot()
        for i in root:
            if i.tag=="NADVERB":
                advblst=[]
                advblst=i.attrib['TYPE'].split("/")
                advb=random.choice(advblst)
                ##print(advb)
                return(advb)

    def genverb(self):
        root = type5advqtag.tree.getroot()
        verblst=[]
        for i in root:
            ##print(i.tag,i.attrib)
            if i.tag=="VERB":
                type5advqtag.eclass=i.attrib['ECLASS']
                if i.attrib['ECLASS']=="neutral":
                
                    with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                        for word in nd:                        
                            dh=word.split(':')
                        ##print(dh)
                            if i.attrib['ECLASS']==dh[2]:
                                verblst.append(dh[1])
        verblst.remove("met")
        type5advqtag.verb=random.choice(verblst)
        
        with open("D:\\evakya\\dataset\\tense.txt") as nd:
            for word in nd:
                dh=word.split(':')
                if type5advqtag.verb==dh[1]:
                    type5advqtag.verb1=dh[0]
        if type5advqtag.perspro in ["he","she"]:#-----Rule to add "s" to the verb
            nverb=type5advqtag.verb1+"s"
            return(nverb)

        else:
            nverb=type5advqtag.verb1
            
        if type5advqtag.verb=="met":
            nverb1=nverb+" "+"her"

        else:
            nverb1=nverb
        ##print(type5advqtag.verb)
        return(nverb1)

    def genqtag(self):
        root = type5advqtag.tree.getroot()
        
        for i in root[4]:
            ##print(i.tag,i.attrib)
            if i.tag=="QVERB":
                if type5advqtag.perspro in ["he","she"]:
                    qverb="does"

                else:
                    qverb="do"
                ##print(qverb)

                qtag=qverb+" "+type5advqtag.perspro
                ##print(qtag)
                return(qtag)
    def negqtag2(self):
        root1= type5advqtag.tree1.getroot()
        for i in root1[3]:
            ##print(i.tag,i.attrib)
            if i.tag=="QVERB":
                qverb="do"
                ##print(qverb)
                qtag=qverb+" "+type5advqtag.ppro2
                ##print(qtag)
                return(qtag)
        
    def negtag(self):
        #<NSUBJEG TYPE="x"/>
        root1 = type5advqtag.tree1.getroot()
        for i in root1:
            if i.tag=="NSUBJEG":
                type5advqtag.nsubtag1=random.choice(type5advqtag.nsubtag)
                
                if type5advqtag.nsubtag1=="Neither-nor":
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                           
                            if dh[0]=="personified":
                                
                                type5advqtag.noundict.append(dh[1])
                                ##print(type5advqtag.noundict)
                               
                    ng1=type5advqtag.nsubtag1.split("-")
                    nsubtag2=ng1[0]+" "+type5advqtag.noundict[0]+" "+ng1[1]+" "+type5advqtag.noundict[1]
                    ##print(nsubtag2)
                    return(nsubtag2)
                else:    
                    i.attrib['TYPE']=type5advqtag.nsubtag1
                    ##print(type5advqtag.nsubtag1)
                    return(type5advqtag.nsubtag1)
    def type5nconjprep(self):
        
    #<VERB TYPE="x" CONJ="likes" PREP="to" ECLASS="neutral"  />:
        root1 = type5advqtag.tree1.getroot()
        if type5advqtag.nsubtag1=="Neither-nor":#---------if neither-nor,then "like"
            for i in root1:
            ##print(i.tag,i.attrib)
                if i.tag=="VERB":
                
                    type5advqtag.conj=i.attrib['CONJ']
                    
                    type5advqtag.prep=i.attrib['PREP']
                    return(type5advqtag.conj.replace("s",""),type5advqtag.prep)
        elif type5advqtag.nsubtag1=="None" or "Nobody":
            for i in root1:
            ##print(i.tag,i.attrib)
                if i.tag=="VERB":
                    type5advqtag.conj=i.attrib['CONJ']
                    type5advqtag.prep=i.attrib['PREP']
                    return(type5advqtag.conj,type5advqtag.prep)
    def type5nverb(self):
        verblst1=[]
        root1 = type5advqtag.tree1.getroot()
        for i in root1:
            ##print(i.tag,i.attrib)
            if i.tag=="VERB":
                
                type5advqtag.eclass1=i.attrib['ECLASS']
                if i.attrib['ECLASS']=="neutral":
                
                    with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                        for word in nd:                        
                            dh=word.split(':')
                        ##print(dh)
                            if i.attrib['ECLASS']==dh[2]:
                                verblst1.append(dh[1])
        verblst1.remove("met")
        type5advqtag.verb1=random.choice(verblst1)
       
        #print(type5advqtag.verb1)
        with open("D:\\evakya\\dataset\\tense.txt") as nd:
            for word in nd:
                dh=word.split(':')
                if type5advqtag.verb1==dh[1]:
                    type5advqtag.verb2=dh[0]
##        #print("ec1",type5advqtag.eclass1)
##        #print("v1",type5advqtag.verb2)
        return(type5advqtag.verb2)

    def type5advnoun(self):
        
        root=type5advqtag.tree.getroot()
        #root1 = type5advqtag.tree1.getroot()
        verbclasslst=[]
        for i in root:
            if i.tag=="ONOUN":
                type5advqtag.vclass=i.attrib["VCLASS"]
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if type5advqtag.verb == dh[1]:
                            verbclasslst.append(dh[0])
                type5advqtag.verbclass=random.choice(verbclasslst)
                ##print(type5advqtag.verbclass)
                            
                            
        for i in root:
            with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                onounlist=[]
                for word in nd:
                    dh=word.split(':')
                    ##print(dh)
                    if type5advqtag.verbclass==dh[0]:
                       
                        onounlist.append(dh[1])
                        
                type5advqtag.onoun=random.choice(onounlist)
                
                ##print(type5advqtag.onoun)
                return(type5advqtag.onoun)

    def type5negnoun(self):
        
        #root=type5advqtag.tree.getroot()
        root1 = type5advqtag.tree1.getroot()
        verbclasslst1=[]
        for i in root1:
            if i.tag=="ONOUN":
               
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if type5advqtag.verb1 == dh[1]:
                            verbclasslst1.append(dh[0])
                type5advqtag.verbclass1=random.choice(verbclasslst1)
##                #print(type5advqtag.eclass1)                       
##                #print(type5advqtag.verbclass1)
##                            
                            
        for i in root1:
            with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                onounlist1=[]
                for word in nd:
                    dh=word.split(':')
                    ##print(dh)
                    if type5advqtag.verbclass1==dh[0]:
                       
                        onounlist1.append(dh[1])
                        
                type5advqtag.onoun1=random.choice(onounlist1)
                
                ##print(type5advqtag.onoun1)
                return(type5advqtag.onoun1)


##    def gentype5nqtag(self):
##        
##        question="?"
##        comma=","
##        perspro=p1.genperspro()
##        nadvb=p1.negadverb()
##        verb=p1.genverb()
##        qtag=p1.genqtag()
##        negtag=p1.negtag()
##        conj,prep=p1.type5nconjprep()
##        verb1=p1.type5nverb()
##        qtag1=p1.negqtag2()
##        qtag2=qtag.split(" ")
##        print("qtag2",qtag)
##        onoun=p1.type5advnoun()
##        onoun1=p1.type5negnoun()
##        if verb1=="drinks" :
##            sent=perspro.capitalize()+" "+nadvb+" "+verb+" "+onoun+comma+" "+qtag+question
##            taggedsent=perspro.capitalize()+"<w>"+nadvb+"<w>"+verb+"<w>"+onoun+"<m>"+qtag2[0]+"<w>"+qtag2[1]+"<m>"
##        else:
##            sent=perspro.capitalize()+" "+nadvb+" "+verb+" "+"a"+" "+onoun+comma+" "+qtag+question
##        
##            taggedsent=perspro.capitalize()+"<w>"+nadvb+"<w>"+verb+"<w>"+"a"+"<w>"+onoun+"<m>"+qtag2[0]+"<w>"+qtag2[1]+"<m>"
##        level=4
##        category="questionmark"
##        #--------------------unpunctuate-----------------------------------------------------------------
##        punctuations = '''!()[]{};:."\,<>/?@#$%^&*_~'''
##        nopunct=""
##        for char in sent:
##            if char not in punctuations:
##                nopunct = nopunct + char
##
## 
##        return(sent,taggedsent,nopunct,category,level) 

for i in range(0,2):
    p1=type5advqtag()   
    question="?"
    comma=","
    perspro=p1.genperspro()
    nadvb=p1.negadverb()
    verb=p1.genverb()
    qtag=p1.genqtag()
    negtag=p1.negtag()
    conj,prep=p1.type5nconjprep()
    verb1=p1.type5nverb()
    qtag1=p1.negqtag2()
    qtag2=qtag.split(" ")
   
    onoun=p1.type5advnoun()
    onoun1=p1.type5negnoun()
    
    if verb1=="drinks" :
        sent=perspro.capitalize()+" "+nadvb+" "+verb+" "+onoun+comma+" "+qtag+question
        taggedsent=perspro.capitalize()+"<w>"+nadvb+"<w>"+verb+"<w>"+onoun+"<m>"+qtag2[0]+"<w>"+qtag2[1]+"<m>"
    else:
        sent=perspro.capitalize()+" "+nadvb+" "+verb+" "+"a"+" "+onoun+comma+" "+qtag+question
    
        taggedsent=perspro.capitalize()+"<w>"+nadvb+"<w>"+verb+"<w>"+"a"+"<w>"+onoun+"<m>"+qtag2[0]+"<w>"+qtag2[1]+"<m>"
    level=4
    category="questionmark"
    #--------------------unpunctuate-----------------------------------------------------------------
    punctuations = '''!()[]{};:."\,<>/?@#$%^&*_~'''
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
    category="questionmark"
    mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))
    mydb.commit()
    print(taggedsent)
for i in range(0,3):
    comma=","
    question="?"
    p1=type5advqtag()
    negtag=p1.negtag()
    conj,prep=p1.type5nconjprep()
    
    verb1=p1.type5nverb()
    qtag1=p1.negqtag2()
    qtag=p1.genqtag()
    onoun1=p1.type5negnoun()
    qtag2=qtag1.split(" ")
##    print("qtag2",qtag2)
    if negtag=="None of them":
        negtag1=negtag.split(" ")
        sent=negtag+" "+conj+" "+prep+" "+verb1+" "+"a"+" "+onoun1+comma+" "+qtag1+question
        taggedsent=negtag1[0]+"<w>"+negtag1[1]+"<w>"+negtag1[2]+"<w>"+conj+"<w>"+prep+"<w>"+verb1+"<w>"+"a"+"<w>"+onoun1+"<m>"+qtag2[0]+"<w>"+qtag2[1]+"<m>"
    elif negtag.startswith("Neither"):
        negtag1=negtag.split(" ")
        sent=negtag+" "+conj+" "+prep+" "+verb1+" "+"a"+" "+onoun1+comma+" "+qtag1+question
        taggedsent=negtag1[0]+"<w>"+negtag1[1]+"<w>"+negtag1[2]+"<w>"+negtag1[3]+"<w>"+conj+"<w>"+prep+"<w>"+verb1+"<w>"+"a"+"<w>"+onoun1+"<m>"+qtag2[0]+"<w>"+qtag2[1]+"<m>"
    else:    
        sent=negtag+" "+conj+" "+prep+" "+verb1+" "+"a"+" "+onoun1+comma+" "+qtag1+question
        taggedsent=negtag+"<w>"+conj+"<w>"+prep+"<w>"+verb1+"<w>"+"a"+"<w>"+onoun1+"<m>"+qtag2[0]+"<w>"+qtag2[1]+"<m>"
    level=4
    category="questionmark"
#--------------------unpunctuate-----------------------------------------------------------------
    punctuations = '''!()[]{};:."\,<>/?@#$%^&*_~'''
    nopunct=""
    for char in sent:
        if char not in punctuations:
            nopunct = nopunct + char
    import mysql.connector
    print(taggedsent)
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
    
        
