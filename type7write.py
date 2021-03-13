import xml.etree.ElementTree as ET
import random
import re
#from dictionarylist import dictionarylist as dl 
class type7w:
    
    
    snname=""
    alst=[]
    noundict=[]
    verb=""
    title=""
    tree = ET.parse('D:\\evakya\\xml\\type72wrote.xml')
    authorslst={'Arundhati Roy':'A. Roy','Khushwant Singh':'K. Singh','Rasipuram Krishnaswami Iyer Narayanaswami':'R. K. I. Narayan','Rachel Kushner':'R. Kushner','G. B. Shaw': 'G. B. Shaw'}
    booklst={'A. Roy':'The God of Small Things','K. Singh':'Train to Pakistan','R. K. I. Narayan':'The Malgudi Days','R. Kushner':'The Mars Room','G. B. Shaw':'Arms and the Man'}   
    def generatesent(self):
        
        root = type7w.tree.getroot()
        alst=[]
        
        for i in root:
            if i.tag=="SNOUN":
                                
                item=['Arundhati Roy', 'Khushwant Singh', 'Rasipuram Krishnaswami Iyer Narayanaswami', 'Rachel Kushner', 'G. B. Shaw']
                for j in item:
                    
                # Substring Key match in dictionary 
                    res = [val for key, val in type7w.authorslst.items() if j == key] 
                    author=res[0]
                    author1=res
                    

                    
                    bookres = [val for key, val in type7w.booklst.items() if author == key]
                    
                    #print("book",bookres[0])
                    type7w.verb="wrote"
                    
##            if i.tag=="VERB":
##                type7w.verb=i.attrib['TYPE'] 
##                print(type7w.verb)
                    
                    sq='"'
                    eq='"'
                    period="."
                    correctans=author+" "+type7w.verb+" "+sq+bookres[0]+eq+" "+period
                    taggedsent=correctans.replace(".","<m>")
                    taggedsent=taggedsent.replace('"' ,"<m>")
                
                    taggedsent=taggedsent.replace(" ","<w>")
                    taggedsent=taggedsent.replace("<m><w>","<m>")
                    taggedsent=taggedsent.replace("<w><w>","<w>")
                    taggedsent=taggedsent.replace("<w><m>","<w>")
                    taggedsent=taggedsent.replace("<m><m>","<m>")
                    print(taggedsent)
                      
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
                            ##print("id1:",row[0])
                    #--------------------unpunctuate-----------------------------------------------------------------
                    punctuations = '''!()[]{};:'\,<>./?@#$%^&*_~'''
                    nopunct=""
                    for char in correctans:
                        if char not in punctuations:
                            nopunct = nopunct + char
                    ##print(nopunct)         
                    id2=id1+1
                    category="fullstop"
                    level=4    
                    
                  ###-----------------------------insert into database------------------------------------------------------------------------------------------------------------------   
                    mycursor.execute('insert into sentencedb(exerciseid,nopunct,correctans,taggedsent,category,level,displayorder) values(%s,%s, %s, %s, %s, %s, %s )', (id2,nopunct,correctans,taggedsent,category,level,1))
                    mydb.commit()
##

p1=type7w()                
p1.generatesent()
