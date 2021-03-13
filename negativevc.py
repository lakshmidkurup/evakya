import xml.etree.ElementTree as ET
import random
import re
import string
import regex
class negativec:
    sent=""
    snname=""
    adj1=""
    noundict=[]
    vbz=""
    helpingverbs=["could","will","would","might","can","may"]
    oadj1=""
    onoun=""
    oarticle=""
    coadv=""
    verb=""
    prep="to"
    converb=""
    subjpronoun=""
    opronoun=""
    onounlist=[]
    eml=[]
    verbtype=""   
    tree = ET.parse('D:\\evakya\\xml\\simplenegativeclass.xml')
    root=tree.getroot()
    def generatesubject(self):
        
        root = negativec.tree.getroot()
        
        for i in root[0][0]:
            #print(i.tag)
            if i.tag=="SNOUN":
                
                if i.attrib['TYPE']=="personified":
                

                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                negativec.noundict.append(dh[1])

                                #print(type5.noundict)
                        negativec.snname=random.choice(negativec.noundict)
                        
                    return(negativec.snname)
                
    def generatesubjectpronoun(self):
        root = negativec.tree.getroot()
        
        for i in root[0][0]:
            #print(i.tag)
            if i.tag=="SNOUN":
                
                if i.attrib['TYPE']=="personified":
                

                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                if negativec.snname==dh[1]:
                                    negativec.opronoun=dh[3]
                                    negativec.subjpronoun=dh[2]
                    return(negativec.subjpronoun,negativec.opronoun) 
    def gensubarticle(self):
        
        root = negativec.tree.getroot()
        for i in root[0][0]:  # SARTICLE
            #print(i.tag,i.attrib)
            if i.tag=="SARTICLE":
                #print("hi")
    #-----------------------------ARTICLE--------------------------------------------------------------------------------------------------------
                
                pattern = '^[aeiou]'
                test_string = negativec.adj1
                #print("test",test_string)
                result = re.match(pattern, test_string)

                if result:
                  #print("Search successful.")
                  article="an"
                else:
                  #print("Search unsuccessful.")
                  article="a"

                return(article)
            

    def generateadjectivephrase(self):
        #tree = ET.parse('D:\\phd\\renewed\\negativecintwon.xml')
        #tree = ET.parse('D:\\phd\\renewed\\negativec1cook.xml')
        #tree = ET.parse('D:\\phd\\renewed\\negativecmorever.xml')
        root = negativec.tree.getroot()
        for i in root[0][0][3]:  # OADJECTIVEPHRASE
            #print(i.tag,i.attrib)
            if i.tag=="SCNOUN":
                cnounlist=[]
                with open("D:\\evakya\\dataset\\cnoun.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if negativec.snname==dh[1]:
                            cnounlist=dh[2:5]
                                        
                            #print("snname",cnounlist)
                            cnoun=random.choice(cnounlist)
                            #print("cnoun",cnoun)   
                

        for i in root[0][0][3]:      
            if i.tag=="SADJECTIVE":
                if i.attrib['TYPE']=="personified":
                    adjectivelst=[]
                    with open("D:\\evakya\\dataset\\adjectives.txt") as nd:
                        for word in nd:                        
                            dh=word.split(':')
                            if i.attrib['TYPE']== dh[0]:
                                adjectivelst.append(dh[1])
                    #print("adjectivelst",adjectivelst)
                    
                    negativec.adj1=random.choice(adjectivelst)

            adjphrase=negativec.adj1+" "+cnoun        
            return(adjphrase,negativec.adj1,cnoun)
        
    def genverbphrase(self):
        verblst2=[]
        
        for i in negativec.root[0][1]: # VERBPHRASE
            negativec.verbtype=i.attrib["VERBTYPE"]
            #print(i.tag,i.attrib)
            if i.tag=="VERB":
                if i.attrib['VERBTYPE']=="negative" :
                    #print("hi")
                    with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                        for word in nd:                        
                            dh=word.split(':')
                            if i.attrib['VERBTYPE']==dh[2]:
                                verblst2.append(dh[1])
                            
                        #print(verblst2)            
            vbz=i.attrib['VERBBE']
            negativec.verb=str(random.choice(verblst2))
            
            
            vp=vbz+" "+negativec.verb
        return(vp,vbz,negativec.verb)

    def getobjnounphrase(self):
        onounlist=[]
        with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
            for word in nd:                        
                dh=word.split(':')
                if negativec.verb==dh[1]:
                    verbclass=dh[0]
                    #print(verbclass)
        for i in negativec.root[0][2]:  # ONOUN
            if i.tag=="ONOUN":
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if verbclass==dh[0]:
                            onounlist.append(dh[1]) 
                onoun=random.choice(onounlist)
                #print(type9.onoun)                       
                    
        return(onoun)    
        
    def gensent(self):
        
        p1=negativec()
        snname=p1.generatesubject()
        subjpronoun,negativec.opronoun=p1.generatesubjectpronoun()
        
        title=["Dr.","Prof."]
        snname1=random.choice(title)+snname
        adjphrase,negativec.adj1,cnoun=p1.generateadjectivephrase()
        article=p1.gensubarticle()
        vp,vbz,negativec.verb=p1.genverbphrase()
        onoun=p1.getobjnounphrase()
        ophrase=negativec.opronoun+" "+onoun

      
        correctans='"'+subjpronoun.capitalize()+" "+vp+" "+ophrase+', "'
        clause1=correctans
        punctuations = '''!.()[]{};:,'\<>/?@#$%^&*_~'''
        nopunct=""
        for char in clause1:
            if char not in punctuations:
                nopunct = nopunct + char
        PUNCT_RE = regex.compile(r'\s|(\p{Punctuation})')
        ##PUNCT_RE=regex.compile(r'/([a-zA-Z]\.)+/g')
        s=PUNCT_RE.split(nopunct)
        mylist = list(filter(None, s))   
        mylist.insert(-1," ")
##        print("nopunct",nopunct)
            
             
        taglst=[]
##        print("mylst",mylist)
        title1=['Dr','Prof']
        #"He has achieved the position",Mary said to John.
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            ###print(previous_element, current_element, next_element)
            if current_element =='"' and next_element==subjpronoun.capitalize():
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element==subjpronoun.capitalize() and next_element==vbz:
                    taglst.append(current_element)
                    taglst.append("<w>")        
            if current_element==vbz and next_element==negativec.verb:
                    taglst.append(current_element)
                    taglst.append("<w>")
                    taggedsent="".join(taglst)

            if current_element==negativec.verb and next_element==negativec.opronoun:
                    taglst.append(current_element)
                    taglst.append("<w>")
                    taggedsent="".join(taglst)
            
            if current_element==negativec.opronoun and next_element==onoun:
                    taglst.append(current_element)
                    taglst.append("<w>")
                    taggedsent="".join(taglst)
            if current_element==onoun and next_element==" ":
                    taglst.append(current_element)
                    taglst.append("<m>")     #--------------------comma-----------------------------------------
                    taggedsent="".join(taglst)
           
##            if current_element==" " and next_element=='"':
##                    taglst.append(current_element)
##                    taglst.append("<w>")     #--------------------comma-----------------------------------------
##                    taggedsent="".join(taglst)        
            if current_element=='"' and next_element==None:
                    taglst.append(current_element)
                    taglst.append("<w>")     #--------------------comma-----------------------------------------
                    taggedsent="".join(taglst) 

                    
            category="comma"
            level="7"
        print(taggedsent)    
##        print(correctans)      
        return(correctans,taggedsent,nopunct)  
        
p1=negativec()

p1.gensent()
