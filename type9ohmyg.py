import xml.etree.ElementTree as ET
import random
import re

class type9ohmyg:
    
    tree = ET.parse('D:\\evakya\\xml\\type9ohmyg.xml')
    adj=[]
    onoun=""
    onounlist=[]
    verb=""
    verbclass=""
    standaloneinter=['Oh my goodness','Oh my God']
    
            
    def generatesubject(self):#--------------------If noun ends in "s",then "That" else "Those".
        root = type9ohmyg.tree.getroot()
        #<DEMONSTRATIVEADJ TYPE="That" />
        for i in root:
            if i.tag=="DEMONSTRATIVEADJ":
                dadj=str(i.attrib['TYPE'])
                dadj=dadj.split("/")
                if type9ohmyg.onoun.endswith('s'):
                    dadj=dadj[1]
                else:
                    dadj=dadj[0]
                return(dadj)




    def genverb(self):
        root = type9ohmyg.tree.getroot()
        for i in root:
            if i.tag=="VERB":#--------------------If noun ends in "s",then plural and verbtobe is "are".
                if type9ohmyg.onoun.endswith('s'):
                    i.attrib['VERBTOBE']="are/'re"
                    vb=i.attrib['VERBTOBE']
                    vb=vb.split("/")
                    vb1=random.choice(vb)
                    return(vb1)
                    
                else:
                    i.attrib['VERBTOBE']="is"
                    vb=i.attrib['VERBTOBE']
                    return(vb)
                    
                

    def genonoun(self):
       # <ONOUN NAME="x" ART="x" ADJ="x" ECLASS="negative" />
        root=type9ohmyg.tree.getroot()
        verblst=[]
        for i in root:  # ONOUN
            if i.tag=="ONOUN":
                type9ohmyg.verbclass=i.attrib['ECLASS']
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:                        
                        dh=word.split(':')
                        if type9ohmyg.verbclass==dh[2]:
                            verblst.append(dh[0])

                    verbcat=random.choice(verblst)
                    #print(verbcat)
        for i in root:  # ONOUN
            if i.tag=="ONOUN":
                
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                
                    for word in nd:
                        dh=word.split(':')
                        #print(dh)
                        if verbcat==dh[0]:
                           
                            type9ohmyg.onounlist.append(dh[1])                            
                type9ohmyg.onoun=random.choice(type9ohmyg.onounlist)
                #print(type9ohmyg.onoun)
                
                
    
                with open("D:\\evakya\\dataset\\adjectives.txt") as nd:
                    adjlst=[]
                    for word in nd:
                        dh=word.split(':')
                        #print("eclass",type9ohmyg.verbclass)
                        if verbcat==dh[0]:
                           
                            adjlst.append(dh[1])
                            #print(adjlst)
        type9ohmyg.adj=random.choice(adjlst)
        pattern = '^[aeiou]'
        test_string = type9ohmyg.adj
        #print("test",test_string)
        result = re.match(pattern, test_string)
        if type9ohmyg.onoun.endswith('s'):
            pro=['her','his']
            article=random.choice(pro)
            
        else:
            if result:
               
              #print("Search successful.")
              article="an"
            else:
              #print("Search unsuccessful.")
              article="a"
        nadj=type9ohmyg.adj
        nobjnoun=type9ohmyg.onoun
        nart=article
        
            
        return(nart,nadj,nobjnoun)

    def getinterjection(self):
        root=type9ohmyg.tree.getroot()
        for i in root:
            if (i.tag=="INTERJECTION" and i.attrib['TYPE']=="Standalone"):
                intn=random.choice(type9ohmyg.standaloneinter)
                return(intn)
                
                
                
    def gentype9ohmyg(self):
       
       intn=p1.getinterjection()
       i=intn.split(" ")
       nart,nadj,nobjnoun=p1.genonoun()
       vb=p1.genverb()
       dadj=p1.generatesubject()
       excl="!"
       period="."
       print("vb",vb)
       if vb=="is":
           text1=dadj+" "+vb
           text2=dadj+"'s"
           #sent1=intn+excl+text1+" "+nart+" "+nadj+" "+nobjnoun+period
           sent2=intn+excl+text2+" "+nart+" "+nadj+" "+nobjnoun+period
           taggedsent=i[0]+"<w>"+i[1]+"<w>"+i[2]+"<m>"+text2+"<w>"+nart+"<w>"+nadj+"<w>"+nobjnoun+"<m>"
           nopunct=intn+" "+text2+" "+nart+" "+nadj+" "+nobjnoun
           print(sent2,taggedsent,nopunct)
           
           return(sent2,taggedsent,nopunct)
       elif vb=="are" or "'re":
           text1=dadj+" "+vb
           text2=dadj+"'re"      
           sent1=intn+excl+" "+text2+" "+nart+nadj+" "+nobjnoun+period
           taggedsent=i[0]+"<w>"+i[1]+"<w>"+i[2]+"<m>"+text2+"<w>"+nart+"<w>"+nadj+"<w>"+nobjnoun+"<m>"
           nopunct=intn+" "+text1+" "+nart+" "+nadj+" "+nobjnoun
           print(sent1,taggedsent,nopunct)
           return(sent1,taggedsent,nopunct)
           
for i in range(0,5):
    p1=type9ohmyg()
    sent1,taggedsent,nopunct=p1.gentype9ohmyg()
    
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
           
    id2=id1+1
    category="exclamation"
    level=3
    
    mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent1,taggedsent,category,level,1))
    mydb.commit() 

