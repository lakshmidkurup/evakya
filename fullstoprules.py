import re
import datetime
import mysql.connector
from dateutil.parser import parse
mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="rohith@123",
                database="pythonlogin"
        )
mycursor = mydb.cursor()
class frules:
    snoun=['Mary','James','John','Alice','A. Roy', 'K. Singh', 'R. K. Narayan', 'R. Kushner','Esmail','Bagani' ]
    verb=['lift','stand','answered','won','got','secured','achieved','hurt','lost','opened','closed','cooked','met','read','wrote','drew','drank','paid','bought','stayed','worked','joined','taught','married','dated','intracted','consulted','visited','debated','argued','fought','lived','seperated']
    verb1=[]
    verbs=['lift','stand','answer','win','get','secure','achieve','hurt','lose','open','close','cook','meet','read','write','draw','drink','pay','buy','stay','work','join','teach','married','date','intract','consult','visit','debate','argue','fight','live','seperate']
    for i in verbs:
        verb1.append(i+"s")
    verbing=[]
    for i in verbs:
        if i.endswith("e"):
            i=i[:-1]
            verbing.append(i+"ing")
        else:
            verbing.append(i+"ing")
    boolst=['The God of Small Things','Train to Pakistan','The Malgudi Days','The Mars Room']
    
    for i in verbs:
        verb1.append(i.capitalize())
    article=['a','an']
    det='the'
    adj=['confident','adorable','generous','charming','clever','huge','red','small','heavy','beautiful','fantastic','mesmerising','well-defined','hot','cold','warm','strong-flavored','delicious','tasty','mind-blowing','spicy','excellent','lovely','thrilled','elated','difficult','intelligent','rapid-fire','open-ended','lovely','fascinating','short','precise','interesting','selective','magnificent','high-grade','exceptional','focused','ambitious','demanding','competetive','exciting','brilliant','amazing','three-room','luxurious','spacious','own','modern','adorable','favorite','new','worthy','valuable','expensive','precious','limpy','twisted','sprained','fractured','considerate','attractive','amusing','jovial']
    onoun=['box','book','cage','scenary','house','building','tea','water','coffee','biriyani','pulav','kichdi','novel','story','match','race','ankle','leg','first-prize','second-prize','job','position','keys','books','poem','story','furniture','vegetables','fruits','bicycles','bicycle','house','organisation','school','college','flat','question']
    prep=['in','for','with','from','on','of']
    title=['Dr','Prof','Mr','Mrs','Sr','Bro','Major','Capt','Miss']
    beforetitle=['Late']
    vbz=['is','has','was']
    hverb=["could","will","would","might","can"]
    hintlst=[]
    correctlst=[]
    mandlst=[]
    pronoun=['his','her','he','she','it']
    pronoun1=[]
    cnoun=["man","gentleman","orator","woman","lady"]
    conj=["and","but"]
    for i in pronoun:
        pronoun1.append(i.capitalize())
    author=['Arundhati Roy', 'Khushwant Singh', 'Rasipuram Krishnaswami Iyer Narayan', 'Rachel Kushner', 'G. B. Shaw']
    booklst={'The God of Small Things','Train to Pakistan','The Malgudi Days','The Mars Room','Arms and the Man'}
    initial=[]
    lastname=[]
    firstbook=[]
    lastbook=[]
    lastbook2=[]
    midbook=[]
    abbrlst1=[]
    abbrlst2=[]
    abbrexp1=[]
    abbrexp2=[]
    with open("D:\\evakya\\dataset\\abbreviations.txt") as nd:
        for word in nd:
            dh=word.split(':')
            if dh[0] in ["state"]:
                abbrlst1.append(dh[1])
                abbrlst1.append(dh[2])
            if dh[0] in ["acronym"]:
                abbrlst1.append(dh[1])
                abbrlst2.append(dh[2])
            if dh[0] in ["workplace"]:
                abbrlst1.append(dh[1])
                abbrlst2.append(dh[2])    
    for i in abbrlst2:#--------------split all expansions
        k=i.split(" ")
        for l in k:
            abbrexp1.append(l)
    for i in abbrexp1:#---------------remove dupicates
        if i not in abbrexp2:
            abbrexp2.append(i)        
##    print("abbrexp2",abbrexp1) 
##    print("abbrexp2",abbrexp2)
    print("abbrexp2",abbrlst1) 
    for i in author:
        f1=i.split()
        if len(f1)==2:
            fname=f1[0][0]
            fname2=f1[1]
            initial.append(fname)
            lastname.append(fname2)
        elif len(f1)==3:
            fname=f1[0][0]
            fname2=f1[1][0]
            fname3=f1[2]
            initial.append(fname)
            initial.append(fname2)
            lastname.append(fname3)
        elif len(f1)==4:
            fname=f1[0][0]
            fname2=f1[1][0]
            fname3=f1[2][0]
            fname4=f1[3]
            initial.append(fname)
            initial.append(fname2)
            initial.append(fname3)
            lastname.append(fname4)
            #print("initial",lastname)
    for i in booklst:
        f2=i.split()
        book1=f2[0]
        book2=f2[-1]
        book3=f2[1:-1]
        firstbook.append(book1)
        
        lastbook.append(book2)
        for i in book3:
            midbook.append(i)
        #print("lastcbook",firstbook)    
    def fone(b,c,correct,category,level,username,userid,eid,submittedtext):
##    def fone(self):
##        b=['A', '<m>', 'Roy', '<w>', 'wrote', '<w>', 'The', '<w>', 'God', '<w>', 'of', '<w>', 'Small', '<w>', 'Things', '<m>', ' ']
##        c=['A', ' ', 'Roy', ' ', 'wrote', '"', 'The', ' ', 'God', ' ', 'of', ' ', 'Small', ' ', 'Things', ' ', '".', ' ', ' ']
##        b=['James','<w>','met','<w>','a','<w>','confident','<w>','James','<m>']
##        c=['James',' ','met',' ','a',' ','confident',' ','James',',']i
##        #b=['John', '<w>', 'paid', '<w>', 'Rs', '<m>', '4', '<m>', '300', '<w>', 'for', '<w>', 'his', '<w>', 'adorable', '<w>', 'bicycle', '<m>']
##        c=['James','.','met','.','a','.','confident','.','James','.',' ']
##        print(c)
##        b=['G','<m>','B','<m>','Shaw','<w>','wrote','<w>','"Arms','<w>','and','<w>','the','<w>','Man"','<m>']
##        c=['G',',','B','?','Shaw',',','wrote',',','"Arms',',','and',',','the',',','Man"','.']
        #c=['Prof', ' ', 'Alice', '.', 'has', ' ', 'got', ' ', 'the', ' ', 'job', '.']

##        b=['The','<w>','acronym','<w>','W','<w>','A','<w>','P','<w>','stands','<w>','for','<w>','Wireless','<w>','Access','<w>','Point','<m>']
##        c=['The','?','acronym','?','W','?','A','?','P','?','stands','?','for','?','Wireless','?','Access','?','Point','.']
##        b=['The', '<w>', 'acronym', '<w>', 'W', '<w>', 'C', '<w>', 'A', '<w>', 'G', '<w>', 'stands', '<w>', 'for', '<w>', 'Web', '<w>', 'Content', '<w>', 'Accessibility', '<w>', 'Guidelines', '<m>', ' ']
##        c=['The', ' ', 'acronym', ' ', 'W', ' ', 'C', ' ', 'A', ' ', 'G', ' ', 'Content', ' ', 'Accessibility', ' ', 'Guidelines', ' ', ' ']
##        b=['Alice', '<w>', 'drank', '<w>', 'a', '<w>', 'strong-flavored', '<w>', 'coffee', '<m>', ' ']
##        c['Alice', ' ', 'drank', ' ', 'a', ' ', 'strong', ' ', '-', ' ', 'flavored', ' ', 'coffee', '.', ' ']
        mandlst=[]
        correctlst=[]
        hintlst=[]
        b.append(" ")
        c.append(" ")
        ct=0
        for i in b:
            if i=="<m>":
                ct=ct+1
        mandatory=ct
        print("b at fullstop", b)
        print("c at fullstop",c)
        c = ['.' if i=='".' else i for i in c]
        for i in c:
            if i in frules.lastbook:
                c.pop(c.index(i)+1)
        print("c",c) 
#-----------------------------------------------------<m> with comma--------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):
                  
                hint="Comma not needed.Click the appropriate sidepane and read the manuals"
                mandlst.append(hint)
                        
#---------------------------------------------------<m> with questionmark--------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="?"):
                  
                hint="Question mark not needed.A fullstop required at mandatory location.Click the appropriate sidepane and read the manuals"
                mandlst.append(hint)
                           
            
#---------------------------------------------------<m> with no punctuation---------------------------------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==" "):
               
                hint="Punctuations are required at mandatory locations.Click the appropriate sidepane and read the manuals"
                mandlst.append(hint)            
                               
#------------------------------------------------ ---<m> with Fullstop---------------------------------------------------------------------------------------------        
        for i in range(0,len(b)):    
            if (b[i]=="<m>" and c[i]=="."):
                if b[i-1] in frules.pronoun and c[-2]==".":  
                    hint="Correct Answer. End the sentence with a Fullstop"
                    correctlst.append(hint)
                if b[i-1] in frules.snoun and c[-2]==".":  
                    hint="Correct Answer. End the sentence with a Fullstop"
                    correctlst.append(hint)                             
                if b[i-1] in frules.onoun and c[-2]==".":  
                    hint="Correct Answer. End the sentence with a Fullstop"
                    correctlst.append(hint)                    
                if (b[i-1] in frules.title) and (b[i+1] in frules.snoun):    
                    hint="Correct Answer:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                    correctlst.append(hint)
                 
                if b[i-1] in frules.lastbook and c[i]==".":  
                    hint="Correct Answer. End the sentence with a Fullstop"
                    correctlst.append(hint)
                if b[i-1] in frules.abbrexp2 and c[-2]==".":  
                    hint="Correct Answer. End the sentence with a Fullstop"
                    correctlst.append(hint) 
                if b[i-1] in frules.abbrlst1 or b[i-1] in ['S','M'] and c[-2]==".":  
                    hint="Correct Answer. End the sentence with a Fullstop"
                    correctlst.append(hint)
 #--------------------------------------------------------<w> with comma-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==","):
                
                hint="COMMA not needed.Click the appropriate sidepane and read the manuals"
                hintlst.append(hint)
                    
#--------------------------------------------------------<w> with FULLSTOP-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]=="."):
                
                hint="FULLSTOP at incorrect locations.Click the appropriate sidepane and read the manuals"
                hintlst.append(hint)
       
#--------------------------------------------------------<w> with Question Mark-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]=="?"):
                #if b[i-1] in frules.abbrexp2 and b[i+1] in frules.abbrexp2:
                hint="No need to add unnecessary  punctuations:"       
                hintlst.append(hint)        
        return(hintlst,mandlst,correctlst,mandatory)
#-------------------------------------------------------------------------------end of second attempt------------------------------------------------------------------------------
    def fthree(b,c,correct,category,level,username,userid,eid,submittedtext):
##    def fthree(self):
        mandlst=[]
        correctlst=[]
        hintlst=[]
        
        #print("commarules",b,c,correct,level,username,userid,eid,submittedtext)
##        b=['James','<w>','met','<w>','a','<w>','confident','<w>','James','<m>',' ']
        #b=['Prof','<m>','John','<w>','a','<w>','generous','<w>','man','<m>','drew','<w>','a','<w>','fantastic','<w>','house','<w>','and','<w>','painted','<w>','it','<m>']
        #b=['Dr','<m>','John','<w>','has','<w>','lost','<w>','his','<w>','books','<m>']
##        c=['James','?','met','?','a',',','confident',',','James','.',' ']
        #c=['Prof',',','John','?','a','?','generous','?','man',',','drew',',','a','?','fantastic',',','house','?','and',',','painted',',','it','.']
##        b=['R','<m>','K','<m>','I','<m>',"Narayan",'<m>','wrote','<w>','"Arms','<w>','and','<w>','the','<w>','Man"','<m>']
##        c=['R','.','K','.','I',' ','Narayan','.','wrote',',','"Arms',',','and',',','the',',','Man"'," "]
##        b=['The','<w>','acronym','<w>','GA','<w>','stands','<w>','for','<w>','Goa','<m>']
##        c=['The','.','acronym','.','GA','.','stands','.','for','.','Goa','.']
##        b=['The','<w>','acronym','<w>','W','<w>','A','<w>','P','<w>','stands','<w>','for','<w>','Wireless','<w>','Access','<w>','Point','<m>']
##        c=['The','?','acronym','?','W','?','A','?','P','?','stands','?','for','?','Wireless','?','Access','?','Point','.']
##        b=['Dr', '<m>', 'John', '<w>', 'has', '<w>', 'hurt', '<w>', 'his', '<w>', 'leg', '<m>']
##        c=['Dr', ',', 'John', ',', 'has', ',', 'hurt', ',', 'his', ',', 'leg', ',']
        b.append(" ")
        c.append(" ")
##        print(c)
##        print(b)
        ct=0
        for i in b:
            if i=="<m>":
                ct=ct+1
        mandatory=ct
        c = ['.' if i=='".' else i for i in c]
        for i in c:
            if i in frules.lastbook:
                c.pop(c.index(i)+1)
        print("c",c) 
#---------------------------------------------------------<m> with no punctuation----------------------------------------------------------------------------------
        for i in range(0,len(b)):            
            if (b[i]=="<m>" and c[i]==" "):
              
                if (b[i-1] in frules.title) and (b[i+1] in frules.snoun):
                    hint="Put a fullstop after:"+b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in frules.snoun) and (b[i+1] in frules.article):    
                    hint="Put a comma after the noun:"+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in frules.cnoun) and (b[i+1] in frules.verb):    
                    hint="Put a fullstop after the noun:"+ b[i-1]
                    correctlst.append(hint)
                if b[i-1] in frules.initial and b[i+1] in frules.lastname:
                    hint="Put a fullstop after the initial:"+ b[i-1]        
                    mandlst.append(hint)
                if b[i-1] in frules.initial and b[i+1] in frules.initial:
                    hint="Put a fullstop after the initial:"+ b[i-1]        
                    mandlst.append(hint)            
                if b[i-1] in frules.onoun and c[-2]==" " and c[i+1]==" ":
                    hint="Put a fullstop at the end of the sentence"
                    mandlst.append(hint)
                if b[i-1] in frules.snoun and c[-2]==" " and c[i+1]==" ":
                    hint="Put a fullstop at the end of the sentence"
                    mandlst.append(hint)
                if b[i-1] in frules.pronoun and c[-2]==" " and c[i+1]==" ":
                    hint="Put a fullstop at the end of the sentence"
                    mandlst.append(hint)
                if b[i-1] in frules.lastbook and c[i]==" ":  
                    hint="Put a fullstop at the end of the sentence"
                    mandlst.append(hint)
                if b[i-1] in frules.abbrexp2 and c[-2]==" " and c[i+1]==" ":  
                    hint="Put a fullstop at the end of the sentence"
                    mandlst.append(hint)
                if b[i-1] in frules.abbrlst1 and c[-2]==".":  
                    hint="Put a fullstop at the end of the sentence"
                    mandlst.append(hint)                     
    #---------------------------------------------------<m> with questionmark-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="?"):
                if (b[i-1] in frules.snoun) and (b[i+1] in frules.article):    
                    hint="Remove the questionmark.Put a comma after the noun:"+b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in frules.title) and (b[i+1] in frules.snoun):
                    hint="Remove the questionmark.Put a fullstop after the title:"+b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in frules.cnoun) and (b[i+1] in frules.verb):    
                    hint="Remove the questionmark.Put a fullstop after the noun:"+b[i-1]
                    mandlst.append(hint)   
                if (b[i-1] in frules.onoun) and c[-2]=="?":
                  
                    hint="Remove the questionmark.Put a fullstop at the end of the sentence"
                    mandlst.append(hint)
                if b[i-1] in frules.initial and b[i+1] in frules.lastname:
                    hint="Remove the questionmark.Put a fullstop after the initial:"+b[i-1]        
                    mandlst.append(hint)
                if b[i-1] in frules.initial and b[i+1] in frules.initial:
                    hint="Remove the questionmark.Put a fullstop after the initial:"+b[i-1]            
                    mandlst.append(hint)
                if b[i-1] in frules.snoun and c[-2]=="?":
                    hint="Remove the questionmark.Put a fullstop at the end of the sentence"
                    mandlst.append(hint)
                if b[i-1] in frules.pronoun and c[-2]=="?":
                    hint="Remove the questionmark.Put a fullstop at the end of the sentence"
                    mandlst.append(hint)
                if b[i-1] in frules.lastbook and c[i]=="?":  
                    hint="Remove the questionmark.Put a fullstop at the end of the sentence"
                    mandlst.append(hint) 
                if b[i-1] in frules.abbrexp2 and c[-2]=="?":  
                    hint="Remove the questionmark.Put a fullstop at the end of the sentence"
                    mandlst.append(hint)
                if b[i-1] in frules.abbrlst1 and c[-2]=="?":  
                    hint="Put a fullstop at the end of the sentence"
                    mandlst.append(hint) 

                                      
    #---------------------------------------------------<m> with Comma-------------------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):
               
               if (b[i-1] in frules.snoun) and (b[i+1] in frules.article):    
                    hint="Correct Answer:Always put a comma when there is a relative clause following the subject"
                    correctlst.append(hint)
               if b[i-1] in frules.initial and b[i+1] in frules.lastname:
                    hint="Remove the comma.Put a fullstop after the initial:"+b[i-1]           
                    mandlst.append(hint)
               if b[i-1] in frules.initial and b[i+1] in frules.initial:
                    hint="Remove the comma.Put a fullstop after the initial:"+b[i-1]               
                    mandlst.append(hint)       
               if (b[i-1] in frules.title) and (b[i+1] in frules.snoun):
                    hint="Remove the comma. a fullstop after the title:"+b[i-1]
                    mandlst.append(hint)
               if (b[i-1] in frules.onoun) and c[-2]==",":                  
                    hint="Remove the comma.Put a fullstop at the end of the sentence"
                    mandlst.append(hint)
               if (b[i-1] in frules.cnoun) and (b[i+1] in frules.verb):    
                    hint="Correct Answer:A comma has to be put to seperate the clauses"
                    mandlst.append(hint)

               if b[i-1] in frules.snoun and c[-2]==",":
                    hint="Remove the comma.Put a fullstop at the end of the sentence"
                    mandlst.append(hint)
               if b[i-1] in frules.pronoun and c[-2]==",":
                    hint="Remove the comma.Put a fullstop at the end of the sentence"
                    mandlst.append(hint)
               if b[i-1] in frules.lastbook and c[i]==",":  
                    hint="Remove the comma.Put a fullstop at the end of the sentence"
                    mandlst.append(hint)
               if b[i-1] in frules.abbrexp2 and c[-2]==",":  
                    hint="Remove the comma.Put a fullstop at the end of the sentence"
                    mandlst.append(hint)

               if b[i-1] in frules.abbrlst1 and c[-2]==",":  
                    hint="Put a fullstop at the end of the sentence"
                    mandlst.append(hint) 
                       
    #---------------------------------------------------<m> with Fullstop--------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                               
                if (b[i-1] in frules.title) and (b[i+1] in frules.snoun):    
                    hint="Correct Answer:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                    correctlst.append(hint)
                if (b[i-1] in frules.snoun) and (b[i+1] in frules.article):    
                    hint="Put a COMMA after:"+b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in frules.onoun) and c[-2]==".":                  
                    hint="Correct Answer.Always end a sentence with fullstop"
                    correctlst.append(hint)   
                if b[i-1] in frules.snoun and c[-2]==".":
                    hint="Correct Answer.Put a fullstop at the end of the sentence"
                    correctlst.append(hint)
                if b[i-1] in frules.initial and b[i+1] in frules.lastname:
                    hint="Correct Answer.Put a fullstop after the initial:"+b[i-1]        
                    correctlst.append(hint)
                if b[i-1] in frules.initial and b[i+1] in frules.initial:
                    hint="Correct Answer.Put a fullstop after the initial:"+b[i-1]            
                    correctlst.append(hint)
                if (b[i-1] in frules.cnoun) and (b[i+1] in frules.verb):    
                    hint="Correct Answer.Put a fullstop after the noun:"+b[i-1]
                    mandlst.append(hint)
                if b[i-1] in frules.pronoun and c[-2]==".":
                    hint="Correct Answer.Always end a sentence with fullstop"
                    correctlst.append(hint)
                if b[i-1] in frules.lastbook and c[i]==".":
                    hint="Correct Answer.Always end a sentence with fullstop"
                    correctlst.append(hint)
                if b[i-1] in frules.abbrexp2 and c[-2]==".":
                    hint="Correct Answer.Always end a sentence with fullstop"
                    correctlst.append(hint)
                if b[i-1] in frules.abbrlst1 and c[-2]==".":  
                    hint="Put a fullstop at the end of the sentence"
                    mandlst.append(hint)                       
 #--------------------------------------------------------<w> with comma-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==","):
                if b[i-1] in frules.snoun and b[i+1] in frules.verb:
                    hint="Remove the comma after the noun:"+b[i-1]
         
                    hintlst.append(hint)
                if b[i-1] in frules.verb and b[i+1] in frules.article:
                    hint="Remove the comma after the verb:"+b[i-1]
         
                    hintlst.append(hint) 
                if b[i-1] in frules.article and b[i+1] in frules.adj:
                    hint="Remove the comma after the article:"+b[i-1]
         
                    hintlst.append(hint)
                if b[i-1] in frules.adj and b[i+1] in frules.snoun:
                    hint="Remove the comma after the adjective:"+b[i-1]         
                    hintlst.append(hint)

                if b[i-1] in frules.snoun and b[i+1] in frules.vbz:
                    hint="Remove the comma after the noun:"+b[i-1]      
                    hintlst.append(hint)

                if b[i-1] in frules.vbz and b[i+1] in frules.verb:
                    hint="Remove the comma after the verb-to-be:"+b[i-1]         
                    hintlst.append(hint)

                if b[i-1] in frules.verb and b[i+1] in frules.pronoun:
                    hint="Remove the comma after the verb:"+b[i-1]    
                    hintlst.append(hint)
                if b[i-1] in frules.pronoun and b[i+1] in frules.onoun:
                    hint="Remove the comma after the pronoun:"+b[i-1]
                    hintlst.append(hint)
                    #-------------imperativenum.py--------------------------------
                if b[i-1] in frules.verb1 and (b[i+1] in frules.prep or b[i+1] =="the"):
                    hint="Remove the comma after the verb:"+b[i-1]    
                    hintlst.append(hint)
                if b[i-1] in frules.prep and b[i+1] in frules.onoun:
                    hint="Remove the comma after the preposition:"+b[i-1]        
                    hintlst.append(hint)
                if b[i-1] in frules.prep and b[i+1]=="the" :
                    hint="Remove the comma after the preposition:"+b[i-1]        
                    hintlst.append(hint)
                #-----------------------------------type1-------------------------
                if b[i-1] in frules.snoun and b[i+1] in frules.article:
                    hint="Remove the comma after the noun: "+b[i-1] 
                    hintlst.append(hint)
                if b[i-1] in frules.adj and b[i+1] in frules.cnoun:
                    hint="Remove the comma after the adjective: "+b[i-1]  
                    hintlst.append(hint)
                if b[i-1] in frules.cnoun and b[i+1] in frules.verb:
                    hint="Remove the comma after the common noun: "+b[i-1] 
                    hintlst.append(hint)
                if b[i-1] in frules.cnoun and b[i+1] in frules.verb:
                    hint="Remove the comma after the common noun "+b[i-1] 
                    hintlst.append(hint)
                if b[i-1] in frules.adj and b[i+1] in frules.onoun:
                    hint="Remove the comma after the adjective: "+b[i-1]       
                    hintlst.append(hint)     
                if b[i-1] in frules.onoun and b[i+1] in frules.conj:
                    hint="Remove the comma after the noun: "+b[i-1]         
                    hintlst.append(hint)
                if b[i-1] in frules.conj and b[i+1] in frules.verb:
                    hint="Remove the comma after the conjunction: "+b[i-1]  
                    hintlst.append(hint)
                
                    #-----------------type7write---------------------------------------------------------------------------
                if b[i-1] in frules.lastname and b[i+1]=="wrote":
                    hint="Remove the comma after the lastname: " +b[i-1]     
                    hintlst.append(hint)
                if b[i-1] =="wrote" and b[i+1] in frules.firstbook:
                    hint="Remove the comma after the verb: " +b[i-1]          
                    hintlst.append(hint)
                if b[i-1] in frules.midbook and b[i+1] in frules.lastbook:
                    hint="Remove the comma in between the book name-after(" +b[i-1]+")"          
                    hintlst.append(hint)
                if b[i-1] in frules.midbook and b[i+1] in frules.midbook:
                    hint="Remove the comma in between the book name-after(" +b[i-1] +")"      
                    hintlst.append(hint)
                #-----------------acronymwork/abbreviation----------------COMMA-----------------------------------------------------------
                if b[i-1] in frules.det.capitalize() and b[i+1] == "acronym":
                    hint="Remove the comma after the determiner "+b[i-1]        
                    hintlst.append(hint)
              
                if b[i-1] =="acronym" and b[i+1] in frules.abbrlst1 :
                    hint="Remove the comma after the keyword:"+b[i-1]      
                    hintlst.append(hint)
                 
                if b[i-1] in frules.abbrlst1 and b[i+1]=="stands":
                    hint="Remove the comma after the acronym:"+b[i-1]         
                    hintlst.append(hint)
                if b[i-1] in frules.abbrexp2 and b[i+1] in frules.abbrexp2:
                    hint="Remove the comma in between the exapnsion of acronym:"+b[i-1]          
                    hintlst.append(hint)
                if b[i-1] in frules.prep and b[i+1] in frules.abbrlst1:
                    hint="Remove the comma after the preposition:"+b[i-1]            
                    hintlst.append(hint) 
                if b[i-1] in frules.verb and b[i+1] in frules.prep:
                    hint="Remove the comma after the verb:"+b[i-1]          
                    hintlst.append(hint)
                if b[i-1] in frules.prep and len(b[i+1])==1:
                    hint="Remove the comma after the preposition:"+b[i-1]       
                    hintlst.append(hint)
                if b[i-1] =="acronym" and len(b[i+1])==1:
                    hint="Remove the comma after the keyword:"+b[i-1]        
                    hintlst.append(hint)
                if len(b[i-1])==1 and len(b[i+1])==1 :
                    hint="Remove the comma in between the acronyms:"+b[i-1]        
                    hintlst.append(hint)
                if len(b[i-1])==1 and (b[i+1]=="stands") :
                    hint="Remove the comma after the acronym:"+b[i-1]        
                    hintlst.append(hint)            
                    
 #--------------------------------------------------------<w> with FULLSTOP-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]=="."):
                if b[i-1] in frules.snoun and b[i+1] in frules.verb:
                    hint="Remove the FULLSTOP after the noun:"+b[i-1]
         
                    hintlst.append(hint)
                if b[i-1] in frules.verb and b[i+1] in frules.article:
                    hint="Remove the FULLSTOP after the verb:"+b[i-1]
         
                    hintlst.append(hint) 
                if b[i-1] in frules.article and b[i+1] in frules.adj:
                    hint="Remove the FULLSTOP after the article:"+b[i-1]
         
                    hintlst.append(hint)
                if b[i-1] in frules.adj and b[i+1] in frules.snoun:
                    hint="Remove the FULLSTOP after the adjective:"+b[i-1]         
                    hintlst.append(hint)

                if b[i-1] in frules.snoun and b[i+1] in frules.vbz:
                    hint="Remove the FULLSTOP after the noun:"+b[i-1]      
                    hintlst.append(hint)

                if b[i-1] in frules.vbz and b[i+1] in frules.verb:
                    hint="Remove the FULLSTOP after the verb-to-be:"+b[i-1]         
                    hintlst.append(hint)

                if b[i-1] in frules.verb and b[i+1] in frules.pronoun:
                    hint="Remove the FULLSTOP after the verb:"+b[i-1]    
                    hintlst.append(hint)
                if b[i-1] in frules.pronoun and b[i+1] in frules.onoun:
                    hint="Remove the FULLSTOP after the pronoun:"+b[i-1]
                    hintlst.append(hint)
                    #-------------imperativenum.py--------------------------------
                if b[i-1] in frules.verb1 and (b[i+1] in frules.prep or b[i+1] =="the"):
                    hint="Remove the FULLSTOP after the verb:"+b[i-1]    
                    hintlst.append(hint)
                if b[i-1] in frules.prep and b[i+1] in frules.onoun:
                    hint="Remove the FULLSTOP after the preposition:"+b[i-1]        
                    hintlst.append(hint)
                if b[i-1] in frules.prep and b[i+1]=="the" :
                    hint="Remove the FULLSTOP after the preposition:"+b[i-1]        
                    hintlst.append(hint)
                #-----------------------------------type1-------------------------
                if b[i-1] in frules.snoun and b[i+1] in frules.article:
                    hint="Remove the FULLSTOP after the noun:"+b[i-1] 
                    hintlst.append(hint)
                if b[i-1] in frules.adj and b[i+1] in frules.cnoun:
                    hint="Remove the FULLSTOP after the adjective:"+b[i-1] 
                    hintlst.append(hint)
                if b[i-1] in frules.cnoun and b[i+1] in frules.verb:
                    hint="Remove the FULLSTOP after the common noun:"+b[i-1] 
                    hintlst.append(hint)
                if b[i-1] in frules.cnoun and b[i+1] in frules.verb:
                    hint="Remove the FULLSTOP after the common noun:"+b[i-1] 
                    hintlst.append(hint)
                if b[i-1] in frules.adj and b[i+1] in frules.onoun:
                    hint="Remove the FULLSTOP after the adjective:"+b[i-1]       
                    hintlst.append(hint)     
                if b[i-1] in frules.onoun and b[i+1] in frules.conj:
                    hint="Remove the FULLSTOP after the noun:"+b[i-1]         
                    hintlst.append(hint)
                if b[i-1] in frules.conj and b[i+1] in frules.verb:
                    hint="Remove the FULLSTOP after the conjunction:"+b[i-1]  
                    hintlst.append(hint)
               
                    #-----------------type7write---------------------------------------------------------------------------
                if b[i-1] in frules.lastname and b[i+1]=="wrote":
                    hint="Remove the FULLSTOP after the lastname:"+b[i-1]     
                    hintlst.append(hint)
                if b[i-1] =="wrote" and b[i+1] in frules.firstbook:
                    hint="Remove the FULLSTOP after the verb:"+b[i-1]          
                    hintlst.append(hint)
                if b[i-1] in frules.midbook and b[i+1] in frules.lastbook:
                    hint="Remove the FULLSTOP in between the book name: after-("+b[i-1]+")"        
                    hintlst.append(hint)
                if b[i-1] in frules.midbook and b[i+1] in frules.midbook:
                    hint="Remove the FULLSTOP in between the book name:after("+b[i-1] +")"       
                    hintlst.append(hint)
                #-----------------acronymwork/abbreviation----------------COMMA-----------------------------------------------------------
                if b[i-1] in frules.det.capitalize() and b[i+1] == "acronym":
                    hint="Remove the FULLSTOP after the determiner: "+b[i-1]        
                    hintlst.append(hint)
              
                if b[i-1] =="acronym" and b[i+1] in frules.abbrlst1 :
                    hint="Remove the FULLSTOP after the keyword:"+b[i-1]      
                    hintlst.append(hint)
                 
                if b[i-1] in frules.abbrlst1 and b[i+1]=="stands":
                    hint="Remove the FULLSTOP after the acronym:"+b[i-1]         
                    hintlst.append(hint)
                if b[i-1] in frules.abbrexp2 and b[i+1] in frules.abbrexp2:
                    hint="Remove the FULLSTOP in between the exapnsion of acronym:"+b[i-1]          
                    hintlst.append(hint)
                if b[i-1] in frules.prep and b[i+1] in frules.abbrlst1:
                    hint="Remove the FULLSTOP after the preposition:"+b[i-1]            
                    hintlst.append(hint) 
                if b[i-1] in frules.verb and b[i+1] in frules.prep:
                    hint="Remove the FULLSTOP after the verb:"+b[i-1]          
                    hintlst.append(hint)
                if b[i-1] in frules.prep and len(b[i+1])==1:
                    hint="Remove the FULLSTOP after the preposition:"+b[i-1]       
                    hintlst.append(hint)
                if b[i-1] =="acronym" and len(b[i+1])==1:
                    hint="Remove the FULLSTOP after the keyword:"+b[i-1]        
                    hintlst.append(hint)
                if len(b[i-1])==1 and len(b[i+1])==1 :
                    hint="Remove the FULLSTOP in between the acronyms:"+b[i-1]        
                    hintlst.append(hint)
                if len(b[i-1])==1 and (b[i+1]=="stands") :
                    hint="Remove the FULLSTOP after the acronym:"+b[i-1]        
                    hintlst.append(hint)                      
#--------------------------------------------------------<w> with Question MArk-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]=="?"):
                if b[i-1] in frules.snoun and b[i+1] in frules.verb:
                    hint="Remove the [QUESTION MARK] after the noun:"+b[i-1]
         
                    hintlst.append(hint)
                if b[i-1] in frules.verb and b[i+1] in frules.article:
                    hint="Remove the [QUESTION MARK] after the verb:"+b[i-1]
         
                    hintlst.append(hint) 
                if b[i-1] in frules.article and b[i+1] in frules.adj:
                    hint="Remove the [QUESTION MARK] after the article:"+b[i-1]
         
                    hintlst.append(hint)
                if b[i-1] in frules.adj and b[i+1] in frules.snoun:
                    hint="Remove the [QUESTION MARK] after the adjective:"+b[i-1]         
                    hintlst.append(hint)

                if b[i-1] in frules.snoun and b[i+1] in frules.vbz:
                    hint="Remove the [QUESTION MARK] after the noun:"+b[i-1]      
                    hintlst.append(hint)

                if b[i-1] in frules.vbz and b[i+1] in frules.verb:
                    hint="Remove the [QUESTION MARK] after the verb-to-be:"+b[i-1]         
                    hintlst.append(hint)

                if b[i-1] in frules.verb and b[i+1] in frules.pronoun:
                    hint="Remove the [QUESTION MARK] after the verb:"+b[i-1]    
                    hintlst.append(hint)
                if b[i-1] in frules.pronoun and b[i+1] in frules.onoun:
                    hint="Remove the [QUESTION MARK] after the pronoun:"+b[i-1]
                    hintlst.append(hint)
                     #-------------imperativenum.py--------------------------------
                if b[i-1] in frules.verb1 and (b[i+1] in frules.prep or b[i+1] =="the"):
                    hint="Remove the [QUESTION MARK] after the verb:"+b[i-1]    
                    hintlst.append(hint)
                if b[i-1] in frules.prep and b[i+1] in frules.onoun:
                    hint="Remove the [QUESTION MARK] after the preposition:"+b[i-1]        
                    hintlst.append(hint)
                if b[i-1] in frules.prep and b[i+1]=="the" :
                    hint="Remove the [QUESTION MARK] after the preposition:"+b[i-1]        
                    hintlst.append(hint)
                #-----------------------------------type1-------------------------
                if b[i-1] in frules.snoun and b[i+1] in frules.article:
                    hint="Remove the [QUESTION MARK] after the noun:"+b[i-1] 
                    hintlst.append(hint)
                if b[i-1] in frules.adj and b[i+1] in frules.cnoun:
                    hint="Remove the [QUESTION MARK] after the adjective:"+b[i-1] 
                    hintlst.append(hint)
                if b[i-1] in frules.cnoun and b[i+1] in frules.verb:
                    hint="Remove the [QUESTION MARK] after the common noun"+b[i-1] 
                    hintlst.append(hint)
                if b[i-1] in frules.cnoun and b[i+1] in frules.verb:
                    hint="Remove the [QUESTION MARK] after the common noun: "+b[i-1] 
                    hintlst.append(hint)
                if b[i-1] in frules.adj and b[i+1] in frules.onoun:
                    hint="Remove the [QUESTION MARK] after the adjective: "+b[i-1]       
                    hintlst.append(hint)     
                if b[i-1] in frules.onoun and b[i+1] in frules.conj:
                    hint="Remove the [QUESTION MARK] after the noun: "+b[i-1]         
                    hintlst.append(hint)
                if b[i-1] in frules.conj and b[i+1] in frules.verb:
                    hint="Remove the [QUESTION MARK] after the conjunction: "+b[i-1]  
                    hintlst.append(hint)
               
          
                    #-----------------type7write---------------------------------------------------------------------------
                if b[i-1] in frules.lastname and b[i+1]=="wrote":
                    hint="Remove the  [QUESTION MARK] after the lastname:"+b[i-1]     
                    hintlst.append(hint)
                if b[i-1] =="wrote" and b[i+1] in frules.firstbook:
                    hint="Remove the [QUESTION MARK] after the verb:"+b[i-1]          
                    hintlst.append(hint)
                if b[i-1] in frules.midbook and b[i+1] in frules.lastbook:
                    hint="Remove the [QUESTION MARK] in between the book name:after( "+b[i-1] +")"          
                    hintlst.append(hint)
                if b[i-1] in frules.midbook and b[i+1] in frules.midbook:
                    hint="Remove the [QUESTION MARK] in between the book name:after( "+b[i-1]+")"        
                    hintlst.append(hint) 
           #-----------------acronymwork/abbreviation----------------COMMA-----------------------------------------------------------
                if b[i-1] in frules.det.capitalize() and b[i+1] == "acronym":
                    hint="Remove the [QUESTION MARK] after the determiner"+b[i-1]        
                    hintlst.append(hint)
              
                if b[i-1] =="acronym" and b[i+1] in frules.abbrlst1 :
                    hint="Remove the [QUESTION MARK] after the keyword:"+b[i-1]      
                    hintlst.append(hint)
                 
                if b[i-1] in frules.abbrlst1 and b[i+1]=="stands":
                    hint="Remove the [QUESTION MARK] after the acronym:"+b[i-1]         
                    hintlst.append(hint)
                if b[i-1] in frules.abbrexp2 and b[i+1] in frules.abbrexp2:
                    hint="Remove the [QUESTION MARK] in between the exapnsion of acronym:"+b[i-1]          
                    hintlst.append(hint)
                if b[i-1] in frules.prep and b[i+1] in frules.abbrlst1:
                    hint="Remove the [QUESTION MARK] after the preposition:"+b[i-1]            
                    hintlst.append(hint) 
                if b[i-1] in frules.verb and b[i+1] in frules.prep:
                    hint="Remove the [QUESTION MARK] after the verb:"+b[i-1]          
                    hintlst.append(hint)
                if b[i-1] in frules.prep and len(b[i+1])==1:
                    hint="Remove the [QUESTION MARK] after the preposition:"+b[i-1]       
                    hintlst.append(hint)
                if b[i-1] =="acronym" and len(b[i+1])==1:
                    hint="Remove the [QUESTION MARK] after the keyword:"+b[i-1]        
                    hintlst.append(hint)
                if len(b[i-1])==1 and len(b[i+1])==1 :
                    hint="Remove the [QUESTION MARK] in between the acronyms:"+b[i-1]        
                    hintlst.append(hint)
                if len(b[i-1])==1 and (b[i+1]=="stands") :
                    hint="Remove the [QUESTION MARK] after the acronym:"+b[i-1]        
                    hintlst.append(hint)            
                    
          
        return(hintlst,mandlst,correctlst,mandatory)
    def ftwo(b,c,correct,category,level,username,userid,eid,submittedtext):
##    def ftwo(self):
        mandlst=[]
        correctlst=[]
        hintlst=[]
        
        #print("commarules",b,c,correct,level,username,userid,eid,submittedtext)
##        b=['Mary','<w>','wrote','<w>','a','<w>','short','<w>','poem','<m>']
##        b.append(" ")no:of attempts at the end
        #b=['Prof','<m>','John','<w>','a','<w>','generous','<w>','man','<m>','drew','<w>','a','<w>','fantastic','<w>','house','<w>','and','<w>','painted','<w>','it','<m>']
        #b=['Dr','<m>','John','<w>','has','<w>','lost','<w>','his','<w>','books','<m>']
##        c=['Mary','.','wrote','?','a',',','short',',','poem',',']
##        c.append(" ")
        #c=['Prof',',','John','?','a','?','generous','?','man',',','drew',',','a','?','fantastic',',','house','?','and',',','painted',',','it','.']
##        b=['G','<m>','B','<m>','Shaw','<w>','wrote','<w>','"Arms','<w>','and','<w>','the','<w>','Man"','<m>']
####        c=['G',',','B','?','Shaw',',','wrote',',','"Arms',',','and',',','the','?','Man"','.',' ']
##        b=['The','<w>','acronym','<w>','GA','<w>','stands','<w>','for','<w>','Goa','<m>']
##        c=['The','?','acronym','?','GA','?','stands','?','for','?','Goa','.']
##        b=['The','<w>','acronym','<w>','W','<w>','A','<w>','P','<w>','stands','<w>','for','<w>','Wireless','<w>','Access','<w>','Point','<m>']
##        c=['The','?','acronym','?','W','?','A','?','P','?','stands','?','for','?','Wireless','?','Access','?','Point',' ']
##        b=['Capt','<m>','John','<w>','worked','<w>','in','<w>','I','<w>','B','<w>','M','<m>']
##        c=['Capt','?','John','?','worked','?','in','?','I','?','B','?','M','.']
##        b=['Dr', '<m>', 'John', '<w>', 'has', '<w>', 'hurt', '<w>', 'his', '<w>', 'leg', '<m>']
##        c=['Dr', ',', 'John', ',', 'has', ',', 'hurt', ',', 'his', ',', 'leg', ',']
        
##        print(c)
##        print(b)
        c.append(" ")
        b.append(" ")
        ct=0
        for i in b:
            if i=="<m>":
                ct=ct+1
        mandatory=ct
        c = ['.' if i=='".' else i for i in c]
        for i in c:
            if i in frules.lastbook:
                c.pop(c.index(i)+1)
        print("c",c) 
#---------------------------------------------------------<m> with no punctuation----------------------------------------------------------------------------------
        for i in range(0,len(b)):            
            if (b[i]=="<m>" and c[i]==" "):
               
                if (b[i-1] in frules.title) and (b[i+1] in frules.snoun):
                    hint="Read The manual again:Always end a title with a Fullstop as in Prof. Dr. Sr. etc"
                    mandlst.append(hint)
                if (b[i-1] in frules.snoun) and (b[i+1] in frules.article):    
                    hint="Read The manual again:A comma should be used a relative clause follows the main subject."
                    mandlst.append(hint)
                if (b[i-1] in frules.cnoun) and (b[i+1] in frules.verb):    
                    hint="Read The manual again:A comma should be used when a relative clause follows the main subject."
                    mandlst.append(hint)
                if b[i-1] in frules.initial and b[i+1] in frules.lastname:
                    hint="Read The manual again:A fullstop has to be added after an initial of the name"         
                    mandlst.append(hint)
                if b[i-1] in frules.initial and b[i+1] in frules.initial:
                    hint="Read The manual again:A fullstop has to be added to seperate the initials"         
                    mandlst.append(hint)        
                if (b[i-1] in frules.snoun) and c[-2]==" " and c[i+1]==" ":                  
                    hint="Read The manual again:Always end a sentence with Fullstop"
                    mandlst.append(hint)  
                if (b[i-1] in frules.onoun) and c[-2]==" " and c[i+1]==" ":
                  
                    hint="Read The manual again:Always end a sentence with fullstop"
                    mandlst.append(hint)
                if b[i-1] in frules.pronoun and c[-2]==" " and c[i+1]==" ":
                    hint="Read The manual again:Always end a sentence with fullstop"
                    mandlst.append(hint)
                if b[i-1] in frules.pronoun and c[-2]==" " and c[i+1]==" ":    
                    hint="Read The manual again:Always end a sentence with fullstop"
                    mandlst.append(hint)
                if b[i-1] in frules.abbrexp2 and c[-2]==" " and c[i+1]==" ":
                    hint="Read The manual again:Always end a sentence with fullstop"
                    mandlst.append(hint)
                if (b[i-1] in frules.lastbook) and c[i]==" ":
                  
                    hint="Read The manual again:Always end a sentence with fullstop"
                    mandlst.append(hint)

                if b[i-1] in frules.abbrlst1 or b[i-1] in ['S','M'] and c[-2]==" ":  
                    hint="Put a fullstop at the end of the sentence"
                    mandlst.append(hint)                       
    #---------------------------------------------------<m> with questionmark-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="?"):
                if (b[i-1] in frules.snoun) and (b[i+1] in frules.article):    
                    hint="Read The manual again:A comma should be used a relative clause follows the main subject."
                    mandlst.append(hint)
                if (b[i-1] in frules.title) and (b[i+1] in frules.snoun):
                    hint="Read The manual again:Always end a title with a Fullstop"
                    mandlst.append(hint)
                if (b[i-1] in frules.cnoun) and (b[i+1] in frules.verb):    
                    hint="Read The manual again:A comma should be used when a relative clause follows the main subject."
                    mandlst.append(hint)   
                if (b[i-1] in frules.onoun) and c[-2]=="?":
                  
                    hint="Read The manual again:Always end a sentence with fullstop"
                    mandlst.append(hint)
                if b[i-1] in frules.initial and b[i+1] in frules.lastname:
                    hint="Read The manual again:A fullstop has to be added after an initial of the name"         
                    mandlst.append(hint)
                if b[i-1] in frules.initial and b[i+1] in frules.initial:
                    hint="Read The manual again:A fullstop has to be added to seperate the initials"         
                    mandlst.append(hint)

                if (b[i-1] in frules.snoun) and c[-2]=="?":                  
                    hint="Read The manual again:Always end a sentence with Fullstop"
                    mandlst.append(hint)
                    
                if b[i-1] in frules.pronoun and c[-2]=="?":
                    hint="Read The manual again:Always end a sentence with fullstop"
                    mandlst.append(hint)
               
                if b[i-1] in frules.abbrexp2 and c[-2]=="?":
                    hint="Read The manual again:Always end a sentence with fullstop"
                    mandlst.append(hint)
                if (b[i-1] in frules.lastbook) and c[i]=="?":
                  
                    hint="Read The manual again:Always end a sentence with fullstop"
                    mandlst.append(hint)
                if b[i-1] in frules.abbrlst1 and c[-2]=="?":  
                    hint="Put a fullstop at the end of the sentence"
                    mandlst.append(hint)
                if b[i-1] in frules.abbrlst1 or b[i-1] in ['S','M'] and c[-2]=="?":  
                    hint="Put a fullstop at the end of the sentence"
                    mandlst.append(hint)                       
    #---------------------------------------------------<m> with Comma-------------------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):

               if (b[i-1] in frules.snoun) and (b[i+1] in frules.article):    
                    hint="Correct Answer:A comma should be used a relative clause follows the main subject."
                    correctlst.append(hint)
               
               if (b[i-1] in frules.cnoun) and (b[i+1] in frules.verb):    
                    hint="Correct Answer:A comma should be used when a relative clause ends and a verb/adjective phrase starts."
                    correctlst.append(hint) 
               if b[i-1] in frules.initial and b[i+1] in frules.lastname:
                    hint="Read The manual again:Is there a need of [Comma] after an initial of the name"         
                    mandlst.append(hint)
               if b[i-1] in frules.initial and b[i+1] in frules.initial:
                    hint="Read The manual again:A fullstop has to be added to seperate the initials"         
                    mandlst.append(hint)       
               if (b[i-1] in frules.title) and (b[i+1] in frules.snoun):
                    hint="Read The manual again:Always end a title with a Fullstop"
                    mandlst.append(hint)
               if (b[i-1] in frules.onoun) and c[-2]==",":                  
                    hint="Read The manual again:Always end a sentence with Fullstop"
                    mandlst.append(hint)
               if (b[i-1] in frules.snoun) and c[-2]==",":                  
                    hint="Read The manual again:Always end a sentence with Fullstop"
                    mandlst.append(hint)
               if b[i-1] in frules.pronoun and c[-2]==",":
                    hint="Read The manual again:Always end a sentence with fullstop"
                    mandlst.append(hint)
              
               if b[i-1] in frules.abbrexp2 and c[-2]==",":
                    hint="Read The manual again:Always end a sentence with fullstop"
                    mandlst.append(hint)
               if (b[i-1] in frules.lastbook) and c[i]==",":
                  
                    hint="Read The manual again:Always end a sentence with fullstop"
                    mandlst.append(hint)
               if b[i-1] in frules.abbrlst1 or b[i-1] in ['S','M'] and c[-2]==",":  
                    hint="Put a fullstop at the end of the sentence"
                    mandlst.append(hint)                        
    #---------------------------------------------------<m> with Fullstop--------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                if (b[i-1] in frules.onoun)  and c[-2]==".":    
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                if (b[i-1] in frules.snoun)  and c[-2]==".":    
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)    
                if (b[i-1] in frules.title) and (b[i+1] in frules.snoun):
                    hint="Correct Answer.:Always end a title with a Fullstop"
                    correctlst.append(hint)    
                
                if b[i-1] in frules.initial and b[i+1] in frules.lastname:
                    hint="Correct Answer:A fullstop has to be added after an initial of the name "         
                    correctlst.append(hint)
                if b[i-1] in frules.initial and b[i+1] in frules.initial:
                    hint="Correct Answer:A fullstop has to be added to seperate the initials"         
                    correctlst.append(hint)
                if (b[i-1] in frules.snoun) and (b[i+1] in frules.article):    
                    hint="Read the manual again:A comma should be used a relative clause follows the main subject."
                    mandlst.append(hint)
                if (b[i-1] in frules.cnoun) and (b[i+1] in frules.verb):    
                    hint="REad the manual again :A comma should be used when a relative clause ends and a verb/adjective phrase starts."
                    mandlst.append(hint)
                if b[i-1] in frules.pronoun and c[-2]==".":
                    hint="Correct Answer:Always end a sentence with fullstop"
                    correctlst.append(hint)
              
                if b[i-1] in frules.abbrexp2 and c[-2]==".":
                    hint="Correct Answer:Always end a sentence with fullstop"
                    correctlst.append(hint)
                if (b[i-1] in frules.lastbook) and c[i]=="." :
                  
                    hint="COrrect Answer:Always end a sentence with fullstop"
                    correctlst.append(hint)
                if b[i-1] in frules.abbrlst1 or b[i-1] in ['S','M'] and c[-2]==".":  
                    hint="Put a fullstop at the end of the sentence"
                    correctlst.append(hint)                       
 #--------------------------------------------------------<w> with comma-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==","):
                if b[i-1] in frules.snoun and b[i+1] in frules.verb:
                    hint="Read The manual again::Is there a need of punctuation[COMMA] between a noun and a verb"
         
                    hintlst.append(hint)
                if b[i-1] in frules.verb and b[i+1] in frules.article:
                    hint="Read The manual again::Is there a need of punctuation[COMMA] between a verb and an article"
         
                    hintlst.append(hint) 
                if b[i-1] in frules.article and b[i+1] in frules.adj:
                    hint="Read The manual again::Is there a need of punctuation[COMMA] between an article and an adjective"
         
                    hintlst.append(hint)
                if b[i-1] in frules.adj and b[i+1] in frules.snoun:
                    hint="Read The manual again::Is there a need of punctuation[COMMA] between an adjective and a noun"
         
                    hintlst.append(hint)

                if b[i-1] in frules.snoun and b[i+1] in frules.vbz:
                    hint="Read The manual again::Is there a need of punctuation[COMMA] between a noun when followed by is/has etc."         
                    hintlst.append(hint)

                if b[i-1] in frules.vbz and b[i+1] in frules.verb:
                    hint="Read The manual again::Is there a need of punctuation[COMMA] before a verb when it is preceded by a verb-to-be like [has/had]."         
                    hintlst.append(hint)

                if b[i-1] in frules.verb and b[i+1] in frules.pronoun:
                    hint="Read The manual again::Is there a need of punctuation[COMMA] after a verb when it is followed by a pronoun."         
                    hintlst.append(hint)
                if b[i-1] in frules.pronoun and b[i+1] in frules.onoun:
                    hint="Read The manual again::Is there a need of punctuation[COMMA] after a pronoun when it is followed by a noun."         
                    hintlst.append(hint)
                    #-------------imperativenum.py--------------------------------
                if b[i-1] in frules.verb1 and (b[i+1] in frules.prep or b[i+1] =="the"):
                    hint="Read The manual again::Is there a need of punctuation[COMMA] after a verb when it is followed by a preposition."         
                    hintlst.append(hint)
                if b[i-1] in frules.prep and b[i+1] in frules.onoun:
                    hint="Read The manual again::Is there a need of punctuation[COMMA] after a preposition when it is followed by a noun."         
                    hintlst.append(hint)
                if b[i-1] in frules.prep and b[i+1]=="the" :
                    hint="Read The manual again::Is there a need of punctuation[COMMA] after a preposition when it is followed by a determiner like[the]."         
                    hintlst.append(hint)
                #-----------------------------------type1-------------------------
                if b[i-1] in frules.snoun and b[i+1] in frules.article:
                    hint="Read The manual again:Is there a need of [COMMA] between a noun and an article"
                    hintlst.append(hint)
                if b[i-1] in frules.adj and b[i+1] in frules.cnoun:
                    hint="Read The manual again, HINT:No need to add a [COMMA] in between a noun/adjective phrase"
                    hintlst.append(hint)
                if b[i-1] in frules.cnoun and b[i+1] in frules.verb:
                    hint="Read The manual again, HINT:No need to add a [COMMA] after a noun"
                    hintlst.append(hint)
                if b[i-1] in frules.cnoun and b[i+1] in frules.verb:
                    hint="Read The manual again, HINT:No need to add a [COMMA] after a noun"
                    hintlst.append(hint)
                if b[i-1] in frules.adj and b[i+1] in frules.onoun:
                    hint="Read The manual again:Is there a need of [COMMA] between an adjective and a noun"         
                    hintlst.append(hint)     
                if b[i-1] in frules.onoun and b[i+1] in frules.conj:
                    hint="Read The manual again:Is there a need of [COMMA] before a conjunction [and]"         
                    hintlst.append(hint)
                if b[i-1] in frules.conj and b[i+1] in frules.verb:
                    hint="Read The manual again:Is there a need of [COMMA] after a conjunction [and]"         
                    hintlst.append(hint)
                
                
                    #-----------------type7write---------------------------------------------------------------------------
                if b[i-1] in frules.lastname and b[i+1]=="wrote":
                    hint="Read The manual again:Is there a need of [COMMA] after a verb, when it is folowed by a verb"         
                    hintlst.append(hint)
                if b[i-1] =="wrote" and b[i+1] in frules.firstbook:
                    hint="Read The manual again:No need of a [COMMA] after a verb, when it is folowed by an object noun"         
                    hintlst.append(hint)
                if b[i-1] in frules.midbook and b[i+1] in frules.lastbook:
                    hint="Read The manual again:No need of a [COMMA] in between a single enity(e.g. bookname)"         
                    hintlst.append(hint)
                if b[i-1] in frules.midbook and b[i+1] in frules.midbook:
                    hint="Read The manual again:No need of a [COMMA] in between a single enity(e.g. bookname)"         
                    hintlst.append(hint)
                #-----------------acronymwork/abbreviation----------------COMMA-----------------------------------------------------------
                if b[i-1] in frules.det.capitalize() and b[i+1] == "acronym":
                    hint="Read The manual again:No need for any [COMMA] after a determiner"         
                    hintlst.append(hint)
              
                if b[i-1] =="acronym" and b[i+1] in frules.abbrlst1 :
                    hint="Read The manual again:No need for any [COMMA] after the keyword-acronym"         
                    hintlst.append(hint)
                 
                if b[i-1] in frules.abbrlst1 and b[i+1]=="stands":
                    hint="Read The manual again:No need for any [COMMA] after an acronym"         
                    hintlst.append(hint)
                if b[i-1] in frules.abbrexp2 and b[i+1] in frules.abbrexp2:
                    hint="Read The manual again:No need for any [COMMA] in between the expanded form"         
                    hintlst.append(hint)
                if b[i-1] in frules.prep and b[i+1] in frules.abbrlst1:
                    hint="Read The manual again:No need for any [[COMMA]] after the preposition"           
                    hintlst.append(hint) 
                if b[i-1] in frules.verb and b[i+1] in frules.prep:
                    hint="Read The manual again:No need for any [COMMA] in between a verb and a preposition"         
                    hintlst.append(hint)
                if b[i-1] in frules.prep and len(b[i+1])==1:
                    hint="Read The manual again:No need for any [COMMA] after a preposition"         
                    hintlst.append(hint)
                if b[i-1] =="acronym" and len(b[i+1])==1:
                    hint="Read The manual again:No need for any [COMMA] after the keyword-acronymaaa"          
                    hintlst.append(hint)
                if len(b[i-1])==1 and len(b[i+1])==1 :
                    hint="Read The manual again:No need for any [COMMA] in between the acronyms"        
                    hintlst.append(hint)
                if len(b[i-1])==1 and (b[i+1]=="stands") :
                    hint="Read The manual again:No need for any [COMMA] after an acronym and before a verb"             
                    hintlst.append(hint)
                
                    
#--------------------------------------------------------<w> with FULLSTOP-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]=="."):
                if b[i-1] in frules.snoun and b[i+1] in frules.verb:
                    hint="Read The manual again:Is there a need of [FULLSTOP] between a noun and a verb"
         
                    hintlst.append(hint)
                if b[i-1] in frules.verb and b[i+1] in frules.article:
                    hint="Read The manual again:Is there a need of [FULLSTOP] between a verb and an article"
         
                    hintlst.append(hint) 
                if b[i-1] in frules.article and b[i+1] in frules.adj:
                    hint="Read The manual again:Is there a need of [FULLSTOP] between an article and an adjective"
         
                    hintlst.append(hint)
                if b[i-1] in frules.adj and b[i+1] in frules.snoun:
                    hint="Read The manual again:Is there a need of [FULLSTOP] between an adjective and a noun"
         
                    hintlst.append(hint)  
        
                if b[i-1] in frules.snoun and b[i+1] in frules.vbz:
                    hint="Read The manual again:Is there a need of punctuation[FULLSTOP] between a noun when followed by is/has etc."         
                    hintlst.append(hint)

                if b[i-1] in frules.vbz and b[i+1] in frules.verb:
                    hint="Read The manual again:Is there a need of punctuation[FULLSTOP] before a verb when it is preceded by a verb-to-be like [has/had]."         
                    hintlst.append(hint)

                if b[i-1] in frules.verb and b[i+1] in frules.pronoun:
                    hint="Read The manual again:Is there a need of punctuation[FULLSTOP] after a verb when it is followed by a pronoun."         
                    hintlst.append(hint)
                if b[i-1] in frules.pronoun and b[i+1] in frules.onoun:
                    hint="Read The manual again:Is there a need of punctuation[FULLSTOP] after a pronoun when it is followed by a noun."         
                    hintlst.append(hint)
                    #-------------imperativenum.py--------------------------------
                if b[i-1] in frules.verb1 and (b[i+1] in frules.prep or b[i+1] =="the"):
                    hint="Read The manual again:Is there a need of punctuation[FULLSTOP] after a verb when it is followed by a preposition."         
                    hintlst.append(hint)
                if b[i-1] in frules.prep and b[i+1] in frules.onoun:
                    hint="Read The manual again:Is there a need of punctuation[FULLSTOP] after a preposition when it is followed by a noun."         
                    hintlst.append(hint)
                if b[i-1] in frules.prep and b[i+1]=="the" :
                    hint="Read The manual again:Is there a need of punctuation[FULLSTOP] after a preposition when it is followed by a determiner like[the]."         
                    hintlst.append(hint)  
                 #---------------type1-----------------------------------------------
                if b[i-1] in frules.snoun and b[i+1] in frules.article:
                    hint="Read The manual again:Is there a need of [FULLSTOP] between a noun and an article"
                    hintlst.append(hint)
                if b[i-1] in frules.adj and b[i+1] in frules.cnoun:
                    hint="Read The manual again, HINT:No need to add a [FULLSTOP] in between a noun/adjective phrase"
                    hintlst.append(hint)
                if b[i-1] in frules.cnoun and b[i+1] in frules.verb:
                    hint="Read The manual again, HINT:No need to add a [FULLSTOP] after a noun"
                    hintlst.append(hint)
                if b[i-1] in frules.cnoun and b[i+1] in frules.verb:
                    hint="Read The manual again, HINT:No need to add a [FULLSTOP] after a noun"
                    hintlst.append(hint)
                if b[i-1] in frules.adj and b[i+1] in frules.onoun:
                    hint="Read The manual again:Is there a need of [FULLSTOP] between an adjective and a noun"         
                    hintlst.append(hint)     
                if b[i-1] in frules.onoun and b[i+1] in frules.conj:
                    hint="Read The manual again:Is there a need of [FULLSTOP] before a conjunction [and]"         
                    hintlst.append(hint)
                if b[i-1] in frules.conj and b[i+1] in frules.verb:
                    hint="Read The manual again:Is there a need of [FULLSTOP] after a conjunction [and]"         
                    hintlst.append(hint)
              
               
            #-----------------type7write---------------------------------------------------------------------------
                if b[i-1] in frules.lastname and b[i+1]=="wrote":
                    hint="Read The manual again:Is there a need of [FULLSTOP] after a verb, when it is folowed by a verb"         
                    hintlst.append(hint)
                if b[i-1] =="wrote" and b[i+1] in frules.firstbook:
                    hint="Read The manual again:No need of a [FULLSTOP] after a verb, when it is folowed by a object noun"         
                    hintlst.append(hint)
                if b[i-1] in frules.midbook and b[i+1] in frules.lastbook:
                    hint="Read The manual again:No need of a [FULLSTOP] in between a single enity(e.g. bookname)"         
                    hintlst.append(hint)
                if b[i-1] in frules.midbook and b[i+1] in frules.midbook:
                    hint="Read The manual again:No need of a [FULLSTOP] in between a single enity(e.g. bookname)"         
                    hintlst.append(hint)
            #-----------------acronymwork/abbreviation---------------------------------------------------------------------------
                if b[i-1] in frules.det.capitalize() and b[i+1] == "acronym":
                    hint="Read The manual again:No need for any [FULLSTOP] after a determiner"         
                    hintlst.append(hint)
              
                if b[i-1] =="acronym" and b[i+1] in frules.abbrlst1 :
                    hint="Read The manual again:No need for any [FULLSTOP] after the keyword-acronym"         
                    hintlst.append(hint)
                 
                if b[i-1] in frules.abbrlst1 and b[i+1]=="stands":
                    hint="Read The manual again:No need for any [FULLSTOP] after an acronym"         
                    hintlst.append(hint)
                if b[i-1] in frules.prep and b[i+1] in frules.abbrlst1:
                    hint="Read The manual again:No need for any [FULLSTOP] in after the preposition"           
                    hintlst.append(hint)    
                if b[i-1] in frules.abbrexp2 and b[i+1] in frules.abbrexp2:
                    hint="Read The manual again:No need for any [FULLSTOP] in between the expanded form"         
                    hintlst.append(hint)
                
                if b[i-1] in frules.verb and b[i+1] in frules.prep:
                    hint="Read The manual again:No need for any [FULLSTOP] in between a verb and a preposition"         
                    hintlst.append(hint)
                    
                if b[i-1] in frules.prep and len(b[i+1])==1:
                    hint="Read The manual again:No need for any [FULLSTOP] after a preposition"         
                    hintlst.append(hint)
             
                if b[i-1] =="acronym" and len(b[i+1])==1:
                    hint="Read The manual again:No need for any [FULLSTOP] after the keyword-acronymaaa"          
                    hintlst.append(hint)
                if len(b[i-1])==1 and len(b[i+1])==1 :
                    hint="Read The manual again:No need for any [FULLSTOP] in between the acronyms"        
                    hintlst.append(hint)
                if len(b[i-1])==1 and (b[i+1]=="stands") :
                    hint="Read The manual again:No need for any [FULLSTOP] after an acronym and before a verb"             
                    hintlst.append(hint)

#--------------------------------------------------------<w> with Question Mark-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]=="?"):
                if b[i-1] in frules.snoun and b[i+1] in frules.verb:
                    hint="Read The manual again:Is there a need of [QUESTION MARK] between a noun and a verb"
         
                    hintlst.append(hint)
                if b[i-1] in frules.verb and b[i+1] in frules.article:
                    hint="Read The manual again:Is there a need of [QUESTION MARK] between a verb and an article"
         
                    hintlst.append(hint) 
                if b[i-1] in frules.article and b[i+1] in frules.adj:
                    hint="Read The manual again:Is there a need of [QUESTION MARK] between an article and an adjective"
         
                    hintlst.append(hint)
                if b[i-1] in frules.adj and b[i+1] in frules.snoun:
                    hint="Read The manual again:Is there a need of [QUESTION MARK] between an adjective and a noun"
         
                    hintlst.append(hint)  
                
                if b[i-1] in frules.snoun and b[i+1] in frules.vbz:
                    hint="Read The manual again:Is there a need of punctuation[QUESTION MARK] between a noun when followed by is/has etc."         
                    hintlst.append(hint)

                if b[i-1] in frules.vbz and b[i+1] in frules.verb:
                    hint="Read The manual again:Is there a need of punctuation[QUESTION MARK] before a verb when it is preceded by a verb-to-be like [has/had]."         
                    hintlst.append(hint)

                if b[i-1] in frules.verb and b[i+1] in frules.pronoun:
                    hint="Read The manual again:Is there a need of punctuation[QUESTION MARK] after a verb when it is followed by a pronoun."         
                    hintlst.append(hint)
                if b[i-1] in frules.pronoun and b[i+1] in frules.onoun:
                    hint="Read The manual again:Is there a need of punctuation[QUESTION MARK] after a pronoun when it is followed by a noun."         
                    hintlst.append(hint)
                    
            #-------------------------imperativenum.py---------------------------------------------------------------------------------------------------------------
                    
                if b[i-1] in frules.verb1 and (b[i+1] in frules.prep or b[i+1] =="the"):
                    hint="Read The manual again:Is there a need of punctuation[QUESTION MARK] after a verb when it is followed by a preposition."         
                    hintlst.append(hint)
                if b[i-1] in frules.prep and b[i+1] in frules.onoun:
                    hint="Read The manual again:Is there a need of punctuation[QUESTION MARK] after a preposition when it is followed by a noun."         
                    hintlst.append(hint)
                if b[i-1] in frules.prep and b[i+1]=="the" :
                    hint="Read The manual again:Is there a need of punctuation[QUESTION MARK] after a preposition when it is followed by a determiner like[the]."         
                    hintlst.append(hint)

                    
               #--------------------------type1---------------------------------------------------------------------------------------------------------------------
                if b[i-1] in frules.snoun and b[i+1] in frules.article:
                    hint="Read The manual again:Is there a need of [QUESTION MARK] between a noun and an article"
                    hintlst.append(hint)
                if b[i-1] in frules.adj and b[i+1] in frules.cnoun:
                    hint="Read The manual again, HINT:No need to add a [QUESTION MARK] in between a noun/adjective phrase"
                    hintlst.append(hint)
                if b[i-1] in frules.cnoun and b[i+1] in frules.verb:
                    hint="Read The manual again, HINT:No need to add a [QUESTION MARK] after a noun"
                    hintlst.append(hint)
                if b[i-1] in frules.cnoun and b[i+1] in frules.verb:
                    hint="Read The manual again, HINT:No need to add a [QUESTION MARK] after a noun"
                    hintlst.append(hint)
                if b[i-1] in frules.adj and b[i+1] in frules.onoun:
                    hint="Read The manual again:Is there a need of [QUESTION MARK] between an adjective and a noun"         
                    hintlst.append(hint)     
                if b[i-1] in frules.onoun and b[i+1] in frules.conj:
                    hint="Read The manual again:Is there a need of [QUESTION MARK] before a conjunction [and]"         
                    hintlst.append(hint)
                if b[i-1] in frules.conj and b[i+1] in frules.verb:
                    hint="Read The manual again:Is there a need of [QUESTION MARK] after a conjunction [and]"         
                    hintlst.append(hint)
                
                    #-----------------type7write---------------------------------------------------------------------------
                if b[i-1] in frules.lastname and b[i+1] in frules.verb:
                    hint="Read The manual again:Is there a need of [QUESTION MARK] after a verb, when it is folowed by a verb"         
                    hintlst.append(hint)
                if b[i-1] =="wrote" and b[i+1] in frules.firstbook:
                    hint="Read The manual again:No need of a [QUESTION MARK] after a verb, when it is folowed by an object noun"         
                    hintlst.append(hint)
                if b[i-1] in frules.midbook and b[i+1] in frules.lastbook:
                    hint="Read The manual again:No need of a [QUESTION MARK] in between a single enity(e.g. bookname)"         
                    hintlst.append(hint)
                if b[i-1] in frules.midbook and b[i+1] in frules.midbook:
                    hint="Read The manual again:No need of a [QUESTION MARK] in between a single enity(e.g. bookname)"         
                    hintlst.append(hint)

                 #-----------------acronymwork/abbreviation---------------------------------------------------------------------------
                if b[i-1] in frules.det.capitalize() and b[i+1] == "acronym":
                    hint="Read The manual again:No need for any [QUESTION MARK] after a determiner"         
                    hintlst.append(hint)
              
                if b[i-1] =="acronym" and b[i+1] in frules.abbrlst1 :
                    hint="Read The manual again:No need for any [QUESTION MARK] after the keyword-acronym"         
                    hintlst.append(hint)
                 
                if b[i-1] in frules.abbrlst1 and b[i+1]=="stands":
                    hint="Read The manual again:No need for any [QUESTION MARK] after an acronym"         
                    hintlst.append(hint)
                if b[i-1] in frules.abbrexp2 and b[i+1] in frules.abbrexp2:
                    hint="Read The manual again:No need for any [QUESTION MARK] in between the expanded form"         
                    hintlst.append(hint)
                
                if b[i-1] in frules.verb and b[i+1] in frules.prep:
                    hint="Read The manual again:No need for any [QUESTION MARK] in between a verb and a preposition"         
                    hintlst.append(hint)
                if b[i-1] in frules.prep and len(b[i+1])==1:
                    hint="Read The manual again:No need for any [QUESTION MARK] after a preposition"         
                    hintlst.append(hint)
                if b[i-1] =="acronym" and len(b[i+1])==1:
                    hint="Read The manual again:No need for any [QUESTION MARK] after the keyword-acronymaaa"          
                    hintlst.append(hint)
                if len(b[i-1])==1 and len(b[i+1])==1 :
                    hint="Read The manual again:No need for any [QUESTION MARK] in between the acronyms"        
                    hintlst.append(hint)
                if len(b[i-1])==1 and (b[i+1]=="stands") :
                    hint="Read The manual again:No need for any [QUESTION MARK] after an acronym and before a verb"             
                    hintlst.append(hint)
                
                if b[i-1] in frules.prep and b[i+1] in frules.abbrlst1:
                    hint="Read The manual again:No need for any [QUESTION MARK] in between the expanded form"           
                    hintlst.append(hint) 
        return(hintlst,mandlst,correctlst,mandatory)    
##p1=frules()
##hintlst,mandlst,correctlst,mandatory=p1.fone()
##
##for i in hintlst:
##    print(i)
##for j in mandlst:
##    print(j)
##for k in correctlst:
##    print(k)
##print("mand",mandatory)
 
