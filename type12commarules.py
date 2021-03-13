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
class type12crules:
    snoun=['Mary','James','John','Alice','A. Roy', 'K. Singh', 'R. K. Narayan', 'R. Kushner','Esmail','Bagani']
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
    regex= "\d{4}"
    #----------------------number---------------------------------------
    weekdays =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    #year=['2009','2020','2021']
    yearregex="[1-3][0-9]{3}"
    flatno=['Y/2/122','C-403','299/15','No:88','1304','2345']
    wing=['B-Wing']
    landmark=['Opp Presidential Complex','Next to Mutta Chambers','Near Payal Cinema Complex']
    societyname=['Sarayu Society','Sarayu Co. Housing Society Ltd.']
    road=['Satghara Road','Vallabh Bagh Lane','Padmavati Vikar Mandal Road','2NS Main Road','Coronation Road','Dhakuria Station Road']
    street=['M.R.Campus','Srinivasa Nagar','Bargarpet','Dhakuria']
    location=['Badartala','Ghatkopar','Shahibaug','Kolathur','Kolar','Jadavpur','Manesar','Santacruz']
    city=['Basirhat','Mumbai','Ahmedabad','Chennai','Bangalore','Kolkata','Gurgaon']
    state=['West Bengal','Haryana','Tamil Nadu','Karnataka','Maharashtra','Gujarat']
    statel=['West','Bengal','Tamil','Nadu']
    onamelst=['Life', 'Style', 'International', 'Pvt', 'Ltd','BMC', 'Software']
    buildingl=['Daksha', 'Bldng']
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
                        
    
    def commatwo(b,c,correct,category,level,username,userid,eid,submittedtext):
        mandlst=[]
        correctlst=[]
        hintlst=[]
##        b=['John', '<w>', 'stays', '<w>', 'in', '<w>', 'a', '<w>', 'house', '<m>', 'His', '<w>', 'address', '<w>', 'is', '<w>', 'C/O', '<w>', 'Late', '<m>', 'Mr', '<m>', 'Esmail', '<w>', 'Bagani', '<m>', 'Y/2/122', '<m>', 'B-Wing', '<m>', 'Sarayu', '<w>', 'Society', '<m>', 'Satghara', '<w>', 'Road', '<m>', 'Badartala', '<m>', 'Kolkata', '<m>', 'West', '<w>', 'Bengal', '<m>', '700044', '<m>']
##        c=['John', ' ', 'stays', ' ', 'in', ' ', 'a', ' ', 'house', '.', 'His', ' ', 'address', ' ', 'is', ' ', 'C/O', ' ', 'Late', '.', 'Mr', '.', 'Esmail', ' ', 'Bagani', ',', 'Y/2/122', ' ', 'B-Wing', ' ', 'Sarayu', ' ', 'Society', ' ', 'Satghara', ' ', 'Road', ' ', 'Badartala', ',', 'Kolkata', ' ', 'West', ' ', 'Bengal', ' ', '700044', '.']

        #print("commarules",b,c,correct,level,username,userid,eid,submittedtext)
        ##print(tagged)
##        b=['Alice', '<w>', 'joins', '<w>', 'an', '<w>', 'organisation.The', '<w>', 'name', '<w>', 'of', '<w>', 'the', '<w>', 'organisation', '<w>', 'is', '<w>', 'Life', '<w>', 'Style', '<w>', 'International', '<w>', 'Pvt', '<m>', 'Ltd', '<m>','<m>','The', '<w>', 'address', '<w>', 'Mumbai', '<m>', 'Maharashtra', '<m>', '400098', '<m>']
##        c=['Alice', ' ', 'joins', ' ', 'an', ' ', 'organisation.The', ' ', 'name', ' ', 'of', ' ', 'the', ' ', 'organisation', ' ', 'is', ' ', 'Life', ' ', 'Style', ' ', 'International', ' ', 'Pvt', '.', 'Ltd', ',', ' ', 'The', ',', 'address', ',', 'Mumbai', ',', 'Maharashtra', '.', '400098', '.']
##
##        b=['John', '<w>', 'works', '<w>', 'in', '<w>', 'an', '<w>', 'organisation.The', '<w>', 'name', '<w>', 'of', '<w>', 'the', '<w>', 'organisation', '<w>', 'is', '<w>', 'B', '<w>', 'M', '<w>', 'C', '<w>', 'Software', '<m>', 'The', '<w>', 'address', '<w>', 'Mumbai', '<m>', 'Maharashtra', '<m>', '400098', '<m>']
##        c=['John', ' ', 'works', ' ', 'in', ' ', 'an', ' ', 'organisation.The', ' ', 'name', ' ', 'of', ' ', 'the', ' ', 'organisation', ' ', 'is', ' ', 'B', '.', 'M', '.', 'C', '.', 'Software', '.', 'The', '<w>', 'address', ',', 'Mumbai', ',', 'Maharashtra', ',', '400098', '.']
##        b=['Mary', '<w>', 'stays', '<w>', 'in', '<w>', 'a', '<w>', 'house', '<m>', 'Her', '<w>', 'address', '<w>', 'is', '<w>', 'C/O', '<w>', 'Late', '<m>', 'Mr', '<m>', 'E', '<m>', 'Bagani', '<m>', 'Y/2/122', '<m>', 'B-Wing', '<m>', 'Sarayu', '<w>', 'Society', '<m>', 'Satghara', '<w>', 'Road', '<m>', 'Badartala', '<m>', 'Kolkata', '<m>', 'Bengal', '<m>', '700044', '<m>']
##        c=['Mary', ' ', 'stays', ';', 'in', ';', 'a', ' ', 'house', '.', 'Her', ' ', 'address', ',', 'is', ' ', 'C/O', ' ', 'Late', ' ', 'Mr', ' ', 'E', '.', 'Bagani', ' ', 'Y/2/122', ' ', 'B-Wing', ' ', 'Sarayu', ' ', 'Society', ' ', 'Satghara', ' ', 'Road', ' ', 'Badartala', ' ', 'Kolkata', ' ', 'Bengal', ' ', '700044', '.']
        single=[]        
        for i in c:
            if len(i)==1:
                if i>="A" and i<="Z":
                    single.append(i)
                
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
                if (b[i-1] in type12crules.onoun) and (b[i+1] in type12crules.pronoun1):    
                    hint="Read the manual again, HINT:Fullstop has to be used to seperate two statements"
                    mandlst.append(hint)
                            
                if b[i-1] in type12crules.wing and b[i+1] in type12crules.societyl:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)
                if b[i-1] in type12crules.societyl and b[i+1] in type12crules.roadl:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)      
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.location:
                    hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                    mandlst.append(hint)
                if b[i-1] in type12crules.location and b[i+1] in type12crules.city:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)
                if b[i-1] in type12crules.city and b[i+1] in type12crules.statel:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)    
                if b[i-1] in type12crules.statel and b[i+1] in type12crules.pincode:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)
                if b[i-1]==type12crules.new_landmark and b[i+1]==type12crules.city:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)
                if b[i-1] in single and b[i+1] in type12crules.snoun:
                    hint="Read the manual again, HINT:Put a fullstop between the initials of the name"
                    mandlst.append(hint)
                if b[i-1] in type12crules.pincode and c[-2]==";" and c[i+1]=="":
                    hint="Read the manual again, HINT:Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                if b[i-1] in type12crules.onamelst and b[i+1]=="The":
                    hint="Read the manual again, HINT:Always end a sentence with a FULLSTOP"
                    mandlst.append(hint)
                if b[i-1]=="Pvt" and b[i+1]=="Ltd":
                    hint="Read the manual again, HINT:When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    mandlst.append(hint)
                if b[i-1]=="Ltd":
                    hint="Read the manual again, HINT:When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    mandlst.append(hint)
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.flatno:
                    hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                    mandlst.append(hint)
                if b[i-1] in type12crules.flatno and b[i+1] in type12crules.wing:
                    hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                    mandlst.append(hint)      
                if b[i-1] in type12crules.title and b[i+1] in type12crules.snoun:
                   hint="Read the manual again, HINT:When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                   mandlst.append(hint)
                if b[i-1]=="Late":
                    hint="Read the manual again, HINT:When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    mandlst.append(hint)
              
                if b[i-1]=="Opp":
                    hint="Read the manual again, HINT:When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    mandlst.append(hint)
                if b[i-1] in single and b[i+1] in type12crules.snoun:
                    hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                    mandlst.append(hint)
                if b[i-1] in type12crules.onoun and b[i+1]=="The":
                     hint="Read the manual again, HINT: Always end a sentence with a FULLSTOP"
                     mandlst.append(hint)    
                if b[i-1] =="Ltd." and b[i+1]==" ":
                     hint="Read the manual again, HINT: Always end a sentence with a FULLSTOP"
                     mandlst.append(hint)   
                if b[i-1] in type12crules.location and b[i+1]=="The":
                     hint="Read the manual again, HINT: Always end a sentence with a FULLSTOP"
                     mandlst.append(hint)    
                if b[i-1] =="Ltd." and b[i+1]=="The":
                     hint="Read the manual again, HINT: Always end a sentence with a FULLSTOP"
                     mandlst.append(hint)          
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.city:
                    
                    hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                    mandlst.append(hint)
                if b[i-1] in type12crules.new_landmark and b[i+1] in type12crules.roadl:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)
                if b[i-1] in type12crules.flatno and b[i+1] in type12crules.new_landmark:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)
                if b[i-1] in type12crules.buildingl and b[i+1] in type12crules.flatno:
                    hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                    mandlst.append(hint)
##                if b[i-1] in type12crules.pincode:
##                     hint="Read the manual again, HINT: Always end a sentence with a FULLSTOP"
##                     mandlst.append(hint)  
    #---------------------------------------------------<m> with Comma-------------------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):

                if (b[i-1] in type12crules.onoun) and (b[i+1] in type12crules.pronoun1):    
                    hint="Read the manual again, HINT:Fullstop has to be used after the initials of a name"
                    mandlst.append(hint)
                
                if b[i-1] in type12crules.wing and b[i+1] in type12crules.societyl:
                    hint="Correct Answer,Comma is used to seperate two entities(enumeration)"
                    correctlst.append(hint)
                if b[i-1] in type12crules.societyl and b[i+1] in type12crules.roadl:
                    hint="Correct Answer,Comma is used to seperate two entities(enumeration)"
                    correctlst.append(hint)      
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.location:
                    hint="Correct Answer,Comma is used to seperate two entities(enumeration)"
                    correctlst.append(hint)
                if b[i-1] in type12crules.location and b[i+1] in type12crules.city:
                    hint="Correct Answer,Comma is used to seperate two entities(enumeration)"
                    correctlst.append(hint)
                if b[i-1] in type12crules.city and b[i+1] in type12crules.statel:
                    hint="Correct Answer,Comma is used to seperate two entities(enumeration)"
                    correctlst.append(hint)    
                if b[i-1] in type12crules.statel and b[i+1] in type12crules.pincode:
                    hint="Correct Answer,Comma is used to seperate two entities(enumeration)state"
                    correctlst.append(hint)
                if b[i-1] in single and b[i+1] in type12crules.snoun:
                    hint="Read the manual again, HINT:Put a fullstop between the initials of the name"
                    mandlst.append(hint)
                if b[i-1]in type12crules.pincode and c[-2]=="," and c[i+1]==" ":
                    hint="Read the manual again, HINT:Always end a sentence with a FULLSTOP"
                    mandlst.append(hint)
                if b[i-1] in type12crules.onamelst and b[i+1]=="The":
                    hint="Read the manual again, HINT:Always end a sentence with a FULLSTOP"
                    mandlst.append(hint)
                if b[i-1]=="Pvt" and b[i+1]=="Ltd":
                    hint="Read the manual again, HINT:When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    mandlst.append(hint)
                if b[i-1]=="Ltd":
                    hint="Read the manual again, HINT:When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    mandlst.append(hint)
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.flatno:
                    hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                    correctlst.append(hint)
                if b[i-1] in type12crules.flatno and b[i+1] in type12crules.wing:
                    hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                    correctlst.append(hint)      
                if b[i-1] in type12crules.title and b[i+1] in type12crules.snoun:
                   hint="Read the manual again, HINT:When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                   mandlst.append(hint)
                if b[i-1]=="Late":
                    hint="Read the manual again, HINT:When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    mandlst.append(hint)
              
                if b[i-1]=="Opp":
                    hint="Read the manual again, HINT:When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    mandlst.append(hint)
                if b[i-1] in type12crules.onoun and b[i+1]=="The":
                     hint="Read the manual again, HINT: Always end a sentence with a FULLSTOP"
                     mandlst.append(hint)    
                if b[i-1] =="Ltd." and c[i+1]==" ":
                     hint="Read the manual again, HINT: Always end a sentence with a FULLSTOP"
                     mandlst.append(hint)   
                if b[i-1] in type12crules.location and b[i+1]=="The":
                     hint="Read the manual again, HINT: Always end a sentence with a FULLSTOP"
                     mandlst.append(hint)    
                if b[i-1] =="Ltd." and b[i+1]=="The":
                     hint="Read the manual again, HINT: Always end a sentence with a FULLSTOP"
                     mandlst.append(hint)          
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.city:
                    
                    hint="Correct Answer,Comma is used to seperate two entities(enumeration)"
                    correctlst.append(hint)
                if b[i-1] in type12crules.new_landmark and b[i+1] in type12crules.roadl:
                     hint="Correct Answer,Comma is used to seperate two entities(enumeration)"
                     correctlst.append(hint)
                if b[i-1] in type12crules.flatno and b[i+1] in type12crules.new_landmark:
                     hint="Correct Answer,Comma is used to seperate two entities(enumeration)"
                     correctlst.append(hint)
                if b[i-1] in type12crules.buildingl and b[i+1] in type12crules.flatno:
                    hint="Correct Answer,Comma is used to seperate two entities(enumeration)"
                    correctlst.append(hint)
##                if b[i-1] in type12crules.pincode:
##                     hint="Read the manual again, HINT: Always end a sentence with a FULLSTOP"
##                     mandlst.append(hint)
    #---------------------------------------------------<m> with Fullstop--------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
               
                if (b[i-1] in type12crules.onoun) and (b[i+1] in type12crules.pronoun1):    
                    hint="Correct Ans, Fullstop has to be used to seperate two statements"
                    correctlst.append(hint)
                
                if b[i-1] in type12crules.wing and b[i+1] in type12crules.societyl:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)
                if b[i-1] in type12crules.societyl and b[i+1] in type12crules.roadl:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)      
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.location:
                    hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                    mandlst.append(hint)
                if b[i-1] in type12crules.location and b[i+1] in type12crules.city:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)
                if b[i-1] in type12crules.city and b[i+1] in type12crules.statel:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)    
                if b[i-1] in type12crules.statel and b[i+1] in type12crules.pincode:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)
                if b[i-1] in single and b[i+1] in type12crules.snoun:
                    hint="Correct Answer, Put a fullstop between the initials of the name"
                    correctlst.append(hint)
##                if c[-1]==".":
##                    hint="Correct Answer, Always end a sentence with a FULLSTOP"
##                    correctlst.append(hint)
                if b[i-1] in type12crules.pincode and c[-2]=="." and c[i+1]==" ":
                    hint="Correct Answer, Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                if b[i-1] in type12crules.onamelst and b[i+1]=="The":
                    hint="Correct Answer, Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                if b[i-1]=="Pvt" and b[i+1]=="Ltd":
                    hint="Correct Answer, When a word is abbreviated after the first few letters,x the traditional rule is to put a full stop after the abbreviation"
                    correctlst.append(hint)
                if b[i-1]=="Ltd":
                    hint="Correct Answer,When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    correctlst.append(hint)
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.flatno:
                    hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                    mandlst.append(hint)
                if b[i-1] in type12crules.flatno and b[i+1] in type12crules.wing:
                    hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                    mandlst.append(hint)     
                if b[i-1] in type12crules.title and b[i+1] in type12crules.snoun:
                   hint="Correct Answer:When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                   correctlst.append(hint)
                if b[i-1]=="Late":
                    hint="Correct Answer:When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    correctlst.append(hint)
              
                if b[i-1]=="Opp":
                    hint="Correct Answer:When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    correctlst.append(hint)
                if b[i-1] in type12crules.onoun and b[i+1]=="The":
                     hint="Correct Answer, Always end a sentence with a FULLSTOP"
                     correctlst.append(hint)    
                if b[i-1] =="Ltd." and b[i+1]==" ":
                     hint="Correct Answer, Always end a sentence with a FULLSTOP"
                     correctlst.append(hint)  
                if b[i-1] in type12crules.location and b[i+1]=="The":
                     hint="Correct Answer, Always end a sentence with a FULLSTOP"
                     correctlst.append(hint) 
                if b[i-1] =="Ltd." and b[i+1]=="The":
                     hint="Correct Answer, Always end a sentence with a FULLSTOP"
                     correctlst.append(hint)          
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.city:
                    
                    hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                    mandlst.append(hint)
                if b[i-1] in type12crules.new_landmark and b[i+1] in type12crules.roadl:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)
                if b[i-1] in type12crules.flatno and b[i+1] in type12crules.new_landmark:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)
                if b[i-1] in type12crules.buildingl and b[i+1] in type12crules.flatno:
                    hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                    mandlst.append(hint)
##                if b[i-1] in type12crules.pincode:
##                     hint="Correct Answer, Always end a sentence with a FULLSTOP"
##                     correctlst.append(hint)                
 #--------------------------------------------------------<w> with comma-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==","):


           #-----------------------------type12.py---------------------------------------------------------------------------------------------------------------------
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.verb1:
                    hint="Read the manual again, HINT:No need of a comma between a noun and a verb"
                    hintlst.append(hint)
                if b[i-1] in type12crules.verb1 and b[i+1] in type12crules.prep:
                    hint="Read the manual again, HINT:No need of a comma between a verb and a prep"
                    hintlst.append(hint)
                if b[i-1] in type12crules.prep and b[i+1] in type12crules.article:
                    hint="Read the manual again, HINT:No need of a comma between a prep and an article"
                    hintlst.append(hint)
                if b[i-1] in type12crules.article and b[i+1] in type12crules.onoun:
                    hint="Read the manual again, HINT:No need of a comma between an article and a noun"               
                    hintlst.append(hint)
                if b[i-1] in type12crules.pronoun1 and b[i+1]=="address":
                    hint="Read the manual again, HINT:No need of a comma between a noun and the word 'address'"
                    hintlst.append(hint)
                if b[i-1] =="address" and b[i+1] in type12crules.vbz:
                    hint="Read the manual again, HINT:No need of a comma between the word 'address' and [is/was]"
                    hintlst.append(hint)
                if b[i-1] in type12crules.vbz and b[i+1]=="C/O":
                    hint="Read the manual again, HINT:No need of a comma after [is/was]"
                    hintlst.append(hint)
                if b[i-1]=="C/O" and b[i+1] in type12crules.title:
                    hint="Read the manual again, HINT:No need of a comma addresstag [C/O,S/O]"
                    hintlst.append(hint)

                
                  
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.snoun:
                    hint="Read the manual again, HINT:Don't split the name with a comma"
                    hintlst.append(hint)
                if b[i-1] in type12crules.societyl and b[i+1] in type12crules.societyl:
                    hint="Read the manual again, HINT:Don't split the society name with a comma"
                    hintlst.append(hint)
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.roadl:
                    hint="Read the manual again, HINT:Don't split the road name with a comma"
                    hintlst.append(hint)
                if b[i-1] in type12crules.statel and b[i+1] in type12crules.statel:
                    hint="Read the manual again, HINT:Don't split the state name with a comma"
                    hintlst.append(hint)
                
#-----------------------------------------------------------------type12stay.py-----------------------------------
                if b[i-1] in type12crules.verb1 and b[i+1] in type12crules.article:
                    hint="Read the manual again, HINT:No need of a comma between a verb and an article.."
                    hintlst.append(hint)
                if b[i-1] in type12crules.article and b[i+1]=="organisation"+".":
                    hint="Read the manual again, HINT:No need of a comma between a aricle and a noun.."
                    hintlst.append(hint) 
                if b[i-1] =="The" and b[i+1]=="name":
                    hint="Read the manual again, HINT:No need of a comma between a determiner and the keyword name .."
                    hintlst.append(hint) 
                if b[i-1] =="name" and b[i+1]=="of":
                    hint="Read the manual again, HINT:No need of a comma between and keyword name and a preposition .."
                    hintlst.append(hint)
                if b[i-1] =="of" and b[i+1] in type12crules.det:
                    hint="Read the manual again, HINT:No need of a comma between a preposition and a determiner"
                    hintlst.append(hint)
                if b[i-1] in type12crules.det and b[i+1] in type12crules.onoun:
                    hint="Read the manual again, HINT:No need of a comma between a determiner and the keyword name .."
                    hintlst.append(hint)
                if b[i-1] in type12crules.onoun and b[i+1] in type12crules.vbz:
                    hint="Read the manual again, HINT:No need of a comma between a noun and [is/was] .."
                    hintlst.append(hint)
                if b[i-1] in type12crules.vbz and b[i+1] in type12crules.onamelst:
                    hint="Read the manual again, HINT:No need of a comma between [is/was] and an object name like building name,name of a person etc. "
                    hintlst.append(hint)
                if b[i-1] in type12crules.onamelst and b[i+1] in type12crules.onamelst:
                    hint="Read the manual again, HINT:There is no listing of items here, it has to be considered as a single entity..so please avoid comma here."
                    hintlst.append(hint)
                if b[i-1]=="The" and b[i+1]=="address":
                    hint="Read the manual again, HINT:No need of a comma between a determiner and the a propernoun 'address'"
                    hintlst.append(hint)
                if b[i-1] =="address" and b[i+1] in type12crules.vbz:
                    hint="Read the manual again, HINT:No need of a comma in between a sentence,continuity gets lost"
                    hintlst.append(hint)
                if b[i-1] in type12crules.vbz and b[i+1] in type12crules.new_landmark:
                    hint="Read the manual again, HINT:No need of a comma after [is/was]"
                    hintlst.append(hint)
                if b[i-1] in type12crules.new_landmark and b[i+1] in type12crules.new_landmark:
                    hint="Read the manual again, HINT:There is no listing of items here, it has to be considered as a single entity..so please avoid comma here."
                    hintlst.append(hint)
                if b[i-1] in single and b[i+1] in single:
                    hint="Read the manual again, HINT:No need of a comma here as it is an abbreviation"
                    hintlst.append(hint)
                if b[i-1] in single and b[i+1] in type12crules.onamelst:
                    hint="Read the manual again, HINT:No need of a comma here as it is an abbreviation"
                    hintlst.append(hint)    
                    
#--------------------------------------------------------<w> with FULLSTOP-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]=="."):
                
           #-----------------------------type12.py---------------------------------------------------------------------------------------------------------------------
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.verb1:
                    hint="Read the manual again, HINT:No need of a  fullstop between a noun and a verb"
                    hintlst.append(hint)
                if b[i-1] in type12crules.verb1 and b[i+1] in type12crules.prep:
                    hint="Read the manual again, HINT:No need of a fullstop between a verb and a prep"
                    hintlst.append(hint)
                if b[i-1] in type12crules.prep and b[i+1] in type12crules.article:
                    hint="Read the manual again, HINT:No need of a fullstop between a prep and an article"
                    hintlst.append(hint)
                if b[i-1] in type12crules.article and b[i+1] in type12crules.onoun:
                    hint="Read the manual again, HINT:No need of a fullstop between an article and a noun"
                    hintlst.append(hint)
                    
                if b[i-1] in type12crules.pronoun1 and b[i+1]=="address":
                    hint="Read the manual again, HINT:No need of a fullstop between a noun and the word 'address'"
                    hintlst.append(hint)
                if b[i-1] =="address" and b[i+1] in type12crules.vbz:
                    hint="Read the manual again, HINT:No need of a fullstop in between a sentence,continuity gets lost"
                    hintlst.append(hint)
                if b[i-1] in type12crules.vbz and b[i+1]=="C/O":
                    hint="Read the manual again, HINT:No need of a fullstop after verbtobe like is,was"
                    hintlst.append(hint)
                if b[i-1]=="C/O" and b[i+1] in type12crules.title:
                    hint="Read the manual again, HINT:No need of a fullstop addresstag [C/O,S/O]"
                    hintlst.append(hint)               
                  
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.snoun:
                    hint="Read the manual again, HINT:Don't split the name with a fullstop"
                    hintlst.append(hint)                
                if b[i-1] in type12crules.societyl and b[i+1] in type12crules.societyl:
                    hint="Read the manual again, HINT:Don't split the society name with a fullstop"
                    hintlst.append(hint)
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.roadl:
                    hint="Read the manual again, HINT:Don't split the road name with a fullstop"
                    hintlst.append(hint)
                if b[i-1] in type12crules.statel and b[i+1] in type12crules.statel:
                    hint="Read the manual again, HINT:Don't split the state name with a fullstop"
                    hintlst.append(hint)
                
#-----------------------------------------------------------------type12stay.py-----------------------------------
                if b[i-1] in type12crules.verb1 and b[i+1] in type12crules.article:
                    hint="Read the manual again, HINT:No need of a fullstop between a verb and an article.."
                    hintlst.append(hint)
                if b[i-1] in type12crules.article and b[i+1]=="organisation"+".":
                    hint="Read the manual again, HINT:No need of a fullstop between a aricle and a noun.."
                    hintlst.append(hint)
                
                if b[i-1] =="The" and b[i+1]=="name":
                    hint="Read the manual again, HINT:No need of a fullstop between a determiner and the keyword name .."
                    hintlst.append(hint)
                if b[i-1] =="name" and b[i+1]=="of":
                    hint="Read the manual again, HINT:No need of a fullstop between and keyword name and a preposition .."
                    hintlst.append(hint)
                if b[i-1] =="of" and b[i+1] in type12crules.det:
                    hint="Read the manual again, HINT:No need of a fullstop between a preposition and a determiner"
                    hintlst.append(hint)
                if b[i-1] in type12crules.det and b[i+1] in type12crules.onoun:
                    hint="Read the manual again, HINT:No need of a fullstop between a determiner and the keyword name .."
                    hintlst.append(hint)
                if b[i-1] in type12crules.onoun and b[i+1] in type12crules.vbz:
                    hint="Read the manual again, HINT:No need of a fullstop between a noun and [is/was] .."
                    hintlst.append(hint)
                if b[i-1] in type12crules.vbz and b[i+1] in type12crules.onamelst:
                    hint="Read the manual again, HINT: No need of a punctuaion in between a single phrase,as in a landmak name, building name,name of a person etc. "
                    
                    hintlst.append(hint)
                if b[i-1] in type12crules.onamelst and b[i+1] in type12crules.onamelst:
                    hint="Read the manual again, HINT:There is no need of a fullstop on beween a name."
                    hintlst.append(hint)
                if b[i-1]=="The" and b[i+1]=="address":
                    hint="Read the manual again, HINT:No need of a fullstop between a determiner and the a propernoun 'address'"
                    hintlst.append(hint)
                if b[i-1] =="address" and b[i+1] in type12crules.vbz:
                    hint="Read the manual again, HINT:No need of a fullstop between the word 'address' and [is/was]"
                    hintlst.append(hint)
                if b[i-1] in type12crules.vbz and b[i+1] in type12crules.new_landmark:
                    hint="Read the manual again, HINT:No need of a fullstop after [is/was]"
                    hintlst.append(hint)
                if b[i-1] in type12crules.new_landmark and b[i+1] in type12crules.new_landmark:
                    hint="Read the manual again, HINT: No need of a punctuaion in between a single phrase,as in a landmak name."
                    hintlst.append(hint)
                if b[i-1] in single and b[i+1] in single:
                    hint="Read the manual again, HINT:No need of a fullstop here as it is an abbreviation"
                    hintlst.append(hint)
                if b[i-1] in single and b[i+1] in type12crules.onamelst:
                    hint="Read the manual again, HINT:No need of a fullstop here as it is an abbreviation"
                    hintlst.append(hint)
              

#--------------------------------------------------------<w> with SEMICOLON-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==";"):
                                
           #-----------------------------type12.py---------------------------------------------------------------------------------------------------------------------
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.verb1:
                    hint="Read the manual again, HINT:No need of a  semicolon between a noun and a verb"
                    hintlst.append(hint)
                if b[i-1] in type12crules.verb1 and b[i+1] in type12crules.prep:
                    hint="Read the manual again, HINT:No need of a semicolon between a verb and a prep"
                    hintlst.append(hint)
                if b[i-1] in type12crules.prep and b[i+1] in type12crules.article:
                    hint="Read the manual again, HINT:No need of a semicolon between a prep and an article"
                    hintlst.append(hint)
                if b[i-1] in type12crules.article and b[i+1] in type12crules.onoun:
                    hint="Read the manual again, HINT:No need of a semicolon between an article and a noun"
                    hintlst.append(hint)
                    
                if b[i-1] in type12crules.pronoun1 and b[i+1]=="address":
                    hint="Read the manual again, HINT:No need of a semicolon between a noun and the word 'address'"
                    hintlst.append(hint)
                if b[i-1] =="address" and b[i+1] in type12crules.vbz:
                    hint="Read the manual again, HINT:No need of a semicolon between the word 'address' and [is/was]"
                    hintlst.append(hint)
                if b[i-1] in type12crules.vbz and b[i+1]=="C/O":
                    hint="Read the manual again, HINT:No need of a semicolon after [is/was]"
                    hintlst.append(hint)
                if b[i-1]=="C/O" and b[i+1] in type12crules.title:
                    hint="Read the manual again, HINT:No need of a semicolon addresstag [C/O,S/O]"
                    hintlst.append(hint)

                if b[i-1] in type12crules.snoun and b[i+1]==type12crules.snoun:
                    hint="Read the manual again, HINT:Don't split the name with a semicolon"
                    hintlst.append(hint)
              
                    
                if b[i-1] in type12crules.societyl and b[i+1] in type12crules.societyl:
                    hint="Read the manual again, HINT:Don't split the society name with a semicolon"
                    hintlst.append(hint)
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.roadl:
                    hint="Read the manual again, HINT:Don't split the road name with a semicolon"
                    hintlst.append(hint)
                if b[i-1] in type12crules.statel and b[i+1] in type12crules.statel:
                    hint="Read the manual again, HINT:Don't split the state name with a semicolon"
                    hintlst.append(hint)
                
#-----------------------------------------------------------------type12stay.py-----------------------------------
                if b[i-1] in type12crules.verb1 and b[i+1] in type12crules.article:
                    hint="Read the manual again, HINT:No need of a semicolon between a verb and an article.."
                    hintlst.append(hint)
                if b[i-1] in type12crules.article and b[i+1]=="organisation"+".":
                    hint="Read the manual again, HINT:No need of a semicolon between a aricle and a noun.."
                    hintlst.append(hint)
                
                if b[i-1] =="The" and b[i+1]=="name":
                    hint="Read the manual again, HINT:No need of a semicolon between a determiner and the keyword name .."
                    hintlst.append(hint)
                
                if b[i-1] =="name" and b[i+1]=="of":
                    hint="Read the manual again, HINT:No need of a semicolon between and keyword name and a preposition .."
                    hintlst.append(hint)
                if b[i-1] =="of" and b[i+1] in type12crules.det:
                    hint="Read the manual again, HINT:No need of a semicolon between a preposition and a determiner"
                    hintlst.append(hint)
                if b[i-1] in type12crules.det and b[i+1] in type12crules.onoun:
                    hint="Read the manual again, HINT:No need of a semicolon between a determiner and the keyword name .."
                    hintlst.append(hint)
                if b[i-1] in type12crules.onoun and b[i+1] in type12crules.vbz:
                    hint="Read the manual again, HINT:No need of a semicolon between a noun and [is/was] .."
                    hintlst.append(hint)
                if b[i-1] in type12crules.vbz and b[i+1] in type12crules.onamelst:
                    hint="Read the manual again, HINT: No need of a punctuaion after verb to be[is/was]"
                    hintlst.append(hint)
                if b[i-1] in type12crules.onamelst and b[i+1] in type12crules.onamelst:
                    hint="Read the manual again, HINT:There is no need of any punctuation in between a single phrase,as in a landmak name, building name,name of a person etc."
                    hintlst.append(hint)
                if b[i-1]=="The" and b[i+1]=="address":
                    hint="Read the manual again, HINT:No need of a fullstop between a determiner and the a propernoun 'address'"
                    hintlst.append(hint)
                if b[i-1] =="address" and b[i+1] in type12crules.vbz:
                    hint="Read the manual again, HINT:No need of a fullstop between the word 'address' and [is/was]"
                    hintlst.append(hint)
                if b[i-1] in type12crules.vbz and b[i+1] in type12crules.new_landmark:
                    hint="Read the manual again, HINT:No need of a fullstop after [is/was]"
                    hintlst.append(hint)
                if b[i-1] in type12crules.new_landmark and b[i+1] in type12crules.new_landmark:
                    hint="Read the manual again, HINT: No need of a punctuation in between a single phrase,as in a landmak name."
                    hintlst.append(hint)
                if b[i-1] in single and b[i+1] in single:
                    hint="Read the manual again, HINT:No need of a semicolon here as it is an abbreviation"
                    hintlst.append(hint)
                if b[i-1] in single and b[i+1] in type12crules.onamelst:
                    hint="Read the manual again, HINT:No need of a semicolon here as it is an abbreviation"
                    hintlst.append(hint)
                #---------------------------------------------------------<m> with no punctuation----------------------------------------------------------------------------------
        for i in range(0,len(b)):            
            if (b[i]=="<m>" and c[i]==" "):
                       #-----------------------------type12.py---------------------------------------------------------------------------------------------------------------------
                if b[i-1] in single and b[i+1] in type12crules.snoun:
                    hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                    mandlst.append(hint)
                if (b[i-1] in type12crules.onoun) and (b[i+1] in type12crules.pronoun1):    
                    hint="Read the manual again, HINT:Fullstop has to be used to seperate two statements"
                    mandlst.append(hint)
               
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.snoun:
                     hint="Correct Answer, HINT:Don't split the name with any punctuaion"
                     correctlst.append(hint)
                
                    
                if b[i-1] in type12crules.wing and b[i+1] in type12crules.societyl:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)
                if b[i-1] in type12crules.societyl and b[i+1] in type12crules.roadl:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)      
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.location:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)
                if b[i-1] in type12crules.location and b[i+1] in type12crules.city:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)
                if b[i-1] in type12crules.city and b[i+1] in type12crules.statel:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)    
                if b[i-1] in type12crules.statel and b[i+1]in type12crules.pincode:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)
                if b[i-1] in type12crules.pincode and b[i+1]==None:
                     hint="Read the manual again, HINT: Always end a sentence with a FULLSTOP"
                     mandlst.append(hint)
                if b[i-1] in type12crules.onamelst and b[i+1]=="The":
                     hint="Read the manual again, HINT: Always end a sentence with a FULLSTOP"
                     mandlst.append(hint)
                if b[i-1]=="Pvt" and b[i+1]=="Ltd":
                     hint="Read the manual again, HINT:When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                     mandlst.append(hint)
                if b[i-1]=="Ltd":
                     hint="Read the manual again, HINT:When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                     mandlst.append(hint)
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.flatno:
                    hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                    mandlst.append(hint)
                if b[i-1] in type12crules.flatno and b[i+1] in type12crules.wing:
                    hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                    mandlst.append(hint)      
                if b[i-1] in type12crules.title and b[i+1] in type12crules.snoun:
                   hint="Read the manual again, HINT:When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                   mandlst.append(hint)
                if b[i-1]=="Late":
                    hint="Read the manual again, HINT:When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    mandlst.append(hint)
              
                if b[i-1]=="Opp":
                    hint="Read the manual again, HINT:When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    mandlst.append(hint)
                if b[i-1] in type12crules.onoun and b[i+1]=="The":
                     hint="Read the manual again, HINT: Always end a sentence with a FULLSTOP"
                     mandlst.append(hint)    
                if b[i-1] =="Ltd." and c[i+1]==" ":
                     hint="Read the manual again, HINT: Always end a sentence with a FULLSTOP"
                     mandlst.append(hint)   
                if b[i-1] in type12crules.location and b[i+1]=="The":
                     hint="Read the manual again, HINT: Always end a sentence with a FULLSTOP"
                     mandlst.append(hint)    
                if b[i-1] =="Ltd." and b[i+1]=="The":
                     hint="Read the manual again, HINT: Always end a sentence with a FULLSTOP"
                     mandlst.append(hint)          
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.city:
                    
                    hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                    mandlst.append(hint)
                if b[i-1] in type12crules.new_landmark and b[i+1] in type12crules.roadl:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)
                if b[i-1] in type12crules.flatno and b[i+1] in type12crules.new_landmark:
                     hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                     mandlst.append(hint)
                if b[i-1] in type12crules.buildingl and b[i+1] in type12crules.flatno:
                    hint="Read the manual again, HINT:Comma is used to seperate two entities(enumeration)"
                    mandlst.append(hint)
##                if b[i-1] in type12crules.pincode:
##                     hint="Read the manual again, HINT: Always end a sentence with a FULLSTOP"
##                     mandlst.append(hint)      
   
        return(hintlst,mandlst,correctlst,mandatory)
    
    def commathree(b,c,correct,category,level,username,userid,eid,submittedtext):
    #def commathree(self):    
        mandlst=[]
        correctlst=[]
        hintlst=[]
##        b=['James', '<w>', 'stays', '<w>', 'in', '<w>', 'a', '<w>', 'flat', '<m>', 'His', '<w>', 'address', '<w>', 'is', '<w>', 'Mr', '<m>', 'Esmail', '<w>', 'Bagani', '<m>', 'Y/2/122', '<m>', 'B-Wing', '<m>', 'Sarayu', '<w>', 'Society', '<m>', 'Satghara', '<w>', 'Road', '<m>', 'Badartala', '<m>', 'Kolkata', '<m>', 'West', '<w>', 'Bengal', '<m>', '700044', '<m>']
##        c=['James', ' ', 'stays', ' ', 'in', ' ', 'a', ' ', 'flat', '.', 'His', ' ', 'address', ' ', 'is', ' ', 'C/O', ' ', 'Late', ' ', 'Mr', ' ', 'Esmail', ' ', 'Bagani', ' ', 'Y/2/122', ' ', 'B-Wing', ' ', 'Sarayu', ' ', 'Society', ' ', 'Satghara', ' ', 'Road', ' ', 'Badartala', ' ', 'Kolkata', ' ', 'West', ' ', 'Bengal', ' ', '700044', '.']
##        b=['Alice', '<w>', 'stays', '<w>', 'in', '<w>', 'a', '<w>', 'house', '<m>', 'Her', '<w>', 'address', '<w>', 'is', '<w>', 'Daksha', '<w>', 'Bldng', '<m>', 'C-403', '<m>', 'Opp.', '<m>', 'Presidential', '<w>', 'Complex', '<m>', 'Vallabh', '<w>', 'Bagh', '<w>', 'Lane', '<m>', 'Mumbai', '<m>', 'Maharashtra', '<m>', '400077', '<m>', ' ']
##        c=['Alice', ' ', 'stays', ' ', 'in', ' ', 'a', ' ', 'house', ' ', 'Her', ' ', 'address', ' ', 'is', ' ', 'Daksha', ' ', 'Bldng', ' ', 'C-403', ' ', 'Opp', ' ', 'Presidential', ' ', 'Complex', ' ', 'Vallabh', ' ', 'Bagh', ' ', 'Lane', ' ', 'Ghatkopar', ' ', 'Mumbai', ' ', 'Maharashtra', ' ', '400077', ' ', ' ']
##        b=['John', '<w>', 'stays', '<w>', 'in', '<w>', 'a', '<w>', 'house', '<m>', 'His', '<w>', 'address', '<w>', 'is', '<w>', 'C/O', '<w>', 'Late', '<m>', 'Mr', '<m>', 'Esmail', '<w>', 'Bagani', '<m>', 'Y/2/122', '<m>', 'B-Wing', '<m>', 'Sarayu', '<w>', 'Society', '<m>', 'Satghara', '<w>', 'Road', '<m>', 'Badartala', '<m>', 'Kolkata', '<m>', 'West', '<w>', 'Bengal', '<m>', '700044', '<m>']
##        c=['John', ' ', 'stays', ' ', 'in', ' ', 'a', ' ', 'house', '.', 'His', ' ', 'address', ' ', 'is', ' ', 'C/O', ' ', 'Late', '.', 'Mr', '.', 'Esmail', ' ', 'Bagani', ',', 'Y/2/122', ' ', 'B-Wing', ' ', 'Sarayu', ' ', 'Society', ' ', 'Satghara', ' ', 'Road', ' ', 'Badartala', ',', 'Kolkata', ' ', 'West', ' ', 'Bengal', ' ', '700044', '.']

        #print("commarules",b,c,correct,level,username,userid,eid,submittedtext)
        ##print(tagged)
##        b=['Alice', '<w>', 'joins', '<w>', 'an', '<w>', 'organisation.The', '<w>', 'name', '<w>', 'of', '<w>', 'the', '<w>', 'organisation', '<w>', 'is', '<w>', 'Life', '<w>', 'Style', '<w>', 'International', '<w>', 'Pvt', '<m>', 'Ltd', '<m>','<m>','The', '<w>', 'address', '<w>', 'Mumbai', '<m>', 'Maharashtra', '<m>', '400098', '<m>']
##        c=['Alice', ' ', 'joins', ' ', 'an', ' ', 'organisation.The', ' ', 'name', ' ', 'of', ' ', 'the', ' ', 'organisation', ' ', 'is', ' ', 'Life', ' ', 'Style', ' ', 'International', ' ', 'Pvt', '.', 'Ltd', ',', ' ', 'The', ',', 'address', ',', 'Mumbai', ',', 'Maharashtra', '.', '400098', '.']
##
##        b=['John', '<w>', 'works', '<w>', 'in', '<w>', 'an', '<w>', 'organisation.The', '<w>', 'name', '<w>', 'of', '<w>', 'the', '<w>', 'organisation', '<w>', 'is', '<w>', 'B', '<w>', 'M', '<w>', 'C', '<w>', 'Software', '<m>', 'The', '<w>', 'address', '<w>', 'Mumbai', '<m>', 'Maharashtra', '<m>', '400098', '<m>']
##        c=['John', ' ', 'works', ' ', 'in', ' ', 'an', ' ', 'organisation.The', ' ', 'name', ' ', 'of', ' ', 'the', ' ', 'organisation', ' ', 'is', ' ', 'B', '.', 'M', '.', 'C', '.', 'Software', '.', 'The', '<w>', 'address', ',', 'Mumbai', ',', 'Maharashtra', ',', '400098', '.']
##        b=['Mary', '<w>', 'stays', '<w>', 'in', '<w>', 'a', '<w>', 'house', '<m>', 'Her', '<w>', 'address', '<w>', 'is', '<w>', 'C/O', '<w>', 'Late', '<m>', 'Mr', '<m>', 'E', '<m>', 'Bagani', '<m>', 'Y/2/122', '<m>', 'B-Wing', '<m>', 'Sarayu', '<w>', 'Society', '<m>', 'Satghara', '<w>', 'Road', '<m>', 'Badartala', '<m>', 'Kolkata', '<m>', 'Bengal', '<m>', '700044', '<m>']
##        c=['Mary', ' ', 'stays', ';', 'in', ';', 'a', ' ', 'house', '.', 'Her', ' ', 'address', ',', 'is', ' ', 'C/O', ' ', 'Late', ' ', 'Mr', ' ', 'E', '.', 'Bagani', ' ', 'Y/2/122', ' ', 'B-Wing', ' ', 'Sarayu', ' ', 'Society', ' ', 'Satghara', ' ', 'Road', ' ', 'Badartala', ' ', 'Kolkata', ' ', 'Bengal', ' ', '700044', '.']
        single=[]        
        for i in c:
            if len(i)==1:
                if i>="A" and i<="Z":
                    single.append(i)
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
                if b[i-1] in single and b[i+1] in type12crules.snoun:
                    hint="Remove the Semicolon,Put a Fullstop after: "+ b[i-1]
                    mandlst.append(hint) 
                if (b[i-1] in type12crules.onoun) and (b[i+1] in type12crules.pronoun1):    
                    hint="Remove Semicolon and Put Mandatory Fullstop  after: "+b[i-1]
                    mandlst.append(hint)
                
               
                if b[i-1] in cules.wing and b[i+1] in type12crules.societyl:
                     hint="Remove Semicolon and Put Mandatory Comma  after: "+ b[i-1]
                     mandlst.append(hint)
                if b[i-1] in type12crules.societyl and b[i+1] in type12crules.roadl:
                     hint="Remove Semicolon and Put Mandatory COmma  after: "+ b[i-1]
                     mandlst.append(hint)      
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.location:
                     hint="Remove Semicolon and Put a Mandatory COmma  after: "+ b[i-1]
                     mandlst.append(hint)
                     
                if b[i-1] in type12crules.location and b[i+1] in type12crules.city:
                     hint="Remove Semicolon and Put a Mandatory COmma  after: "+ b[i-1]
                     mandlst.append(hint)
                     
                if b[i-1] in type12crules.city and b[i+1] in type12crules.statel:
                     hhint="Remove Semicolon and Put a Mandatory COmma  after: "+ b[i-1]
                     mandlst.append(hint)
                     
                if b[i-1] in type12crules.statel and b[i+1] in type12crules.pincode:
                     hint="Remove Semicolon and Put a Mandatory COmma  after: "+ b[i-1]
                     mandlst.append(hint)
                     
                if b[i-1]==type12crules.new_landmark and b[i+1]==type12crules.city:
                     hint="Remove Semicolon and Put a Mandatory COmma  after: "+ b[i-1]
                     mandlst.append(hint)
                     
                if b[i-1] in single and b[i+1] in type12crules.snoun:
                     hint="Remove Semicolon and Put a Mandatory Fullstop  after: "+ b[i-1]
                     mandlst.append(hint)
                     
                if b[i-1] in type12crules.pincode and c[-2]==";" and c[i+1]==" ":
                     hint="Remove Semicolon and Put a Mandatory Comma  after: "+ b[i-1]
                     mandlst.append(hint)      
                if b[i-1] in type12crules.onamelst and b[i+1]=="The":
                    hint="Remove Semicolon and Put a Mandatory Fullstop  after: "+ b[i-1]
                    mandlst.append(hint)
                    
                if b[i-1]=="Pvt" and b[i+1]=="Ltd":
                    hint="Remove Semicolon and Put a Mandatory Fullstop  after: "+ b[i-1]
                    mandlst.append(hint)
                    
                if b[i-1]=="Ltd":
                    hint="Remove Semicolon and Put a Mandatory Fullstop  after: "+ b[i-1]
                    mandlst.append(hint) 
                                  
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.flatno:
                    hint="Remove Semicolon and Put a Mandatory Comma  after: "+ b[i-1]
                    mandlst.append(hint)    
                if b[i-1] in type12crules.title and b[i+1] in type12crules.snoun:
                    hint="Remove the Semicolon and Put Mandatory Comma after: "+ b[i-1]
                    mandlst.append(hint)
               
                if b[i-1]=="Late":
                    hint="Remove Semicolon and Put a Mandatory Fullstop  after: "+ b[i-1]
                    mandlst.append(hint)
                if b[i-1] in type12crules.title and b[i+1] in type12crules.snoun:
                    hint="Remove a Semicolon and Put a Mandatory Fullstop after: "+ b[i-1]
                    mandlst.append(hint)    
                
                if b[i-1]=="Opp":
                    hint="Remove a Semicolon and Put a Mandatory Fullstop after: "+ b[i-1]
                    mandlst.append(hint)  
                if b[i-1] in type12crules.onoun and b[i+1]=="The":
                     hint="Remove the  semicolon and Put a mandatory Fullstop after: "+ b[i-1]
                     mandlst.append(hint)    
                if b[i-1] =="Ltd." and c[i+1]==" ":
                     hint="Remove the  semicolon and Put a mandatory Fullstop after: "+ b[i-1]
                     mandlst.append(hint)   
                if b[i-1] in type12crules.location and b[i+1]=="The":
                     hint="Remove the  semicolon and Put a mandatory Fullstop after: "+ b[i-1]
                     mandlst.append(hint)    
                if b[i-1] =="Ltd." and b[i+1]=="The":
                     hint="Remove the  semicolon and Put a mandatory Fullstop after: "+ b[i-1]
                     mandlst.append(hint)          
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.city:
                    
                    hint="Remove the  semicolon and Put a mandatory Comma after: "+b[i-1]
                    mandlst.append(hint)
                if b[i-1] in type12crules.new_landmark and b[i+1] in type12crules.roadl:
                     hint="Remove the  semicolon and Put a mandatory Comma after: "+ b[i-1]
                     mandlst.append(hint)
                if b[i-1] in type12crules.flatno and b[i+1] in type12crules.new_landmark:
                     hint="Remove the  semicolon and Put a mandatory Comma after: "+ b[i-1]
                     mandlst.append(hint)
                if b[i-1] in type12crules.buildingl and b[i+1] in type12crules.flatno:
                     hint="Remove the  semicolon and put a mandatory comma after: "+ b[i-1]
                     mandlst.append(hint)
##                if b[i-1] in type12crules.pincode:
##                     hint="Remove the  semicolon and Put a mandatory Fullstop after: "+ b[i-1]
##                     mandlst.append(hint)
    #---------------------------------------------------<m> with Comma-------------------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):
                
                   
                if (b[i-1] in type12crules.onoun) and (b[i+1] in type12crules.pronoun1):    
                   hint="Remove the Comma and Put Mandatory Fullstop  after: "+ b[i-1]
                   mandlst.append(hint) 
                
                if b[i-1] in type12crules.wing and b[i+1] in type12crules.societyl:
                    hint="Correct Answer,Comma is used to seperate two entities(enumeration)"
                    correctlst.append(hint)
                if b[i-1] in type12crules.societyl and b[i+1] in type12crules.roadl:
                    hint="Correct Answer,Comma is used to seperate two entities(enumeration)"
                    correctlst.append(hint)      
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.location:
                    hint="Correct Answer,Comma is used to seperate two entities(enumeration)"
                    correctlst.append(hint)
                if b[i-1] in type12crules.location and b[i+1] in type12crules.city:
                    hint="Correct Answer,Comma is used to seperate two entities(enumeration)"
                    correctlst.append(hint)
                if b[i-1] in type12crules.city and b[i+1] in type12crules.statel:
                    hint="Correct Answer,Comma is used to seperate two entities(enumeration)"
                    correctlst.append(hint)    
                if b[i-1] in type12crules.statel and b[i+1] in type12crules.pincode:
                    C
                if b[i-1] in single and b[i+1] in type12crules.snoun:
                    hint="Remove the Comma and Put Mandatory Fullstop after: "+ b[i-1]
                    mandlst.append(hint) 
                if b[i-1]in type12crules.pincode and c[-1]==",":
                    hint="Remove the Comma and Put Mandatory Fullstop after: "+ b[i-1]
                    mandlst.append(hint) 
                if b[i-1] in type12crules.onamelst and b[i+1]=="The":
                    hint="Remove the Comma and Put Mandatory Fullstop after: "+ b[i-1]
                    mandlst.append(hint) 
                if b[i-1]=="Pvt" and b[i+1]=="Ltd":
                    hint="Remove the Comma and Put Mandatory Fullstop after: "+ b[i-1]
                    mandlst.append(hint) 
                if b[i-1]=="Ltd":
                   hint="Remove the Comma and Put Mandatory Fullstop after: "+ b[i-1]
                   mandlst.append(hint) 
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.flatno:
                    hint="Remove the Comma and Put Mandatory Fullstop after: "+ b[i-1]
                    mandlst.append(hint)    
                
                if b[i-1]=="Late":
                    hint="Remove COmma and Put a Mandatory Fullstop  after: "+ b[i-1]
                    mandlst.append(hint)
                    
                if b[i-1] in type12crules.title and b[i+1] in type12crules.snoun:
                    hint="Remove Comma and Put a Mandatory Fullstop after: "+ b[i-1]
                    mandlst.append(hint)
                    
                if b[i-1] in type12crules.flatno and b[i+1] in type12crules.wing:
                    hint="Correct Answer,Comma is used to seperate two entities(enumeration)"
                    correctlst.append(hint)
                    
                if b[i-1]=="Opp":
                    hint="Remove the Comma and Put a Mandatory Fullstop after: "+ b[i-1]
                    mandlst.append(hint)  
                if b[i-1] in type12crules.onoun and b[i+1]=="The":
                     hint="Remove the Comma and Put a mandatory Fullstop after: "+ b[i-1]
                     mandlst.append(hint)    
                if b[i-1] =="Ltd." and c[i+1]==" ":
                     hint="Remove the Comma and Put a mandatory Fullstop after: "+ b[i-1]
                     mandlst.append(hint)   
                if b[i-1] in type12crules.location and b[i+1]=="The":
                     hint="Remove the Comma and Put a mandatory Fullstop after: "+ b[i-1]
                     mandlst.append(hint)    
                if b[i-1] =="Ltd." and b[i+1]=="The":
                     hint="Remove the Comma and Put a mandatory Fullstop after: "+ b[i-1]
                     mandlst.append(hint)          
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.city:
                    
                    hint="Correct Answer,Comma is used to seperate two entities(enumeration)"
                    correctlst.append(hint)
                if b[i-1] in type12crules.new_landmark and b[i+1] in type12crules.roadl:
                     hint="Correct Answer,Comma is used to seperate two entities(enumeration)"
                     correctlst.append(hint)
                if b[i-1] in type12crules.flatno and b[i+1] in type12crules.new_landmark:
                     hint="Correct Answer,Comma is used to seperate two entities(enumeration)"
                     correctlst.append(hint)
                if b[i-1] in type12crules.buildingl and b[i+1] in type12crules.flatno:
                     hint="Correct Answer,Comma is used to seperate two entities(enumeration)"
                     correctlst.append(hint)
##                if b[i-1] in type12crules.pincode:
##                     hint="Put a mandatory Fullstop after: "+ b[i-1]
##                     mandlst.append(hint)
                
    #---------------------------------------------------<m> with Fullstop--------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                
                if (b[i-1] in type12crules.onoun) and (b[i+1] in type12crules.pronoun1):    
                    hint="Correct Ans, Fullstop has to be used to seperate two statements"
                    correctlst.append(hint)
                
                if b[i-1] in type12crules.wing and b[i+1] in type12crules.societyl:
                    hint="Remove the Fullstop and Put Mandatory Comma after: "+ b[i-1]
                    mandlst.append(hint) 
                if b[i-1] in type12crules.societyl and b[i+1] in type12crules.roadl:
                     hint="Remove the Fullstop and Put Mandatory Comma after: "+ b[i-1]
                     mandlst.append(hint)     
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.location:
                    hint="Remove the Fullstop and Put Mandatory Comma after: "+ b[i-1]
                    mandlst.append(hint)
                if b[i-1] in type12crules.location and b[i+1] in type12crules.city:
                    hint="Remove the Fullstop and Put Mandatory Comma after: "+ b[i-1]
                    mandlst.append(hint)
                if b[i-1] in type12crules.city and b[i+1] in type12crules.statel:
                    hint="Remove the Fullstop and Put Mandatory Comma after: "+ b[i-1]
                    mandlst.append(hint)   
                if b[i-1] in type12crules.statel and b[i+1] in type12crules.pincode:
                    hint="Remove the Fullstop and Put Mandatory Comma after: "+ b[i-1]
                    mandlst.append(hint)
                if b[i-1] in single and b[i+1] in type12crules.snoun:
                    hint="Correct Answer, Put a fullstop between the initials of the name"
                    correctlst.append(hint)
##                if c[-1]==".":
##                    hint="Correct Answer, Always end a sentence with a FULLSTOP"
##                    correctlst.append(hint)
                if b[i-1] in type12crules.pincode and c[-2]=="." and c[i+1]==" ":
                    hint="Correct Answer, Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                if b[i-1] in type12crules.onamelst and b[i+1]=="The":
                    hint="Correct Answer, Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
                if b[i-1]=="Pvt" and b[i+1]=="Ltd":
                    hint="Correct Answer, When a word is abbreviated after the first few letters,x the traditional rule is to put a full stop after the abbreviation"
                    correctlst.append(hint)
                if b[i-1]=="Ltd":
                    hint="Correct Answer,When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    correctlst.append(hint)
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.flatno:
                    hint="Remove the Comma and Put Mandatory Fullstop after: "+ b[i-1]
                    mandlst.append(hint)    
                
                if b[i-1]=="Late":
                    hint="Correct Answer, When a word is abbreviated after the first few letters,the traditional rule is to put a full stop after the abbreviation"
                    correctlst.append(hint)  
                
                if b[i-1] in type12crules.flatno and b[i+1] in type12crules.wing:
                     hint="Remove the Fullstop and Put a mandatory Comma after: "+ b[i-1]
                     mandlst.append(hint)    
                if b[i-1] in type12crules.title and b[i+1] in type12crules.snoun:
                    hint="Remove the Fullstop and Put Mandatory Comma after: "+ b[i-1]
                    mandlst.append(hint)
               
               #type12add2
                    
                if b[i-1]=="Opp":
                    hint="Correct Answer, When a word is abbreviated after the first few letters,the traditional rule is to put a full stop after the abbreviation"
                    correctlst.append(hint)  
                
                if b[i-1] in type12crules.onoun and b[i+1]=="The":
                    hint="Correct Answer, Always end a sentence with fullstop"
                    correctlst.append(hint)  
                if b[i-1] =="Ltd." and c[i+1]==" ":
                     hint="Correct Answer, Always end a sentence with fullstop"
                     correctlst.append(hint)  
                if b[i-1] in type12crules.location and b[i+1]=="The":
                    hint="Correct Answer, Always end a sentence with fullstop"
                    correctlst.append(hint)    
                if b[i-1] =="Ltd." and b[i+1]=="The":
                    hint="Correct Answer, Always end a sentence with fullstop"
                    correctlst.append(hint)         
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.city:
                    
                    hint="Put a mandatory Comma after: "+b[i-1]
                    mandlst.append(hint)
                if b[i-1] in type12crules.new_landmark and b[i+1] in type12crules.roadl:
                     hint="Put a mandatory Comma after: "+ b[i-1]
                     mandlst.append(hint)
                if b[i-1] in type12crules.flatno and b[i+1] in type12crules.new_landmark:
                     hint="Put a mandatory Comma after: "+ b[i-1]
                     mandlst.append(hint)
                if b[i-1] in type12crules.buildingl and b[i+1] in type12crules.flatno:
                     hint="Put a mandatory Comma after: "+ b[i-1]
                     mandlst.append(hint)
##                if b[i-1] in type12crules.pincode:
##                     hint="Correct Answer, Always end a sentence with fullstop"
##                     correctlst.append(hint)
                
                            
 #--------------------------------------------------------<w> with comma-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==","):


           #-----------------------------type12.py---------------------------------------------------------------------------------------------------------------------
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.verb1:
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint) 
                if b[i-1] in type12crules.verb1 and b[i+1] in type12crules.prep:
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.prep and b[i+1] in type12crules.article:
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.article and b[i+1] in type12crules.onoun:
                    hinhint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)             
                    
                if b[i-1] in type12crules.pronoun1 and b[i+1]=="address":
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] =="address" and b[i+1] in type12crules.vbz:
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)       
                if b[i-1] in type12crules.vbz and b[i+1]=="C/O":
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1]=="C/O" and b[i+1] in type12crules.title:
                    hhint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)

                if b[i-1] in type12crules.societyl and b[i+1] in type12crules.societyl:
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.roadl:
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.statel and b[i+1] in type12crules.statel:
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                
#-----------------------------------------------------------------type12stay.py-----------------------------------
                if b[i-1] in type12crules.verb1 and b[i+1] in type12crules.article:
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.article and b[i+1]=="organisation"+".":
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                
                if b[i-1] =="The" and b[i+1]=="name":
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                
                if b[i-1] =="name" and b[i+1]=="of":
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    mandlst.append(hint)
                if b[i-1] =="of" and b[i+1] in type12crules.det:
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.det and b[i+1] in type12crules.onoun:
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.onoun and b[i+1] in type12crules.vbz:
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.vbz and b[i+1] in type12crules.onamelst:
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.onamelst and b[i+1] in type12crules.onamelst:
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1]=="The" and b[i+1]=="address":
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] =="address" and b[i+1] in type12crules.vbz:
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.vbz and b[i+1] in type12crules.new_landmark:
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.new_landmark and b[i+1] in type12crules.new_landmark:
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in single and b[i+1] in single:
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in single and b[i+1] in type12crules.onamelst:
                    hint="Remove the Comma ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)  
                    
#--------------------------------------------------------<w> with FULLSTOP-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]=="."):
                
           #-----------------------------type12.py---------------------------------------------------------------------------------------------------------------------
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.verb1:
                    hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)  
                    
                if b[i-1] in type12crules.verb1 and b[i+1] in type12crules.prep:
                    hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)  
                if b[i-1] in type12crules.prep and b[i+1] in type12crules.article:
                   hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                   hintlst.append(hint)  
                if b[i-1] in type12crules.article and b[i+1] in type12crules.onoun:
                    hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)  
                    
                if b[i-1] in type12crules.pronoun1 and b[i+1]=="address":
                   hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                   hintlst.append(hint)  
                if b[i-1] =="address" and b[i+1] in type12crules.vbz:
                   hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                   hintlst.append(hint)  
                if b[i-1] in type12crules.vbz and b[i+1]=="C/O":
                   hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                   hintlst.append(hint)  
                if b[i-1]=="C/O" and b[i+1] in type12crules.title:
                   hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                   hintlst.append(hint)                
                  
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.snoun:
                   hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                   hintlst.append(hint)                
                if b[i-1] in type12crules.societyl and b[i+1] in type12crules.societyl:
                    hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)  
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.roadl:
                    hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)  
                if b[i-1] in type12crules.statel and b[i+1] in type12crules.statel:
                    hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)  
                
#-----------------------------------------------------------------type12stay.py-----------------------------------
                if b[i-1] in type12crules.verb1 and b[i+1] in type12crules.article:
                    hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)  
                if b[i-1] in type12crules.article and b[i+1]=="organisation"+".":
                    hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)  
                
                if b[i-1] =="The" and b[i+1]=="name":
                    hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)  
                if b[i-1] =="name" and b[i+1]=="of":
                    hint="Read the manual again, HINT:No need of a fullstop between and keyword name and a preposition .."
                    hintlst.append(hint)
                if b[i-1] =="of" and b[i+1] in type12crules.det:
                    hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)  
                if b[i-1] in type12crules.det and b[i+1] in type12crules.onoun:
                    hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)  
                if b[i-1] in type12crules.onoun and b[i+1] in type12crules.vbz:
                    hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)  
                if b[i-1] in type12crules.vbz and b[i+1] in type12crules.onamelst:
                    hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)  
                if b[i-1] in type12crules.onamelst and b[i+1] in type12crules.onamelst:
                    hint="Read the manual again, HINT:There is no need of a fullstop on beween a name."
                    hintlst.append(hint)
                if b[i-1]=="The" and b[i+1]=="address":
                    hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)  
                if b[i-1] =="address" and b[i+1] in type12crules.vbz:
                    hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)  
                if b[i-1] in type12crules.vbz and b[i+1] in type12crules.new_landmark:
                    hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)  
                if b[i-1] in type12crules.new_landmark and b[i+1] in type12crules.new_landmark:
                    hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)  
                if b[i-1] in single and b[i+1] in single:
                    hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)  
                if b[i-1] in single and b[i+1] in type12crules.onamelst:
                   hint="Remove the Fullstop ,no need of any punctuation after: "+ b[i-1]
                   hintlst.append(hint)  

#--------------------------------------------------------<w> with SEMICOLON-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==";"):
                                
           #-----------------------------type12.py---------------------------------------------------------------------------------------------------------------------
                
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.verb1:
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.verb1 and b[i+1] in type12crules.prep:
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.prep and b[i+1] in type12crules.article:
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.article and b[i+1] in type12crules.onoun:
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                    
                if b[i-1] in type12crules.pronoun1 and b[i+1]=="address":
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] =="address" and b[i+1] in type12crules.vbz:
                   hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                   hintlst.append(hint)
                if b[i-1] in type12crules.vbz and b[i+1]=="C/O":
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1]=="C/O" and b[i+1] in type12crules.title:
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)

                if b[i-1] in type12crules.snoun and b[i+1]==type12crules.snoun:
                   hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                   hintlst.append(hint)
              
                    
                if b[i-1] in type12crules.societyl and b[i+1] in type12crules.societyl:
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.roadl:
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.statel and b[i+1] in type12crules.statel:
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
#-----------------------------------------------------------------type12stay.py-----------------------------------
                if b[i-1] in type12crules.verb1 and b[i+1] in type12crules.article:
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.article and b[i+1]=="organisation"+".":
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                
                if b[i-1] =="The" and b[i+1]=="name":
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] =="name" and b[i+1]=="of":
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] =="of" and b[i+1] in type12crules.det:
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.det and b[i+1] in type12crules.onoun:
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.onoun and b[i+1] in type12crules.vbz:
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.vbz and b[i+1] in type12crules.onamelst:
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.onamelst and b[i+1] in type12crules.onamelst:
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1]=="The" and b[i+1]=="address":
                    hhint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] =="address" and b[i+1] in type12crules.vbz:
                   hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                   hintlst.append(hint)
                if b[i-1] in type12crules.vbz and b[i+1] in type12crules.new_landmark:
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in type12crules.new_landmark and b[i+1] in type12crules.new_landmark:
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in single and b[i+1] in single:
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)
                if b[i-1] in single and b[i+1] in type12crules.onamelst:
                    hint="Remove the semicolon ,no need of any punctuation after: "+ b[i-1]
                    hintlst.append(hint)


                    
                #---------------------------------------------------------<m> with no punctuation----------------------------------------------------------------------------------
        for i in range(0,len(b)):            
            if (b[i]=="<m>" and c[i]==" "):
                       #-----------------------------type12.py---------------------------------------------------------------------------------------------------------------------
                if b[i-1] in single and b[i+1] in type12crules.snoun:
                    hint="Put a mandaory fullstop after: "+ b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in type12crules.onoun) and (b[i+1] in type12crules.pronoun1):    
                    hint="Put a mandatory Fullstop after: "+b[i-1]
                    mandlst.append(hint)
                
                
                if b[i-1] in type12crules.wing and b[i+1] in type12crules.societyl:
                     hint="Put a mandatory Comma after: "+ b[i-1]
                     mandlst.append(hint)
                if b[i-1] in type12crules.societyl and b[i+1] in type12crules.roadl:
                     hint="Put a mandatory Comma after: "+ b[i-1]
                     mandlst.append(hint)      
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.location:
                    
                    hint="Put a mandatory Comma after: "+b[i-1]
                    mandlst.append(hint)  
                if b[i-1] in type12crules.location and b[i+1] in type12crules.city:
                    hint="Put a mandatory Comma after: "+ b[i-1]
                    mandlst.append(hint)
                if b[i-1] in type12crules.city and b[i+1] in type12crules.statel:
                     hint="Put a mandatory Comma after: "+ b[i-1]
                     mandlst.append(hint)    
                if b[i-1] in type12crules.statel and b[i+1]in type12crules.pincode:
                     print("statel",type12crules.statel)
                     hint="Put a mandatory Comma after: "+ b[i-1]
                     mandlst.append(hint)
                
                if b[i-1] in type12crules.onamelst and b[i+1]=="The":
                     hint="Put a mandatory Fullstop after: "+ b[i-1]
                     mandlst.append(hint)
                if b[i-1]=="Pvt" and b[i+1]=="Ltd":
                     hint="Put a mandatory Fullstop after: "+ b[i-1]
                     mandlst.append(hint)
                if b[i-1]=="Ltd" or b[i-1]=="Late":
                     hint="Put a mandatory Fullstop after: "+ b[i-1]
                     mandlst.append(hint)
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.flatno:
                    hint="Put a Mandatory COmma after: "+ b[i-1]
                    mandlst.append(hint)    
                if b[i-1] in type12crules.flatno and b[i+1] in type12crules.wing:
                     hint="Put a mandatory Comma after: "+ b[i-1]
                     mandlst.append(hint)
                
                  
                if b[i-1] in type12crules.title and b[i+1] in type12crules.snoun:
                     hint="Put a mandatory Fullstop after: "+ b[i-1]
                     mandlst.append(hint)
               
               
                if b[i-1]=="Opp":
                    hint="Put a mandatory Fullstop after: "+ b[i-1]
                    mandlst.append(hint) 
                if b[i-1] in type12crules.onoun and b[i+1]=="The":
                     hint="Put a mandatory Fullstop after: "+ b[i-1]
                     mandlst.append(hint)    
                if b[i-1] =="Ltd." and b[i+1]==" ":
                     hint="Put a mandatory Fullstop after: "+ b[i-1]
                     mandlst.append(hint)   
                if b[i-1] in type12crules.location and b[i+1]=="The":
                     hint="Put a mandatory Fullstop after: "+ b[i-1]
                     mandlst.append(hint)    
                if b[i-1] =="Ltd." and b[i+1]=="The":
                     hint="Put a mandatory Fullstop after: "+ b[i-1]
                     mandlst.append(hint)          
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.city:
                    
                    hint="Put a mandatory Comma after: "+b[i-1]
                    mandlst.append(hint)
                if b[i-1] in type12crules.new_landmark and b[i+1] in type12crules.roadl:
                     hint="Put a mandatory Comma after: "+ b[i-1]
                     mandlst.append(hint)
                if b[i-1] in type12crules.flatno and b[i+1] in type12crules.new_landmark:
                     hint="Put a mandatory Comma after: "+ b[i-1]
                     mandlst.append(hint)
                if b[i-1] in type12crules.buildingl and b[i+1] in type12crules.flatno:
                     hint="Put a mandatory Comma after: "+ b[i-1]
                     mandlst.append(hint)
                if b[i-1] in type12crules.pincode:
                     hint="Put a mandatory Fullstop after: "+ b[i-1]
                     mandlst.append(hint)
                     
        return(hintlst,mandlst,correctlst,mandatory)
    def commaone(b,c,correct,category,level,username,userid,eid,submittedtext):
    #def commaone(self):   
        mandlst=[]
        correctlst=[]
        hintlst=[]
##        b=['John', '<w>', 'works', '<w>', 'in', '<w>', 'an', '<w>', 'organisation', '<m>', 'The', '<w>', 'name', '<w>', 'of', '<w>', 'the', '<w>', 'organisation', '<w>', 'is', '<w>', 'B', '<w>', 'M', '<w>', 'C', '<w>', 'Software', '<m>', 'The', '<w>', 'address', '<w>', 'is', '<w>', 'Santacruz', '<m>', 'Mumbai', '<m>', 'Maharashtra', '<m>', '400098', '<m>']
##        c=['John', ' ', 'works', ' ', 'in', ' ', 'an', ' ', 'organisation', ' ', 'The', ' ', 'name', ' ', 'of', ' ', 'the', ' ', 'organisation', ' ', 'is', ' ', 'B', ' ', 'M', ' ', 'C', ' ', 'Software', ' ', 'The', ' ', 'address', ' ', 'is', ' ', 'Santacruz', ' ', 'Mumbai', ' ', 'Maharashtra', ' ', '400098', ' ']
##        b=['John', '<w>', 'stays', '<w>', 'in', '<w>', 'a', '<w>', 'house', '<m>', 'His', '<w>', 'address', '<w>', 'is', '<w>', 'C/O', '<w>', 'Late', '<m>', 'Mr', '<m>', 'Esmail', '<w>', 'Bagani', '<m>', 'Y/2/122', '<m>', 'B-Wing', '<m>', 'Sarayu', '<w>', 'Society', '<m>', 'Satghara', '<w>', 'Road', '<m>', 'Badartala', '<m>', 'Kolkata', '<m>', 'West', '<w>', 'Bengal', '<m>', '700044', '<m>']
##        c=['John', ' ', 'stays', ' ', 'in', ' ', 'a', ' ', 'house', '.', 'His', ' ', 'address', ' ', 'is', ' ', 'C/O', ' ', 'Late', '.', 'Mr', '.', 'Esmail', ' ', 'Bagani', ',', 'Y/2/122', ' ', 'B-Wing', ' ', 'Sarayu', ' ', 'Society', ' ', 'Satghara', ' ', 'Road', ' ', 'Badartala', ',', 'Kolkata', ' ', 'West', ' ', 'Bengal', ' ', '700044', '.']

        ##print(tagged)
##        b=['Alice', '<w>', 'joins', '<w>', 'an', '<w>', 'organisation.The', '<w>', 'name', '<w>', 'of', '<w>', 'the', '<w>', 'organisation', '<w>', 'is', '<w>', 'Life', '<w>', 'Style', '<w>', 'International', '<w>', 'Pvt', '<m>', 'Ltd', '<m>','<m>','The', '<w>', 'address', '<w>', 'Mumbai', '<m>', 'Maharashtra', '<m>', '400098', '<m>']
##        c=['Alice', ' ', 'joins', ' ', 'an', ' ', 'organisation.The', ' ', 'name', ' ', 'of', ' ', 'the', ' ', 'organisation', ' ', 'is', ' ', 'Life', ' ', 'Style', ' ', 'International', ' ', 'Pvt', '.', 'Ltd', ',', ' ', 'The', ',', 'address', ',', 'Mumbai', ',', 'Maharashtra', '.', '400098', '.']
##
##        b=['John', '<w>', 'works', '<w>', 'in', '<w>', 'an', '<w>', 'organisation.The', '<w>', 'name', '<w>', 'of', '<w>', 'the', '<w>', 'organisation', '<w>', 'is', '<w>', 'B', '<w>', 'M', '<w>', 'C', '<w>', 'Software', '<m>', 'The', '<w>', 'address', '<w>', 'Mumbai', '<m>', 'Maharashtra', '<m>', '400098', '<m>']
##        c=['John', ' ', 'works', ' ', 'in', ' ', 'an', ' ', 'organisation.The', ' ', 'name', ' ', 'of', ' ', 'the', ' ', 'organisation', ' ', 'is', ' ', 'B', '.', 'M', '.', 'C', '.', 'Software', '.', 'The', '<w>', 'address', ',', 'Mumbai', ',', 'Maharashtra', ',', '400098', '.']
##        b=['Mary', '<w>', 'stays', '<w>', 'in', '<w>', 'a', '<w>', 'house', '<m>', 'Her', '<w>', 'address', '<w>', 'is', '<w>', 'C/O', '<w>', 'Late', '<m>', 'Mr', '<m>', 'E', '<m>', 'Bagani', '<m>', 'Y/2/122', '<m>', 'B-Wing', '<m>', 'Sarayu', '<w>', 'Society', '<m>', 'Satghara', '<w>', 'Road', '<m>', 'Badartala', '<m>', 'Kolkata', '<m>', 'Bengal', '<m>', '700044', '<m>']
##        c=['Mary', ' ', 'stays', ';', 'in', ';', 'a', ' ', 'house', '.', 'Her', ' ', 'address', ',', 'is', ' ', 'C/O', ' ', 'Late', ' ', 'Mr', ' ', 'E', '.', 'Bagani', ' ', 'Y/2/122', ' ', 'B-Wing', ' ', 'Sarayu', ' ', 'Society', ' ', 'Satghara', ' ', 'Road', ' ', 'Badartala', ' ', 'Kolkata', ' ', 'Bengal', ' ', '700044', '.']
        single=[]        
        for i in c:
            if len(i)==1:
                if i>="A" and i<="Z":
                    single.append(i)
        b.append(" ")
        c.append(" ")
        ct=0
        for i in b:
            if i=="<m>":
                ct=ct+1
        mandatory=ct
        print(ct)
        mandlst=[]
        correctlst=[]
        hintlst=[]
        print(b)
        print(c)
          
    #---------------------------------------------------<m> with semicolon-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==";"):
                if b[i-1] in single and b[i+1] in type12crules.snoun:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                
                if b[i-1] in type12crules.flatno and b[i+1] in type12crules.wing:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in type12crules.onoun) and (b[i+1] in type12crules.pronoun1):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in type12crules.pincode) and c[i]==" " and (c[i+1]==" "):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if b[i-1] in type12crules.wing and b[i+1] in type12crules.societyl:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if b[i-1] in type12crules.societyl and b[i+1] in type12crules.roadl:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)      
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.location:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if b[i-1] in type12crules.location and b[i+1] in type12crules.city:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if b[i-1] in type12crules.city and b[i+1] in type12crules.statel:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)    
                if b[i-1] in type12crules.statel and b[i+1] in type12crules.pincode:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.flatno:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)    
                if b[i-1]=="Pvt" and b[i+1]=="Ltd":
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint) 
                if b[i-1]=="Late" and b[i+1]==";":
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if b[i-1] in type12crules.title and b[i+1] in type12crules.snoun:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)     
                if b[i-1]=="Ltd":
                   hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                   mandlst.append(hint) 
                if b[i-1]=="Opp":
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)      
             
    #---------------------------------------------------<m> with comma-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):
                if b[i-1] in single and b[i+1] in type12crules.snoun:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint) 
                if b[i-1] in type12crules.flatno and b[i+1] in type12crules.wing:
                    hint="Correct Answer,Seperate two entities using a comma"
                    correctlst.append(hint) 
                
                if (b[i-1] in type12crules.onoun) and (b[i+1] in type12crules.pronoun1):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in type12crules.pincode) and c[i]==" " and (c[i+1]==" "):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if b[i-1] in type12crules.wing and b[i+1] in type12crules.societyl:
                    hint="Correct Answer,Seperate two entities using a comma"
                    correctlst.append(hint)
                if b[i-1] in type12crules.societyl and b[i+1] in type12crules.roadl:
                    hint="Correct Answer,Seperate two entities using a comma"
                    correctlst.append(hint)     
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.location:
                    hint="Correct Answer,Seperate two entities using a comma"
                    correctlst.append(hint)
                if b[i-1] in type12crules.location and b[i+1] in type12crules.city:
                    hint="Correct Answer,Seperate two entities using a comma"
                    correctlst.append(hint)
                if b[i-1] in type12crules.city and b[i+1] in type12crules.statel:
                    hint="Correct Answer,Seperate two entities using a comma"
                    correctlst.append(hint)    
                if b[i-1] in type12crules.statel and b[i+1] in type12crules.pincode:
                    hint="Correct Answer,Seperate two entities using a comma"
                    correctlst.append(hint)
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.flatno:
                    hint="Correct Answer,Seperate two entities using a comma"
                    correctlst.append(hint)   
                if b[i-1]=="Pvt" and b[i+1]=="Ltd":
                    hint="Correct Answer,Seperate two entities using a comma"
                    correctlst.append(hint)
                if b[i-1]=="Late" and b[i+1]==",":
                    hint="Correct Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if b[i-1] in type12crules.title and b[i+1] in type12crules.snoun:
                    hint="Correct Answer,When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    correctlst.append(hint)
                        
                if b[i-1]=="Ltd":
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint) 
                if b[i-1]=="Opp":
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)    
    #---------------------------------------------------<m> with Fullstop--------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                if b[i-1] in single and b[i+1] in type12crules.snoun:
                    hint="Correct Answer,Fullstop has to be used after the initials of the name"
                    mandlst.append(hint)
                if b[i-1] in type12crules.flatno and b[i+1] in type12crules.wing:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint) 
                if (b[i-1] in type12crules.onoun) and (b[i+1] in type12crules.pronoun1):    
                    hint="Correct Ans, Fullstop has to be used to seperate two statements"
                    correctlst.append(hint)
                if (b[i-1] in type12crules.pincode) and c[i]=="." and (c[i+1]==" "):    
                    hint="Correct Ans, Always end  a sentence with Fullstop"
                    correctlst.append(hint)
                if b[i-1] in type12crules.wing and b[i+1] in type12crules.societyl:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if b[i-1] in type12crules.societyl and b[i+1] in type12crules.roadl:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)      
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.location:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if b[i-1] in type12crules.location and b[i+1] in type12crules.city:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if b[i-1] in type12crules.city and b[i+1] in type12crules.statel:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)    
                if b[i-1] in type12crules.statel and b[i+1] in type12crules.pincode:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.flatno:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)    
                if b[i-1]=="Pvt" and b[i+1]=="Ltd":
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint) 
                if b[i-1]=="Late" and b[i+1]==".":
                    hint="Correct Answer,When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    correctlst.append(hint)
                if b[i-1] in type12crules.title and b[i+1] in type12crules.snoun:
                    hint="Correct Answer,When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    correctlst.append(hint)  
                if b[i-1]=="Ltd":
                    hint="Correct Answer,When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    correctlst.append(hint)
                if b[i-1]=="Opp":
                    hint="Correct Answer,When a word is abbreviated after the first few letters, the traditional rule is to put a full stop after the abbreviation"
                    correctlst.append(hint)    
#---------------------------------------------------------<m> with no punctuation---------------------------------------------------------------
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==" "):
                if b[i-1] in single and b[i+1] in type12crules.snoun:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if b[i-1] in type12crules.flatno and b[i+1] in type12crules.wing:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint) 
                if (b[i-1] in type12crules.onoun) and (b[i+1] in type12crules.pronoun1):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if (b[i-1] in type12crules.pincode) and c[i]==" " and (c[i+1]==" "):    
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if b[i-1] in type12crules.wing and b[i+1] in type12crules.societyl:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if b[i-1] in type12crules.societyl and b[i+1] in type12crules.roadl:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)      
                if b[i-1] in type12crules.roadl and b[i+1] in type12crules.location:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if b[i-1] in type12crules.location and b[i+1] in type12crules.city:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if b[i-1] in type12crules.city and b[i+1] in type12crules.statel:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)    
                if b[i-1] in type12crules.statel and b[i+1] in type12crules.pincode:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if b[i-1] in type12crules.snoun and b[i+1] in type12crules.flatno:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)    
                if b[i-1]=="Pvt" and b[i+1]=="Ltd":
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint) 
                if b[i-1]=="Late" and b[i+1]==" ":
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                if b[i-1] in type12crules.title and b[i+1] in type12crules.snoun:
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)     
                if b[i-1]=="Ltd":
                   hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                   mandlst.append(hint) 
                if b[i-1]=="Opp":
                    hint="InCorrect Answer,Click the appropriate sidepane and read the manuals"
                    mandlst.append(hint)
                
                

                    
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
                
                hint="SEMICOLON at incorrect locations.Click the appropriate sidepane and read the manuals"
                hintlst.append(hint)
##        print(hintlst,mandlst,correctlst,mandatory)        
        return(hintlst,mandlst,correctlst,mandatory)                                                        
##p1=type12crules()
##hintlst,mandlst,correctlst,mandatory=p1.commaone()
##
##for i in hintlst:
##    print(i)
##for j in mandlst:
##    print(j)
##for k in correctlst:
##    print(k)
##
##                             
                        
