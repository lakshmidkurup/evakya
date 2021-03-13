import xml.etree.ElementTree as ET
import random
import re

class positivec:
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
    tree = ET.parse('D:\\evakya\\xml\\simplepositiveclass.xml')
    root=tree.getroot()
    def generatesubject(self):
        
        root = positivec.tree.getroot()
        
        for i in root[0][0]:
            #print(i.tag)
            if i.tag=="SNOUN":
                
                if i.attrib['TYPE']=="personified":
                

                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                positivec.noundict.append(dh[1])

                                #print(type5.noundict)
                        positivec.snname=random.choice(positivec.noundict)
                        
                    return(positivec.snname)
                
    def generatesubjectpronoun(self):
        root = positivec.tree.getroot()
        
        for i in root[0][0]:
            #print(i.tag)
            if i.tag=="SNOUN":
                
                if i.attrib['TYPE']=="personified":
                

                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                if positivec.snname==dh[1]:
                                    positivec.opronoun=dh[3]
                                    positivec.subjpronoun=dh[2]
                    return(positivec.subjpronoun,positivec.opronoun) 
    def gensubarticle(self):
        
        root = positivec.tree.getroot()
        for i in root[0][0]:  # SARTICLE
            #print(i.tag,i.attrib)
            if i.tag=="SARTICLE":
                #print("hi")
    #-----------------------------ARTICLE--------------------------------------------------------------------------------------------------------
                
                pattern = '^[aeiou]'
                test_string = positivec.adj1
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
        #tree = ET.parse('D:\\phd\\renewed\\positivecintwon.xml')
        #tree = ET.parse('D:\\phd\\renewed\\positivec1cook.xml')
        #tree = ET.parse('D:\\phd\\renewed\\positivecmorever.xml')
        root = positivec.tree.getroot()
        for i in root[0][0][3]:  # OADJECTIVEPHRASE
            #print(i.tag,i.attrib)
            if i.tag=="SCNOUN":
                cnounlist=[]
                with open("D:\\evakya\\dataset\\cnoun.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if positivec.snname==dh[1]:
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
                    
                    positivec.adj1=random.choice(adjectivelst)

            adjphrase=positivec.adj1+" "+cnoun        
            return(adjphrase,positivec.adj1,cnoun)
        
    def genverbphrase(self):
        #tree = ET.parse('D:\\phd\\renewed\\positivecintwon.xml')
        #tree = ET.parse('D:\\phd\\renewed\\positivec1cook.xml')
        verblst2=[]
        root = positivec.tree.getroot()
        
        for i in root[0][1]: # VERBPHRASE
            positivec.verbtype=i.attrib["VERBTYPE"]
            #print(i.tag,i.attrib)
            if i.tag=="VERB":
                if i.attrib['VERBTYPE']=="positive" or i.attrib['VERBTYPE']=="negative" :
                    #print("hi")
                    with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                        for word in nd:                        
                            dh=word.split(':')
                            if i.attrib['VERBTYPE']==dh[2]:
                                verblst2.append(dh[1])
                            
                        #print(verblst2)            
            positivec.vbz=i.attrib['VERBBE']
            positivec.verb=str(random.choice(verblst2))
            
            
            vp=positivec.vbz+" "+positivec.verb
        return(vp,positivec.vbz,positivec.verb)

    def getobjnounphrase(self):
        #tree = ET.parse('D:\\phd\\renewed\\positivecintwon.xml')
        #tree = ET.parse('D:\\phd\\renewed\\positivec1cook.xml')
        #tree = ET.parse('D:\\phd\\renewed\\positivecmorever.xml')
        root = positivec.tree.getroot()
        #---reteieve the class of the verb
        with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
            for word in nd:                        
                dh=word.split(':')
                if positivec.verb==dh[1]:
                    verbclass=dh[0]
                    print("class",verbclass)
        for i in root[0][2]:  # ONOUN
            if i.tag=="ONOUN":
                positivec.onounlist=[]
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                    
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if verbclass==dh[0]:
                            
                            positivec.onounlist.append(dh[1])
                            
                positivec.onoun=random.choice(positivec.onounlist)
                print("onoun",positivec.onoun)                       
            
        for i in root[0][2]:  # ONOUN
            if i.tag=="ONOUN":
                if positivec.verbtype=="negative":
    ##                    positivec.subjpronoun,positivec.opronoun=p1.generatesubjectpronoun()
                    i.attrib['DET']=positivec.opronoun
                else:
                    i.attrib['DET']="the"
                    det=i.attrib['DET']
                    
        ophrase=det+" "+positivec.onoun
        return(ophrase,det,positivec.onoun)

    def gensent(self):
        snname=p1.generatesubject()
        positivec.subjpronoun,positivec.opronoun=p1.generatesubjectpronoun()
        title=["Dr.","Prof."]
        snname1=random.choice(title)+snname
        adjphrase=p1.generateadjectivephrase()
        article=p1.gensubarticle()
        vp,positivec.vbz,positivec.verb=p1.genverbphrase()
        ophrase,det,positivec.onoun=p1.getobjnounphrase()
        
        correctans='"'+" "+positivec.subjpronoun.capitalize()+" "+vp+" "+ophrase+', "'
        punctuations = '''!.()[]{};:'\,>/?@#$%^&*_~'''
        nopunct=""
        import regex
        import string
        for char in correctans:
            if char not in punctuations:
                nopunct = nopunct + char
        
##        print("nopunct",nopunct)
        PUNCT_RE = regex.compile(r'\s|(.,?;"})')
        ##PUNCT_RE=regex.compile(r'/([a-zA-Z]\.)+/g')
        s=PUNCT_RE.split(nopunct)
        mylist = list(filter(None, s))   
        mylist.insert(-1," ")
        #print("mylist",mylist)
        taglst=[]
        #print("mylst",mylist)
        title1=['Dr','Prof']
        det="the"
        #"He has achieved the position",Mary said to John.
        for i, element in enumerate(mylist):
            previous_element = mylist[i-1] if i > 0 else None
            current_element = element
            next_element = mylist[i+1] if i < len(mylist)-1 else None
            print(previous_element, current_element, next_element)
            if current_element =='"' and next_element==positivec.subjpronoun.capitalize():
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element==positivec.subjpronoun.capitalize() and next_element==positivec.vbz:
                    taglst.append(current_element)
                    taglst.append("<w>") 
           
            if current_element==positivec.vbz and next_element==positivec.verb:
                    taglst.append(current_element)
                    taglst.append("<w>")
                    taggedsent="".join(taglst)

            if current_element==positivec.verb and next_element=="the":
                    taglst.append(current_element)
                    taglst.append("<w>")
                    taggedsent="".join(taglst)
##            print("onoun",positivec.onoun,det)
            if current_element=="the" and next_element==positivec.onoun:
                    taglst.append(current_element)
                    taglst.append("<w>")
                    taggedsent="".join(taglst)
                    
            if current_element==positivec.onoun and next_element==" ":
                    taglst.append(current_element)
                    taglst.append("<m>")     #--------------------comma-----------------------------------------
                    taggedsent="".join(taglst)
            if current_element=='"' and next_element==None:
                    taglst.append(current_element)
                    taglst.append("<w>")     #--------------------comma-----------------------------------------
                    taggedsent="".join(taglst)         
            category="comma"
            level="7"
##        print(taggedsent)    
##        print(correctans,taggedsent)      
        return(correctans,taggedsent,nopunct)  
        
p1=positivec()
p1.gensent()

