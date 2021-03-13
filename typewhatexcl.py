import xml.etree.ElementTree as ET
import random
import re

class type9excl2:
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
    tree11=[]
    tree=[]
    tree1 = ET.parse('D:\\evakya\\xml\\type9whexcl.xml')
    
    
    adj=""
    tagname=""
    pro=""
    
    def tagname1(self):
        root = type9excl2.tree1.getroot()
        for i in root:
            if i.tag=="TAG":
                type9excl2.tag=i.attrib["NAME"]
                ##print(type9excl2.tag)
                return(type9excl2.tag)
    
    def gennoun(self):
        root = type9excl2.tree1.getroot()
        verbclasslst=[]
        for i in root:
            if i.tag=="NOUN":
                type9excl2.vclass=i.attrib["VCLASS"]
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if i.attrib['VCLASS'] == dh[2]:
                            verbclasslst.append(dh[0])
                type9excl2.verbclass=random.choice(verbclasslst)
                print(type9excl2.verbclass)
                            
                            
        for i in root:
            with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        onounlist=[]
                        for word in nd:
                            dh=word.split(':')
                            ##print(dh)
                            if type9excl2.verbclass==dh[0]:
                               
                                onounlist.append(dh[1])
##                                onounlist=onounlist.remove("Mary")
##                                onounlist=onounlist.remove("Alice")
##                                onounlist=onounlist.remove("James")
##                                onounlist=onounlist.remove("John")
                                
                        #print(onounlist)        
                        type9excl2.onoun=random.choice(onounlist)
                        if type9excl2.onoun in ["Mary","Alice"]:
                            type9excl2.onoun="lady"
                        elif type9excl2.onoun in ["John","James"]:
                            type9excl2.onoun="gentleman"
                        ##print(type9excl2.onoun)
        for i in root:
            with open("D:\\evakya\\dataset\\adjectives.txt") as nd:
                adjlst=[]
                for word in nd:
                    dh=word.split(':')
                    ##print(dh)
                    if type9excl2.verbclass==dh[0]:
                       
                        adjlst.append(dh[1])
                        
                type9excl2.adj=random.choice(adjlst)
        pattern = '^[aeiou]'
        test_string = type9excl2.adj
        ##print("test",test_string)
        result = re.match(pattern, test_string)

        if result:
          ##print("Search successful.")
          article="an"
        else:
          ##print("Search unsuccessful.")
          article="a"
        if type9excl2.onoun=="lady":
            type9excl2.pro="she"
        elif type9excl2.onoun=="gentleman":
            type9excl2.pro="he"
        else:
            type9excl2.pro="it"
        sentence=article+" "+type9excl2.adj+" "+type9excl2.onoun
        ##print(sentence)                   
        return(article,type9excl2.adj,type9excl2.onoun)

    def geninterjection(self):
        #tree = ET.parse('D:\\evakya\\dataset\\type71read.xml')
        #tree = ET.parse('D:\\evakya\\dataset\\type71cook.xml')
        root = type9excl2.tree1.getroot()
        for i in root:
            if i.tag=="INTERJECTION":
                with open("D:\\evakya\\dataset\\interjections.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')

                        if i.attrib['EMOTION']==dh[1]:
                            type9excl2.eml.append(dh[2])
                            
            type9excl2.em=random.choice(type9excl2.eml)
                
            i.attrib['NAME']=type9excl2.em

            return(type9excl2.em)
    

    def genverbtobe(self):
        root = type9excl2.tree1.getroot()
        for i in root:
            if i.tag=="VERB":
                if type9excl2.onoun:
                    i.attrib['VERBTOBE']="is"
                    verbtobe=i.attrib['VERBTOBE']
                    ##print("VERBTOBE",verbtobe)
                return(verbtobe)
        
    def genhowphrase(self):
        root2 = type9excl2.tree1.getroot()
        verblst=[]
        advlst=[]
        for i in root2:
            ##print(i.tag,i.attrib)
            if i.tag=="TAG":
                type9excl2.tagname=i.attrib['NAME']
                    
                        
      
        verblst=[]
        advlst=[]
        for i in root2:
            if i.tag=="SNOUN":
                if i.attrib['TYPE']=="personified":
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                type9excl2.noundict.append(dh[1])

                                ##print(type9excl2.noundict)
                        type9excl2.snname=random.choice(type9excl2.noundict)
                        
                    
                
        for i in root2:
            if i.tag=="VERB":
                type9excl2.vclass=i.attrib["VCLASS"]
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if i.attrib['VCLASS'] == dh[2]:
                            verblst.append(dh[1])
                            ##print(verblst)
                type9excl2.verb=random.choice(verblst)
                #print(type9excl2.verb)

        for i in root2:
            if i.tag=="VERB":
                
                with open("D:\\evakya\\dataset\\adverb.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if type9excl2.verb == dh[0]:
                            advlst.append(dh[1])
                            #print(advlst)
                type9excl2.adverb=random.choice(advlst)

        verbhow= type9excl2.tagname+" "+type9excl2.adverb+" "+type9excl2.snname+" "+type9excl2.verb
        ##print(verbhow)
        return(type9excl2.tagname,type9excl2.adverb,type9excl2.snname,type9excl2.verb)
##                #print(type9excl2.verbclass)
    
    def type9sentence(self):
        

        verbhow=p1.genhowphrase()
        tagname=p1.tagname1()
        op=p1.gennoun()
        interjn=p1.geninterjection()
        verbtobe=p1.genverbtobe()
        excl="!"
        comma=","
        period="."
        sentence1=tagname+" "+op+" "+type9excl2.pro+" "+verbtobe+excl
        sentence2=verbhow+excl   
        sentence3=interjn+comma+tagname+" "+op+excl
        
        sentence4=interjn+excl+tagname+" "+op+period
        #print("1.",sentence1)
        #print("2.",sentence2)
        #print("3.",sentence3)
        #print("4.",sentence4)
        return(sentence1,sentence2,sentence3,sentence4)
        
p1=type9excl2()


for i in range(0,2):
    type9excl2.tagname,type9excl2.adverb,type9excl2.snname,type9excl2.verb=p1.genhowphrase()
    interjn=p1.geninterjection()
    verbtobe=p1.genverbtobe()
    article,type9excl2.adj,type9excl2.onoun=p1.gennoun()
    excl="!"
    comma=","
    period="."
    sentence4=type9excl2.tagname+" "+article+" "+type9excl2.adj+" "+type9excl2.onoun+" "+type9excl2.pro+" "+verbtobe+excl
    taggedsent=type9excl2.tagname+"<w>"+article+"<w>"+type9excl2.adj+"<w>"+type9excl2.onoun+"<w>"+type9excl2.pro+"<w>"+verbtobe+"<m>"
    #--------------------unpunctuate-----------------------------------------------------------------
    punctuations = '''!()[]{};:'"\,<>.?@#$%^&*_~'''
    nopunct=""
    for char in sentence4:
        if char not in punctuations:
            nopunct = nopunct + char
    print(sentence4)
    print(nopunct)
    print(taggedsent)
    
    import mysql.connector



##for i in range(0,2):
##    tagname=p1.tagname1()
##    op=p1.gennoun()
##    interjn=p1.geninterjection()
##    verbtobe=p1.genverbtobe()
##    excl="!"
##    comma=","
##    period="."
##    sentence3=interjn+comma+tagname+" "+op+excl
##    #print(sentence3)
