import re
##import datetime
##import mysql.connector
##from dateutil.parser import parse
##mydb = mysql.connector.connect(
##                host="localhost",
##                user="root",
##                passwd="rohith@123",
##                database="pythonlogin"
##        )
##mycursor = mydb.cursor()
class qmrules:
    snoun=['Mary','James','John','Alice','A. Roy', 'K. Singh', 'R. K. Narayan', 'R. Kushner','Esmail','Bagani' ]
    verb=['went','said','yelled','exclaimed','shouted','knew','lift','stand','answered','won','got','secured','achieved','hurt','lost','opened','closed','cooked','met','read','wrote','drew','drank','paid','bought','stayed','worked','joined','taught','married','dated','intracted','consulted','visited','debated','argued','fought','lived','seperated']
    verb1=[]
    verbs=['go','say','yell','exclaim','shout','know','lift','stand','answer','win','get','secure','achieve','hurt','lose','open','close','cook','meet','read','write','draw','drink','pay','buy','stay','work','join','teach','married','date','intract','consult','visit','debate','argue','fight','live','seperate']
    for i in verbs:
        verb1.append(i+"s")
    indirecttag=["I'd like to know", "Do you have any idea","Do you know","Could you tell me"]
    intagsplit=[]
    title=['Dr','Prof','Mr','Mrs','Sr','Bro','Major','Capt','Miss']
    for i in indirecttag:
        
        word=i.split(" ")
        for j in word:
            
            intagsplit.append(j)
    det=['the']
    pronounl=[]
    
    pronoun=['his','her','he','she','it','you']
    pronoun1=[]
    for i in pronoun:
        pronoun1.append(i.capitalize())
    qtag=['what','where','why']
    qtagcap=[]
    for i in qtag:
        qtagcap.append(i.capitalize())
    print("cap",qtagcap)
    hverb=["could","will","would","might","can"]
    hverbcap=[]
    for i in hverb:
        hverbcap.append(i.capitalize())
    doverbs=['do','does','did']
    negverbs=['seldom','hardly']
    article=['a','an']
    onoun=['box','book','cage','scenary','house','building','tea','water','coffee','biriyani','pulav','kichdi','novel','story','match','race','ankle','leg','first-prize','second-prize','job','position','keys','books','poem','story','furniture','vegetables','fruits','bicycles','bicycle','house','organisation','school','college','flat','question']
    prep=['in','for','with','from','on']
    hverb=["could","will","would","might","can"]
    cnoun=["man","gentleman","orator","woman","lady"]
    nhverb=["couldn't","won't","wouldn't","can't","mighn't"]
    adj=['confident','adorable','generous','charming','clever','huge','red','small','heavy','beautiful','fantastic','mesmerising','well-defined','hot','cold','warm','strong-flavored','delicious','tasty','mind-blowing','spicy','excellent','lovely','thrilled','elated','difficult','intelligent','rapid-fire','open-ended','lovely','fascinating','short','precise','interesting','selective','magnificent','high-grade','exceptional','focused','ambitious','demanding','competetive','exciting','brilliant','amazing','three-room','luxurious','spacious','own','modern','adorable','favorite','new','worthy','valuable','expensive','precious','limpy','twisted','sprained','fractured','considerate','attractive','amusing','jovial']
    linkingverb=['"Are','"Did','Are','Did']
    helpnoun=['stupid']
    neg=['not']
    standaloneinter=['Stop','Wait','Oh my goodness','Oh my God','yikes','er','eek','eh']
    conj=['So','and','but']
    
    
    
    def qmtwo(self):
        mandlst=[]
        correctlst=[]
        hintlst=[]
        b=['So','<m>','she','<w>','could','<w>','not','<w>','draw','<w>','the','<w>','scenary','<m>','eek','<m>']
        c=['So',',','she',' ','could',' ','not',',','draw',',','the',',','scenary',',','eek','?']
##        b=['"Look','<w>','at','<w>','that!"','<w>','"John','<w>','exclaimed','<m>','"Did','<w>','you','<w>','know','<m>','"',' ']
##        c=['"Look',',','at',',','that!"',',','"John',',','exclaimed','?','"Did',',','you',',','know','?','"',' ']  
##        b=['Mary','<w>','yelled','<w>','"Why','<w>','not','<m>','"'," "]
##        c=['Mary',',','yelled',' ','"Why',' ','not','?','"',' ']
##        b=['"Are','<w>','you','<w>','stupid','<m>','"','<w>','Alice','<w>','yelled','<m>']
##        c=['"Are',',','you',',','stupid','?','"',' ','Alice',',','yelled','.']
##        b=['"Who','<w>','knows','<m>','"','Mary','<w>','yelled','<m>',' ']
##        c=['"Who',',','knows','?','"','Mary','?','yelled','.',' ']   
##        b=['Prof', '<m>', 'Mary', '<m>', 'a', '<w>', 'confident', '<w>', 'lady','<m>','might','<w>','open','<w>','a','<w>','heavy','<w>','box','<m>',"won't",'<w>','she','<m>',' ']
##        c=['Prof', ',', 'Mary', ',', 'a', '.', 'confident', '.', 'lady',',','might',',','open',',','a',',','heavy',',','box',',',"won't",',','she',' ',' ']
##        
##        b=['You', '<w>', 'seldom', '<w>', 'read', '<w>', 'novel', '<m>', 'do', '<w>', 'you', '<m>',' ']
##        c=['You', '.', 'seldom', '.', 'read', '.', 'novel', '.', 'do', ',', 'you', ',',' ']
        print(c)
##        b=['Where', '<w>','does', '<w>', 'John', '<w>', 'stay', '<m>', '']
##        c=['Where', ',','does', ',', 'John', ',', 'stay', ',', '']
##        b=["I'd", '<w>', 'like', '<w>', 'to', '<w>', 'know', '<w>', 'where', '<w>', 'John', '<w>', 'stays', '<m>', '']
##        c=["I'd", '.', 'like', '.', 'to', '.', 'know', ',', 'where', ';', 'John', '.', 'stays', '.', '']       
##        b=['Do', '<w>', 'you', '<w>', 'have', '<w>', 'any', '<w>', 'idea', '<w>', 'where', '<w>', 'Mary', '<w>', 'stays', '<m>', '']
##        c=['Do', ',', 'you', ',', 'have', ',', 'any', ',', 'idea', ',', 'where', ',', 'Mary', ',', 'stays', '.', '']
        
    #---------------------------------------------------<m> with fullstop-----------------------------------------------------------------------------------
        #rhetorical.py-----------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                  #------------------type9endsurprise----------------------------------------------------------------------------
                if (b[i-1] in qmrules.conj) and (b[i+1] in qmrules.pronoun or b[i+1] in qmrules.snoun):     
                    hint="Read the manual again, HINT:If a sentence starts with a Conjunction like So/Eventhough/But which id followed by a clause, then seperate the conjunction and the clause with a comma"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.onoun) and b[i+1] in qmrules.standaloneinter:
                    hint="Read the manual again, HINT:Put a comma to seperate the clause and the interjection"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.standaloneinter) and c[i]==".":
                    hint="Read the manual again, HINT:if an interjection is intended to show the emotion of surprise,we can put a questionamrk after the interjection"
                    mandlst.append(hint)
                 #----------------------------------------------------------------------------------------------------------------
                if (b[i-3] in qmrules.snoun) and (b[i-1] in qmrules.verb ) and (c[i]=="."):    
                    hint="Correct  Answer:Always end a sentence with fullstop"
                    correctlst.append(hint)
                if (b[i-1] in qmrules.verb1) and (b[i+1]=='"'):    
                    hint="Read the manual again,HINT:Put a question mark within the quotations if it is a direct question "
                    mandlst.append(hint)
                if (b[i-1] in qmrules.helpnoun) and (b[i+1]=='"'):    
                    hint="Read the manual again,HINT:Put a question mark within the quotations if it is a direct question "
                    mandlst.append(hint)
                if (b[i-3]==qmrules.qtagcap) and (b[i-1] in qmrules.neg) and (c[i]=="."):    
                    hint="Read the manual again,HINT:Put a question mark within the quotations if it is a direct question "
                    mandlst.append(hint)
                if (b[i-1] in qmrules.verb) and (c[i]==".") and b[i+1] in qmrules.linkingverb:    
                    hint="Correct  Answer:Always end a sentence with fullstop if it is again followed by quoted words"
                    correctlst.append(hint)
                if (b[i-1] in qmrules.verbs) and b[i+1]=="May":    
                    hint="Read the manual again,HINT:Put a omma ater speakers inferene wen followed by quoted words"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.pronounl) and b[i+1]=='go"':    
                    hint="Read the manual again,HINT:Put a question mark within the quotations if it is a direct question"
                    mandlst.append(hint)      
                    
          #type5------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                  
                if (b[i-1] in qmrules.title) and (b[i+1] in qmrules.snoun):    
                    hint="Correct  Answer:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                    correctlst.append(hint)
                                        
                if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.article):    
                    hint="Read the manual again,HINT:A comma should be used when a relative clause follows the main subject."
                    mandlst.append(hint)
                if (b[i-1] in qmrules.cnoun) and (b[i+1] in qmrules.hverb):    
                    hint="Read the manual again,HINT:A comma should be used when a relative clause follows the main subject."
                    mandlst.append(hint)
                if (b[i-1] in qmrules.onoun) and (b[i+1] in qmrules.nhverb):    
                    hint="Read the manual again,HINT:A comma should be used before a questiontag."
                    mandlst.append(hint)
                if (b[i-3] in qmrules.nhverb) and (b[i-1] in qmrules.pronoun):    
                    hint="Read the manual again:Hint:A questionmark should be used after a questiontag."
                    mandlst.append(hint)
        #---------------------------type5nadvneg.py--------------------------
        for i in range(0,len(b)):
     
             if (b[i]=="<m>" and c[i]=="."):
                if (b[i-1] in qmrules.onoun and (b[i+1] in qmrules.doverbs)):    
                    hint="Read the manual again, HINT:Comma has to be used before a question tag"
                    mandlst.append(hint)
           
                if (b[i-3] in qmrules.doverbs and b[i-1] in qmrules.pronoun and c[i]=="."):    
                    hint="Correct Answer: Fullstop has to be used at the end of an indirect question"
                    mandlst.append(hint)        
        #--------------------------indirectwhat.py-------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                if (b[i-1] in ["stays","cooks"] and (b[i+1]==" ")):    
                    hint="Correct Answer:Fullstop has to be used at the end of indirect questions"
                    correctlst.append(hint)
                    
                if (b[i-1] in qmrules.verbs and (b[i+1]==" ")):    
                    hint="Read the manual again, HINT:Question Mark has to be used at the end of direct questions"
                    correctlst.append(hint)
                    
    #---------------------------------------------------<m> with comma-----------------------------------------------------------------------------------       
                #rhetorical.py-----------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):
                 #------------------type9endsurprise----------------------------------------------------------------------------
                if (b[i-1] in qmrules.conj) and (b[i+1] in qmrules.pronoun or b[i+1] in qmrules.snoun):     
                    hint="Correct Answer:If a sentence starts with a Conjunction like So/Eventhough/But which id followed by a clause, then put seperate the conjunction and the clause with a comma"
                    correctlst.append(hint)
                if (b[i-1] in qmrules.onoun) and b[i+1] in qmrules.standaloneinter:
                    hint="Correct Answer:Put a comma to seperate the clause and the interjection"
                    correctlst.append(hint)
                if (b[i-1] in qmrules.standaloneinter) and b[i-2] in qmrules.onoun:
                    hint="Read the manual again, HINT:if an interjection is intended to show the emotion of surprise,we can put a questionamrk after the interjection"
                    mandlst.append(hint)
            #--------------------------------------  
                if (b[i-3] in qmrules.snoun) and (b[i-1] in qmrules.verb) and c[i]==",":      
                    hint="Read the manual again,HINT:Always end a sentence with fullstop"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.verb1) and (b[i+1]=='"'):    
                    hint="Read the manual again,HINT:Put a question mark within the quotations if it is a direct question"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.helpnoun) and (b[i+1]=='"'):    
                    hint="Read the manual again,HINT:Put a question mark within the quotations if it is a direct question "
                    mandlst.append(hint)
                if b[i-3] in qmrules.qtagcap and (b[i-1] in qmrules.neg) and (c[i]==","):    
                    hint="Read the manual again,HINT:Put a question mark within the quotations if it is a direct question "
                    mandlst.append(hint)
                if (b[i-1] in qmrules.verb ) and (c[i]==",") and b[i+1] in qmrules.linkingverb:    
                    hint="Read the manual again,HINT:Always end a sentence with fullstop if it is again fgollowed by quoted words"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.verbs) and b[i+1]=="May":    
                    hint="Correct Answer:Put a omma ater speakers inferene wen followed by quoted words"
                    correctlst.append(hint)
                if (b[i-1] in qmrules.pronounl) and b[i+1]=='go"':    
                    hint="Read the manual again,HINT:Put a question mark within the quotations if it is a direct question"
                    mandlst.append(hint)        
        #type5.py--------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):
                  
                if (b[i-1] in qmrules.title) and (b[i+1] in qmrules.snoun):    
                    hint="Read the manual again:Hint:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                    mandlst.append(hint)
                                        
                if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.article):    
                    hint="Correct Answer:A comma should be used when a relative clause follows the main subject."
                    correctlst.append(hint)
                if (b[i-1] in qmrules.cnoun) and (b[i+1] in qmrules.hverb):    
                    hint="Correct Answer:A comma should be used when a relative clause follows the main subject."
                    correctlst.append(hint)
                if (b[i-1] in qmrules.onoun) and (b[i+1] in qmrules.nhverb):    
                    hint="Correct Answer:A comma should be used before a questiontag."
                    correctlst.append(hint)
                if (b[i-3] in qmrules.nhverb) and (b[i-1] in qmrules.pronoun):    
                    hint="Read the manual again:Hint:A questionmark should be used after a questiontag."
                    mandlst.append(hint)    
        #------type5nadvneg.py--------------------------
       
                if (b[i-1] in qmrules.onoun and (b[i+1] in qmrules.doverbs)):    
                    hint="Correct Answer,Comma has to be used before a question tag"
                    correctlst.append(hint)
           
                if (b[i-3] in qmrules.doverbs and b[i-1] in qmrules.pronoun and c[i]==","):    
                    hint="Read the manual again, HINT:Fullstop has to be used at the end of an indirect question"
                    mandlst.append(hint) 
         #--------------------------indirectwhat.py-------------------------------------
       
                if (b[i-1] in ["stays","cooks"] and (b[i+1]=="")):    
                    hint="Read the manual again, HINT:Fullstop has to be used at the end of indirect questions"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.verbs and (b[i+1]=="")):    
                    hint="Read the manual again, HINT:Question Mark has to be used at the end of direct questions"
                    mandlst.append(hint)    
                    #print(mandlst)
    #---------------------------------------------------<m> with questionamrk-----------------------------------------------------------------------------------       
        #rhetorical.py-----------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="?"):
                #------------------type9endsurprise----------------------------------------------------------------------------
                if (b[i-1] in qmrules.conj) and (b[i+1] in qmrules.pronoun or b[i+1] in qmrules.snoun)  :     
                    hint="Read the manual again, HINT:If a sentence starts with a Conjunction like So/Eventhough/But which id followed by a clause, then seperate the conjunction and the clause with a comma"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.onoun) and b[i+1] in qmrules.standaloneinter:
                    hint="Read the manual again, HINT:Put a comma to seperate the clause and the interjection"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.standaloneinter) and b[i-2] in qmrules.onoun:
                    hint="Correct Answer:if an interjection is intended to show the emotion of surprise,we can put a questionamrk after the interjection"
                    correctlst.append(hint)
                #------
                  
                if (b[i-3] in qmrules.snoun) and  (b[i-1] in qmrules.verb) and c[i]=="?":       
                    hint="Read the manual again,HINT:Always end a sentence with fullstop"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.verb1) and (b[i+1]=='"'):    
                    hint="Correct Answer:Always put a question mark within the quotations if it is a direct question"
                    correctlst.append(hint)
                if (b[i-1] in qmrules.helpnoun) and (b[i+1]=='"'):    
                    hint="Correct Answer:Always put a question mark within the quotations if it is a direct question"
                    correctlst.append(hint)
                if b[i-3] in qmrules.qtagcap and (b[i-1] in qmrules.neg) and (c[i]=="?"):    
                    hint="Correct Answer:Always put a question mark within the quotations if it is a direct question"
                    correctlst.append(hint)
           
                if (b[i-1] in qmrules.verb) and (c[i]=="?") and b[i+1] in qmrules.linkingverb:    
                    hint="Read the manual again,HINT:Always end a sentence with fullstop if it is again fgollowed by quoted words"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.verbs) and b[i+1]=="May":    
                    hint="Read the manual again,HINT:Put a omma ater speakers inferene wen followed by quoted words"
                    mandlst.append(hint)       
                if (b[i-1] in qmrules.pronoun1) and b[i+1]=='go"':    
                    hint="Correct Answer:Put a question mark within the quotations if it is a direct question"
                    correctlst.append(hint) 
        #type5------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="?"):
                  
                if (b[i-1] in qmrules.title) and (b[i+1] in qmrules.snoun):    
                    hint="Read the manual again:Hint:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                    mandlst.append(hint)
                                        
                if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.article):    
                    hint="Read the manual again,HINT:A comma should be used when a relative clause follows the main subject."
                    mandlst.append(hint)
                if (b[i-1] in qmrules.cnoun) and (b[i+1] in qmrules.hverb):    
                    hint="Read the manual again,HINT:A comma should be used when a relative clause follows the main subject."
                    mandlst.append(hint)
                if (b[i-1] in qmrules.onoun) and (b[i+1] in qmrules.nhverb):    
                    hint="Read the manual again,HINT:A comma should be used before a questiontag."
                    mandlst.append(hint)
                if (b[i-3] in qmrules.nhverb) and (b[i-1] in qmrules.pronoun):    
                    hint="Correct Answer:A questionmark should be used after a questiontag."
                    correctlst.append(hint)
         #-------------------------type5nadvneg.py--------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="?"):
                if (b[i-1] in qmrules.onoun and (b[i+1] in qmrules.doverbs)):    
                    hint="Read the manual again, HINT:Comma has to be used before a question tag"
                    mandlst.append(hint)
           
                if (b[i-3] in qmrules.doverbs and b[i-1] in qmrules.pronoun and c[i]=="?"):    
                    hint="Read the manual again, HINT:Fullstop has to be used at the end of an indirect question"
                    mandlst.append(hint)
         #--------------------------indirectwhat.py-------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="?"):
                if (b[i-1] in ["stays","cooks"] and (b[i+1]=="")):    
                    hint="Read the manual again, HINT:Fullstop has to be used at the end of indirect questions"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.verbs and (b[i+1]=="")):    
                    hint="Correct Answer:Question mark has to be used at the end of direct questions"
                    correctlst.append(hint)     
                    #print(correctlst)                      
    #---------------------------------------------------<m> with no punctuation-----------------------------------------------------------------------------------       

         #rhetorical.py-----------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==" "):
                  #------------------type9endsurprise----------------------------------------------------------------------------
                if (b[i-1] in qmrules.conj) and (b[i+1] in qmrules.pronoun or b[i+1] in qmrules.snoun):     
                    hint="Read the manual again, HINT:If a sentence starts with a Conjunction like So/Eventhough/But which id followed by a clause, then                  seperate the conjunction and the clause with a comma"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.onoun) and b[i+1] in qmrules.standaloneinter:
                    hint="Read the manual again, HINT:Put a comma to seperate the clause and the interjection"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.standaloneinter) and b[i-2] in qmrules.onoun:
                    hint="Read the manual again, HINT:if an interjection is intended to show the emotion of surprise,we can put a questionamrk after the interjection"
                    mandlst.append(hint)
                #--------  
                if (b[i-1] in qmrules.verb) and c[i]==" ":      
                    hint="Read the manual again,HINT:Always end a sentence with fullstop"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.verb1) and (b[i+1]=='"'):    
                    hint="Read the manual again,HINT:Put a question mark within the quotations if it is a direct question "
                    mandlst.append(hint)
                if (b[i-1] in qmrules.helpnoun) and (b[i+1]=='"'):    
                    hint="Read the manual again,HINT:Put a question mark within the quotations if it is a direct question "
                    mandlst.append(hint)
                if (b[i-1] in qmrules.neg) and (c[i]==" pp"):    
                    hint="Read the manual again,HINT:Always end a sentence with fullstop"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.verbs) and b[i+1]=="May":    
                    hint="Read the manual again,HINT:Put a omma ater speakers inferene wen followed by quoted words"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.pronounl) and b[i+1]=='go"':    
                    hint="Read the manual again,HINT:Put a question mark within the quotations if it is a direct question"
                    mandlst.append(hint)    
         #type5------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==" "):
                  
                if (b[i-1] in qmrules.title) and (b[i+1] in qmrules.snoun):    
                    hint="Read the manual again:Hint:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                    mandlst.append(hint)
                                        
                if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.article):    
                    hint="Read the manual again,HINT:A comma should be used when a relative clause follows the main subject."
                    mandlst.append(hint)
                if (b[i-1] in qmrules.cnoun) and (b[i+1] in qmrules.hverb):    
                    hint="Read the manual again,HINT:A comma should be used when a relative clause follows the main subject."
                    mandlst.append(hint)
                if (b[i-1] in qmrules.onoun) and (b[i+1] in qmrules.nhverb):    
                    hint="Read the manual again,HINT:A comma should be used before a questiontag."
                    mandlst.append(hint)
                if (b[i-3] in qmrules.nhverb) and (b[i-1] in qmrules.pronoun):    
                    hint="Read the manual again,HINT:A questionmark should be used after a questiontag."
                    mandlst.append(hint)
         #-------------------------type5nadvneg.py--------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==" "):
                if (b[i-1] in qmrules.onoun and (b[i+1] in qmrules.doverbs)):    
                    hint="Read the manual again, HINT:Comma has to be used before a question tag"
                    mandlst.append(hint)
           
                if (b[i-3] in qmrules.doverbs and b[i-1] in qmrules.pronoun and (b[i+1]==" ")):    
                    hint="Read the manual again, HINT:Fullstop has to be used at the end of an indirect question"
                    mandlst.append(hint)
         #--------------------------indirectwhat.py-------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==" "):
                if (b[i-1] in ["stays","cooks"] and (b[i+1]=="")):    
                    hint="Read the manual again, HINT:Fullstop has to be used at the end of indirect questions"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.verb and (b[i+1]=="")):    
                    hint="Read the manual again, HINT:Question Mark has to be used at the end of direct questions"
                    mandlst.append(hint)     
                    #print(mandlst) 
    #---------------------------------------------------<w> with fullstop-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<w>" and c[i]=="."):
                #-----type9endsurprise------
                 if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.hverb):    
                    hint="Read the manual again,HINT:No need of any punctuation between a noun and a helping verb"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.hverb) and (b[i+1] =="not"):    
                    hint="Read the manual again,HINT:No need of any punctuation between could and not"
                    hintlst.append(hint)
                 if (b[i-1] =="not") and (b[i+1] in qmrules.verb):    
                    hint="Read the manual again,HINT:No need of any punctuation between a negation and a verb"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.verb) and (b[i+1] in qmrules.det):    
                    hint="Read the manual again,HINT:No need of any punctuation between a verb and a determiner"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.det) and (b[i+1] in qmrules.onoun):    
                    hint="Read the manual again,HINT:No need of any punctuation between a determiner and a noun"
                    hintlst.append(hint)   
                #--------------------------rhetorical.py-----------------
                  
                 if (b[i-1]=='"Who') and (b[i+1] in qmrules.verb1):    
                    hint="Read The manual again, HINT:No need of a fullstop in between a sentence"
                    hintlst.append(hint)
                 if (b[i-1] =='"') and (b[i+1] in qmrules.snoun):    
                    hint="Read the manual again,HINT:No need of any punctuation after the quotations"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.verb):    
                    hint="Read the manual again,HINT:No need of any punctuation between a noun and a verb"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.linkingverb) and (b[i+1] in qmrules.pronoun):    
                    hint="Read the manual again,HINT:No need of any punctuation between a ['Are'/Do/Did] and a pronoun"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.pronoun) and (b[i+1] in qmrules.helpnoun):    
                    hint="Read the manual again,HINT:No need of any punctuation between a pronoun and a noun"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.verb) and (b[i+1] =='"'):    
                    hint="Read the manual again,HINT:No need of any punctuation immediately before an opening quotation"
                    hintlst.append(hint)
                 if (b[i-1] =='"') and (b[i+1] in qmrules.qtagcap):    
                    hint="Read the manual again,HINT:No need of any punctuation immediately after an opening quotation"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.qtagcap) and (b[i+1] in qmrules.neg):    
                    hint="Read the manual again,HINT:No need of any punctuation in between a question tag"
                    hintlst.append(hint)
                 if (b[i-1]=='"Look') and (b[i+1] == 'at'):    
                    hint="Read the manual again,HINT:No need of any punctuation a verb and and prep...should be considered as a single entity"
                    hintlst.append(hint)
                 if (b[i-1]=='at') and (b[i+1] == 'that!"'):    
                    hint="Read the manual again,HINT:No need of any punctuation after a preposition..should be considered as a single entity"
                    hintlst.append(hint) 
                 if (b[i-1]=='that!"') and (b[i+1] in qmrules.snoun):    
                    hint="Read the manual again,HINT:No need of any punctuation after the quoted words."
                    hintlst.append(hint) 
                 if (b[i-1] in qmrules.pronoun) and (b[i+1] in qmrules.verbs):    
                    hint="Read the manual again,HINT:No need of any punctuation between a pronoun and a verb"
                    hintlst.append(hint)
                 if b[i-1] in qmrules.hverbcap and b[i+1] in qmrules.pronounl:
                    hint="Read The manual again, HINT:No need to add a fullstop in between a helping verb like (can,could,may) and a pronoun"
                    hintlst.append(hint)
                 if b[i-1] in qmrules.pronounl and b[i+1] in qmrules.verbs:
                    hint="Read The manual again, HINT:No need to add a fullstop in between a pronoun and a verb"
                    hintlst.append(hint)     
                #----------------------------type5.py---------------------------------------
                 if b[i-1] in qmrules.article and b[i+1] in qmrules.adj:
                    hint="Read The manual again, HINT:No need to seperate an article and a adjective with comma"
                    hintlst.append(hint)
                 if b[i-1] in qmrules.adj and b[i+1] in qmrules.cnoun:
                    hint="Read The manual again, HINT:No need to add a fullstop in between a noun/adjective phrase"
                    hintlst.append(hint)
                 if b[i-1] in qmrules. hverb and b[i+1] in qmrules.verb:
                    hint="Read The manual again, HINT:No need to add a fullstop in between a helping verb like (can,could) and a verb"
                    hintlst.append(hint)
                 if b[i-1] in qmrules.verb and b[i+1] in qmrules.article:
                    hint="Read The manual again, HINT:No need to put a fullstop before an article if it is preceeded by a verb"
                    hintlst.append(hint)
                 if b[i-1] in qmrules.article and b[i+1] in qmrules.adj:
                    hint="Read The manual again, HINT:Don't put a fullstop in between an adjective phrase or noun phrase,especially after an article like [a,an]"
                    hintlst.append(hint)
                 if b[i-1] in qmrules.adj and b[i+1] in qmrules.onoun:
                   hint="Read The manual again, HINT:No need to add a fullstop in between a noun/adjective phrase"
                   hintlst.append(hint)
                 if b[i-1] in qmrules.nhverb and b[i+1] in qmrules.pronoun:
                   hint="Read The manual again, HINT:No need to add a fullstop in between question tags"
                   hintlst.append(hint)
                 #-------------------------type5nadvneg.py--------------------------
      
                 if (b[i-1] in qmrules.verb or qmrules.verbs) and (b[i+1] in qmrules.article):    
                    hint="Read the manual again, HINT::No need of a punctuation between a verb and a article"
                    mandlst.append(hint)
                 if (b[i-1] in qmrules.article) and (b[i+1] in qmrules.onoun):    
                    hint="Read the manual again, HINT::No need of a punctuation between an article and a noun"
                    mandlst.append(hint)
                 if (b[i-1] in qmrules.doverbs) and (b[i+1] in qmrules.pronoun):    
                    hint="Read the manual again, HINT::No need of a punctuation between do/did and a pronoun"
                    mandlst.append(hint)     
                 if (b[i-1] in qmrules.pronoun1 and (b[i+1] in qmrules.negverbs)):    
                    hint="Read the manual again, HINT:No need of a punctuation between a pronoun and a negative adverb"
                    mandlst.append(hint)
                 if (b[i-1] in qmrules.negverbs and (b[i+1] in qmrules.verb or qmrules.verbs)):    
                    hint="Read the manual again, HINT:No need of a punctuation between a negative adverb and a verb"
                    mandlst.append(hint)    
                 #--------------------------indirectwhat.py-------------------------------------
                 if (b[i-1] in qmrules.intagsplit) and (b[i+1] in qmrules.intagsplit):  
                    hint="Read the manual again, HINT:No need of a fullstop in between indirect question tags"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.intagsplit) and (b[i+1] in qmrules.qtag):  
                    hint="Read the manual again, HINT:No need of a fullstop before a question tag"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.qtag) and (b[i+1] in qmrules.snoun):  
                    hint="Read the manual again, HINT:No need of a fullstop between a question tag and a noun"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.verb1):  
                    hint="Read the manual again, HINT:No need of a fullstop between a noun and a verb"
                    hintlst.append(hint)
                  #--------------------------/directq/directwhat.py-------------------------------------  
                 if (b[i-1] in qmrules.qtagcap) and (b[i+1] in qmrules.doverbs):  
                    hint="Read the manual again, HINT:No need of a fullstop after a question tag"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.doverbs) and (b[i+1] in qmrules.snoun):  
                    hint="Read the manual again, HINT:No need of a fullstop after 'do/does/did'"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.verbs):  
                    hint="Read the manual again, HINT:No need of a fullstop between a noun and a verb"
                    hintlst.append(hint)   
    #---------------------------------------------------<w> with comma-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<w>" and c[i]==","):
                #-----type9endsurprise------
                 if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.hverb):    
                    hint="Read the manual again,HINT:No need of any punctuation between a noun and a helping verb"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.hverb) and (b[i+1] =="not"):    
                    hint="Read the manual again,HINT:No need of any punctuation between could and not"
                    hintlst.append(hint)
                 if (b[i-1] =="not") and (b[i+1] in qmrules.verbs):    
                    hint="Read the manual again,HINT:No need of any punctuation between a negation and a verb"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.verbs
                     ) and (b[i+1] in qmrules.det):    
                    hint="Read the manual again,HINT:No need of any punctuation between a verb and a determiner"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.det) and (b[i+1] in qmrules.onoun):    
                    hint="Read the manual again,HINT:No need of any punctuation between a determiner and a noun"
                    hintlst.append(hint)  
                #--------------------------rhetorical.py-----------------
                  
                 if (b[i-1]=='"Who') and (b[i+1] in qmrules.verb1):    
                    hint="Read The manual again, HINT:No need of a comma in between a sentence especially after a Wh-question tag"
                    hintlst.append(hint)
                 if (b[i-1] =='"') and (b[i+1] in qmrules.snoun):    
                    hint="Read the manual again,HINT:No need of any punctuation after the quotations"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.verb):    
                    hint="Read the manual again,HINT:No need of any punctuation between a noun and a verb"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.linkingverb) and (b[i+1] in qmrules.pronoun):    
                    hint="Read the manual again,HINT:No need of any punctuation between a ['Are'/Do/Did] and a pronoun"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.pronoun) and (b[i+1] in qmrules.helpnoun):    
                    hint="Read the manual again,HINT:No need of any punctuation between a pronoun and a noun"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.verb) and (b[i+1] =='"'):    
                    hint="Read the manual again,HINT:No need of any punctuation immediately before an opening quotation"
                    hintlst.append(hint)
                 if (b[i-1] =='"') and (b[i+1] in qmrules.qtagcap):    
                    hint="Read the manual again,HINT:No need of any punctuation immediately after an opening quotation"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.qtagcap) and (b[i+1] in qmrules.neg):    
                    hint="Read the manual again,HINT:No need of any punctuation in between a question tag"
                    hintlst.append(hint) 
                 if (b[i-1]=='"Look') and (b[i+1] == 'at'):    
                    hint="Read the manual again,HINT:No need of any punctuation a verb and and prep...should be considered as a single entity"
                    hintlst.append(hint)
                 if (b[i-1]=='at') and (b[i+1] == 'that!"'):    
                    hint="Read the manual again,HINT:No need of any punctuation after a preposition..should be considered as a single entity"
                    hintlst.append(hint) 
                 if (b[i-1]=='that!"') and (b[i+1] in qmrules.snoun):    
                    hint="Read the manual again,HINT:No need of any punctuation after the quoted words."
                    hintlst.append(hint) 
                 if (b[i-1] in qmrules.pronoun) and (b[i+1] in qmrules.verbs):    
                    hint="Read the manual again,HINT:No need of any punctuation between a pronoun and a verb"
                    hintlst.append(hint)
                 if b[i-1] in qmrules. hverbcap and b[i+1] in qmrules.pronounl:
                    hint="Read The manual again, HINT:No need to add a comma in between a helping verb like (can,could,may) and a pronoun"
                    hintlst.append(hint)
                 if b[i-1] in qmrules.pronoun1 and b[i+1] in qmrules.verbs:
                    hint="Read The manual again, HINT:No need to add a comma in between a pronoun and a verb"
                    hintlst.append(hint)     
                #--------------type5.py---------------------------------------
                 if b[i-1] in qmrules.article and b[i+1] in qmrules.adj:
                    hint="Read The manual again, HINT:No need to seperate an article and a adjective with comma"
                    hintlst.append(hint)
                 if b[i-1] in qmrules.adj and b[i+1] in qmrules.cnoun:
                    hint="Read The manual again, HINT:No need to add a comma in between a noun/adjective phrase"
                    hintlst.append(hint)
                 if b[i-1] in qmrules. hverb and b[i+1] in qmrules.verb:
                    hint="Read The manual again, HINT:No need to add a comma in between a helping verb like (can,could) and a verb"
                    hintlst.append(hint)
                 if b[i-1] in qmrules.verb and b[i+1] in qmrules.article:
                    hint="Read The manual again, HINT:No need to put a comma before an article if it is preceeded by a verb"
                    hintlst.append(hint)
                 if b[i-1] in qmrules.article and b[i+1] in qmrules.adj:
                    hint="Read The manual again, HINT:Don't put a comma in between an adjective phrase or noun phrase,especially after an article like [a,an]"
                    hintlst.append(hint)
                 if b[i-1] in qmrules.adj and b[i+1] in qmrules.onoun:
                   hint="Read The manual again, HINT:No need to add a comma in between a noun/adjective phrase"
                   hintlst.append(hint)
                 if b[i-1] in qmrules.nhverb and b[i+1] in qmrules.pronoun:
                   hint="Read The manual again, HINT:No need to add a comma in between question tags"
                   hintlst.append(hint)
                #-------------------------type5nadvneg.py--------------------------
      
                 if (b[i-1] in qmrules.verb or b[i-1] in qmrules.verbs) and (b[i+1] in qmrules.article):    
                    hint="Read the manual again, HINT::No need of a punctuation between a verb and a article"
                    mandlst.append(hint)
                 if (b[i-1] in qmrules.article) and (b[i+1] in qmrules.onoun):    
                    hint="Read the manual again, HINT::No need of a punctuation between an article and a noun"
                    mandlst.append(hint)
                 if (b[i-1] in qmrules.doverbs) and (b[i+1] in qmrules.pronoun):    
                    hint="Read the manual again, HINT::No need of a punctuation between do/did and a pronoun"
                    mandlst.append(hint)     
                 if (b[i-1] in qmrules.pronoun1 and (b[i+1] in qmrules.negverbs)):    
                    hint="Read the manual again, HINT:No need of a punctuation between a pronoun and a negative adverb"
                    mandlst.append(hint)
                 #--------------------------indirectwhat.py-------------------------------------
                 if (b[i-1] in qmrules.intagsplit) and (b[i+1] in qmrules.intagsplit):  
                    hint="Read the manual again, HINT:No need of a comma in between indirect question tags"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.intagsplit) and (b[i+1] in qmrules.qtag):  
                    hint="Read the manual again, HINT:No need of a comma before a question tag"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.qtag) and (b[i+1] in qmrules.snoun):  
                    hint="Read the manual again, HINT:No need of a comma between a question tag and a noun"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.verb1):  
                    hint="Read the manual again, HINT:No need of a comma between a noun and a verb"
                    hintlst.append(hint)
                   #--------------------------/directq/directwhat.py-------------------------------------  
                 if (b[i-1] in qmrules.qtagcap) and (b[i+1] in qmrules.doverbs):  
                    hint="Read the manual again, HINT:No need of a comma after a question tag"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.doverbs) and (b[i+1] in qmrules.snoun):  
                    hint="Read the manual again, HINT:No need of a comma after 'do/does/did'"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.verbs):  
                    hint="Read the manual again, HINT:No need of a comma between a noun and a verb"
                    hintlst.append(hint)       
    #---------------------------------------------------<w> with questionamrk-----------------------------------------------------------------------------------      
        for i in range(0,len(b)):
            if (b[i]=="<w>" and c[i]=="?"):
                #-----type9endsurprise------
                 if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.hverb):    
                    hint="Read the manual again,HINT:No need of any punctuation between a noun and a helping verb"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.hverb) and (b[i+1] =="not"):    
                    hint="Read the manual again,HINT:No need of any punctuation between could and not"
                    hintlst.append(hint)
                 if (b[i-1] =="not") and (b[i+1] in qmrules.verb):    
                    hint="Read the manual again,HINT:No need of any punctuation between a negation and a verb"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.verb) and (b[i+1] in qmrules.det):    
                    hint="Read the manual again,HINT:No need of any punctuation between a verb and a determiner"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.det) and (b[i+1] in qmrules.onoun):    
                    hint="Read the manual again,HINT:No need of any punctuation between a determiner and a noun"
                    hintlst.append(hint)  
                #--------------------------rhetorical.py-----------------
                  
                 if (b[i-1]=='"Who') and (b[i+1] in qmrules.verb1):    
                    hint="Read The manual again, HINT:No need of a questionmark in between a sentence especially after a Wh-question tag"
                    hintlst.append(hint)
                 if (b[i-1] =='"') and (b[i+1] in qmrules.snoun):    
                    hint="Read the manual again,HINT:No need of any punctuation after the quotations"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.verb):    
                    hint="Read the manual again,HINT:No need of any punctuation between a noun and a verb"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.linkingverb) and (b[i+1] in qmrules.pronoun):    
                    hint="Read the manual again,HINT:No need of any punctuation between a  and a pronoun"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.pronoun) and (b[i+1] in qmrules.helpnoun):    
                    hint="Read the manual again,HINT:No need of any punctuation between a pronoun and a noun"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.verb) and (b[i+1] =='"'):    
                    hint="Read the manual again,HINT:No need of any punctuation immediately before an opening quotation"
                    hintlst.append(hint)
                 if (b[i-1] =='"') and (b[i+1] in qmrules.qtagcap):    
                    hint="Read the manual again,HINT:No need of any punctuation immediately after an opening quotation"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.qtagcap) and (b[i+1] in qmrules.neg):    
                    hint="Read the manual again,HINT:No need of any punctuation in between a question tag"
                    hintlst.append(hint) 
                 if (b[i-1]=='"Look') and (b[i+1] == 'at'):    
                    hint="Read the manual again,HINT:No need of any punctuation a verb and and prep...should be considered as a single entity"
                    hintlst.append(hint)
                 if (b[i-1]=='at') and (b[i+1] == 'that!"'):    
                    hint="Read the manual again,HINT:No need of any punctuation after a preposition..should be considered as a single entity"
                    hintlst.append(hint) 
                 if (b[i-1]=='that!"') and (b[i+1] in qmrules.snoun):    
                    hint="Read the manual again,HINT:No need of any punctuation after the quoted words."
                    hintlst.append(hint) 
                 if (b[i-1] in qmrules.pronoun) and (b[i+1] in qmrules.verbs):    
                    hint="Read the manual again,HINT:No need of any punctuation between a pronoun and a verb"
                    hintlst.append(hint)
                 if b[i-1] in qmrules. hverbcap and b[i+1] in qmrules.pronounl:
                    hint="Read The manual again, HINT:No need to add a questionmark in between a helping verb like (can,could,may) and a pronoun"
                    hintlst.append(hint)
                 if b[i-1] in qmrules.pronounl and b[i+1] in qmrules.verbs:
                    hint="Read The manual again, HINT:No need to add a questionmark in between a pronoun and a verb"
                    hintlst.append(hint)    
                #--------------type5.py---------------------------------------
                 if b[i-1] in qmrules.article and b[i+1] in qmrules.adj:
                    hint="Read The manual again, HINT:No need to seperate an article and a adjective with comma"
                    hintlst.append(hint)
                 if b[i-1] in qmrules.adj and b[i+1] in qmrules.cnoun:
                    hint="Read The manual again, HINT:No need to add a questionamrk in between a noun/adjective phrase"
                    hintlst.append(hint)
                 if b[i-1] in qmrules. hverb and b[i+1] in qmrules.verb:
                    hint="Read The manual again, HINT:No need to add a questionamrk in between a helping verb like (can,could) and a verb"
                    hintlst.append(hint)
                 if b[i-1] in qmrules.verb and b[i+1] in qmrules.article:
                    hint="Read The manual again, HINT:No need to put a questionamrk before an article if it is preceeded by a verb"
                    hintlst.append(hint)
                 if b[i-1] in qmrules.article and b[i+1] in qmrules.adj:
                    hint="Read The manual again, HINT:Don't put a questionamrk in between an adjective phrase or noun phrase,especially after an article like [a,an]"
                    hintlst.append(hint)
                 if b[i-1] in qmrules.adj and b[i+1] in qmrules.onoun:
                   hint="Read The manual again, HINT:No need to add a questionamrk in between a noun/adjective phrase"
                   hintlst.append(hint)
                 if b[i-1] in qmrules.nhverb and b[i+1] in qmrules.pronoun:
                   hint="Read The manual again, HINT:No need to add a questionamrk in between question tags"
                   hintlst.append(hint)
                
                    
                #-------------------------type5nadvneg.py--------------------------
      
                 if (b[i-1] in qmrules.verb or b[i-1] in qmrules.verbs) and (b[i+1] in qmrules.article):    
                    hint="Read the manual again, HINT::No need of a punctuation between a verb and a article"
                    mandlst.append(hint)
                 if (b[i-1] in qmrules.article) and (b[i+1] in qmrules.onoun):    
                    hint="Read the manual again, HINT::No need of a punctuation between an article and a noun"
                    mandlst.append(hint)
                 if (b[i-1] in qmrules.doverbs) and (b[i+1] in qmrules.pronoun):    
                    hint="Read the manual again, HINT::No need of a punctuation between do/did and a pronoun"
                    mandlst.append(hint)     
                 if (b[i-1] in qmrules.pronoun1 and (b[i+1] in qmrules.negverbs)):    
                    hint="Read the manual again, HINT:No need of a punctuation between a pronoun and a negative adverb"
                    mandlst.append(hint)
                 #--------------------------indirectwhat.py-------------------------------------
                 if (b[i-1] in qmrules.intagsplit) and (b[i+1] in qmrules.intagsplit):  
                    hint="Read the manual again, HINT:No need of a questionmark in between indirect question tags"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.intagsplit) and (b[i+1] in qmrules.qtag):  
                    hint="Read the manual again, HINT:No need of a question mark before a question tag"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.qtag) and (b[i+1] in qmrules.snoun):  
                    hint="Read the manual again, HINT:No need of a question mark between a question tag and a noun"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.verb1):  
                    hint="Read the manual again, HINT:No need of a questionmark between a noun and a verb"
                    hintlst.append(hint)
                  #--------------------------/directq/directwhat.py-------------------------------------  
                 if (b[i-1] in qmrules.qtagcap) and (b[i+1] in qmrules.doverbs):  
                    hint="Read the manual again, HINT:No need of a questionmark after a question tag"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.doverbs) and (b[i+1] in qmrules.snoun):  
                    hint="Read the manual again, HINT:No need of a questionmark after 'do/does/did'"
                    hintlst.append(hint)
                 if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.verbs):  
                    hint="Read the manual again, HINT:No need of a questionmark between a noun and a verb"
                    hintlst.append(hint)        
        return(correctlst,mandlst,hintlst)   
  
    

            
p1=qmrules()
c,m,h=p1.qmtwo()
for i in c:
    print(i)
for j in m:
    print(j)
for k in h:
    print(k)    
