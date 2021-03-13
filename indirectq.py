import xml.etree.ElementTree as ET
import random
import re
class indirectq:
        
    snname=""
    adj1=""
    noundict=[]
    tree = ET.parse('D:\\evakya\\xml\\indirectstay.xml')
    #tree = ET.parse('D:\\evakya\\indirectwork.xml')
    root=tree.getroot()
    vclass=""

    def genqtag(self):
        for i in indirectq.root:
            if i.tag=="QTAG":
                qtag=i.attrib['TYPE']
                print(qtag)
        return(qtag)

    def genindirecttag(self):
        for i in indirectq.root:
            if i.tag=="INDIRECTTAG":
                hverb=i.attrib['HVERB']
                tpro=i.attrib['TPRO']
                iverb=i.attrib['VERB']
                fpro=i.attrib['FPRO']
        itag=hverb+" "+tpro+" "+iverb+" "+fpro                     
        #print(itag)
        return(itag)

    def gensnoun(self):
        for i in indirectq.root:
            if i.tag=="SNOUN":
                if i.attrib['TYPE']=="personified":
                

                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                indirectq.noundict.append(dh[1])

                                #print(type5.noundict)
                    indirectq.snname=random.choice(indirectq.noundict)
                    
        #print(indirectq.snname)
        return(indirectq.snname)
        
    def genverb(self):
        verblst=[]
        for i in indirectq.root:
            if i.tag=="PRESENTVERB":
                indirectq.vclass=i.attrib['VCLASS']
                #print("indirectq.vclass",indirectq.vclass)
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if indirectq.vclass==dh[0]:
                            verblst.append(dh[1])
                    indirectq.verb=random.choice(verblst)
                    #print("indirectq.verb",indirectq.verb)

                with open("D:\\evakya\\dataset\\tense.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        #print(dh)
                        if indirectq.verb==dh[1]:
                            presentverb=dh[0]

                    
        #print("preverb",presentverb)
        return(presentverb)
    
    def gensent(self):
##        qmark="?"
##        itag=p1.genindirecttag()
##        qtag=p1.genqtag()
##        snoun=p1.gensnoun()
##        verb=p1.genverb()
##        sent=itag+" "+qtag+" "+snoun+" "+verb+"s"+qmark
##        taggedsent=itag+"<w>"+qtag+" "+snoun+" "+verb+"s"+qmark
##        nopunct=itag+" "+qtag+" "+snoun+" "+verb+"s"
        #---------------------------------------------------------------------------------------------0 --
        sent2="I’d"+" "+"like"+" "+"to"+" "+"know"+" "+"where"+" "+"James"+" "+"work"+"?"
        nopunct2="I’d"+" "+"like"+" "+"to"+" "+"know"+" "+"where"+" "+"James"+" "+"work"
        taggedsent2="I’d"+"<w>"+"like"+"<w>"+"to"+"<w>"+"know"+"<w>"+"where"+"<w>"+"James"+"<w>"+"work"+"<m>"
        import mysql.connector
        #----------------------------------------------------------------------------------------
        sent3="Do"+" "+"you"+" "+"have"+" "+"any"+" "+"idea"+" "+"what"+" "+"James"+" "+"cooks"+"?"
        nopunct3="Do"+" "+"you"+" "+"have"+" "+"any"+" "+"idea"+" "+"what"+" "+"James"+" "+"cooks"
        taggedsent3="Do"+"<w>"+"you"+"<w>"+"have"+"<w>"+"any"+"<w>"+"idea"+"<w>"+"what"+"<w>"+"James"+"<w>"+"cooks"+"<m>"
        #-----------------------------------------------------------------------------------------
        sent4="Do"+" "+"you"+" "+"know"+" "+"what"+" "+"Mary"+" "+"reads"+"?"
        nopunct4="Do"+" "+"you"+" "+"know"+" "+"what"+" "+"Mary"+" "+"reads"
        taggedsent4="Do"+"<w>"+"you"+"<w>"+"know"+"<w>"+"what"+"<w>"+"Mary"+"<w>"+"reads"+"<m>"
        #------------------------------------------------------------------------------------------
        sent5="Can"+" "+"you"+" "+"tell"+" "+"me"+" "+"where"+" "+"James"+" "+"works"+"?"
        nopunct5="Can"+" "+"you"+" "+"tell"+" "+"me"+" "+"where"+" "+"James"+" "+"works"
        taggedsent5="Can"+"<w>"+"you"+"<w>"+"tell"+"<w>"+"me"+"<w>"+"where"+"<w>"+"James"+"<w>"+"works"+"<m>"
        #------------------------------------------------------------------------------------------------
        sent6="Could"+" "+"you"+" "+"tell"+" "+"me"+" "+"where"+" "+"James"+" "+"works"+"?"
        nopunct6="Could"+" "+"you"+" "+"tell"+" "+"me"+" "+"where"+" "+"James"+" "+"works"
        taggedsent6="Could"+"<w>"+"you"+"<w>"+"tell"+"<w>"+"me"+"<w>"+"where"+"<w>"+"James"+"<w>"+"works"+"<m>"
        level=2
        category="questionmark"
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="rohith@123",
                database="pythonlogin"
        )
        mycursor = mydb.cursor()
        level=2
##        mycursor.execute("select max(exerciseid) from sentencedb")  
##        rows = mycursor.fetchall()
##        for row in rows:
##                id1=0
##                id1=row[0]
##                #####print("id1:",row[0])
##        id2=id1+1
##        
##        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))
##        mydb.commit() 
        mycursor.execute("select max(exerciseid) from sentencedb")  
        rows = mycursor.fetchall()
        for row in rows:
                id1=0
                id1=row[0]
                #####print("id1:",row[0])
        id2=id1+1
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct2,sent2,taggedsent2,category,level,1))
        mydb.commit()  
        mycursor.execute("select max(exerciseid) from sentencedb")  
        rows = mycursor.fetchall()
        for row in rows:
                id1=0
                id1=row[0]
                #####print("id1:",row[0])
        id2=id1+1
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct3,sent3,taggedsent3,category,level,1))
        mydb.commit() 
        mycursor.execute("select max(exerciseid) from sentencedb")  
        rows = mycursor.fetchall()
        for row in rows:
                id1=0
                id1=row[0]
                #####print("id1:",row[0])
        id2=id1+1
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct4,sent4,taggedsent4,category,level,1))

        mycursor.execute("select max(exerciseid) from sentencedb")  
        rows = mycursor.fetchall()
        for row in rows:
                id1=0
                id1=row[0]
                #####print("id1:",row[0])
        id2=id1+1
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct5,sent5,taggedsent5,category,level,1))

        mydb.commit() 
        mycursor.execute("select max(exerciseid) from sentencedb")  
        rows = mycursor.fetchall()
        for row in rows:
                id1=0
                id1=row[0]
                #####print("id1:",row[0])
        id2=id1+1
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct6,sent6,taggedsent6,category,level,1))

        mydb.commit()
        
   
p1=indirectq()
p1.gensent()
