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
class crules:
    snoun=['Mary','James','John','Alice','A. Roy', 'K. Singh', 'R. K. Narayan', 'R. Kushner' ]
    verb=['tasted','born','lift','stand','answered','won','got','secured','achieved','hurt','lost','opened','closed','cooked','met','read','wrote','drew','drank','paid','bought','stayed','worked','joined','taught','married','dated','intracted','consulted','visited','debated','argued','fought','lived','seperated']
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
    alpha=['T','C','S','I','B','M']
    for i in verb:
        verb1.append(i.capitalize())
    article=['a','an']
    det=['the']
    adj=['confident','adorable','generous','charming','costly','clever','huge','red','small','heavy','beautiful','fantastic','mesmerising','well-defined','hot','cold','warm','strong-flavored','delicious','tasty','mind-blowing','spicy','excellent','lovely','thrilled','elated','difficult','intelligent','rapid-fire','open-ended','lovely','fascinating','short','precise','interesting','selective','magnificent','high-grade','exceptional','focused','ambitious','demanding','competetive','exciting','brilliant','amazing','three-room','luxurious','spacious','own','modern','adorable','favorite','new','worthy','valuable','expensive','precious','limpy','twisted','sprained','fractured','considerate','attractive','amusing','jovial']
    onoun=['box','book','cage','scenary','house','building','tea','water','coffee','biriyani','pulav','kichdi','novel','story','match','race','ankle','leg','first-prize','second-prize','job','position','keys','books','poem','story','furniture','vegetables','fruits','bicycles','bicycle','house','organisation','school','college','flat','question']
    prep=['in','for','with','from','on']
    title=['Dr','Prof','Mr','Mrs','Sr','Bro','Major','Capt','Miss','Late']
    vbz=['is','has','was']
    hverb=["could","will","would","might","can"]
    hintlst=[]
    correctlst=[]
    mandlst=[]
    pronoun=['his','her','he','she','it','I','you']
    pronoun1=[]
    for i in pronoun:
        pronoun1.append(i.capitalize())
    cnoun=["man","gentleman","orator","woman","lady"]
    conj=['and','but']
    conjadv=['however','morever','However','Morever']
    coverb=['lift']
    neg=["not"]
    cordconj=['and','but']
    adverb=['slowly','çarefully','artistically','frequently','joyful','deliciously','fast','happily']
    madverb=['extremely','very','eagerly','keenly','finally']
    intro_words=['Although','Because','While']
    regex= "\d{4}"        #----------------------number---------------------------------------
    weekdays =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    year=['2009','2020','2021']
    yearregex="[1-3][0-9]{3}"
    f=open("D:\\evakya\\dataset\\adverb.txt")
    oadverblst=[]
    for line in f:
        dh=line.split(":") 
        oadverblst.append(dh[1])


   


    def commathree(b,c,correct,category,level,username,userid,eid,submittedtext):         
##    def commathree(self):
##        b=['John', '<w>', 'paid', '<w>', 'Rs', '<m>', '4', '<m>', '300', '<w>', 'for', '<w>', 'his', '<w>', 'adorable', '<w>', 'bicycle', '<m>']
##        c=['John', ',', 'paid', '', 'Rs', ' ', '4', ' ', '300', ' ', 'for', ' ', 'his', ' ', 'adorable', ' ', 'bicycle',' ']
##        b=['Alice','<w>','bought','<w>','her','<w>','favorite','<w>','furniture','<w>','for','<w>','Rs','<m>','3','<m>','500','<m>']
##        c=['Alice',' ','bought',' ','her',' ','favorite',' ','furniture',' ','for',' ','Rs',' ','3',' ','500',' ']
####        b=['Mary','<w>','was','<w>','born','<w>','on','<w>','February','<w>','17','<m>','2021','<m>']
##        c=['Mary',' ','was',' ','born',' ','on',' ','February',' ','17',' ','2021',' ']
##        b=['Mr', '<m>', 'John', '<m>', 'a', '<w>', 'charming', '<w>', 'gentleman', '<m>', 'might', '<w>', 'open', '<w>', 'a', '<w>', 'small', '<w>', 'cage', '<m>', 'Morever', '<m>', 'he', '<w>', 'might', '<w>', 'lift', '<w>', 'it', '<m>']
##                                                                                                                                                                    
##        c=['Mr', '.', 'John', ' ', 'a', ';', 'charming', ' ', 'gentleman', ',', 'might', ' ', 'open', ' ', 'a', ' ', 'small', ' ', 'cage', '.', 'Morever', ' ', 'he', ' ', 'might', ' ', 'lift', ' ', 'it', '.']

##        c=['Sr', ';', 'Mary', ' ', 'a', ' ', 'generous', ' ', 'lady', ';', 'could', ' ', 'open', ' ', 'a', ' ', 'huge', ' ', 'cage', ' ', 'and', ' ', 'a', ' ', 'red', ' ', 'box',' ']
##        b=['Sr', '<m>', 'Mary', '<m>' , 'a', '<w>', 'generous', '<w>', 'lady', '<m>', 'could', '<w>', 'open', '<w>', 'a', '<w>', 'huge', '<w>', 'cage', '<w>', 'and', '<w>', 'a', '<w>', 'red', '<w>', 'box','<m>']
##        c=['Major', ' ', 'John', ' ', 'a', ' ', 'charming', ' ', 'gentleman', ' ', 'could', ' ', 'open', ' ', 'a', ' ', 'box', ' ', 'a', ' ', 'book', ' ', 'and', ' ', 'a', ' ', 'cage', ' ']
##        b=['Major', '<m>', 'John', '<m>', 'a', '<w>', 'charming', '<w>', 'gentleman', '<m>', 'could', '<w>', 'open', '<w>', 'a', '<w>', 'box', '<m>', 'a', '<w>', 'book', '<w>', 'and', '<w>', 'a', '<w>', 'cage', '<m>']
##        b=['Mr', '<m>', 'John', '<m>', 'a', '<w>', 'charming', '<w>', 'gentleman', '<m>', 'might', '<w>', 'open', '<w>', 'a', '<w>', 'small', '<w>', 'cage', '<m>', 'Morever', '<m>', 'he', '<w>', 'might', '<w>', 'lift', '<w>', 'it', '<m>']
##        c=['Mr', '', 'John', ' ', 'a', ',', 'charming', '', 'gentleman', ',', 'might', ' ', 'open', ',', 'a', ',', 'small', '<w>', 'cage', '.', 'Morever', ',', 'he', ' ', 'might', ',', 'lift', ' ', 'it', '.']
##        b=['John', '<w>', 'paid', '<w>', 'Rs', '<m>', '4', '<m>', '300', '<w>', 'for', '<w>', 'his', '<w>', 'adorable', '<w>', 'bicycle', '<m>']
##        c=['John', ',', 'paid', ',', 'Rs', ',', '4', ',', '300', ',', 'for', ' ', 'his', ' ', 'adorable', ' ', 'bicycle',' ']
##        #Capt<m>John<m>a<w>generous<w>orator<m>could<w>open<w>a<w>huge<w>box<m>However<m>he<w>could<w>not<w>lift<w>it<m>
##        b=['Miss', '<m>', 'Alice', '<m>', 'a', '<w>', 'generous', '<w>', 'woman', '<m>', 'will', '<w>', 'open', '<w>', 'a', '<w>', 'book', '<m>', 'and', '<w>', 'a', '<w>', 'cage', '<m>', ' ']
##        c=['Miss', ' ', 'Alice', ' ', 'a', ' ', 'generous', ' ', 'woman', ' ', 'will', ' ', 'open', ' ', 'a', ' ', 'book', ' ', 'and', ' ', 'a', ' ', 'cage', ' ', ' ']
##        b=['James', '<w>', 'bought', '<w>', 'his', '<w>', 'costly', '<w>', 'furniture', '<w>', 'for', '<w>', 'Rs', '<m>', '3', '<m>', '500', '<m>', ' ']
##        c=['James', ';', 'bought', ';', 'his', ';', 'costly', ';', 'furniture', ';', 'for', ';', 'Rs', ';', '3', ';', '500', ';', ' ']
##        b=['Mary', '<w>', 'achieved', '<w>', 'a', '<w>', 'position', '<w>', 'on', '<w>', 'February', '<w>', '17', '<m>', '2021', '<m>', ' ']
##        c=['Mary', ' ', 'achieved', ' ', 'a', ' ', 'position', ' ', 'on', ' ', 'February', ' ', '17', '.', '2021', '.', ' ']
##        b=['Prof', '<m>', 'John', '<m>', 'a', '<w>', 'charming', '<w>', 'man', '<m>', 'tasted', '<w>', 'the', '<w>', 'warm', '<w>', 'water', '<w>', 'and', '<w>', 'gulped', '<w>', 'it', '<m>', ' ', ' ']
##        c=['Prof', ';', 'John', ';', 'a', ' ', 'charming', ' ', 'man', ';', 'tasted', ' ', 'the', ' ', 'warm', ' ', 'water', ' ', 'and', ' ', 'gulped', ' ', 'it', ',', ' ']
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
        co="".join(c)
               
 #-----------------------------------------------------------------------------------<m> with no punctuation-----------------------
         
        for i in range(0,len(b)):
            
                if (b[i]=="<m>" and c[i]==" "):
                    
            #---------------------------------------------type11date.py----------------------------------------------------------------    
                
                    try:
                        if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                            
                            hint="Incorrect Answer:A comma should be used after a date " +b[i-1]
                            mandlst.append(hint)
                        if b[i-1]==str(str(parse(co, fuzzy=True).year)) and c[i]==" " and c[i+1]==" ": #-------------------type11date------------------------
                            hint="InCorrect Answer:Sentence should be ended with a FULLSTOP"
                            mandlst.append(hint)     
                        
                        if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                            hint="Incorrect Answer:A comma should be used after a month " +b[i-1]
                            mandlst.append(hint)
                        if b[i-1]==str(parse(co,fuzzy=True).day) and c[i]==" " and c[i+1]==" ":
                            hint="Incorrect Answer:Put a fullstop after the day " +b[i-1]
                            mandlst.append(hint)    
                        
                        if b[i-3]==str(parse(co,fuzzy=True).day) and b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                            hint="InCorrect Answer:Put a comma just after the month" +b[i-1]
                            mandlst.append(hint)    
                            
                        if b[i-1] in crules.weekdays and b[i+1]==crules.months :
                            hint="Incorrect Answer:A comma should be used after a weekday " +b[i-1]
                            mandlst.append(hint)
                    except:
                        pass
                         
                if b[i-1] in crules.pronoun and c[-2]==" " and c[i+1]==" ":  
                    hint="InCorrect Answer. Put a Fullstop after--"+ b[i-1]
                    mandlst.append(hint)
                if b[i-1] in crules.snoun and c[i]==" " and c[i+1]==" ":  
                    hint="InCorrect Answer. Put a Fullstop after--"+ b[i-1]
                    mandlst.append(hint)                             
                if b[i-1] in crules.onoun and c[i]==" " and c[i+1]==" ":  
                    hint="InCorrect Answer. Put a Fullstop after--"+ b[i-1]  #---------3
                    mandlst.append(hint)                    
                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
                    hint="InCorrect Answer:Put a Fullstop after--"+ b[i-1]
                    mandlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.conjadv: #-------------type6.py
                    hint="InCorrect Answer.Put a Fullstop after--"+ b[i-1]
                    mandlst.append(hint)
                if b[i-1] in crules.oadverblst and c[i]==" " and c[i+1]==" ":  
                    hint="InCorrect Answer. Put a Fullstop after--"+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.verb):    
                    hint="InCorrect Answer:Put a Comma after--"+b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="InCorrect Answer:Put a Comma after--"+b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.verb1):    
                    hint="InCorrect Answer:Put a Comma after--"+b[i-1]
                    mandlst.append(hint)    
                if (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="InCorrect Answer:Put a Comma after--"+ b[i-1]
                    mandlst.append(hint)
              
                if (b[i-1] in crules.onoun) and (b[i+1] in crules.article):    
                    hint="InCorrect Answer:Put a Comma after--"+ b[i-1]
                    mandlst.append(hint)
                
                
                if b[i-1] in crules.onoun and b[i+1] in crules.pronoun :
                    hint="Incorrect answer:Put a Comma after--"+ b[i-1]
                    mandlst.append(hint)  
   #---------------------------type10comma.py----------------------------------------------------------------
                for j in c:
                    if j == "Rs":
                        phrase="".join(b)
                        oned=re.findall("\d+",phrase)
                        if len(oned)!=0:
                            
                        #print("oned",oned[0],oned[1])
                            if b[i-1]=="Rs" and b[i+1]==oned[0]:
                                hint="InCorrect Answer:You should use a fullstop after keyword {Rs]"
                                mandlst.append(hint)
                            if b[i-3]=="Rs" and b[i-1]==oned[0] and b[i+1]==oned[1]:
                                hint="Incorrect Answer:Put a Comma after--"+ b[i-1]
                                mandlst.append(hint)
                                
                            if b[i-1]==oned[1] and c[i]==" " and c[i+1]==" ":
                                hint="InCorrect Answer:Put a Fullstop after --"+ b[i-1]
                                mandlst.append(hint)
        
                
    #---------------------------------------------------<m> with semicolon-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            
            if (b[i]=="<m>" and c[i]==";"):
                
               
                if b[i-1] in crules.pronoun and c[i]==";" and c[i+1]==" ":  
                    hint="InCorrect Answer.Put a Fullstop after--"+ b[i-1]
                    mandlst.append(hint)
                if b[i-1] in crules.snoun and c[i]==";" and c[i+1]==" ":  
                    hint="InCorrect Answer. Put a Fullstop after--"+ b[i-1]
                    mandlst.append(hint)                             
                if b[i-1] in crules.onoun and c[i]==";" and c[i+1]==" ":  
                    hint="InCorrect Answer. Put a Fullstop after--"+ b[i-1]
                    mandlst.append(hint)                    
                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
                    hint="InCorrect Answer:Put a Fullstop after--"+ b[i-1]
                    mandlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.conjadv: #-------------type6.py
                    hint="InCorrect Answer.Put a Fullstop after--"+ b[i-1]
                    mandlst.append(hint)
                if b[i-1] in crules.oadverblst and c[i]==";" and c[i+1]==" ":  
                    hint="InCorrect Answer. Put a Fullstop after--"+ b[i-1]
                    mandlst.append(hint)
                
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="InCorrect Answer:Put a Comma after--"+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.verb):    
                    hint="InCorrect Answer:Put a Comma after--"+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.verb1):    
                    hint="InCorrect Answer:Put a Comma after--"+ b[i-1]
                    mandlst.append(hint)
                    
                if (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="InCorrect Answer:Put a Comma after--"+ b[i-1]
                    mandlst.append(hint)
              
                if (b[i-1] in crules.onoun) and (b[i+1] in crules.article):    
                    hint="InCorrect Answer:Put a Comma after--"+ b[i-1]
                    mandlst.append(hint)
                
                
                if b[i-1] in crules.onoun and b[i+1] in crules.pronoun :
                    hint="Incorrect answer:Put a Comma after--"+ b[i-1]
                    mandlst.append(hint)
                    
   #---------------------------type10comma.py----------------------------------------------------------------
                for j in c:
                    if j == "Rs":
                        phrase="".join(b)
                        oned=re.findall("\d+",phrase)
                        if len(oned)!=0:
                            
                        #print("oned",oned[0],oned[1])
                            if b[i-1]=="Rs" and b[i+1]==oned[0]:
                                hint="InCorrect Answer:You should use a fullstop after keyword {Rs]"
                                mandlst.append(hint)
                            if b[i-3]=="Rs" and b[i-1]==oned[0] and b[i+1]==oned[1]:
                                hint="correct Answer:Put a Comma after--"+ b[i-1]
                                correctlst.append(hint)
                                
                            if b[i-1]==oned[1]  or b[i-1]==oned[0] and c[i]=="," and c[i+1]==" ":
                                hint="InCorrect Answer:END the sentence with a fullstop"
                                mandlst.append(hint)
                     #-----------type11date.py----------------------------------------------------------------
               
                try:
                    if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        
                        hint="Incorrect Answer:A comma should be used after a date " +b[i-1]
                        mandlst.append(hint)
                    if b[i-1]==str(str(parse(co, fuzzy=True).year)) and c[i]==";" and c[i+1]==" ": #-------------------type11date------------------------
                        hint="Incorrect Answer:Sentence should be ended with a FULLSTOP"
                        mandlst.append(hint)     
                    
                    if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                        hint="Incorrect Answer:A comma should be used after a month " +b[i-1]
                        mandlst.append(hint)
                    if b[i-1]==str(parse(co,fuzzy=True).day) and c[i]==";" and c[i+1]==" ":
                        hint="Incorrect Answer:Put a fullstop after the day " +b[i-1]
                        mandlst.append(hint)    
                    
                    if b[i-3]==str(parse(co,fuzzy=True).day) and b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        hint="Incorrect Answer:Put a comma just after the month" +b[i-1]
                        mandlst.append(hint)    
                        
                    if b[i-1] in crules.weekdays and b[i+1]==crules.months :
                        hint="Incorrect Answer:A comma should be used after a weekday " +b[i-1]
                        mandlst.append(hint)
                except:
                    pass

                            
 #---------------------------------------------------<m> with Comma-------------------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):
                 
                if b[i-1] in crules.pronoun and c[i]=="," and c[i+1]==" ":  
                    hint="InCorrect Answer.Put a Fullstop after--"+ b[i-1]
                    mandlst.append(hint)
                if b[i-1] in crules.snoun and c[i]=="," and c[i+1]==" ":  
                    hint="InCorrect Answer. Put a Fullstop after--"+ b[i-1]
                    mandlst.append(hint)                             
                if b[i-1] in crules.onoun and c[i]=="," and c[i+1]==" ":  
                    hint="InCorrect Answer. Put a Fullstop after--"+ b[i-1]
                    mandlst.append(hint)                    
               
                if b[i-1] in crules.onoun and b[i+1] in crules.conjadv: #-------------type6.py
                    hint="InCorrect Answer.Need a Fullstop after--"+ b[i-1]
                    mandlst.append(hint)
                if b[i-1] in crules.oadverblst and c[i]=="," and c[i+1]==" ":  
                    hint="InCorrect Answer. Need a Fullstop after--"+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="Correct Answer:Put a Comma to seperate two clauses"
                    correctlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.verb):    
                    hint="Correct Answer:Put a Comma to seperate two clauses"
                    correctlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.verb1):    
                    hint="Correct Answer:Always put a comma to seperate clauses"
                    correctlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.pronoun :
                    hint="Correct answer:If a clause has introductory words such as [although, as, because, if, since, when, while],Put a Comma to seperate the following clause."
                    correctlst.append(hint)  
                  #---------------------------type10comma.py----------------------------------------------------------------
                for j in c:
                    if j == "Rs":
                        phrase="".join(b)
                        oned=re.findall("\d+",phrase)
                        if len(oned)!=0:
                            
                        #print("oned",oned[0],oned[1])
                            if b[i-1]=="Rs" and b[i+1]==oned[0]:
                                hint="InCorrect Answer:You should use a fullstop after keyword {Rs]"
                                mandlst.append(hint)
                            if b[i-3]=="Rs" and b[i-1]==oned[0] and b[i+1]==oned[1]:
                                hint="Correct Answer:Comma used to seperate amount above 999"
                                mandlst.append(hint)
                                
                            if b[i-1]==oned[1]  or b[i-1]==oned[0] and c[i]=="," and c[i+1]==" ":
                                hint="InCorrect Answer:END the sentence with a fullstop"
                                mandlst.append(hint)
          
                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
                    hint="InCorrect Answer:Put a fullstop after the title--"+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="Correct Answer:A comma can be used to seperate an adjective phrase from the verbphrase"
                    correctlst.append(hint)
                if (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="Correct Answer:A comma should be used a relative clause follows the main subject."
                    correctlst.append(hint)
               
                if (b[i-1] in crules.onoun) and (b[i+1] in crules.article):    
                    hint="Correct Answer:A comma should be used after an object noun, when you are trying to list 2 or more nouns."
                    correctlst.append(hint)
                                  
               
                try:
                    if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        
                        hint="correct Answer:A comma should be used after a date " +b[i-1]
                        correctlst.append(hint)
                    if b[i-1]==str(str(parse(co, fuzzy=True).year)) and c[i]=="," and c[i+1]==" ": #-------------------type11date------------------------
                        hint="InCorrect Answer:Sentence should be ended with a FULLSTOP"
                        correctlst.append(hint)     
                    
                    if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                        hint="correct Answer:A comma should be used after a month " +b[i-1]
                        correctlst.append(hint)
                    if b[i-1]==str(parse(co,fuzzy=True).day) and c[i]=="," and c[i+1]==" ":
                        hint="Incorrect Answer:Put a fullstop after the day " +b[i-1]
                        mandlst.append(hint)    
                    
                    if b[i-3]==str(parse(co,fuzzy=True).day) and b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        hint="Correct Answer:Put a comma just after the month" +b[i-1]
                        correctlst.append(hint)    
                        
                    if b[i-1] in crules.weekdays and b[i+1] in crules.months :
                        hint="correct Answer:A comma should be used after a weekday " +b[i-1]
                        correctlst.append(hint)
                except:
                    pass
               
                            
    #---------------------------------------------------<m> with Fullstop--------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                try:
                    co=co.replace(".","?")
                    if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        
                        hint="Incorrect Answer:A comma should be used after a date " +b[i-1]
                        mandlst.append(hint)
                    if b[i-1]==str(str(parse(co, fuzzy=True).year)) and c[i]=="." and c[i+1]==" ": #-------------------type11date------------------------
                        hint="Correct Answer:Sentence should be ended with a FULLSTOP"
                        correctlst.append(hint)     
                    
                    if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                        hint="Incorrect Answer:A comma should be used after a month " +b[i-1]
                        mandlst.append(hint)
                    if b[i-1]==str(parse(co,fuzzy=True).day) and c[i]=="." and c[i+1]==" ":
                        hint="Correct Answer:End the sentencce with a FULLSTOP"
                        correctlst.append(hint)    
                    
                    if b[i-3]==str(parse(co,fuzzy=True).day) and b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        hint="InCorrect Answer:Put a comma just after the month" +b[i-1]
                        mandlst.append(hint)    
                        
                    if b[i-1] in crules.weekdays and b[i+1] in crules.months :
                        hint="Incorrect Answer:A comma should be used after a weekday " +b[i-1]
                        mandlst.append(hint)
                except:
                    pass
              
                    
                if b[i-1] in crules.pronoun and c[i]=="." and c[i+1]==" ":  
                    hint="Correct Answer.Put a Fullstop after--"+ b[i-1]
                    correctlst.append(hint)
                if b[i-1] in crules.snoun and c[i]=="." and c[i+1]==" ":  
                    hint="Correct Answer. Put a Fullstop after--"+ b[i-1]
                    correctlst.append(hint)                             
                if b[i-1] in crules.onoun and c[i]=="." and c[i+1]==" ":  
                    hint="Correct Answer. Put a Fullstop after--"+ b[i-1]
                    correctlst.append(hint)                    
                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
                    hint="Correct Answer:Put a Fullstop after the title--"+ b[i-1]
                    correctlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.conjadv: #-------------type6.py
                    hint="Correct Answer.Put a Fullstop after--"+ b[i-1]
                    correctlst.append(hint)
                if b[i-1] in crules.oadverblst and c[i]=="." and c[i+1]==" ":  
                    hint="InCorrect Answer. Put a Comma after--"+ b[i-1]
                    correctlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.verb1):    
                    hint="InCorrect Answer:Put a Comma after--"+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="InCorrect Answer:Put a Comma after--"+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.verb):    
                    hint="InCorrect Answer:Put a Comma after--"+ b[i-1]
                    mandlst.append(hint)
##                if (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
##                    hint="InCorrect Answer:Put a Comma after--"+ b[i-1]
##                    mandlst.append(hint)
##              
                if (b[i-1] in crules.onoun) and (b[i+1] in crules.article):    
                    hint="InCorrect Answer:Put a Comma after--"+ b[i-1]
                    mandlst.append(hint)
                
                
                if b[i-1] in crules.onoun and b[i+1] in crules.pronoun :
                    hint="Incorrect answer:Put a Comma after--"+ b[i-1]
                    mandlst.append(hint)  
                #---------------------------type10comma.py----------------------------------------------------------------
                for j in c:
                    if j == "Rs":
                        phrase="".join(b)
                        oned=re.findall("\d+",phrase)
                        if len(oned)!=0:
                            
                        #print("oned",oned[0],oned[1])
                            if b[i-1]=="Rs" and b[i+1]==oned[0]:
                                hint="Correct Answer:You should use a fullstop after keyword {Rs]"
                                correctlst.append(hint)
                            if b[i-3]=="Rs" and b[i-1]==oned[0] and b[i+1]==oned[1]:
                                hint="correct Answer:Comma used to seperate amount above 999"
                                correctlst.append(hint)
                                
                            if (b[i-3]==oned[0]  or b[i-1]==oned[1]) and c[i]==".":
                                hint="Correct Answer:END a sentence with a fullstop"
                                correctlst.append(hint)
                
                onounlst=list(set(crules.onoun) & set(b))
                if len(onounlst) > 2:
                    if (b[i-1] in crules.onoun and (b[i+1] in crules.article)):
                
                        hint="InCorrect Answer:Put a COMMA after--"+ b[i-1]
                        mandlst.append(hint) 
                             
                
 #--------------------------------------------------------<w> with comma-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==","):
                
#-----------------------------------type1.py----------------------------------------------------------
                
                if b[i-1] in crules.verb or b[i-1] in crules.verb1 and b[i+1] in crules.article:
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.madverb:
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.madverb and b[i+1] in crules.adverb:
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)
#--------------------------------compound.py----------------------------------------
                if b[i-1] in crules.cordconj and b[i+1] in crules.verb:
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)
               
#--------------------------------inrocomma.py---------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.intro_words and b[i+1] in crules.snoun:
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.snoun and b[i+1] in crules.vbz:
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.vbz and b[i+1] in crules.verbing:
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.verbing and b[i+1] in crules.article:
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)
                  
                if b[i-1] in crules.pronoun and b[i+1] in crules.verb:
                    hint="Remove the Comma after: "+b[i-1]
                    
                    hintlst.append(hint)
                if b[i-1] in crules.pronoun and b[i+1] in crules.adj:
                    hint="Remove the Comma after: "+ b[i-1]
                    hintlst.append(hint)
                
                #--------------type6.py------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
                  hint="Remove the Comma after: "+b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules. pronoun and b[i+1] in crules.hverb:
                  hint="Remove the Comma after: "+b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules.hverb and b[i+1] in crules.neg:
                  hint="Remove the Comma after: "+b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules. hverb and b[i+1] in crules.verb:
                  hint="Remove the Comma after: "+b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules.neg and b[i+1] in crules.verb:
                  hint="Remove the Comma after: "+b[i-1]
                  hintlst.append(hint)
                
                #--------------type3.py-----------------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.adj and b[i+1] in crules.cnoun:
                   hint="Remove the Comma after: "+b[i-1]
                   hintlst.append(hint)
                if b[i-1] in crules. hverb and b[i+1] in crules.verb:
                   hint="Remove the Comma after: "+b[i-1]
                   hintlst.append(hint)
                
                if b[i-1] in crules.article and b[i+1] in crules.adj:
                   hint="Remove the Comma after: "+b[i-1]
                   hintlst.append(hint)
                 
                if b[i-1] in crules.verb or b[i-1] in crules.verb1 and b[i+1] in crules.article:
                   hint="Remove the Comma after: "+b[i-1]
                   hintlst.append(hint)
                
                
                if b[i-1] in crules.cordconj and b[i+1] in crules.article:
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)
                #-----------------------------type4.py--------------------------------------------
                if b[i-1] in crules.hverb and b[i+1] in crules.verb:
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)
                    
                if b[i-1] in crules.cnoun and b[i+1] in crules.hverb:
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)
                    
                if b[i-1] in crules.article and b[i+1] in crules.onoun:
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.article and b[i+1] in crules.adj:
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)     
                if b[i-1] in crules.onoun and b[i+1] in crules.cordconj:
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)
                    
                if b[i-1] in crules.cordconj and b[i+1] in crules.article:
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)
            #-----------------------------type10comma.py---------------------------------------------------------------------------------------------------

                if b[i-1] in crules.snoun and b[i+1] in crules.verb:
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
                    hint="Remove the Comma after: "+[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.pronoun and b[i+1] in crules.adj:
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)
                
                if b[i-1] in crules.verb and b[i+1]=="Rs":
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)    
                
                phrase="".join(b)
                oned=re.findall("\d+",phrase)                                                                                                                                                                                                                
                #print("oned",oned[0],oned[1])
                if len(oned)!=0 :
                    if b[i-1] == oned[1] and b[i+1] in crules.prep:
                        hint="Remove the Comma after: "+b[i-1]
                        hintlst.append(hint)
                    
                if b[i-1] in crules.onoun and b[i+1] in crules.prep:
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)
                    
                if b[i-1] in crules.prep and b[i+1] in crules.pronoun:
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)
                    
                if b[i-1] in crules.prep and b[i+1]=="Rs":
                    hint="Remove the Comma after: "+b[i-1]
                    hintlst.append(hint)
    #-----------------------------type11date.py---------------------------------------------------------------------------------------------------
                try:
                   
                    if b[i-1] in crules.prep and b[i+1] in crules.months:
                        hint="Remove the Comma after: "+b[i-1]
                        hintlst.append(hint)
                       
                    if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                        hint="Remove the Comma after: "+b[i-1]
                        hintlst.append(hint)
    ##                if b[i-1]  in crules.snoun and b[i+1] in crules.vbz:
    ##                    hint="Read the manual again, HINT:No need of a comma after a noun when it is followed by a ['is','was']"
    ##                    hintlst.append(hint)
                    if b[i-1] in crules.vbz and b[i+1] in crules.verb:
                        hint="Remove the Comma after: "+b[i-1]
                        hintlst.append(hint)
                    if b[i-1] in crules.verb and b[i+1] in crules.prep:
                        hint="Remove the Comma after: "+b[i-1]
                        hintlst.append(hint)
                    if b[i-1] in crules.prep and b[i+1] in crules.weekdays:
                        hint="Remove the Comma after: "+b[i-1]
                        hintlst.append(hint)
                    if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1] in crules.months  :
                        hint="Remove the Comma after:"+b[i-1]
                        hintlst.append(hint)
                       
                    if b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        hint="Remove the Comma after: "+b[i-1]
                        hintlst.append(hint)
    ##                
                except:
                    pass
                    
#--------------------------------------------------------<w> with FULLSTOP-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]=="."):
                
 #--------------type3.py-----------------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.adj and b[i+1] in crules.cnoun:
                   hint="Remove the Fullstop after: "+b[i-1]
                   hintlst.append(hint)
                if b[i-1] in crules. hverb and b[i+1] in crules.verb:
                   hint="Remove the Fullstop after: "+b[i-1]
                   hintlst.append(hint)
                
                if b[i-1] in crules.article and b[i+1] in crules.adj:
                   hint="Remove the Fullstop after: "+b[i-1]
                   hintlst.append(hint)
                 
                if b[i-1] in crules.verb or b[i-1] in crules.verbl and b[i+1] in crules.article:
                   hint="Remove the Fullstop after: "+b[i-1]
                   hintlst.append(hint)
                if b[i-1] in crules. article and b[i+1] in crules.adj:
                   hint="Remove the Fullstop after: "+b[i-1]
                   hintlst.append(hint)
                
                if b[i-1] in crules.cordconj and b[i+1] in crules.article:
                    hint="Remove the Fullstop after: "+b[i-1]
                    hintlst.append(hint)
#-----------------------------------type1.py----------------------------------------------------------
                
                if b[i-1] in crules.verb or b[i-1] in crules.verb1 and b[i+1] in crules.article:
                    hint="Remove the fullstop after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.madverb:
                    hint="Remove the fullstop after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.madverb and b[i+1] in crules.adverb:
                    hint="Remove the fullstop after: "+b[i-1]
                    hintlst.append(hint)
#--------------------------------compound.py----------------------------------------
                if b[i-1] in crules.cordconj and b[i+1] in crules.verb:
                    hint="Remove the Fullstop after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
                    hint="Remove the Fullstop after: "+b[i-1]
                    hintlst.append(hint)
#--------------------------------inrocomma.py---------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.intro_words and b[i+1] in crules.snoun:
                    hint="Remove the Fullstop after: "+b[i-1]
                    hintlst.append(hint)
                
               
                if (b[i-1] in crules.verbing or  b[i-1] in crules.verb)  and b[i+1] in crules.article:
                    hint="Remove the Fullstop after:"+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in (crules.prep):
                    hint="Remove the Fullstop after: "+b[i-1]
                    hintlst.append(hint)  
                if b[i-1] in crules.pronoun and b[i+1] in crules.verb:
                    hint="Remove the Fullstop after: "+b[i-1]
                    
                    hintlst.append(hint)
                                  #-----------------------------type4.py--------------------------------------------
                if b[i-1] in crules.hverb and b[i+1] in crules.verb:
                    hint="Remove the Fullstop after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.cnoun and b[i+1] in crules.hverb:
                    hint="Remove the Fullstop after: "+b[i-1]
                    hintlst.append(hint)        
                if b[i-1] in crules.article and b[i+1] in crules.onoun:
                    hint="Remove the Fullstop after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.article and b[i+1] in crules.adj:
                    hint="Remove the Fullstop after: "+b[i-1]
                    hintlst.append(hint)    
                if b[i-1] in crules.onoun and b[i+1] in crules.cordconj:
                    hint="Remove the Fullstop after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.cordconj and b[i+1] in crules.article:
                    hint="Remove the Fullstop after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.pronoun and b[i+1] in crules.adj:
                    hint="Remove the Fullstop after: "+b[i-1]
                    
                    hintlst.append(hint) 
                 #--------------type6.py------------------------------------------------------------------------------------------------------
            
                if b[i-1] in crules. pronoun and b[i+1] in crules.hverb:
                  hint="Remove the Fullstop after: "+b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules.hverb and b[i+1] in crules.neg:
                  hint="Remove the Fullstop after: "+b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules. hverb and b[i+1] in crules.verb:
                  hint="Remove the Fullstop after: "+b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules.neg and b[i+1] in crules.verb:
                  hint="Remove the Fullstop after: "+b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
                  hint="Remove the Fullstop after: "+b[i-1]
                  hintlst.append(hint) 
              
                 #-----------------------------type10comma.py---------------------------------------------------------------------------------------------------

                if b[i-1] in crules.snoun and b[i+1] in crules.verb:
                    hint="Remove the Fullstop after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
                    hint="Remove the Fullstop after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.pronoun and b[i+1] in crules.adj:
                    hint="Remove the Fullstop after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
                    hint="Remove the Fullstop after: "+b[i-1]
                    hintlst.append(hint)
                   
                     
                phrase="".join(b)
                oned=re.findall("\d+",phrase)
                #print("oned",oned[0],oned[1])
                if len(oned)!=0:
                    if b[i-1]==oned[1] and b[i+1]==crules.prep:
                        hint="Remove the Fullstop after: "+b[i-1]
                        hintlst.append(hint)
                                           
              
                if b[i-1] in crules.onoun and b[i+1] in crules.prep:
                    hint="Remove the Fullstop after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.prep and b[i+1] in crules.pronoun:
                    hint="Remove the Fullstop after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.prep and b[i+1]=="Rs":
                    hint="Remove the Fullstop after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1]=="Rs":
                    hint="Remove the Fullstop after: "+b[i-1]
                    hintlst.append(hint)
                    
                    #-----------------type11date.py--------------------------------
                try:
                    if b[i-1] in crules.onoun and b[i+1] in crules.prep:
                        hint="Remove the Fullstop after: "+b[i-1]
                        hintlst.append(hint) 
                   
                    if b[i-1] in crules.prep and b[i+1] in crules.months:
                        hint="Remove the Fullstop after: "+b[i-1]
                        hintlst.append(hint) 
                    if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                        hint="Remove the Fullstop after: "+b[i-1]
                        hintlst.append(hint) 
                    if b[i-1]  in crules.snoun and b[i+1] in crules.vbz:
                        hint="Remove the Fullstop after: "+b[i-1]
                        hintlst.append(hint) 
                    if b[i-1] in crules.vbz and b[i+1] in crules.verb:
                        hint="Remove the Fullstop after: "+b[i-1]
                        hintlst.append(hint) 
                   
                    if b[i-1] in crules.prep and b[i+1] in crules.weekdays:
                        hint="Remove the Fullstop after: "+b[i-1]
                        hintlst.append(hint) 
                    if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1] in crules.months and b[i+2]==str(str(parse(co, fuzzy=True).year)):
                        hint="Remove the Fullstop after: "+b[i-1]
                        hintlst.append(hint) 
                    if b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)) and b[i+2]==None:
                        hint="Remove the Fullstop after: "+b[i-1]
                        hintlst.append(hint)  
                except:
                    pass
               

#--------------------------------------------------------<w> with SEMICOLON-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==";"):
               #-----------------------------------type1.py----------------------------------------------------------
                
                if b[i-1] in crules.verb or b[i-1] in crules.verb1 and b[i+1] in crules.article:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.madverb:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.madverb and b[i+1] in crules.adverb:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                     #--------------type3.py-----------------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.adj and b[i+1] in crules.cnoun:
                   hint="Remove the SEMICOLON after: "+b[i-1]
                   hintlst.append(hint)
                if b[i-1] in crules. hverb and b[i+1] in crules.verb:
                   hint="Remove the SEMICOLON after: "+b[i-1]
                   hintlst.append(hint)
                
                if b[i-1] in crules.article and b[i+1] in crules.adj:
                   hint="Remove the SEMICOLON after: "+b[i-1]
                   hintlst.append(hint)
                 
                if b[i-1] in crules.verb or b[i-1] in crules.verbl and b[i+1] in crules.article:
                   hint="Remove the SEMICOLON after: "+b[i-1]
                   hintlst.append(hint)
                if b[i-1] in crules. article and b[i+1] in crules.adj:
                   hint="Remove the SEMICOLON after: "+b[i-1]
                   hintlst.append(hint)
                
                if b[i-1] in crules.cordconj and b[i+1] in crules.article:
                    hint="Remove the SEMICOLON after: "+b[i-1]
#--------------------------------compound.py----------------------------------------
                if b[i-1] in crules.cordconj and b[i+1] in crules.verb:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
              
#--------------------------------inrocomma.py---------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.intro_words and b[i+1] in crules.snoun:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.snoun and b[i+1] in crules.vbz:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.vbz and (b[i+1] in crules.verbing or b[i+1] in crules.verb):
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if (b[i-1] in crules.verbing or  b[i-1] in crules.verb)  and b[i+1] in crules.article:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in (crules.prep):
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)  
                if b[i-1] in crules.pronoun and b[i+1] in crules.verb:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                    
                  #-----------------------------type4.py--------------------------------------------
                if b[i-1] in crules.hverb and b[i+1] in crules.verb:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.cnoun and b[i+1] in crules.hverb:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)      
                if b[i-1] in crules.article and b[i+1] in crules.onoun:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.cordconj:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.cordconj and b[i+1] in crules.article:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.article and b[i+1] in crules.adj:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint) 
                
                 #-----------------------------type10comma.py---------------------------------------------------------------------------------------------------

                if b[i-1] in crules.snoun and b[i+1] in crules.verb:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.pronoun and b[i+1] in crules.adj:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                 
                     
                phrase="".join(b)
                oned=re.findall("\d+",phrase)
                #print("oned",oned[0],oned[1])
                if len(oned)!=0:
                    if b[i-1]==oned[1] and b[i+1]==crules.prep:
                        hint="Remove the semicolon after: "+b[i-1]
                        hintlst.append(hint)
                                           
              
                if b[i-1] in crules.onoun and b[i+1] in crules.prep:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.prep and b[i+1] in crules.pronoun:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.prep and b[i+1]=="Rs":
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1]=="Rs":
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)  
                #--------------type6.py------------------------------------------------------------------------------------------------------
##                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
##                  hint="Read The manual again, HINT:No need to add a SEMICOLON in between a noun/adjective phrase"
##                  hintlst.append(hint)
                if b[i-1] in crules. pronoun and b[i+1] in crules.hverb:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.hverb and b[i+1] in crules.neg:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules. hverb and b[i+1] in crules.verb:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.neg and b[i+1] in crules.verb:
                    hint="Remove the semicolon after: "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.pronoun and b[i+1] in crules.adj :
                    hint="Remove the semicolon after:"+ b[i-1]
                    mandlst.append(hint)
                
   #-----------------------------type11date.py---------------------------------------------------------------------------------------------------
                try:
                   
                    if b[i-1] in crules.prep and b[i+1] in crules.months:
                        hint="Remove the semicolon after: "+b[i-1]
                        hintlst.append(hint)
                       
                    if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                        hint="Remove the semicolon after: "+b[i-1]
                        hintlst.append(hint)
    ##                if b[i-1]  in crules.snoun and b[i+1] in crules.vbz:
    ##                    hint="Read the manual again, HINT:No need of a comma after a noun when it is followed by a ['is','was']"
    ##                    hintlst.append(hint)
                   
                   
                    if b[i-1] in crules.prep and b[i+1] in crules.weekdays:
                        hint="Remove the semicolon after: "+b[i-1]
                        hintlst.append(hint)
                    if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1] in crules.months  :
                        hint="Remove the semicolon after: "+b[i-1]
                        hintlst.append(hint)
                       
                    if b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        hint="Remove the semicolon after: "+b[i-1]
                        hintlst.append(hint)
##                
                except:
                    pass
#---------------------------------------------------------<m> with no punctuation----------------------------------------------------------------------------------
        for i in range(0,len(b)):            
            if (b[i]=="<m>" and c[i]==" "):
                  
                #---------------------------------------------type11date.py----------------------------------------------------------------    
                try:
                    if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        hint="Put a comma after: "+b[i-1]
                        hintlst.append(hint)
                    if b[i-1]==str(str(parse(co, fuzzy=True).year)) and c[-1]==" ":
                        hint="Put a sentence with a FULLSTOP"
                        mandlst.append(hint)
                    if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                        hint="Put a comma after: "+b[i-1]
                        mandlst.append(hint)
                    if b[i-1]==str(parse(co,fuzzy=True).day) and c[-1]==" ":
                        hint="Put a comma after: "+b[i-1]
                        mandlst.append(hint)   
                    
                    if b[i-3]==str(parse(co,fuzzy=True).day) and b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        hint="Put a comma after: "+b[i-1]
                        correctlst.append(hint)    
                        
                    if b[i-1] in crules.weekdays and b[i+1] in crules.months :
                        hint="Put a comma after: "+b[i-1]
                        mandlst.append(hint)
                except:
                     pass
                   #----------------------------type6.py-----------------------------------------------------------------------------------
                for j in c:
                    if j in crules.conjadv:
                        if b[i-1] in crules.conjadv and b[i+1] in crules.pronoun:                            
                            hint="Put a comma after: "+b[i-1]                        
                            mandlst.append(hint)                             
                       
                        if b[i-1] in crules.onoun and b[i+1] in crules.conjadv:
                            
                            hint="Put a comma after: "+b[i-1]
                            mandlst.append(hint)    

        #--------------------------type10comma.py----------------------------------------------------------------
                if b[i-1] =="Rs" and b[i+1].isdigit():
                    hint="Incorrect Answer,HINT:Put a fullstop after Rs"
                    mandlst.append(hint)     
                phrase="".join(b)
                oned=re.findall("\d+",phrase)
                #print("oned",oned[0],oned[1])
                if b[i-1]==oned[0] and b[i]=="Rs":
                    hint="Incorrect Answer, Put a comma after the first digit"
                    mandlst.append(hint)
                    
                if b[i-1].isdigit() and c[i]==" ":
                    hint="Incorrect Answer, HINT:A sentence ends with a Fullstop"
                    mandlst.append(hint)
                              
      
        
                if b[i-1] in crules.pronoun and c[i]==" " and c[i+1]==" ":  
                    hint="InCorrect Answer. End the sentence with a Fullstop"
                    mandlst.append(hint)
                if b[i-1] in crules.snoun and c[i]==" " and c[i+1]==" ":  
                    hint="InCorrect Answer. End the sentence with a Fullstop"
                    mandlst.append(hint)                             
                if b[i-1] in crules.onoun and c[i]==" " and c[i+1]==" ":  #--------------------------4
                    hint="InCorrect Answer. End the sentence wit a Fullstop"
                    mandlst.append(hint)                    
                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
                    hint="InCorrect Answer:Put a Fullstop after --"+ b[i-1]
                    mandlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.conjadv: #-------------type6.py
                    hint="InCorrect Answer.Put A FULLSTOP after-- "+ b[i-1]
                    mandlst.append(hint)
                if b[i-1] in crules.oadverblst and c[i]==" " and c[i+1]==" ":  
                    hint="InCorrect Answer. End the sentence with a Fullstop"
                    mandlst.append(hint)
               
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="InCorrect Answer:Put a Comma after--"+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.verb):    
                    hint="InCorrect Answer:Put a Comma after--"+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.verb1):    
                    hint="InCorrect Answer:Put a Comma after--"+ b[i-1]
                    mandlst.append(hint)    
                if (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="Incorrect answer: Put a Comma after--:"+ b[i-1]
                    mandlst.append(hint)
              
                if (b[i-1] in crules.onoun) and (b[i+1] in crules.article):    
                    hint="InCorrect Answer:Put a Comma after--:"+ b[i-1]
                    mandlst.append(hint)
                
                
                if b[i-1] in crules.onoun and b[i+1] in crules.pronoun :
                    hint="Incorrect answer: Put a Comma after--:"+ b[i-1]
                    mandlst.append(hint)
             
            return(hintlst,mandlst,correctlst,mandatory)   

        
    def commatwo(b,c,correct,category,level,username,userid,eid,submittedtext):         
##    def commatwo(self):
##        b=['John', '<w>', 'paid', '<w>', 'Rs', '<m>', '4', '<m>', '300', '<w>', 'for', '<w>', 'his', '<w>', 'adorable', '<w>', 'bicycle', '<m>']
##        c=['John', ',', 'paid', '', 'Rs', ' ', '4', ' ', '300', ' ', 'for', ' ', 'his', ' ', 'adorable', ' ', 'bicycle',' ']
##        b=['Alice','<w>','bought','<w>','her','<w>','favorite','<w>','furniture','<w>','for','<w>','Rs','<m>','3','<m>','500','<m>']
##        c=['Alice',' ','bought',' ','her',' ','favorite',' ','furniture',' ','for',' ','Rs',' ','3',' ','500',' ']
##        b= ['James', '<w>', 'got', '<w>', 'a', '<w>', 'position', '<w>', 'on', '<w>', 'February', '<w>', '17', '<m>', '2021', '<m>']
##        c=['James', ' ', 'got', ' ', 'a', ' ', 'position', ' ', 'on', ' ', 'February', ' ', '17', ' ', '2021', ' ']
##        b=['Mr', '<m>', 'John', '<m>', 'a', '<w>', 'charming', '<w>', 'gentleman', '<m>', 'might', '<w>', 'open', '<w>', 'a', '<w>', 'small', '<w>', 'cage', '<m>', 'Morever', '<m>', 'he', '<w>', 'might', '<w>', 'lift', '<w>', 'it', '<m>']
##                                                                                                                                                                    
##        c=['Mr', '.', 'John', ' ', 'a', ';', 'charming', '', 'gentleman', ',', 'might', ' ', 'open', ' ', 'a', ' ', 'small', '<w>', 'cage', '.', 'Morever', ' ', 'he', ' ', 'might', ' ', 'lift', ' ', 'it', '.']

##        c=['Sr', ';', 'Mary', ' ', 'a', ' ', 'generous', ' ', 'lady', ';', 'could', ' ', 'open', ' ', 'a', ' ', 'huge', ' ', 'cage', ' ', 'and', ' ', 'a', ' ', 'red', ' ', 'box',' ']
##        b=['Sr', '<m>', 'Mary', '<m>' , 'a', '<w>', 'generous', '<w>', 'lady', '<m>', 'could', '<w>', 'open', '<w>', 'a', '<w>', 'huge', '<w>', 'cage', '<w>', 'and', '<w>', 'a', '<w>', 'red', '<w>', 'box','<m>']
##        c=['Major', ' ', 'John', ' ', 'a', ' ', 'charming', ' ', 'gentleman', ' ', 'could', ' ', 'open', ' ', 'a', ' ', 'box', ' ', 'a', ' ', 'book', ' ', 'and', ' ', 'a', ' ', 'cage', ' ']
##        b=['Major', '<m>', 'John', '<m>', 'a', '<w>', 'charming', '<w>', 'gentleman', '<m>', 'could', '<w>', 'open', '<w>', 'a', '<w>', 'box', '<m>', 'a', '<w>', 'book', '<w>', 'and', '<w>', 'a', '<w>', 'cage', '<m>']
##        b=['Mr', '<m>', 'John', '<m>', 'a', '<w>', 'charming', '<w>', 'gentleman', '<m>', 'might', '<w>', 'open', '<w>', 'a', '<w>', 'small', '<w>', 'cage', '<m>', 'Morever', '<m>', 'he', '<w>', 'might', '<w>', 'lift', '<w>', 'it', '<m>']
##        c=['Mr', '', 'John', ' ', 'a', ',', 'charming', '', 'gentleman', ',', 'might', ' ', 'open', ',', 'a', ',', 'small', '<w>', 'cage', '.', 'Morever', ',', 'he', ' ', 'might', ',', 'lift', ' ', 'it', '.']
##        b=['John', '<w>', 'paid', '<w>', 'Rs', '<m>', '4', '<m>', '300', '<w>', 'for', '<w>', 'his', '<w>', 'adorable', '<w>', 'bicycle', '<m>']
##        c=['John', ',', 'paid', ',', 'Rs', ',', '4', ',', '300', ',', 'for', ' ', 'his', ' ', 'adorable', ' ', 'bicycle',' ']
##        #Capt<m>John<m>a<w>generous<w>orator<m>could<w>open<w>a<w>huge<w>box<m>However<m>he<w>could<w>not<w>lift<w>it<m>
##        b=['Miss', '<m>', 'Alice', '<m>', 'a', '<w>', 'generous', '<w>', 'woman', '<m>', 'will', '<w>', 'open', '<w>', 'a', '<w>', 'book', '<m>', 'and', '<w>', 'a', '<w>', 'cage', '<m>', ' ']
##        c=['Miss', ' ', 'Alice', ' ', 'a', ' ', 'generous', ' ', 'woman', ' ', 'will', ' ', 'open', ' ', 'a', ' ', 'book', ' ', 'and', ' ', 'a', ' ', 'cage', ' ', ' ']
##        b=['James', '<w>', 'bought', '<w>', 'his', '<w>', 'costly', '<w>', 'furniture', '<w>', 'for', '<w>', 'Rs', '<m>', '3', '<m>', '500', '<m>', ' ']
##        c=['James', ';', 'bought', ';', 'his', ';', 'costly', ';', 'furniture', ';', 'for', ';', 'Rs', ';', '3', ';', '500', ';', ',']
##        b=['Major', '<m>', 'James', '<m>', 'a', '<w>', 'clever', '<w>', 'orator', '<m>', 'would', '<w>', 'open', '<w>', 'a', '<w>', 'book', '<m>', 'a', '<w>', 'cage', '<w>', 'and', '<w>', 'a', '<w>', 'box', '<m>', ' ', ' ']
##        c=['Major', ' ', 'James', ' ', 'a', ' ', 'clever', ' ', 'orator', ' ', 'would', ' ', 'open', ' ', 'a', ' ', 'book', ' ', 'a', ' ', 'cage', ' ', 'and', ' ', 'a', ' ', 'box', ' ', ' ']
##        b=['Prof', '<m>', 'James', '<m>', 'a', '<w>', 'confident', '<w>', 'man', '<m>', 'closes', '<w>', 'a', '<w>', 'huge', '<w>', 'box', '<w>', 'extremely', '<w>', 'carefully', '<m>', ' ']
##        c=['Prof', '.', 'James', ',', 'a', ' ', 'confident', ' ', 'man', ' ', 'closes', ' ', 'a', ' ', 'huge', ' ', 'box', ' ', 'extremely', ' ', 'carefully', '.', ' ']   
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
        co="".join(c)
        
     #-----------------------------------------------------------------------------------<m> with no punctuation-----------------------
         
        for i in range(0,len(b)):
            
            if (b[i]=="<m>" and c[i]==" "):
                
                  #---------------------------------------------type11date.py----------------------------------------------------------------    
                
                try:
                    if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        
                        hint="Incorrect Answer:A comma should be used after a date " +b[i-1]
                        mandlst.append(hint)
                    if b[i-1]==str(str(parse(co, fuzzy=True).year)) and c[i]==" " and c[i+1]==" ": #-------------------type11date------------------------
                        hint="InCorrect Answer:Sentence should be ended with a FULLSTOP"
                        mandlst.append(hint)     
                    
                    if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                        hint="Incorrect Answer:A comma should be used after a month when followed by a date(no year mentioned)"
                        mandlst.append(hint)
                    if b[i-1]==str(parse(co,fuzzy=True).day) and c[i]==" " and c[i+1]==" ":
                        hint="Incorrect Answer:Always Put a fullstop at the end"
                        mandlst.append(hint)    
                    
                    if b[i-3]==str(parse(co,fuzzy=True).day) and b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        hint="InCorrect Answer:Put a comma just after the month, as in the format 25 August, 2021"
                        mandlst.append(hint)    
                        
                    if b[i-1] in crules.weekdays and b[i+1] in crules.months :
                        hint="Incorrect Answer:A comma should be used after a weekday when followed by a month"
                        mandlst.append(hint)
                except:
                    pass
                         
                if b[i-1] in crules.pronoun and c[i]==" " and c[i+1]==" ":  
                    hint="InCorrect Answer. Sentence should be ended with a FULLSTOP"
                    mandlst.append(hint)
                if b[i-1] in crules.snoun and c[i]==" " and c[i+1]==" ":  
                    hint="InCorrect Answer. Sentence should be ended with a FULLSTOP"
                    mandlst.append(hint)                             
                if b[i-1] in crules.onoun and c[i]==" " and c[i+1]==" ":  
                    hint="InCorrect Answer. Sentence should be ended with a FULLSTOP"
                    mandlst.append(hint)                    
                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
                    hint="InCorrect Answer:Always put a fullstp after the title"
                    mandlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.conjadv: #-------------type6.py
                    hint="InCorrect Answer.Put a Fullstop between two complete sentences."
                    mandlst.append(hint)
                if b[i-1] in crules.oadverblst and c[i]==" " and c[i+1]==" ":  
                    hint="InCorrect Answer. Sentence should be ended with a FULLSTOP"
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.verb):    
                    hint="InCorrect Answer:Put a Comma after--"+b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="InCorrect Answer:Put a Comma between two clauses"
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.verb1):    
                    hint="InCorrect Answer:Put a Comma between two clauses"
                    mandlst.append(hint)    
                if (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="InCorrect Answer:Put a Comma between two clauses"
                    mandlst.append(hint)
              
                if (b[i-1] in crules.onoun) and (b[i+1] in crules.article):    
                    hint="InCorrect Answer:Put a Comma between two clauses"
                    mandlst.append(hint)
                
                
                if b[i-1] in crules.onoun and b[i+1] in crules.pronoun :
                    hint="Incorrect answer:If a clause has introductory words such as [although, as, because, if, since, when, while],Put a Comma to seperate the following clause."
                    mandlst.append(hint)  
   #---------------------------type10comma.py----------------------------------------------------------------
                for j in c:
                    if j == "Rs":
                        phrase="".join(b)
                        oned=re.findall("\d+",phrase)
                        if len(oned)!=0:
                            
                        #print("oned",oned[0],oned[1])
                            if b[i-1]=="Rs" and b[i+1]==oned[0]:
                                hint="InCorrect Answer:You should use a fullstop after keyword {Rs]"
                                mandlst.append(hint)
                            if b[i-3]=="Rs" and b[i-1]==oned[0] and b[i+1]==oned[1]:
                                hint="Incorrect Answer:Put a Comma after--"+ b[i-1]
                                mandlst.append(hint)
                                
                            if b[i-1]==oned[1] and c[i]==" " and c[i+1]==" ":
                                hint="InCorrect Answer:Sentence should be ended with a FULLSTOP"
                                mandlst.append(hint)
        
                
    #-----
    #---------------------------------------------------<m> with semicolon-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            
            if (b[i]=="<m>" and c[i]==";"):
                
               
                if b[i-1] in crules.pronoun and c[i]==";" and c[i+1]==" ":  
                    hint="InCorrect Answer. End the sentence with a Fullstop"
                    mandlst.append(hint)
                if b[i-1] in crules.snoun and c[i]==";" and c[i+1]==" ":  
                    hint="InCorrect Answer. End the sentence with a Fullstop"
                    mandlst.append(hint)                             
                if b[i-1] in crules.onoun and c[i]==";" and c[i+1]==" ":  
                    hint="InCorrect Answer. End the sentence wit a Fullstop"
                    mandlst.append(hint)                    
                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
                    hint="InCorrect Answer:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                    mandlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.conjadv: #-------------type6.py
                    hint="InCorrect Answer.A FULLSTOP is used to seperate two complete sentences."
                    mandlst.append(hint)
                if b[i-1] in crules.oadverblst and c[i]==";" and c[i+1]==" ":  
                    hint="InCorrect Answer. End the sentence with a Fullstop"
                    mandlst.append(hint)
                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
                    hint="InCorrect Answer:Never end a Abbreviation with a semicolon"
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="InCorrect Answer:A semicolon cannot be used to seperate an adjective phrase from the verbphrase"
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.verb):    
                    hint="Correct Answer:A comma can be used to seperate an adjective phrase from the verbphrase"
                    correctlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.verb1):    
                    hint="InCorrect Answer:Put a Comma between two clauses"
                    mandlst.append(hint)    
                if (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="InCorrect Answer:A semicolon should not be used when a relative clause follows the main subject."
                    mandlst.append(hint)
              
                if (b[i-1] in crules.onoun) and (b[i+1] in crules.article):    
                    hint="InCorrect Answer:A semicolon should not be used after an object noun, when you are trying to list 2 or more nouns."
                    mandlst.append(hint)
                
                
                if b[i-1] in crules.onoun and b[i+1] in crules.pronoun:
                    hint="Incorrect answer:If a clause has introductory words such as [although, as, because, if, since, when, while],Put a Comma to seperate the following clause."
                    mandlst.append(hint)  
   #---------------------------type10comma.py----------------------------------------------------------------
                for j in c:
                    if j == "Rs":
                        phrase="".join(b)
                        oned=re.findall("\d+",phrase)
                        if len(oned)!=0:
                       
                            if b[i-1]=="Rs" and b[i+1]==oned[0]:
                                hint="InCorrect Answer:You should use a fullstop after keyword {Rs]"
                                mandlst.append(hint)
                            if b[i-3]=="Rs" and b[i-1]==oned[0] and b[i+1]==oned[1]:
                                hint="correct Answer:Comma used to seperate amount above 999"
                                correctlst.append(hint)
                                
                            if (b[i-3]==oned[0]  or b[i-1]==oned[1]) and c[i]==";":
                                hint="InCorrect Answer:Never END a sentence with a semicolon"
                                mandlst.append(hint)
                     #-----------type11date.py----------------------------------------------------------------
               
                if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                    hint="InCorrect Answer:Comma should be used after a date, when it is followed by a year."
                    mandlst.append(hint)
                    
                if (b[i-1]==str(parse(co,fuzzy=True).year) and b[i-1]!=oned[1]) and c[i]==";" and c[i+1]==" ":
                    hint="InCorrect Answer:Sentence should be ended with a FULLSTOP"
                    mandlst.append(hint)  
                if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                    hint="InCorrect Answer:A comma should be used after a month, when it is followed by just a date(no year mentioned)."
                    mandlst.append(hint)
                if b[i-1]==str(parse(co,fuzzy=True).day) and c[i]==";" and c[i+1]==" ":
                    hint="InCorrect Answer:Sentence should be ended with a FULLSTOP"
                    mandlst.append(hint)    
                      
                if b[i-1] in crules.weekdays and b[i+1] in crules.months :
                    hint="InCorrect Answer:A comma should be used after a weekday, when it is followed by a month and date."
                    mandlst.append(hint)    
                if b[i-3]==str(parse(co,fuzzy=True).day) and b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                    hint="InCorrect Answer:Put a comma just after the month,if the date format is date-month-year"
                    mandlst.append(hint)
                
##                if (b[i-1] in crules.onoun and (b[i+1] in crules.article)):
##                    hint="InCorrect Answer:A comma should be used after an object noun, when you are trying to list 2 or more nouns."
##                    mandlst.append(hint)     


                            
 #---------------------------------------------------<m> with Comma-------------------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):
                  #---------------------------type10comma.py----------------------------------------------------------------
                for j in c:
                    if j == "Rs":
                        phrase="".join(b)
                        oned=re.findall("\d+",phrase)
                        if len(oned)!=0:
                
                            
                        #print("oned",oned[0],oned[1])
                            if b[i-1]=="Rs" and b[i+1]==oned[0]:
                                hint="InCorrect Answer:You should use a fullstop after keyword {Rs]"
                                mandlst.append(hint)
                            if b[i-3]=="Rs" and b[i-1]==oned[0] and b[i+1]==oned[1]:
                                hint="Correct Answer:Comma used to seperate amount above 999"
                                mandlst.append(hint)
                                
                            if (b[i-3]==oned[0]  or b[i-1]==oned[1]) and c[i]==",":
                                hint="InCorrect Answer:END a sentence with a fullstop"
                                mandlst.append(hint)
#-----------------------------------------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.pronoun and c[i]=="," and c[i+1]==" ":  
                    hint="InCorrect Answer. End the sentence with a Fullstop"
                    mandlst.append(hint)
                if b[i-1] in crules.snoun and c[i]=="," and c[i+1]==" ":  
                    hint="InCorrect Answer. End the sentence with a Fullstop"
                    mandlst.append(hint)                             
                                    
               
                if b[i-1] in crules.onoun and b[i+1] in crules.conjadv: #-------------type6.py
                    hint="InCorrect Answer.A FULLSTOP is used to seperate two complete sentences."
                    mandlst.append(hint)
                if b[i-1] in crules.oadverblst and c[i]=="," and c[i+1]==" ":  
                    hint="InCorrect Answer. End the sentence with a Fullstop"
                    mandlst.append(hint)
                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
                    hint="InCorrect Answer:Always put  a period after the title"
                    mandlst.append(hint)
                
                
                if b[i-1] in crules.onoun and b[i+1] in crules.pronoun :
                    hint="Correct answer:If a clause has introductory words such as [although, as, because, if, since, when, while],Put a Comma to seperate the following clause."
                    correctlst.append(hint)  
                                
#-----------------------------                    
        
               
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb) or (b[i+1] in crules.verb) :    
                    hint="Correct Answer:A comma can be used to seperate an adjective phrase from the verbphrase"
                    correctlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.verb1):    
                    hint="Correct Answer:Put a Comma between two clauses"
                    correctlst.append(hint)    
                if (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="Correct Answer:A comma should be used a relative clause follows the main subject."
                    correctlst.append(hint)
               
                if (b[i-1] in crules.onoun) and (b[i+1] in crules.article):    
                    hint="Correct Answer:A comma should be used after an object noun, when you are trying to list 2 or more nouns."
                    correctlst.append(hint)
                                  
               
      #-----------type11date.py----------------------------------------------------------------    
                try:
                    if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        hint="Correct Answer:A comma should be used after a date, when it is followed by a year."
                        correctlst.append(hint)
                    if (b[i-1]==(str(parse(co, fuzzy=True).year)) and b[i-1]!=oned[1]) and c[i]==",":
                        hint="InCorrect Answer:Sentence should be ended with a FULLSTOP"
                        mandlst.append(hint)
                    if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                        hint="Correct Answer:A comma should be used after a month, when it is followed by just a date(no year mentioned)."
                        correctlst.append(hint)
                    if b[i-1]==str(parse(co,fuzzy=True).day) and c[i]=="," and c[i+1]==" ":
                        hint="InCorrect Answer:Sentence should be ended with a FULLSTOP"
                        mandlst.append(hint)    
                    if b[i-3]==str(parse(co,fuzzy=True).day) and b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        hint="Correct Answer:Put a comma just after the month,if the date format is date-month-year"
                        correctlst.append(hint) 
                         
                    if b[i-1] in crules.weekdays and b[i+1] in crules.months :
                        hint="Correct Answer:A comma should be used after a weekday, when it is followed by a month and date."
                        correctlst.append(hint) 
                   
                    if b[i-1] in crules.onoun and b[i+1] in crules.pronoun :
                        hint="correct answer:If a clause has introductory words such as [although, as, because, if, since, when, while],Put a Comma to seperate the following clause."
                        correctlst.append(hint)

                except:
                    pass
                    
              #---------------------------type10comma.py----------------------------------------------------------------
                for j in c:
                    if j == "Rs":
                        phrase="".join(b)
                        oned=re.findall("\d+",phrase)
                        if len(oned)==0:
                            
                        #print("oned",oned[0],oned[1])
                            if b[i-1]=="Rs" and b[i+1]==oned[0]:
                                hint="InCorrect Answer:You should not use a comma after keyword {Rs]"
                                mandlst.append(hint)
                            if b[i-3]=="Rs" and b[i-1]==oned[0] and b[i+1]==oned[1]:
                                hint="correct Answer:Comma used to seperate amount above 999"
                                correctlst.append(hint)
                                
                            if b[i-3]=="Rs" and (b[i-1]==oned[1]  or b[i-1]==oned[0]) and c[i]==",":
                                hint="InCorrect Answer:Never END a sentence with a comma"
                                mandlst.append(hint)

               
                            
    #---------------------------------------------------<m> with Fullstop--------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                
                #---------------------------type10comma.py----------------------------------------------------------------
                for j in c:
                    if j == "Rs":
                        phrase="".join(b)
                        oned=re.findall("\d+",phrase)
                        if len(oned)!=0:
                          
                            if b[i-1]=="Rs" and b[i+1]==oned[0]:
                                hint="Correct Answer:You should use a fullstop after keyword {Rs]"
                                correctlst.append(hint)
                            if b[i-3]=="Rs" and b[i-1]==oned[0] and b[i+1]==oned[1]:
                                hint="correct Answer:Comma used to seperate amount above 999"
                                correctlst.append(hint)
                                
                            if (b[i-3]==oned[0]  or b[i-1]==oned[0]) and c[i]==".":
                                hint="Correct Answer:END a sentence with a fullstop"
                                correctlst.append(hint)
 
                   
                if (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="InCorrect Answer:Never usea fullstop before a sentence ends!No need of a period between the noun and the article."
                    mandlst.append(hint)
                onounlst=list(set(crules.onoun) & set(b))
                if len(onounlst) > 2:
                    if (b[i-1] in crules.onoun and (b[i+1] in crules.article)):
                
                        hint="InCorrect Answer:A comma should be used after an object noun, when you are trying to list 2 or more nouns."
                        mandlst.append(hint) 
                   
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb) or b[i+1] in crules.verb:    
                    hint="InCorrect Answer:Never use fullstop before a sentence ends!No need of a period between the common noun and the verb."
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.verb1):    
                    hint="InCorrect Answer:Put a Comma between two clauses"
                    mandlst.append(hint)    
                if b[i-1] in crules.title and b[i+1] in crules.snoun:
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always put a period/fullstop after a title"
                
                    correctlst.append(hint)
                    
                if (b[i-1] in crules.onoun) and c[i]=="." and c[i+1]==" ":
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                
                    correctlst.append(hint)
                if b[i-1] in crules.pronoun and c[i]=="." and c[i+1]==" ":  
                    hint="Correct Answer. End the sentence with a Fullstop"
                    correctlst.append(hint)
                if b[i-1] in crules.snoun and c[i]=="." and c[i+1]==" ":  
                    hint="Correct Answer. End the sentence with a Fullstop"
                    correctlst.append(hint)                             
                               
               
                if b[i-1] in crules.onoun and b[i+1] in crules.conjadv: #-------------type6.py
                    hint="Correct Answer.A FULLSTOP is used to seperate two complete sentences."
                    correctlst.append(hint)
                if b[i-1] in crules.oadverblst and c[i]=="." and c[i+1]==" ":  
                    hint="Correct Answer. End the sentence with a Fullstop"
                    correctlst.append(hint)
                
                
                if b[i-1] in crules.onoun and b[i+1] in crules.pronoun :
                    hint="Incorrect answer:If a clause has introductory words such as [although, as, because, if, since, when, while],Put a Comma to seperate the following clause."
                    mandlst.append(hint)  
                             
                     #-----------type11date.py----------------------------------------------------------------
                try:    
                    co=co.replace(".","?")
                    if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        hint="InCorrect Answer:Is there a need of fullstop after a date, when it is followed by a year."
                        mandlst.append(hint)
                        
                    if b[i-1]==str(parse(co,fuzzy=True).year) and c[i]=="." and c[i+1]==" ":
                        hint="Correct Answer:Sentence should be ended with a FULLSTOP"
                        correctlst.append(hint)  
                    if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                        hint="InCorrect Answer:A comma should be used after a month, when it is followed by just a date(no year mentioned)."
                        mandlst.append(hint)
                    if b[i-1]==str(parse(co,fuzzy=True).day) and c[i]=="." and c[i+1]==" ":
                        hint="InCorrect Answer:Sentence should be ended with a FULLSTOP"
                        mandlst.append(hint)    
                          
                    if b[i-1] in crules.weekdays and b[i+1] in crules.months :
                        hint="InCorrect Answer:A comma should be used after a weekday, when it is followed by a month and date."
                        mandlst.append(hint)    
                    if b[i-3]==str(parse(co,fuzzy=True).day) and b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        hint="InCorrect Answer:Put a comma just after the month,if the date format is date-month-year"
                        mandlst.append(hint)
                except:
                    pass
 #--------------------------------------------------------<w> with comma-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==","):
                
#-----------------------------------type1.py----------------------------------------------------------
                if b[i-1] in crules.verb or b[i-1] in crules.verb1 and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:No need to put a comma after a noun especially when there is no enumeration..."
                    hintlst.append(hint)
               
                if b[i-1] in crules.onoun and b[i+1] in crules.madverb:
                    hint="Read The manual again, HINT:Noun when followed by a modifying adverb,don't put a comma in between"
                    hintlst.append(hint)
                if b[i-1] in crules.madverb and b[i+1] in crules.adverb:
                    hint="Read The manual again, HINT:Modifying adverb like extremely,very etc shoud not be seperated from main adverbs using a comma"
                    hintlst.append(hint)
#--------------------------------compound.py----------------------------------------
                if b[i-1] in crules.cordconj and b[i+1] in crules.verb:
                    hint="Read The manual again, HINT:Avoid comma after a Conjunction like [and] or [but]"
                    hintlst.append(hint)
               
#--------------------------------inrocomma.py---------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.intro_words and b[i+1] in crules.snoun:
                    hint="Read The manual again, HINT:Avoid comma after Introductory wirds like [while/Although] etc."
                    hintlst.append(hint)
                if b[i-1] in crules.snoun and b[i+1] in crules.vbz:
                    hint="Read The manual again, HINT:No need to add a comma after a noun, when it is followed by [is/was]"
                    hintlst.append(hint)
                if b[i-1] in crules.vbz and b[i+1] in crules.verbing:
                    hint="Read The manual again, HINT:No need to add a comma after [is/was], when it is followed by a verb"
                    hintlst.append(hint)
                if b[i-1] in crules.verbing and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:No need to add a comma after a verb ,in a verbphrase"
                    hintlst.append(hint)
                  
                if b[i-1] in crules.pronoun and b[i+1] in crules.verb:
                    hint="Read The manual again, HINT:No need to add a comma after a pronoun"
                    
                    hintlst.append(hint)
                if b[i-1] in crules.pronoun and b[i+1] in crules.adj:
                    hint="Read The manual again, HINT:No need to add a comma after a pronoun"
                    
                    hintlst.append(hint)
                #--------------type6.py-------------------------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
                  hint="Read The manual again, HINT:No need to add a comma within a noun/adjective phrase[after a noun/ad]"
                  hintlst.append(hint)
                if b[i-1] in crules. pronoun and b[i+1] in crules.hverb:
                  hint="Read The manual again, HINT:No need to add a comma after a pronoun"
                  hintlst.append(hint)
                if b[i-1] in crules.hverb and b[i+1] in crules.neg:
                  hint="Read The manual again, HINT:No need to add a comma in between a helping verb like (can,could) and a negation:not"
                  hintlst.append(hint)
                if b[i-1] in crules. hverb and b[i+1] in crules.verb:
                  hint="Read The manual again, HINT:No need to add a comma in between a helping verb like (can,could) and a verb"
                  hintlst.append(hint)
                if b[i-1] in crules.neg and b[i+1] in crules.verb:
                  hint="Read The manual again, HINT:No need to add a comma after a negation"
                  hintlst.append(hint)
                
                #--------------type3.py-----------------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.adj and b[i+1] in crules.cnoun:
                  hint="Read The manual again, HINT:No need to seperate an adjective and a commoun noun with comma"
                  hintlst.append(hint)
                if b[i-1] in crules. hverb and b[i+1] in crules.verb:
                    hint="Read The manual again, HINT:Caution! Helping verb is supporting the verb.No need to seperate with a comma"
                    hintlst.append(hint)
                
                if b[i-1] in crules.article and b[i+1] in crules.adj:
                    hint="Read The manual again, HINT:No need to seperate an article and a adjective with comma"
                    hintlst.append(hint)
                 
                if b[i-1] in crules.verb and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:No need to put a comma before an article if it is preceeded by a verb"
                    hintlst.append(hint)
                if b[i-1] in crules. article and b[i+1] in crules.adj:
                    hint="Read The manual again, HINT:Don't put a comma in between an adjective phrase or noun phrase,especially after an article like [a,an]"
                    hintlst.append(hint)
                
                if b[i-1] in crules.cordconj and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:Avoid Comma before/after a Conjunction like [and] or [but]"
                    hintlst.append(hint)
                #-----------------------------type4.py------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.hverb and b[i+1] in crules.verb:
                    hint="Read The manual again, HINT:No need to put a comma in between a verbphrase..."
                    hintlst.append(hint)
                    
                if b[i-1] in crules.hverb and b[i+1] in crules.verb:
                    hint="Read The manual again, HINT:No need to put a comma in between a verbphrase..."
                    hintlst.append(hint)    
                if b[i-1] in crules.article and b[i+1] in crules.onoun:
                    hint="Read The manual again, HINT:No need to put a comma between a article and a noun.Here article is used to modify the noun."
                    hintlst.append(hint)
                if b[i-1] in crules.article and b[i+1] in crules.adj:
                    hint="Read The manual again, HINT:No need to put a FULLSTOP between a article and an adjective.Here article is used to modify the noun."
                    hintlst.append(hint)     
                if b[i-1] in crules.onoun and b[i+1] in crules.cordconj:
                    hint="Read The manual again, HINT:No need to put a comma before/after conjunctions like [and,but] etc."
                    hintlst.append(hint)
                  
                if b[i-1] in crules.cordconj and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:No need to put a comma before/after conjunctions like [and,but] etc."
                    hintlst.append(hint)
            #-----------------------------type10comma.py---------------------------------------------------------------------------------------------------

                if b[i-1] in crules.snoun and b[i+1] in crules.verb:
                    hint="Read The manual again, HINT:No need to put a comma after a noun when it is followed by a verb"
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
                    hint="Read The manual again, HINT:No need to put a comma after a verb when it is followed by a pronoun"
                    hintlst.append(hint)
                if b[i-1] in crules.pronoun and b[i+1] in crules.adj:
                    hint="Read The manual again, HINT:No need to put a comma after a pronoun when it is followed by a verbphrase/adjective"
                    hintlst.append(hint)
                
                if b[i-1] in crules.verb and b[i+1]=="Rs":
                    hint="Read The manual again, HINT:No need to put a comma after a verb like paid especially when an amount is specified afterwards"
                    hintlst.append(hint)    
                
                phrase="".join(b)
                oned=re.findall("\d+",phrase)                                                                                                                                                                                                                
                #print("oned",oned[0],oned[1])
                if len(oned)!=0 :
                    if b[i-1] == oned[1] and b[i+1] in crules.prep:
                        hint="Incorrect Answer, HINT: No need of a comma after the amount when followed by a preposition"
                        hintlst.append(hint)
                    
                if b[i-1] in crules.onoun and b[i+1] in crules.prep:
                    hint="Incorrect Answer, HINT: Is there a need of comma after a noun when it is followed by a preposition"
                    hintlst.append(hint)
                    
                if b[i-1] in crules.prep and b[i+1] in crules.pronoun:
                    hint="Incorrect Answer, HINT: Is there a need of comma between a preposition and a pronoun"
                    hintlst.append(hint)
                    
                if b[i-1] in crules.prep and b[i+1]=="Rs":
                    hint="Incorrect Answer, HINT: No comma needed after the preposition"
                    hintlst.append(hint)
    #-----------------------------type11date.py---------------------------------------------------------------------------------------------------
                try:
                   
                    if b[i-1] in crules.prep and b[i+1] in crules.months:
                        hint="Read the manual again, HINT:No need of a comma after a preposition when it is followed by a month"
                        hintlst.append(hint)
                       
                    if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                        hint="Read the manual again, HINT:No need of a comma in the format - month followed by a date"
                        hintlst.append(hint)

                    if b[i-1] in crules.vbz and b[i+1] in crules.verb:
                        hint="Read the manual again, HINT:No need of a comma after ['is','was'] when it is followed by a verb"
                        hintlst.append(hint)
                    if b[i-1] in crules.verb and b[i+1] in crules.prep:
                        hint="Read the manual again, HINT:No need of a comma after a verb when it is followed by a preposition"
                        hintlst.append(hint)
                    if b[i-1] in crules.prep and b[i+1] in crules.weekdays:
                        hint="Read the manual again, HINT:No need of a comma after a prep when it is followed by a weekday"
                    if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1] in crules.months  :
                        hint="Read the manual again, HINT:No need of a comma after a date when it is followed by a month and a year if the date format is [15 March 2003]"
                        hintlst.append(hint)
                       
                    if b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        hint="Read the manual again, HINT:No need of a comma after a month when it is followed by a year if the date format is [15 March 2003]" 
                        hintlst.append(hint)
                except:
                    
                    pass                    
#--------------------------------------------------------<w> with FULLSTOP-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]=="."):
                

#-----------------------------------type1.py----------------------------------------------------------
                if b[i-1] in crules.verb or b[i-1] in crules.verb1 and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:No need to put a FULLSTOP after a noun especially when there is no enumeration..."
                    hintlst.append(hint)
               
                if b[i-1] in crules.onoun and b[i+1] in crules.madverb:
                    hint="Read The manual again, HINT:Noun when followed by a modifying adverb,don't put a FULLSTOP in between"
                    hintlst.append(hint)
                if b[i-1] in crules.madverb and b[i+1] in crules.adverb:
                    hint="Read The manual again, HINT:Modifying adverb like extremely,very etc shoud not be seperated from main adverbs using a FULLSTOP"
                    hintlst.append(hint)
#--------------------------------compound.py----------------------------------------
                if b[i-1] in crules.cordconj and b[i+1] in crules.verb:
                    hint="Read The manual again, HINT:Avoid Fullstop after a Conjunction like [and] or [but]"
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
                    hint="Read The manual again, HINT:No need to add a Fullstop after a verb, when it is followed by a neuter pronoun(e.g. it)"
                    hintlst.append(hint)
#--------------------------------inrocomma.py---------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.intro_words and b[i+1] in crules.snoun:
                    hint="Read The manual again, HINT:Avoid FULLSTOP after Introductory wirds like [while/Although] etc."
                    hintlst.append(hint)
                
               
                if (b[i-1] in crules.verbing or  b[i-1] in crules.verb)  and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:No need to add a FULLSTOP after a verb ,in a verbphrase"
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in (crules.prep):
                    hint="Read The manual again, HINT:No need to add a FULLSTOP after a verb, when it is followed by a preposition"
                    hintlst.append(hint)  
                if b[i-1] in crules.pronoun and b[i+1] in crules.verb:
                    hint="Read The manual again, HINT:No need to add a FULLSTOP after a pronoun"
                    
                    hintlst.append(hint)
                        #--------------type3.py-----------------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.adj and b[i+1] in crules.cnoun:
                  hint="Read The manual again, HINT:No need to seperate an adjective and a commoun noun with FULLSTOP"
                  hintlst.append(hint)
                if b[i-1] in crules. hverb and b[i+1] in crules.verb:
                    hint="Read The manual again, HINT:Caution! Helping verb is supporting the verb.No need to seperate with a FULLSTOP"
                    hintlst.append(hint)
                
                if b[i-1] in crules.article and b[i+1] in crules.adj:
                    hint="Read The manual again, HINT:No need to seperate an article and a adjective with FULLSTOP"
                    hintlst.append(hint)
                 
                if b[i-1] in crules.verb and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:No need to put a FULLSTOP before an article if it is preceeded by a verb"
                    hintlst.append(hint)
                if b[i-1] in crules. article and b[i+1] in crules.adj:
                    hint="Read The manual again, HINT:Don't put a FULLSTOP in between an adjective phrase or noun phrase,especially after an article like [a,an]"
                    hintlst.append(hint)
                
                if b[i-1] in crules.cordconj and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:Avoid Punctuation before/after a Conjunction like [and] or [but]"
                    hintlst.append(hint)
                    
                #-----------------------------type4.py--------------------------------------------
                if b[i-1] in crules.hverb and b[i+1] in crules.verb:
                    hint="Read The manual again, HINT:No need to put a FULLSTOP in between a verbphrase..."
                    hintlst.append(hint)
                     
                if b[i-1] in crules.article and b[i+1] in crules.onoun:
                    hint="Read The manual again, HINT:No need to put a FULLSTOP between a article and a noun.Here article is used to modify the noun."
                    hintlst.append(hint)
                if b[i-1] in crules.article and b[i+1] in crules.adj:
                    hint="Read The manual again, HINT:No need to put a FULLSTOP between a article and an adjective.Here article is used to modify the noun."
                    hintlst.append(hint)    
                if b[i-1] in crules.onoun and b[i+1] in crules.cordconj:
                    hint="Read The manual again, HINT:No need to put a FULLSTOP before conjunctions like and,but etc."
                    hintlst.append(hint)
                if b[i-1] in crules.cordconj and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:No need to put a FULLSTOP after conjunctions like and,but etc."
                    hintlst.append(hint)
                if b[i-1] in crules.pronoun and b[i+1] in crules.adj:
                    hint="Read The manual again, HINT:No need to put a FULLSTOP after a pronoun"
                    hintlst.append(hint)   
                 #--------------type6.py------------------------------------------------------------------------------------------------------
            
                if b[i-1] in crules. pronoun and b[i+1] in crules.hverb:
                  hint="Read The manual again, HINT:No need to add a fullstop after a pronoun"
                  hintlst.append(hint)
                if b[i-1] in crules.hverb and b[i+1] in crules.neg:
                  hint="Read The manual again, HINT:No need to add a fullstop in between a helping verb like (can,could) and a negation:not"
                  hintlst.append(hint)
                if b[i-1] in crules. hverb and b[i+1] in crules.verb:
                  hint="Read The manual again, HINT:No need to add a fullstop in between a helping verb like (can,could) and a verb"
                  hintlst.append(hint)
                if b[i-1] in crules.neg and b[i+1] in crules.verb:
                  hint="Read The manual again, HINT:No need to add a fullstop after a negation"
                  hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
                  hint="Read The manual again, HINT:No need to add a fullstop after a verb, when it is followed by a neuter pronoun(e.g. it)"
                  hintlst.append(hint) 
              
                 #-----------------------------type10comma.py---------------------------------------------------------------------------------------------------

                if b[i-1] in crules.snoun and b[i+1] in crules.verb:
                    hint="Incorrect Answer, HINT: No need of a FULLSTOP between a noun and a verb"
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
                    hint="Incorrect Answer, HINT: No need of a FULLSTOP after a verb"
                    hintlst.append(hint)
                if b[i-1] in crules.pronoun and b[i+1] in crules.adj:
                    hint="Incorrect Answer, HINT: No need to seperate a pronoun and an adjective using a FULLSTOP"
                    hintlst.append(hint)
                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
                    hint="Incorrect Answer, HINT: Don't add any punctuation within an adjective phrase"
                    hintlst.append(hint)
                    
                     
                phrase="".join(b)
                oned=re.findall("\d+",phrase)
                #print("oned",oned[0],oned[1])
                if len(oned)!=0:
                    if b[i-1]==oned[1] and b[i+1]==crules.prep:
                        hint="Incorrect Answer, HINT: No need of a FULLSTOP after a number"
                        hintlst.append(hint)
                                           
              
                if b[i-1] in crules.onoun and b[i+1] in crules.prep:
                    hint="Incorrect Answer, HINT: Is there a need of FULLSTOP after a noun when it is followed by a preposition"
                    hintlst.append(hint)
                if b[i-1] in crules.prep and b[i+1] in crules.pronoun:
                    hint="Incorrect Answer, HINT: Is there a need of FULLSTOP between a preposition and a pronoun"
                    hintlst.append(hint)
                if b[i-1] in crules.prep and b[i+1]=="Rs":
                    hint="Incorrect Answer, HINT: No FULLSTOP needed after the preposition"
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1]=="Rs":
                    hint="Incorrect Answer, HINT: No need of a FULLSTOP after a verb/before the keyword Rs"
                    hintlst.append(hint)
                    
                    #-----------------type11date.py--------------------------------
               
                if b[i-1] in crules.onoun and b[i+1] in crules.prep:
                    hint="Read the manual again, HINT:No need of a FULLSTOP after an object noun when it is followed by a preposition"
                    hintlst.append(hint) 
               
                if b[i-1] in crules.prep and b[i+1] in crules.months:
                    hint="Read the manual again, HINT:No need of a FULLSTOP after a preposition when it is followed by a month"
                    hintlst.append(hint)
                try:
                    #if b[i] in crules.
                    if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                        hint="Read the manual again, HINT:No need of a FULLSTOP after a month when it is followed by a date"
                        hintlst.append(hint) 
                    if b[i-1]  in crules.snoun and b[i+1] in crules.vbz:
                        hint="Read the manual again, HINT:No need of a FULLSTOP after a noun when it is followed by a ['is','was']"
                        hintlst.append(hint) 
                    if b[i-1] in crules.vbz and b[i+1] in crules.verb:
                        hint="Read the manual again, HINT:No need of a FULLSTOP after ['is','was'] when it is followed by a verb"
                        hintlst.append(hint) 
                   
                    if b[i-1] in crules.prep and b[i+1] in crules.weekdays:
                        hint="Read the manual again, HINT:No need of a FULLSTOP after a prep when it is followed by a weekday"
                        hintlst.append(hint) 
                    if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1] in crules.months and b[i+2]==str(str(parse(co, fuzzy=True).year)):
                        hint="Read the manual again, HINT:No need of a FULLSTOP after a date when it is followed by a month and a year if the date format is [15 March 2003]"
                        hintlst.append(hint) 
                    if b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)) and b[i+2]==None:
                        hint="Read the manual again, HINT:No need of a FULLSTOP after a month when it is followed by a year if the date format is [15 March 2003]"
                        hintlst.append(hint)  
                    
                except:
                    pass

#--------------------------------------------------------<w> with SEMICOLON-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==";"):
               #-----------------------------------type1.py----------------------------------------------------------
                if b[i-1] in crules.verb or b[i-1] in crules.verb1 and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:No need to put a SEMICOLON after a noun especially when there is no enumeration..."
                    hintlst.append(hint)
               
                if b[i-1] in crules.onoun and b[i+1] in crules.madverb:
                    hint="Read The manual again, HINT:Noun when followed by a modifying adverb,don't put a SEMICOLON in between"
                    hintlst.append(hint)
                if b[i-1] in crules.madverb and b[i+1] in crules.adverb:
                    hint="Read The manual again, HINT:Modifying adverb like extremely,very etc shoud not be seperated from main adverbs using a SEMICOLON"
                    hintlst.append(hint)
#--------------------------------compound.py----------------------------------------
                if b[i-1] in crules.cordconj and b[i+1] in crules.verb:
                    hint="Read The manual again, HINT:Avoid SEMICOLON after a Conjunction like [and] or [but]"
                    hintlst.append(hint)
              
#--------------------------------inrocomma.py---------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.intro_words and b[i+1] in crules.snoun:
                    hint="Read The manual again, HINT:Avoid SEMICOLON after Introductory wirds like [while/Although] etc."
                    hintlst.append(hint)
                if b[i-1] in crules.snoun and b[i+1] in crules.vbz:
                    hint="Read The manual again, HINT:No need to add a SEMICOLON  after a noun, when it is followed by [is/was]"
                    hintlst.append(hint)
                if b[i-1] in crules.vbz and (b[i+1] in crules.verbing or b[i+1] in crules.verb):
                    hint="Read The manual again, HINT:No need to add a SEMICOLON after [is/was], when it is followed by a verb"
                    hintlst.append(hint)
                if (b[i-1] in crules.verbing or  b[i-1] in crules.verb)  and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:No need to add a SEMICOLON after a verb ,in a verbphrase"
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in (crules.prep):
                    hint="Read The manual again, HINT:No need to add a SEMICOLON after a verb, when it is followed by a preposition"
                    hintlst.append(hint)  
                if b[i-1] in crules.pronoun and b[i+1] in crules.verb:
                    hint="Read The manual again, HINT:No need to add a SEMICOLON after a pronoun"
                    hintlst.append(hint)

                if b[i-1] in crules.pronoun and b[i+1] in crules.adj:
                    hint="Read The manual again, HINT:No need to add a SEMICOLON after a pronoun"
                    hintlst.append(hint)   
                  #-----------------------------type4.py--------------------------------------------
                if b[i-1] in crules.hverb and b[i+1] in crules.verb:
                    hint="Read The manual again, HINT:No need to put a SEMICOLON in between a verbphrase..."
                    hintlst.append(hint)
                     
                if b[i-1] in crules.article and b[i+1] in crules.onoun:
                    hint="Read The manual again, HINT:No need to put a SEMICOLON between a article and a noun"
                    hintlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.cordconj:
                    hint="Read The manual again, HINT:No need to put a SEMICOLON before conjunctions like and,but etc."
                    hintlst.append(hint)
                if b[i-1] in crules.cordconj and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:No need to put a SEMICOLON after conjunctions like and,but etc."
                    hintlst.append(hint)
                if b[i-1] in crules.article and b[i+1] in crules.adj:
                    hint="Read The manual again, HINT:No need to put a SEMICOLON between a article and an adjective.Here article is used to modify the noun."
                    hintlst.append(hint) 
                          #--------------type3.py-----------------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.adj and b[i+1] in crules.cnoun:
                  hint="Read The manual again, HINT:No need to seperate an adjective and a commoun noun with a semicolon"
                  hintlst.append(hint)
                if b[i-1] in crules. hverb and b[i+1] in crules.verb:
                    hint="Read The manual again, HINT:Caution! Helping verb is supporting the verb.No need to seperate with a semicolon"
                    hintlst.append(hint)
                
                if b[i-1] in crules.article and b[i+1] in crules.adj:
                    hint="Read The manual again, HINT:No need to seperate an article and a adjective with semicolon"
                    hintlst.append(hint)
                 
                if b[i-1] in crules.verb and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:No need to put a semicolon before an article if it is preceeded by a verb"
                    hintlst.append(hint)
                if b[i-1] in crules. article and b[i+1] in crules.adj:
                    hint="Read The manual again, HINT:Don't put a semicolon in between an adjective phrase or noun phrase,especially after an article like [a,an]"
                    hintlst.append(hint)
                
                if b[i-1] in crules.cordconj and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:Avoid Punctuation before/after a Conjunction like [and] or [but]"
                    hintlst.append(hint)
                 #-----------------------------type10comma.py---------------------------------------------------------------------------------------------------

                if b[i-1] in crules.snoun and b[i+1] in crules.verb:
                    hint="Incorrect Answer, HINT: No need of a semicolon between a noun and a verb"
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
                    hint="Incorrect Answer, HINT: No need of a semicolon after a verb"
                    hintlst.append(hint)
                if b[i-1] in crules.pronoun and b[i+1] in crules.adj:
                    hint="Incorrect Answer, HINT: No need to seperate a pronoun and an adjective using a semicolon"
                    hintlst.append(hint)
                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
                    hint="Incorrect Answer, HINT: Don't add any punctuation within an adjective phrase"
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1]=="Rs":
                    hint="Incorrect Answer, HINT: No need of a semicolon after a verb"
                    hintlst.append(hint)    
                     
                phrase="".join(b)
                oned=re.findall("\d+",phrase)
                #print("oned",oned[0],oned[1])
                if len(oned)!=0:
                    if b[i-1]==oned[1] and b[i+1]==crules.prep:
                        hint="Incorrect Answer, HINT: No need of a semicolon after a number"
                        hintlst.append(hint)
                                           
              
                if b[i-1] in crules.onoun and b[i+1] in crules.prep:
                    hint="Incorrect Answer, HINT: Is there a need of semicolon after a noun when it is followed by a preposition"
                    hintlst.append(hint)
                if b[i-1] in crules.prep and b[i+1] in crules.pronoun:
                    hint="Incorrect Answer, HINT: Is there a need of semicolon between a preposition and a pronoun"
                    hintlst.append(hint)
                if b[i-1] in crules.prep and b[i+1]=="Rs":
                    hint="Incorrect Answer, HINT: No semicolon needed after the preposition"
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1]=="Rs":
                    hint="Incorrect Answer, HINT: No need of a semicolon after a verb/before the keyword Rs"
                    hintlst.append(hint)   
                #--------------type6.py------------------------------------------------------------------------------------------------------
##                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
##                  hint="Read The manual again, HINT:No need to add a SEMICOLON in between a noun/adjective phrase"
##                  hintlst.append(hint)
                if b[i-1] in crules. pronoun and b[i+1] in crules.hverb:
                  hint="Read The manual again, HINT:No need to add a SEMICOLON after a pronoun"
                  hintlst.append(hint)
                if b[i-1] in crules.hverb and b[i+1] in crules.neg:
                  hint="Read The manual again, HINT:No need to add a SEMICOLON in between a helping verb like (can,could) and a negation:not"
                  hintlst.append(hint)
                if b[i-1] in crules. hverb and b[i+1] in crules.verb:
                  hint="Read The manual again, HINT:No need to add a SEMICOLON in between a helping verb like (can,could) and a verb"
                  hintlst.append(hint)
                if b[i-1] in crules.neg and b[i+1] in crules.verb:
                  hint="Read The manual again, HINT:No need to add a SEMICOLON after a negation"
                  hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
                  hint="Read The manual again, HINT:No need to add a SEMICOLON after a verb, when it is followed by a pronoun"
                  hintlst.append(hint)


   #-----------------------------type11date.py---------------------------------------------------------------------------------------------------
                try:
                   
                    if b[i-1] in crules.prep and b[i+1] in crules.months:
                        hint="Read the manual again, HINT:No need of a SEMICOLON after a preposition when it is followed by a month"
                        hintlst.append(hint)
                       
                    if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day) and c[i]==" " and c[i+1]==" ":
                        hint="Read the manual again, HINT:No need of a SEMICOLON in the format - month followed by a date"
                        hintlst.append(hint)
    ##                if b[i-1]  in crules.snoun and b[i+1] in crules.vbz:
    ##                    hint="Read the manual again, HINT:No need of a comma after a noun when it is followed by a ['is','was']"
    ##                    hintlst.append(hint)
                   
                   
                    if b[i-1] in crules.prep and b[i+1] in crules.weekdays:
                        hint="Read the manual again, HINT:No need of a SEMICOLON after a prep when it is followed by a weekday"
                    if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1] in crules.months  :
                        hint="Read the manual again, HINT:No need of a SEMICOLON after a date when it is followed by a month and a year if the date format is [15 March 2003]"
                        hintlst.append(hint)
                       
                    if b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        hint="Read the manual again, HINT:No need of a SEMICOLON after a month when it is followed by a year if the date format is [15 March 2003]" 
                        hintlst.append(hint)
##                
                except:
                    pass

       
        return(hintlst,mandlst,correctlst,mandatory)    


    def commaone(b,c,correct,category,level,username,userid,eid,submittedtext):                
##    def commaone(self):
##        b=['John', '<w>', 'paid', '<w>', 'Rs', '<m>', '4', '<m>', '300', '<w>', 'for', '<w>', 'his', '<w>', 'adorable', '<w>', 'bicycle', '<m>']
##        =['John', ',', 'paid', '', 'Rs', ' ', '4', ' ', '300', ' ', 'for', ' ', 'his', ' ', 'adorable', ' ', 'bicycle',' ']
##        b=['Alice','<w>','bought','<w>','her','<w>','favorite','<w>','furniture','<w>','for','<w>','Rs','<m>','3','<m>','500','<m>']
##        c=['Alice',',','bought',',','her',',','favorite',',','furniture',',','for',' ','Rs','.','3',',','500','.']
##        b=['Mary','<w>','was','<w>','born','<w>','on','<w>','February','<m>','17','<m>','2009','<m>']
##        c=['Mary',',','was',',','born',',','on',',','February',',','17',',','2009','.']
####        b=['Mr', '<m>', 'John', '<m>', 'a', '<w>', 'charming', '<w>', 'gentleman', '<m>', 'might', '<w>', 'open', '<w>', 'a', '<w>', 'small', '<w>', 'cage', '<m>', 'Morever', '<m>', 'he', '<w>', 'might', '<w>', 'lift', '<w>', 'it', '<m>']
##                                                                                                                                                                    
##        c=['Mr', '.', 'John', ' ', 'a', ';', 'charming', '', 'gentleman', ',', 'might', ' ', 'open', ' ', 'a', ' ', 'small', '<w>', 'cage', '.', 'Morever', ' ', 'he', ' ', 'might', ' ', 'lift', ' ', 'it', '.']

##        c=['Sr', ';', 'Mary', ' ', 'a', ' ', 'generous', ' ', 'lady', ';', 'could', ' ', 'open', ' ', 'a', ' ', 'huge', ' ', 'cage', ' ', 'and', ' ', 'a', ' ', 'red', ' ', 'box',' ']
##        b=['Sr', '<m>', 'Mary', '<m>' , 'a', '<w>', 'generous', '<w>', 'lady', '<m>', 'could', '<w>', 'open', '<w>', 'a', '<w>', 'huge', '<w>', 'cage', '<w>', 'and', '<w>', 'a', '<w>', 'red', '<w>', 'box','<m>']
##        c=['Major', '.', 'John', '.', 'a', ',', 'charming', ' ', 'gentleman', '.', 'could', ',', 'open', ' ', 'a', ' ', 'box', ';', 'a', ' ', 'book', ',', 'and', ' ', 'a', ' ', 'cage', '.']
##        b=['Major', '<m>', 'John', '<m>', 'a', '<w>', 'charming', '<w>', 'gentleman', '<m>', 'could', '<w>', 'open', '<w>', 'a', '<w>', 'box', '<m>', 'a', '<w>', 'book', '<w>', 'and', '<w>', 'a', '<w>', 'cage', '<m>']
##        b=['Mr', '<m>', 'John', '<m>', 'a', '<w>', 'charming', '<w>', 'gentleman', '<m>', 'might', '<w>', 'open', '<w>', 'a', '<w>', 'small', '<w>', 'cage', '<m>', 'Morever', '<m>', 'he', '<w>', 'might', '<w>', 'lift', '<w>', 'it', '<m>']
##        c=['Mr', '', 'John', ' ', 'a', ',', 'charming', '', 'gentleman', ',', 'might', ' ', 'open', ',', 'a', ',', 'small', '<w>', 'cage', '.', 'Morever', ',', 'he', ' ', 'might', ',', 'lift', ' ', 'it', '.']
##        b=['John', '<w>', 'paid', '<w>', 'Rs', '<m>', '4', '<m>', '300', '<w>', 'for', '<w>', 'his', '<w>', 'adorable', '<w>', 'bicycle', '<m>']
##        c=['John', '.', 'paid', ';', 'Rs', ',', '4', ',', '300', ',', 'for', ' ', 'his', ' ', 'adorable', ' ', 'bicycle','.']
##        #Capt<m>John<m>a<w>generous<w>orator<m>could<w>open<w>a<w>huge<w>box<m>However<m>he<w>could<w>not<w>lift<w>it<m>
##        b=['Miss', '<m>', 'Alice', '<m>', 'a', '<w>', 'generous', '<w>', 'woman', '<m>', 'will', '<w>', 'open', '<w>', 'a', '<w>', 'book', '<m>', 'and', '<w>', 'a', '<w>', 'cage', '<m>']
##        c=['Miss', ' ', 'Alice', ' ', 'a', ' ', 'generous', ' ', 'woman', ' ', 'will', ' ', 'open', ' ', 'a', ' ', 'book', ' ', 'and', ' ', 'a', ' ', 'cage', ' ']
##        b=['James', '<w>', 'bought', '<w>', 'his', '<w>', 'costly', '<w>', 'furniture', '<w>', 'for', '<w>', 'Rs', '<m>', '3', '<m>', '500', '<m>', ' ']
##        c=['James', ' ', 'bought', ' ', 'his', ' ', 'costly', ' ', 'furniture', ' ', 'for', ' ', 'Rs', ' ', '3', ',', '500', '.', ' ']
##        b=['Dr', '.', 'James', '<m>', 'a', '<w>', 'charming', '<w>', 'orator', '<m>', 'drew', '<w>', 'a', '<w>', 'fantastic', '<w>', 'building', '<w>', 'and', '<w>', 'painted', '<w> ', 'it', '<m>']
##        c=['Dr', '.', 'James', ',', 'a', ' ', 'charming', ' ', 'orator', '.', 'drew', ' ', 'a', ' ', 'fantastic', ' ', 'building', ' ', 'and', ' ', 'painted', ' ', 'it', '.']
        b.append(" ")
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
        co="".join(c)
       
#---------------------------------------------------<m> with semicolon--------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==";"):
                  
                hint="SEMICOLON not needed.Click the appropriate sidepane and read the manuals"
                mandlst.append(hint)
                        
   
            
#---------------------------------------------------------<m> with no punctuation---------------------------------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==" "):
               
                hint="Punctuations are required at mandatory locations.Click the appropriate sidepane and read the manuals"
                mandlst.append(hint)            
                      
#---------------------------------------------------<m> with Comma--------------------------------------------------------------------------        
        for i in range(0,len(b)):
           
            if (b[i]=="<m>" and c[i]==","):

                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
                    hint="Correct Answer:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                    correctlst.append(hint)
                    
                    
                if (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="Correct Answer:A comma should be used when a relative clause follows the main subject."
                    correctlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="Correct Answer:A comma should be used when a relative clause follows the main subject."
                    correctlst.append(hint)
                if (b[i-1] in crules.onoun) and (b[i+1] in crules.pronoun):    
                    hint="correct answer:If a clause has introductory words such as [although, as, because, if, since, when, while],Put a Comma to seperate the following clause."    
                   
                    correctlst.append(hint)    
                 
                if (b[i-1] in crules.onoun) and (b[i+1] in crules.article):    
                    hint="Correct Answer:A comma should be used after an object noun, when you are trying to list 2 or more nouns."
                    correctlst.append(hint)
                 #-----------type6.py----------------------
                if b[i-1] in crules.conjadv and b[i+1] in crules.pronoun:
                    hint="Correct Answer:A comma is used to seperate a conjunctive adverb."
                    correctlst.append(hint) 
              
                             
                #-----------type11date.py----------------------------------------------------------------    
                try:
                    if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        hint="Correct Answer:A comma should be used after a date, when it is followed by a year."
                        correctlst.append(hint)
      
                    if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                        hint="Correct Answer:A comma should be used after a month, when it is followed by just a date(no year mentioned)."
                        correctlst.append(hint)
                       
                    if b[i-3]==str(parse(co,fuzzy=True).day) and b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                        hint="Correct Answer:Put a comma just after the month,if the date format is date-month-year"
                        correctlst.append(hint) 
                         
                    if b[i-1] in crules.weekdays and b[i+1] in crules.months :
                        hint="Correct Answer:A comma should be used after a weekday, when it is followed by a month and date."
                        correctlst.append(hint)

                except:
                   pass
                             
               
                 #---------------------------type10comma.py----------------------------------------------------------------
                for j in c:
                    if j == "Rs":
                        phrase="".join(b)
                        oned=re.findall("\d+",phrase)
                        if len(oned)!=0:
                       
                            if b[i-3]=="Rs" and b[i-1]==oned[0] and b[i+1]==oned[1]:
                                hint="Correct Answer:Comma is used to seperate amount above 999"
                                correctlst.append(hint)
                                
                           
    #---------------------------------------------------<m> with Fullstop---------------------------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
               
                #--------------------------------------------------
                if b[i-1] in crules.pronoun and c[i]=="." and c[i+1]==" ":  
                    hint="Correct Answer. End the sentence with a Fullstop"
                    correctlst.append(hint)
                if b[i-1] in crules.snoun and c[i]=="." and c[i+1]==" ":  
                    hint="Correct Answer. End the sentence with a Fullstop"
                    correctlst.append(hint)                             
                if b[i-1] in crules.onoun and c[i]=="." and c[i+1]==" ":  
                    hint="Correct Answer. End the sentence with a Fullstop"
                    correctlst.append(hint)                    
                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
                    hint="Correct Answer:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                    correctlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.conjadv: 
                    hint="Correct Answer.A FULLSTOP is used to seperate two complete sentences."
                    correctlst.append(hint)
                if b[i-1] in crules.oadverblst and c[i]=="." and c[i+1]==" ":  
                    hint="Correct Answer. End the sentence with a Fullstop"
                    correctlst.append(hint)
                if b[i-1] in crules.cnoun and b[i+1] in crules.hverb or b[i+1]in crules.verb:
                    hint="FULLSTOP at incorrect locations.Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)    
                 #---------------------------type10comma.py----------------------------------------------------------------
                for j in c:
                    if j == "Rs":
                        phrase="".join(b)
                        oned=re.findall("\d+",phrase)
                        if len(oned)!=0:
                       
                            if b[i-1]=="Rs" and b[i+1]==oned[0]:
                                hint="Correct Answer:You should use a fullstop after keyword {Rs]"
                                correctlst.append(hint)
                           
                                
                            if (b[i-3]==oned[0]  or b[i-1]==oned[1]) and c[i]=="." and c[i+1]==" ":
                                hint="Correct Answer:Always end a sentence with fullstop"
                                correctlst.append(hint)
                try:            
                    if b[i-1]==str(str(parse(co, fuzzy=True).year)) and b[i-1]!=oned[1] and c[i]=="." and c[i+1]==" ":
                        hint="Correct Answer:Sentence should be ended with a FULLSTOP"
                        correctlst.append(hint)            
                    if b[i-1]==str(parse(co,fuzzy=True).day) and c[i]=="." and c[i+1]==" ":
                        hint="InCorrect Answer:FULLSTOP at incorrect locations.Click the appropriate sidepane and read the manuals"
                        mandlst.append(hint)       
                except:
                    pass
#--------------------------------------------------------<w> with comma-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==","):
                
                hint="COMMA not needed.Click the appropriate sidepane and read the manuals"
                hintlst.append(hint)
                
        
#--------------------------------------------------- --<w> with FULLSTOP-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]=="."):
                
                hint="FULLSTOP at incorrect locations.Click the appropriate sidepane and read the manuals"
                hintlst.append(hint)
       
#--------------------------------------------------------<w> with SEMICOLON-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
            if (b[i]=="<w>" and c[i]==";"):
                
                hint="SEMICOLON at incorrect locations.Click the appropriate sidepane and read the manuals"
                hintlst.append(hint)
        return(hintlst,mandlst,correctlst,mandatory)       

##p1=crules()
##hintlst,mandlst,correctlst,mandatory=p1.commathree()
####print("hintlst",hintlst)
####print("mandlst",mandlst)
####print("correctlst",correctlst)
##for i in hintlst:
##    print(i)
##for j in mandlst:
##    print(j)
##for k in correctlst:
##    print(k)
