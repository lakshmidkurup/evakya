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
    alpha=['T','C','S','I','B','M']
    for i in verb:
        verb1.append(i.capitalize())
    article=['a','an']
    det=['the']
    adj=['confident','adorable','generous','charming','clever','huge','red','small','heavy','beautiful','fantastic','mesmerising','well-defined','hot','cold','warm','strong-flavored','delicious','tasty','mind-blowing','spicy','excellent','lovely','thrilled','elated','difficult','intelligent','rapid-fire','open-ended','lovely','fascinating','short','precise','interesting','selective','magnificent','high-grade','exceptional','focused','ambitious','demanding','competetive','exciting','brilliant','amazing','three-room','luxurious','spacious','own','modern','adorable','favorite','new','worthy','valuable','expensive','precious','limpy','twisted','sprained','fractured','considerate','attractive','amusing','jovial']
    onoun=['box','book','cage','scenary','house','building','tea','water','coffee','biriyani','pulav','kichdi','novel','story','match','race','ankle','leg','first-prize','second-prize','job','position','keys','books','poem','story','furniture','vegetables','fruits','bicycles','bicycle','house','organisation','school','college','flat','question']
    prep=['in','for','with','from','on']
    title=['Dr','Prof','Mr','Mrs','Sr','Bro','Major','Capt','Miss']
    beforetitle=['Late']
    vbz=['is','has','was']
    hverb=["could","will","would","might","can"]
    hintlst=[]
    correctlst=[]
    mandlst=[]
    pronoun=['his','her','he','she','it']
    pronoun1=[]
    for i in pronoun:
        pronoun1.append(i.capitalize())
    cnoun=["man","gentleman","orator","woman","lady"]
    conj=['and','but']
    conjadv=['However','Morever']
    neg=["not"]
    cordconj=['and','but']
    adverb=['slowly']
    madverb=['extremely']
    intro_words=['Although','Because','While']
    regex= "\d{4}"        #----------------------number---------------------------------------
    weekdays =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    #year=['2009','2020','2021']
    yearregex="[1-3][0-9]{3}"
    flatno=['Y/2/122','C-403','299/15','No:88','1304','2345']
    wing=['B-Wing']
    landmark=['Opp. Presidential Complex','Next to Mutta Chambers','Near Payal Cinema Complex']
    societyname=['Sarayu Society','Sarayu Co. Housing Society Ltd.']
    road=['Satghara Road','Vallabh Bagh Lane','Padmavati Vikar Mandal Road','2NS Main Road','Coronation Road','Dhakuria Station Road']
    street=['M.R.Campus','Srinivasa Nagar','Bargarpet','Dhakuria']
    location=['Badartala','Ghatkopar','Shahibaug','Kolathur','Kolar','Jadavpur']
    city=['Basirhat','Mumbai','Ahmedabad','Chennai','Bangalore','Kolkata','Gurgaon']
    state=['West Bengal','Haryana','Tamil Nadu','Karnataka','Maharashtra','Gujarat']
    onamelst=['Life', 'Style', 'International', 'Pvt', 'Ltd','BMC', 'Software']
    
    new_landmark=[]
    roadl=[]
    statel=[]
    societyl=[]
    for i in landmark:
        j=i.split(" ")
        for k in j:
            new_landmark.append(k)
        
    pincode=['700044','400077','380001','600099','560000','700031','400098','122001']
    for i in societyname:
        j=i.split(" ")
        for k in j:
            societyl.append(k)
    for i in road:
        j=i.split(" ")
        for k in j:
            roadl.append(k)
    for i in state:
        j=i.split(" ")
        for k in j: 
            statel.append(k)
        
    with open("D:\\evakya\\dataset\\tense.txt") as nd:
            for word in nd:                        
                dh=word.split(':')
                for i in verb:
                    if i==dh[1]:
                        presentverb=dh[0]
                        presentverb1=presentverb.capitalize()
    
   # def commaone(b,c,correct,category,level,username,userid,eid,submittedtext):
    def commaone(self):
        b=['John', '<w>', 'paid', '<w>', 'Rs', '<m>', '4', '<m>', '300', '<w>', 'for', '<w>', 'his', '<w>', 'adorable', '<w>', 'bicycle', '<m>']
        c=['John', ',', 'paid', '', 'Rs', ' ', '4', ' ', '300', ' ', 'for', ' ', 'his', ' ', 'adorable', ' ', 'bicycle',' ']
        
##        b=['Mr', '<m>', 'John', '<m>', 'a', '<w>', 'charming', '<w>', 'gentleman', '<m>', 'might', '<w>', 'open', '<w>', 'a', '<w>', 'small', '<w>', 'cage', '<m>', 'Morever', '<m>', 'he', '<w>', 'might', '<w>', 'lift', '<w>', 'it', '<m>']
##                                                                                                                                                                    
##        c=['Mr', '.', 'John', ' ', 'a', ';', 'charming', '', 'gentleman', ',', 'might', ' ', 'open', ' ', 'a', ' ', 'small', '<w>', 'cage', '.', 'Morever', ' ', 'he', ' ', 'might', ' ', 'lift', ' ', 'it', '.']

##        c=['Sr', ';', 'Mary', ' ', 'a', ' ', 'generous', ' ', 'lady', ';', 'could', ' ', 'open', ' ', 'a', ' ', 'huge', ' ', 'cage', ' ', 'and', ' ', 'a', ' ', 'red', ' ', 'box',' ']
##        b=['Sr', '<m>', 'Mary', '<m>' , 'a', '<w>', 'generous', '<w>', 'lady', '<m>', 'could', '<w>', 'open', '<w>', 'a', '<w>', 'huge', '<w>', 'cage', '<w>', 'and', '<w>', 'a', '<w>', 'red', '<w>', 'box','<m>']
##        c=['Major', '.', 'John', '.', 'a', ',', 'charming', ' ', 'gentleman', '.', 'could', ',', 'open', ' ', 'a', ' ', 'box', ';', 'a', ' ', 'book', ',', 'and', ' ', 'a', ' ', 'cage', '.']
##        b=['Major', '<m>', 'John', '<m>', 'a', '<w>', 'charming', '<w>', 'gentleman', '<m>', 'could', '<w>', 'open', '<w>', 'a', '<w>', 'box', '<m>', 'a', '<w>', 'book', '<w>', 'and', '<w>', 'a', '<w>', 'cage', '<m>']
        print(b)
        print(c)
        mandlst=[]
        correctlst=[]
        hintlst=[]
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
                    
                                    
                if (b[i-1] in crules.onoun) and (b[i+1] in crules.article):    
                    hint="Correct Answer:A comma should be used after an object noun, when you are trying to list 2 or more nouns."
                    correctlst.append(hint)
                    
                if (b[i-1]==number1) and (b[i+1]==None):    
                    hint="Correct Answer:A comma should be used after the first number, When a number is over 999."
                    correctlst.append(hint)
                    
                if b[i-1].isdigit() and b[i+1]==year:
                    hint="Correct Answer:A comma should be used after a date, when it is followed by a year."
                    correctlst.append(hint)
                    
                if b[i-1] in crules.months and b[i+1]==year and b[i+2]==None:
                    hint="Correct Answer:A comma should be used after a month, when it is followed by a date and no year is mentioned."
                    correctlst.append(hint)
                    
                if b[i-1] in crules.weekdays and b[i+1]==crules.months :
                    hint="Correct Answer:A comma should be used after a weekday, when it is followed by a month and date."
                    correctlst.append(hint)
                    
                if b[i-1] in crules.flatno and b[i+1] in crules.wing :
                    hint="Correct Answer:A comma should be used to seperate two entities-flatno and wing."
                    correctlst.append(hint)
                if b[i-1] in crules.wing and b[i+1] in crules.societyname :
                    hint="Correct Answer:A comma should be used to seperate two entities-wing and societyname."
                    correctlst.append(hint)    
                if b[i-1] in crules.societyname and b[i+1] in crules.road :
                    hint="Correct Answer:A comma should be used to seperate two entities-societyname and road."
                    correctlst.append(hint)
                if b[i-1] in crules.road and b[i+1] in crules.street :
                    hint="Correct Answer:A comma should be used to seperate two entities-road and street."
                    correctlst.append(hint)
                if b[i-1] in crules.street and b[i+1] in crules.location :
                    hint="Correct Answer:A comma should be used to seperate two entities-street and location."
                    correctlst.append(hint)
                if b[i-1] in crules.new_landmark and b[i+1] in crules.city :
                    hint="Correct Answer:A comma should be used to seperate two entities-landmark and city."
                    correctlst.append(hint)    
                if b[i-1] in crules.location and b[i+1] in crules.city :
                    hint="Correct Answer:A comma should be used to seperate two entities-street and location."
                    correctlst.append(hint)
                if b[i-1] in crules.city and b[i+1] in crules.state :
                    hint="Correct Answer:A comma should be used to seperate two entities-street and location."
                    correctlst.append(hint)
                if b[i-1] in crules.state and b[i+1] in crules.pincode :
                    hint="Correct Answer:A comma should be used to seperate two entities-state and pincode."
                    correctlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.pronoun :
                    hint="Correct Answer:A comma should be used to seperate two clauses"
                    correctlst.append(hint) 
         
    #---------------------------------------------------<m> with Fullstop---------------------------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
               
                    
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="InCorrect Answer:Inappropriate use of fullstop.Read the manuals."
                    mandlst.append(hint)
                    
                if (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="InCorrect Answer:Inappropriate use of fullstop.Read the manuals."
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="IInCorrect Answer:Inappropriate use of fullstop.Read the manuals."
                    mandlst.append(hint)
                if c[-1]==" ":
                    hint="Correct Answer:Always end a sentence with FUllSTOP."
                    mandlst.append(hint)
                    
                                           
                if b[i-1] in crules.title and b[i+1] in crules.snoun:
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always put a period/fullstop after a title"
                
                    correctlst.append(hint)
                
                  
                
                   
##                if b[i-1] =="Rs" and b[i+1]==number:
##                    
##                    hint="Correct Answer.Fullstop at appropriate place.Always put a FULLSTOP after the keyword Rs"
##                
##                    correctlst.append(hint) 
##                if b[i-1] =="Rs" and b[i+1]==number1:
##                    hint="Correct Answer.Fullstop at appropriate place.Always put a FULLSTOP after the keyword Rs"
##                    correctlst.append(hint) 

##                if b[i-1]==number or b[i-1]==number1 and b[i+1]==None:
##                    
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                
##                    correctlst.append(hint)
                
##                if b[i-1]==str(year) and b[i+1]==None:
##                    
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                
##                    correctlst.append(hint)
##                if b[i-1].isdigit() and b[i+1]==None:
##                    
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                
##                    correctlst.append(hint)
##
##                if b[i-1] ==crules.onoun and b[i+1]==crules.pronoun.capitalize():
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                    correctlst.append(hint)
##                if b[i-1]==crules.title and b[i+1]== crules.title:
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                    correctlst.append(hint)
##                name=['Esmail Bagani']
##                
##                for i in name:
##                    name1=i.split(" ")
##                if b[i-1]==crules.title and b[i+1]== crules.name1[0]:
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                    correctlst.append(hint)
##                if b[i-1]==crules.title and b[i+1]== crules.name1[1]:
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                    correctlst.append(hint)
##                if b[i-1].isaplha() and b[i+1]==name1[0] or name1[1]:
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                    correctlst.append(hint)
##                if b[i-1]==crules.pincode and b[i+1]==None:
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                    correctlst.append(hint)
##                if b[i-1] in crules.onamelst and b[i+1]=="The":
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                    correctlst.append(hint)
##                if b[i-1]=="Pvt" and b[i+1]=="Ltd":
##                    hint="Correct Answer.Fullstop at appropriate place."
##                    correctlst.append(hint)
##                if b[i-1]=="Ltd":
##                    hint="Correct Answer.Fullstop at appropriate place.When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
##                    correctlst.append(hint)
##                    

 #--------------------------------------------------------<w> with comma-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==","):
                
                hint="COMMA not needed.Click the appropriate sidepane and read the manuals"
                hintlst.append(hint)
                
        
###--------------------------------------------------------<w> with FULLSTOP-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]=="."):
                
                hint="FULLSTOP at incorrect locations.Click the appropriate sidepane and read the manuals"
                hintlst.append(hint)
       
#--------------------------------------------------------<w> with SEMICOLON-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==";"):
                
                hint="Please add SEMOCOLON at appropriate locations.Click the appropriate sidepane and read the manuals"
                hintlst.append(hint)

         

        return(hintlst,mandlst,correctlst)


    def commatwo(self):
        mandlst=[]
        correctlst=[]
        hintlst=[]
        #print("commarules",b,c,correct,level,username,userid,eid,submittedtext)
        b=['Mary', '<w>', 'stays', '<w>', 'in', '<w>', 'a', '<w>', 'house', '<m>', 'Her', '<w>', 'address', '<w>', 'is', '<w>', 'C/O', '<w>', 'Late', '<m>', 'Mr', '<m>', 'Esmail', '<w>', 'Bagani', '<m>', 'Y/2/122', '<m>', 'B-Wing', '<m>', 'Sarayu', '<w>', 'Society', '<m>', 'Satghara', '<w>', 'Road', '<m>', 'Badartala', '<m>', 'Kolkata', '<m>', 'Bengal', '<m>', '700044', '<m>']
        c=['Mary', ' ', 'stays', ' ', 'in', ' ', 'a', ' ', 'house', ',', 'Her', ' ', 'address', ' ', 'is', ' ', 'C/O', ' ', 'Late', ' ', 'Mr', ' ', 'Esmail', ' ', 'Bagani', ' ', 'Y/2/122', ' ', 'B-Wing', ' ', 'Sarayu', ' ', 'Society', ' ', 'Satghara', ' ', 'Road', ' ', 'Badartala', ' ', 'Kolkata', ' ', 'Bengal', ' ', '700044', '.']
        
##        b=['Mary', '<w>', 'was', '<w>', 'born', '<w>', 'on', '<w>', 'Tuesday', '<m>', 'February', '<w>', '17', '<m>', '2009', '<m>']
##        c=['Mary',' ', 'was',' ', 'born', ';', 'on', ' ', 'Tuesday', ',', 'February', ' ', '17', ' ', '2009', '.']
        
##        b=['James', '<w>', 'won', '<w>', 'a', '<w>', 'race', '<w>', 'on', '<w>', 'February', '<w>', '17', '<m>', '2009', '<m>']
##        c=['James', ' ', 'won', ',', 'a', ';', 'race', ' ', 'on', ',', 'February', ' ', '17', ',', '2009', ',']
##        b=['John', '<w>', 'paid', '<w>', 'Rs', '<m>', '4', '<m>', '300', '<w>', 'for', '<w>', 'his', '<w>', 'adorable', '<w>', 'bicycle', '<m>']
##        c=['John', '.', 'paid', ';', 'Rs', ',', '4', ',', '300', ',', 'for', ' ', 'his', ' ', 'adorable', ' ', 'bicycle','.']
##        b=['Mr', '<m>', 'John', '<m>', 'a', '<w>', 'charming', '<w>', 'gentleman', '<m>', 'might', '<w>', 'open', '<w>', 'a', '<w>', 'small', '<w>', 'cage', '<m>', 'Morever', '<m>', 'he', '<w>', 'might', '<w>', 'lift', '<w>', 'it', '<m>']
##                                                                                                                                                                    
##        c=['Mr', '', 'John', ' ', 'a', ',', 'charming', '', 'gentleman', ',', 'might', ' ', 'open', ',', 'a', ',', 'small', '<w>', 'cage', ',', 'Morever', ',', 'he', ' ', 'might', ',', 'lift', ' ', 'it', '.']

##        c=['Sr', ';', 'Mary', ' ', 'a', ' ', 'generous', ' ', 'lady', ';', 'could', ' ', 'open', ' ', 'a', ' ', 'huge', ' ', 'cage', ' ', 'and', ' ', 'a', ' ', 'red', ' ', 'box',' ']
##        b=['Sr', '<m>', 'Mary', '<m>' , 'a', '<w>', 'generous', '<w>', 'lady', '<m>', 'could', '<w>', 'open', '<w>', 'a', '<w>', 'huge', '<w>', 'cage', '<w>', 'and', '<w>', 'a', '<w>', 'red', '<w>', 'box','<m>']

##        c=['Major', '.', 'John', '.', 'a', ',', 'charming', ' ', 'gentleman', '.', 'could', ',', 'open', ' ', 'a', ' ', 'box', ';', 'a', ' ', 'book', ',', 'and', ' ', 'a', ' ', 'cage', '.']
##        b=['Major', '<m>', 'John', '<m>', 'a', '<w>', 'charming', '<w>', 'gentleman', '<m>', 'could', '<w>', 'open', '<w>', 'a', '<w>', 'box', '<m>', 'a', '<w>', 'book', '<w>', 'and', '<w>', 'a', '<w>', 'cage', '<m>']
        print(b)
        print(c)
        co="".join(c)
##        year=str(str(parse(co, fuzzy=True).year))
##        day=parse(co,fuzzy=True).day
##        year=str(year)
##        day=str(day)
     
    #---------------------------------------------------<m> with semicolon-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==";"):
                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
                    hint="InCorrect Answer:Never end a Abbreviation with a semicolon"
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="InCorrect Answer:A semicolon cannot be used to seperate an adjective phrase from the verbphrase"
                    mandlst.append(hint)
                if (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="InCorrect Answer:A semicolon should not be used when a relative clause follows the main subject."
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="InCorrect Answer:A semicolon should not be used when a relative clause follows the main subject."
                    mandlst.append(hint)
                if (b[i-1] in crules.onoun) and (b[i+1] in crules.article):    
                    hint="InCorrect Answer:A semicolon should not be used after an object noun, when you are trying to list 2 or more nouns."
                    mandlst.append(hint)
                
                if c[-1]==";":
                    hint="Incorrect answer:never end a sentence with a semicolon"
                    mandlst.append(hint)
                
    #---------------------------------------------------type10comma.py----------------------------------------------------------------
                if b[i-1] =="Rs" and b[i+1].isdigit():
                    hint="InCorrect Answer:No semicolon needed after the keyword {Rs]"
                    mandlst.append(hint)     
                phrase="".join(b)
                oned=re.findall("\d+",phrase)
                #print("oned",oned[0],oned[1])
                if b[i-1]==oned[0] and b[i+1]==oned[1]:
                    hint="Incorrect Answer:HINT:Should you use semicolon,when you write an amount in figures?"
                    mandlst.append(hint)
                    
                if b[i-1].isdigit() and c[-1]==" ":
                    hint="InCorrect Answer:Never END a sentence with a semicolon"
                    mandlst.append(hint)  
                     #-----------type11date.py----------------------------------------------------------------
                for i in c:
                    if c in crules.months:
                        if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                            hint="InCorrect Answer:Is there a need of semicolon after a date, when it is followed by a year."
                            mandlst.append(hint)
                        if b[i-1]==str(str(parse(co, fuzzy=True).year)) and c[-1]==";":
                            hint="Incorrect Ans:Can a sentence end with semicolon?"
                            mandlst.append(hint)
                        if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                            hint="InCorrect Answer:A comma should be used after a month, when it is followed by just a date(no year mentioned)."
                            mandlst.append(hint)
                        if b[i-1]==str(parse(co,fuzzy=True).day) and c[-1]==";":
                            hint="InCorrect Answer:Sentence should be ended with a FULLSTOP"
                            mandlst.append(hint)    
                              
                        if b[i-1] in crules.weekdays and b[i+1] in crules.months :
                            hint="InCorrect Answer:A comma should be used after a weekday, when it is followed by a month and date."
                            mandlst.append(hint)    
                        if b[i-3]==str(parse(co,fuzzy=True).day) and b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                            hint="InCorrect Answer:Put a comma just after the month,if the date format is date-month-year"
                            mandlst.append(hint)      
    #---------------------------------------------------<m> with Comma-------------------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):

                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
                    hint="Correct Answer:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                    correctlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="Correct Answer:A comma can be used to seperate an adjective phrase from the verbphrase"
                    correctlst.append(hint)
                if (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="Correct Answer:A comma should be used a relative clause follows the main subject."
                    correctlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="Correct Answer:A comma should be used a relative clause follows the main subject."
                    correctlst.append(hint)
                if (b[i-1] in crules.onoun) and (b[i+1] in crules.article):    
                    hint="Correct Answer:A comma should be used after an object noun, when you are trying to list 2 or more nouns."
                    correctlst.append(hint)
                                  
               
      #-----------type11date.py----------------------------------------------------------------    
                for i in c:
                    if c in crules.months:
                        if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                            hint="Correct Answer:A comma should be used after a date, when it is followed by a year."
                            correctlst.append(hint)
                        if b[i-1]==str(str(parse(co, fuzzy=True).year)) and c[-1]==",":
                            hint="InCorrect Answer:Sentence should be ended with a FULLSTOP"
                            mandlst.append(hint)
                        if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                            hint="Correct Answer:A comma should be used after a month, when it is followed by just a date(no year mentioned)."
                            correctlst.append(hint)
                        if b[i-1]==str(parse(co,fuzzy=True).day) and c[-1]==",":
                            hint="InCorrect Answer:Sentence should be ended with a FULLSTOP"
                            mandlst.append(hint)    
                        if b[i-3]==str(parse(co,fuzzy=True).day) and b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                            hint="Correct Answer:Put a comma just after the month,if the date format is date-month-year"
                            correctlst.append(hint) 
                             
                        if b[i-1] in crules.weekdays and b[i+1] in crules.months :
                            hint="Correct Answer:A comma should be used after a weekday, when it is followed by a month and date."
                            correctlst.append(hint) 
                        if b[i-1] in crules.flatno and b[i+1] in crules.wing :
                            hint="Correct Answer:A comma should be used to seperate two entities-flatno and wing."
                            correctlst.append(hint)
                        if b[i-1] in crules.wing and b[i+1] in crules.societyname :
                            hint="Correct Answer:A comma should be used to seperate two entities-wing and societyname."
                            correctlst.append(hint)    
                        if b[i-1] in crules.societyname and b[i+1] in crules.road :
                            hint="Correct Answer:A comma should be used to seperate two entities-societyname and road."
                            correctlst.append(hint)
                        if b[i-1] in crules.road and b[i+1] in crules.street :
                            hint="Correct Answer:A comma should be used to seperate two entities-road and street."
                            correctlst.append(hint)
                        if b[i-1] in crules.street and b[i+1] in crules.location :
                            hint="Correct Answer:A comma should be used to seperate two entities-street and location."
                            correctlst.append(hint)
                        if b[i-1] in crules.new_landmark and b[i+1] in crules.city :
                            hint="Correct Answer:A comma should be used to seperate two entities-landmark and city."
                            correctlst.append(hint)    
                        if b[i-1] in crules.location and b[i+1] in crules.city :
                            hint="Correct Answer:A comma should be used to seperate two entities-street and location."
                            correctlst.append(hint)
                        if b[i-1] in crules.city and b[i+1] in crules.state :
                            hint="Correct Answer:A comma should be used to seperate two entities-street and location."
                            correctlst.append(hint)
                        if b[i-1] in crules.state and b[i+1] in crules.pincode :
                            hint="Correct Answer:A comma should be used to seperate two entities-state and pincode."
                            correctlst.append(hint)
                        if b[i-1] in crules.onoun and b[i+1] in crules.pronoun :
                            hint="Correct Answer:A comma should be used to seperate two clauses"
                            correctlst.append(hint)     
              #---------------------------type10comma.py----------------------------------------------------------------
                for j in c:
                    if j == "Rs":
                        phrase="".join(b)
                        oned=re.findall("\d+",phrase)
                        fd=str(oned[0])
                        sd=str(oned[1])
                        rw="Rs"
                        #print("oned",oned[0],oned[1])
                        if b[i-1] =="Rs" and b[i+1] ==oned[0]:
                            hint="InCorrect Answer:You should not use a semicolon after keyword {Rs]"
                            mandlst.append(hint)
                        if b[i-3]=="Rs" and b[i-1]==oned[0] and b[i+1]==oned[1]:
                            hint="correct Answer:Comma used to seperate amount above 999"
                            correctlst.append(hint)
                            
                        if b[i-3]=="Rs" and (b[i-1]==oned[1]  or b[i-1]==oned[0]) and c[-1]==",":
                            hint="InCorrect Answer:Never END a sentence with a comma"
                            mandlst.append(hint) 
    
    #---------------------------------------------------<m> with Fullstop--------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                
               #---------------------------type10comma.py----------------------------------------------------------------
                if b[i-1] =="Rs" and b[i+1].isdigit():
                    hint="Correct Answer:Put a FULLSTOP after the keyword {Rs]"
                    correctlst.append(hint)     
                phrase="".join(b)
                oned=re.findall("\d+",phrase)
                #print("oned",oned[0],oned[1])
                if b[i-1]==oned[0] and b[i+1]==oned[1]:
                    hint="Incorrect Answer:HINT:Can you use a fullstop to mention an amount in figures?"
                    mandlst.append(hint)
                    
                if b[i-1].isdigit() and c[-1]==" ":
                    hint="Correct Answer:END a sentence with a FULLSTOP"
                    correct.append(hint) 
                    
                if (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="InCorrect Answer:Never use fullstop in between a sentence,No need of a period between the noun and the article."
                    mandlst.append(hint)
                onounlst=list(set(crules.onoun) & set(b))
                if len(onounlst) > 2:
                    if (b[i-1] in crules.onoun and (b[i+1] in crules.article)):
                
                        hint="Correct Answer:A comma should be used after an object noun, when you are trying to list 2 or more nouns."
                        correctlst.append(hint) 
                   
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="InCorrect Answer:Never use fullstop in between a sentence,No need of a period between thecommon noun and the helping verb."
                    mandlst.append(hint)
                    
                if b[i-1] in crules.title and b[i+1] in crules.snoun:
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always put a period/fullstop after a title"
                
                    correctlst.append(hint)
                    
                if (b[i-1] in crules.onoun) and c[-1]==".":
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                
                    correctlst.append(hint)
              
#----------=---------------------------------------type11date.py----------------------------------------------------------------
                for i in c:
                    if c in crules.months:
                    
                        if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                            hint="InCorrect Answer:can you use a FULLSTOP after a date, when it is followed by a year."
                            mandlst.append(hint)
                        
                        if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                            hint="InCorrect Answer:A comma should be used after a month, when it is followed by just a date(no year mentioned)."
                            mandlst.append(hint)
                        if b[i-1]==str(parse(co,fuzzy=True).day) and c[-1]==".":
                            hint="Correct Answer:Sentence should be ended with a FULLSTOP"
                            correctlst.append(hint)    
                       
                        if b[i-1]==str(str(parse(co, fuzzy=True).year)) and c[-1]==".":
                            hint="Correct Answer:Sentence should be ended with a FULLSTOP"
                            correctlst.append(hint)        
                        if b[i-1] in crules.weekdays and b[i+1] in crules.months :
                            hint="InCorrect Answer:A comma should be used after a weekday, when it is followed by a month and date."
                            mandlst.append(hint)
                        if b[i-3]==str(parse(co,fuzzy=True).day) and b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                            hint="InCorrect Answer:Put a comma just after the month,if the date format is date-month-year"
                            mandlst.append(hint)     
##                if b[i-1] =="Rs" and b[i+1]==number:
##                    
##                    hint="Correct Answer.Fullstop at appropriate place.Always put a FULLSTOP after the keyword Rs"
##                
##                    correctlst.append(hint) 
##                if b[i-1] =="Rs" and b[i+1]==number1:
##                    hint="Correct Answer.Fullstop at appropriate place.Always put a FULLSTOP after the keyword Rs"
##                    correctlst.append(hint) 

##                if b[i-1]==number or b[i-1]==number1 and b[i+1]==None:
##                    
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                
##                    correctlst.append(hint)
##                if b[i-1]==number or b[i-1]==number1 and b[i+1]==None:
##                    
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                
##                    correctlst.append(hint)
##                if b[i-1]==year and b[i+1]==None:
##                    
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                
##                    correctlst.append(hint)
##                if b[i-1].isdigit() and b[i+1]==None:
##                    
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                
##                    correctlst.append(hint)
##
##                if b[i-1] ==crules.onoun and b[i+1]==crules.pronoun.capitalize():
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                    correctlst.append(hint)
##                if b[i-1]==crules.title and b[i+1]== crules.title:
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                    correctlst.append(hint)
##                name=['Esmail Bagani']
##                
##                for i in name:
##                    name1=i.split(" ")
##                if b[i-1]==crules.title and b[i+1]== crules.name1[0]:
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                    correctlst.append(hint)
##                if b[i-1]==crules.title and b[i+1]== crules.name1[1]:
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                    correctlst.append(hint)
##                if b[i-1].isaplha() and b[i+1]==name1[0] or name1[1]:
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                    correctlst.append(hint)
##                if b[i-1]==crules.pincode and b[i+1]==None:
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                    correctlst.append(hint)
##                if b[i-1] in crules.onamelst and b[i+1]=="The":
##                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
##                    correctlst.append(hint)
##                if b[i-1]=="Pvt" and b[i+1]=="Ltd":
##                    hint="Correct Answer.Fullstop at appropriate place."
##                    correctlst.append(hint)
##                if b[i-1]=="Ltd":
##                    hint="Correct Answer.Fullstop at appropriate place.When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
##                    correctlst.append(hint)
##               
##       

   
 #--------------------------------------------------------<w> with comma-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==","):
                #--------------type6.py------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
                  hint="Read The manual again, HINT:No need to add a comma in between a noun/adjective phrase"
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
                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
                  hint="Read The manual again, HINT:No need to add a comma after a verb, when it is followed by a neuter pronoun(e.g. it)"
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
                #-----------------------------type4.py--------------------------------------------
                if b[i-1] in crules.hverb and b[i+1] in crules.verb:
                    hint="Read The manual again, HINT:No need to put a comma in between a verbphrase..."
                    hintlst.append(hint)
                if b[i-1] in crules.cnoun and b[i+1] in crules.hverb:
                    hint="Read The manual again, HINT:No need to put a comma after a common noun especially when there is no enumeration..."
                    hintlst.append(hint)        
                if b[i-1] in crules.article and b[i+1] in crules.onoun:
                    hint="Read The manual again, HINT:No need to put a comma between a article and a noun.Here article is used to modify the noun."
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
                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
                    hint="Read The manual again, HINT:No need to put a comma within a nounphrase, preferably after an adjective"
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1]=="Rs":
                    hint="Read The manual again, HINT:No need to put a comma after a verb like paid especially when an amount is specified afterwards"
                    hintlst.append(hint)    
                
                phrase="".join(b)
                oned=re.findall("\d+",phrase)
                #print("oned",oned[0],oned[1])
               
                if b[i-1]==oned[1] and b[i+1]==crules.prep:
                    hint="Incorrect Answer, HINT: No need of a comma after a number"
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
                for i in c:
                    if c in crules.months:
            
                        if b[i-1] in crules.prep and b[i+1] in crules.months:
                            hint="Read the manual again, HINT:No need of a comma after a preposition when it is followed by a month"
                            hintlst.append(hint)
                           
                        if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                            hint="Read the manual again, HINT:No need of a comma in the format - month followed by a date"
                            hintlst.append(hint)
                        if b[i-1]  in crules.snoun and b[i+1] in crules.vbz:
                            hint="Read the manual again, HINT:No need of a comma after a noun when it is followed by a ['is','was']"
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
                        phrase="".join(b)
        ##                oned=re.findall("\d+",phrase)
                        
                                   
                        if b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                            hint="Read the manual again, HINT:No need of a comma after a month when it is followed by a year if the date format is [15 March 2003]" 
                            hintlst.append(hint)
                
##                if b[i-1] ==number1 and b[i+1] in crules.prep:
##                    hint="Read the manual again, HINT:No need of a comma after an amount when it is followed by a preposition"
##                if b[i-1] ==number and b[i+1] in crules.prep:
##                    hint="Read the manual again, HINT:No need of a comma after an amount when it is followed by a preposition"    
##                              
##                if b[i-1] in crules.onoun and b[i+1] in crules.prep:
##                    hint="Read the manual again, HINT:No need of a comma after an object noun when it is followed by a preposition"
##                if b[i-1] in crules.onoun and b[i+1] in crules.prep:
##                    hint="Read the manual again, HINT:No need of a comma after an object noun when it is followed by a preposition"
##                if b[i-1] in crules.prep and b[i+1] in crules.pronoun:
##                    hint="Read the manual again, HINT:No need of a comma after a preposition when it is followed by a pronoun"

                    

           #-----------------------------type12.py---------------------------------------------------------------------------------------------------------------------
##                if b[i-1] in crules.snoun and b[i+1] in crules.verb1:
##                    hint="Read the manual again, HINT:No need of a comma between a noun and a verb"
##                if b[i-1] in crules.verb1 and b[i+1] in crules.prep:
##                    hint="Read the manual again, HINT:No need of a comma between a verb and a prep"
##                if b[i-1] in crules.prep and b[i+1] in crules.article:
##                    hint="Read the manual again, HINT:No need of a comma between a prep and an article"
##                if b[i-1] in crules.article and b[i+1] in crules.onoun:
##                    hint="Read the manual again, HINT:No need of a comma between an article and a noun"               
##                    
##                if b[i-1] in crules.pronoun1 and b[i+1]=="address":
##                    hint="Read the manual again, HINT:No need of a comma between a noun and the word 'address'"
##                if b[i-1] =="address" and b[i+1] in crules.vbz:
##                    hint="Read the manual again, HINT:No need of a comma between the word 'address' and [is/was]"         
##                if b[i-1] in crules.vbz and b[i+1]=="C/O":
##                    hint="Read the manual again, HINT:No need of a comma after [is/was]"
##                if b[i-1]=="C/O" and b[i+1] in crules.title:
##                    hint="Read the manual again, HINT:No need of a comma addresstag [C/O,S/O]"
##
##                name=['Esmail Bagani']
##                
##                for i in name:
##                    name1=i.split(" ")
##                  
##                if b[i-1]==name1[0] and b[i+1]==name1[1]:
##                    hint="Read the manual again, HINT:Don't split the name with a comma"
##                if b[i-1]==name1[1] and b[i+1]==name1[0]:
##                    hint="Read the manual again, HINT:Don't split the name with a comma"
##                    
##                if b[i-1] in crules.societyl and b[i+1] in crules.societyl:
##                    hint="Read the manual again, HINT:Don't split the society name with a comma"
##                if b[i-1] in crules.roadl and b[i+1] in crules.roadl:
##                    hint="Read the manual again, HINT:Don't split the road name with a comma"
##                if b[i-1] in crules.statel and b[i+1] in crules.statel:
##                    hint="Read the manual again, HINT:Don't split the state name with a comma"
##                
#-----------------------------type12stay.py-----------------------------------
##                if b[i-1] in crules.verb1 and b[i+1] in crules.article:
##                    hint="Read the manual again, HINT:No need of a comma between a verb and an article.."
##                if b[i-1] in crules.article and b[i+1]=="organisation"+".":
##                    hint="Read the manual again, HINT:No need of a comma between a aricle and a noun.."
##                
##                if b[i-1] =="The" and b[i+1]=="name":
##                    hint="Read the manual again, HINT:No need of a comma between a determiner and the keyword name .."
##                
##                if b[i-1] =="name" and b[i+1]=="of":
##                    hint="Read the manual again, HINT:No need of a comma between and keyword name and a preposition .."
##                if b[i-1] =="of" and b[i+1] in crules.det:
##                    hint="Read the manual again, HINT:No need of a comma between a preposition and a determiner"
##                if b[i-1] in det and b[i+1] in crules.onoun:
##                    hint="Read the manual again, HINT:No need of a comma between a determiner and the keyword name .."
##                if b[i-1] in crules.onoun and b[i+1] in crules.vbz:
##                    hint="Read the manual again, HINT:No need of a comma between a noun and [is/was] .."
##                if b[i-1] in crules.vbz and b[i+1] in crules.onamelst:
##                    hint="Read the manual again, HINT:No need of a comma between [is/was] and an object name like building name,name of a person etc. "
##                    hintlst.append(hint)
##                if b[i-1] in crules.onamelst and b[i+1] in crules.onamelst:
##                    hint="Read the manual again, HINT:There is no listing of items here, it has to be considered as a single entity..so please avoid comma here."
##                    hintlst.append(hint)
##                if b[i-1]=="The" and b[i+1]=="address":
##                    hint="Read the manual again, HINT:No need of a comma between a determiner and the a propernoun 'address'"
##                    hintlst.append(hint)
##                if b[i-1] =="address" and b[i+1] in crules.vbz:
##                    hint="Read the manual again, HINT:No need of a comma between the word 'address' and [is/was]"
##                    hintlst.append(hint)
##                if b[i-1] in crules.vbz and b[i+1] in crules.new_landmark:
##                    hint="Read the manual again, HINT:No need of a comma after [is/was]"
##                    hintlst.append(hint)
##                if b[i-1] in crules.new_landmark and b[i+1] in crules.new_landmark:
##                    hint="Read the manual again, HINT:There is no listing of items here, it has to be considered as a single entity..so please avoid comma here."
##                    hintlst.append(hint)
##                if b[i-1].isalpha() and b[i+1].isalpha():
##                    hint="Read the manual again, HINT:No need of a comma here as it is an abbreviation"
##                    hintlst.append(hint)
                
 #--------------------------------quotneg.py----------------------------------------------------------          
##                if b[i-1] in crules.verb and b[i+1] in crules.prep:
##                    hint="Read the manual again, HINT:No need of a comma between a verb and a preposition"
##                    hintlst.append(hint)
##                if b[i-1] in crules.prep and b[i+1] in crules.snoun:
##                    hint="Read the manual again, HINT:No need of a comma between a preposition and a noun"
##                    hintlst.append(hint)     
##                
###-----------------------------------type1.py----------------------------------------------------------
##                if b[i-1] in crules.cnoun and b[i+1] in crules.verb:
##                    hint="Read The manual again, HINT:No need to put a comma after a common noun especially when there is no enumeration..."
##                    hintlst.append(hint)
##                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
##                    hint="Read The manual again, HINT:No need to seperate a adjective phrase with a comma"
##                    hintlst.append(hint)
##                if b[i-1] in crules.onoun and b[i+1] in crules.madverb:
##                    hint="Read The manual again, HINT:Noun when followed by a modifying adverb,don't put a comma in between"
##                    hintlst.append(hint)
##                if b[i-1] in crules.madverb and b[i+1] in crules.adverb:
##                    hint="Read The manual again, HINT:Modifying adverb like extremely,very etc shoud not be seperated from main adverbs using a comma"
##                    hintlst.append(hint)
###--------------------------------compound.py----------------------------------------
##                if b[i-1] in crules.cordconj and b[i+1] in crules.verb:
##                    hint="Read The manual again, HINT:Avoid Comma after a Conjunction like [and] or [but]"
##                    hintlst.append(hint)
##                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
##                    hint="Read The manual again, HINT:No need to add a comma after a verb, when it is followed by a neuter pronoun(e.g. it)"
##                    hintlst.append(hint)
###--------------------------------inrocomma.py---------------------------------------------------------------------------------------------------------------
##                if b[i-1] in crules.intro-words and b[i+1] in crules.snoun:
##                    hint="Read The manual again, HINT:Avoid Comma after Introductory wirds like [while/Although] etc."
##                    hintlst.append(hint)
##                if b[i-1] in crules.snoun and b[i+1] in crules.vbz:
##                    hint="Read The manual again, HINT:No need to add a comma after a noun, when it is followed by [is/was]"
##                    hintlst.append(hint)
##                if b[i-1] in crules.vbz and b[i+1] in crules.verbing:
##                    hint="Read The manual again, HINT:No need to add a comma after [is/was], when it is followed by a verb"
##                    hintlst.append(hint)
##                if b[i-1] in crules.verbing and b[i+1] in crules.article:
##                    hint="Read The manual again, HINT:No need to add a comma after a verb ,in a verbphrase"
##                    hintlst.append(hint)
##                  
##                if b[i-1] in crules.pronoun and b[i+1] in crules.verb:
##                    hint="Read The manual again, HINT:No need to add a comma after a pronoun"
##                    
##                    hintlst.append(hint)
##               
                    
#--------------------------------------------------------<w> with FULLSTOP-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]=="."):
                
                   #-----------------------------type4.py--------------------------------------------
                if b[i-1] in crules.hverb and b[i+1] in crules.verb:
                    hint="Read The manual again, HINT:No need to put a FULLSTOP in between a verbphrase..."
                    hintlst.append(hint)
                if b[i-1] in crules.cnoun and b[i+1] in crules.hverb:
                    hint="Read The manual again, HINT:No need to put a FULLSTOP after a common noun especially when there is no enumeration..."
                    hintlst.append(hint)        
                if b[i-1] in crules.article and b[i+1] in crules.onoun:
                    hint="Read The manual again, HINT:No need to put a FULLSTOP between a article and a noun.Here article is used to modify the noun."
                    hintlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.cordconj:
                    hint="Read The manual again, HINT:No need to put a FULLSTOP before conjunctions like and,but etc."
                    hintlst.append(hint)
                if b[i-1] in crules.cordconj and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:No need to put a FULLSTOP after conjunctions like and,but etc."
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
                if b[i-1] in crules.verb and b[i+1]=="Rs":
                    hint="Incorrect Answer, HINT: No need of a FULLSTOP after a verb"
                    hintlst.append(hint)    
                     
                phrase="".join(b)
                oned=re.findall("\d+",phrase)
               
               
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
  
                    #-----------------type11date.py--------------------------------
                for i in c:
                    if c in crules.months:
                        if b[i-1] in crules.onoun and b[i+1] in crules.prep:
                            hint="Read the manual again, HINT:No need of a FULLSTOP after an object noun when it is followed by a preposition"
                            hintlst.append(hint) 
                       
                        if b[i-1] in crules.prep and b[i+1] in crules.months:
                            hint="Read the manual again, HINT:No need of a FULLSTOP after a preposition when it is followed by a month"
                            hintlst.append(hint) 
                        if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                            hint="Read the manual again, HINT:No need of a FULLSTOP after a month when it is followed by a date"
                            hintlst.append(hint) 
                        if b[i-1]  in crules.snoun and b[i+1] in crules.vbz:
                            hint="Read the manual again, HINT:No need of a FULLSTOP after a noun when it is followed by a ['is','was']"
                            hintlst.append(hint) 
                        if b[i-1] in crules.vbz and b[i+1] in crules.verb:
                            hint="Read the manual again, HINT:No need of a FULLSTOP after ['is','was'] when it is followed by a verb"
                            hintlst.append(hint) 
                        if b[i-1] in crules.verb and b[i+1] in crules.prep:
                            hint="Read the manual again, HINT:No need of a FULLSTOP after a verb when it is followed by a preposition"
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
                
                #--------------type6.py------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
                  hint="Read The manual again, HINT:No need to add a fullstop in between a noun/adjective phrase"
                  hintlst.append(hint)
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
              

#--------------------------------------------------------<w> with SEMICOLON-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==";"):
                  #-----------------------------type4.py--------------------------------------------
                if b[i-1] in crules.hverb and b[i+1] in crules.verb:
                    hint="Read The manual again, HINT:No need to put a SEMICOLON in between a verbphrase..."
                    hintlst.append(hint)
                if b[i-1] in crules.cnoun and b[i+1] in crules.hverb:
                    hint="Read The manual again, HINT:No need to put a SEMICOLON after a common noun especially when there is no enumeration..."
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
                #--------------type6.py------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
                  hint="Read The manual again, HINT:No need to add a SEMICOLON in between a noun/adjective phrase"
                  hintlst.append(hint)
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
                  hint="Read The manual again, HINT:No need to add a SEMICOLON after a verb, when it is followed by a neuter pronoun(e.g. it)"
                  hintlst.append(hint)



                    #-----------------type11date.py--------------------------------
                for i in c:
                    if c in crules.months:
                        if b[i-1] in crules.onoun and b[i+1] in crules.prep:
                            hint="Read the manual again, HINT:No need of a SEMICOLON after an object noun when it is followed by a preposition"
                            hintlst.append(hint) 
                        
                        if b[i-1] in crules.prep and b[i+1] in crules.months:
                            hint="Read the manual again, HINT:No need of a SEMICOLON after a preposition when it is followed by a month"
                            hintlst.append(hint) 
                        if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                            hint="Read the manual again, HINT:No need of a SEMICOLON after a month when it is followed by a date"
                            hintlst.append(hint) 
                        if b[i-1]  in crules.snoun and b[i+1] in crules.vbz:
                            hint="Read the manual again, HINT:No need of a SEMICOLON after a noun when it is followed by a ['is','was']"
                            hintlst.append(hint) 
                        if b[i-1] in crules.vbz and b[i+1] in crules.verb:
                            hint="Read the manual again, HINT:No need of a SEMICOLON after ['is','was'] when it is followed by a verb"
                            hintlst.append(hint) 
                        if b[i-1] in crules.verb and b[i+1] in crules.prep:
                            hint="Read the manual again, HINT:No need of a SEMICOLON after a verb when it is followed by a preposition"
                            hintlst.append(hint) 
                        if b[i-1] in crules.prep and b[i+1] in crules.weekdays:
                            hint="Read the manual again, HINT:No need of a SEMICOLON after a prep when it is followed by a weekday"
                            hintlst.append(hint) 
                        if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1] in crules.months and b[i+2]==str(str(parse(co, fuzzy=True).year)):
                            hint="Read the manual again, HINT:No need of a SEMICOLON after a date when it is followed by a month and a year if the date format is [15 March 2003]"
                            hintlst.append(hint) 
                        if b[i-1] in crules.months and b[i+1]==year and b[i+2]==None:
                            hint="Read the manual again, HINT:No need of a SEMICOLON after a month when it is followed by a year if the date format is [15 March 2003]"
                            hintlst.append(hint)  
#---------------------------------------------------------<m> with no punctuation----------------------------------------------------------------------------------
        for i in range(0,len(b)):            
            if (b[i]=="<m>" and c[i]==" "):
                       #-----------------------------type12.py---------------------------------------------------------------------------------------------------------------------
##                for j in c:
##                    if j=="address":
##                        if b[i-1] in crules.snoun and b[i+1] in crules.verb1:
##                             hint="Correct Answer, HINT:No need of a comma between a noun and a verb"
##                             correctlst.append(hint)
##                        if b[i-1] in crules.verb1 and b[i+1] in crules.prep:
##                             hint="Correct Answer, HINT:No need of a comma between a verb and a prep"
##                             correctlst.append(hint)
##                        if b[i-1] in crules.prep and b[i+1] in crules.article:
##                             hint="Correct Answer, HINT:No need of a comma between a prep and an article"
##                             correctlst.append(hint)
##                        if b[i-1] in crules.article and b[i+1] in crules.onoun:
##                            hint="Correct Answer, HINT:No need of a comma between an article and a noun"               
##                            correctlst.append(hint)
##                        if b[i-1] in crules.pronoun1 and b[i+1]=="address":
##                             hint="Correct Answer, HINT:No need of a comma between a noun and the word 'address'"
##                             correctlst.append(hint)
##                        if b[i-1] =="address" and b[i+1] in crules.vbz:
##                             hint="Correct Answer, HINT:No need of a comma between the word 'address' and [is/was]"
##                             correctlst.append(hint)
##                        if b[i-1] in crules.vbz and b[i+1]=="C/O":
##                             hint="Correct Answer, HINT:No need of a comma after [is/was]"
##                             correctlst.append(hint)
##                        if b[i-1]=="C/O" and b[i+1] in crules.title:
##                             hint="Correct Answer, HINT:No need of a comma addresstag [C/O,S/O]"
##                             correctlst.append(hint)
##
##                        name=['Esmail Bagani']
##                        
##                        for i in name:
##                            name1=i.split(" ")
##                            print(name1)
##                        
##                        if b[i-1]==str(name1[0]) and b[i+1]==str(name1[1]):
##                             hint="Correct Answer, HINT:Don't split the name with any punctuaion"
##                             correctlst.append(hint)
##                        if b[i-1]==name1[1] and b[i+1]==name1[0]:
##                             hint="Correct Answer, HINT:Don't split the name with any punctuaion"
##                             correctlst.append(hint)
##                        if b[i-1] in crules.societyl and b[i+1] in crules.societyl:
##                             hint="Correct Answer,HINT:Don't split the society name with any punctuaion"
##                             correctlst.append(hint)
##                        if b[i-1] in crules.roadl and b[i+1] in crules.roadl:
##                             hint="Correct Answer,HINT:Don't split the road name with any punctuaion"
##                             correctlst.append(hint)
##                        if b[i-1] in crules.statel and b[i+1] in crules.statel:
##                             hint="Correct Answer,HINT:Don't split the state name with any punctuaion"
##                             correctlst.append(hint)
                        
                #---------------------------------------------type11date.py----------------------------------------------------------------    
                
                for i in c:
                    if c in crules.months:
                        if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                            hint="Incorrect Answer:A comma should be used after a date, when it is followed by a year."
                            mandlst.append(hint)
                        if b[i-1]==str(str(parse(co, fuzzy=True).year)) and c[-1]==" ":
                            hint="Incorrect Answer:Sentence should be ended with a FULLSTOP"
                            mandlst.append(hint)
                        if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                            hint="Incorrect Answer:A comma should be used after a month, when it is followed by just a date(no year mentioned)."
                            mandlst.append(hint)
                        if b[i-1]==str(parse(co,fuzzy=True).day) and c[-1]==" ":
                            hint="Incorrect Answer:Sentence should be ended with a FULLSTOP"
                            mandlst.append(hint)    
                        
                        if b[i-3]==str(parse(co,fuzzy=True).day) and b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                            hint="Correct Answer:Put a comma just after the month,if the date format is date-month-year"
                            correctlst.append(hint)    
                            
                        if b[i-1] in crules.weekdays and b[i+1]==crules.months :
                            hint="Incorrect Answer:A comma should be used after a weekday, when it is followed by a month and date."
                            mandlst.append(hint)
                
                   #----------------------------type6.py-----------------------------------------------------------------------------------
                for j in c:
                    if j in crules.conjadv:
                        if b[i-1] in crules.conjadv and b[i+1] in crules.pronoun:
                            
                            hint="Read The manual again, HINT:A comma is used to seperate a conjunctive adverb."
                        
                            mandlst.append(hint) 
                            
                       
                        if b[i-1] in crules.onoun and b[i+1] in crules.conjadv:
                            
                            hint="InCorrect Answer.A FULLSTOP is used to seperate two complete sentences."
                        
                            mandlst.append(hint)    
                #-----------------------------------------------------------------------------------------------------------------------------------
       
##                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
##                    hint="Read The manual again, HINT:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
##                    hintlst.append(hint)
##                if (b[i-1] =="Mr") and (b[i+1]=="Esmail"):    
##                    hint="Read The manual again, HINT:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
##                    hintlst.append(hint)            
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="Read The manual again, HINT:A comma can be used to seperate an adjective phrase from the verbphrase"
                    hintlst.append(hint)
                if (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="Read The manual again, HINT:comma should be used when a relative clause follows the main subject."
                    hintlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="Read The manual again, HINT:A comma should be used a relative clause follows the main subject."
                    hintlst.append(hint)
                onounlst=list(set(crules.onoun) & set(b))
                #print(onounlst)
                if len(onounlst) > 2:
                    if (b[i-1] in crules.onoun and (b[i+1] in crules.article)):
                
                        hint="Read The manual again, HINT:A comma should be used after an object noun, when you are trying to list 2 or more nouns."
                        hintlst.append(hint)
               
                if b[i-1] in crules.onoun and b[-1]==" ":
                    hint="Read The manual again, HINT:Always end a sentence with a FULLSTOP."
                    hintlst.append(hint) 
        #--------------------------type10comma.py----------------------------------------------------------------
                if b[i-1] =="Rs" and b[i+1].isdigit():
                    hint="Incorrect Answer,HINT:When you represent an amount in Rs,add a fullstop after Rs"
                    mandlst.append(hint)     
                phrase="".join(b)
                oned=re.findall("\d+",phrase)
                #print("oned",oned[0],oned[1])
                if b[i-1]==oned[0] and b[i]=="Rs":
                    hint="Incorrect Answer, HINT:When a number is above 999, You have to put a comma after the first digit"
                    mandlst.append(hint)
                    
                if b[i-1].isdigit() and c[-1]==" ":
                    hint="Incorrect Answer, HINT:A sentence ends with a Fullstop"
                    mandlst.append(hint)
            
#-----------------------------type12stay.py-----------------------------------
                if b[i-1] in crules.verb1 and b[i+1] in crules.article:
                    hint="Read the manual again, HINT:No need of any punctuation between a verb and an article.."
                    correctlst.append(hint)
                if b[i-1] in crules.article and b[i+1]=="organisation"+".":
                    hint="Read the manual again, HINT:No need of any punctuation between a aricle and a noun.."
                    correctlst.append(hint)
                if b[i-1] =="The" and b[i+1]=="name":
                    hint="Read the manual again, HINT:No need of any punctuation between a determiner and the keyword name .."
                    correctlst.append(hint)
                if b[i-1] =="name" and b[i+1]=="of":
                    hint="Read the manual again, HINT:No need of any punctuation between and keyword name and a preposition .."
                    correctlst.append(hint)
                if b[i-1] =="of" and b[i+1] in crules.det:
                    hint="Read the manual again, HINT:No need of any punctuation between a preposition and a determiner"
                    correctlst.append(hint)
                if b[i-1] in det and b[i+1] in crules.onoun:
                    hint="Read the manual again, HINT:No need of any punctuation between a determiner and the keyword name .."
                    correctlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.vbz:
                    hint="Read the manual again, HINT:No need of any punctuation between a noun and [is/was] .."
                    correctlst.append(hint)
                if b[i-1] in crules.vbz and b[i+1] in crules.onamelst:
                    hint="Read the manual again, HINT:No need of any punctuation between [is/was] and an object name like building name,name of a person etc. "
                    correctlst.append(hint)
                if b[i-1] in crules.onamelst and b[i+1] in crules.onamelst:
                    hint="Read the manual again, HINT:There is no listing of items here, it has to be considered as a single entity.So no punctuation needed"
                    correctlst.append(hint)
                if b[i-1]=="The" and b[i+1]=="address":
                    hint="Correct Answer, HINT:No need of a punctuation after the determiner 'The'"
                    correctlst.append(hint)
                if b[i-1] =="address" and b[i+1] in crules.vbz:
                    hint="Correct Answer, HINT:No need of a punctuation after address"
                    correctlst.append(hint)
                if b[i-1] in crules.vbz and b[i+1] in crules.new_landmark:
                    hint="Correct Answer, HINT:No need of a punctuation after [is/was]"
                    correctlst.append(hint)
                if b[i-1] in crules.new_landmark and b[i+1] in crules.new_landmark:
                    hint="Correct Answer, HINT:There is no listing of items here, it has to be considered as a single entity..so no punctaution needed."
                    correctlst.append(hint)
                if b[i-1].isalpha() and b[i+1].isalpha():
                    hint="Read the manual again, HINT:No punctuation needed needed as it is an abbreviation"
                    correctlst.append(hint)              
        return(hintlst,mandlst,correctlst)
    

    
p1=crules()
hintlst,mandlst,correctlst=p1.commatwo()

for i in hintlst:
    print(i)
for j in mandlst:
    print(j)
for k in correctlst:
    print(k)

 
