import xml.etree.ElementTree as ET
import random
import re

class type15:
    sname=""
    oname=""
    noundict=[]
    eclass=""
    eclasssub2=""
    eclasssub3=""
    eclasssub4=""
    eclasssub5=""
    verb=""
    verbsub2=""
    verbsub3=""
    verbsub4=""
    verbsub5=""
    conj=""
    adv=""
    advt=""
    adv5=""
    pluralpro=""
    adj=""
    adjv=""
    spro=""
    tree = ET.parse('D:\\evakya\\xml\\type15.xml')
    root = tree.getroot()
    

    def generatesubjectobj(self):    
        onamelst=[]
        for i in type15.root[0]:  
            if i.tag=="SNOUN":     
                if i.attrib['TYPE']=="personified":   
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0] and dh[4]=="M":
                                type15.noundict.append(dh[1])
                                
                       
                            if i.attrib['TYPE'] == dh[0] and dh[4]=="F":
                                onamelst.append(dh[1])
                                
                        type15.snname=random.choice(type15.noundict)
                        type15.oname=random.choice(onamelst)      
                       
                       # print(type15.snname,type15.oname)                        
                    return(type15.snname,type15.oname)

    def genverb(self):
        verblst=[]
        for i in type15.root[0]:  
            if i.tag=="VERB":     
                type15.eclass=i.attrib['ECLASS']
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if type15.eclass == dh[2]:
                            verblst.append(dh[1])
                    type15.verb=random.choice(verblst)        

       # print(type15.verb)
        return(type15.verb)
     
    def genconj(self):
        for i in type15.root:
            #print(i.tag)
            if i.tag=="CONJ":
                #print(i.attrib)
                conj=i.attrib['NAME']
                conj=conj.split("-")
                type15.conj=random.choice([conj[0],conj[1]])
        #print(type15.conj)
        return(type15.conj)
    def clause1(self):
        advlst1=[]
        for i in type15.root[2]:
            #print(i.tag)
            if i.tag=="PRO":
                if i.attrib['TYPE']=="personified":
                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if type15.snname==dh[1]:
                                type15.spro=dh[2]
                    
            if i.tag=="VBZ":
                vbz=i.attrib['TYPE']
            if i.tag=="VERBP":
                advd=i.attrib['ADVDEGREE']
                with open("D:\\evakya\\dataset\\adjectives.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if dh[0]==i.attrib['TYPE']:
                            advlst1.append(dh[1])
                    adv1=random.choice(advlst1) 
        s=" "
        clause1=type15.spro,vbz,advd,adv1
        clause=s.join(clause1)
        return(clause)            
            
                #print(i.attrib)
    def clause3(self):
        verblst3=[]
        for i in type15.root[4]:
            #print(i.attrib)
            if i.tag=="PRO":
                if i.attrib['TYPE']=="PLURAL":
                    pro="They"
            
                
            if i.tag=="VERB":
                type15.eclasssub3=i.attrib['ECLASS']
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if type15.eclasssub3 == dh[2]:
                            verblst3.append(dh[1])
                type15.verbsub3=random.choice(verblst3)
                #print("type15.verbsub3",type15.verbsub3)    
            if i.tag=="PREP":
                
                prep="with"
            
                       
                    
            if i.tag=="RECIPROCALPRONOUN":
                typepro=i.attrib['TYPE']
                typepro=typepro.split("-")
                recpro=random.choice([typepro[0],typepro[1]])
            
               
        s=" "
        sent=pro,type15.verbsub3,prep,recpro
        clause3=s.join(sent)
        return(clause3)  
    def clause2(self):

        verblst2=[]
        for i in type15.root[3]:
            #print(i.attrib)
            if i.tag=="PRO":
                if i.attrib['TYPE']=="PLURAL":
                    pro="They"
            
                
            if i.tag=="VERB":
                type15.eclasssub2=i.attrib['ECLASS']
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if type15.eclasssub2 == dh[2]:
                            verblst2.append(dh[1])
                type15.verbsub2=random.choice(verblst2)        
            if i.tag=="PREP":
                if type15.verbsub2=="interacted":
                    prep="with"
                else:
                    prep=""
                       
                    
            if i.tag=="RECIPROCALPRONOUN":
                typepro=i.attrib['TYPE']
                typepro=typepro.split("-")
                recpro=random.choice([typepro[0],typepro[1]])
            
               
        s=" "
        sent=pro,type15.verbsub2,prep,recpro
        clause2=s.join(sent)
        return(clause2)
                    
    def clause4(self):
       #<VERB NAME="x" ADV="x" ECLASS="mconclusionclassp" 
 
        verblst4=[]
        advlst4=[]
        for i in type15.root[5][2]:
            #print(i.tag,i.attrib)
            if i.tag=="VERB":
                type15.eclasssub4=i.attrib['ECLASS']
                #print(type15.eclasssub4)
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if type15.eclasssub4 == dh[2]:
                            verblst4.append(dh[1])
                type15.verbsub4=random.choice(verblst4)
        for i in type15.root[5][2]:
            
            if i.tag=="VERB":
              
                if i.attrib['ADV']=="x":
                    #print("abc",i.attrib['ADV'])
                    with open("D:\\evakya\\dataset\\adverb.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if type15.verbsub4==dh[0]:
                                advlst4.append(dh[1])
                    type15.adv=random.choice(advlst4)
                    #print("advvvv",type15.adv)
        for i in type15.root[5]:
                  
            if i.tag=="PRO":
                if i.attrib['TYPE']=="PLURAL":
                    type15.pluralpro="they"
      
        for i in type15.root[5]:
##            print(i.tag,i.attrib)            
            if i.tag=="ADVT":
                advclass=i.attrib['TYPE']
##                print("advclass",advclass)
                with open("D:\\evakya\\dataset\\adverb.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if advclass==dh[0]:
                            type15.advt=dh[1]
                            #print("adverbt",type15.advt)
                
        
        s=" "
        clause41=type15.advt.capitalize()+" "+type15.pluralpro+" "+type15.verbsub4+" "+type15.adv
        #print("clause4 is:",clause41)
        return(clause41)
    def clause5(self):
        verblst5=[]
        adjlst5=[]
        for i in type15.root[6][2]:
            #print(i.tag,i.attrib)
            if i.tag=="VERB":
                type15.eclasssub5=i.attrib['ECLASS']
                #print("eclass5",type15.eclasssub5)
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if type15.eclasssub5 == dh[2]:
                            verblst5.append(dh[1])
                type15.verbsub5=random.choice(verblst5)
                #print(type15.verbsub5)
          
        for i in type15.root[6]:
                  
            if i.tag=="PRO":
                if i.attrib['TYPE']=="PLURAL":
                    type15.pluralpro="they"
      
        for i in type15.root[6]:
            #print("ADV",i.attrib)            
            if i.tag=="ADVT":
                advclass=i.attrib['TYPE']
                with open("D:\\evakya\\dataset\\adverb.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if advclass==dh[0]:
                            type15.adv5=dh[1]
                            #print("adverb5",type15.adv5)
                
        
        s=" "
        clause51=type15.adv5.capitalize()+" "+type15.pluralpro+" "+type15.verbsub5
       
        #print("clause5 is:",clause51)
        return(clause51)
    def type15sentence(self):
                                  
        snname,oname=p1.generatesubjectobj()
        period="."
    

        snname,oname=p1.generatesubjectobj()
        period="."
        verb=p1.genverb()
        conj=p1.genconj()
        clause1=p1.clause1()
        clause2=p1.clause2()
        
        clause3=p1.clause3()
        
        s=" "
        sent=snname,verb,oname
        mainp=s.join(sent)
        n=int(input("Enter the Level:"))
        if n==1:
            sentence=mainp+period
            print(sentence)

        elif n==2:
            semicolon=";"
            sentence=mainp+" "+conj+" "+clause1+period
            sent2=mainp+semicolon+" "+clause1+period
            print(sentence)
            print(sent2)
            
        elif n==3:
            sentence=clause2
            sentence1=re.sub(' +',' ',sentence)+period#remove double space
            print(sentence1)
        elif n==4:
            sentence=clause3+period
            print(sentence)
        elif n==5:
            verb=p1.genverb()
            conj=p1.genconj()
            clause=p1.clause1()
            clause2=p1.clause2()
            c2=re.sub(' +',' ',clause2)
            clause1=mainp+" "+conj+" "+clause1
            clause3=p1.clause3()
            s=" "
            period="."
            sent=snname,verb,oname
            mainp=s.join(sent)+period
            sentence=mainp+clause1+period+c2+period+clause3+period
            print(sentence)
        elif n==6:
            sentence=p1.clause4()+period
            print(sentence)
        elif n==7:#--------------------------------------------------negative conclusion----------------------------
            verb=p1.genverb()
            conj=p1.genconj()
            clause=p1.clause1()
            clause2=p1.clause2()
            c2=re.sub(' +',' ',clause2)
            clause1=mainp+" "+conj+" "+clause1
            clause3=p1.clause3()
         
            clause5=p1.clause5()
            s=" "
            period="."
            sent=snname,verb,oname
            mainp=s.join(sent)+period
            sentence=mainp+clause1+period+c2+period+clause3+period+clause5+period
            print(sentence)
        elif n==8:#--------------------------------------------------positive conclusion-----------------------------
            verb=p1.genverb()
            conj=p1.genconj()
            clause=p1.clause1()
            clause2=p1.clause2()
            c2=re.sub(' +',' ',clause2)
            clause1=mainp+" "+conj+" "+clause1
            clause3=p1.clause3()
            clause4=p1.clause4()
            
            s=" "
            period="."
            sent=snname,verb,oname
            mainp=s.join(sent)+period
            sentence=mainp+clause1+period+c2+period+clause3+period+clause4+period
            print(sentence)    
        return(sentence)
    
p1=type15()
p1.type15sentence()                
