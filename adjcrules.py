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
class adjcrules:
    snoun=['Mary','James','John','Alice','A. Roy', 'K. Singh', 'R. K. Narayan', 'R. Kushner','Esmail','Bagani' ]
    verb=['said','lift','stand','answered','won','got','secured','achieved','hurt','lost','opened','closed','cooked','met','read','wrote','drew','drank','paid','bought','stayed','worked','joined','taught','married','dated','intracted','consulted','visited','debated','argued','fought','lived','seperated']
    verb1=[]
    verbs=['lift','stand','answer','win','get','secure','achieve','hurt','lose','open','close','cook','meet','read','write','draw','drink','pay','buy','stay','work','join','teach','married','date','intract','consult','visit','debate','argue','fight','live','seperate']
    onoun=['box','book','cage','scenary','house','building','tea','water','coffee','biriyani','pulav','kichdi','novel','story','match','race','ankle','leg','first-prize','second-prize','job','position','keys','books','poem','story','furniture','vegetables','fruits','bicycles','bicycle','house','organisation','school','college','flat','question']
    prep=['in','for','with','from','on','to']
    vbz=['is','has','was']
    pronoun=['his','her','he','she','it']
    pronoun1=[]
    pronounq=[]
    onounq=[]
    adj=['confident','adorable','generous','charming','clever','huge','red','small','heavy','beautiful','fantastic','mesmerising','well-defined','hot','cold','warm','strong-flavored','delicious','tasty','mind-blowing','spicy','excellent','lovely','thrilled','elated','difficult','intelligent','rapid-fire','open-ended','lovely','fascinating','short','precise','interesting','selective','magnificent','high-grade','exceptional','focused','ambitious','demanding','competetive','exciting','brilliant','amazing','three-room','luxurious','spacious','own','modern','adorable','favorite','new','worthy','valuable','expensive','precious','limpy','twisted','sprained','fractured','considerate','attractive','amusing','jovial']
    det="the"
    detcap=det.capitalize()
    for i in pronoun:
        pronoun1.append(i.capitalize())
    for i in pronoun1:
        pronounq.append('"'+i)
    for i in onoun:
        onounq.append(i+'"')


    def commatwo(self):
        mandlst=[]
        correctlst=[]
        hintlst=[]
        adjlst=[]

        b=['The', '<w>', 'story', '<w>', 'Alice', '<w>', 'read', '<w>', 'is', '<w>', 'short', '<m>', 'interesting', '<m>', 'selective', '<w>', 'and', '<w>', 'fascinating', '<m>',' ']
        c=['The', ';', 'story', ';', 'Alice', ';', 'read', ',' ,'is', ';', 'short', ';', 'interesting', ',', 'selective', ',', 'and', ',', 'fascinating', '.',' ']  
        print(b)
        print(c)
        
            
    #---------------------------------------------------<m> with semicolon-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==";"):
                #print("adj",adjcrules.adj)
                 
            #--------------------------------------------adjcommafinal.py-----------------------------------------------------------------
                if b[i-1] in adjcrules.adj and b[i+1] in adjcrules.adj:
                    hint="Read the manual again, HINT:No need of a semicolon,but a comma should be used in between the adjectives"
                    mandlst.append(hint)
                if b[i]=="<m>" and c[i+1]==" ":
                    hint="Read the manual again, HINT:Always end a sentence with a FULLSTOP"
                    mandlst.append(hint)

            #---------------------------------------------------<m> with comma-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):
            #-------------------------------------------adjcommafinal.py-----------------------------------------------------------------
                if b[i-1] in adjcrules.adj and b[i+1] in adjcrules.adj:
                    hint="Correct Answer:A comma should be used in between the adjectives"
                    correctlst.append(hint)
                if b[i] == "<m>" and c[i+1]==",":
                    hint="Read the manual again, HINT:Always end a sentence with a FULLSTOP"
                    mandlst.append(hint)  
                  
          #---------------------------------------------------<m> with fullstop-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                #-------------------------------------------adjcommafinal.py-----------------------------------------------------------------
                if b[i-1] in adjcrules.adj and b[i+1] in adjcrules.adj:
                    hint="Read the manual again, HINT:No need of a fullstop,but a comma should be used in between the adjectives"
                    mandlst.append(hint)
                if b[i-1] in adjcrules.adj and c[i+1]==".":
                    hint="Correct Answer:Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)    
        return(mandlst,correctlst)

p1=adjcrules()
mandlst,correctlst=p1.commatwo()


for j in mandlst:
    print(j)
for k in correctlst:
    print(k)

                     
