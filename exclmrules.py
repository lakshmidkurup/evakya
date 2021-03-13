import datetime
##import mysql.connector
##from dateutil.parser import parse
##mydb = mysql.connector.connect(
##                host="localhost",
##                user="root",
##                passwd="rohith@123",
##                database="pythonlogin"
##        )
##mycursor = mydb.cursor()
class exclmrules:
    snoun=['Mary','James','John','Alice','A. Roy', 'K. Singh', 'R. K. Narayan', 'R. Kushner','Esmail','Bagani' ]
    verb=['lift','stand','answered','won','got','secured','achieved','hurt','lost','opened','closed','cooked','met','read','wrote','drew','drank','paid','bought','stayed','worked','joined','taught','married','dated','intracted','consulted','visited','debated','argued','fought','lived','seperated']
    article=['a','an']
    det=['the']
    adj=['confident','adorable','generous','charming','clever','huge','red','small','heavy','beautiful','fantastic','mesmerising','well-defined','hot','cold','warm','strong-flavored','delicious','tasty','mind-blowing','spicy','excellent','lovely','thrilled','elated','difficult','intelligent','rapid-fire','open-ended','lovely','fascinating','short','precise','interesting','selective','magnificent','high-grade','exceptional','focused','ambitious','demanding','competetive','exciting','brilliant','amazing','three-room','luxurious','spacious','own','modern','adorable','favorite','new','worthy','valuable','expensive','precious','limpy','twisted','sprained','fractured','considerate','attractive','amusing','jovial']
    onoun=['box','book','cage','scenary','house','building','tea','water','coffee','biriyani','pulav','kichdi','novel','story','match','race','ankle','leg','first-prize','second-prize','job','position','keys','books','poem','story','furniture','vegetables','fruits','bicycles','bicycle','house','organisation','school','college','flat','question']
    prep=['in','for','with','from','on']
    adverb=['slowly','carefully','frequently','eagerly','keenly','joyful','deliciously','artistically','happily','finally','fast','very','extremely']
    qtag=['What','How','Why','Where']
    vbz=['are','is','was','has','had','have']
    pronoun=['his','her','he','she','it']
    exclm=['Ah','Aha','Wow','Hi','Alas','Oh','Hey','Yippee']
    article=['a','an']
    det=['the']
    title=['Dr','Prof','Mr','Mrs','Sr','Bro','Major','Capt','Miss']
    cnoun=["man","gentleman","orator","woman","lady"]
    standaloneinter=['Stop','Wait','Oh my goodness','Oh my God','yikes','er','eek','eh','Yippee']
    adj=['confident','adorable','generous','charming','clever','huge','red','small','heavy','beautiful','fantastic','mesmerising','well-defined','hot','cold','warm','strong-flavored','delicious','tasty','mind-blowing','spicy','excellent','lovely','thrilled','elated','difficult','intelligent','rapid-fire','open-ended','lovely','fascinating','short','precise','interesting','selective','magnificent','high-grade','exceptional','focused','ambitious','demanding','competetive','exciting','brilliant','amazing','three-room','luxurious','spacious','own','modern','adorable','favorite','new','worthy','valuable','expensive','precious','limpy','twisted','sprained','fractured','considerate','attractive','amusing','jovial']
    conj=['So','and','but']
    standalonesplit=[]
    determiner=['This','That','Those','The']
    det=["Those're","That's"]
    for i in standaloneinter:
        words=i.split(" ")
        standalonesplit.extend(words)
    print(standalonesplit)
    def exclmone(b,c,correct,category,level,username,userid,eid,submittedtext):
##    def exclmone(self):
    
        
##        b=['What', '<w>', 'a', '<w>', 'fascinating', '<w>', 'book', '<w>', 'it', '<w>', 'is', '<m>']
##        c=['What', ' ', 'a', ' ', 'fascinating', ' ', 'book', ' ', 'it', ' ', 'is', ' ', '!', ' ']
##        b=['Ah', '<c>', 'What', '<w>', 'a', '<w>', 'precise', '<w>', 'poem', '<c>']
##        c=['Ah', '!', 'What', ' ', 'a', ' ', 'precise', ' ', 'poem', '.']
##        b=['Ah', '<c>', 'What', '<w>', 'a', '<w>', 'precise', '<w>', 'poem', '<c>', ' ']
##        c=['Ah', ' ', '!', ' ', 'What', ' ', 'a', ' ', 'precise', ' ', 'poem', '.', ' ']
##        b=['Yippee', '<c>', 'Prof', '<m>', 'John', '<m>', 'a', '<w>', 'generous', '<w>', 'orator', '<m>', 'has', '<w>', 'won', '<w>', 'the', '<w>', 'race', '<c>']
##        c=['Yippee', '!', 'Prof', '.', 'John', ',', 'a', ' ', 'generous', ' ', 'orator', ',', 'has', ' ', 'won', ' ', 'the', ' ', 'race', '.']
##        b=['"', '<w>', 'Wait', '<m>', '"', '<w>', ' ']
##        c=['"', ' ', 'Wait', '!', '"', ' ', ' ']
        print("bone",b)
        print("cone",c)
        b.append(" ")
        c.append(" ")
        ct=0
        for i in b:
            if i=="<m>" or i=="<c>":
                ct=ct+1
        mandatory=ct
        print(ct)
        hintlst=[]
        correctlst=[]
        mandlst=[]
        print(b)
        print(c)
##        print("c[-2]",c[-2])
##        

          #------------------------------------------<c> with exclm--------------------------------------
        for i in range(0,len(c)):
           if (b[i]=="<c>" and c[1]==" " and c[-2] in [".",",","!"]) :
                   
                hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                mandlst.append(hint)
           if (b[i]=="<c>" and c[-2]==" " and c[1] in [".",",","!"]) :
               
                hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                mandlst.append(hint)    
               
           if (b[i]=="<c>" and c[1]=="!" and c[-2]==".") :
                hint="Correct Answer:If you put an exclamation after an interjection, the sentence has to be ended with a period"
                correctlst.append(hint)
           if (b[i]=="<c>" and c[1]=="!" and c[-2]=="!") :
                hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]=="!" and c[-2]==",") :
                hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                mandlst.append(hint)     
           if (b[i]=="<c>" and c[1]=="," and c[-2]=="!") :
                hint="Correct Answer:If you put an comma after an interjection, the sentence has to be ended with a exclamation"
                correctlst.append(hint)
           if (b[i]=="<c>" and c[1]=="," and c[-2]==".") :
                hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                mandlst.append(hint) 
           if (b[i]=="<c>" and c[1]=="," and c[-2]==",") :
                hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]=="." and c[-2]==".") :
                hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]=="." and c[-2]==",") :
                hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]=="." and c[-2]=="!") :
                hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]==" " and c[-2]=="!") :
                hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]==" " and c[-2]==".") :
                hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]==" " and c[-2] in [" ",","]) :
                hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                mandlst.append(hint)
        #-----------------------------------------<m> with exclamation----------------------------------------------------------------------------
        for i in range(0,len(b)):
           
            if (b[i]=="<m>" and c[i]=="!"):
                #------------------type9endsurprise-----------------------------------------------------------------------------------------------
                if (b[i-1] in exclmrules.conj) and (b[i+1] in exclmrules.pronoun or b[i+1] in exclmrules.snoun)  :     
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and b[i+1] in exclmrules.standalonesplit:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and b[i-2] in exclmrules.onoun:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and c[-2]=="!":
                    hint="Correct Answer,Click the appropriate sidepane and read the manuals"
                    correctlst.append(hint)    
                #---------------------type9ohmyg-------------
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det and c[-2]==".":
                    hint="Correct Answer,Put a exclamation after standslone interjections and end the senten e with a fullstop "
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det and c[-2] in [" ",",","?"]:
                    hint="InCorrect Answer,Put a exclamation after standslone interjections and end the sentence with a fullstop "
                    mandlst.append(hint)
                    
                #----------------------simpleintjn----
                if (b[i-1] in ['Stop','Wait','Lost','goodness','You'] and c[i]=="!"):    
                    hint="Correct Answer:Can put an exclmation after the standalone interjections "
                    correctlst.append(hint)
                #-----------------------type9excmn---
                if (b[i-1] in exclmrules.title) and (b[i+1] in exclmrules.snoun):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)                   
                    
                if (b[i-1] in exclmrules.snoun) and (b[i+1] in exclmrules.article):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.cnoun) and (b[i+1] in exclmrules.vbz):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)   
        #----------------------------------------
                if (b[i-1] in exclmrules.vbz) and (c[-2]=="!"):    
                    hint="Correct Answer:Always end a exclamatory sentence with an exclamation"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.verb) and (c[-2]=="!") and c[0] in exclmrules.qtag:    
                    hint="Correct Answer:Always end a exclamatory sentence with an exclamation"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and (c[-2]=="!") and c[0] in exclmrules.qtag:     
                    hint="Correct Answer:Always end a exclamatory sentence with an exclamation"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and b[i+1] in exclmrules.qtag and c[-2]==".":    
                    hint="Correct Answer:put an exclamation after an interjection, if the sentence has to ended with a period"
                    correctlst.append(hint)
               
                if (b[i-1] in exclmrules.exclm) and b[i+1] in exclmrules.qtag and c[-2]=="!":    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
        #--------------------------------type9---------------------------------------------------------------------------------
                    
                    
        #-----------------------------------------<m> with comma---------------------------------
        for i in range(0,len(b)):
            
            if (b[i]=="<m>" and c[i]==","):
               #------------------type9endsurprise----------------------------------------------------------------------------
                if (b[i-1] in exclmrules.conj) and (b[i+1] in exclmrules.pronoun or b[i+1] in exclmrules.snoun):     
                    hint="Correct Answer:If a sentence starts with a Conjunction like So/Eventhough/But which id followed by a clause, then put seperate the conjunction and the clause with a comma"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and b[i+1] in exclmrules.standalonesplit:
                    hint="Correct Answer:Put a comma to seperate the clause and the interjection"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and b[i-2] in exclmrules.onoun:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and c[-2]==",":
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)      
                #--------------type9ohmyg------------------------------------------------------------------------------
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det and c[-2] in ["."]:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det and c[-2] in [" ",",","!"]:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)

                        
                #-------------simpleintjn------------------------------------------------------------------------------
                if (b[i-1] in ['Stop','Wait','Lost','goodness','You']):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                    
                #-------------type9exclmn--------------------------------------------------------------------------------
                if (b[i-1] in exclmrules.title) and (b[i+1] in exclmrules.snoun):    
                    hint="InCorrect Answer:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                    mandlst.append(hint)
                    
                    
                if (b[i-1] in exclmrules.snoun) and (b[i+1] in exclmrules.article):    
                    hint="Correct Answer:A comma should be used when a relative clause follows the main subject."
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.cnoun) and (b[i+1] in exclmrules.vbz):    
                    hint="Correct Answer:A comma should be used when a relative clause follows the main subject."
                    correctlst.append(hint)    
                #----------------------------------------
           
                if (b[i-1] in exclmrules.verb) and (c[-2]==",") and c[0] in exclmrules.qtag:     
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and (c[-2]==",") and c[0] in exclmrules.qtag:     
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and (b[i+1] in exclmrules.qtag):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.vbz) and (c[-2]==","):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and (c[-2]==",") and c[1]=="!":    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and b[i+1] in exclmrules.qtag and c[-2]=="!":    
                    hint="Correct Answer,Put a Comma after an interjection, if the sentence has to ended with a exclamation"
                    correctlst.append(hint)     
        #-----------------------------------------<m> with fullstop---------------------------------
        for i in range(0,len(b)):
           
            if (b[i]=="<m>" and c[i]=="."):
                #------------------type9endsurprise----------------------------------------------------------------------------
                if (b[i-1] in exclmrules.conj) and (b[i+1] in exclmrules.pronoun or b[i+1] in exclmrules.snoun):     
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and b[i+1] in exclmrules.standalonesplit:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and b[i-2] in exclmrules.onoun:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and c[-2]==".":
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)     
                #-------------------------------------------type9ohmyg-------------
              
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det and c[-2] in ["."]:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det and c[-2] in [" ",",","!"]:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)    
                #---simpleintjn----
                if (b[i-1] in ['Stop','Wait','Lost','goodness','You']):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                #---type9exclmn---
                if (b[i-1] in exclmrules.title) and (b[i+1] in exclmrules.snoun):    
                    hint="Correct Answer,Title Abbreviation had be done by a FULLSTOP"
                    correctlst.append(hint)
                    
                    
                if (b[i-1] in exclmrules.snoun) and (b[i+1] in exclmrules.article):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.cnoun) and (b[i+1] in exclmrules.vbz):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)    
                #----------------------------------------

                if (b[i-1] in exclmrules.vbz) and (c[-2]=="."):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and (c[-2]==".") and c[0] in exclmrules.qtag:     
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and (b[i+1] in exclmrules.qtag):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)  
                if (b[i-1] in exclmrules.verb) and (c[-2]==".") and c[0] in exclmrules.qtag:     
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and (c[-2]==".") and c[0] in exclmrules.exclm and c[1]=="!":    
                    hint="Correct Answer:Sentence has to ended with a period if a exclamation is put after the interjection"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and b[i+1] in exclmrules.qtag and c[-2]=="!":    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)    
         #-----------------------------------------<m> with no punctuation---------------------------------
        for i in range(0,len(b)):
           
            if (b[i]=="<m>" and c[i]==" "):
                #------------------type9endsurprise----------------------------------------------------------------------------
                if (b[i-1] in exclmrules.conj) and (b[i+1] in exclmrules.pronoun or b[i+1] in exclmrules.snoun):     
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and b[i+1] in exclmrules.standalonesplit:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and b[i-2] in exclmrules.onoun:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and c[-2]==" ":
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint) 
                    
                #type9ohmyg-------------
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det and c[-2] in [" "]:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det and c[-2] in [".",",","!"]:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint) 
                 #---simpleintjn----
                if (b[i-1] in ['Stop','Wait','Lost','goodness','You']):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                #---type9excmn---
                if (b[i-1] in exclmrules.title) and (b[i+1] in exclmrules.snoun):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                                        
                if (b[i-1] in exclmrules.snoun) and (b[i+1] in exclmrules.article):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.cnoun) and (b[i+1] in exclmrules.vbz):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)   
                #----------------------------------------
                if (b[i-1] in exclmrules.vbz) and (c[-2]==" "):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and (c[-2]==" ") and c[0] in exclmrules.qtag:     
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and (b[i+1] in exclmrules.qtag):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)   
                if (b[i-1] in exclmrules.verb) and (c[-2]==" ") and c[0] in exclmrules.qtag:     
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and (c[-2]==".") and c[1]=="!":    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and b[i+1] in exclmrules.qtag and c[-2]=="!":    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)  
           #-----------------------------------------<w> with fullstop ------------------------------------------------------------------------------------
        for i in range(0,len(b)):
           
            if (b[i]=="<w>" and c[i]=="."):
                hint="Fullstop not needed.Click the appropriate sidepane and read the manuals""
                hintlst.append(hint)
            if (b[i]=="<w>" and c[i]==","):
                hint="Comma not needed.Click the appropriate sidepane and read the manuals"
                hintlst.append(hint)   
            if (b[i]=="<w>" and c[i]=="!"):
                hint="Exclamation not needed.Click the appropriate sidepane and read the manuals"
                hintlst.append(hint)   
  

        return(hintlst,mandlst,correctlst,mandatory) 
    def exclmtwo(b,c,correct,category,level,username,userid,eid,submittedtext):
##    def exclmtwo(self):  
        hintlst=[]
        correctlst=[]
        mandlst=[]
##        b=['What','<w>','a','<w>','red','<w>','cage','<w>','it','<w>','is','<m>']
##        c=['What','!','a',',','red',',','cage',',','it',',','is','!']
##        b=['How','<w>','deliciously','<w>','Mary','<w>','cooked','<m>']
##        c=['How',',','deliciously',',','Mary',',','cooked','!']
##        b=['Ah','<m>','What','<w>','a','<w>','well-defined','<w>','house','<m>']
##        c=['Ah','!','What',',','a',',','well-defined',',','house','.']
##        b=['So','<m>','John','<w>',"could'nt",'<w>','answer','<w>','the','<w>','question','<w>','eh','<m>']
##        c=['So',',','John',',',"could'nt",',','answer',',','the',',','question',',','eh','!']
##        b=['Yikes','<m>','Dr','<m>','Alice','<m>','a','<w>','clever','<w>','lady','<m>','has','<w>','won','<w>','the','<w>','match','<m>']
##        c=['Yikes','!','Dr','.','Alice',',','a',',','clever',',','lady',',','has',' ','won',' ','the','','match','.']
##        b=['"Stop','<m>','"','<w>']
##        c=['"Stop','!','"','<w>']
##        b=['<w>','Get','<w>','Lost','<m>','"','<w>']
##        c=[',','Get',',','Lost','!','"',',']
##        b=['Oh','<w>','my','<w>','goodness','<m>','Those','<w>','are','<w>','her','<w>','expensive','<w>','keys','<m>']
##        c=['Oh',',','my',',','goodness','!','Those',',','are',',','her',',','expensive',',','keys','.']
##        print(c)
##        b=['Ah', '<c>', 'What', '<w>', 'a', '<w>', 'precise', '<w>', 'poem', '<c>']
##        c=['Ah', ',', 'What', ' ', 'a', ' ', 'precise', ' ', 'poem', '.']
##        b=['Yippee', '<c>', 'Prof', '<m>', 'John', '<m>', 'a', '<w>', 'generous', '<w>', 'orator', '<w>', 'has', '<w>', 'won', '<w>', 'the', '<w>', 'race', '<c>']
##        c=['Yippee', '!', 'Prof', '.', 'John', ',', 'a', ' ', 'generous', ' ', 'orator', ',', 'has', ' ', 'won', ' ', 'the', ' ', 'race', '.']
        b.append(" ")
        c.append(" ")
        ct=0
        for i in b:
            if i=="<m>":
                ct=ct+1
        mandatory=ct
        print(ct)
        print(b)
        print(c)



          #------------------------------------------<c> with exclm--------------------------------------
        for i in range(0,len(c)):
           if (b[i]=="<c>" and c[1]==" " and c[-2] in [".",",","!"]) :
                   
                hint="InCorrect Answer:put an exclamation after an interjection, if the sentence has to ended with a period/if u put a comma after interjection,add an exclamtion at the end"
                mandlst.append(hint)
           if (b[i]=="<c>" and c[-2]==" " and c[1] in [".",",","!"]) :
               
                hint="InCorrect Answer:put an exclamation after an interjection, if the sentence has to ended with a period/if u put a comma after interjection,add an exclamtion at the end"
                mandlst.append(hint)    
               
           if (b[i]=="<c>" and c[1]=="!" and c[-2]==".") :
                hint="Correct Answer:If you put an exclamation after an interjection, the sentence has to ended with a period"
                correctlst.append(hint)
           if (b[i]=="<c>" and c[1]=="!" and c[-2]=="!") :
                hint="Incorrect Answer:If you put an exclamation after an interjection, the sentence has to ended with a period"
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]=="!" and c[-2]==",") :
                hint="Incorrect Answer:If you put an exclamation after an interjection, the sentence has to ended with a period"
                mandlst.append(hint)     
           if (b[i]=="<c>" and c[1]=="," and c[-2]=="!") :
                hint="Correct Answer:If you put an comma after an interjection, the sentence has to ended with a exclamation"
                correctlst.append(hint)
           if (b[i]=="<c>" and c[1]=="," and c[-2]==".") :
                hint="InCorrect Answer:If you put an comma after an interjection, the sentence has to ended with a exclamation"
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]=="," and c[-2]==",") :
                hint="InCorrect Answer:If you put an comma after an interjection, the sentence has to ended with a exclamation"
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]=="." and c[-2]==".") :
                hint="InCorrect Answer:If you put an comma after an interjection, the sentence has to ended with a exclamation"
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]=="." and c[-2]==",") :
                hint="InCorrect Answer:If you put an comma after an interjection, the sentence has to ended with a exclamation"
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]=="." and c[-2]=="!") :
                hint="InCorrect Answer:If you put an comma after an interjection, the sentence has to ended with a exclamation"
                mandlst.append(hint)     
           if (b[i]=="<c>" and c[1]==" " and c[-2]=="!") :
                hint="InCorrect Answer:If you put an comma after an interjection, the sentence has to ended with a exclamation"
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]==" " and c[-2]==".") :
                hint="Incorrect Answer:If you put an exclamation after an interjection, the sentence has to ended with a period"
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]==" " and c[-2] in [" ",","]) :
                hint="Incorrect Answer:If you put an exclamation after an interjection, the sentence has to ended with a period"
                mandlst.append(hint)
        #-----------------------------------------<m> with exclamation---------------------------------
        for i in range(0,len(b)):
            
           
            if (b[i]=="<m>" and c[i]=="!"):
                #------------------type9endsurprise----------------------------------------------------------------------------
                if (b[i-1] in exclmrules.conj) and (b[i+1] in exclmrules.pronoun or b[i+1] in exclmrules.snoun)  :     
                    hint="Read the manual again, HINT:If a sentence starts with a Conjunction like So/Eventhough/But which id followed by a clause, then put seperate the conjunction and the clause with a comma"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and b[i+1] in exclmrules.standalonesplit:
                    hint="Read the manual again, HINT:Put a comma to seperate the clause and the interjection"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and b[i-2] in exclmrules.onoun:
                    hint="Read the manual again, HINT:if an interjection is intended to show the emotion of surprise,we can put a questionamrk after the interjection"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and c[-2]=="!":
                    hint="Correct Ans:HINT:if an interjection is used,put an exclamation"
                    correctlst.append(hint)     
                #type9ohmyg-------------
             
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det and c[-2] in ["."]:
                    hint="Correct Answer,Standalone interjections end with an exclamation and the sentnce end with a fullstop"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det and c[-2] in [".",","," "]:
                    hint="InCorrect Answer,Standalone interjections end with an exclamation and the sentnce end with a fullstop"
                    mandlst.append(hint) 
                    
                #----------------------simpleintjn----
                if (b[i-1] in ['Stop','Wait','Lost','goodness','You']):    
                    hint="Correct Answer:Can put an exclmation after the standalone interjections "
                    correctlst.append(hint)
                #-----------------------type9excmn---
                if (b[i-1] in exclmrules.title) and (b[i+1] in exclmrules.snoun):    
                    hint="Read the manual again,HINT:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                    mandlst.append(hint)                    
                    
                if (b[i-1] in exclmrules.snoun) and (b[i+1] in exclmrules.article):    
                    hint="Read the manual again,HINT:A comma should be used when a relative clause follows the main subject."
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.cnoun) and (b[i+1] in exclmrules.vbz):    
                    hint="Read the manual again,HINT:A comma should be used when a relative clause follows the main subject."
                    mandlst.append(hint)    
        #----------------------------------------
                if (b[i-1] in exclmrules.vbz) and (c[-2]=="!"):    
                    hint="Correct Answer:Always end a exclamatory sentence with an exclamation"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.verb) and (c[-2]=="!") and c[0] in exclmrules.qtag:    
                    hint="Correct Answer:Always end a exclamatory sentence with an exclamation"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and (c[-2]=="!") and c[0] in exclmrules.qtag:     
                    hint="Correct Answer:Always end a exclamatory sentence with an exclamation"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and b[i+1] in exclmrules.qtag and c[-2]==".":    
                    hint="Correct Answer:put an exclamation after an interjection, if the sentence has to ended with a period"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and (c[-2]=="!") and c[1]=="!":    
                    hint="Read the manual again,Hint:Sentence has to ended with a period if a exclamation is put after the interjection"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and b[i+1] in exclmrules.qtag and c[-2]=="!":    
                    hint="Read the manual again:Hint:Put a Comma after an interjection, if the sentence has to ended with a exclamation"
                    mandlst.append(hint)
        #--------------------------------type9---------------------------------------------------------------------------------
                    
                    
        #-----------------------------------------<m> with comma---------------------------------
        for i in range(0,len(b)):
            
            if (b[i]=="<m>" and c[i]==","):
             
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det and c[-2] in [".",","," ","!"]:
                    hint="InCorrect Answer,Standalone interjections end with an exclamation and the sentnce end with a fullstop"
                    mandlst.append(hint) 
               #------------------type9endsurprise----------------------------------------------------------------------------
                if (b[i-1] in exclmrules.conj) and (b[i+1] in exclmrules.pronoun or b[i+1] in exclmrules.snoun):     
                    hint="Correct Answer:If a sentence starts with a Conjunction like So/Eventhough/But which id followed by a clause, then put seperate the conjunction and the clause with a comma"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and b[i+1] in exclmrules.standalonesplit:
                    hint="Correct Answer:Put a comma to seperate the clause and the interjection"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and b[i-2] in exclmrules.onoun:
                    hint="Read the manual again, HINT:if an interjection is intended to show the emotion of surprise,we can put a questionamrk after the interjection"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and c[-2]==",":
                    hint="Read the manual again, HINT:if an interjection is used,put an exclamation"
                    mandlst.append(hint)         
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det:
                    hint="Read the manual again,Standalone interjections need to be ended with exclamtions"
                    mandlst.append(hint)
                #-------------simpleintjn------------------------------------------------------------------------------
                if (b[i-1] in ['Stop','Wait','Lost','goodness','You']):    
                    hint="Read the manual again:Can put an exclmation after the commands like stop/wait within quotes "
                    mandlst.append(hint)
                #-------------type9excmn--------------------------------------------------------------------------------
                if (b[i-1] in exclmrules.title) and (b[i+1] in exclmrules.snoun):    
                    hint="INCorrect Answer:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.cnoun) and (b[i+1] in exclmrules.vbz):    
                    hint="Correct Answer:A comma should be used when a relative clause follows the main subject."
                    correctlst.append(hint)      
                    
                if (b[i-1] in exclmrules.snoun) and (b[i+1] in exclmrules.article):    
                    hint="Correct Answer:A comma should be used when a relative clause follows the main subject."
                    correctlst.append(hint)
                  
                #----------------------------------------
           
                if (b[i-1] in exclmrules.verb) and (c[-2]==",") and c[0] in exclmrules.qtag:     
                    hint="Read the manual again, HINT:Always end a exclamatory sentence with an exclamation"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and (c[-2]==",") and c[0] in exclmrules.qtag:     
                    hint="Read the manual again, HINT:Always end a exclamatory sentence with an exclamation"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and (b[i+1] in exclmrules.qtag):    
                    hint="Read the manual again, HINT:put an exclamation after an interjection, if the sentence has to ended with a period"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.vbz) and (c[-2]==","):    
                    hint="Read the manual again, HINT:Always end a exclamatory sentence with an exclamation"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and (c[-2]==",") and c[1]=="!":    
                    hint="Read the manual again,Hint:Sentence has to ended with a period if a exclamatioon is put after the interjection"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and b[i+1] in exclmrules.qtag and c[-2]=="!":    
                    hint="Correct Answer,Put a Comma after an interjection, if the sentence has to ended with a exclamation"
                    correctlst.append(hint)     
        #-----------------------------------------<m> with fullstop---------------------------------
        for i in range(0,len(b)):
           
            if (b[i]=="<m>" and c[i]=="."):
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det and c[-2] in [".",","," ","!"]:
                    hint="InCorrect Answer,Standalone interjections end with an exclamation and the sentnce end with a fullstop"
                    mandlst.append(hint) 
                #------------------type9endsurprise----------------------------------------------------------------------------
                if (b[i-1] in exclmrules.conj) and (b[i+1] in exclmrules.pronoun or b[i+1] in exclmrules.snoun):     
                    hint="Read the manual again, HINT:If a sentence starts with a Conjunction like So/Eventhough/But which id followed by a clause, then put seperate the conjunction and the clause with a comma"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and b[i+1] in exclmrules.standalonesplit:
                    hint="Read the manual again, HINT:Put a comma to seperate the clause and the interjection"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and b[i-2] in exclmrules.onoun:
                    hint="Read the manual again, HINT:if an interjection is intended to show the emotion of surprise,we can put a questionamrk after the interjection"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and c[-2]==".":
                    hint="Read the manual again, HINT:if an interjection is used,pt an exclamation"
                    mandlst.append(hint)         
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det:
                    hint="Read the manual again,Standalone interjections need to be ended with exclamtions"
                    mandlst.append(hint)
                #---simpleintjn----
                if (b[i-1] in ['Stop','Wait','Lost','goodness','You']):    
                    hint="Read the manual again:Can put an exclmation after the commands like stop/wait within quotes "
                    mandlst.append(hint)
                #---type9exclmn---
                if (b[i-1] in exclmrules.title) and (b[i+1] in exclmrules.snoun):    
                    hint="Correct Answer.Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                    correctlst.append(hint)
                    
                    
                if (b[i-1] in exclmrules.snoun) and (b[i+1] in exclmrules.article):    
                    hint="Read the manual again,HINT:A comma should be used when a relative clause follows the main subject."
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.cnoun) and (b[i+1] in exclmrules.vbz):    
                    hint="Read the manual again,HINT:A comma should be used when a relative clause follows the main subject."
                    mandlst.append(hint)    
                #----------------------------------------

                if (b[i-1] in exclmrules.vbz) and (c[-2]=="."):    
                    hint="Read the manual again, HINT:Always end a exclamatory sentence with an exclamation"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and (c[-2]==".") and c[0] in exclmrules.qtag:     
                    hint="Read the manual again, HINT:Always end a exclamatory sentence with an exclamation"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and (b[i+1] in exclmrules.qtag):    
                    hint="Read the manual again, HINT:put an exclamation after an interjection, if the sentence has to ended with a period"
                    mandlst.append(hint)     
                if (b[i-1] in exclmrules.verb) and (c[-2]==".") and c[0] in exclmrules.qtag:     
                    hint="Read the manual again, HINT:Always end a exclamatory sentence with an exclamation"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and (c[-2]==".") and c[0] in exclmrules.exclm and c[1]=="!":    
                    hint="Correct Answer:Sentence has to ended with a period if a exclamation is put after the interjection"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and b[i+1] in exclmrules.qtag and c[-2]=="!":    
                    hint="Read the manual again:Hint:Put a Comma after an interjection, if the sentence has to ended with a exclamation"
                    mandlst.append(hint)     
         #-----------------------------------------<m> with no punctuation---------------------------------
        for i in range(0,len(b)):
           
            if (b[i]=="<m>" and c[i]==" "):
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det and c[-2] in [".",","," ","!"]:
                    hint="InCorrect Answer,Standalone interjections end with an exclamation and the sentnce end with a fullstop"
                    mandlst.append(hint) 
                #------------------type9endsurprise----------------------------------------------------------------------------
                if (b[i-1] in exclmrules.conj) and (b[i+1] in exclmrules.pronoun or b[i+1] in exclmrules.snoun):     
                    hint="Read the manual again, HINT:If a sentence starts with a Conjunction like So/Eventhough/But which id followed by a clause, then seperate the conjunction and the clause with a comma"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and b[i+1] in exclmrules.standalonesplit:
                    hint="Read the manual again, HINT:Put a comma to seperate the clause and the interjection"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and b[i-2] in exclmrules.onoun:
                    hint="Read the manual again, HINT:if an interjection is intended to show the emotion of surprise,we can put a questionamrk after the interjection"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and c[-2]==" ":
                    hint="Read the manual again, HINT:if an interjection is used,pt an exclamation"
                    mandlst.append(hint)         
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det:
                    hint="Read the manual again,Standalone interjections need to be ended with exclamtions"
                    mandlst.append(hint)
                 #---simpleintjn----
                if (b[i-1] in ['Stop','Wait','Lost','goodness','You']):    
                    hint="Read the manual again:Can put an exclmation after the commands like stop/wait within quotes "
                    mandlst.append(hint)
                #---type9excmn---
                if (b[i-1] in exclmrules.title) and (b[i+1] in exclmrules.snoun):    
                    hint="Read the manual again,HINT:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                    mandlst.append(hint)
                                        
                if (b[i-1] in exclmrules.snoun) and (b[i+1] in exclmrules.article):    
                    hint="Read the manual again,HINT:A comma should be used when a relative clause follows the main subject."
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.cnoun) and (b[i+1] in exclmrules.vbz):    
                    hint="Read the manual again,HINT:A comma should be used when a relative clause follows the main subject."
                    mandlst.append(hint)    
                #----------------------------------------
                if (b[i-1] in exclmrules.vbz) and (c[-2]==" "):    
                    hint="Read the manual again, HINT:Always end a exclamatory sentence with an exclamation"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and (c[-2]==" ") and c[0] in exclmrules.qtag:     
                    hint="Read the manual again, HINT:Always end a exclamatory sentence with an exclamation"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and (b[i+1] in exclmrules.qtag):    
                    hint="Read the manual again, HINT:put an exclamation after an interjection, if the sentence has to ended with a period"
                    mandlst.append(hint)     
                if (b[i-1] in exclmrules.verb) and (c[-2]==" ") and c[0] in exclmrules.qtag:     
                    hint="Read the manual again, HINT:Always end a exclamatory sentence with an exclamation"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and (c[-2]==".") and c[1]=="!":    
                    hint="Read the manual again,Hint:Sentence has to ended with a period if a exclamatioon is put after the interjection"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and b[i+1] in exclmrules.qtag and c[-2]=="!":    
                    hint="Read the manual again:Hint:Put a Comma after an interjection, if the sentence has to ended with a exclamation"
                    mandlst.append(hint)     
        #-----------------------------------------<w> with exclamation--------------------------------
        for i in range(0,len(b)):
           
            if (b[i]=="<w>" and c[i]=="!"):
                #---------------------------------type9ohmyg-----------------
                if (b[i-1] in exclmrules.standalonesplit and b[i+1] in exclmrules.standalonesplit):
                    hint="Read the manual again:HINT: No need of any punctuation between the standalone interjections"                      
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.determiner and b[i+1] in exclmrules.vbz):
                    hint="Read the manual again:HINT: No need of any punctuation between a det/pronoun and [is/are]"                      
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.vbz and b[i+1] in exclmrules.pronoun):
                    hint="Read the manual again:HINT: No need of any punctuation between is/are and a pronoun"                      
                    hintlst.append(hint)
                if b[i-1] in exclmrules.adj and b[i+1] in exclmrules.snoun:
                  hint="Read The manual again, HINT:No need to seperate an adjective and a noun with an exclamtion "
                  hintlst.append(hint)    

                #--------------------------------------simpleintjn----
                if (b[i-1] == '"' or b[i-1]== 'Get'):    
                    hint="Read the manual again:No need for any punctuation after/in between/ the quotes(after the direct speech especially when it is a command/request)"
                    hintlst.append(hint)
                #-------------------------------------type9exclm---------------------------------
                if b[i-1] in exclmrules.adj and b[i+1] in exclmrules.cnoun:
                  hint="Read The manual again, HINT:No need to seperate an adjective and a commoun noun with exclamtion"
                  hintlst.append(hint)
                if b[i-1] in exclmrules.vbz and b[i+1] in exclmrules.verb:
                    hint="Read The manual again, HINT:Caution! Helping verb is supporting the verb.No need to seperate with a exclamtion"
                    hintlst.append(hint)
                

                if b[i-1] in exclmrules.article and b[i+1] in exclmrules.adj:
                    hint="Read The manual again, HINT:No need to seperate an article and a adjective with exclamtion"
                    hintlst.append(hint)
                if b[i-1] in exclmrules.verb and b[i+1] in (exclmrules.pronoun or exclmrules.det):
                    hint="Incorrect Answer, HINT: No need of an exclamtion after a verb"
                    hintlst.append(hint)
                if b[i-1] in (exclmrules.pronoun or exclmrules.det) and b[i+1] in exclmrules.onoun:
                    hint="Incorrect Answer, HINT: No need of an exclamtion before a noun, when it is not preceeded by any clause"
                    hintlst.append(hint)    

                 #----------------------------------------------
                if (b[i-1] in exclmrules.qtag) and (b[i+1] in exclmrules.article):    
                    hint="Read the manual again, HINT:No need of a punctuation in between a Wh/how-question and an article"
                    hintlst.append(hint)
                   
                if (b[i-1] in exclmrules.article) and (b[i+1] in exclmrules.adj):    
                    hint="Read the manual again, HINT:No need of a punctuation in between an article and an adjective"
                    hintlst.append(hint)

                if (b[i-1] in exclmrules.adj) and (b[i+1] in exclmrules.onoun):    
                    hint="Read the manual again, HINT:No need of a punctuation in between an adjective and a noun"
                    hintlst.append(hint)

                if (b[i-1] in exclmrules.onoun) and (b[i+1] in exclmrules.pronoun):    
                    hint="Read the manual again, HINT:No need of a punctaution in between a noun and a pronoun"
                    hintlst.append(hint)

                if (b[i-1] in exclmrules.pronoun) and (b[i+1] in exclmrules.vbz):    
                    hint="Read the manual again, HINT:No need of a punctuation in between a pronoun and [is/was]"
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.qtag) and (b[i+1] in exclmrules.adverb):    
                    hint="Read the manual again, HINT:No need of a punctuation in between a Wh/how-question and an adverb"
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.adverb) and (b[i+1] in exclmrules.snoun):    
                    hint="Read the manual again, HINT:No need of a punctuation after an  adverb when followed by a person's name"
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.snoun) and (b[i+1] in exclmrules.verb):    
                    hint="Read the manual again, HINT:No need of a punctuation after a noun when followed by a verb"
                    hintlst.append(hint)
                    
                
                   
        #-----------------------------------------<w> with comma------------------------------------------------------------------------------------------
        for i in range(0,len(b)):
           
            if (b[i]=="<w>" and c[i]==","):
                #---------------------------------type9ohmyg----------------------------------------------------------------------------------------------
                if (b[i-1] in exclmrules.standalonesplit and b[i+1] in exclmrules.standalonesplit):
                    hint="Read the manual again:HINT: No need of any punctuation between the standalone interjections"                      
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.determiner and b[i+1] in exclmrules.vbz):
                    hint="Read the manual again:HINT: No need of any punctuation between a det/pronoun and [is/are]"                      
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.vbz and b[i+1] in exclmrules.pronoun):
                    hint="Read the manual again:HINT: No need of any punctuation between is/are and a pronoun"                      
                    hintlst.append(hint)
                  
                #-------------------------------------simpleintjn----------------------------------------------------------------------------------------------------------------------------
                if (b[i-1] == '"' or b[i-1]== 'Get'):    
                    hint="Read the manual again:No need for any punctuation after/in between the quotes(after the direct speech especially when it is a command/request)"
                    hintlst.append(hint)
                #--------------------------------------type9exclm----------------------------------------------------------------------------------------------------------------------
                if b[i-1] in exclmrules.adj and b[i+1] in exclmrules.cnoun:
                  hint="Read The manual again, HINT:No need to seperate an adjective and a commoun noun with comma"
                  hintlst.append(hint)
                if b[i-1] in exclmrules.vbz and b[i+1] in exclmrules.verb:
                    hint="Read The manual again, HINT:Caution! Helping verb is supporting the verb.No need to seperate with a comma"
                    hintlst.append(hint)

                if b[i-1] in exclmrules.article and b[i+1] in exclmrules.adj:
                    hint="Read The manual again, HINT:No need to seperate an article and a adjective with comma"
                    hintlst.append(hint)
                if b[i-1] in exclmrules.verb and b[i+1] in (exclmrules.pronoun or exclmrules.det):
                    hint="Incorrect Answer, HINT: No need of a comma after a verb"
                    hintlst.append(hint)
                if b[i-1] in (exclmrules.pronoun or exclmrules.det) and b[i+1] in exclmrules.onoun:
                    hint="Incorrect Answer, HINT: No need of a comma before a noun, when it is not preceeded by any clause"
                    hintlst.append(hint)
                
                if (b[i-1] in exclmrules.qtag) and (b[i+1] in exclmrules.article):    
                    hint="Read the manual again, HINT:No need of a punctuation in between a Wh/how-question and an article"
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.article) and (b[i+1] in exclmrules.adj):    
                    hint="Read the manual again, HINT:No need of a punctuation in between an article and an adjective"
                    hintlst.append(hint)

                if (b[i-1] in exclmrules.adj) and (b[i+1] in exclmrules.onoun):    
                    hint="Read the manual again, HINT:No need of a punctuation in between an adjective and a noun"
                    mandlst.append(hint)

                if (b[i-1] in exclmrules.onoun) and (b[i+1] in exclmrules.pronoun):    
                    hint="Read the manual again, HINT:No need of a punctuation in between a noun and a pronoun"
                    hintlst.append(hint)

                if (b[i-1] in exclmrules.pronoun) and (b[i+1] in exclmrules.vbz):    
                    hint="Read the manual again, HINT:No need of a punctuation in between a pronoun and [is/was]"
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.qtag) and (b[i+1] in exclmrules.adverb):    
                    hint="Read the manual again, HINT:No need of a punctuation in between a Wh/how-question and an adverb"
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.adverb) and (b[i+1] in exclmrules.snoun):    
                    hint="Read the manual again, HINT:No need of a punctuation after an  adverb when followed by a person's name"
                    hintlst.append(hint)     
                if (b[i-1] in exclmrules.snoun) and (b[i+1] in exclmrules.verb):    
                    hint="Read the manual again, HINT:No need of a punctuation after a noun when followed by a verb"
                    hintlst.append(hint)
                if b[i-1] in exclmrules.adj and b[i+1] in exclmrules.snoun:
                  hint="Read The manual again, HINT:No need to seperate an adjective and a noun with comma"
                  hintlst.append(hint)    

        #-----------------------------------------<w> with fullstop ------------------------------------------------------------------------------------
        for i in range(0,len(b)):
           
            if (b[i]=="<w>" and c[i]=="."):
            #--------------------------------------type9endsurprise.py-----------------------------------------------------------------------------------
                
                #---------------------------------type9ohmyg---------------------------------------------------------------------------------------------
                if (b[i-1] in exclmrules.standalonesplit and b[i+1] in exclmrules.standalonesplit):
                    hint="Read the manual again:HINT: No need of any punctuation between the standalone interjections"                      
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.determiner and b[i+1] in exclmrules.vbz):
                    hint="Read the manual again:HINT: No need of any punctuation between a det/pronoun and [is/are]"                      
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.vbz and b[i+1] in exclmrules.pronoun):
                    hint="Read the manual again:HINT: No need of any punctuation between is/are and a pronoun"                      
                    hintlst.append(hint)
                if b[i-1] in exclmrules.adj and b[i+1] in exclmrules.snoun:
                  hint="Read The manual again, HINT:No need to seperate an adjective and a noun with a fullstop"
                  hintlst.append(hint)    

                
                #-------------------------------------------simpleintjn----------------------------------------------------------------------------------------------------------------------------
                    
                if (b[i-1] == '"' or b[i-1]== 'Get'):    
                    hint="Read the manual again:No need for any punctuation after/in between the quotes(after the direct speech) especially when it is a command/request)"
                    hintlst.append(hint)
                    
                #-------------------------------------------type9exclm----------------------------------------------------------------------------------------------------------------------
                if b[i-1] in exclmrules.adj and b[i+1] in exclmrules.cnoun:
                  hint="Read The manual again, HINT:No need to seperate an adjective and a commoun noun with fullstop"
                  hintlst.append(hint)
                if b[i-1] in exclmrules.vbz and b[i+1] in exclmrules.verb:
                    hint="Read The manual again, HINT:Caution! Helping verb is supporting the verb.No need to seperate with a fullstop"
                    hintlst.append(hint)
                

                if b[i-1] in exclmrules.article and b[i+1] in exclmrules.adj:
                    hint="Read The manual again, HINT:No need to seperate an article and a adjective with fullstop"
                    hintlst.append(hint)
                if b[i-1] in exclmrules.verb and b[i+1] in (exclmrules.pronoun or exclmrules.det):
                    hint="Incorrect Answer, HINT: No need of a fullstop after a verb"
                    hintlst.append(hint)
                if b[i-1] in (exclmrules.pronoun or exclmrules.det) and b[i+1] in exclmrules.onoun:
                    hint="Incorrect Answer, HINT: No need of a punctuation before a noun, when it is not preceeded by any clause"
                    hintlst.append(hint)
                #------------------------------------------------------------------------------------------------------------------------------------------- 

                if (b[i-1] in exclmrules.qtag) and (b[i+1] in exclmrules.article):    
                    hint="Read the manual again, HINT:No need of a punctuation in between a Wh/how-question and an article"
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.article) and (b[i+1] in exclmrules.adj):    
                    hint="Read the manual again, HINT:No need of a punctuation in between an article and an adjective"
                    hintlst.append(hint)

                if (b[i-1] in exclmrules.adj) and (b[i+1] in exclmrules.onoun):    
                    hint="Read the manual again, HINT:No need of a punctuation in between an adjective and a noun"
                    
                    hintlst.append(hint)

                if (b[i-1] in exclmrules.onoun) and (b[i+1] in exclmrules.pronoun):    
                    hint="Read the manual again, HINT:No need of a punctuation in between a noun and a pronoun"
                    hintlst.append(hint)

                if (b[i-1] in exclmrules.pronoun) and (b[i+1] in exclmrules.vbz):    
                    hint="Read the manual again, HINT:No need of a punctuation in between a pronoun and [is/was]"
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.qtag) and (b[i+1] in exclmrules.adverb):    
                    hint="Read the manual again, HINT:No need of a punctuation in between a Wh/how-question and an adverb"
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.adverb) and (b[i+1] in exclmrules.snoun):    
                    hint="Read the manual again, HINT:No need of a punctuation after an  adverb when followed by a person's name"
                    hintlst.append(hint)     
                if (b[i-1] in exclmrules.snoun) and (b[i+1] in exclmrules.verb):    
                    hint="Read the manual again, HINT:No need of a punctuation after a noun when followed by a verb"
                    hintlst.append(hint)     
  

        return(hintlst,mandlst,correctlst,mandatory) 
    def exclmthree(b,c,correct,category,level,username,userid,eid,submittedtext):
##    def exclmthree(self):
        hintlst=[]
        correctlst=[]
        mandlst=[]
##        b=['What','<w>','a','<w>','red','<w>','cage','<w>','it','<w>','is','<m>']
##        c=['What','!','a',',','red',',','cage',',','it',',','is','!']
##        b=['How','<w>','deliciously','<w>','Mary','<w>','cooked','<m>']
##        c=['How',',','deliciously',',','Mary',',','cooked','!']
##        b=['Ah','<m>','What','<w>','a','<w>','well-defined','<w>','house','<m>']
##        c=['Ah','!','What',',','a',',','well-defined',',','house','.']
##        b=['So','<m>','John','<w>',"could'nt",'<w>','answer','<w>','the','<w>','question','<w>','eh','<m>']
##        c=['So',',','John',',',"could'nt",',','answer',',','the',',','question',',','eh','!']
##        b=['Yikes','<m>','Dr','<m>','Alice','<m>','a','<w>','clever','<w>','lady','<m>','has','<w>','won','<w>','the','<w>','match','<m>']
##        c=['Yikes','!','Dr','.','Alice',',','a',',','clever',',','lady',',','has',' ','won',' ','the','','match','.']
##        b=['"Stop','<m>','"','<w>']
##        c=['"Stop','!','"','<w>']
##        b=['<w>','Get','<w>','Lost','<m>','"','<w>']
##        c=[',','Get',',','Lost','!','"',',']
##        b=['Oh','<w>','my','<w>','goodness','<m>','Those','<w>','are','<w>','her','<w>','expensive','<w>','keys','<m>']
##        c=['Oh',',','my',',','goodness','!','Those',',','are',',','her',',','expensive',',','keys','.']
####        print(c)
##        b=['Ah', '<c>', 'What', '<w>', 'a', '<w>', 'precise', '<w>', 'poem', '<c>', ' ']
##        c=['Ah', ' ', '!', ' ', 'What', ' ', 'a', ' ', 'precise', ' ', 'poem', '.', ' ']
##        b=['Yikes', '<c>', 'Dr', '<m>', 'Mary', '<m>', 'a', '<w>', 'charming', '<w>', 'woman', '<m>', 'has', '<w>', 'got', '<w>', 'the', '<w>', 'match', '<c>']
##        c=['Yikes', ' ', 'Dr', ' ', 'Mary', ' ', 'a', ' ', 'charming', ' ', 'woman', ' ', 'has', ' ', 'got', ' ', 'the', ' ', 'match', ' ']
        b.append(" ")
        c.append(" ")
        ct=0
        for i in b:
            if i=="<m>":
                ct=ct+1
        mandatory=ct
        print(ct)

        
           #------------------------------------------<c> with exclm--------------------------------------
        for i in range(0,len(c)):
           if (b[i]=="<c>" and c[1]==" " and c[-2] in [".",",","!"]) :
                hint="Put a comma/exclamation after:"+ c[0] + "Put a exclamation/fullstop after:"+c[-3]
                mandlst.append(hint)
           if (b[i]=="<c>" and c[-2]==" " and c[1] in [".",",","!"]) :
               
                hint="Put a comma/exclamation after:"+ c[0] + "Put a exclamation/fullstop after:"+c[-3]
                mandlst.append(hint)  
               
           if (b[i]=="<c>" and c[1]=="!" and c[-2]==".") :
                hint="Correct Answer:If you put an exclamation after an interjection, the sentence has to ended with a period"
                correctlst.append(hint)
           if (b[i]=="<c>" and c[1]=="!" and c[-2]=="!") :
                hint="Put a fullstop after:"+c[-3]
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]=="!" and c[-2]==",") :
                hint="Put a fullstop after:"+c[-3]
                mandlst.append(hint)    
           if (b[i]=="<c>" and c[1]=="," and c[-2]=="!") :
                hint="Correct Answer:If you put an comma after an interjection, the sentence has to ended with a exclamation"
                correctlst.append(hint)
           if (b[i]=="<c>" and c[1]=="," and c[-2]==".") :
                hint="Put a exclamation after:"+c[-3]
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]=="," and c[-2]==",") :
                hint="Put a exclamation after:"+c[-3]
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]=="." and c[-2]==".") :
                hint="Put an exclamation after:"+c[0]
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]=="." and c[-2]==",") :
                hint="Put a comma/exclamation after:"+ c[0] + "Put an exclamation/fullstop after:"+c[-3]
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]=="." and c[-2]=="!") :
                hint="Put a comma after:"+ c[0] 
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]==" " and c[-2]=="!") :
                hint="Put a comma after:"+ c[0] 
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]==" " and c[-2]==".") :
                hint="Put a exclammation after:"+ c[0] 
                mandlst.append(hint)
           if (b[i]=="<c>" and c[1]==" " and c[-2] in [" ",","]) :
                hint="Put a exclamation after:"+ c[0] +"Put  a comma after:"+c[-3]
                mandlst.append(hint)     
        #-----------------------------------------<m> with exclamation---------------------------------
        for i in range(0,len(b)):
           
            if (b[i]=="<m>" and c[i]=="!"):
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det and c[-2] in ["."]:
                    hint="Correct Answer,Standalone interjections end with an exclamation and the sentnce end with a fullstop"
                    correctlst.append(hint)
             
                if (b[i-1] in exclmrules.onoun) and c[0] in exclmrules.standalonesplit:     
                    hint="Put a fullstop after: "+ c[-3]
                    mandlst.append(hint)
                #------------------type9endsurprise----------------------------------------------------------------------------
                if (b[i-1] in exclmrules.conj) and (b[i+1] in exclmrules.pronoun or b[i+1] in exclmrules.snoun)  :     
                    hint="Put a comma after: "+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and b[i+1] in exclmrules.standalonesplit:
                    hint="Put a fullstop after: "+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and b[i-2] in exclmrules.onoun:
                    hint="Correct Ans, HINT:if an interjection is used,put an exclamation"
                    correctlst.append(hint)   
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det:
                    hint="Correct Ans, HINT:if an interjection is used,put an exclamation"
                    correctlst.append(hint)
                #----------------------simpleintjn----
                if (b[i-1] in ['Stop','Wait','Lost','goodness','You']):    
                    hint="Put an exclamtion after: "+ b[i-1]
                    mandlst.append(hint)
                #-----------------------type9excmn---
                if (b[i-1] in exclmrules.title) and (b[i+1] in exclmrules.snoun):    
                    hint="Remove an exclamation and Put a fullstop after: "+ b[i-1]
                    mandlst.append(hint)                    
                    
                if (b[i-1] in exclmrules.snoun) and (b[i+1] in exclmrules.article):    
                    hint="Remove the exclamation and put a comma after: "+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.cnoun) and (b[i+1] in exclmrules.vbz):    
                    hint="Remove the exclamation and put a comma after: "+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and c[-2]=="!":
                    hint="Correct Ans, HINT:if an interjection is used,put an exclamation"
                    correctlst.append(hint)         
        #----------------------------------------
                if (b[i-1] in exclmrules.vbz) and (c[-2]=="!"):    
                    hint="Correct Answer:Always end a exclamatory sentence with an exclamation"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.verb) and (c[-2]=="!") and c[0] in exclmrules.qtag:    
                    hint="Correct Answer:Always end a exclamatory sentence with an exclamation"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and (c[-2]=="!") and c[0] in exclmrules.qtag:     
                    hint="Correct Answer:Always end a exclamatory sentence with an exclamation"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and b[i+1] in exclmrules.qtag and c[-2]==".":    
                    hint="Correct Answer:put an exclamation after an interjection, if the sentence has to ended with a period"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and (c[-2]=="!") and c[1]=="!":    
                    hint="Read the manual again,Hint:Sentence has to ended with a period if a exclamation is put after the interjection"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and b[i+1] in exclmrules.qtag and c[-2]=="!":    
                    hint="Put an exclamtion after: "+ b[i-1]
                    mandlst.append(hint)  
                  
                    
        #-----------------------------------------<m> with comma---------------------------------
        for i in range(0,len(b)):
            
            if (b[i]=="<m>" and c[i]==","):
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det and c[-2] in [","]:
                    hint="InCorrect Answer,Standalone interjections end with an exclamation and the sentnce end with a fullstop"
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det and c[-2] in ["!"," ",","]:
                    hint="InCorrect Answer,Standalone interjections end with an exclamation and the sentnce end with a fullstop"
                    mandlst.append(hint)
               #------------------type9endsurprise----------------------------------------------------------------------------
                if (b[i-1] in exclmrules.conj) and (b[i+1] in exclmrules.pronoun or b[i+1] in exclmrules.snoun):     
                    hint="Correct Answer:If a sentence starts with a Conjunction like So/Eventhough/But which id followed by a clause, then put seperate the conjunction and the clause with a comma"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and b[i+1] in exclmrules.standalonesplit:
                    hint="Put a fullstop after: "+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and b[i-2] in exclmrules.onoun:
                    hint="Put an exclamtion after: "+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and c[-2]==",":
                    hint="Put an exclamtion after: "+ b[i-1]
                    mandlst.append(hint)        
                #--------------type9ohmyg------------------------------------------------------------------------------
                 #-------------------------------------------type9ohmyg-------------
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det:
                    hint="Put an exclamation after: "+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and c[0] in exclmrules.standalonesplit:     
                    hint="Put a fullstop after: "+ c[-3]
                    mandlst.append(hint)
                #-------------simpleintjn------------------------------------------------------------------------------
                if (b[i-1] in ['Stop','Wait','Lost','goodness','You']):    
                    hint="Put a comma after: "+ b[i-1]
                    mandlst.append(hint) 
                #-------------type9exclmn--------------------------------------------------------------------------------
                if (b[i-1] in exclmrules.title) and (b[i+1] in exclmrules.snoun):    
                    hint="InCorrect Answer:Remove comma and Put a Fullstop after:"+ b[i-1]
                    mandlst.append(hint)
                    
                    
                if (b[i-1] in exclmrules.snoun) and (b[i+1] in exclmrules.article):    
                    hint="Correct Answer:A comma should be used when a relative clause follows the main subject.."
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.cnoun) and (b[i+1] in exclmrules.vbz):    
                    hint="Correct Answer:A comma should be used when a relative clause follows the main subject"
                    correctlst.append(hint)    
                #----------------------------------------
           
                if (b[i-1] in exclmrules.verb) and (c[-2]==",") and c[0] in exclmrules.qtag:     
                    hint="Put a comma after: "+ b[i-1]
                    mandlst.append(hint) 
                if (b[i-1] in exclmrules.onoun) and (c[-2]==",") and c[0] in exclmrules.qtag:     
                    hint="Put a comma after: "+ b[i-1]
                    mandlst.append(hint) 
                if (b[i-1] in exclmrules.exclm) and (b[i+1] in exclmrules.qtag):    
                    hint="Put a comma after: "+ b[i-1]
                    mandlst.append(hint) 
                if (b[i-1] in exclmrules.vbz) and (c[-2]==","):    
                    hint="Put a comma after: "+ b[i-1]
                    mandlst.append(hint) 
                if (b[i-1] in exclmrules.onoun) and (c[-2]==",") and c[1]=="!":    
                    hint="Put a comma after: "+ b[i-1]
                    mandlst.append(hint) 
                if (b[i-1] in exclmrules.exclm) and b[i+1] in exclmrules.qtag and c[-2]=="!":    
                    hint="Correct Answer,Put a Comma after an interjection, if the sentence has to ended with a exclamation"
                    correctlst.append(hint)     
        #-----------------------------------------<m> with fullstop---------------------------------
        for i in range(0,len(b)):
           
            if (b[i]=="<m>" and c[i]=="."):
                #------------------type9endsurprise----------------------------------------------------------------------------
                if (b[i-1] in exclmrules.conj) and (b[i+1] in exclmrules.pronoun or b[i+1] in exclmrules.snoun):     
                    hint="Put a comma after: "+ b[i-1]
                    mandlst.append(hint) 
                if (b[i-1] in exclmrules.onoun) and b[i+1] in exclmrules.standalonesplit:
                    hint="Correct Answer.End a clause with a fullstop"
                    correctlst.append(hint) 
                if (b[i-1] in exclmrules.standalonesplit) and b[i-2] in exclmrules.onoun:
                    hint="Put a exclamtion after: "+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and c[-2]==".":
                    hint="Put an exclamtion after: "+ b[i-1]
                    mandlst.append(hint)    
                #-------------------------------------------type9ohmyg-------------
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det:
                    hint="Put an exclamation after: "+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and c[0] in exclmrules.standalonesplit:     
                    hint="Correct Answer:End the sentence with a fullstop if you have an exclamation after the standalone interjections"
                    correctlst.append(hint)
                #---simpleintjn----
                if (b[i-1] in ['Stop','Wait','Lost','goodness','You']):    
                    hint="Put a fullstop after: "+ b[i-1]
                    mandlst.append(hint) 
                #---type9exclmn---
                if (b[i-1] in exclmrules.title) and (b[i+1] in exclmrules.snoun):    
                    hint="Correct Answer: Always put a fullstop after the title"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det:
                    hint="Put an exclamtion after: "+ b[i-1]
                    mandlst.append(hint)    
                    
                if (b[i-1] in exclmrules.snoun) and (b[i+1] in exclmrules.article):    
                    hint="Remove the fullstop and Put a comma after: "+ b[i-1]
                    mandlst.append(hint) 
                if (b[i-1] in exclmrules.cnoun) and (b[i+1] in exclmrules.vbz):    
                    hint="Remove the fullstop and Put a comma after: "+ b[i-1]
                    mandlst.append(hint)     
                #----------------------------------------

                if (b[i-1] in exclmrules.vbz) and (c[-2]=="."):    
                    hint="Put a fullstop after: "+ b[i-1]
                    mandlst.append(hint) 
                if (b[i-1] in exclmrules.onoun) and (c[-2]==".") and c[0] in exclmrules.qtag:     
                    hint="Put a fullstop after: "+ b[i-1]
                    mandlst.append(hint) 
                if (b[i-1] in exclmrules.exclm) and (b[i+1] in exclmrules.qtag):    
                    hint="Put a fullstop after: "+ b[i-1]
                    mandlst.append(hint)     
                if (b[i-1] in exclmrules.verb) and (c[-2]==".") and c[0] in exclmrules.qtag:     
                    hint="Put a fullstop after: "+ b[i-1]
                    mandlst.append(hint) 
                if (b[i-1] in exclmrules.onoun) and (c[-2]==".") and c[0] in exclmrules.exclm and c[1]=="!":    
                    hint="Correct Answer:Sentence has to ended with a period if a exclamation is put after the interjection"
                    correctlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and b[i+1] in exclmrules.qtag and c[-2]=="!":    
                    hint="Put a fullstop after: "+ b[i-1]
                    mandlst.append(hint)     
         #-----------------------------------------<m> with no punctuation---------------------------------
        for i in range(0,len(b)):
           
            if (b[i]=="<m>" and c[i]==" "):
                #------------------type9endsurprise----------------------------------------------------------------------------
                if (b[i-1] in exclmrules.conj) and (b[i+1] in exclmrules.pronoun or b[i+1] in exclmrules.snoun):     
                    hint="Put a comma after: "+ b[i-1]
                    mandlst.append(hint) 
                if (b[i-1] in exclmrules.onoun) and b[i+1] in exclmrules.standalonesplit:
                    hint="PUT a fullstop after: "+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and b[i-2] in exclmrules.onoun:
                    hint="PUT the punctuation after: "+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.standalonesplit) and c[-2]==" ":
                    hint="Put an exclamation after: "+ b[i-1]
                    mandlst.append(hint)    
                #type9ohmyg-------------
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det:
                    hint="Put an exclamtion after: "+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and c[0] in exclmrules.standalonesplit:     
                    hint="Put a fullstop after: "+ c[-3]
                    mandlst.append(hint)    
                 #---simpleintjn----
                if (b[i-1] in ['Stop','Wait','Lost','goodness','You']):    
                    hint="PUT the exclmation after: "+ b[i-1]
                    mandlst.append(hint)
                #---type9excmn---
                if (b[i-1] in exclmrules.title) and (b[i+1] in exclmrules.snoun):    
                    hint="PUT a fullstop "+ b[i-1]
                    mandlst.append(hint)
                                        
                if (b[i-1] in exclmrules.snoun) and (b[i+1] in exclmrules.article):    
                    hint="PUT a comma "+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.cnoun) and (b[i+1] in exclmrules.vbz):    
                    hint="PUT a comma "+ b[i-1]
                    mandlst.append(hint)   
                #----------------------------------------
                if (b[i-1] in exclmrules.vbz) and (c[-2]==" "):    
                    hint="PUT the exclmation "+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and (c[-2]==" ") and c[0] in exclmrules.qtag:     
                    hint="PUT the exclmation after: "+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and (b[i+1] in exclmrules.qtag):    
                    hint="PUT the exclmation after: "+ b[i-1]
                    mandlst.append(hint)    
                if (b[i-1] in exclmrules.verb) and (c[-2]==" ") and c[0] in exclmrules.qtag:     
                    hint="PUT a fullstop after: "+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.onoun) and (c[-2]==".") and c[1]=="!":    
                    hint="PUT the exclmation after: "+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in exclmrules.exclm) and b[i+1] in exclmrules.qtag and c[-2]=="!":    
                    hint="PUT the exclmation after: "+ b[i-1]
                    mandlst.append(hint)
                    
        #-----------------------------------------<w> with exclamation--------------------------------
        for i in range(0,len(b)):
           
            if (b[i]=="<w>" and c[i]=="!"):
                #---------------------------------type9ohmyg-----------------
                if (b[i-1] in exclmrules.standalonesplit and b[i+1] in exclmrules.standalonesplit):
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.determiner and b[i+1] in exclmrules.vbz):
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.vbz and b[i+1] in exclmrules.pronoun):
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
            
                #--------------------------------------simpleintjn----
                if (b[i-1] == '"' or b[i-1]== 'Get'):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                #-------------------------------------type9exclm---------------------------------
                if b[i-1] in exclmrules.adj and b[i+1] in exclmrules.cnoun:
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in exclmrules.vbz and b[i+1] in exclmrules.verb:
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)

                if b[i-1] in exclmrules.article and b[i+1] in exclmrules.adj:
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in exclmrules.verb and b[i+1] in (exclmrules.pronoun or exclmrules.det):
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in (exclmrules.pronoun or exclmrules.det) and b[i+1] in exclmrules.onoun:
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)  

                 #----------------------------------------------
                if (b[i-1] in exclmrules.qtag) and (b[i+1] in exclmrules.article):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                   
                if (b[i-1] in exclmrules.article) and (b[i+1] in exclmrules.adj):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.adj) and (b[i+1] in exclmrules.onoun):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)

                if (b[i-1] in exclmrules.onoun) and (b[i+1] in exclmrules.pronoun):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)

                if (b[i-1] in exclmrules.pronoun) and (b[i+1] in exclmrules.vbz):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.qtag) and (b[i+1] in exclmrules.adverb):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.adverb) and (b[i+1] in exclmrules.snoun):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.snoun) and (b[i+1] in exclmrules.verb):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                    
                if (b[i-1] in exclmrules.standalonesplit) and b[i+1] in exclmrules.determiner or b[i+1] in exclmrules.det:
                    hint="Put an exclamtion after: "+ b[i-1]
                    mandlst.append(hint)
                   
        #-----------------------------------------<w> with comma------------------------------------------------------------------------------------------
        for i in range(0,len(b)):
           
            if (b[i]=="<w>" and c[i]==","):
                #---------------------------------type9ohmyg----------------------------------------------------------------------------------------------
                if (b[i-1] in exclmrules.standalonesplit and b[i+1] in exclmrules.standalonesplit):
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.determiner and b[i+1] in exclmrules.vbz):
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.vbz and b[i+1] in exclmrules.pronoun):
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                  
                #-------------------------------------simpleintjn----------------------------------------------------------------------------------------------------------------------------
                if (b[i-1] == '"' or b[i-1]== 'Get'):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                #--------------------------------------type9exclm----------------------------------------------------------------------------------------------------------------------
                if b[i-1] in exclmrules.adj and b[i+1] in exclmrules.cnoun:
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in exclmrules.vbz and b[i+1] in exclmrules.verb:
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)

                if b[i-1] in exclmrules.article and b[i+1] in exclmrules.adj:
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in exclmrules.verb and b[i+1] in (exclmrules.pronoun or exclmrules.det):
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in (exclmrules.pronoun or exclmrules.det) and b[i+1] in exclmrules.onoun:
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                
                if (b[i-1] in exclmrules.qtag) and (b[i+1] in exclmrules.article):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.article) and (b[i+1] in exclmrules.adj):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)

                if (b[i-1] in exclmrules.adj) and (b[i+1] in exclmrules.onoun):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)

                if (b[i-1] in exclmrules.onoun) and (b[i+1] in exclmrules.pronoun):    
                    hint="Read the manual again, HINT:No need of a punctuation in between a noun and a pronoun"
                    hintlst.append(hint)

                if (b[i-1] in exclmrules.pronoun) and (b[i+1] in exclmrules.vbz):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.qtag) and (b[i+1] in exclmrules.adverb):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.adverb) and (b[i+1] in exclmrules.snoun):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)    
                if (b[i-1] in exclmrules.snoun) and (b[i+1] in exclmrules.verb):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
        #-----------------------------------------<w> with fullstop ------------------------------------------------------------------------------------
        for i in range(0,len(b)):
           
            if (b[i]=="<w>" and c[i]=="."):
            #--------------------------------------type9endsurprise.py-----------------------------------------------------------------------------------
                
                #---------------------------------type9ohmyg---------------------------------------------------------------------------------------------
                if (b[i-1] in exclmrules.standalonesplit and b[i+1] in exclmrules.standalonesplit):
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.determiner and b[i+1] in exclmrules.vbz):
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.vbz and b[i+1] in exclmrules.pronoun):
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
               
                
                #-------------------------------------------simpleintjn----------------------------------------------------------------------------------------------------------------------------
                    
                if (b[i-1] == '"' or b[i-1]== 'Get'):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                #-------------------------------------------type9exclm----------------------------------------------------------------------------------------------------------------------
                if b[i-1] in exclmrules.adj and b[i+1] in exclmrules.cnoun:
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in exclmrules.vbz and b[i+1] in exclmrules.verb:
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)

                if b[i-1] in exclmrules.article and b[i+1] in exclmrules.adj:
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in exclmrules.verb and b[i+1] in (exclmrules.pronoun or exclmrules.det):
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in (exclmrules.pronoun or exclmrules.det) and b[i+1] in exclmrules.onoun:
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                #------------------------------------------------------------------------------------------------------------------------------------------- 

                if (b[i-1] in exclmrules.qtag) and (b[i+1] in exclmrules.article):    
                    hhint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.article) and (b[i+1] in exclmrules.adj):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)

                if (b[i-1] in exclmrules.adj) and (b[i+1] in exclmrules.onoun):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)

                if (b[i-1] in exclmrules.onoun) and (b[i+1] in exclmrules.pronoun):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.pronoun) and (b[i+1] in exclmrules.vbz):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.qtag) and (b[i+1] in exclmrules.adverb):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if (b[i-1] in exclmrules.adverb) and (b[i+1] in exclmrules.snoun):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)   
                if (b[i-1] in exclmrules.snoun) and (b[i+1] in exclmrules.verb):    
                    hint="Remove the punctuation after: "+ b[i-1]
                    hintlst.append(hint)    
  

        return(hintlst,mandlst,correctlst,mandatory)     
##p1=exclmrules()
##hintlst,mandlst,correctlst,mandatory=p1.exclmone()
##
##for i in hintlst:
##    print(i)
##for j in mandlst:
##    print(j)
##for k in correctlst:
##    print(k)

         
