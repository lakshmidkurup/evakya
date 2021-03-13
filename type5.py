import xml.etree.ElementTree as ET
import random
import re

class type5:
    sname=""
    noundict=[]
    oadj1=""
    oadj2=""
    cordconj=""
    oarticle=""
    oarticle2=""
    oarticle3=""
    onoun=""
    hverb=""
    helpingverbs=["could","will","would","might","can","may"]
    prodict=[]

    def generatesubject(self):    
        
        tree = ET.parse('D:\\evakya\\xml\\type5.xml')
        root = tree.getroot()
        
        for i in root[0]:
            
            if i.tag=="SNOUN":
                
                if i.attrib['TYPE']=="personified":
                
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                type5.noundict.append(dh[1])

                                #print(type5.noundict)
                        type5.snname=random.choice(type5.noundict)
                        
                    return(type5.snname)
            
    def generateadjectivephrase(self):
        tree = ET.parse('D:\\evakya\\xml\\type5.xml')
        root = tree.getroot()
        for i in root[0][2]:  # OADJECTIVEPHRASE
            #print(i.tag,i.attrib)
            if i.tag=="SCNOUN":
                cnounlist=[]
                with open("D:\\evakya\\dataset\\cnoun.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if type5.snname==dh[1]:
                            cnounlist=dh[2:5]
                                        
                                        #print(snname1,cnounlist)
                            cnoun=random.choice(cnounlist)
                            #print("cnoun",cnoun)   
                

        for i in root[0][2]:      
            if i.tag=="SADJECTIVE":
                if i.attrib['TYPE']=="personified":
                    adjectivelst=[]
                    with open("D:\\evakya\\dataset\\adjectives.txt") as nd:
                        for word in nd:                        
                            dh=word.split(':')
                            if i.attrib['TYPE']== dh[0]:
                                adjectivelst.append(dh[1])
                    #print("adjectivelst",adjectivelst)
                    
                    type5.adj1=random.choice(adjectivelst)

            adjphrase=type5.adj1+" "+cnoun        
            return(type5.adj1,cnoun)

    def gensubarticle(self):
        tree = ET.parse('D:\\evakya\\xml\\type5.xml')
        root = tree.getroot()
        for i in root[0]:  # SARTICLE
            #print(i.tag,i.attrib)
            if i.tag=="SARTICLE":
                #print("hi")
#-----------------------------ARTICLE--------------------------------------------------------------------------------------------------------
                
                pattern = '^[aeiou]'
                test_string = type5.adj1
                #print("test",test_string)
                result = re.match(pattern, test_string)

                if result:
                  #print("Search successful.")
                  article="an"
                else:
                  #print("Search unsuccessful.")
                  article="a"

                return(article)

    def genverbphrase(self):
        tree=tree = ET.parse('D:\\evakya\\xml\\type5.xml')
        root = tree.getroot()
        #type5.helpingverbs=["could","will","would","might","can","may"]
        for i in root[1]: # VERBPHRASE
            if i.tag=="HELPINGVERB":
                 i.attrib['NAME']=random.choice(type5.helpingverbs)
                 type5.hverb=i.attrib['NAME']
        for i in root[1]: # VERBPHRASE
            if i.tag=="VERB":
                 type5.verb=i.attrib['VNAME']
                 #print(verb)        
        vp=type5.hverb+" "+type5.verb
        return(type5.hverb,type5.verb)
    
    def getobadjphrase1(self):
        tree = ET.parse('D:\\evakya\\xml\\type5.xml')
        root = tree.getroot()
               
        for i in root[2]:  # OARTICLE
            #print(i.tag,i.attrib)
            if i.tag=="OARTICLE":
                #print("hi")
    #-----------------------------OARTICLE--------------------------------------------------------------------------------------------------------
                pattern = '^[aeiou]'
                test_string = type5.oadj1
                #print("test",test_string)
                result = re.match(pattern, test_string)

                if result:
                  #print("Search successful.")
                  type5.oarticle="an"
                 # print(oarticle)
                else:
                  #print("Search unsuccessful.")
                  type5.oarticle="a"
                  #print(oarticle)
        
            if i.tag=="ONOUN":
                onounlist=[]
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if i.attrib['CLASS']==dh[0]:
                            onounlist.append(dh[1])
                type5.onoun=random.choice(onounlist)            
                                        
                                     
                #print("0noun",onoun)  
        for i in root[2][2]:  # OADJECTIVE
            #print(i.tag,i.attrib)
            if i.tag=="OADJECTIVE":


                 
                oadjectivelst=[]
                with open("D:\\evakya\\dataset\\adjectives.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        #print(i.attrib['CLASS'])
                        if i.attrib['CLASS']== dh[0]:
                            oadjectivelst.append(dh[1])
                #print("oadjectivelst",oadjectivelst)
                
                type5.oadj1=random.choice(oadjectivelst)
                #print(type5.oadj1)
                
                    
                oadjphrase=type5.oarticle+" "+type5.oadj1+" "+type5.onoun        
            #return(oadjphrase)


            return(type5.oarticle,type5.oadj1,type5.onoun)
        
    

    def questtag(self):
        tree = ET.parse('D:\\evakya\\xml\\type5.xml')
        root = tree.getroot()
        for i in root[3]: # VERBPHRASE
            if i.tag=="NHELPVERB":
                if i.attrib['TYPE']=="HVERB":
                    qtagl = [('would',"wouldn't"),('will',"won't"),('could', "couldn't"), ('may', "won't"), ('can', "can't"),('might',"won't")]
                    qtag_dict={}
                    a=type5.hverb
                    ra_list=['would','can','could','will','can','might','may']
                    for key,val in qtagl:
                       qtag_dict.setdefault(key,[]).append(val)
                       #print(qtag_dict)
                        #hverblst=['can','could','may']
                    if a in ra_list: 
                       a=qtag_dict.get(a,[0])
                       a=str(a).strip('[""]')
                       return(a)
            
    def getpronoun(self):
        tree = ET.parse('D:\\evakya\\xml\\type5.xml')
        root = tree.getroot()
        pro=""
        for i in root[3]: # VERBPHRASE
            if i.tag=="PRONOUN":
                if i.attrib['TYPE']=="personified":
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            #print(dh[0])
                            if type5.snname in dh[1]:
                                pro=dh[2]
                                #print("ppppp",pro)
                                #print(type5.noundict)
        #pro=random.choice(type5.prodict)
                        
                                return(pro)
                                      
        
    def type5sentence(self):
      
        snname=p1.generatesubject()
        title=['Dr','Prof']
        snname1=random.choice(title)
        adj1,cnoun=p1.generateadjectivephrase()
        article=p1.gensubarticle()
        hverb,verb=p1.genverbphrase()
        oarticle,oadj,onoun=p1.getobadjphrase1()
        qt=p1.questtag()
        pro=p1.getpronoun()
   
        s=" "
        comma=","
        period="."
        questionmark="?"
        type1=snname1
        type2=article,adj1,cnoun,hverb,verb,comma,oarticle,oadj,onoun
        typeq=qt,pro
        #typef1=oadjphrase2,type5.cordconj,oadjphrase3
        text1=type1
        #text2=s.join(type2)
        text3=s.join(typeq)
        text2=article+" "+adj1+" "+cnoun+comma+" "+hverb+" "+verb+" "+oarticle+" "+oadj+" "+onoun
        sent=snname1+"."+" "+snname+comma+" "+text2+comma+" "+text3+"?"
        taggedsent=snname1+"<m>"+snname+"<m>"+article+"<w>"+type5.adj1+"<w>"+cnoun+"<m>"+hverb+"<w>"+verb+"<w>"+oarticle+"<w>"+oadj+"<w>"+onoun+"<m>"+qt+"<w>"+pro+"<m>"
        print(sent)
        print(taggedsent)
        return(sent,taggedsent)
                   
p1=type5()
for i in range(0,5):
    sent,taggedsent=p1.type5sentence()
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
                    
    nopunct=""
    punctuations = '?.,'
    mylist=[]
    for char in sent:
        if char not in punctuations:
            nopunct = nopunct + char
         
    category="questionmark"
    level=3
    #print(sent,taggedsent,nopunct,category,level) 
    #-----------------------------insert into database------------------------------------------------------------------------------------------------------------------   

    mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))
    mydb.commit() 
            
    

##snname=p1.generatesubject()
##adjphrase=p1.generateadjectivephrase()
##article=p1.gensubarticle()
##vp=p1.genverbphrase()
##oadjphrase1,oarticle1=p1.getobadjphrase1()
####oadjphrase2,oarticle2=p1.getobadjphrase2()
####cordconj=p1.gencordconj()
##print("snname",snname)
##print("adj",adjphrase)
##print("article",article)
##print("vphrase",vp)

##print("oadjphrase",oadjphrase2)
##print("oarticle",oarticle2)
##print("oadjphrase",oadjphrase1)
##print("oarticle",oarticle1)
##print("cordconj",cordconj)
##
##
##
