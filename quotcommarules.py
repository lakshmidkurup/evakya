import mysql.connector
import re
from dateutil.parser import parse
mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="rohith@123",
                database="pythonlogin"
        )
mycursor = mydb.cursor()
class quotcrules:
    snoun=['Mary','James','John','Alice','A. Roy', 'K. Singh', 'R. K. Narayan', 'R. Kushner','Esmail','Bagani' ]
    verb=['said','lift','stand','answered','won','got','secured','achieved','hurt','lost','opened','closed','cooked','met','read','wrote','drew','drank','paid','bought','stayed','worked','joined','taught','married','dated','intracted','consulted','visited','debated','argued','fought','lived','seperated']
    verb1=[]
    verbs=['lift','stand','answer','win','get','secure','achieve','hurt','lose','open','close','cook','meet','read','write','draw','drink','pay','buy','stay','work','join','teach','married','date','intract','consult','visit','debate','argue','fight','live','seperate']
    onoun=['box','book','cage','scenary','house','building','tea','water','coffee','biriyani','pulav','kichdi','novel','story','match','race','ankle','leg','first-prize','second-prize','job','position','keys','books','poem','story','furniture','vegetables','fruits','bicycles','bicycle','house','organisation','school','college','flat','question']
    prep=['in','for','with','from','on','to']
    vbz=['is','has','was']
    pronoun=['his','her','he','she','it']
    pronounc=[]
    for i in pronoun:
        pronounc.append(i.capitalize())
    pronoun1=[]
    pronounq=[]
    onounq=[]
    adj=['confident','adorable','generous','charming','clever','huge','red','small','heavy','beautiful','fantastic','mesmerising','well-defined','hot','cold','warm','strong-flavored','delicious','tasty','mind-blowing','spicy','excellent','lovely','thrilled','elated','difficult','intelligent','rapid-fire','open-ended','lovely','fascinating','short','precise','interesting','selective','magnificent','high-grade','exceptional','focused','ambitious','demanding','competetive','exciting','brilliant','amazing','three-room','luxurious','spacious','own','modern','adorable','favorite','new','worthy','valuable','expensive','precious','limpy','twisted','sprained','fractured','considerate','attractive','amusing','jovial']
    det="the"
    conj=['and','but']
    detcap=det.capitalize()
    for i in pronoun:
        pronoun1.append(i.capitalize())
    for i in pronoun1:
        pronounq.append('"'+i)
    for i in onoun:
        onounq.append(i+'"')
    def commaone(b,c,correct,category,level,username,userid,eid,submittedtext):
##    def commaone(self):    
##        b=['"', '<w>', 'He', '<w>', 'has', '<w>', 'hurt', '<w>', 'his', '<w>', 'leg', '<m>', '"', '<w>', 'John', '<w>', 'said', '<w>', 'to', '<w>', 'James', '<m>']
##        c=['"', ',', 'He', ' ', 'has', ' ', 'hurt', ' ', 'his', ' ', 'leg', ',', '"', ' ', 'John', ' ', 'said', ' ', 'to', ' ', 'James', ' ']
##        b=['The', '<w>', 'pulav', '<m>', 'Alice', '<w>', 'cooked', '<w>', 'is', '<w>', 'delicious', '<m>', 'tasty', '<m>', 'mind-blowing', '<w>', 'and', '<w>', 'spicy', '<m>', ' ']
##        c=['The', ' ', 'pulav', ',', 'Alice', ' ', 'cooked', ' ', 'is', ' ', 'delicious', ' ', 'tasty', ',', 'mind', ' ', '-', ' ', 'blowing', ',', 'and', ' ', 'spicy', '.', ' ']
        b.append(" ")
        c.append(" ")
        ct=0
        for i in b:
            if i=="<m>":
                ct=ct+1
        mandatory=ct    
        mandlst=[]
        correctlst=[]
        hintlst=[]
        print(b)
        print(c)
          
##        b=['"He', '<w>', 'has', '<w>', 'lost', '<w>', 'his', '<w>', 'keys"', '<m>', 'Alice', '<w>', 'said', '<w>', 'to', '<w>', 'Mary', '<m>', '"']
##
##        c=['"He', ';', 'has', ';', 'lost', ';', 'his', ';', 'keys"', ',', 'Alice', '', 'said', ';', 'to', ';', 'Mary', '.', '"']
##        b=['The', '<w>', 'story', '<w>', 'Alice', '<w>', 'read', '<w>', 'is', '<w>', 'short', '<m>', 'interesting', '<m>', 'selective', '<w>', 'and', '<w>', 'fascinating', '<m>',' ']
##        c=['The', ';', 'story', ' ', 'Alice', ' ', 'read', ' ' ,'is', ' ', 'short', ',', 'interesting', ',', 'selective', ',', 'and', ';', 'fascinating', '.',' ']  
      
           
    #---------------------------------------------------<m> with semicolon-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==";"):
                
                if (b[i-1] in quotcrules.onoun) and (b[i+1]=='"'):    
                    hint="Incorrect Answer:Click on the sidepane and read the manuals,HINT: Put a Comma at mandatory location"
                    mandlst.append(hint)
                if b[i-1] in quotcrules.snoun and c[i]==";" and c[i+1]==" ":  
                    hint="Incorrect Answer.Always end a sentence with fullstop"
                    mandlst.append(hint)
                if b[i-1] in quotcrules.onoun and b[i+1] in quotcrules.snoun:  
                    hint="Incorrect Answer.Click on the sidepane and read the manuals,HINT: Put a Comma at mandatory location"
                    mandlst.append(hint)      
               
                if b[i-1] in quotcrules.adj and b[i+1]in quotcrules.conj: 
                    hint="InCorrect Answer:Click on the sidepane and read the manuals,HINT: Put a Comma at mandatory location"
                    correctlst.append(hint) 
                if b[i-1] in quotcrules.adj and b[i+1] in quotcrules.adj:  
                    hint="Incorrect Answer.Click on the sidepane and read the manuals,HINT: Put a Comma at mandatory location"
                    mandlst.append(hint)    
   #---------------------------------------------------<m> with comma-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):
                
                if (b[i-1] in quotcrules.onounq) and (b[i+1] in quotcrules.snoun):    
                    hint="Correct Answer:Comma is used to separate the reported speech and reporting speech. It separates who is saying what"
                    correctlst.append(hint)
                if (b[i-1] in quotcrules.onoun) and (b[i+1]=='"'):    
                    hint="Correct Answer:Comma is used to separate the reported speech and reporting speech. It separates who is saying what"
                    correctlst.append(hint)
                if b[i-1] in quotcrules.snoun and c[i]=="," and c[i+1]==" ":  
                    hint="Incorrect Answer.Click on the sidepane and read the manuals,HINT: Put a Comma at mandatory location"
                    mandlst.append(hint)
               
                if b[i-1] in quotcrules.onoun and b[i+1] in quotcrules.snoun:  
                    hint="Correct Answer.Use a Comma After an Introductory Word or Phrase"
                    correctlst.append(hint)      
                if b[i-1] in quotcrules.adj and b[i+1] in quotcrules.adj:  
                    hint="correct Answer.Commas needed to seperate adjectives"
                    correctlst.append(hint) 
    #---------------------------------------------------<m> with fullstop-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                
                if (b[i-1] in quotcrules.onoun) and (b[i+1]=='"'):    
                    hint="Incorrect Answer:Click on the sidepane and read the manuals,HINT: Put a Comma at mandatory location"
                    mandlst.append(hint)      
                if (b[i-1] in quotcrules.onoun) and (b[i+1]=='"'):    
                    hint="Incorrect Answer:Click on the sidepane and read the manuals,HINT: Put a Comma at mandatory location"
                    mandlst.append(hint)
                if b[i-1] in quotcrules.snoun and c[i]=="." and c[i+1]==" ":  
                    hint="correct Answer.Always end a sentence with fullstop"
                    correctlst.append(hint)
            #-------------------------------------------adjcommafinal.py-----------------------------------------------------------------
               
                if b[i-1] in quotcrules.adj and b[i+1]==" ": 
                    hint="Correct Answer:Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)    
                if b[i-1] in quotcrules.onoun and b[i+1] in quotcrules.snoun:  
                    hint="Incorrect Answer.Click on the sidepane and read the manuals,HINT: Put a Comma at mandatory location"
                    mandlst.append(hint)     
                if b[i-1] in quotcrules.adj and b[i+1] in quotcrules.adj:  
                    hint="Incorrect Answer.Click on the sidepane and read the manuals,HINT: Put a Comma at mandatory location"
                    mandlst.append(hint)  
    #---------------------------------------------------<m> with no punctuation-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==" "):
                if (b[i-1] in quotcrules.onoun) and (b[i+1]=='"'):    
                    hint="Incorrect Answer:Click on the sidepane and read the manuals,HINT: Put a Comma at mandatory location"
                    mandlst.append(hint)
                if b[i-1] in quotcrules.snoun and c[i]==" " and c[i+1]==" ":  
                    hint="Incorrect Answer.Always end a sentence with fullstop"
                    mandlst.append(hint)
                if b[i-1] in quotcrules.onoun and b[i+1] in quotcrules.snoun:  
                    hint="Incorrect Answer.Click on the sidepane and read the manuals,HINT: Put a Comma at mandatory location"
                    mandlst.append(hint) 
                if b[i-1] in quotcrules.adj and b[i+1] in quotcrules.adj:  
                    hint="Incorrect Answer.Click on the sidepane and read the manuals,HINT: Put a Comma at mandatory location"
                    mandlst.append(hint)  
    #---------------------------------------------------<w> with semicolon-----------------------------------------------------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<w>" and c[i]==";"):
                 hint="Click on the sidepane and read the manuals,HINT: Remove punctuations where they arent mandatory"
                 hintlst.append(hint)

                
                      
             
                            
    #---------------------------------------------------<w> with fullstop-----------------------------------------------------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<w>" and c[i]=="."):
                hint="Click on the sidepane and read the manuals,HINT: Remove punctuations where they arent mandatory"
                hintlst.append(hint)

                
#---------------------------------------------------<w> with comma-----------------------------------------------------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<w>" and c[i]==","):
                hint="Click on the sidepane and read the manuals,HINT: Remove punctuations where they arent mandatory"
                hintlst.append(hint)
                  
                    
        return(hintlst,mandlst,correctlst,mandatory)      
    def commatwo(b,c,correct,category,level,username,userid,eid,submittedtext):
##    def commatwo(self):  
          
##        b=['"', '<w>', 'He', '<w>', 'has', '<w>', 'hurt', '<w>', 'his', '<w>', 'leg', '<m>', '"', '<w>', 'John', '<w>', 'said', '<w>', 'to', '<w>', 'James', '<m>']
##        c=['"', ',', 'He', ' ', 'has', ' ', 'hurt', ' ', 'his', ' ', 'leg', ',', '"', ' ', 'John', ' ', 'said', ' ', 'to', ' ', 'James', ' ']
        b.append(" ")
        c.append(" ")
        ct=0
        for i in b:
            if i=="<m>":
                ct=ct+1
        mandatory=ct    
        mandlst=[]
        correctlst=[]
        hintlst=[]
        print(b)
        print(c)
           
    #---------------------------------------------------<m> with semicolon-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==";"):
               
                if (b[i-1] in quotcrules.onoun) and (b[i+1]=='"'):    
                    hint="Incorrect Answer:HINT:Comma is used to separate the reported speech and reporting speech. It separates who is saying what"
                    mandlst.append(hint)
                if b[i-1] in quotcrules.snoun and c[i]==";" and c[i+1]==" ":  
                    hint="Incorrect Answer.Always end a sentence with fullstop"
                    mandlst.append(hint)                      
                if b[i-1] in quotcrules.snoun and b[i+1]== '"':
                    hint="Read the manual again, HINT:Put a fullstop after the reporting speech[who said to whom]"
                    mandlst.append(hint)
                if b[i-1] == '"' and b[i+1] in quotcrules.snoun :
                    hint="Read the manual again, HINT:Put a fullstop after the reporting speech[who said to whom]"
                    mandlst.append(hint) 
        #--------------------------------------------adjcommafinal.py-----------------------------------------------------------------
                if b[i-1] in quotcrules.adj and b[i+1] in quotcrules.adj:
                    hint="Read the manual again, HINT:A comma should be used in between the adjectives"
                    mandlst.append(hint)
                if b[i-1] in quotcrules.adj and b[i+1]==" ":
                    hint="Read the manual again, HINT:Always end a sentence with a FULLSTOP"
                    mandlst.append(hint)
                if b[i-1] in quotcrules.onoun and b[i+1] in quotcrules.snoun:  
                    hint="Incorrect Answer.Read the manual again,Use a Comma After an Introductory Word or Phrase"
                    mandlst.append(hint)
                   
   #---------------------------------------------------<m> with comma-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):
                if (b[i-1] in quotcrules.onoun) and (b[i+1]=='"'):    
                    hint="correct Answer:HINT:Comma is used to separate the reported speech and reporting speech. It separates who is saying what"
                    correctlst.append(hint)
               
                
                if (b[i-1] in quotcrules.onounq) and (b[i+1] in quotcrules.snoun):    
                    hint="Correct Answer:Comma is used to separate the reported speech and reporting speech. It separates who is saying what"
                    correctlst.append(hint)
                    
                if b[i-1] in quotcrules.snoun and c[i]== ',' and c[i+1]==" ":
                    hint="Read the manual again, HINT:Always end a sentence with FUllSTOP"
                    mandlst.append(hint)
                 
                if b[i-1] in quotcrules.snoun and b[i+1]== '"':
                    hint="Read the manual again, HINT:Put a fullstop after the reporting speech[who said to whom]"
                    mandlst.append(hint)

                if b[i-1] == '"' and b[i+1] in quotcrules.snoun :
                    hint="Read the manual again, HINT:Put a fullstop after the reporting speech[who said to whom]"
                    mandlst.append(hint)     
                     #-------------------------------------------adjcommafinal.py-----------------------------------------------------------------
                if b[i-1] in quotcrules.adj and b[i+1] in quotcrules.adj:
                    hint="Correct Answer:A comma should be used in between the adjectives"
                    correctlst.append(hint)
                if b[i-1] in quotcrules.adj and b[i+1]==" ": 
                    hint="Read the manual again, HINT:Always end a sentence with a FULLSTOP"
                    mandlst.append(hint)  
                if b[i-1] in quotcrules.onoun and b[i+1] in quotcrules.snoun:  
                    hint="Correct Answer.Read the manual again,Use a Comma After an Introductory Word or Phrase"
                    correctlst.append(hint)   
                    
    #---------------------------------------------------<m> with fullstop-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                if (b[i-1] in quotcrules.onoun) and (b[i+1]=='"'):    
                    hint="Incorrect Answer:HINT:Comma is used to separate the reported speech and reporting speech. It separates who is saying what"
                    mandlst.append(hint)
                    
                if b[i-1] in quotcrules.snoun and c[i]=="." and c[i+1]==" ":  
                    hint="correct Answer.Always end a sentence with fullstop"
                    correctlst.append(hint)
                    
                if (b[i-1] in quotcrules.onounq) and (b[i+1] in quotcrules.snoun):    
                    hint="Read the manual again, HINT:Comma is used to separate the reported speech and reporting speech. It separates who is saying what"
                    mandlst.append(hint)
               
                      
                if b[i-1] in quotcrules.snoun and b[i+1]== '"':
                    hint="Correct Answer:Put a fullstop after the reporting speech[who said to whom], before the ending quotation"
                    correctlst.append(hint)
                    
                if b[i-1] == '"' and b[i+1] in quotcrules.snoun :
                    hint="Read the manual again, HINT:Put a fullstop after the reporting speech[who said to whom]"
                    correctlst.append(hint)
                    
            #-------------------------------------------adjcommafinal.py-----------------------------------------------------------------
                if b[i-1] in quotcrules.adj and b[i+1] in quotcrules.adj:
                    hint="Correct Answer:HINT:No need of a fullstop,but a comma should be used in between the adjectives"
                    mandlst.append(hint)
                    
                if b[i-1] in quotcrules.adj and b[i+1]==" ": 
                    hint="Correct Answer:Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)    
                    
                if b[i-1] in quotcrules.onoun and b[i+1] in quotcrules.snoun:  
                    hint="Correct Answer.Use a Comma After an Introductory Word or Phrase"
                    correctlst.append(hint)      
                         
    #---------------------------------------------------<m> with no punctuation-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==" "):
                
                if (b[i-1] in quotcrules.onoun) and (b[i+1]=='"'):    
                    hint="Incorrect Answer:HINT:Comma is used to separate the reported speech and reporting speech. It separates who is saying what"
                    mandlst.append(hint)
                    
              
                if (b[i-1] in quotcrules.onounq) and (b[i+1] in quotcrules.snoun):    
                    hint="Read the manual again, HINT:Comma is used to separate the reported speech and reporting speech. It separates who is saying what"
                    mandlst.append(hint)
                    
                if b[i-1] in quotcrules.snoun and c[i]==" " and c[i+1]==" ":
                    hint="Read the manual again, HINT:Always end a sentence with FUllSTOP"
                    mandlst.append(hint)
                    
                if b[i-1] in quotcrules.snoun and b[i+1]=='"':
                    hint="Correct Answer:Put a fullstop after the reporting speech[who said to whom], before the ending quotation"
                    mandlst.append(hint)
                if b[i-1] == '"' and b[i+1] in quotcrules.snoun :
                    hint="Read the manual again, HINT:Put a fullstop after the reporting speech[who said to whom]"
                    mandlst.append(hint)   
          #-------------------------------------------adjcommafinal.py-----------------------------------------------------------------
                if b[i-1] in quotcrules.adj and b[i+1] in quotcrules.adj:
                    hint="Read the manual again, HINT:A comma should be used in between the adjectives"
                    mandlst.append(hint)
                if b[i-1] in quotcrules.onoun and b[i+1] in quotcrules.snoun:  
                    hint="Read the manual again,Use a Comma After an Introductory Word or Phrase"
                    mandlst.append(hint)       
                              
                    
    #---------------------------------------------------<w> with semicolon-----------------------------------------------------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<w>" and c[i]==";"):
                if (b[i-1] in quotcrules.pronounc) and (b[i+1] in quotcrules.vbz):    
                    hint="Read the manual again, HINT:No need of semicolon after a pronoun when followed by [is,was,has] etc."
                    hintlst.append(hint)
                if (b[i-1] =='"') and (b[i+1] in quotcrules.pronoun1):    
                    hint="Read the manual again, HINT:No need of semicolon at the start of the speech."
                    hintlst.append(hint)
                      
                if b[i-1] in quotcrules.vbz and b[i+1] in quotcrules.verb:
                    hint="Read the manual again, HINT:No need of semicolon after [is,was,has etc.]  when followed by a verb"
                    hintlst.append(hint)

                if b[i-1] in quotcrules.verb and b[i+1] in quotcrules.pronoun:
                    hint="Read the manual again, HINT:No need of semicolon after the verb when followed by a pronoun."
                    hintlst.append(hint)

                if b[i-1] in quotcrules.pronoun and b[i+1] in quotcrules.onounq:
                    hint="Read the manual again, HINT:No need of semicolon between a pronoun and a noun"
                    hintlst.append(hint)

                if b[i-1] in quotcrules.snoun and b[i+1] in quotcrules.verb:
                    hint="Read the manual again, HINT:No need of a semicolon after a noun when followed by a verb"
                    hintlst.append(hint)

                if b[i-1] in quotcrules.verb and b[i+1] in quotcrules.prep:
                    hint="Read the manual again, HINT:No need of a semicolon after a  verb when followed by a preposition"
                    hintlst.append(hint)    
                if b[i-1] in quotcrules.prep and b[i+1] in quotcrules.snoun:
                    hint="Read the manual again, HINT:No need of a semicolon after a  preposition when followed by a noun"
                    hintlst.append(hint)

        #----------------------------------adjcomma.py------------------------------------
                if b[i-1] in quotcrules.detcap and b[i+1] in quotcrules.onoun:
                    hint="Read the manual again, HINT:No need of a semicolon after the determiner when followed by a noun"
                    hintlst.append(hint)
                if b[i-1] in quotcrules.onoun and b[i+1] in quotcrules.snoun:
                    hint="Read the manual again, HINT:No need of a semicolon between object noun and subject noun"
                    hintlst.append(hint)     
                if b[i-1] in quotcrules.snoun and b[i+1] in quotcrules.verb:
                    hint="Read the manual again, HINT:No need of a semicolon after the noun when followed by a verb"
                    hintlst.append(hint)
                if b[i-1] in quotcrules.verb and b[i+1] in quotcrules.vbz:
                    hint="Read the manual again, HINT:No need of a semicolon after a verb when followed by [is/was/has] etc"
                    hintlst.append(hint)    
               
                if b[i-1] in quotcrules.conj and b[i+1] in quotcrules.adj:
                    hint="Read the manual again, HINT:No need of a semicolon after a conjunction-[and]"
                    hintlst.append(hint)   
                if b[i-1] in quotcrules.adj and b[i+1] in quotcrules.conj:
                    hint="Read the manual again, HINT:No need of a semicolon before a conjunction-[and]"
                    hintlst.append(hint)            
    #---------------------------------------------------<w> with fullstop-----------------------------------------------------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<w>" and c[i]=="."):
            
                if (b[i-1] =='"') and (b[i+1] in quotcrules.pronoun1):    
                    hint="Read the manual again, HINT:No need of fullstop at the start of the speech."
                    hintlst.append(hint)
                if (b[i-1] in quotcrules.pronounq) and (b[i+1] in quotcrules.vbz):    
                    hint="Read the manual again, HINT:No need of fullstop after a pronoun when followed by [is,was,has] etc."
                    hintlst.append(hint)
                
                      
                if b[i-1] in quotcrules.vbz and b[i+1] in quotcrules.verb:
                    hint="Read the manual again, HINT:No need of fullstop after [is,was,has etc.]  when followed by a verb"
                    hintlst.append(hint)

                if b[i-1] in quotcrules.verb and b[i+1] in quotcrules.pronoun:
                    hint="Read the manual again, HINT:No need of fullstop after the verb when followed by a pronoun."
                    hintlst.append(hint)

                if b[i-1] in quotcrules.pronoun and b[i+1] in quotcrules.onounq:
                    hint="Read the manual again, HINT:No need of fullstop between a pronoun and a noun"
                    hintlst.append(hint)

                if b[i-1] in quotcrules.snoun and b[i+1] in quotcrules.verb:
                    hint="Read the manual again, HINT:No need of a fullstop after a noun when followed by a verb"
                    hintlst.append(hint)

                if b[i-1] in quotcrules.verb and b[i+1] in quotcrules.prep:
                    hint="Read the manual again, HINT:No need of a fullstop after a  verb when followed by a preposition"
                    hintlst.append(hint)    
                if b[i-1] in quotcrules.prep and b[i+1] in quotcrules.snoun:
                    hint="Read the manual again, HINT:No need of a fullstop after a  preposition when followed by a noun"
                    hintlst.append(hint)
                    #----------------------------------adjcomma.py------------------------------------
                if b[i-1] in quotcrules.detcap and b[i+1] in quotcrules.onoun:
                    hint="Read the manual again, HINT:No need of a fullstop after the determiner when followed by a noun"
                    hintlst.append(hint)
                if b[i-1] in quotcrules.onoun and b[i+1] in quotcrules.snoun:
                    hint="Read the manual again, HINT:No need of a fullstop between object noun and subject noun"
                    hintlst.append(hint)     
                if b[i-1] in quotcrules.snoun and b[i+1] in quotcrules.verb:
                    hint="Read the manual again, HINT:No need of a fullstop after the noun when followed by a verb"
                    hintlst.append(hint)
                if b[i-1] in quotcrules.verb and b[i+1] in quotcrules.vbz:
                    hint="Read the manual again, HINT:No need of a fullstop after a verb when followed by [is/was/has] etc"
                    hintlst.append(hint)
                if b[i-1] in quotcrules.conj and b[i+1] in quotcrules.adj:
                    hint="Read the manual again, HINT:No need of a fullstop after a conjunction-[and]"
                    hintlst.append(hint)
                if b[i-1] in quotcrules.adj and b[i+1] in quotcrules.conj:
                    hint="Read the manual again, HINT:No need of a fullstop before a conjunction-[and]"
                    hintlst.append(hint)
                    
                        
#---------------------------------------------------<w> with comma-----------------------------------------------------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<w>" and c[i]==","):
                if (b[i-1] in quotcrules.pronounc) and (b[i+1] in quotcrules.vbz):    
                    hint="Read the manual again, HINT:No need of comma after a pronoun when followed by [is,was,has] etc."
                    hintlst.append(hint)
                if (b[i-1] =='"') and (b[i+1] in quotcrules.pronoun1):    
                    hint="Read the manual again, HINT:No need of comma at the start of the speech."
                    hintlst.append(hint)
                      
                if b[i-1] in quotcrules.vbz and b[i+1] in quotcrules.verb:
                    hint="Read the manual again, HINT:No need of comma after [is,was,has etc.]  when followed by a verb"
                    hintlst.append(hint)

                if b[i-1] in quotcrules.verb and b[i+1] in quotcrules.pronoun:
                    hint="Read the manual again, HINT:No need of comma after the verb when followed by a pronoun."
                    hintlst.append(hint)

                if b[i-1] in quotcrules.pronoun and b[i+1] in quotcrules.onounq:
                    hint="Read the manual again, HINT:No need of comma between a pronoun and a noun"
                    hintlst.append(hint)

                if b[i-1] in quotcrules.snoun and b[i+1] in quotcrules.verb:
                    hint="Read the manual again, HINT:No need of a comma after a noun when followed by a verb"
                    hintlst.append(hint)

                if b[i-1] in quotcrules.verb and b[i+1] in quotcrules.prep:
                    hint="Read the manual again, HINT:No need of a comma after a  verb when followed by a preposition"
                    hintlst.append(hint)    
                if b[i-1] in quotcrules.prep and b[i+1] in quotcrules.snoun:
                    hint="Read the manual again, HINT:No need of a comma after a  preposition when followed by a noun"
                    hintlst.append(hint)
            #----------------------------------adjcomma.py------------------------------------
                if b[i-1] in quotcrules.detcap and b[i+1] in quotcrules.onoun:
                    hint="Read the manual again, HINT:No need of a comma after the determiner when followed by a noun"
                    hintlst.append(hint)
                if b[i-1] in quotcrules.onoun and b[i+1] in quotcrules.snoun:
                    hint="Read the manual again, HINT:No need of a comma between object noun and subject noun"
                    hintlst.append(hint)    
                if b[i-1] in quotcrules.snoun and b[i+1] in quotcrules.verb:
                    hint="Read the manual again, HINT:No need of a comma after the noun when followed by a verb"
                    hintlst.append(hint)
                if b[i-1] in quotcrules.verb and b[i+1] in quotcrules.vbz:
                    hint="Read the manual again, HINT:No need of a comma after the verb when followed by a [is/was] etc"
                    hintlst.append(hint)
                if b[i-1] in quotcrules.conj and b[i+1] in quotcrules.adj:
                    hint="Read the manual again, HINT:No need of a comma after a conjunction-[and]"
                    hintlst.append(hint)
                if b[i-1] in quotcrules.adj and b[i+1] in quotcrules.conj:
                    hint="Read the manual again, HINT:No need of a comma before a conjunction-[and]"
                    hintlst.append(hint)    
        print(hintlst,mandlst,correctlst,mandatory)            
        return(hintlst,mandlst,correctlst,mandatory)         
    def commathree(b,c,correct,category,level,username,userid,eid,submittedtext):
    #def commathree(self):    
##        b=['"', '<w>', 'He', '<w>', 'has', '<w>', 'hurt', '<w>', 'his', '<w>', 'leg', '<m>', '"', '<w>', 'John', '<w>', 'said', '<w>', 'to', '<w>', 'James', '<m>']
##        c=['"', ',', 'He', ' ', 'has', ' ', 'hurt', ' ', 'his', ' ', 'leg', ',', '"', ' ', 'John', ' ', 'said', ' ', 'to', ' ', 'James', ' ']

        b.append(" ")
        c.append(" ")
        ct=0
        for i in b:
            if i=="<m>":
                ct=ct+1
        mandatory=ct    
        mandlst=[]
        correctlst=[]
        hintlst=[]
        print(b)
        print(c)
          
##        b=['"He', '<w>', 'has', '<w>', 'lost', '<w>', 'his', '<w>', 'keys"', '<m>', 'Alice', '<w>', 'said', '<w>', 'to', '<w>', 'Mary', '<m>', '"']
##
##        c=['"He', ';', 'has', ';', 'lost', ';', 'his', ';', 'keys"', ',', 'Alice', '', 'said', ';', 'to', ';', 'Mary', '.', '"']
##        b=['The', '<w>', 'story', '<w>', 'Alice', '<w>', 'read', '<w>', 'is', '<w>', 'short', '<m>', 'interesting', '<m>', 'selective', '<w>', 'and', '<w>', 'fascinating', '<m>',' ']
##        c=['The', ';', 'story', ' ', 'Alice', ' ', 'read', ' ' ,'is', ' ', 'short', ',', 'interesting', ',', 'selective', ',', 'and', ';', 'fascinating', '.',' ']  
##        print(b)
##        print(c)
       
           
    #---------------------------------------------------<m> with semicolon-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==";"):
                if (b[i-1] in quotcrules.onounq) and (b[i+1] in quotcrules.snoun):    
                    hint="Remove the semicolon and put a comma after:"+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in quotcrules.onoun) and (b[i+1]=='"'):    
                    hint="Remove the semicolon and put a comma after:"+ b[i-1]
                    mandlst.append(hint)
                        
                if b[i-1] in quotcrules.snoun and c[i]== ';' and c[i+1]==" ":
                    hint="Remove the semocolon and put a  FUllSTOP after: "+b[i-1]
                    mandlst.append(hint)
                      
                if b[i-1] in quotcrules.snoun and b[i+1]== '"':
                    hint="Remove the semicolon and put a fullstop after:"+ b[i-1]
                    mandlst.append(hint)
         
        #--------------------------------------------adjcommafinal.py-----------------------------------------------------------------
                if b[i-1] in quotcrules.adj and b[i+1] in quotcrules.adj:
                    hint="Remove the semicolon and put a comma after:"+ b[i-1]
                    mandlst.append(hint)
                if b[i-1] in quotcrules.adj and c[-2]==";" and c[i+1]==" ":
                    hint="Remove the semicolon and put a fullstop after:"+ b[i-1]
                    mandlst.append(hint)
                if b[i-1] in quotcrules.onoun and b[i+1] in quotcrules.snoun:  
                    hint="Remove the semicolon and put a comma after:"+ b[i-1]
                    mandlst.append(hint)       
   #---------------------------------------------------<m> with comma-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):
                
                if (b[i-1] in quotcrules.onounq) and (b[i+1] in quotcrules.snoun):    
                    hint="Correct Answer:Comma is used to separate the reported speech and reporting speech. It separates who is saying what"
                    correctlst.append(hint)
                if (b[i-1] in quotcrules.onoun) and (b[i+1]=='"'):    
                    hint="Correct Answer:Comma is used to separate the reported speech and reporting speech. It separates who is saying what"
                    correctlst.append(hint)    
                if b[i -1] in quotcrules.snoun and c[i]==',' and c[i+1]==" ":
                    hint="Remove the comma and put a sentence with FUllSTOP after: "+b[i-1]
                    mandlst.append(hint)
                                            
                if b[i-1] in quotcrules.snoun and b[i+1]== '"':
                    hint="Remove the comma and put a fullstop after:"+ b[i-1]
                    mandlst.append(hint)
            #-------------------------------------------adjcommafinal.py-----------------------------------------------------------------
                if b[i-1] in quotcrules.adj and b[i+1] in quotcrules.adj:
                    hint="Correct Answer:A comma should be used in between the adjectives"
                    correctlst.append(hint)
                if b[i-1] in quotcrules.adj and b[i+1]==" ": 
                    hint="Remove the comma and put a fullstop after:"+ b[i-1]
                    mandlst.append(hint)  
                if b[i-1] in quotcrules.onoun and b[i+1] in quotcrules.snoun:  
                    hint="Correct Answer.Use a Comma After an Introductory Word or Phrase"  
                    correctlst.append(hint)
    #---------------------------------------------------<m> with fullstop-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                if (b[i-1] in quotcrules.onoun) and (b[i+1]=='"'):    
                    hint="Remove the fullstop and put a comma after:"+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in quotcrules.onounq) and (b[i+1] in quotcrules.snoun):    
                    hint="Remove the fullstop and put a comma after:"+ b[i-1]
                    mandlst.append(hint)
                if b[i -1] in quotcrules.snoun and c[i]=='.' and c[i+1]==" ":
                    hint="Correct Answer:End a sentence with FUllSTOP after: "+b[i-1]
                    mandlst.append(hint)
                      
                if b[i-1] in quotcrules.snoun and b[i+1]== '"':
                    hint="Correct Answer:Put a fullstop after the reporting speech[who said to whom], before the ending quotation"
                    correctlst.append(hint)
            #-------------------------------------------adjcommafinal.py-----------------------------------------------------------------
                if b[i-1] in quotcrules.adj and b[i+1] in quotcrules.adj:
                    hint="Remove the fullstop and put a comma after:", b[i-1]
                    mandlst.append(hint)
                if b[i-1] in quotcrules.adj and b[i+1]==" ": 
                    hint="Correct Answer:Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)    
                    
                if b[i-1] in quotcrules.onoun and b[i+1] in quotcrules.snoun:  
                    hint="Remove the fullstop and put a comma after:"+ b[i-1]
                    mandlst.append(hint)   
                         
    #---------------------------------------------------<m> with no punctuation-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==" "):
                if (b[i-1] in quotcrules.onoun) and (b[i+1]=='"'):    
                    hint="put a comma after:"+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in quotcrules.onounq) and (b[i+1] in quotcrules.snoun):    
                    hint="Remove the fullstop and put a comma after:", b[i-1]
                    mandlst.append(hint)
                if b[i -1] in quotcrules.snoun and c[i]==' ' and c[i+1]==" ":
                    hint="Put a  FUllSTOP after: "+b[i-1]
                    mandlst.append(hint)
                      
                if b[i-1] in quotcrules.snoun and b[i+1]== '"':
                    hint="Put a fullstop after:"+ b[i-1]
                    mandlst.append(hint)

          #-------------------------------------------adjcommafinal.py-----------------------------------------------------------------
                if b[i-1] in quotcrules.adj and b[i+1] in quotcrules.adj:
                    hint=" put a comma after:"+ b[i-1]
                    mandlst.append(hint)
                if b[i-1] in quotcrules.onoun and b[i+1] in quotcrules.snoun:  
                    hint="put a comma after:"+ b[i-1]
                    mandlst.append(hint)   
                              
                    
    #---------------------------------------------------<w> with semicolon-----------------------------------------------------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<w>" and c[i]==";"):
                if (b[i-1] in quotcrules.pronounq) and (b[i+1] in quotcrules.vbz):    
                    hint="Remove the semicolon after :" + b[i-1]
                    hintlst.append(hint)
                if (b[i-1] =='"') and (b[i+1] in quotcrules.pronoun1):    
                    hint="Remove the semicolon after the starting quotation "
                    
                    hintlst.append(hint)
                      
                if b[i-1] in quotcrules.vbz and b[i+1] in quotcrules.verb:
                    hint="Remove the semicolon after :" + b[i-1]
                    hintlst.append(hint)

                if b[i-1] in quotcrules.verb and b[i+1] in quotcrules.pronoun:
                    hint="Remove the semicolon after :" + b[i-1]
                    hintlst.append(hint)
                if b[i-1] in quotcrules.pronoun and b[i+1] in quotcrules.onounq:
                    hint="Remove the semicolon after :" + b[i-1]
                    hintlst.append(hint)

               

                if b[i-1] in quotcrules.verb and b[i+1] in quotcrules.prep:
                    hint="Remove the semicolon after :" + b[i-1]
                    hintlst.append(hint)    
                if b[i-1] in quotcrules.prep and b[i+1] in quotcrules.snoun:
                    hint="Remove the semicolon after :" + b[i-1]
                    hintlst.append(hint)

        #----------------------------------adjcomma.py------------------------------------
                if b[i-1] in quotcrules.detcap and b[i+1] in quotcrules.onoun:
                    hint="Remove the semicolon after :" + b[i-1]
                    hintlst.append(hint)
                if b[i-1] in quotcrules.onoun and b[i+1] in quotcrules.snoun:
                    hint="Remove the semicolon after :" + b[i-1]
                    hintlst.append(hint)   
                if b[i-1] in quotcrules.snoun and b[i+1] in quotcrules.verb:
                    hint="Remove the semicolon after :" + b[i-1]
                    hintlst.append(hint)
                if b[i-1] in quotcrules.verb and b[i+1] in quotcrules.vbz:
                    hint="Remove the semicolon after :" + b[i-1]
                    hintlst.append(hint)
               
                if b[i-1] in quotcrules.conj and b[i+1] in quotcrules.adj:
                    hint="Remove the semicolon after :" + b[i-1]
                    hintlst.append(hint)
                if b[i-1] in quotcrules.adj and b[i+1] in quotcrules.conj:
                    hint="Remove the semicolon after :" + b[i-1]
                    hintlst.append(hint)    
    #---------------------------------------------------<w> with fullstop-----------------------------------------------------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<w>" and c[i]=="."):
                if (b[i-1] in quotcrules.pronounq) and (b[i+1] in quotcrules.vbz):    
                    hint="Remove the fullstop after :" + b[i-1]
                    hintlst.append(hint)
                if (b[i-1] =='"') and (b[i+1] in quotcrules.pronoun1):    
                    hint="Remove the fullstop after the starting quotation "
                    hintlst.append(hint)      
                if b[i-1] in quotcrules.vbz and b[i+1] in quotcrules.verb:
                    hint="Remove the fullstop after :" + b[i-1]
                    hintlst.append(hint)

                if b[i-1] in quotcrules.verb and b[i+1] in quotcrules.pronoun:
                    hint="Remove the fullstop after :" + b[i-1]
                    hintlst.append(hint)

                if b[i-1] in quotcrules.pronoun and b[i+1] in quotcrules.onounq:
                    hint="Remove the fullstop after :" + b[i-1]
                    hintlst.append(hint)

                if b[i-1] in quotcrules.snoun and b[i+1] in quotcrules.verb:
                    hint="Remove the fullstop after :" + b[i-1]
                    hintlst.append(hint)

                if b[i-1] in quotcrules.verb and b[i+1] in quotcrules.prep:
                    hint="Remove the fullstop after :" + b[i-1]
                    hintlst.append(hint) 
                if b[i-1] in quotcrules.prep and b[i+1] in quotcrules.snoun:
                    hint="Remove the fullstop after :" + b[i-1]
                    hintlst.append(hint)
                    #----------------------------------adjcomma.py--------------------------------------------------------------------------------
                if b[i-1] in quotcrules.detcap and b[i+1] in quotcrules.onoun:
                    hint="Remove the fullstop after :" + b[i-1]
                    hintlst.append(hint)
                if b[i-1] in quotcrules.onoun and b[i+1] in quotcrules.snoun:
                    hint="Remove the fullstop after :" + b[i-1]
               
                if b[i-1] in quotcrules.verb and b[i+1] in quotcrules.vbz:
                    hint="Remove the fullstop after :" + b[i-1]
                    hintlst.append(hint)
                if b[i-1] in quotcrules.conj and b[i+1] in quotcrules.adj:
                    hint="Remove the fullstop after :" + b[i-1]
                    hintlst.append(hint)  
                if b[i-1] in quotcrules.adj and b[i+1] in quotcrules.conj:
                    hint="Remove the fullstop after :" + b[i-1]
                    hintlst.append(hint)        
#---------------------------------------------------<w> with comma-----------------------------------------------------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<w>" and c[i]==","):
                if (b[i-1] in quotcrules.pronounq) and (b[i+1] in quotcrules.vbz):    
                    hint="Remove the comma after :" + b[i-1]
                    hintlst.append(hint)
                
                if (b[i-1] =='"') and (b[i+1] in quotcrules.pronoun1):    
                    hint="Remove the comma after the starting quotation "
                    hintlst.append(hint)      
                if b[i-1] in quotcrules.vbz and b[i+1] in quotcrules.verb:
                    hint="Remove the comma after :" + b[i-1]
                    hintlst.append(hint)

                if b[i-1] in quotcrules.verb and b[i+1] in quotcrules.pronoun:
                    hint="Remove the comma after :" + b[i-1]
                    hintlst.append(hint)

                if b[i-1] in quotcrules.pronoun and b[i+1] in quotcrules.onounq:
                    hint="Remove the comma after :" + b[i-1]
                    hintlst.append(hint)

                if b[i-1] in quotcrules.snoun and b[i+1] in quotcrules.verb:
                    hint="Remove the comma after :" + b[i-1]
                    hintlst.append(hint)

                if b[i-1] in quotcrules.verb and b[i+1] in quotcrules.prep:
                    hint="Remove the comma after :" + b[i-1]
                    hintlst.append(hint)   
                if b[i-1] in quotcrules.prep and b[i+1] in quotcrules.snoun:
                    hint="Remove the comma after :" + b[i-1]
                    hintlst.append(hint)
            #----------------------------------adjcomma.py------------------------------------
                if b[i-1] in quotcrules.detcap and b[i+1] in quotcrules.onoun:
                    hint="Remove the comma after :" + b[i-1]
                    hintlst.append(hint)
                if b[i-1] in quotcrules.onoun and b[i+1] in quotcrules.snoun:
                    hint="Remove the comma after :" + b[i-1]
                    hintlst.append(hint) 
                
                if b[i-1] in quotcrules.verb and b[i+1] in quotcrules.vbz:
                    hint="Remove the comma after :" + b[i-1]
                    hintlst.append(hint)
                if b[i-1] in quotcrules.conj and b[i+1] in quotcrules.adj:
                    hint="Remove the comma after :" + b[i-1]
                    hintlst.append(hint) 
                if b[i-1] in quotcrules.adj and b[i+1] in quotcrules.conj:
                    hint="Remove the comma after :" + b[i-1]
                    hintlst.append(hint)    
        print(hintlst,mandlst,correctlst,mandatory) 
        return(hintlst,mandlst,correctlst,mandatory)             
##p1=quotcrules()
##hintlst,mandlst,correctlst,mandatory=p1.commaone()
##
##for i in hintlst:
##    print(i)
##for j in mandlst:
##    print(j)
##for k in correctlst:
##    print(k)

                             
                        
