import xml.etree.ElementTree as ET
from indirectq import indirectq as p1
import re
import random
class indirect2:
    
    tree1=ET.parse('D:\\evakya\\xml\\indirect2work.xml')

    root=tree1.getroot()
    def genindirecttag(self):
        for i in indirect2.root:
            if i.tag=="INDIRECTTAG":
                hverb=i.attrib['HVERB']
                tpro=i.attrib['TPRO']
                iverb=i.attrib['VERB']
               
        itag=hverb+" "+tpro+" "+iverb                 
        #print(itag)
        return(hverb,tpro,iverb)
    def gensent(self):
        qmark="?"
        hverb,tpro,iverb=p2.genindirecttag()
        qtag=p1.genqtag(self)
        snoun=p1.gensnoun(self)
        verb=p1.genverb(self)
        sent=hverb+" "+tpro+" "+iverb+" "+qtag+" "+snoun+" "+verb+"s"+"?"
        taggedsent=hverb+"<w>"+tpro+"<w>"+iverb+"<w>"+qtag+"<w>"+snoun+"<w>"+verb+"s"+"<m>"
        nopunct=hverb+" "+tpro+" "+iverb+" "+qtag+" "+snoun+" "+verb+"s"
             
        category="questionmark"
        level=1
        print(sent,taggedsent,nopunct,category,level)
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
        category="exclamation"
        level=1
        
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))
        mydb.commit()        

p2=indirect2()
p2.gensent()
        
class indirect3:
    
    tree1=ET.parse('D:\\evakya\\xml\\indirect3.xml')
    root=tree1.getroot()
    def genindirecttag(self):
        for i in indirect3.root:
            if i.tag=="INDIRECTTAG":
                hverb=i.attrib['HVERB']
                tpro=i.attrib['TPRO']
                auxv=i.attrib['AUXV']
                adv=i.attrib['ADV']
                iverb=i.attrib['VERB']
                qtag="where"
        snoun=p1.gensnoun(self)
        verb=p1.genverb(self)
        itag=hverb+" "+tpro+" "+auxv+" "+adv+" "+iverb
        sent=hverb+" "+tpro+" "+auxv+" "+adv+" "+iverb+" "+qtag+" "+snoun+" "+verb+"s"+"?"
        taggedsent=hverb+"<w>"+tpro+"<w>"+auxv+"<w>"+adv+"<w>"+iverb+"<w>"+qtag+"<w>"+snoun+"<w>"+verb+"s"+"<m>"
        
        punctuations = '?'
        mylist=[]
        nopunct=hverb+" "+tpro+" "+auxv+" "+adv+" "+iverb+" "+qtag+" "+snoun+" "+verb+"s"
             
        category="questionmark"
        level=1
        print(sent,taggedsent,nopunct,category,level)
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
        category="exclamation"
        level=1
        
        mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))
        mydb.commit() 
           
 
p3=indirect3()
p3.genindirecttag()


