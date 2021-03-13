import xml.etree.ElementTree as ET
import random
import re

class type9excl:
    tag=""
    vclass=""
    verbclass=""
    onoun=""
    verb=""
    adverb=""
    snname=""
    noundict=[]
    eml=[]
    em=""
    tree1 = ET.parse('D:\\evakya\\xml\\type9whexcl.xml')
    tree2=ET.parse('D:\\evakya\\xml\\type9howexcl.xml')
    adj=""
    tagname=""
    pro=""

    def tagname1(self):
        root = type9excl.tree1.getroot()
        for i in root:
            if i.tag=="TAG":
                type9excl.tag=i.attrib["NAME"]
                ##print(type9excl.tag)
                return(type9excl.tag)
    
    def gennoun(self):
        root = type9excl.tree1.getroot()
        verbclasslst=[]
        for i in root:
            if i.tag=="NOUN":
                type9excl.vclass=i.attrib["VCLASS"]
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if i.attrib['VCLASS'] == dh[2]:
                            verbclasslst.append(dh[0])
                type9excl.verbclass=random.choice(verbclasslst)
##                #print(type9excl.verbclass)
                            
                            
        for i in root:
            with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        onounlist=[]
                        for word in nd:
                            dh=word.split(':')
                            ##print(dh)
                            if type9excl.verbclass==dh[0]:
                               
                                onounlist.append(dh[1])
##                                onounlist=onounlist.remove("Mary")
##                                onounlist=onounlist.remove("Alice")
##                                onounlist=onounlist.remove("James")
##                                onounlist=onounlist.remove("John")
                                
                        #print(onounlist)        
                        type9excl.onoun=random.choice(onounlist)
                        if type9excl.onoun in ["Mary","Alice"]:
                            type9excl.onoun="lady"
                        elif type9excl.onoun in ["John","James"]:
                            type9excl.onoun="gentleman"
                        ##print(type9excl.onoun)
        for i in root:
            with open("D:\\evakya\\dataset\\adjectives.txt") as nd:
                adjlst=[]
                for word in nd:
                    dh=word.split(':')
                    ##print(dh)
                    if type9excl.verbclass==dh[0]:
                       
                        adjlst.append(dh[1])
                        
                type9excl.adj=random.choice(adjlst)
        pattern = '^[aeiou]'
        test_string = type9excl.adj
        ##print("test",test_string)
        result = re.match(pattern, test_string)

        if result:
          ##print("Search successful.")
          article="an"
        else:
          ##print("Search unsuccessful.")
          article="a"
        if type9excl.onoun=="lady":
            type9excl.pro="she"
        elif type9excl.onoun=="gentleman":
            type9excl.pro="he"
        else:
            type9excl.pro="it"
        sentence=article+" "+type9excl.adj+" "+type9excl.onoun
        ##print(sentence)                   
        return(article,type9excl.adj,type9excl.onoun)

    def geninterjection(self):
        #tree = ET.parse('D:\\evakya\\dataset\\type71read.xml')
        #tree = ET.parse('D:\\evakya\\dataset\\type71cook.xml')
        root = type9excl.tree1.getroot()
        for i in root:
            if i.tag=="INTERJECTION":
                
                
                with open("D:\\evakya\\dataset\\interjections.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
##                                            #print(dh)
                        if i.attrib['EMOTION']==dh[1]:
                            type9excl.eml.append(dh[2])
                            
            type9excl.em=random.choice(type9excl.eml)
                
            i.attrib['NAME']=type9excl.em
            ##print("i.attrib['NAME']",i.attrib['NAME'])
            return(type9excl.em)
    

    def genverbtobe(self):
        root = type9excl.tree1.getroot()
        for i in root:
            if i.tag=="VERB":
                if type9excl.onoun:
                    i.attrib['VERBTOBE']="is"
                    verbtobe=i.attrib['VERBTOBE']
                    ##print("VERBTOBE",verbtobe)
                return(verbtobe)
        
    def genhowphrase(self):
        root2 = type9excl.tree2.getroot()
        verblst=[]
        advlst=[]
        for i in root2:
            ##print(i.tag,i.attrib)
            if i.tag=="TAG":
                type9excl.tagname=i.attrib['NAME']
                    
                        
        root2 = type9excl.tree2.getroot()
        verblst=[]
        advlst=[]
        for i in root2:
            if i.tag=="SNOUN":
                if i.attrib['TYPE']=="personified":
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                type9excl.noundict.append(dh[1])

                                ##print(type9excl.noundict)
                        type9excl.snname=random.choice(type9excl.noundict)
                        
                    
                
        for i in root2:
            if i.tag=="VERB":
                type9excl.vclass=i.attrib["VCLASS"]
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if i.attrib['VCLASS'] == dh[2]:
                            verblst.append(dh[1])
                            ##print(verblst)
                type9excl.verb=random.choice(verblst)
                #print(type9excl.verb)

        for i in root2:
            if i.tag=="VERB":
                
                with open("D:\\evakya\\dataset\\adverb.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if type9excl.verb == dh[0]:
                            advlst.append(dh[1])
                            #print(advlst)
                type9excl.adverb=random.choice(advlst)

        verbhow= type9excl.tagname+" "+type9excl.adverb+" "+type9excl.snname+" "+type9excl.verb
        ##print(verbhow)
        return(type9excl.tagname,type9excl.adverb,type9excl.snname,type9excl.verb)
##                #print(type9excl.verbclass)
    
    def type9sentence(self):
        
        p1=type9excl()

        verbhow=p1.genhowphrase()
        tagname=p1.tagname1()
        op=p1.gennoun()
        interjn=p1.geninterjection()
        verbtobe=p1.genverbtobe()
        excl="!"
        comma=","
        period="."
        sentence1=tagname+" "+op+" "+type9excl.pro+" "+verbtobe+excl
        sentence2=verbhow+excl   
        sentence3=interjn+comma+tagname+" "+op+excl
        
        sentence4=interjn+excl+tagname+" "+op+period
        #print("1.",sentence1)
        #print("2.",sentence2)
        #print("3.",sentence3)
        #print("4.",sentence4)
        return(sentence1,sentence2,sentence3,sentence4)
        
p1=type9excl()

for i in range(0,1):
    tagname=p1.tagname1()
    article,type9excl.adj,type9excl.onoun=p1.gennoun()
    interjn=p1.geninterjection()
    verbtobe=p1.genverbtobe()
    excl="!"
    comma=","
    period="."
    sentence1=tagname+" "+article+" "+type9excl.adj+" "+type9excl.onoun+" "+type9excl.pro+" "+verbtobe+excl
    taggedsent=tagname+"<w>"+article+"<w>"+type9excl.adj+"<w>"+type9excl.onoun+"<w>"+type9excl.pro+"<w>"+verbtobe+"<m>"
    print("sentence1",sentence1)    
#------------------- -unpunctuate-----------------------------------------------------------------
    punctuations = '''!()[]{};:'"\,<>.?@#$%^&*_~'''
    nopunct=""
    for char in sentence1:
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
    category="exclamation"
    level=1
    
    mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sentence1,taggedsent,category,level,1))
    mydb.commit() 
for i in range(0,1):
    type9excl.tagname,type9excl.adverb,type9excl.snname,type9excl.verb=p1.genhowphrase()
    
    excl="!"
    comma=","
    period="."
    sentence2=type9excl.tagname+" "+type9excl.adverb+" "+type9excl.snname+" "+type9excl.verb+excl
    print("sentence2",sentence2)   
    taggedsent=type9excl.tagname+"<w>"+type9excl.adverb+"<w>"+type9excl.snname+"<w>"+type9excl.verb+"<m>"
    #--------------------unpunctuate-----------------------------------------------------------------
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

    mycursor.execute("select max(exerciseid) from sentencedb")  
    rows = mycursor.fetchall()
    for row in rows:
            id1=0
            id1=row[0]
            #####print("id1:",row[0])
    id2=id1+1
    category="exclamation"
    level=1
    
    mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sentence2,taggedsent,category,level,1))
    mydb.commit() 
for i in range(0,2):
    tagname=p1.tagname1()
    article,type9excl.adj,type9excl.onoun=p1.gennoun()
    interjn=p1.geninterjection()
    verbtobe=p1.genverbtobe()
    excl="!"
    comma=","
    period="."
    category="exclamation"
    sent=interjn+comma+" "+tagname+" "+article+" "+type9excl.adj+" "+type9excl.onoun+excl
    taggedsent=interjn+"<c>"+tagname+"<w>"+article+"<w>"+type9excl.adj+"<w>"+type9excl.onoun+"<c>"
    print("sentence3",sent)   
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
    category="exclamation"
    level=1
    mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))
    mydb.commit() 
    #print(sent,taggedsent)
for i in range(0,1):
    
    tagname=p1.tagname1()
    article,type9excl.adj,type9excl.onoun=p1.gennoun()
    interjn=p1.geninterjection()
    verbtobe=p1.genverbtobe()
    excl="!"
    comma=","
    period="."
    level=1
    category="exclamation"
    sent=interjn+excl+" "+tagname+" "+article+" "+type9excl.adj+" "+type9excl.onoun+period
    print("sent4",sent)
    taggedsent=interjn+"<c>"+tagname+"<w>"+article+"<w>"+type9excl.adj+"<w>"+type9excl.onoun+"<c>"
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
    level=1
    mycursor.execute("select max(exerciseid) from sentencedb")  
    rows = mycursor.fetchall()
    for row in rows:
            id1=0
            id1=row[0]
            #####print("id1:",row[0])
    id2=id1+1
    
    mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))
    mydb.commit() 
