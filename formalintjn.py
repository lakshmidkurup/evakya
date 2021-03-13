import xml.etree.ElementTree as ET
import random
import re

class formalintjn:
    tree = ET.parse('D:\\evakya\\xml\\formalintjn.xml')
    root=tree.getroot()
    sname=""
    noundict=[]
    verblst=[]
    verbclass=""
    def genaddtag(self):
        for i in formalintjn.root:
            if i.tag=="ADDTAG":
                tag1=i.attrib['TAG']
                abbrlst=['Dr','Prof']
                abbr=random.choice(abbrlst)
                if i.attrib['TYPE']=="personified":
                    noundict=[]

                    with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                        for word in nd:
                            dh=word.split(':')
                            if i.attrib['TYPE'] == dh[0]:
                                formalintjn.noundict.append(dh[1])

                                ##print(type5.noundict)
                        formalintjn.snname=random.choice(formalintjn.noundict) 
        addtag=tag1+" "+abbr+" "+formalintjn.snname
        #print(tag1,abbr,formalintjn.snname)
        return(tag1,abbr,formalintjn.snname)

    def genclause1(self):
        for i in formalintjn.root:
            if i.tag=="CLAUSE1":
                ppro=i.attrib['PPRO']
                VBZ=i.attrib['VBZ']
                verb=i.attrib['VERB']
        clause1=ppro+" "+VBZ+" "+verb
        #print(ppro,VBZ,verb)
        return(ppro,VBZ,verb)
        
    def genconjphrase(self):

        for i in formalintjn.root:
            if i.tag=="CONJPHRASE":
                prep=i.attrib['PREP']
                verb2=i.attrib['VERB']
                spro=i.attrib['SPRO']
                conj=i.attrib['CONJ']
        cphrase=prep+" "+verb2+" "+spro+" "+conj
        #print(prep,verb2,spro,conj)
        return(prep,verb2,spro,conj)

    def genclause2(self):
        
        for i in formalintjn.root[3]:
            if i.tag=="SNOUN":
                formalintjn.noundict.remove(formalintjn.snname)
                snoun2=random.choice(formalintjn.noundict)
                #print(snoun2)
            if i.tag=="VERBP":
                hverb=i.attrib['HVERB']
                #print("hv",hverb)
                verbclass=i.attrib['ECLASS']
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if verbclass == dh[2]:
                            formalintjn.verblst.append(dh[1])
                verbclause2=random.choice(formalintjn.verblst)
                #print(verbclause2)
                with open("D:\\evakya\\dataset\\verbclass.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if verbclause2 == dh[1]:
                            formalintjn.verbclass=dh[0]
                            #print(formalintjn.verbclass)
            if i.tag=="ONOUNP":
                det=i.attrib['DET']
                with open("D:\\evakya\\dataset\\noundict.txt") as nd:
                    for word in nd:
                        dh=word.split(':')
                        if formalintjn.verbclass == dh[0]:
                            formalintjn.noundict.append(dh[1])
                onlst=[]
                #print("form",formalintjn.noundict)
                onoun=formalintjn.noundict[-1]
               
                #onoun=random.choice(formalintjn.noundict)
                
                #print("onoun",det,onoun)
                
        clause2=snoun2+" "+hverb+" "+verbclause2+" "+det+" "+onoun
        #print("onoun",onoun)
        #print(snoun2,hverb,verbclause2,det,onoun)
        return(snoun2,hverb,verbclause2,det,onoun)
    def gensent(self):
        for i in range(1,6):
            comma=","
            period="."
            prep,verb2,spro,conj=p1.genconjphrase()
            
            ppro,VBZ,verb=p1.genclause1()
            tag1,abbr,formalintjn.snname=p1.genaddtag()
            snoun2,hverb,verbclause2,det,onoun=p1.genclause2()
            
            sent=tag1+" "+abbr+"."+formalintjn.snname+comma+" "+ppro+" "+VBZ+" "+verb+" "+prep+" "+verb2+" "+spro+" "+conj+" "+snoun2+" "+hverb+" "+verbclause2+" "+det+" "+onoun+period
            nopunct=tag1+" "+abbr+" "+formalintjn.snname+" "+ppro+" "+VBZ+" "+verb+" "+prep+" "+verb2+" "+spro+" "+conj+" "+snoun2+" "+hverb+" "+verbclause2+" "+det+" "+onoun
            taggedsent=tag1+"<w>"+abbr+"<m>"+formalintjn.snname+"<m>"+ppro+"<w>"+VBZ+"<w>"+verb+"<w>"+prep+"<w>"+verb2+"<w>"+spro+"<w>"+conj+"<w>"+snoun2+"<w>"+hverb+"<w>"+verbclause2+"<w>"+det+"<w>"+onoun+"<m>"
            print(taggedsent)
            formalintjn.noundict=[]
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
            level="1"
            #-----------------------------insert into database------------------------------------------------------------------------------------------------------------------   

            mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s, %s, %s, %s, %s, %s, %s )', (id2,nopunct,sent,taggedsent,category,level,1))
            mydb.commit()


p1=formalintjn()
p1.gensent()
            
