import re
import datetime
import mysql.connector
mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="rohith@123",
                database="pythonlogin"
        )
mycursor = mydb.cursor()
class crules:
    snoun=['Mary','James','John','Alice','A. Roy', 'K. Singh', 'R. K. Narayan', 'R. Kushner' ]
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
    onoun=['box','book','cage','scenary','house','building','tea','water','coffee','biriyani','pulav','kichdi','novel','story','match','race','ankle','leg','first-prize','second-prize','job','position','keys','books','poem','story','furniture','vegetables','fruits','bicycles','house','organisation','school','college','flat','question']
    prep=['in','for','with','from']
    title=['Dr','Prof','Mr','Mrs','Sr','Bro','Major','Capt','Miss','Late']
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
    conjadv=['however','morever']
    coverb=['lift']
    neg=["not"]
    cordconj=['and','but']
    adverb=['slowly']
    madverb=['extremely']
    intro_words=['Although','Because','While']
    regex= "\d{4}"        #----------------------number---------------------------------------
    weekdays =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    year=['2009','2020','2021']
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
##        b=['Dr', '<m>', 'John', '<w>', 'has', '<w>', 'hurt', '<w>', 'his', '<w>', 'leg', '<m>']
##        c=[Dr. Mary, an old woman can lift a book, a cage and a box.]#        number="0"
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
    #---------------------------------------------------------<m> with no punctuation----------------------------------------------------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==" "):
                hint="Punctuations are required at mandatory locations.Click the appropriate sidepane and read the manuals"
                mandlst.append(hint)
        
    #---------------------------------------------------<m> with semicolon--------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==";"):
                  
                hint="Correct Answer:A semicolon can be used to seperate two independent clauses"
                correctlst.append(hint)
                        
    #---------------------------------------------------<m> with Comma--------------------------------------------------------------------------        
        for i in range(0,len(b)):
             if (b[i]=="<m>" and c[i]==","):
                
                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
                    hint="Correct Answer:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                    correctlst.append(hint)
                    
                elif (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="Correct Answer:A comma can be used to seperate an adjective phrase from the verbphrase"
                    correctlst.append(hint)
                    flash(hint,"success")
                elif (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="Correct Answer:A comma should be used a relative clause follows the main subject."
                    correctlst.append(hint)
                elif (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="Correct Answer:A comma should be used a relative clause follows the main subject."
                    correctlst.append(hint)
                    
                elif (b[i-1] in crules.onoun) and (b[i+1] in crules.article):    
                    hint="Correct Answer:A comma should be used after an object noun, when you are trying to list 2 or more nouns."
                    correctlst.append(hint)
                    
                elif (b[i-1] in crules.onoun) and (b[i+1] in crules.article):    
                    hint="Correct Answer:A comma should be used after an object noun, when you are trying to list 2 or more nouns."
                    correctlst.append(hint)
                    
##                elif (b[i-1]==number1) and (b[i+1]==None):    
##                    hint="Correct Answer:A comma should be used after the first number, When a number is over 999."
##                    correctlst.append(hint)
                    
                elif b[i-1].isdigit() and b[i+1]==year:
                    hint="Correct Answer:A comma should be used after a date, when it is followed by a year."
                    correctlst.append(hint)
                    
                elif b[i-1] in crules.months and b[i+1]==year and b[i+2]==None:
                    hint="Correct Answer:A comma should be used after a month, when it is followed by a date and no year is mentioned."
                    correctlst.append(hint)
                    
                elif b[i-1] in crules.weekdays and b[i+1]==crules.months :
                    hint="Correct Answer:A comma should be used after a weekday, when it is followed by a month and date."
                    correctlst.append(hint)
                    
##                elif b[i-1] in crules.flatno and b[i+1] in crules.wing :
##                    hint="Correct Answer:A comma should be used to seperate two entities-flatno and wing."
##                    correctlst.append(hint)
##                elif b[i-1] in crules.wing and b[i+1] in crules.societyname :
##                    hint="Correct Answer:A comma should be used to seperate two entities-wing and societyname."
##                    correctlst.append(hint)    
##                elif b[i-1] in crules.societyname and b[i+1] in crules.road :
##                    hint="Correct Answer:A comma should be used to seperate two entities-societyname and road."
##                    correctlst.append(hint)
##                elif b[i-1] in crules.road and b[i+1] in crules.street :
##                    hint="Correct Answer:A comma should be used to seperate two entities-road and street."
##                    correctlst.append(hint)
##                elif b[i-1] in crules.street and b[i+1] in crules.location :
##                    hint="Correct Answer:A comma should be used to seperate two entities-street and location."
##                    correctlst.append(hint)
##                elif b[i-1] in crules.new_landmark and b[i+1] in crules.city :
##                    hint="Correct Answer:A comma should be used to seperate two entities-landmark and city."
##                    correctlst.append(hint)    
##                elif b[i-1] in crules.location and b[i+1] in crules.city :
##                    hint="Correct Answer:A comma should be used to seperate two entities-street and location."
##                    correctlst.append(hint)
##                elif b[i-1] in crules.city and b[i+1] in crules.state :
##                    hint="Correct Answer:A comma should be used to seperate two entities-street and location."
##                    correctlst.append(hint)
##                elif b[i-1] in crules.state and b[i+1] in crules.pincode :
##                    hint="Correct Answer:A comma should be used to seperate two entities-state and pincode."
##                    correctlst.append(hint)
##                elif b[i-1] in crules.onoun and b[i+1] in crules.pronoun :
##                    hint="Correct Answer:A comma should be used to seperate two clauses"
##                    correctlst.append(hint) 
  #---------------------------------------------------<m> with Fullstop---------------------------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                if b[i-1] in crules.title and b[i+1] in crules.snoun:
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always put a period/fullstop after a title"
                
                    correctlst.append(hint)
                
                if b[i-1] in crules.onoun:
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                
                    correctlst.append(hint)
                    
                if b[i-1] in crules.pronoun:
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                
                    correctlst.append(hint)
                for i in b:
                    regex= "\d{4,6}"
                    regex1= "\d{1,4}"
                    if re.findall(regex, i):
                        number=i
                    elif re.findall(regex1, i):
                        number1=i     
                if b[i-1] =="Rs" and b[i+1]==number:
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always put a FULLSTOP after the keyword Rs"
                
                    correctlst.append(hint) 
                if b[i-1] =="Rs" and b[i+1]==number1:
                    hint="Correct Answer.Fullstop at appropriate place.Always put a FULLSTOP after the keyword Rs"
                    correctlst.append(hint) 

                if b[i-1]==number or b[i-1]==number1 and b[i+1]==None:
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                
                    correctlst.append(hint)
                
                if b[i-1]==str(year) and b[i+1]==None:
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                
                    correctlst.append(hint)
                if b[i-1].isdigit() and b[i+1]==None:
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                
                    correctlst.append(hint)

                if b[i-1] ==crules.onoun and b[i+1]==crules.pronoun.capitalize():
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                if b[i-1]==crules.title and b[i+1]== crules.title:
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                name=['Esmail Bagani']
                
                for i in name:
                    name1=i.split(" ")
                if b[i-1]==crules.title and b[i+1]== crules.name1[0]:
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                if b[i-1]==crules.title and b[i+1]== crules.name1[1]:
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                if b[i-1].isaplha() and b[i+1]==name1[0] or name1[1]:
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                if b[i-1]==crules.pincode and b[i+1]==None:
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                if b[i-1] in crules.onamelst and b[i+1]=="The":
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                if b[i-1]=="Pvt" and b[i+1]=="Ltd":
                    hint="Correct Answer.Fullstop at appropriate place."
                    correctlst.append(hint)
                if b[i-1]=="Ltd":
                    hint="Correct Answer.Fullstop at appropriate place.When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    correctlst.append(hint)        
  

 #--------------------------------------------------------<w> with comma-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==","):
                
                hint="Please add COMMA at appropriate locations.Click the appropriate sidepane and read the manuals"
                hintlst.append(hint)
                
     
###--------------------------------------------------------<w> with FULLSTOP-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==","):
                
                hint="Please add FULLSTOP at appropriate locations.Click the appropriate sidepane and read the manuals"
                hintlst.append(hint)
      
#--------------------------------------------------------<w> with SEMICOLON-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==";"):
                
                hint="Please add SEMICOLON at appropriate locations.Click the appropriate sidepane and read the manuals"
                hintlst.append(hint)

        return(hintlst,mandlst,correctlst)
    
    #def commatwo(b,c,correct,category,level,username,userid,eid,submittedtext):
    def commatwo(self):
        c=['Major', ',', 'John', ' ', 'a', ' ', 'charming', ' ', 'gentleman', ' ', 'could', ' ', 'open', ' ', 'a', ' ', 'box', ' ', 'a', ' ', 'book', ' ', 'and', ' ', 'a', ' ', 'cage', '.']
        b=['Major', '<m>', 'John', '<m> ', 'a', '<w> ', 'charming', '<w> ', 'gentleman', '<m> ', 'could', '<w> ', 'open', '<w>', 'a', '<w> ', 'box', ' <m>', 'a', '<w> ', 'book', '<w>', 'and', '<w> ', 'a', '<w>', 'cage', '<m>']
        number="0"
        mandlst=[]
        correctlst=[]
        hintlst=[]
        #print("commarules",b,c,correct,level,username,userid,eid,submittedtext)

       

        
    #---------------------------------------------------<m> with semicolon-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==";"):
                  
                hint="Correct Answer:A semicolon can be used to seperate two independent clauses"
                correctlst.append(hint)
                 
                score1=0
                for i in correctlst:
                    mySql_insert_query = """INSERT INTO exercisedetails (userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

                    recordTuple = (userid, username, eid,correct,submittedtext,hint,0,1,score1,datetime.datetime.now(),category,level,0)
                    mycursor.execute(mySql_insert_query, recordTuple)
                    mydb.commit()
                #print("Record inserted successfully into exercise table")        
                    
    #---------------------------------------------------<m> with Comma-------------------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):
                for i in b:
                    regex= "\d{4,6}"
                    if re.findall(regex, i):
                        print(i)
                        number=i
                        print(i)
                    if re.findall(crules.yearregex, i):
                        year=i   
                if len(number)>3 :
                    number1=number[0]
                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
                    hint="Correct Answer:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                    correctlst.append(hint)
                elif (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="Correct Answer:A comma can be used to seperate an adjective phrase from the verbphrase"
                    correctlst.append(hint)
                elif (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="Correct Answer:A comma should be used a relative clause follows the main subject."
                    correctlst.append(hint)
                elif (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="Correct Answer:A comma should be used a relative clause follows the main subject."
                    correctlst.append(hint)
                elif (b[i-1] in crules.onoun) and (b[i+1] in crules.article):    
                    hint="Correct Answer:A comma should be used after an object noun, when you are trying to list 2 or more nouns."
                    correctlst.append(hint)
                
                elif (b[i-1] in crules.onoun) and (b[i+1] in crules.article):    
                    hint="Correct Answer:A comma should be used after an object noun, when you are trying to list 2 or more nouns."
                    correctlst.append(hint)                    
                elif (b[i-1]==number1) and (b[i+1]==None):    
                    hint="Correct Answer:A comma should be used after the first number, When a number is over 999."
                    correctlst.append(hint)
                elif b[i-1].isdigit() and b[i+1]==year:
                    hint="Correct Answer:A comma should be used after a date, when it is followed by a year."
                    correctlst.append(hint)
                elif b[i-1] in crules.months and b[i+1]==year and b[i+2]==None:
                    hint="Correct Answer:A comma should be used after a month, when it is followed by a date and no year is mentioned."
                    correctlst.append(hint)
                elif b[i-1] in crules.weekdays and b[i+1]==crules.months :
                    hint="Correct Answer:A comma should be used after a weekday, when it is followed by a month and date."
                    correctlst.append(hint)
                elif b[i-1] in crules.flatno and b[i+1] in crules.wing :
                    hint="Correct Answer:A comma should be used to seperate two entities-flatno and wing."
                    correctlst.append(hint)
                elif b[i-1] in crules.wing and b[i+1] in crules.societyname :
                    hint="Correct Answer:A comma should be used to seperate two entities-wing and societyname."
                    correctlst.append(hint)    
                elif b[i-1] in crules.societyname and b[i+1] in crules.road :
                    hint="Correct Answer:A comma should be used to seperate two entities-societyname and road."
                    correctlst.append(hint)
                elif b[i-1] in crules.road and b[i+1] in crules.street :
                    hint="Correct Answer:A comma should be used to seperate two entities-road and street."
                    correctlst.append(hint)
                elif b[i-1] in crules.street and b[i+1] in crules.location :
                    hint="Correct Answer:A comma should be used to seperate two entities-street and location."
                    correctlst.append(hint)
                elif b[i-1] in crules.new_landmark and b[i+1] in crules.city :
                    hint="Correct Answer:A comma should be used to seperate two entities-landmark and city."
                    correctlst.append(hint)    
                elif b[i-1] in crules.location and b[i+1] in crules.city :
                    hint="Correct Answer:A comma should be used to seperate two entities-street and location."
                    correctlst.append(hint)
                elif b[i-1] in crules.city and b[i+1] in crules.state :
                    hint="Correct Answer:A comma should be used to seperate two entities-street and location."
                    correctlst.append(hint)
                elif b[i-1] in crules.state and b[i+1] in crules.pincode :
                    hint="Correct Answer:A comma should be used to seperate two entities-state and pincode."
                    correctlst.append(hint)
                elif b[i-1] in crules.onoun and b[i+1] in crules.pronoun :
                    hint="Correct Answer:A comma should be used to seperate two clauses"
                    correctlst.append(hint)     
                score1=0
                for i in correctlst:
                    mySql_insert_query = """INSERT INTO exercisedetails (userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

                    recordTuple = (userid, username, eid,correct,submittedtext,hint,0,1,score1,datetime.datetime.now(),category,level,0)
                    mycursor.execute(mySql_insert_query, recordTuple)
                    mydb.commit()
                sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                mycursor.execute(sql_select_query1,(eid,))
                mydb.commit()
    
    #---------------------------------------------------<m> with Fullstop--------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                if b[i-1] in crules.onoun and b[i+1]==None:
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                
                    correctlst.append(hint)
                    
                if b[i-1] in crules.pronoun and b[i+1]==None:
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                
                    correctlst.append(hint)
                for i in b:
                    regex= "\d{4,6}"
                    regex1= "\d{1,4}"
                    if re.findall(regex, i):
                        number=i
                    elif re.findall(regex1, i):
                        number1=i     
##                if b[i-1] =="Rs" and b[i+1]==number:
##                    
##                    hint="Correct Answer.Fullstop at appropriate place.Always put a FULLSTOP after the keyword Rs"
##                
##                    correctlst.append(hint) 
##                if b[i-1] =="Rs" and b[i+1]==number1:
##                    hint="Correct Answer.Fullstop at appropriate place.Always put a FULLSTOP after the keyword Rs"
##                    correctlst.append(hint) 

                if b[i-1]==number or b[i-1]==number1 and b[i+1]==None:
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                
                    correctlst.append(hint)
                if b[i-1]==number or b[i-1]==number1 and b[i+1]==None:
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                
                    correctlst.append(hint)
                if b[i-1]==year and b[i+1]==None:
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                
                    correctlst.append(hint)
                if b[i-1].isdigit() and b[i+1]==None:
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                
                    correctlst.append(hint)

                if b[i-1] ==crules.onoun and b[i+1]==crules.pronoun.capitalize():
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                if b[i-1]==crules.title and b[i+1]== crules.title:
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                name=['Esmail Bagani']
                
                for i in name:
                    name1=i.split(" ")
                if b[i-1]==crules.title and b[i+1]== crules.name1[0]:
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                if b[i-1]==crules.title and b[i+1]== crules.name1[1]:
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                if b[i-1].isaplha() and b[i+1]==name1[0] or name1[1]:
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                if b[i-1]==crules.pincode and b[i+1]==None:
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                if b[i-1] in crules.onamelst and b[i+1]=="The":
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                if b[i-1]=="Pvt" and b[i+1]=="Ltd":
                    hint="Correct Answer.Fullstop at appropriate place."
                    correctlst.append(hint)
                if b[i-1]=="Ltd":
                    hint="Correct Answer.Fullstop at appropriate place.When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    correctlst.append(hint)
                    
                mycursor = mydb.cursor()
                score1=0
                #print("details",userid, username, eid,correct,submittedtext,hint,score1,datetime.datetime.now(),category,level)
                mySql_insert_query = """INSERT INTO exercisedetails (userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

                recordTuple = (userid, username, eid,correct,submittedtext,hint,0,1,score1,datetime.datetime.now(),category,level,0)
                mycursor.execute(mySql_insert_query, recordTuple)
                mydb.commit()
                #print("Record inserted successfully into exercise table")
            sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
            mycursor.execute(sql_select_query1,(eid,))
            mydb.commit()   

   
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
                if b[i-1] in crules. hverb and b[i+1] in crules.coverb:
                  hint="Read The manual again, HINT:No need to add a comma in between a helping verb like (can,could) and a verb"
                  hintlst.append(hint)
                if b[i-1] in crules.neg and b[i+1] in crules.coverb:
                  hint="Read The manual again, HINT:No need to add a comma after a negation"
                  hintlst.append(hint)
                if b[i-1] in crules.coverb and b[i+1] in crules.pronoun:
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
                    hint="Read The manual again, HINT:No need to seperate an article and a noun with comma"
                    hintlst.append(hint)
                 
                if b[i-1] in crules.verb and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:No need to put a comma before an article if it is preceeded by a verb"
                    hintlst.append(hint)
                if b[i-1] in crules. article and b[i+1] in crules.adj:
                    hint="Read The manual again, HINT:Don't put a comma,It is an adjective phrase/noun phrase"
                    hintlst.append(hint)
                
                if b[i-1] in crules.cordconj and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:Avoid Comma after a Conjunction like [and] or [but]"
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
                    hint="Read The manual again, HINT:No need to put a comma before conjunctions like and,but etc."
                    hintlst.append(hint)
                if b[i-1] in crules.cordconj and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:No need to put a comma after conjunctions like and,but etc."
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
                for i in b:
                    regex= "\d{4,6}"
                    regex1= "\d{1,4}"
                    if re.findall(regex, i):
                        number=i
                    elif re.findall(regex1, i):
                        number1=i   
                if b[i-1] ==number1 and b[i+1] in crules.prep:
                    hint="Read the manual again, HINT:No need of a comma after an amount when it is followed by a preposition"
                if b[i-1] ==number and b[i+1] in crules.prep:
                    hint="Read the manual again, HINT:No need of a comma after an amount when it is followed by a preposition"    
                              
                if b[i-1] in crules.onoun and b[i+1] in crules.prep:
                    hint="Read the manual again, HINT:No need of a comma after an object noun when it is followed by a preposition"
                if b[i-1] in crules.onoun and b[i+1] in crules.prep:
                    hint="Read the manual again, HINT:No need of a comma after an object noun when it is followed by a preposition"
                if b[i-1] in crules.prep and b[i+1] in crules.pronoun:
                    hint="Read the manual again, HINT:No need of a comma after a preposition when it is followed by a pronoun"

                    

           #-----------------------------type11date.py---------------------------------------------------------------------------------------------------
                
                for i in b:
                    if re.findall(crules.yearregex, i):
                        year=i
                if b[i-1] in crules.prep and b[i+1] in crules.months:
                    hint="Read the manual again, HINT:No need of a comma after a preposition when it is followed by a month"
                if b[i-1] in crules.months and b[i+1].isdigit():
                    hint="Read the manual again, HINT:No need of a comma after a month when it is followed by a date"
                if b[i-1]  in crules.snoun and b[i+1] in crules.vbz:
                    hint="Read the manual again, HINT:No need of a comma after a noun when it is followed by a ['is','was']"
                if b[i-1] in crules.vbz and b[i+1] in crules.verb:
                    hint="Read the manual again, HINT:No need of a comma after ['is','was'] when it is followed by a verb"
                if b[i-1] in crules.verb and b[i+1] in crules.prep:
                    hint="Read the manual again, HINT:No need of a comma after a verb when it is followed by a preposition"
                if b[i-1] in crules.prep and b[i+1] in crules.weekdays:
                    hint="Read the manual again, HINT:No need of a comma after a prep when it is followed by a weekday"
                if b[i-1].isdigit() and b[i+1] in crules.months and b[i+2]==year:
                    hint="Read the manual again, HINT:No need of a comma after a date when it is followed by a month and a year if the date format is [15 March 2003]"          
                if b[i-1] in crules.months and b[i+1]==year and b[i+2]==None:
                    hint="Read the manual again, HINT:No need of a comma after a month when it is followed by a year if the date format is [15 March 2003]"                                     
                
         
                
 #--------------------------------quotneg.py----------------------------------------------------------          
                if b[i-1] in crules.verb and b[i+1] in crules.prep:
                    hint="Read the manual again, HINT:No need of a comma between a verb and a preposition"
                    hintlst.append(hint)
                if b[i-1] in crules.prep and b[i+1] in crules.snoun:
                    hint="Read the manual again, HINT:No need of a comma between a preposition and a noun"
                    hintlst.append(hint)     
                
#-----------------------------------type1.py----------------------------------------------------------
                if b[i-1] in crules.cnoun and b[i+1] in crules.verb:
                    hint="Read The manual again, HINT:No need to put a comma after a common noun especially when there is no enumeration..."
                    hintlst.append(hint)
                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
                    hint="Read The manual again, HINT:No need to seperate a adjective phrase with a comma"
                    hintlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.madverb:
                    hint="Read The manual again, HINT:Noun when followed by a modifying adverb,don't put a comma in between"
                    hintlst.append(hint)
                if b[i-1] in crules.madverb and b[i+1] in crules.adverb:
                    hint="Read The manual again, HINT:Modifying adverb like extremely,very etc shoud not be seperated from main adverbs using a comma"
                    hintlst.append(hint)
#--------------------------------compound.py----------------------------------------
                if b[i-1] in crules.cordconj and b[i+1] in crules.verb:
                    hint="Read The manual again, HINT:Avoid Comma after a Conjunction like [and] or [but]"
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
                    hint="Read The manual again, HINT:No need to add a comma after a verb, when it is followed by a neuter pronoun(e.g. it)"
                    hintlst.append(hint)
#--------------------------------inrocomma.py---------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.intro-words and b[i+1] in crules.snoun:
                    hint="Read The manual again, HINT:Avoid Comma after Introductory wirds like [while/Although] etc."
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
                for i in hintlst:
                    score1=0
                    mySql_insert_query = """INSERT INTO exercisedetails (userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

                    recordTuple = (userid, username, eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0)
                    mycursor.execute(mySql_insert_query, recordTuple)
                    mydb.commit()

                    
#--------------------------------------------------------<w> with FULLSTOP-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]=="."):
                
                hint="Please add FULLSTOP at appropriate locations.Click the appropriate sidepane and read the manuals"
                hintlst.append(hint)
                
                for i in hintlst:
                    score1=0
                    mySql_insert_query = """INSERT INTO exercisedetails (userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

                    recordTuple = (userid, username, eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0)
                    mycursor.execute(mySql_insert_query, recordTuple)
                    mydb.commit()
                    
                                       
                sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                mycursor.execute(sql_select_query1,(eid,))
                mydb.commit()

#--------------------------------------------------------<w> with SEMICOLON-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==","):
                
                hint="Please add SEMOCOLON at appropriate locations.Click the appropriate sidepane and read the manuals"
                hintlst.append(hint)
                
                
        
#---------------------------------------------------------<m> with no punctuation----------------------------------------------------------------------------------
        for i in range(0,len(b)):            
            if (b[i]=="<m>" and c[i]==" "):
                
                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
                    hint="Read The manual again, HINT:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                    hintlst.append(hint)
                elif (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="Read The manual again, HINT:A comma can be used to seperate an adjective phrase from the verbphrase"
                    hintlst.append(hint)
                elif (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="Read The manual again, HINT:comma should be used a relative clause follows the main subject."
                    hintlst.append(hint)
                elif (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="Read The manual again, HINT:A comma should be used a relative clause follows the main subject."
                    hintlst.append(hint)
                elif (b[i-1] in crules.onoun) and (b[i+1] in crules.article):    
                    hint="Read The manual again, HINT:A comma should be used after an object noun, when you are trying to list 2 or more nouns."
                    hintlst.append(hint) 
                    
              
        return(hintlst,mandlst,correctlst)
    
p1=crules()
hintlst,mandlst,correctlst=p1.commaone()
for i in hintlst:
    print(i)
for i in mandlst:
    print(i)
for i in correctlst:
    print(i)
    
