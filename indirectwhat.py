import xml.etree.ElementTree as ET
from indirect2 import indirect2 as i1
from indirectq import indirectq as p1
import re
import random
##tree1=ET.parse('D:\\evakya\\xml\\indirectwhat1.xml')
##root=tree1.getroot()
class indirectwhat:#---cookable
    tree1=ET.parse('D:\\evakya\\xml\\indirectwhat1.xml')
    root=tree1.getroot()
    def genverb(self):
        verblst=[]
        for i in indirectwhat.root:
            if i.tag=="PRESENTVERB":
                vclass=i.attrib['VCLASS']
                ##print("indirectq.vclass",indirectq.vclass)
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        ##print(dh)
                        if vclass==dh[0]:
                            verblst.append(dh[1])
                    verb=random.choice(verblst)
                    ##print("indirectq.verb",indirectq.verb)

                with open("D:\\evakya\\dataset\\tense.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        ##print(dh)
                        if verb==dh[1]:
                            presentverb=dh[0]                    
        ##print("preverb",presentverb)
        return(presentverb)
                    
    def genqtag(self):
        for i in indirectwhat.root:
            if i.tag=="QTAG":
                qtag=i.attrib['TYPE']
                ##print(qtag)
        return(qtag)
    def gensent(self):
       
        itag=i1.genindirecttag(self)
        qtag=p2.genqtag()
        snoun=p1.gensnoun(self)
        verb=p2.genverb()
        print("itag",verb)
        qmark="?"
    
        sent1=itag+" "+qtag+" "+snoun+" "+verb+"s"+qmark
    
        
        from indirect2 import indirect4 as f1
        sent2=f1.gensent(self)
        #print(sent2)
        from indirect2 import indirect3 as f2
        sent3=f2.gensent(self)
        #print(sent3)
        
                
        #--------------------unpunctuate-----------------------------------------------------------------
        punctuations = '''!()[]{};:."\,<>/?@#$%^&*_~'''
        nopunct=""
        for char in sent1:
            if char not in punctuations:
                nopunct = nopunct + char
        mylist1=nopunct.split(" ")
        #print(mylist1)
        taglst=[]
        qtag=['Do','Can','Could']
        wtag=['what','where','why']
        snoun=['Mary','James','John','Alice','A. Roy', 'K. Singh', 'R. K. Narayan', 'R. Kushner','Esmail','Bagani' ]
        verbs=['cooks','stays']
        #Do you know what Alice cooks?
        for i, element in enumerate(mylist1):
            previous_element = mylist1[i-1] if i > 0 else None
            current_element = element
            next_element = mylist1[i+1] if i < len(mylist1)-1 else None
            #print(previous_element, current_element, next_element)
            if current_element in qtag and next_element=="you":
                    taglst.append(current_element)
                    taglst.append("<w>")
            if current_element=="you" and next_element=="know":
                    taglst.append(current_element)
                    taglst.append("<w>")
                    taggedsent="".join(taglst)
            if current_element=="know" and next_element in wtag:
                    taglst.append(current_element)
                    taglst.append("<w>")
                    taggedsent="".join(taglst)
            if current_element in wtag and next_element in snoun:
                    taglst.append(current_element)
                    taglst.append("<w>")
                    taggedsent="".join(taglst)
            if current_element in snoun and next_element in verbs:
                    taglst.append(current_element)
                    taglst.append("<w>")
                    taggedsent="".join(taglst)
            if current_element in verbs and next_element==None:
                    taglst.append(current_element)
                    taglst.append("<m>")#----------------fullstop
                    taggedsent="".join(taglst)         
        print(sent1)
        taggedsent="".join(taglst)
        print("nopunct",nopunct)
        #------------------sent2 unpunctuate---I'd like to know where Alice stays?------------------------
        nopunct2=""
        taglst1=[]
        current_element=""
        next_element=""
        previous_element=""
        for char in sent2:
            if char not in punctuations:
                nopunct2 = nopunct2 + char
             
        mylist2=nopunct2.split(" ")
        #print(mylist2)
        for i, element in enumerate(mylist2):
            previous_element = mylist2[i-1] if i > 0 else None
            current_element = element
            next_element = mylist2[i+1] if i < len(mylist2)-1 else None
            #print(previous_element, current_element, next_element)
            
            if current_element=="I'd" and next_element=="like":
                    taglst1.append(current_element)
                    taglst1.append("<w>")
                   
            if current_element=="like" and next_element=="to":
                    taglst1.append(current_element)
                    taglst1.append("<w>")
                    
            if current_element=="to" and next_element=="know":
                    taglst1.append(current_element)
                    taglst1.append("<w>")
                    
            if current_element=="know" and next_element in wtag:
                    taglst1.append(current_element)
                    taglst1.append("<w>")
                    
            if current_element in wtag and next_element in snoun:
                    taglst1.append(current_element)
                    taglst1.append("<w>")
            print("verbs",verbs)       
            if current_element in snoun and next_element in verbs:
                    taglst1.append(current_element)
                    taglst1.append("<w>")
                         
            if current_element in verbs and next_element==None:
                    taglst1.append(current_element)
                    taglst1.append("<m>")#----------------fullstop
        print(sent2)
        taggedsent2="".join(taglst1)         
        
        print("sent2tagged",taggedsent2)
         #------------------sent3 unpunctuate-----Do you have any idea where James stays?----------------------
        nopunct3=""
        for char in sent3:
            if char not in punctuations:
                nopunct3 = nopunct3 + char
             
        mylist3=nopunct3.split(" ")
        #print(mylist3)

        
        taglst3=[]
        current_element=""
        next_element=""
        previous_element=""
        for i, element in enumerate(mylist3):
            previous_element = mylist3[i-1] if i > 0 else None
            current_element = element
            next_element = mylist3[i+1] if i < len(mylist3)-1 else None
            #print(previous_element, current_element, next_element)
           
            if current_element=="Do" and next_element=="you":
                    taglst3.append(current_element)
                    taglst3.append("<w>")
                   
            if current_element=="you" and next_element=="have":
                    taglst3.append(current_element)
                    taglst3.append("<w>")
                    
            if current_element=="have" and next_element=="any":
                    taglst3.append(current_element)
                    taglst3.append("<w>")
                    
            if current_element=="any" and next_element=="idea":
                    taglst3.append(current_element)
                    taglst3.append("<w>")
                    
            if current_element=="idea" and next_element in wtag:
                    taglst3.append(current_element)
                    taglst3.append("<w>")
                   
            if current_element in wtag and next_element in snoun:
                    taglst3.append(current_element)
                    taglst3.append("<w>")
            if current_element in snoun and next_element in verbs:
                    taglst3.append(current_element)
                    taglst3.append("<w>")             
            if current_element in verbs and next_element==None:
                    taglst3.append(current_element)
                    taglst3.append("<m>")#----------------fullstop
        print(sent3)
        taggedsent3="".join(taglst3)         
        
        print("sent3tagged",taggedsent3)
       
     #------------------sent4 unpunctuate-----------Do you know where Alice stays?----------------
        from indirect2 import indirect2 as f3
        sent4=f3.gensent(self)
        print("sent4",sent4)
        from indirectq import indirectq as f4
        sent5=f4.gensent(self)
        print("sent5",sent5)
        nopunct4=""
        punctuations="?"
        for char in sent4:
            if char not in punctuations:
                nopunct4 = nopunct4 + char
             
        mylist4=nopunct4.split(" ")
        ##print(mylist4)
       
        taglst4=[]
        current_element=""
        next_element=""
        previous_element=""
        for i, element in enumerate(mylist4):
            previous_element = mylist4[i-1] if i > 0 else None
            current_element = element
            next_element = mylist4[i+1] if i < len(mylist4)-1 else None
            ##print(previous_element, current_element, next_element)
           
            if current_element=="Do" and next_element=="you":
                    taglst4.append(current_element)
                    taglst4.append("<w>")
                   
            if current_element=="you" and next_element=="know":
                    taglst4.append(current_element)
                    taglst4.append("<w>")
                    
          
                    
            if current_element=="know" and next_element in wtag:
                    taglst4.append(current_element)
                    taglst4.append("<w>")
                   
            if current_element in wtag and next_element in snoun:
                    taglst4.append(current_element)
                    taglst4.append("<w>")
            if current_element in snoun and next_element in verbs:
                    taglst4.append(current_element)
                    taglst4.append("<w>")             
            if current_element in verbs and next_element==None:
                    taglst4.append(current_element)
                    taglst4.append("<m>")#----------------fullstop
        print("sent4",sent4)
        taggedsent4="".join(taglst4)
        
        
        print("sent4tagged",taggedsent4)
       
     #------------------sent5 unpunctuate---------------Could you tell me where Mary stays?------------
        nopunct5=""
        for char in sent5:
            if char not in punctuations:
                nopunct5 = nopunct5 + char
             
        mylist5=nopunct5.split(" ")
        #print(mylist5)
        
        taglst5=[]
        current_element=""
        next_element=""
        previous_element=""
        for i, element in enumerate(mylist5):
            previous_element = mylist5[i-1] if i > 0 else None
            current_element = element
            next_element = mylist5[i+1] if i < len(mylist5)-1 else None
            #print(previous_element, current_element, next_element)
           
            if current_element in qtag and next_element=="you":
                    taglst5.append(current_element)
                    taglst5.append("<w>")
                   
            if current_element=="you" and next_element=="tell":
                    taglst5.append(current_element)
                    taglst5.append("<w>")
                    
            if current_element=="tell" and next_element=="me":
                    taglst5.append(current_element)
                    taglst5.append("<w>")
                    
            if current_element=="me" and next_element in wtag:
                    taglst5.append(current_element)
                    taglst5.append("<w>")
           
                   
            if current_element in wtag and next_element in snoun:
                    taglst5.append(current_element)
                    taglst5.append("<w>")
            if current_element in snoun and next_element in verbs:
                    taglst5.append(current_element)
                    taglst5.append("<w>")             
            if current_element in verbs and next_element==None:
                    taglst5.append(current_element)
                    taglst5.append("<m>")#----------------fullstop
        print("sent5",sent5)
        taggedsent5="".join(taglst5)
        print("tag5",taggedsent5)
        return(sent1,nopunct,taggedsent,sent2,nopunct2,taggedsent2,sent3,nopunct3,taggedsent3,sent4,nopunct4,taggedsent4,sent5,nopunct5,taggedsent5)
p2=indirectwhat()
sent1,nopunct,taggedsent,sent2,nopunct2,taggedsent2,sent3,nopunct3,taggedsent3,sent4,nopunct4,taggedsent4,sent5,nopunct5,taggedsent5=p2.gensent()
print("nopunct")
category="questionmark"
level=1
import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="rohith@123",
        database="pythonlogin"
)
mycursor = mydb.cursor()

mycursor.execute("select max(exerciseid) from sentencedb")  
rows = mycursor.fetchall()
for row in rows:
        id1=0
        id1=row[0]
        #####print("id1:",row[0])
id2=id1+1
        

-----------------------------insert into database------------------------------------------------------------------------------------------------------------------   

mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent1,taggedsent,category,level,1))
mydb.commit()
id2=0
mycursor.execute("select max(exerciseid) from sentencedb")  
rows = mycursor.fetchall()
for row in rows:
        id1=0
        id1=row[0]
        #####print("id1:",row[0])
id2=id1+1
mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct2,sent2,taggedsent2,category,level,1))
mydb.commit()
id2=0
mycursor.execute("select max(exerciseid) from sentencedb")  
rows = mycursor.fetchall()
for row in rows:
        id1=0
        id1=row[0]
        #####print("id1:",row[0])
id2=id1+1
mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct3,sent3,taggedsent3,category,level,1))
mydb.commit()
id2=0
mycursor.execute("select max(exerciseid) from sentencedb")  
rows = mycursor.fetchall()
for row in rows:
        id1=0
        id1=row[0]
        #####print("id1:",row[0])
id2=id1+1
mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct4,sent4,taggedsent4,category,level,1))
mydb.commit()
id2=0
mycursor.execute("select max(exerciseid) from sentencedb")  
rows = mycursor.fetchall()
for row in rows:
        id1=0
        id1=row[0]
        #####print("id1:",row[0])
id2=id1+1
level=1
mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct5,sent5,taggedsent5,category,level,1))
mydb.commit() 
print("sent5tagged",taggedsent5)

       



