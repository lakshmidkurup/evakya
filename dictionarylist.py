#import pandas as pd
import random


class dictionarylist:

    cooksent=""
    readsent=""
    cookitemsl=[]
    readitemsl=[]
    book=""
    author=""


    colors = {
        'colors' : ['red', 'green', 'blue', 'orange'],
        'flowers' : ['roses', 'zinnias', 'tulips', 'sunflowers'],
        'vegetables' : ['tomatoes', 'ladies fingers', 'cabbages', 'cucumbers'],
        'fruits': ['apples', 'guavas', 'dragon fruits', 'oranges'],
        'nature': ['sun', 'meadow grass', 'sky', 'sunset']
        
    }

    cook= {
        'items':['seasonings', 'non-vegetarian', 'vegetarian', 'oil'],
        'biriyani':['pepper', 'chicken', 'carrot', 'ghee'],
        'friedrice':['cloves', 'fish', 'beans', 'butter'],
        'kichdi':['salt', 'prawns', 'cauliflower', 'vegetable oil'],
        'pulav':['origamo', 'pork', 'cabbage', 'dalda']
          }

    read={
        'book':["non-fictional","fictional","children","science-fiction"],
        'title':['The God of Small Things','Train to Pakistan','The Malgudi Days','The Mars Room'],
        'authored by':['Arundhati Roy','Khushwant Singh','Rasipuram Krishnaswami Iyer Narayanaswami','Rachel Kushner'],
        'rated by amazon kindle':['4.2/5','3.8/5','4.2/5','3.9/5'],
        'suitable for':['all age groups','adult age groups','kids','science lovers']       
        }
    write={
        'category':['poems','stories','blogs','novels'],
        'type':['short','long','internet','lengthy'],
        'section':['epic','fictional','technological','adventurous'],
        'language':['marati','hindi','english','spanish'],
        'suitable for':['all age groups','all age groups','all age groups','adults']}         
        

    def readitems(self):
        
        a=dictionarylist.read.keys()
        for i in a:
            if i=="title":
                dictionarylist.readitemsl=dictionarylist.read['title'][:-1]
        return(dictionarylist.readitemsl)
    
   
    def cookitems(self):
        
        a=dictionarylist.cook.keys()
        for i in a:
            if i not in ['items']:
                dictionarylist.cookitemsl.append(i)
        #print(dictionarylist.cookitemsl)

        return(dictionarylist.cookitemsl)
        
    def genwritesent(self):
        write = {
        'category':['poems','stories','blogs','novels'],
        'type':['short','long','internet','lengthy'],
        'section':['epic','fictional','technological','adventurous'],
        'language':['marati','hindi','english','spanish'],
        'audience':['all age groups','all age groups','all age groups','adults']
        }
        writekeys=write.keys()
        for key in writekeys:#items like friedrice,biriyani,kichdi and pulav
            if key=="category":
                prep="like"
                conj="and"
                val=key+" "+prep+" "+','.join((write['category'][:-1]))+" "+conj+" "+write['category'][-1]
                return(val)
        for key in writekeys:#items like friedrice,biriyani,kichdi and pulav
            if key=="type":
                prep="like"
                conj="and"
                val=key+" "+prep+" "+','.join((write['type'][:-1]))+" "+conj+" "+write['type'][-1]
                return(val)

        for key in writekeys:#items like friedrice,biriyani,kichdi and pulav
            if key=="section":
                prep="like"
                conj="and"
                val=key+" "+prep+" "+','.join((write['section'][:-1]))+" "+conj+" "+write['section'][-1]
                return(val)        
        for key in writekeys:#items like friedrice,biriyani,kichdi and pulav
            if key=="language":
                prep="like"
                conj="and"
                val=key+" "+prep+" "+','.join((write['language'][:-1]))+" "+conj+" "+write['language'][-1]
                return(val)   
        for key in writekeys:#items like friedrice,biriyani,kichdi and pulav
            if key=="audience":
                prep="like"
                conj="and"
                val=key+" "+prep+" "+','.join((write['audience'][:-1]))+" "+conj+" "+write['audience'][-1]
                return(val)
    def gencolorsent(self):
        colors = {
        'colors' : ['red', 'green', 'blue', 'orange'],
        'flowers' : ['roses', 'zinnias', 'tulips', 'sunflowers'],
        'vegetables' : ['tomatoes', 'ladies fingers', 'cabbages', 'cucumbers'],
        'fruits': ['apples', 'guavas', 'dragon fruits', 'oranges'],
        'nature': ['sun', 'meadow grass', 'sky', 'sunset']
        }
        colorkeys=colors.keys()
        for key in colorkeys:#items like friedrice,biriyani,kichdi and pulav
            if key=="type":
                prep="like"
                conj="and"
                val=key+" "+prep+" "+','.join((colors['type'][:-1]))+" "+conj+" "+colors['type'][-1]
                return(val)
        for key in colorkeys:#
            if key=="flowers":
                prep="like"
                conj="and"
                val=key+" "+prep+" "+','.join((colors['flowers'][:-1]))+" "+conj+" "+colors['flowers'][-1]
                return(val)
        for key in colorkeys:
            if key=="vegetables":
                prep="like"
                conj="and"
                val=key+" "+prep+" "+','.join((colors['vegetables'][:-1]))+" "+conj+" "+colors['vegetables'][-1]
                return(val)
        for key in colorkeys:
            if key=="fruits":
                prep="like"
                conj="and"
                val=key+" "+prep+" "+','.join((colors['fruits'][:-1]))+" "+conj+" "+colors['fruits'][-1]
                return(val)
        for key in colorkeys:
            if key=="nature":
                prep="like"
                conj="and"
                val=key+" "+prep+" "+','.join((colors['nature'][:-1]))+" "+conj+" "+colors['nature'][-1]
                return(val) 
        
##        a=cobj.loc[0:3].values
##        #return(a)
##        item="blue"
##        for index1, inner_l in enumerate(a):
##            for index2, item in enumerate(inner_l):
##                if item=="red":
##                    ared=random.choice(inner_l[1:])
##                    return(ared)
##                    return(ared)
##                elif item=="green":
##                    agreen=random.choice(inner_l[1:])
##                    return(agreen)
##                    return(agreen)
##
##                elif item=="orange":
##                    aorange=random.choice(inner_l[1:])
##                    return(aorange)
##                    return(aorange)
##                elif item=="blue":
##                    ablue=random.choice(inner_l[1:])
##                    return(ablue)
##                    return(ablue)


    
        

    def gencooksent(self):
        
        cook= {
        'items':['friedrice', 'biriyani', 'kichdi', 'pulav'],
        'seasonings':['pepper', 'cloves', 'salt', 'origamo'],
        'meat':['chicken', 'fish', 'prawns', 'pork'],
        'vegetables':['carrot', 'beans', 'cauliflower', 'cabbage'],
        'oil':['vegetable oil', 'rice oil', 'sunflower oil', 'coconut oil']
          }
        cookkeys=cook.keys()
       
        for key in cookkeys:#items like friedrice,biriyani,kichdi and pulav
            if key=="items":
                prep="like"
                conj="and"
                val1=key+" "+prep+" "+','.join((cook['items'][:-1]))+" "+conj+" "+cook['items'][-1]
                #print(val1)
        for key in cookkeys:#items like friedrice,biriyani,kichdi and pulav
            if key=="seasonings":
                prep="like"
                conj="and"
                val2=key+" "+prep+" "+','.join((cook['seasonings'][:-1]))+" "+conj+" "+cook['seasonings'][-1]
                #print(val2)
        for key in cookkeys:#items like friedrice,biriyani,kichdi and pulav
            if key=="meat":
                prep="like"
                conj="and"
                val3=key+" "+prep+" "+','.join((cook['meat'][:-1]))+" "+conj+" "+cook['meat'][-1]
                #print(val3)
        for key in cookkeys:#items like friedrice,biriyani,kichdi and pulav
            if key=="vegetables":
                prep="like"
                conj="and"
                val4=key+" "+prep+" "+','.join((cook['vegetables'][:-1]))+" "+conj+" "+cook['vegetables'][-1]
                #print(val4)
        for key in cookkeys:#items like friedrice,biriyani,kichdi and pulav
            if key=="oil":
                prep="like"
                conj="and"
                val5=key+" "+prep+" "+','.join((cook['oil'][:-1]))+" "+conj+" "+cook['oil'][-1]
                #print(val5)                
        s=" "
        semicolon=";"
        res=val2,semicolon,val3,semicolon,val4,semicolon,val5
        sent=s.join(res)
       # print(sent)
        return(sent)
        #items like friedrice biriyani kichdi and pulav can be made using seasonings like pepper,cloves;non-ve
##        
##        for search_key in list(cookkeys):
##            if search_key=='items':
##                res = list(cookkeys).index(search_key)  
##                return(res)
##        
##
##            
##        cookobj = pd.DataFrame(cook)
##        a=cookobj.loc[0:3].values
##        #return(cookobj)
##        
##        for index1, inner_l in enumerate(a):
##            for index2, item in enumerate(inner_l):
##                if item=="seasonings":
##                    abir=random.choice(inner_l[1:])
##                    return(abir)            
##                elif item=="non-vegetarian":
##                    afr=random.choice(inner_lr[1:])
##                    return(afr)
##
##                elif item=="vegetarian":
##                    ak=random.choice(inner_l[1:])
##                    return(ak)
##
##                elif item=="oil":
##                    ap=random.choice(inner_l[1:])
##                    return(ap)       
    def genreadsent(self):
##        read={
##        'book':["non-fictional","fictional","children","science-fiction"],
##        'title':['The God of Small Things','Train to Pakistan','Malgudi Days','The Mars Room'],
##        'authored by':['Arundhati Roy','Khushwant Singh','R.K. Narayanan','Rachel Kushner'],
##        'rated by amazon kindle':['4.2/5','3.8/5','4.2/5','3.9/5'],
##        'suitable for':['all age groups','adult age groups','kids','science lovers']       
##        }
##       
        # Using list() + keys() + index() 
        # Key index in Dictionary
        readkeys=dictionarylist.read.keys()
        for search_key in list(readkeys):
            if search_key=='book':
                res = list(readkeys).index(search_key)  
                #return(res)
            if search_key=='title': 
                res1 = list(readkeys).index(search_key)  
                #return(res1)
            if search_key=='authored by':
                res2 = list(readkeys).index(search_key)  
                #return(res2)
            if search_key=='rated by amazon kindle':
                res3 = list(readkeys).index(search_key)  
                #return(res3)
            if search_key=='suitable for':
                res4 = list(readkeys).index(search_key)  
                #return(res4)    
        for key in readkeys:
            if key=="book":
                val1=dictionarylist.read["book"][res]+" "+key
                val2=dictionarylist.read["book"][res1]+" "+key
                val3=dictionarylist.read["book"][res2]+" "+key
                val10=dictionarylist.read["book"][res3]+" "+key
                
            if key=="title":
                prep="of"
                startqot='"'
                endqot='"'
                val4=prep+" "+key+" "+startqot+dictionarylist.read["title"][res]+endqot
                val5=prep+" "+key+" "+startqot+dictionarylist.read["title"][res1]+endqot
                val6=prep+" "+key+" "+startqot+dictionarylist.read["title"][res2]+endqot
                val12=prep+" "+key+" "+startqot+dictionarylist.read["title"][res3]+endqot
                
            if key=="authored by":
                
                val7=key+" "+dictionarylist.read["authored by"][res]
                val8=key+" "+dictionarylist.read["authored by"][res1]
                val9=key+" "+dictionarylist.read["authored by"][res2]
                val20=key+" "+dictionarylist.read["authored by"][res3]
               
            if key=="rated by amazon kindle":
                prep="as"
                val16=key+" "+prep+" "+dictionarylist.read["rated by amazon kindle"][res]
                val17=key+" "+prep+" "+dictionarylist.read["rated by amazon kindle"][res1]
                val18=key+" "+prep+" "+dictionarylist.read["rated by amazon kindle"][res2]
                val19=key+" "+prep+" "+dictionarylist.read["rated by amazon kindle"][res3]
                

            if key=="suitable for":
                conj="and"
                val21=" "+conj+" "+key+" "+dictionarylist.read["suitable for"][res]
                val22=" "+conj+" "+key+" "+dictionarylist.read["suitable for"][res1]
                val23=" "+conj+" "+key+" "+dictionarylist.read["suitable for"][res2]
                val24=" "+conj+" "+key+" "+dictionarylist.read["suitable for"][res3]
                
        s=""
        semicolon=";"
        conj="and"
        result1=val4,semicolon,val7,semicolon,val16,val21
        result2=val5,semicolon,val8,semicolon,val17,val22
        result3=val6,semicolon,val9,semicolon,val18,val23
        result4=val12,semicolon,val20,semicolon,val19,val24
        
         #-----------------------------
        
        a=s.join(result1)
        b=s.join(result2)
        c=s.join(result3)
        d=s.join(result4)
        import random
        ls=[a,b,c,d]
        res=random.choice(ls)
        
        return(res)
    
    def bookauthordl(self):
        readkeys=dictionarylist.read.keys()
        for search_key in list(readkeys):
            if search_key=='book':
                res = list(readkeys).index(search_key)  
                #return(res)
            if search_key=='title': 
                res1 = list(readkeys).index(search_key)  
                #return(res1)
            if search_key=='authored by':
                res2 = list(readkeys).index(search_key)  
                #return(res2)
            if search_key=='rated by amazon kindle':
                res3 = list(readkeys).index(search_key)  
                #return(res3)
            if search_key=='suitable for':
                res4 = list(readkeys).index(search_key)  
                #return(res4)    
        for key in readkeys:
            
                
            if key=="title":
                prep="of"
                startqot='"'
                endqot='"'
                val4=prep+" "+key+" "+startqot+dictionarylist.read["title"][res]+endqot
                val5=prep+" "+key+" "+startqot+dictionarylist.read["title"][res1]+endqot
                val6=prep+" "+key+" "+startqot+dictionarylist.read["title"][res2]+endqot
                val12=prep+" "+key+" "+startqot+dictionarylist.read["title"][res3]+endqot
                
            if key=="authored by":
                
                val7=key+" "+dictionarylist.read["authored by"][res]
                val8=key+" "+dictionarylist.read["authored by"][res1]
                val9=key+" "+dictionarylist.read["authored by"][res2]
                val20=key+" "+dictionarylist.read["authored by"][res3]
       #----books with author dictionary list
        booksauthor1={dictionarylist.read["title"][res]:dictionarylist.read["authored by"][res]}
        booksauthor2={dictionarylist.read["title"][res1]:dictionarylist.read["authored by"][res1]}
        booksauthor3={dictionarylist.read["title"][res2]:dictionarylist.read["authored by"][res2]}
        booksauthor4={dictionarylist.read["title"][res3]:dictionarylist.read["authored by"][res3]}
        booksauthor=[booksauthor1,booksauthor2,booksauthor3,booksauthor4] 
        import random
        e=random.choice(booksauthor)
        for key in e:
            book=key
        
        print(book,e.values())
        return(book,e.values())
p1=dictionarylist()
#p1.gencooksent()
dictionarylist.readitemsl=p1.readitems()
dictionarylist.cookitemsl=p1.cookitems()
dictionarylist.readsent=p1.genreadsent()
dictionarylist.cooksent=p1.gencooksent()
dictionarylist.book,dictionarylist.author=p1.bookauthordl()
#print(dictionarylist.cookitemsl)
p1.genwritesent()
##print(dictionarylist.readsent)
#p1.bookauthordl()
