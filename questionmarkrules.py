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
class qmrules:
##    NN = ['Noun']
##    NNS =['Noun-plural']
##    NNP =['Proper noun-singular']
##    RB =['Adverb']
##    VB =['Verb-base form']
##    WP =['Wh-pronoun']
    freqadv=['seldom','hardly']
    cor_conj=['neither','nor','either','or']
    indefenitepro=["Nobody","None"]
    article=['a','an']
    det=['the']
    adj=['confident','adorable','generous','charming','clever','huge','red','small','heavy','beautiful','fantastic','mesmerising','well-defined','hot','cold','warm','strong-flavored','delicious','tasty','mind-blowing','spicy','excellent','lovely','thrilled','elated','difficult','intelligent','rapid-fire','open-ended','lovely','fascinating','short','precise','interesting','selective','magnificent','high-grade','exceptional','focused','ambitious','demanding','competetive','exciting','brilliant','amazing','three-room','luxurious','spacious','own','modern','adorable','favorite','new','worthy','valuable','expensive','precious','limpy','twisted','sprained','fractured','considerate','attractive','amusing','jovial']
    onoun=['box','book','cage','scenary','house','building','tea','water','coffee','biriyani','pulav','kichdi','novel','story','match','race','ankle','leg','first-prize','second-prize','job','position','keys','books','poem','story','furniture','vegetables','fruits','bicycles','bicycle','house','organisation','school','college','flat','question']
    prep=['in','for','with','from','on','to']
    title=['Dr','Prof','Mr','Mrs','Sr','Bro','Major','Capt','Miss']
    beforetitle=['Late']
    snoun=['Mary','James','John','Alice','A. Roy', 'K. Singh', 'R. K. Narayan', 'R. Kushner','Esmail','Bagani']
    snoun1=['idea']
    perspro=['you','me']
    quantifier=['any']
    verb=['late','tell','know','like','lift','stand','answered','won','got','secured','achieved','hurt','lost','opened','closed','cooked','met','read','wrote','drew','drank','paid','bought','stayed','worked','joined','taught','married','dated','intracted','consulted','visited','debated','argued','fought','lived','seperated']
    verbl=[]
    cnoun=["man","gentleman","orator","woman","lady"]
    verbs=['late','tell','know','like','lift','stand','answer','win','get','secure','achieve','hurt','lose','open','close','cook','meet','read','write','draw','drink','pay','buy','stay','work','join','teach','married','date','intract','consult','visit','debate','argue','fight','live','seperate']
    for i in verbs:
        verbl.append(i+"s")
    #print(verbl)    
    verbing=[]
    for i in verbs:
        if i.endswith("e"):
            i=i[:-1]
            verbing.append(i+"ing")
        else:
            verbing.append(i+"ing")
    wqtags=['which','what','why','where']
    wqtagsl=[]
    for i in wqtags:
        wqtagsl.append(i.capitalize())
    article=['a','an']
    det=['the']
    adj=['confident','adorable','generous','charming','clever','huge','red','small','heavy','beautiful','fantastic','mesmerising','well-defined','hot','cold','warm','strong-flavored','delicious','tasty','mind-blowing','spicy','excellent','lovely','thrilled','elated','difficult','intelligent','rapid-fire','open-ended','lovely','fascinating','short','precise','interesting','selective','magnificent','high-grade','exceptional','focused','ambitious','demanding','competetive','exciting','brilliant','amazing','three-room','luxurious','spacious','own','modern','adorable','favorite','new','worthy','valuable','expensive','precious','limpy','twisted','sprained','fractured','considerate','attractive','amusing','jovial']
    onoun=['box','book','cage','scenary','house','building','tea','water','coffee','biriyani','pulav','kichdi','novel','story','match','race','ankle','leg','first-prize','second-prize','job','position','keys','books','poem','story','furniture','vegetables','fruits','bicycles','bicycle','house','organisation','school','college','flat','question']
    prep=['in','for','with','from','on','to']
    title=['Dr','Prof','Mr','Mrs','Sr','Bro','Major','Capt','Miss']
    beforetitle=['Late']
    vbz=['is','has','was']
    hverb=["could","will","would","might","can",'has','had','have',"do","did","does"]
    neghverb=["couldn't","won't","wouldn't","mightn't","can't","hasn't","hadn't","haven't","don't","doesn't","didn't"]
    hverbl=[]
    for i in hverb:
        hverbl.append(i.capitalize())
    hintlst=[]
    correctlst=[]
    mandlst=[]
    pronoun=['his','her','he','she','it','they','you']
    pronoun1=[]
    for i in pronoun:
        pronoun1.append(i.capitalize())
    questionwords=['Do','Did','Does']
    questionwordsl=['do','does','did']
    auxstring=["I'd","I would"] 
    def qmone(b,c,correct,category,level,username,userid,eid,submittedtext):
##    def qmone(self):
        
        mandlst=[]
        correctlst=[]
        hintlst=[]
##        b=['Prof', '<m>', 'John', '<m>', 'an', '<w>', 'adorable', '<w>', 'orator', '<m>', 'would', '<w>', 'open', '<w>', 'a', '<w>', 'small', '<w>', 'box', '<m>', "wouldn't", '<w>', 'he', '<m>']
##        c=['Prof', '.', 'John', ',', 'an', ' ', 'adorable', ' ', 'orator', ',', 'would', ' ', 'open', ' ', 'a', ' ', 'small', ' ', 'box', '.', 'wouldn', ' ', "'", ' ', 't', ' ', 'he', '?']
##        b=['Where', '<w>', 'does', '<w>', 'Mary', '<w>', 'stay', '<m>']
##        c=['Where', '.', 'does', ',', 'Mary', '?', 'stay', '?']
##        b=["I'd", '<w>', 'like', '<w>', 'to', '<w>', 'know','<w>','what','<w>', 'John', '<w>', 'reads', '<m>', ' ']
##        c=["I'd", '.', 'like', '.' , 'to', '.', 'know','.','what', '.', 'John', '.', 'reads','?',' ']        
        b.append(" ")
        c.append(" ")
        print(b)
        print(c)
        ct=0
        for i in b:
            if i=="<m>":
                ct=ct+1
        mandatory=ct    
        mandlst=[]
        correctlst=[]
        hintlst=[]
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==" "):
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs and c[i+1]==" " and c[i]==" ":
                     hint="Read the manual again, Use Questionmark at appropriate locations"
                     mandlst.append(hint)
                if b[i-1] in qmrules.pronoun and c[i+1]==" " and c[i]==" ":
                     
                     hint="Read the manual again, Use Questionmark at appropriate locations"
                     mandlst.append(hint)
                     
                if (b[i-1] in qmrules.title) and (b[i+1] in qmrules.snoun):    
                    hint="Read the manual again, Use fullstop at appropriate locations"
                    mandlst.append(hint) 
                if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.article):    
                    hint="Read the manual again, Use comma at appropriate locations"
                    mandlst.append(hint)  
                if (b[i-1] in qmrules.onoun) and (b[i+1] in qmrules.hverb or b[i+1] in qmrules.neghverb):    
                    hint="Read the manual again, Use comma at appropriate locations"
                    mandlst.append(hint)          
    #--------------------------------------------------<m> with fullstop---------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs and c[i+1]==" " and c[i]==".":
                     hint="Read the manual again, Use Questionmark at appropriate locations"
                     mandlst.append(hint)
                if b[i-1] in qmrules.pronoun and c[i]==".":
                     hint="Read the manual again, Use Questionmark at appropriate locations"
                     mandlst.append(hint)     
                if (b[i-1] in qmrules.title) and (b[i+1] in qmrules.snoun):    
                    hint="Correct Answer:Put a fullstop after the title of a name"
                    correctlst.append(hint) 
                if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.article):    
                    hint="Read the manual again, Use comma at appropriate locations"
                    mandlst.append(hint)   
                if (b[i-1] in qmrules.onoun) and (b[i+1] in qmrules.hverb or b[i+1] in qmrules.neghverb):    
                    hint="Read the manual again, Use comma at appropriate locations"
                    mandlst.append(hint)  
     #--------------------------------------------------<m> with questionmark---------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="?"):
                
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs and c[i+1]==" " and c[i]=="?":
                     
                     hint="Correct Answer, AN indirect question always ends with a question mark"
                     correctlst.append(hint)
                if b[i-1] in qmrules.pronoun and c[i]=="?":
                     
                     hint="Correct Answer, A Question tag always ends with a question mark"
                     correctlst.append(hint)
                if (b[i-1] in qmrules.title) and (b[i+1] in qmrules.snoun):    
                    hint="Read the manual again, Use fullstop at appropriate locations"
                    mandlst.append(hint) 
                if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.article):    
                    hint="Read the manual again, Use comma at appropriate locations"
                    mandlst.append(hint)   
                if (b[i-1] in qmrules.onoun) and (b[i+1] in qmrules.hverb or b[i+1] in qmrules.neghverb):    
                    hint="Read the manual again, Use comma at appropriate locations"
                    mandlst.append(hint)  
                     
      #--------------------------------------------------<m> with comma---------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs and c[i+1]==" " and c[i]=="," :
                     hint="Read the manual again, A question always ends with a question mark"
                     mandlst.append(hint)
               
                if b[i-1] in qmrules.pronoun and c[i]==",":
                     hint="Read the manual again, Use Questionmark at appropriate locations"
                     mandlst.append(hint)     
                if (b[i-1] in qmrules.title) and (b[i+1] in qmrules.snoun):    
                    hint="Read the manual again, Use fullstop at appropriate locations"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.article):    
                    hint="Correct Answer:A comma should be used when a relative clause follows the main subject."
                    correctlst.append(hint)
                if (b[i-1] in qmrules.onoun) and (b[i+1] in qmrules.hverb or b[i+1] in qmrules.neghverb):    
                    hint="Correct Answer: A Comma should be used before a question tag"
                    correctlst.append(hint)  
       
#--------------------------------------------------------<w> with Question MARK-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]=="?"):
                
                hint="Question mark not needed.Click the appropriate sidepane and read the manuals"
                hintlst.append(hint)
                
        
###--------------------------------------------------------<w> with FULLSTOP-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]=="."):
                
                hint="FULLSTOP at incorrect locations.Click the appropriate sidepane and read the manuals"
                hintlst.append(hint)
       
#--------------------------------------------------------<w> with comma-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==","):
                
                hint="comma at incorrect locations.Click the appropriate sidepane and read the manuals"
                hintlst.append(hint)

        return(hintlst,mandlst,correctlst,mandatory)
                
    def qmtwo(b,c,correct,category,level,username,userid,eid,submittedtext):
    #def qmtwo(self):    
        mandlst=[]
        correctlst=[]
        hintlst=[]
##        b=['Where', '<w>', 'does', '<w>', 'Mary', '<w>', 'stay', '<m>']
##        c=['Where', '?', 'does', ',', 'Mary', ',', 'stay', '?']
##        b=["I'd", '<w>', 'like', '<w>', 'to', '<w>', 'know','<w>','what','<w>', 'John', '<w>', 'reads', '<m>', ' ']
##        c=["I'd", '.', 'like', '.' , 'to', '.', 'know','.','what', '.', 'John', '.', 'reads','?',' ']        
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
##        print(b)
##        print(c)
##        nounlst=[]
##        snoun = [token for token, pos in pos_tag(c) if pos.startswith('NNP')]
##        nouns = [token for token, pos in pos_tag(c) if pos.startswith('NN')]
##        perspro=[token for token, pos in pos_tag(c) if pos.startswith('PRP')]
##        verbs=[token for token, pos in pos_tag(c) if pos.startswith('VB')]
##        wqtags=[token for token, pos in pos_tag(c) if pos.startswith('WP')]
##        print(snoun,nouns,perspro,verbs,wqtags)
##        
##        
                 
##                    
##                        
##                if dh[0]=="NNP":
##                    snoun.append(dh[1])
##                if dh[0]=="PRP":
##                    perspro.append(dh[1])
##                if dh[0]=="VB":
##                    verbs.append(dh[1])    
##                if dh[0]=="WP":
##                    wqtags.append(dh[1])      
        
     #--------------------------------------------------<m> with no punctuation--------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==" ") :
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs:
                     hint="Read the manual again, Use Questionmark at appropriate locations"
                     mandlst.append(hint)
                if b[i-1] in qmrules.pronoun and c[i+1]==" ":
                     
                     hint="InCorrect Answer, Hint:A Question tag always ends with a question mark"
                     mandlst.append(hint)    
                
                if (b[i-1] in qmrules.title) and (b[i+1] in qmrules.snoun):    
                    hint="Incorrect:Hint:Always put a fullstop after the title"
                    mandlst.append(hint) 
                if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.article):    
                    hint="Incorrect:Hint:A comma should be used when a relative clause follows the main subject."
                    mandlst.append(hint)   
                if (b[i-1] in qmrules.onoun) and (b[i+1] in qmrules.hverb or b[i+1] in qmrules.neghverb):    
                    hint="Incorrect:Hint:A Comma should be used before a question tag"
                    mandlst.append(hint)       
    #--------------------------------------------------<m> with fullstop---------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs or b[i-1] in qmrules.pronoun:
                     hint="Read the manual again, Use Questionmark to indiacte a question"
                     mandlst.append(hint)
                if (b[i-1] in qmrules.title) and (b[i+1] in qmrules.snoun):    
                    hint="correct:Hint:Always put a fullstop after the title"
                    correctlst.append(hint) 
                if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.article):    
                    hint="Incorrect:Hint:A comma should be used when a relative clause follows the main subject."
                    mandlst.append(hint)   
                if (b[i-1] in qmrules.onoun) and (b[i+1] in qmrules.hverb or b[i+1] in qmrules.neghverb):    
                    hint="Incorrect:Hint:A Comma should be used before a question tag"
                    mandlst.append(hint)
                if b[i-1] in qmrules.pronoun and c[i]==".":
                     
                     hint="InCorrect Answer, Hint:A Question tag always ends with a question mark"
                     mandlst.append(hint)    
                
     #--------------------------------------------------<m> with questionmark---------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="?"):
                
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs:
                     
                     hint="Correct Answer, AN indirect question always ends with a question mark"
                     correctlst.append(hint)
                if b[i-1] in qmrules.pronoun and c[i]=="?":
                     
                     hint="Correct Answer, A Question tag always ends with a question mark"
                     correctlst.append(hint)
                if (b[i-1] in qmrules.title) and (b[i+1] in qmrules.snoun):    
                    hint="Incorrect:Hint:Always put a fullstop after the title"
                    mandlst.append(hint) 
                if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.article):    
                    hint="Incorrect:Hint:A comma should be used when a relative clause follows the main subject."
                    mandlst.append(hint)   
                if (b[i-1] in qmrules.onoun) and (b[i+1] in qmrules.hverb or b[i+1] in qmrules.neghverb):    
                    hint="Incorrect:Hint:A Comma should be used before a question tag"
                    mandlst.append(hint)      

                     
      #--------------------------------------------------<m> with comma---------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs :
                     hint="Read the manual again, Use Questionmark to indiacte a question"
                     mandlst.append(hint)
                if b[i-1] in qmrules.pronoun and c[i]==",":
                     
                     hint="InCorrect Answer, Hint:A Question tag always ends with a question mark"
                     mandlst.append(hint)    
                
                if (b[i-1] in qmrules.title) and (b[i+1] in qmrules.snoun):    
                    hint="Incorrect:Hint:Always put a fullstop after a title"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.article):    
                    hint="Correct Answer:A comma should be used when a relative clause follows the main subject."
                    correctlst.append(hint)
                if (b[i-1] in qmrules.onoun) and (b[i+1] in qmrules.hverb or b[i+1] in qmrules.neghverb):    
                    hint="Correct Answer: A Comma should be used before a question tag"
                    correctlst.append(hint)  

                     
    #---------------------------------------------------<w> with fullstop-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<w>" and c[i]=="."):
                if (b[i-1] in qmrules.questionwords) and (b[i+1] in qmrules.perspro):
                    
                    hint="Read the manual again, HINT:No need of any punctuation between a Question tag like[Do/Does/Did] and personal pronoun"
                    mandlst.append(hint)
                            
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.verbl):    
                    hint="Read the manual again, HINT:No need of any punctuation between a personal pronoun like [you/he/she] and a verb"
                    mandlst.append(hint)
                    
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs and b[i+1] in qmrules.wqtags:
                     hint="Read the manual again, HINT:No need of any punctuation between a verb and a questiontag like what/where etc."
                     mandlst.append(hint)      
                
                   
                if b[i-1] in qmrules.auxstring and b[i+1] in qmrules.verb:
                     hint="Read the manual again, HINT:No need of any punctuation between a auxiliary string like [I would/I'd] and the verb"
                     mandlst.append(hint)
                if b[i-1] in qmrules.verb and b[i+1] in qmrules.prep:
                     hint="Read the manual again, HINT:No need of any punctuation between a verb and prep"
                     mandlst.append(hint)
                if b[i-1] in qmrules.prep and b[i+1] in qmrules.verb:
                     hint="Read the manual again, HINT:No need of any punctuation between a prep and a verb"
                     mandlst.append(hint)     
                if b[i-1] in qmrules.verb and b[i+1] in qmrules.wqtags:
                     hint="Read the manual again, HINT:No need of any punctuation between a verb and questiontag like what/where etc."
                     mandlst.append(hint)
                if b[i-1] in qmrules.wqtags and b[i+1] in qmrules.snoun:
                     
                     hint="Read the manual again, HINT:No need of any punctuation between a questiontag like what/where etc. and a noun"
                     mandlst.append(hint)
                
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.hverb):    
                    hint="Read the manual again, HINT:No need of any punctuation between a personal pronoun like [you/he/she] and a helping verb like[has\has\have]"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.hverb) and (b[i+1] in qmrules.quantifier):    
                    hint="Read the manual again, HINT:No need of any punctuation after a helping verb like [has\had\have]"
                    mandlst.append(hint)
                if (b[i-1]in qmrules.quantifier) and (b[i+1] in qmrules.snoun1):    
                    hint="Read the manual again, HINT:No need to seperate an entity(quantifier+object) with a punctuation"
                    mandlst.append(hint)
                if (b[i-1] =="idea") and (b[i+1] in qmrules.wqtags):    
                    hint="Read the manual again, HINT:No need to seperate a noun/subject and a W-question"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.hverbl) and (b[i+1] in qmrules.perspro):    
                    hint="Read the manual again, HINT:No need of any punctuation between a Questiontag and a personal pronoun like [you/he/she]"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.verb):    
                    hint="Read the manual again, HINT:No need of any punctuation between a personal pronoun like [you/he/she] and a verb"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.verb) and (b[i+1] in qmrules.perspro):    
                    hint="Read the manual again, HINT:No need of any punctuation between a verb and a personal pronoun like [you/he/she/me/I]"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.wqtags):    
                    hint="Read the manual again, HINT:No need of any punctuation between a personal pronoun like [you/he/she/me/I] and a W-question"
                    mandlst.append(hint)
                if b[i-1] in qmrules.wqtagsl  and (b[i+1] in qmrules.questionwordsl):
                    hint="Read the manual again, HINT:No need of any punctuation after a Wh question"
                    mandlst.append(hint)
##                if b[i-1] in qmrules.questionwordsl  and (b[i+1] in qmrules.snoun) :
##                    hint="Read the manual again, HINT:No need of any punctuation after [do/does/did]..It interruots the continuity"
##                    mandlst.append(hint)
                if b[i-1] in qmrules.snoun  and b[i+1] in qmrules.verbl :
                    
                    hint="Read the manual again, HINT:No need of any punctuation between a noun and a verb"
                    mandlst.append(hint)
                
##                     #--------------type5.py----------------------------------
                if b[i-1] in qmrules.adj and b[i+1] in qmrules.cnoun:
                    hint="Read the manual again, HINT:No need of any punctuation between a adjective and a common noun"
                    mandlst.append(hint)

                if b[i-1] in qmrules.adj and b[i+1] in qmrules.onoun:
                   hint="Read the manual again, HINT:No need of any punctuation between a adjective and a object noun"
                   mandlst.append(hint)   
                if b[i-1] in qmrules. hverb and b[i+1] in qmrules.verb:
                   hint="Read the manual again, HINT:No need of any punctuation between a helping verb and a verb"
                   mandlst.append(hint)
                if b[i-1] in qmrules.article and b[i+1] in qmrules.adj:
                   hint="Read the manual again, HINT:No need of any punctuation between a article and an adj"
                   mandlst.append(hint)
                 
                if b[i-1] in qmrules.verb or b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs or b[i-1] in qmrules.verbs and b[i+1] in qmrules.article:
                   hint="Read the manual again, HINT:No need of any punctuation between a verb and an article"
                   mandlst.append(hint)
                
                
                if b[i-1] in qmrules.neghverb or b[i-1] in qmrules.hverb and b[i+1] in qmrules.pronoun:
                   hint="Read the manual again, HINT:No need of any punctuation between a helpingverb and a pronoun" 
                   mandlst.append(hint)

                if (b[i-1] in qmrules.pronoun1) and (b[i+1] in qmrules.freqadv):    
                    hint="Read the manual again, HINT:No need of any punctuation between a pronoun like [you/he/she] and frequency adverbs like[hardly/seldom]"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.freqadv) and (b[i+1] in qmrules.verbs or b[i+1] in qmrules.verbl):    
                    hint="Read the manual again, HINT:No need of any punctuation between frequency adverbs like[hardly/seldom] and a verb"
                    mandlst.append(hint)
                if b[i-1] in qmrules.indefenitepro and b[i+1] in qmrules.prep:#---None of them likes to draw
                   hint="Read the manual again, HINT:No need of any punctuation between an indefenite pronoun like[Nobody/None] and preposition"
                   mandlst.append(hint)
                if b[i-1] in qmrules.prep and b[i+1] in qmrules.pronoun:
                   hint="Read the manual again, HINT:No need of any punctuation between a preposition and a pronoun"
                   mandlst.append(hint)
                if b[i-1] in qmrules.pronoun and b[i+1] in qmrules.verbl:
                   hint="Read the manual again, HINT:No need of any punctuation between a pronoun and a verb"
                   mandlst.append(hint)
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbl and b[i+1] in qmrules.prep:
                   hint="Read the manual again, HINT:No need of any punctuation between a verb and preposition"
                   mandlst.append(hint)
                if b[i-1] in qmrules.prep and b[i+1] in qmrules.verbs or b[i+1] in qmrules.verbl:
                   hint="Read the manual again, HINT:No need of any punctuation between a preposition and a verb"
                   mandlst.append(hint)
                if b[i-1] in qmrules.cor_conj and b[i+1] in qmrules.snoun:
                   hint="Read the manual again, HINT:No need of any punctuation between coorelative conjunctions like [neither..nor,either..or] and a noun"
                   mandlst.append(hint)
              
                if b[i-1] in qmrules.snoun and b[i+1] in qmrules.cor_conj:
                   hint="Read the manual again, HINT:No need of any punctuation between a noun and a coorelative conjunctions like [neither..nor,either..or]"
                   mandlst.append(hint)
                if b[i-1] in qmrules.snoun  and b[i+1] in qmrules.verbs:
                    
                    hint="Read the manual again, HINT:No need of any punctuation between a noun and a verb"
                    mandlst.append(hint)
    
                  
##                    
## #---------------------------------------------------<w> with comma-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<w>" and c[i]==","):
                if (b[i-1] in qmrules.questionwords) and (b[i+1] in qmrules.perspro):
                    
                    hint="Read the manual again, HINT:No need of any punctuation between a Question tag like[Do/Does/Did] and personal pronoun"
                    mandlst.append(hint)
                            
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.verbl):    
                    hint="Read the manual again, HINT:No need of any punctuation between a personal pronoun like [you/he/she] and a verb"
                    mandlst.append(hint)
                    
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs and b[i+1] in qmrules.wqtags:
                     hint="Read the manual again, HINT:No need of any punctuation between a verb and a questiontag like what/where etc."
                     mandlst.append(hint)      
                
                   
                if b[i-1] in qmrules.auxstring and b[i+1] in qmrules.verb:
                     hint="Read the manual again, HINT:No need of any punctuation between a auxiliary string like [I would/I'd] and the verb"
                     mandlst.append(hint)
                if b[i-1] in qmrules.verb and b[i+1] in qmrules.prep:
                     hint="Read the manual again, HINT:No need of any punctuation between a verb and prep"
                     mandlst.append(hint)
                if b[i-1] in qmrules.prep and b[i+1] in qmrules.verb:
                     hint="Read the manual again, HINT:No need of any punctuation between a prep and a verb"
                     mandlst.append(hint)     
                if b[i-1] in qmrules.verb and b[i+1] in qmrules.wqtags:
                     hint="Read the manual again, HINT:No need of any punctuation between a verb and questiontag like what/where etc."
                     mandlst.append(hint)
                if b[i-1] in qmrules.wqtags and b[i+1] in qmrules.snoun:
                     
                     hint="Read the manual again, HINT:No need of any punctuation between a questiontag like what/where etc. and a noun"
                     mandlst.append(hint)
                
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.hverb):    
                    hint="Read the manual again, HINT:No need of any punctuation between a personal pronoun like [you/he/she] and a helping verb like[has\has\have]"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.hverb) and (b[i+1] in qmrules.quantifier):    
                    hint="Read the manual again, HINT:No need of any punctuation after a helping verb like [has\had\have]"
                    mandlst.append(hint)
                if (b[i-1]in qmrules.quantifier) and (b[i+1] in qmrules.snoun1):    
                    hint="Read the manual again, HINT:No need to seperate an entity(quantifier+object) with a punctuation"
                    mandlst.append(hint)
                if (b[i-1] =="idea") and (b[i+1] in qmrules.wqtags):    
                    hint="Read the manual again, HINT:No need to seperate a noun/subject and a W-question"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.hverbl) and (b[i+1] in qmrules.perspro):    
                    hint="Read the manual again, HINT:No need of any punctuation between a Questiontag and a personal pronoun like [you/he/she]"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.verb):    
                    hint="Read the manual again, HINT:No need of any punctuation between a personal pronoun like [you/he/she] and a verb"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.verb) and (b[i+1] in qmrules.perspro):    
                    hint="Read the manual again, HINT:No need of any punctuation between a verb and a personal pronoun like [you/he/she/me/I]"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.wqtags):    
                    hint="Read the manual again, HINT:No need of any punctuation between a personal pronoun like [you/he/she/me/I] and a W-question"
                    mandlst.append(hint)
                if b[i-1] in qmrules.wqtagsl  and (b[i+1] in qmrules.questionwordsl):
                    hint="Read the manual again, HINT:No need of any punctuation after a Wh question"
                    mandlst.append(hint)
                if b[i-1] in qmrules.questionwordsl  and (b[i+1] in qmrules.snoun) :
                    hint="Read the manual again, HINT:No need of any punctuation after [do/does/did]..It interruots the continuity"
                    mandlst.append(hint)
                if b[i-1] in qmrules.snoun  and b[i+1] in qmrules.verbl :
                    
                    hint="Read the manual again, HINT:No need of any punctuation between a noun and a verb"
                    mandlst.append(hint)
                     #--------------type5.py----------------------------------
                if b[i-1] in qmrules.adj and b[i+1] in qmrules.cnoun:
                    hint="Read the manual again, HINT:No need of any punctuation between a adjective and a common noun"
                    mandlst.append(hint)

                if b[i-1] in qmrules.adj and b[i+1] in qmrules.onoun:
                   hint="Read the manual again, HINT:No need of any punctuation between a adjective and a object noun"
                   mandlst.append(hint)   
                if b[i-1] in qmrules. hverb and b[i+1] in qmrules.verb:
                   hint="Read the manual again, HINT:No need of any punctuation between a helping verb and a verb"
                   mandlst.append(hint)
                if b[i-1] in qmrules.article and b[i+1] in qmrules.adj:
                   hint="Read the manual again, HINT:No need of any punctuation between a article and an adj"
                   mandlst.append(hint)
                 
                if b[i-1] in qmrules.verb or b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs and b[i+1] in qmrules.article:
                   hint="Read the manual again, HINT:No need of any punctuation between a verb and an article"
                   mandlst.append(hint)
                
                if b[i-1] in qmrules.neghverb or b[i-1] in qmrules.hverb and b[i+1] in qmrules.pronoun:
                   hint="Read the manual again, HINT:No need of any punctuation between a helpingverb and a pronoun" 
                   mandlst.append(hint)
                if (b[i-1] in qmrules.pronoun1) and (b[i+1] in qmrules.freqadv):    
                    hint="Read the manual again, HINT:No need of any punctuation between a pronoun like [you/he/she] and frequency adverbs like[hardly/seldom]"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.freqadv) and (b[i+1] in qmrules.verbs or b[i+1] in qmrules.verbl):    
                    hint="Read the manual again, HINT:No need of any punctuation between frequency adverbs like[hardly/seldom] and a verb"
                    mandlst.append(hint)
                if b[i-1] in qmrules.indefenitepro and b[i+1] in qmrules.prep:#---None of them likes to draw
                   hint="Read the manual again, HINT:No need of any punctuation between an indefenite pronoun like[Nobody/None] and preposition"
                   mandlst.append(hint)
                if b[i-1] in qmrules.prep and b[i+1] in qmrules.pronoun:
                   hint="Read the manual again, HINT:No need of any punctuation between a preposition and a pronoun"
                   mandlst.append(hint)
                if b[i-1] in qmrules.pronoun and b[i+1] in qmrules.verbl:
                   hint="Read the manual again, HINT:No need of any punctuation between a pronoun and a verb"
                   mandlst.append(hint)
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs and b[i+1] in qmrules.prep:
                   hint="Read the manual again, HINT:No need of any punctuation between a verb and preposition"
                   mandlst.append(hint)
                if b[i-1] in qmrules.prep and b[i+1] in qmrules.verbs or b[i+1] in qmrules.verbl:
                   hint="Read the manual again, HINT:No need of any punctuation between a preposition and a verb"
                   mandlst.append(hint)
                if b[i-1] in qmrules.cor_conj and b[i+1] in qmrules.snoun:
                   hint="Read the manual again, HINT:No need of any punctuation between coorelative conjunctions like [neither..nor,either..or] and a noun"
                   mandlst.append(hint)
              
                if b[i-1] in qmrules.snoun and b[i+1] in qmrules.cor_conj:
                   hint="Read the manual again, HINT:No need of any punctuation between a noun and a coorelative conjunctions like [neither..nor,either..or]"
                   mandlst.append(hint)
                if b[i-1] in qmrules.snoun  and b[i+1] in qmrules.verbs:
                    
                    hint="Read the manual again, HINT:No need of any punctuation between a noun and a verb"
                    mandlst.append(hint)
    
## #---------------------------------------------------<w> with questionmark-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<w>" and c[i]==","):
                     #--------------type5.py----------------------------------
                if b[i-1] in qmrules.adj and b[i+1] in qmrules.cnoun:
                    hint="Read the manual again, HINT:No need of any punctuation between a adjective and a common noun"
                    mandlst.append(hint)

                if b[i-1] in qmrules.adj and b[i+1] in qmrules.onoun:
                   hint="Read the manual again, HINT:No need of any punctuation between a adjective and a object noun"
                   mandlst.append(hint)   
                if b[i-1] in qmrules. hverb and b[i+1] in qmrules.verb:
                   hint="Read the manual again, HINT:No need of any punctuation between a helping verb and a verb"
                   mandlst.append(hint)
                if b[i-1] in qmrules.article and b[i+1] in qmrules.adj:
                   hint="Read the manual again, HINT:No need of any punctuation between a article and an adj"
                   mandlst.append(hint)
                 
                if b[i-1] in qmrules.verb or b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs and b[i+1] in qmrules.article:
                   hint="Read the manual again, HINT:No need of any punctuation between a verb and an article"
                   mandlst.append(hint)
                
                
                if b[i-1] in qmrules.neghverb or b[i-1] in qmrules.hverb and b[i+1] in qmrules.pronoun:
                   hint="Read the manual again, HINT:No need of any punctuation between a helpingverb and a pronoun "
                   mandlst.append(hint)
##--------------------------------
                if (b[i-1] in qmrules.questionwords) and (b[i+1] in qmrules.perspro):
                    
                    hint="Read the manual again, HINT:No need of any punctuation between a Question tag like[Do/Does/Did] and personal pronoun"
                    mandlst.append(hint)
                            
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.verbl):    
                    hint="Read the manual again, HINT:No need of any punctuation between a personal pronoun like [you/he/she] and a verb"
                    mandlst.append(hint)
                    
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs and b[i+1] in qmrules.wqtags:
                     hint="Read the manual again, HINT:No need of any punctuation between a verb and a questiontag like what/where etc."
                     mandlst.append(hint)      
                
                   
                if b[i-1] in qmrules.auxstring and b[i+1] in qmrules.verb:
                     hint="Read the manual again, HINT:No need of any punctuation between a auxiliary string like [I would/I'd] and the verb"
                     mandlst.append(hint)
                if b[i-1] in qmrules.verb and b[i+1] in qmrules.prep:
                     hint="Read the manual again, HINT:No need of any punctuation between a verb and prep"
                     mandlst.append(hint)
                if b[i-1] in qmrules.prep and b[i+1] in qmrules.verb:
                     hint="Read the manual again, HINT:No need of any punctuation between a prep and a verb"
                     mandlst.append(hint)     
                if b[i-1] in qmrules.verb and b[i+1] in qmrules.wqtags:
                     hint="Read the manual again, HINT:No need of any punctuation between a verb and questiontag like what/where etc."
                     mandlst.append(hint)
                if b[i-1] in qmrules.wqtags and b[i+1] in qmrules.snoun:
                     
                     hint="Read the manual again, HINT:No need of any punctuation between a questiontag like what/where etc. and a noun"
                     mandlst.append(hint)
                
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.hverb):    
                    hint="Read the manual again, HINT:No need of any punctuation between a personal pronoun like [you/he/she] and a helping verb like[has\has\have]"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.hverb) and (b[i+1] in qmrules.quantifier):    
                    hint="Read the manual again, HINT:No need of any punctuation after a helping verb like [has\had\have]"
                    mandlst.append(hint)
                if (b[i-1]in qmrules.quantifier) and (b[i+1] in qmrules.snoun1):    
                    hint="Read the manual again, HINT:No need to seperate an entity(quantifier+object) with a punctuation"
                    mandlst.append(hint)
                if (b[i-1] =="idea") and (b[i+1] in qmrules.wqtags):    
                    hint="Read the manual again, HINT:No need to seperate a noun/subject and a W-question"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.hverbl) and (b[i+1] in qmrules.perspro):    
                    hint="Read the manual again, HINT:No need of any punctuation between a Questiontag and a personal pronoun like [you/he/she]"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.verb):    
                    hint="Read the manual again, HINT:No need of any punctuation between a personal pronoun like [you/he/she] and a verb"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.verb) and (b[i+1] in qmrules.perspro):    
                    hint="Read the manual again, HINT:No need of any punctuation between a verb and a personal pronoun like [you/he/she/me/I]"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.wqtags):    
                    hint="Read the manual again, HINT:No need of any punctuation between a personal pronoun like [you/he/she/me/I] and a W-question"
                    mandlst.append(hint)
                if b[i-1] in qmrules.wqtagsl  and (b[i+1] in qmrules.questionwordsl):
                    hint="Read the manual again, HINT:No need of any punctuation after a Wh question"
                    mandlst.append(hint)
                if b[i-1] in qmrules.questionwordsl  and (b[i+1] in qmrules.snoun) :
                    hint="Read the manual again, HINT:No need of any punctuation after [do/does/did]..It interruots the continuity"
                    mandlst.append(hint)
                if b[i-1] in qmrules.snoun  and b[i+1] in qmrules.verbl :
                    
                    hint="Read the manual again, HINT:No need of any punctuation between a noun and a verb"
                    mandlst.append(hint)
               
                if (b[i-1] in qmrules.pronoun1) and (b[i+1] in qmrules.freqadv):    
                    hint="Read the manual again, HINT:No need of any punctuation between a pronoun like [you/he/she] and frequency adverbs like[hardly/seldom]"
                    mandlst.append(hint)
                if (b[i-1] in qmrules.freqadv) and (b[i+1] in qmrules.verbs or b[i+1] in qmrules.verbl):    
                    hint="Read the manual again, HINT:No need of any punctuation between frequency adverbs like[hardly/seldom] and a verb"
                    mandlst.append(hint)
                if b[i-1] in qmrules.indefenitepro and b[i+1] in qmrules.prep:#---None of them likes to draw
                   hint="Read the manual again, HINT:No need of any punctuation between an indefenite pronoun like[Nobody/None] and preposition"
                   mandlst.append(hint)
                if b[i-1] in qmrules.prep and b[i+1] in qmrules.pronoun:
                   hint="Read the manual again, HINT:No need of any punctuation between a preposition and a pronoun"
                   mandlst.append(hint)
                if b[i-1] in qmrules.pronoun and b[i+1] in qmrules.verbl:
                   hint="Read the manual again, HINT:No need of any punctuation between a pronoun and a verb"
                   mandlst.append(hint)
                if b[i-1] in qmrules.verbs or b[i-1] in qmrules.verbl and b[i+1] in qmrules.prep:
                   hint="Read the manual again, HINT:No need of any punctuation between a verb and preposition"
                   mandlst.append(hint)
                if b[i-1] in qmrules.prep and b[i+1] in qmrules.verbs or b[i+1] in qmrules.verbl:
                   hint="Read the manual again, HINT:No need of any punctuation between a preposition and a verb"
                   mandlst.append(hint)
                if b[i-1] in qmrules.cor_conj and b[i+1] in qmrules.snoun:
                   hint="Read the manual again, HINT:No need of any punctuation between coorelative conjunctions like [neither..nor,either..or] and a noun"
                   mandlst.append(hint)
              
                if b[i-1] in qmrules.snoun and b[i+1] in qmrules.cor_conj:
                   hint="Read the manual again, HINT:No need of any punctuation between a noun and a coorelative conjunctions like [neither..nor,either..or]"
                   mandlst.append(hint)
                if b[i-1] in qmrules.snoun  and b[i+1] in qmrules.verbs:
                    
                    hint="Read the manual again, HINT:No need of any punctuation between a noun and a verb"
                    mandlst.append(hint)


                    
        return(hintlst,mandlst,correctlst,mandatory)
    def qmthree(b,c,correct,category,level,username,userid,eid,submittedtext):
    #def qmthree(self):    
        mandlst=[]
        correctlst=[]
        hintlst=[]
##        b=['Where', '<w>', 'does', '<w>', 'Mary', '<w>', 'stay', '<m>']
##        c=['Where', '?', 'does', ',', 'Mary', ',', 'stay', '?']
##        b=['Sr', '<m>', 'Mary', '<m>' , 'a', '<w>', 'charming', '<w>', 'gentleman', '<m>', "couldn't", '<w>', 'open', '<w>', 'a', '<w>', 'huge', '<w>', 'cage', '<m>', 'could', '<w>', 'she', '<m>']
##        c=['Sr', '.', 'Mary', '.', 'a', '?', 'charming', '?', 'gentleman', ' ', "couldn't", '?', 'open', '?', 'a','?', 'huge', '?','cage', ' ', 'could', '?', 'she', '?']

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
##        print(b)
##        print(c)
##        nounlst=[]
##        snoun = [token for token, pos in pos_tag(c) if pos.startswith('NNP')]
##        nouns = [token for token, pos in pos_tag(c) if pos.startswith('NN')]
##        perspro=[token for token, pos in pos_tag(c) if pos.startswith('PRP')]
##        verbs=[token for token, pos in pos_tag(c) if pos.startswith('VB')]
##        wqtags=[token for token, pos in pos_tag(c) if pos.startswith('WP')]
##        print(snoun,nouns,perspro,verbs,wqtags)
##        
##        
                 
##                    
##                        
##                if dh[0]=="NNP":
##                    snoun.append(dh[1])
##                if dh[0]=="PRP":
##                    perspro.append(dh[1])
##                if dh[0]=="VB":
##                    verbs.append(dh[1])    
##                if dh[0]=="WP":
##                    wqtags.append(dh[1])      
        
     #--------------------------------------------------<m> with no punctuation--------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==" "):
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs:
                     hint="Put a mandatory questionmark after:" +b[i-1]
                     mandlst.append(hint)
                if b[i-1] in qmrules.pronoun and c[i+1]==" ":
                     hint="Put a mandatory questionmark after:" +b[i-1]
                     mandlst.append(hint)
                if (b[i-1] in qmrules.title) and (b[i+1] in qmrules.snoun):    
                    hint="put a fullstop after:" +b[i-1]
                    mandlst.append(hint) 
                if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.article):    
                    hint="put a comma after:" +b[i-1]
                    mandlst.append(hint)   
                if (b[i-1] in qmrules.onoun) and (b[i+1] in qmrules.hverb or b[i+1] in qmrules.neghverb):    
                    hint="put a comma after:" +b[i-1]
                    mandlst.append(hint)       
    #--------------------------------------------------<m> with fullstop---------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs:
                     hint="Remove the fullstop and put a questionmark after:" +b[i-1]
                     mandlst.append(hint)
                if b[i-1] in qmrules.pronoun and c[i]=="." and c[i+1]==" ":
                     hint="Put a mandatory questionmark after:" +b[i-1]
                     mandlst.append(hint)

                if (b[i-1] in qmrules.title) and (b[i+1] in qmrules.snoun):    
                    hint="Correct Answer: FUllstop after a title"
                    correctlst.append(hint) 
                if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.article):    
                    hint="Remove the fullstop and put a comma after:" +b[i-1]
                    mandlst.append(hint)   
                if (b[i-1] in qmrules.onoun) and (b[i+1] in qmrules.hverb or b[i+1] in qmrules.neghverb):    
                    hint="Remove the fullstop and put a comma after:" +b[i-1]
                    mandlst.append(hint)      
     #--------------------------------------------------<m> with questionmark---------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="?"):
                
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs:
                     
                     hint="Correct Answer, AN indirect question always ends with a question mark"
                     correctlst.append(hint)
                if b[i-1] in qmrules.pronoun and c[i]=="?" and c[i+1]==" ":
                     print(b[i-1],b[i+1],"hghggj")
                     hint="Correct Answer, A Question tag always ends with a question mark"
                     correctlst.append(hint)
                if b[i-1]=="they" and c[i]=="?" and c[i+1]==" ":
                     print(b[i-1],b[i+1],"hghggj")
                     hint="Correct Answer, A Question tag always ends with a question mark"
                     correctlst.append(hint)     
                if (b[i-1] in qmrules.title) and (b[i+1] in qmrules.snoun):    
                    hint="Remove the questionmark and put a fullstop after:" +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.article):    
                    hint="Remove the questionmark and Put a Comma after--"+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.onoun) and (b[i+1] in qmrules.hverb or b[i+1] in qmrules.neghverb):    
                    hint="Remove the questionamrk and put a comma after:" +b[i-1]
                    mandlst.append(hint)     
      #--------------------------------------------------<m> with comma---------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs :
                     hint="Remove the comma and put a questionmark after:" +b[i-1]
                     mandlst.append(hint)
                if b[i-1] in qmrules.pronoun and c[i]==",":
                     hint="PRemove the comma and put a questionmark after:" +b[i-1]
                     mandlst.append(hint) 
                if (b[i-1] in qmrules.title) and (b[i+1] in qmrules.snoun):    
                    hint="Remove the comma and put a fullstop after:" +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.snoun) and (b[i+1] in qmrules.article):    
                    hint="Correct Answer:A comma should be used when a relative clause follows the main subject."
                    correctlst.append(hint)
                if (b[i-1] in qmrules.onoun) and (b[i+1] in qmrules.hverb or b[i+1] in qmrules.neghverb):    
                    hint="Correct Answer: A Comma should be used before a question tag"
                    correctlst.append(hint)     
    #---------------------------------------------------<w> with fullstop-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<w>" and c[i]=="."):
                if (b[i-1] in qmrules.questionwords) and (b[i+1] in qmrules.perspro):
                    
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)
                            
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.verbl):    
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)
                    
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs and b[i+1] in qmrules.wqtags:
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)      
                
                   
                if b[i-1] in qmrules.auxstring and b[i+1] in qmrules.verb:
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)
                if b[i-1] in qmrules.verb and b[i+1] in qmrules.prep:
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)
                if b[i-1] in qmrules.prep and b[i+1] in qmrules.verb:
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)     
                if b[i-1] in qmrules.verb and b[i+1] in qmrules.wqtags:
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)
                if b[i-1] in qmrules.wqtags and b[i+1] in qmrules.snoun:
                     
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)
                
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.hverb):    
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.hverb) and (b[i+1] in qmrules.quantifier):    
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1]in qmrules.quantifier) and (b[i+1] in qmrules.snoun1):    
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.snoun1) and (b[i+1] in qmrules.wqtags):    
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.hverbl) and (b[i+1] in qmrules.perspro):    
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.verb):    
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.verb) and (b[i+1] in qmrules.perspro):    
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.wqtags):    
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)
                if b[i-1] in qmrules.wqtagsl  and (b[i+1] in qmrules.questionwordsl):
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)
                if b[i-1] in qmrules.questionwordsl  and (b[i+1] in qmrules.snoun) :
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)
                if b[i-1] in qmrules.snoun  and b[i+1] in qmrules.verbl :
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)
##                                  #--------------type5.py----------------------------------
                if b[i-1] in qmrules.adj and b[i+1] in qmrules.cnoun:
                   hint="Remove the fullstop after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.adj and b[i+1] in qmrules.onoun:
                   hint="Remove the fullstop after: "+b[i-1] 
                   hintlst.append(hint)   
                if b[i-1] in qmrules. hverb and b[i+1] in qmrules.verb:
                   hint="Remove the fullstop after: "+b[i-1]
                   hintlst.append(hint)
                
                if b[i-1] in qmrules.article and b[i+1] in qmrules.adj:
                   hint="Remove the fullstop after: "+b[i-1]
                   hintlst.append(hint)
                 
                if b[i-1] in qmrules.verb or b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs and b[i+1] in qmrules.article:
                   hint="Remove the fullstop after: "+b[i-1]
                   hintlst.append(hint)
                
                
                if b[i-1] in qmrules.neghverb and b[i+1] in qmrules.pronoun:
                   hint="Remove the fullstop after: "+b[i-1] 
                   hintlst.append(hint)
                if (b[i-1] in qmrules.pronoun1) and (b[i+1] in qmrules.freqadv):    
                   hint="Remove the fullstop after: "+b[i-1] 
                   hintlst.append(hint)
                if (b[i-1] in qmrules.freqadv) and (b[i+1] in qmrules.verbs or b[i+1] in qmrules.verbl):    
                   hint="Remove the fullstop after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.indefenitepro and b[i+1] in qmrules.prep:#---None of them likes to draw
                   hint="Remove the fullstop after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.prep and b[i+1] in qmrules.pronoun:
                   hint="Remove the fullstop after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.pronoun and b[i+1] in qmrules.verbl:
                   hint="Remove the fullstop after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbl and b[i+1] in qmrules.prep:
                   hint="Remove the fullstop after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.prep and b[i+1] in qmrules.verbs or b[i+1] in qmrules.verbl:
                   hint="Remove the fullstop after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.cor_conj and b[i+1] in qmrules.snoun:
                   hint="Remove the fullstop after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.snoun and b[i+1] in qmrules.cor_conj:
                   hint="Remove the fullstop after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.snoun and b[i+1] in qmrules.cor_conj:
                   hint="Remove the fullstop after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.snoun  and b[i+1] in qmrules.verbs:
                    
                    hint="Remove the fullstop after: " +b[i-1]
                    mandlst.append(hint)     
                   
## #---------------------------------------------------<w> with comma-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<w>" and c[i]==","):
                if (b[i-1] in qmrules.questionwords) and (b[i+1] in qmrules.perspro):
                    
                    hint="Remove the comma after: " +b[i-1]
                    mandlst.append(hint)
                            
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.verbl):    
                    hint="Remove the comma after: " +b[i-1]
                    mandlst.append(hint)
                    
                if b[i-1] in qmrules.verbl and b[i+1] in qmrules.wqtags:
                    hint="Remove the comma after: " +b[i-1]
                    mandlst.append(hint)      
                
                   
                if b[i-1] in qmrules.auxstring and b[i+1] in qmrules.verb:
                     hint="Remove the comma after: " +b[i-1]
                     mandlst.append(hint)
                if b[i-1] in qmrules.verb and b[i+1] in qmrules.prep:
                     hint="Remove the comma after: " +b[i-1]
                     mandlst.append(hint)
                if b[i-1] in qmrules.prep and b[i+1] in qmrules.verb:
                     hint="Remove the comma after: " +b[i-1]
                     mandlst.append(hint)    
                if b[i-1] in qmrules.verb and b[i+1] in qmrules.wqtags:
                     hint="Remove the comma after: " +b[i-1]
                     mandlst.append(hint)
                if b[i-1] in qmrules.wqtags and b[i+1] in qmrules.snoun:
                     
                     hint="Remove the comma after: " +b[i-1]
                     mandlst.append(hint)
                
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.hverb):    
                    hint="Remove the comma after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.hverb) and (b[i+1] in qmrules.quantifier):    
                    hint="Remove the comma after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.quantifier) and (b[i+1] in qmrules.snoun1):    
                    hint="Remove the comma after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.snoun1) and (b[i+1] in qmrules.wqtags):    
                    hint="Remove the comma after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.hverbl) and (b[i+1] in qmrules.perspro):    
                    hint="Remove the comma after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.verb):    
                    hint="Remove the comma after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.verb) and (b[i+1] in qmrules.perspro):    
                    hint="Remove the comma after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.wqtags):    
                    hint="Remove the comma after: " +b[i-1]
                    mandlst.append(hint)
                if b[i-1] in qmrules.wqtagsl  and (b[i+1] in qmrules.questionwordsl):
                    hint="Remove the comma after: " +b[i-1]
                    mandlst.append(hint)
                if b[i-1] in qmrules.questionwordsl  and (b[i+1] in qmrules.snoun) :
                    hint="Remove the comma after: " +b[i-1]
                    mandlst.append(hint)
                if b[i-1] in qmrules.snoun  and b[i+1] in qmrules.verbl :
                    
                    hint="Remove the comma after: " +b[i-1]
                    mandlst.append(hint)
                                    #--------------type5.py----------------------------------
                if b[i-1] in qmrules.adj and b[i+1] in qmrules.cnoun:
                   hint="Remove the comma after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.adj and b[i+1] in qmrules.onoun:
                   hint="Remove the comma after: "+b[i-1] 
                   hintlst.append(hint)   
                if b[i-1] in qmrules. hverb and b[i+1] in qmrules.verb:
                   hint="Remove the comma after: "+b[i-1]
                   hintlst.append(hint)
                
                if b[i-1] in qmrules.article and b[i+1] in qmrules.adj:
                   hint="Remove the comma after: "+b[i-1]
                   hintlst.append(hint)
                 
                if b[i-1] in qmrules.verb or b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs and b[i+1] in qmrules.article:
                   hint="Remove the comma after: "+b[i-1]
                   hintlst.append(hint)
                
                
                if b[i-1] in qmrules.neghverb and b[i+1] in qmrules.pronoun:
                   hint="Remove the comma after: "+b[i-1] 
                   hintlst.append(hint)
                if (b[i-1] in qmrules.pronoun1) and (b[i+1] in qmrules.freqadv):    
                   hint="Remove the comma after: "+b[i-1] 
                   hintlst.append(hint)
                if (b[i-1] in qmrules.freqadv) and (b[i+1] in qmrules.verbs or b[i+1] in qmrules.verbl):    
                   hint="Remove the comma after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.indefenitepro and b[i+1] in qmrules.prep:#---None of them likes to draw
                   hint="Remove the comma after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.prep and b[i+1] in qmrules.pronoun:
                   hint="Remove the comma after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.pronoun and b[i+1] in qmrules.verbl:
                   hint="Remove the comma after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbl and b[i+1] in qmrules.prep:
                   hint="Remove the comma after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.prep and b[i+1] in qmrules.verbs or b[i+1] in qmrules.verbl:
                   hint="Remove the comma after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.cor_conj and b[i+1] in qmrules.snoun:
                   hint="Remove the comma after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.snoun and b[i+1] in qmrules.cor_conj:
                   hint="Remove the comma after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.snoun and b[i+1] in qmrules.cor_conj:
                   hint="Remove the comma after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.snoun  and b[i+1] in qmrules.verbs:
                    
                    hint="Remove the comma after: " +b[i-1]
                    mandlst.append(hint)     
                   
## #---------------------------------------------------<w> with questionmark-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<w>" and c[i]=="?"):
                if (b[i-1] in qmrules.questionwords) and (b[i+1] in qmrules.perspro):
                    
                    hint="Remove the Questionmark after: " +b[i-1]
                    mandlst.append(hint)
                            
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.verbl):    
                    hint="Remove the Questionmark after: " +b[i-1]
                    mandlst.append(hint)
                    
                if b[i-1] in qmrules.verbl and b[i+1] in qmrules.wqtags:
                    hint="Remove the Questionmark after: " +b[i-1]
                    mandlst.append(hint)      
                
                   
                if b[i-1] in qmrules.auxstring and b[i+1] in qmrules.verb:
                     hint="Remove the Questionmark after: " +b[i-1]
                     mandlst.append(hint)
                if b[i-1] in qmrules.verb and b[i+1] in qmrules.prep:
                    hint="Remove the Questionmark after: " +b[i-1]
                    mandlst.append(hint)
                if b[i-1] in qmrules.prep and b[i+1] in qmrules.verb:
                     hint="Remove the Questionmark after: " +b[i-1]
                     mandlst.append(hint)    
                if b[i-1] in qmrules.verb and b[i+1] in qmrules.wqtags:
                    hint="Remove the Questionmark after: " +b[i-1]
                    mandlst.append(hint)
                if b[i-1] in qmrules.wqtags and b[i+1] in qmrules.snoun:
                     
                    hint="Remove the Questionmark after: " +b[i-1]
                    mandlst.append(hint)
                
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.hverb):    
                    hint="Remove the Questionmark after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.hverb) and (b[i+1] in qmrules.quantifier):    
                    hint="Remove the Questionmark after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1]in qmrules.quantifier) and (b[i+1] in qmrules.snoun1):    
                    hint="Remove the Questionmark after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.snoun1) and (b[i+1] in qmrules.wqtags):    
                    hint="Remove the Questionmark after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.hverbl) and (b[i+1] in qmrules.perspro):    
                    hint="Remove the Questionmark after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.verb):    
                    hint="Remove the Questionmark after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.verb) and (b[i+1] in qmrules.perspro):    
                    hint="Remove the Questionmark after: " +b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in qmrules.perspro) and (b[i+1] in qmrules.wqtags):    
                    hint="Remove the Questionmark after: " +b[i-1]
                    mandlst.append(hint)
                if b[i-1] in qmrules.wqtagsl  and (b[i+1] in qmrules.questionwordsl):
                    hint="Remove the Questionmark after: " +b[i-1]
                    mandlst.append(hint)
                if b[i-1] in qmrules.questionwordsl  and (b[i+1] in qmrules.snoun) :
                    hint="Remove the Questionmark after: " +b[i-1]
                    mandlst.append(hint)
                if b[i-1] in qmrules.snoun  and b[i+1] in qmrules.verbl:
                    
                    hint="Remove the Questionmark after: " +b[i-1]
                    mandlst.append(hint)
                    #--------------type5.py----------------------------------
                if b[i-1] in qmrules.adj and b[i+1] in qmrules.cnoun:
                   hint="Remove the Questionmark after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.adj and b[i+1] in qmrules.onoun:
                   hint="Remove the Questionmark after: "+b[i-1] 
                   hintlst.append(hint)   
                if b[i-1] in qmrules. hverb and b[i+1] in qmrules.verb:
                   hint="Remove the Questionmark after: "+b[i-1]
                   hintlst.append(hint)
                
                if b[i-1] in qmrules.article and b[i+1] in qmrules.adj:
                   hint="Remove the Questionmark after: "+b[i-1]
                   hintlst.append(hint)
                 
                if b[i-1] in qmrules.verb or b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbs and b[i+1] in qmrules.article:
                   hint="Remove the fullstop after: "+b[i-1]
                   hintlst.append(hint)
                
                
                if b[i-1] in qmrules.neghverb or b[i-1] in qmrules.hverb and b[i+1] in qmrules.pronoun:
                   hint="Remove the Questionmark after: "+b[i-1] 
                   hintlst.append(hint)
                if (b[i-1] in qmrules.pronoun1) and (b[i+1] in qmrules.freqadv):    
                   hint="Remove the Questionmark after: "+b[i-1] 
                   hintlst.append(hint) 
                if (b[i-1] in qmrules.freqadv) and (b[i+1] in qmrules.verbs or b[i+1] in qmrules.verbl):    
                   hint="Remove the Questionmark after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.indefenitepro and b[i+1] in qmrules.prep:#---None of them likes to draw
                   hint="Remove the Questionmark after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.prep and b[i+1] in qmrules.pronoun:
                   hint="Remove the Questionmark after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.pronoun and b[i+1] in qmrules.verbl:
                   hint="Remove the Questionmark after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.verbl or b[i-1] in qmrules.verbl and b[i+1] in qmrules.prep:
                   hint="Remove the Questionmark after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.prep and b[i+1] in qmrules.verbs or b[i+1] in qmrules.verbl:
                   hint="Remove the Questionmark after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.cor_conj and b[i+1] in qmrules.snoun:
                   hint="Remove the Questionmark after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.snoun and b[i+1] in qmrules.cor_conj:
                   hint="Remove the Questionmark after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.snoun and b[i+1] in qmrules.cor_conj:
                   hint="Remove the Questionmark after: "+b[i-1] 
                   hintlst.append(hint)
                if b[i-1] in qmrules.snoun  and b[i+1] in qmrules.verbs:
                    
                    hint="Remove the Questionmark after: " +b[i-1]
                    mandlst.append(hint)  
        return(hintlst,mandlst,correctlst,mandatory)
            
##p1=qmrules()
##hintlst,mandlst,correctlst,mandatory=p1.qmone()
##
##for i in hintlst:
##    print(i)
##for j in mandlst:
##    print(j)
##for k in correctlst:
##    print(k)
##
