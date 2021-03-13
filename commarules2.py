    
########################################################################################################################################################################


    
    def commathree(self):
        mandlst=[]
        correctlst=[]
        hintlst=[]
        #print("commarules",b,c,correct,level,username,userid,eid,submittedtext)
        b=['Mary', '<w>', 'stays', '<w>', 'in', '<w>', 'a', '<w>', 'house', '<m>', 'Her', '<w>', 'address', '<w>', 'is', '<w>', 'C/O', '<w>', 'Late', '<w>', 'Mr', '<m>', 'Esmail', '<w>', 'Bagani', '<m>', 'Y/2/122', '<m>', 'B-Wing', '<m>', 'Sarayu', '<w>', 'Society', '<m>', 'Satghara', '<w>', 'Road', '<m>', 'Badartala', '<m>', 'Kolkata', '<m>', 'Bengal', '<m>', '700044', '<m>']
        c=['Mary', ' ', 'stays', ' ', 'in', ' ', 'a', ' ', 'house', ',', 'Her', ' ', 'address', ' ', 'is', ' ', 'C/O', ',', 'Late', ' ', 'Mr', ',', 'Esmail', ' ', 'Bagani', ' ', 'Y/2/122', ' ', 'B-Wing', ' ', 'Sarayu', ' ', 'Society', ' ', 'Satghara', ' ', 'Road', ' ', 'Badartala', ' ', 'Kolkata', ' ', 'Bengal', ' ', '700044', '.']
        
##        b=['James', '<w>', 'won', '<w>', 'a', '<w>', 'race', '<w>', 'on', '<w>', 'February', '<w>', '17', '<m>', '2009', '<m>']
##        c=['James', ' ', 'won', ' ', 'a', ' ', 'race', ' ', 'on', ' ', 'February', ',', '17', ' ', '2009', ' ']
        
        
##        b=['Mary', '<w>', 'was', '<w>', 'born', '<w>', 'on', '<w>', 'Tuesday', '<m>', 'February', '<w>', '17', '<m>', '2009', '<m>']
##        c=['Mary',' ', 'was',' ', 'born', ';', 'on', ' ', 'Tuesday', ' ', 'February', ' ', '17', ' ', '2009', '.']
        
##        b=['Alice', '<w>', 'was', '<w>', 'born', '<w>', 'on', '<w>', '17', '<w>', 'February', '<m>', '2009', '<m>']
##        c=['Alice', ',', 'was', ' ', 'born', ' ', 'on', ' ', '17', ' ', 'February', ' ', '2009', ' ']
##        b=['James', '<w>', 'was', '<w>', 'born', '<w>', 'on', '<w>', 'February', '<m>', '17', '<m>']
##        c=['James', ' ', 'was', ' ', 'born', ' ', 'on', ' ', 'February', ' ', '17', ';']

##
##        b=['James', '<w>', 'won', '<w>', 'a', '<w>', 'race', '<w>', 'on', '<w>', 'February', '<w>', '17', '<m>', '2009', '<m>']
##        c=['James', ' ', 'won', ',', 'a', ' ', 'race', ' ', 'on', ',', 'February', ',', '17', ' ', '2009', ' ']
##        b=['John', '<w>', 'paid', '<w>', 'Rs', '<m>', '4', '<m>', '300', '<w>', 'for', '<w>', 'his', '<w>', 'adorable', '<w>', 'bicycle', '<m>']
##        c=['John', '.', 'paid', ';', 'Rs', ',', '4', ',', '300', ',', 'for', ' ', 'his', ' ', 'adorable', ' ', 'bicycle','.']
##        b=['Mr', '<m>', 'John', '<m>', 'a', '<w>', 'charming', '<w>', 'gentleman', '<m>', 'might', '<w>', 'open', '<w>', 'a', '<w>', 'small', '<w>', 'cage', '<m>', 'Morever', '<m>', 'he', '<w>', 'might', '<w>', 'lift', '<w>', 'it', '<m>']
##                                                                                                                                                                    
##        c=['Mr', '', 'John', ' ', 'a', ',', 'charming', '', 'gentleman', ',', 'might', ' ', 'open', ',', 'a', ',', 'small', '<w>', 'cage', ',', 'Morever', ',', 'he', ' ', 'might', ',', 'lift', ' ', 'it', '.']

##        c=['Sr', ';', 'Mary', ' ', 'a', ' ', 'generous', ' ', 'lady', ';', 'could', ' ', 'open', ' ', 'a', ' ', 'huge', ' ', 'cage', ' ', 'and', ' ', 'a', ' ', 'red', ' ', 'box',' ']
##        b=['Sr', '<m>', 'Mary', '<m>' , 'a', '<w>', 'generous', '<w>', 'lady', '<m>', 'could', '<w>', 'open', '<w>', 'a', '<w>', 'huge', '<w>', 'cage', '<w>', 'and', '<w>', 'a', '<w>', 'red', '<w>', 'box','<m>']

##        c=['Major', '.', 'John', '.', 'a', ',', 'charming', ' ', 'gentleman', '.', 'could', ',', 'open', ' ', 'a', ' ', 'box', ';', 'a', ' ', 'book', ',', 'and', ' ', 'a', ' ', 'cage', '.']
##        b=['Major', '<m>', 'John', '<m>', 'a', '<w>', 'charming', '<w>', 'gentleman', '<m>', 'could', '<w>', 'open', '<w>', 'a', '<w>', 'box', '<m>', 'a', '<w>', 'book', '<w>', 'and', '<w>', 'a', '<w>', 'cage', '<m>']
        print(b)
        print(c)
        co="".join(c)
##        year=str(str(parse(co, fuzzy=True).year))
##        day=parse(co,fuzzy=True).day
##        year=str(year)
##        day=str(day)
##        print("year",year)
##        print("day",day)
    #---------------------------------------------------<m> with semicolon-----------------------------------------------------------------------------------       
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==";"):
                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
                    hint="InCorrect Answer:Hint:Remove semicolon after the title",b[i-1]
                    
                    mandlst.append(hint)


                if b[i-3]==str(parse(co,fuzzy=True).day) and b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                    hint="InCorrect Answer:Remove the semicolon and Put a comma just after the month, " +b[i-1]+"  if the date format is date-month-year"
                    mandlst.append(hint)     
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="InCorrect Answer:HInt:Remove the semicolon after the common noun",b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="InCorrect Answer:Remove  the semicolon after the main subject",b[i-1]
                    mandlst.append(hint)
                
                if (b[i-1] in crules.onoun) and (b[i]=="<m>"):    
                    hint="InCorrect Answer:Hint:Remove the semicolon after the noun and put a FULLSTOP",b[i-1]
                    mandlst.append(hint)
                onounlst=list(set(crules.onoun) & set(b))    
                if len(onounlst) > 2:
                    if (b[i-1] in crules.onoun and (b[i+1] in crules.article)):
                
                        hint="InCorrect Answer:Hint:Remove the semicolon after the noun and put a comma after ",b[i-1]
                        mandlst.append(hint) 
               
                if c[-1]==";":
                    hint="Incorrect answer:Hint:Remove the semicolon a the end of the sentence"
                    mandlst.append(hint)
                
                                 
    #---------------------------------------------------------type6.py---------------------------------------------------------------------------
                if b[i-1] in crules.conjadv and b[i+1] in crules.pronoun:
                    
                    hint="InCorrect Answer:Hint:A Comma is needed after the conjunctive adverb.", b[i-1]
                
                    mandlst.append(hint) 
                    
               
                if b[i-1] in crules.onoun and b[i+1] in crules.conjadv:
                    
                    hint="InCorrect Answer.Hint: Put a fullstop to seperate two complete sentences."
                
                    mandlst.append(hint)
                if (b[i-1] in crules.onoun) and c[-1]==";":
                    
                    hint="InCorrect Answer.Always end a sentence with a FULLSTOP"
                
                    mandlst.append(hint)
                if(b[i-1] in crules.pronoun) and c[-1]==";":
                    
                    hint="InCorrect Answer.Always end a sentence with a FULLSTOP"
                
                    mandlst.append(hint)    
         #---------------------------type10comma.py----------------------------------------------------------------
                if b[i-1] =="Rs" and b[i+1].isdigit():
                    hint="InCorrect Answer:Remove the semicolon and Put a FULLSTOP after the keyword {Rs]"
                    mandlst.append(hint)     
                phrase="".join(b)
                oned=re.findall("\d+",phrase)
                #print("oned",oned[0],oned[1])
                if b[i-3]=="Rs" and b[i-1]==oned[0] and b[i+1]==oned[1]:
                    hint="InCorrect Answer:Remove the semicolon and Put a Comma after"+" "+b[i-1]
                    correctlst.append(hint)
                    
                if b[i-3]=="Rs" and b[i-1].isdigit() and c[-1]==" ":
                    hint="InCorrect Answer:Remove the semicolon and END the sentence with a FULLSTOP"
                    mandlst.append(hint)
              #-----------type11date.py----------------------------------------------------------------    
               
                if b[i-1]==str(parse(co,fuzzy=True).day) and b[-1]=="<m>":
                    hint="Incorrect Answer:Remove the semicolon and Put a FULLSTOP after the date",b[i-1]
                    mandlst.append(hint)   
                if b[i-3] in crules.months and b[i-1]==str(parse(co,fuzzy=True).day) and b[-1]!="<m>":
                    hint="InCorrect Answer:Remove the semicolon and put a comma after a date ",b[i-1], " when it is followed by a year."
                    mandlst.append(hint)
                if b[i-1]==str(str(parse(co, fuzzy=True).year)) and b[-1]=="<m>":
                    hint="InCorrect Answer:Remove the semicolon after ",b[i-1]," and end the sentence with a FULLSTOP"
                    mandlst.append(hint)
                if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                    hint="InCorrect Answer:Remove the semicolon and add a comma should be used after the month ",b[i-1]," when it is followed by just a date(no year mentioned)."
                    mandlst.append(hint)
              
                     
                if b[i-1] in crules.weekdays and b[i+1] in crules.months :
                    hint="InCorrect Answer:Remove the semicolon after ",b[i-1],"when it is followed by a month and date and put a comma"
                    correctlst.append(hint)
               #-----------------------------------------type12stay.py------------------------------------------------

                    
                if b[i-1]==crules.title and b[i+1]== crules.title:
                    hint="Incorrect Answer.NO need of a semicolon after a title"
                    mandlst.append(hint)
                name=['Esmail Bagani']
                
                for i in name:
                    name1=i.split(" ")
                if b[i-1]==crules.title and b[i+1]== crules.name1[0]:
                    hint="InCorrect Answer.No need of a semicolon between a title and a name"
                    mandlst.append(hint)
                if b[i-1]==crules.title and b[i+1]== crules.name1[1]:
                    hint="InCorrect Answer.No need of a semicolon between a title and a name"
                    mandlst.append(hint)
                if b[i-1].isaplha() and b[i+1]==name1[0] or name1[1]:
                    hint="InCorrect Answer.No need of a semicolon between a tiInitial and a name"
                    mandlst.append(hint)
                if b[i-1]==crules.pincode and b[i+1]==None:
                    hint="InCorrect Answer.No need of a semicolon at the end of the sentence"
                    mandlst.append(hint)
                if b[i-1] in crules.onamelst and b[i+1]=="The":
                    hint="InCorrect Answer.No need of a semicolon between two sentences"
                    mandlst.append(hint)
                if b[i-1]=="Pvt" and b[i+1]=="Ltd":
                    hint="InCorrect Answer.No need of a semicolon between Pvt and Ltd..Is a single entity"
                    mandlst.append(hint)
                if b[i-1]=="Ltd":
                    hint="InCorrect Answer.No need of a semicolon after Ltd"
                    mandlst.append(hint)
                                       
#------------------------------type12.py-------------------------------------------------------------------------------------------------

                if b[i-1] in crules.flatno and b[i+1] in crules.wing :
                    hint="InCorrect Answer:A comma should be used to seperate two entities-flatno and wing."
                    mandlst.append(hint)
                if b[i-1] in crules.wing and b[i+1] in crules.societyname :
                    hint="InCorrect Answer:A comma should be used to seperate two entities-wing and societyname."
                    mandlst.append(hint)    
                if b[i-1] in crules.societyname and b[i+1] in crules.road :
                    hint="InCorrect Answer:A comma should be used to seperate two entities-societyname and road."
                    mandlst.append(hint)
                if b[i-1] in crules.road and b[i+1] in crules.street :
                    hint="InCorrect Answer:A comma should be used to seperate two entities-road and street."
                    mandlst.append(hint)
                if b[i-1] in crules.street and b[i+1] in crules.location :
                    hint="InCorrect Answer:A comma should be used to seperate two entities-street and location."
                    mandlst.append(hint)
                if b[i-1] in crules.new_landmark and b[i+1] in crules.city :
                    hint="InCorrect Answer:A comma should be used to seperate two entities-landmark and city."
                    mandlst.append(hint)    
                if b[i-1] in crules.location and b[i+1] in crules.city :
                    hint="InCorrect Answer::A comma should be used to seperate two entities-street and location."
                    mandlst.append(hint)
                if b[i-1] in crules.city and b[i+1] in crules.state :
                    hint="InCorrect Answer:A comma should be used to seperate two entities-street and location."
                    mandlst.append(hint)
                if b[i-1] in crules.state and b[i+1] in crules.pincode :
                    hint="InCorrect Answer:A comma should be used to seperate two entities-state and pincode."
                    mandlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.pronoun :
                    hint="InCorrect Answer:A comma should be used to seperate two clauses"
                    correctlst.append(hint)               
    #---------------------------------------------------<m> with Comma-------------------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]==","):
 #---------------------------type10comma.py----------------------------------------------------------------
                if b[i-1] =="Rs" and b[i+1].isdigit():
                    hint="InCorrect Answer:Remove the Comma and Put a FULLSTOP after the keyword {Rs]"
                    mandlst.append(hint)     
                phrase="".join(b)
                oned=re.findall("\d+",phrase)
                #print("oned",oned[0],oned[1])
                if b[i-3]=="Rs" and b[i-1]==oned[0] and b[i+1]==oned[1]:
                    hint="Correct Answer:Put a Comma after the first digit, if the number is above 999"
                    correctlst.append(hint)
                    
                if b[i-3]=="Rs" and b[i-1].isdigit() and c[-1]==" ":
                    hint="InCorrect Answer:Remove the Comma and END the sentence with a FULLSTOP"
                    mandlst.append(hint)
                    #-------------------------
                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
                    hint="Correct Answer:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                    correctlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="Correct Answer:A comma can be used to seperate an adjective phrase from the verbphrase"
                    correctlst.append(hint)
                if (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="Correct Answer:A comma should be used a relative clause follows the main subject."
                    correctlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="Correct Answer:A comma should be used a relative clause follows the main subject."
                    correctlst.append(hint)
                onounlst=list(set(crules.onoun) & set(b))
                #print(onounlst)
                if len(onounlst) > 2:
                    if (b[i-1] in crules.onoun and (b[i+1] in crules.article)):
                
                        hint="Correct Answer:A comma should be used after an object noun, when you are trying to list 2 or more nouns."
                        correctlst.append(hint)
                        #-----type11date.py-----------------------------------------------------------------
                if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                    hint="Correct Answer:A comma should be used after a date, when it is followed by a year."
                    correctlst.append(hint)
                if b[i-1]==year and c[-1]==",":
                    hint="InCorrect Answer:Remove the comma after "+b[i-1]+"and end the sentence with a FULLSTOP"
                    mandlst.append(hint)
                if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                    hint="Correct Answer:A comma should be used after a month, when it is followed by just a date(no year mentioned)."
                    correctlst.append(hint)
                if b[i-1]==str(parse(co,fuzzy=True).day) and c[-1]==",":
                    hint="InCorrect Answer:Remove the comma after "+b[i-1]+"and end the sentence with a FULLSTOP"
                    mandlst.append(hint)    
                
                if b[i-1] in crules.weekdays and b[i+1] in crules.months :
                    hint="Correct Answer:A comma should be used after a weekday, when it is followed by a month and date."
                    correctlst.append(hint) 
                if b[i-3]==str(parse(co,fuzzy=True).day) and b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                    hint="Correct Answer:A comma needed just after the month, " +b[i-1]+"  if the date format is date-month-year"
                    mandlst.append(hint)
                                  
#------------------------------type12.py-------------------------------------------------------------------------------------------------

                if b[i-1] in crules.flatno and b[i+1] in crules.wing :
                    hint="Correct Answer:A comma should be used to seperate two entities-flatno and wing."
                    correctlst.append(hint)
                if b[i-1] in crules.wing and b[i+1] in crules.societyname :
                    hint="Correct Answer:A comma should be used to seperate two entities-wing and societyname."
                    correctlst.append(hint)    
                if b[i-1] in crules.societyname and b[i+1] in crules.road :
                    hint="Correct Answer:A comma should be used to seperate two entities-societyname and road."
                    correctlst.append(hint)
                if b[i-1] in crules.road and b[i+1] in crules.street :
                    hint="Correct Answer:A comma should be used to seperate two entities-road and street."
                    correctlst.append(hint)
                if b[i-1] in crules.street and b[i+1] in crules.location :
                    hint="Correct Answer:A comma should be used to seperate two entities-street and location."
                    correctlst.append(hint)
                if b[i-1] in crules.new_landmark and b[i+1] in crules.city :
                    hint="Correct Answer:A comma should be used to seperate two entities-landmark and city."
                    correctlst.append(hint)    
                if b[i-1] in crules.location and b[i+1] in crules.city :
                    hint="Correct Answer:A comma should be used to seperate two entities-street and location."
                    correctlst.append(hint)
                if b[i-1] in crules.city and b[i+1] in crules.state :
                    hint="Correct Answer:A comma should be used to seperate two entities-street and location."
                    correctlst.append(hint)
                if b[i-1] in crules.state and b[i+1] in crules.pincode :
                    hint="Correct Answer:A comma should be used to seperate two entities-state and pincode."
                    correctlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.pronoun :
                    hint="Correct Answer:A comma should be used to seperate two clauses"
                    correctlst.append(hint)
    #---------------------------------------------------------type6.py---------------------------------------------------------------------------
                if b[i-1] in crules.conjadv and b[i+1] in crules.pronoun:
                    
                    hint="Correct Answer:A Comma is needed after the conjunctive adverb.", b[i-1]
                
                    correctlst.append(hint) 
                    
               
                
                if (b[i-1] in crules.onoun) and c[-1]==",":
                    
                    hint="InCorrect Answer.Remove the comma at the end  and add a Fullstop"
                
                    mandlst.append(hint)
                if(b[i-1] in crules.pronoun) and c[-1]==",":
                    
                    hint="InCorrect Answer.Remove the comma at the end and add a FULLSTOP"
                
                    mandlst.append(hint)

                if b[i-1] ==crules.onoun and b[i+1]==crules.pronoun.capitalize():
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                    correctlst.append(hint)
       #-----------------------------------------type12stay.py------------------------------------------------

                    
                if b[i-1]==crules.title and b[i+1]== crules.title:
                    hint="Incorrect Answer.NO need of a comma after a title"
                    mandlst.append(hint)
                name=['Esmail Bagani']
                
                for i in name:
                    name1=i.split(" ")
                if b[i-1]==crules.title and b[i+1]== crules.name1[0]:
                    hint="InCorrect Answer.No need of a comma between a title and a name"
                    mandlst.append(hint)
                if b[i-1]==crules.title and b[i+1]== crules.name1[1]:
                    hint="InCorrect Answer.No need of a comma between a title and a name"
                    mandlst.append(hint)
                if b[i-1].isaplha() and b[i+1]==name1[0] or name1[1]:
                    hint="InCorrect Answer.No need of a comma between a tiInitial and a name"
                    mandlst.append(hint)
                if b[i-1]==crules.pincode and b[i+1]==None:
                    hint="InCorrect Answer.No need of a comma at the end of the sentence"
                    mandlst.append(hint)
                if b[i-1] in crules.onamelst and b[i+1]=="The":
                    hint="InCorrect Answer.No need of a comma between two sentences"
                    mandlst.append(hint)
                if b[i-1]=="Pvt" and b[i+1]=="Ltd":
                    hint="InCorrect Answer.No need of a comma between Pvt and Ltd..Is a single entity"
                    mandlst.append(hint)
                if b[i-1]=="Ltd":
                    hint="InCorrect Answer.No need of a comma after Ltd"
                    mandlst.append(hint)
    
    #---------------------------------------------------<m> with Fullstop--------------------------------------------------------------------------        
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                #-------------------------------type11date.py------------------------------------------------------------
                if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                    hint="InCorrect Answer:Remove the FULLSTOP after "+b[i-1]+" and put a comma"
                    mandlst.append(hint)
                
                if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                    hint="InCorrect Answer:Remove the FULLSTOP after "+b[i-1]+" and put a comma when it is followed by just a date(no year mentioned)."
                    mandlst.append(hint)
                if b[i-1]==str(parse(co,fuzzy=True).day) and c[-1]==".":
                    hint="Correct Answer:Sentence should be ended with a FULLSTOP"
                    correctlst.append(hint)    
               
                if b[i-1]==str(str(parse(co, fuzzy=True).year)) and c[-1]==".":
                    hint="Correct Answer:Sentence should be ended with a FULLSTOP"
                    correctlst.append(hint)        
                if b[i-1] in crules.weekdays and b[i+1] in crules.months :
                    hint="InCorrect Answer:Remove the FULLSTOP after "+b[i-1]+" and put a comma after the weekday, when it is followed by a month and date."
                    mandlst.append(hint)

                if b[i-3]==str(parse(co,fuzzy=True).day) and b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                    hint="InCorrect Answer:Remove the fullstop and put a comma just after the month, " +b[i-1]+"  if the date format is date-month-year"
                    mandlst.append(hint)    
                #---------------------------type10comma.py----------------------------------------------------------------
                if b[i-1] =="Rs" and b[i+1].isdigit():
                    hint="Correct Answer:Put a FULLSTOP after the keyword {Rs]"
                    correctlst.append(hint)     
                phrase="".join(b)
                oned=re.findall("\d+",phrase)
                #print("oned",oned[0],oned[1])
                if b[i-1]==oned[0] and b[i+1]==oned[1]:
                    hint="Incorrect Answer:HINT:Remove the Fullstop and Put a Comma after" + " "+b[i-1]
                    mandlst.append(hint)
                    
                if b[i-1].isdigit() and c[-1]==" ":
                    hint="Correct Answer:END a sentence with a FULLSTOP"
                    correct.append(hint) 

                
                  #----------------------------type6.py-----------------------------------------------------------------------------------
                if b[i-1] in crules.conjadv and b[i+1] in crules.pronoun:
                    
                    hint="InCorrect Answer:Hint: Put a Comma after conjunctive adverb.", b[i-1]
                
                    mandlst.append(hint) 
                    
               
                if b[i-1] in crules.onoun and b[i]=="<m>":
                    
                    hint="Correct Answer.End the sentence with FULLSTOP."
                
                    mandlst.append(hint)  
                    
                if (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="InCorrect Answer:Hint:Remove the FULLSTOP after the noun",b[i-1]
                    mandlst.append(hint)
                   
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="InCorrect Answer:Hint:Remove the FULLSTOP after the common noun",b[i-1]
                    mandlst.append(hint)
                    
                if b[i-1] in crules.title and b[i+1] in crules.snoun:
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always put a period/fullstop after a title"
                
                    correctlst.append(hint)
                    
               
                if(b[i-1] in crules.pronoun) and c[-1]==".":
                    
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                
                    correctlst.append(hint)
                onounlst=list(set(crules.onoun) & set(b))    
                if len(onounlst) > 2:
                    if (b[i-1] in crules.onoun and (b[i+1] in crules.article)):
                
                        hint="INCorrect Answer:Remove the fullstop as, a comma should be used after an object noun "+b[i-1]
                        mandlst.append(hint) 
               
#-----------------------------type12stay.py------------------------------------------------------------------------
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
               

                                       
#------------------------------type12.py-------------------------------------------------------------------------------------------------

                if b[i-1] in crules.flatno and b[i+1] in crules.wing :
                    hint="InCorrect Answer:A comma should be used to seperate two entities-flatno and wing."
                    mandlst.append(hint)
                if b[i-1] in crules.wing and b[i+1] in crules.societyname :
                    hint="InCorrect Answer:A comma should be used to seperate two entities-wing and societyname."
                    mandlst.append(hint)    
                if b[i-1] in crules.societyname and b[i+1] in crules.road :
                    hint="InCorrect Answer:A comma should be used to seperate two entities-societyname and road."
                    mandlst.append(hint)
                if b[i-1] in crules.road and b[i+1] in crules.street :
                    hint="InCorrect Answer:A comma should be used to seperate two entities-road and street."
                    mandlst.append(hint)
                if b[i-1] in crules.street and b[i+1] in crules.location :
                    hint="InCorrect Answer:A comma should be used to seperate two entities-street and location."
                    mandlst.append(hint)
                if b[i-1] in crules.new_landmark and b[i+1] in crules.city :
                    hint="InCorrect Answer:A comma should be used to seperate two entities-landmark and city."
                    mandlst.append(hint)    
                if b[i-1] in crules.location and b[i+1] in crules.city :
                    hint="InCorrect Answer::A comma should be used to seperate two entities-street and location."
                    mandlst.append(hint)
                if b[i-1] in crules.city and b[i+1] in crules.state :
                    hint="InCorrect Answer:A comma should be used to seperate two entities-street and location."
                    mandlst.append(hint)
                if b[i-1] in crules.state and b[i+1] in crules.pincode :
                    hint="InCorrect Answer:A comma should be used to seperate two entities-state and pincode."
                    mandlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.pronoun :
                    hint="InCorrect Answer:A comma should be used to seperate two clauses"
                    mandlst.append(hint)         

   
 #--------------------------------------------------------<w> with comma-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==","):
                 #-----------------------------type11date.py---------------------------------------------------------------------------------------------------
                
            
                if b[i-1] in crules.prep and b[i+1] in crules.months:
                    hint="Incorrect Ans, HINT:Remove the comma after the preposition "+b[i-1]+" when it is followed by a month"
                    hintlst.append(hint)
                   
                if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                    hint="Incorrect Ans, HINT:Remove the comma after the month"+b[i-1]+" format - month followed by a date"
                    hintlst.append(hint)
                if b[i-1]  in crules.snoun and b[i+1] in crules.vbz:
                    hint="Incorrect Ans, HINT:Remove the comma after the noun"+b[i-1]+" when it is followed by a ['is','was']"
                    hintlst.append(hint)
                if b[i-1] in crules.vbz and b[i+1] in crules.verb:
                    hint="Incorrect Ans, HINT:Remove the comma after the verbtobe ['is','was'] ",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in crules.prep:
                    hint="Incorrect Ans, HINT:Remove the comma after the verb ",b[i-1],"when it is followed by a preposition"
                    hintlst.append(hint)
                if b[i-1] in crules.prep and b[i+1] in crules.weekdays:
                    hint="Incorrect Ans, HINT:Remove the comma after the preposition ",b[i-1]," when it is followed by a weekday"
                if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1] in crules.months  :
                    hint="Incorrect Ans, HINT:Remove the comma after the date", b[i-1]," when it is followed by a month and a year if the date format is [15 March 2003]"
                    hintlst.append(hint)
                      
                if b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)):
                    hint="Incorrect Ans, HINT:Remove the comma after the month", b[i-1],"  when it is followed by a year if the date format is [15 March 2003]" 
                    hintlst.append(hint)
                #--------------type6.py------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
                  hint="Read The manual again, HINT:Remove the COMMA after the adjective",b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules. pronoun and b[i+1] in crules.hverb:
                  hint="Read The manual again, HINT:Remove the comma after the pronoun",b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules.hverb and b[i+1] in crules.neg:
                  hint="Read The manual again, HINT:Remove the comma after a helping verb like (can,could)",b[i-1]
                  hintlst.append(hint)
               
                if b[i-1] in crules.neg and b[i+1] in crules.verb:
                  hint="Read The manual again, HINT:Remove the comma after after the negation",b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
                  hint="Read The manual again, HINT:Remove the comma after ",b[i-1]
                  hintlst.append(hint)  
                #--------------type3.py-----------------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.adj and b[i+1] in crules.cnoun:
                    hint="Read The manual again, HINT:Remove the comma after adjective",b[i-1]
                    hintlst.append(hint)
                

                if b[i-1] in crules.article and b[i+1] in crules.adj:
                    hint="Read The manual again, HINT:Remove the comma after the article",b[i-1]
                    hintlst.append(hint)
                 
                if b[i-1] in crules.verb and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:Remove the comma after a verb",b[i-1]
                    hintlst.append(hint)
               
                
                if b[i-1] in crules.cordconj and b[i+1] in crules.article:
                    hint="Read The manual again, HINT:Remove the comma after the conjunction",b[i-1]
                    hintlst.append(hint)
                #-----------------------------type4.py--------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.hverb and b[i+1] in crules.verb:
                    hint="Incorrect Answer, HINT: Remove the comma after the helping verb",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.cnoun and b[i+1] in crules.hverb:
                    hint="Incorrect Answer, HINT: Remove the comma after the common noun",b[i-1]
                    hintlst.append(hint)        
                if b[i-1] in crules.article and b[i+1] in crules.onoun:
                    hint="Incorrect Answer, HINT: Remove the comma after the article",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.cordconj:
                    hint="Incorrect Answer, HINT: Remove the comma after the noun",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.cordconj and b[i+1] in crules.article:
                    hint="Incorrect Answer, HINT: Remove the comma after the conjunction",b[i-1]
                    hintlst.append(hint)
            #-----------------------------type10comma.py---------------------------------------------------------------------------------------------------

                if b[i-1] in crules.snoun and b[i+1] in crules.verb:
                    hint="Incorrect Answer, HINT: Remove the comma after the noun",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
                    hint="Incorrect Answer, HINT: Remove the comma after the verb",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.pronoun and b[i+1] in crules.adj:
                    hint="Incorrect Answer, HINT: Remove the comma after the pronoun",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
                    hint="Incorrect Answer, HINT: Remove the comma after the adjective",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1]=="Rs":
                    hint="Incorrect Answer, HINT: Remove the comma after the verb",b[i-1]
                    hintlst.append(hint)    
                     
                phrase="".join(b)
                oned=re.findall("\d+",phrase)
                #print("oned",oned[0],oned[1])
               
                if b[i-1]==oned[1] and b[i+1]==crules.prep:
                    hint="Incorrect Answer, HINT:Remove the comma after  "+b[i-1]
                    hintlst.append(hint)
                                           
              
                if b[i-1] in crules.onoun and b[i+1] in crules.prep:
                    hint="Incorrect Answer, HINT:Remove the comma after the noun"+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.prep and b[i+1] in crules.pronoun:
                    hint="Incorrect Answer, HINT:Remove the comma after the preposition "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.prep and b[i+1]=="Rs":
                    hint="Incorrect Answer, HINT: Remove the comma after the preposition",b[i-1]
                    hintlst.append(hint)

                                                            
           #-----------------------------type12.py---------------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.snoun and b[i+1] in crules.verb1:
                    hint="Read the manual again, HINT:No need of a comma between a noun and a verb"
                if b[i-1] in crules.verb1 and b[i+1] in crules.prep:
                    hint="Read the manual again, HINT:No need of a comma between a verb and a prep"
                if b[i-1] in crules.prep and b[i+1] in crules.article:
                    hint="Read the manual again, HINT:No need of a comma between a prep and an article"
                if b[i-1] in crules.article and b[i+1] in crules.onoun:
                    hint="Read the manual again, HINT:No need of a comma between an article and a noun"               
                    
                if b[i-1] in crules.pronoun1 and b[i+1]=="address":
                    hint="Read the manual again, HINT:No need of a comma between a noun and the word 'address'"
                if b[i-1] =="address" and b[i+1] in crules.vbz:
                    hint="Read the manual again, HINT:No need of a comma between the word 'address' and [is/was]"         
                if b[i-1] in crules.vbz and b[i+1]=="C/O":
                    hint="Read the manual again, HINT:No need of a comma after [is/was]"
                if b[i-1]=="C/O" and b[i+1] in crules.title:
                    hint="Read the manual again, HINT:No need of a comma addresstag [C/O,S/O]"

                name=['Esmail Bagani']
                
                for i in name:
                    name1=i.split(" ")
                  
                if b[i-1]==name1[0] and b[i+1]==name1[1]:
                    hint="Read the manual again, HINT:Don't split the name with a comma"
                if b[i-1]==name1[1] and b[i+1]==name1[0]:
                    hint="Read the manual again, HINT:Don't split the name with a comma"
                    
                if b[i-1] in crules.societyl and b[i+1] in crules.societyl:
                    hint="Read the manual again, HINT:Don't split the society name with a comma"
                if b[i-1] in crules.roadl and b[i+1] in crules.roadl:
                    hint="Read the manual again, HINT:Don't split the road name with a comma"
                if b[i-1] in crules.statel and b[i+1] in crules.statel:
                    hint="Read the manual again, HINT:Don't split the state name with a comma"
                
#-----------------------------type12stay.py-----------------------------------
                if b[i-1] in crules.verb1 and b[i+1] in crules.article:
                    hint="Read the manual again, HINT:No need of a comma between a verb and an article.."
                if b[i-1] in crules.article and b[i+1]=="organisation"+".":
                    hint="Read the manual again, HINT:No need of a comma between a aricle and a noun.."
                
                if b[i-1] =="The" and b[i+1]=="name":
                    hint="Read the manual again, HINT:No need of a comma between a determiner and the keyword name .."
                
                if b[i-1] =="name" and b[i+1]=="of":
                    hint="Read the manual again, HINT:No need of a comma between and keyword name and a preposition .."
                if b[i-1] =="of" and b[i+1] in crules.det:
                    hint="Read the manual again, HINT:No need of a comma between a preposition and a determiner"
                if b[i-1] in det and b[i+1] in crules.onoun:
                    hint="Read the manual again, HINT:No need of a comma between a determiner and the keyword name .."
                if b[i-1] in crules.onoun and b[i+1] in crules.vbz:
                    hint="Read the manual again, HINT:No need of a comma between a noun and [is/was] .."
                if b[i-1] in crules.vbz and b[i+1] in crules.onamelst:
                    hint="Read the manual again, HINT:No need of a comma between [is/was] and an object name like building name,name of a person etc. "
                    hintlst.append(hint)
                if b[i-1] in crules.onamelst and b[i+1] in crules.onamelst:
                    hint="Read the manual again, HINT:There is no listing of items here, it has to be considered as a single entity..so please avoid comma here."
                    hintlst.append(hint)
                if b[i-1]=="The" and b[i+1]=="address":
                    hint="Read the manual again, HINT:No need of a comma between a determiner and the a propernoun 'address'"
                    hintlst.append(hint)
                if b[i-1] =="address" and b[i+1] in crules.vbz:
                    hint="Read the manual again, HINT:No need of a comma between the word 'address' and [is/was]"
                    hintlst.append(hint)
                if b[i-1] in crules.vbz and b[i+1] in crules.new_landmark:
                    hint="Read the manual again, HINT:No need of a comma after [is/was]"
                    hintlst.append(hint)
                if b[i-1] in crules.new_landmark and b[i+1] in crules.new_landmark:
                    hint="Read the manual again, HINT:There is no listing of items here, it has to be considered as a single entity..so please avoid comma here."
                    hintlst.append(hint)
                if b[i-1].isalpha() and b[i+1].isalpha():
                    hint="Read the manual again, HINT:No need of a comma here as it is an abbreviation"
                    hintlst.append(hint)
                
 #--------------------------------quotneg.py----------------------------------------------------------          
##                if b[i-1] in crules.verb and b[i+1] in crules.prep:
##                    hint="Read the manual again, HINT:No need of a comma between a verb and a preposition"
##                    hintlst.append(hint)
##                if b[i-1] in crules.prep and b[i+1] in crules.snoun:
##                    hint="Read the manual again, HINT:No need of a comma between a preposition and a noun"
##                    hintlst.append(hint)     
##                
###-----------------------------------type1.py----------------------------------------------------------
##                if b[i-1] in crules.cnoun and b[i+1] in crules.verb:
##                    hint="Read The manual again, HINT:No need to put a comma after a common noun especially when there is no enumeration..."
##                    hintlst.append(hint)
##                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
##                    hint="Read The manual again, HINT:No need to seperate a adjective phrase with a comma"
##                    hintlst.append(hint)
##                if b[i-1] in crules.onoun and b[i+1] in crules.madverb:
##                    hint="Read The manual again, HINT:Noun when followed by a modifying adverb,don't put a comma in between"
##                    hintlst.append(hint)
##                if b[i-1] in crules.madverb and b[i+1] in crules.adverb:
##                    hint="Read The manual again, HINT:Modifying adverb like extremely,very etc shoud not be seperated from main adverbs using a comma"
##                    hintlst.append(hint)
###--------------------------------compound.py----------------------------------------
##                if b[i-1] in crules.cordconj and b[i+1] in crules.verb:
##                    hint="Read The manual again, HINT:Avoid Comma after a Conjunction like [and] or [but]"
##                    hintlst.append(hint)
##                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
##                    hint="Read The manual again, HINT:No need to add a comma after a verb, when it is followed by a neuter pronoun(e.g. it)"
##                    hintlst.append(hint)
###--------------------------------inrocomma.py---------------------------------------------------------------------------------------------------------------
##                if b[i-1] in crules.intro-words and b[i+1] in crules.snoun:
##                    hint="Read The manual again, HINT:Avoid Comma after Introductory wirds like [while/Although] etc."
##                    hintlst.append(hint)
##                if b[i-1] in crules.snoun and b[i+1] in crules.vbz:
##                    hint="Read The manual again, HINT:No need to add a comma after a noun, when it is followed by [is/was]"
##                    hintlst.append(hint)
##                if b[i-1] in crules.vbz and b[i+1] in crules.verbing:
##                    hint="Read The manual again, HINT:No need to add a comma after [is/was], when it is followed by a verb"
##                    hintlst.append(hint)
##                if b[i-1] in crules.verbing and b[i+1] in crules.article:
##                    hint="Read The manual again, HINT:No need to add a comma after a verb ,in a verbphrase"
##                    hintlst.append(hint)
##                  
##                if b[i-1] in crules.pronoun and b[i+1] in crules.verb:
##                    hint="Read The manual again, HINT:No need to add a comma after a pronoun"
##                    
##                    hintlst.append(hint)
##               
                    
#--------------------------------------------------------<w> with FULLSTOP-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]=="."):
                
                   #-----------------------------type4.py--------------------------------------------
                if b[i-1] in crules.hverb and b[i+1] in crules.verb:
                    hint="Incorrect Answer:, HINT: Remove the FULLSTOP after the helping verb",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.cnoun and b[i+1] in crules.hverb:
                    hint="Incorrect Answer:, HINT: Remove the FULLSTOP after the helping verb",b[i-1]
                    hintlst.append(hint)        
                if b[i-1] in crules.article and b[i+1] in crules.onoun:
                    hint="Incorrect Answer:, HINT: Remove the FULLSTOP after the article",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.cordconj:
                    hint="Incorrect Answer:, HINT: Remove the FULLSTOP after the object noun",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.cordconj and b[i+1] in crules.article:
                    hint="Incorrect Answer:, HINT: Remove the FULLSTOP after the conjunction",b[i-1]
                    hintlst.append(hint)
               #--------------type6.py------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
                  hint="Read The manual again, HINT:Remove the FULLSTOP after the adjective",b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules. pronoun and b[i+1] in crules.hverb:
                  hint="Read The manual again, HINT:Remove the FULLSTOP after the pronoun",b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules.hverb and b[i+1] in crules.neg:
                  hint="Read The manual again, HINT:Remove the FULLSTOP after a helping verb like (can,could)",b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules. hverb and b[i+1] in crules.verb:
                  hint="Read The manual again, HINT:Remove the FULLSTOP after a helping verb ",b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules.neg and b[i+1] in crules.verb:
                  hint="Read The manual again, HINT:Remove the FULLSTOP after after the negation",b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
                  hint="Read The manual again, HINT:Remove the FULLSTOP after ",b[i-1]
                  hintlst.append(hint)  
                 #-----------------------------type10comma.py---------------------------------------------------------------------------------------------------

                if b[i-1] in crules.snoun and b[i+1] in crules.verb:
                    hint="Incorrect Answer, HINT: Remove the fullstop after the noun",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
                    hint="Incorrect Answer, HINT: Remove the fullstop after the verb",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.pronoun and b[i+1] in crules.adj:
                    hint="Incorrect Answer, HINT: Remove the fullstop after the pronoun",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
                    hint="Incorrect Answer, HINT: Remove the fullstop after the adjective",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1]=="Rs":
                    hint="Incorrect Answer, HINT: Remove the fullstop after the verb",b[i-1]
                    hintlst.append(hint)    
                     
                phrase="".join(b)
                oned=re.findall("\d+",phrase)
                #print("oned",oned[0],oned[1])
               
                if b[i-1]==oned[1] and b[i+1]==crules.prep:
                    hint="Incorrect Answer, HINT:Remove the fullstop after  "+b[i-1]
                    hintlst.append(hint)
                                           
              
                if b[i-1] in crules.onoun and b[i+1] in crules.prep:
                    hint="Incorrect Answer, HINT:Remove the fullstop after the noun"+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.prep and b[i+1] in crules.pronoun:
                    hint="Incorrect Answer, HINT:Remove the fullstop after the preposition "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.prep and b[i+1]=="Rs":
                    hint="Incorrect Answer, HINT: Remove the fullstop after the preposition",b[i-1]
                    hintlst.append(hint)

                       #-----------------type11date.py--------------------------------
               
                if b[i-1] in crules.onoun and b[i+1] in crules.prep:
                    hint="Incorrect Answer, HINT:Remove the fullstop after the object noun",b[i-1]
                    hintlst.append(hint) 
               
                if b[i-1] in crules.prep and b[i+1] in crules.months:
                    hint="Incorrect Answer, HINT:Remove the fullstop after the prep",b[i-1]," when it is followed by a month"
                    hintlst.append(hint) 
                if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                    hint="Incorrect Answer, HINT:Remove the fullstop after the month",b[i-1],"when it is followed by a date"
                    hintlst.append(hint) 
                if b[i-1] in crules.snoun and b[i+1] in crules.vbz:
                    hint="Incorrect Answer, HINT:Remove the fullstop after the noun",b[i-1]," if it is followed by a ['is','was']"
                    hintlst.append(hint) 
                if b[i-1] in crules.vbz and b[i+1] in crules.verb:
                    hint="Incorrect Answer, HINT:Remove the fullstop after ['is','was']",b[i-1]," when it is followed by a verb"
                    hintlst.append(hint) 
                if b[i-1] in crules.verb and b[i+1] in crules.prep:
                    hint="Incorrect Answer, HINT:Remove the fullstop after the verb",b[i-1]," when it is followed by a preposition"
                    hintlst.append(hint) 
                if b[i-1] in crules.prep and b[i+1] in crules.weekdays:
                    hint="Incorrect Answer, HINT:Remove the fullstop after the prep",b[i-1]," when it is followed by a weekday"
                    hintlst.append(hint) 
                if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1] in crules.months and b[i+2]==str(str(parse(co, fuzzy=True).year)):
                    hint="Incorrect Answer, HINT:Remove the fullstop after the date",b[i-1]," when it is followed by a month and a year if the date format is [15 March 2003]"
                    hintlst.append(hint) 
                if b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)) and b[i+2]==None:
                    hint="Incorrect Answer, HINT:Remove the fullstop after the month",b[i-1]," when it is followed by a year if the date format is [15 March 2003]"
                    hintlst.append(hint)       
                
                                                            
           #-----------------------------type12.py---------------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.snoun and b[i+1] in crules.verb1:
                    hint="Read the manual again, HINT:No need of a fullstop between a noun and a verb"
                if b[i-1] in crules.verb1 and b[i+1] in crules.prep:
                    hint="Read the manual again, HINT:No need of a fullstop between a verb and a prep"
                if b[i-1] in crules.prep and b[i+1] in crules.article:
                    hint="Read the manual again, HINT:No need of a fullstop between a prep and an article"
                if b[i-1] in crules.article and b[i+1] in crules.onoun:
                    hint="Read the manual again, HINT:No need of a fullstop between an article and a noun"               
                    
                if b[i-1] in crules.pronoun1 and b[i+1]=="address":
                    hint="Read the manual again, HINT:No need of a fullstop between a noun and the word 'address'"
                if b[i-1] =="address" and b[i+1] in crules.vbz:
                    hint="Read the manual again, HINT:No need of a fullstop between the word 'address' and [is/was]"         
                if b[i-1] in crules.vbz and b[i+1]=="C/O":
                    hint="Read the manual again, HINT:No need of a cfullstopomma after [is/was]"
                if b[i-1]=="C/O" and b[i+1] in crules.title:
                    hint="Read the manual again, HINT:No need of a fullstop addresstag [C/O,S/O]"

                name=['Esmail Bagani']
                
                for i in name:
                    name1=i.split(" ")
                  
                if b[i-1]==name1[0] and b[i+1]==name1[1]:
                    hint="Read the manual again, HINT:Don't split the name with a fullstop"
                if b[i-1]==name1[1] and b[i+1]==name1[0]:
                    hint="Read the manual again, HINT:Don't split the name with a fullstop"
                    
                if b[i-1] in crules.societyl and b[i+1] in crules.societyl:
                    hint="Read the manual again, HINT:Don't split the society name with a fullstop"
                if b[i-1] in crules.roadl and b[i+1] in crules.roadl:
                    hint="Read the manual again, HINT:Don't split the road name with a fullstop"
                if b[i-1] in crules.statel and b[i+1] in crules.statel:
                    hint="Read the manual again, HINT:Don't split the state name with a fullstop"
                
#-----------------------------type12stay.py-----------------------------------
                if b[i-1] in crules.verb1 and b[i+1] in crules.article:
                    hint="Read the manual again, HINT:No need of a fullstop between a verb and an article.."
                if b[i-1] in crules.article and b[i+1]=="organisation"+".":
                    hint="Read the manual again, HINT:No need of a fullstop between a aricle and a noun.."
                
                if b[i-1] =="The" and b[i+1]=="name":
                    hint="Read the manual again, HINT:No need of a fullstop between a determiner and the keyword name .."
                
                if b[i-1] =="name" and b[i+1]=="of":
                    hint="Read the manual again, HINT:No need of a fullstop between and keyword name and a preposition .."
                if b[i-1] =="of" and b[i+1] in crules.det:
                    hint="Read the manual again, HINT:No need of a fullstop between a preposition and a determiner"
                if b[i-1] in det and b[i+1] in crules.onoun:
                    hint="Read the manual again, HINT:No need of a fullstop between a determiner and the keyword name .."
                if b[i-1] in crules.onoun and b[i+1] in crules.vbz:
                    hint="Read the manual again, HINT:No need of a fullstop between a noun and [is/was] .."
                if b[i-1] in crules.vbz and b[i+1] in crules.onamelst:
                    hint="Read the manual again, HINT:No need of a fullstop between [is/was] and an object name like building name,name of a person etc. "
                    hintlst.append(hint)
                if b[i-1] in crules.onamelst and b[i+1] in crules.onamelst:
                    hint="Read the manual again, HINT:There is no  of items here, it has to be considered as a single entity..so please avoid fullstop here."
                    hintlst.append(hint)
                if b[i-1]=="The" and b[i+1]=="address":
                    hint="Read the manual again, HINT:No need of a fullstop between a determiner and the a propernoun 'address'"
                    hintlst.append(hint)
                if b[i-1] =="address" and b[i+1] in crules.vbz:
                    hint="Read the manual again, HINT:No need of a fullstop between the word 'address' and [is/was]"
                    hintlst.append(hint)
                if b[i-1] in crules.vbz and b[i+1] in crules.new_landmark:
                    hint="Read the manual again, HINT:No need of a fullstop after [is/was]"
                    hintlst.append(hint)
                if b[i-1] in crules.new_landmark and b[i+1] in crules.new_landmark:
                    hint="Read the manual again, HINT:There is no listing of items here, it has to be considered as a single entity..so please avoid fullstop here."
                    hintlst.append(hint)
                if b[i-1].isalpha() and b[i+1].isalpha():
                    hint="Read the manual again, HINT:No need of a fullstop here as it is an abbreviation"
                    hintlst.append(hint)
              

#--------------------------------------------------------<w> with SEMICOLON-------------------------------------------------------------------------------------             
        for i in range(0,len(b)) :
          
            if (b[i]=="<w>" and c[i]==";"):
                  #-----------------------------type4.py--------------------------------------------
                if b[i-1] in crules.hverb and b[i+1] in crules.verb:
                    hint="Incorrect Answer:, HINT: Remove the SEMICOLON after the helping verb",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.cnoun and b[i+1] in crules.hverb:
                    hint="Incorrect Answer:, HINT: Remove the SEMICOLON after the helping verb",b[i-1]
                    hintlst.append(hint)        
                if b[i-1] in crules.article and b[i+1] in crules.onoun:
                    hint="Incorrect Answer:, HINT: Remove the SEMICOLON after the helping verb",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.cordconj:
                    hint="Incorrect Answer:, HINT: Remove the SEMICOLON after the helping verb",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.cordconj and b[i+1] in crules.article:
                    hint="Incorrect Answer:, HINT: Remove the SEMICOLON after the helping verb",b[i-1]
                    hintlst.append(hint)
                #--------------type6.py------------------------------------------------------------------------------------------------------
##                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
##                  hint="Read The manual again, HINT:Remove the SEMICOLON after the adjective",b[i-1]
##                  hintlst.append(hint)
                if b[i-1] in crules. pronoun and b[i+1] in crules.hverb:
                  hint="Read The manual again, HINT:Remove the SEMICOLON after the pronoun",b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules.hverb and b[i+1] in crules.neg:
                  hint="Read The manual again, HINT:Remove the SEMICOLON after a helping verb like (can,could)",b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules. hverb and b[i+1] in crules.verb:
                  hint="Read The manual again, HINT:Remove the SEMICOLON after a helping verb ",b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules.neg and b[i+1] in crules.verb:
                  hint="Read The manual again, HINT:Remove the SEMICOLON after after the negation",b[i-1]
                  hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
                  hint="Read The manual again, HINT:Remove the SEMICOLON after ",b[i-1]
                  hintlst.append(hint)  
                
                 #-----------------------------type10comma.py---------------------------------------------------------------------------------------------------

                if b[i-1] in crules.snoun and b[i+1] in crules.verb:
                    hint="Incorrect Answer, HINT: Remove the semicolon after the noun",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1] in crules.pronoun:
                    hint="Incorrect Answer, HINT: Remove the semicolon after the verb",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.pronoun and b[i+1] in crules.adj:
                    hint="Incorrect Answer, HINT: Remove the semicolon after the pronoun",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.adj and b[i+1] in crules.onoun:
                    hint="Incorrect Answer, HINT: Remove the semicolon after the adjective",b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.verb and b[i+1]=="Rs":
                    hint="Incorrect Answer, HINT: Remove the semicolon after the verb",b[i-1]
                    hintlst.append(hint)    
                     
                phrase="".join(b)
                oned=re.findall("\d+",phrase)
                #print("oned",oned[0],oned[1])
               
                if b[i-1]==oned[1] and b[i+1]==crules.prep:
                    hint="Incorrect Answer, HINT:Remove the semicolon after  "+b[i-1]
                    hintlst.append(hint)
                                           
              
                if b[i-1] in crules.onoun and b[i+1] in crules.prep:
                    hint="Incorrect Answer, HINT:Remove the semicolon after the noun"+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.prep and b[i+1] in crules.pronoun:
                    hint="Incorrect Answer, HINT:Remove the semicolon after the preposition "+b[i-1]
                    hintlst.append(hint)
                if b[i-1] in crules.prep and b[i+1]=="Rs":
                    hint="Incorrect Answer, HINT: Remove the semicolon after the preposition",b[i-1]
                    hintlst.append(hint)

                         #-----------------type11date.py--------------------------------
               
                if b[i-1] in crules.onoun and b[i+1] in crules.prep:
                    hint="Incorrect Answer, HINT:Remove the semicolon after the object noun",b[i-1]
                    hintlst.append(hint) 
               
                if b[i-1] in crules.prep and b[i+1] in crules.months:
                    hint="Incorrect Answer, HINT:Remove the semicolon after the prep",b[i-1]," when it is followed by a month"
                    hintlst.append(hint) 
                if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                    hint="Incorrect Answer, HINT:Remove the semicolon after the month",b[i-1],"when it is followed by a date"
                    hintlst.append(hint) 
                if b[i-1] in crules.snoun and b[i+1] in crules.vbz:
                    hint="Incorrect Answer, HINT:Remove the semicolon after the noun",b[i-1]," if it is followed by a ['is','was']"
                    hintlst.append(hint) 
                if b[i-1] in crules.vbz and b[i+1] in crules.verb:
                    hint="Incorrect Answer, HINT:Remove the semicolon after ['is','was']",b[i-1]," when it is followed by a verb"
                    hintlst.append(hint) 
                if b[i-1] in crules.verb and b[i+1] in crules.prep:
                    hint="Incorrect Answer, HINT:Remove the semicolon after the verb",b[i-1]," when it is followed by a preposition"
                    hintlst.append(hint) 
                if b[i-1] in crules.prep and b[i+1] in crules.weekdays:
                    hint="Incorrect Answer, HINT:Remove the semicolon after the prep",b[i-1]," when it is followed by a weekday"
                    hintlst.append(hint) 
                if b[i-1]==str(parse(co,fuzzy=True).day) and b[i+1] in crules.months and b[i+2]==str(str(parse(co, fuzzy=True).year)):
                    hint="Incorrect Answer, HINT:Remove the semicolon after the date",b[i-1]," when it is followed by a month and a year if the date format is [15 March 2003]"
                    hintlst.append(hint) 
                if b[i-1] in crules.months and b[i+1]==str(str(parse(co, fuzzy=True).year)) and b[i+2]==None:
                    hint="Incorrect Answer, HINT:Remove the semicolon after the month",b[i-1]," when it is followed by a year if the date format is [15 March 2003]"
                    hintlst.append(hint)        
     #-----------------------------type12.py---------------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.snoun and b[i+1] in crules.verb1:
                    hint="Read the manual again, HINT:No need of a semicolon between a noun and a verb"
                if b[i-1] in crules.verb1 and b[i+1] in crules.prep:
                    hint="Read the manual again, HINT:No need of a semicolon between a verb and a prep"
                if b[i-1] in crules.prep and b[i+1] in crules.article:
                    hint="Read the manual again, HINT:No need of a semicolon between a prep and an article"
                if b[i-1] in crules.article and b[i+1] in crules.onoun:
                    hint="Read the manual again, HINT:No need of a semicolon between an article and a noun"               
                    
                if b[i-1] in crules.pronoun1 and b[i+1]=="address":
                    hint="Read the manual again, HINT:No need of a semicolon between a noun and the word 'address'"
                if b[i-1] =="address" and b[i+1] in crules.vbz:
                    hint="Read the manual again, HINT:No need of a semicolon between the word 'address' and [is/was]"         
                if b[i-1] in crules.vbz and b[i+1]=="C/O":
                    hint="Read the manual again, HINT:No need of a semicolon after [is/was]"
                if b[i-1]=="C/O" and b[i+1] in crules.title:
                    hint="Read the manual again, HINT:No need of a semicolon addresstag [C/O,S/O]"

                name=['Esmail Bagani']
                
                for i in name:
                    name1=i.split(" ")
                  
                if b[i-1]==name1[0] and b[i+1]==name1[1]:
                    hint="Read the manual again, HINT:Don't split the name with a semicolon"
                if b[i-1]==name1[1] and b[i+1]==name1[0]:
                    hint="Read the manual again, HINT:Don't split the name with a semicolon"
                    
                if b[i-1] in crules.societyl and b[i+1] in crules.societyl:
                    hint="Read the manual again, HINT:Don't split the society name with a semicolon"
                if b[i-1] in crules.roadl and b[i+1] in crules.roadl:
                    hint="Read the manual again, HINT:Don't split the road name with a semicolon"
                if b[i-1] in crules.statel and b[i+1] in crules.statel:
                    hint="Read the manual again, HINT:Don't split the state name with a semicolon"
                
#-----------------------------type12stay.py-----------------------------------
                if b[i-1] in crules.verb1 and b[i+1] in crules.article:
                    hint="Read the manual again, HINT:No need of a semicolon between a verb and an article.."
                if b[i-1] in crules.article and b[i+1]=="organisation"+".":
                    hint="Read the manual again, HINT:No need of a semicolon between a aricle and a noun.."
                
                if b[i-1] =="The" and b[i+1]=="name":
                    hint="Read the manual again, HINT:No need of a semicolon between a determiner and the keyword name .."
                
                if b[i-1] =="name" and b[i+1]=="of":
                    hint="Read the manual again, HINT:No need of a semicolon between and keyword name and a preposition .."
                if b[i-1] =="of" and b[i+1] in crules.det:
                    hint="Read the manual again, HINT:No need of a semicolon between a preposition and a determiner"
                if b[i-1] in det and b[i+1] in crules.onoun:
                    hint="Read the manual again, HINT:No need of a semicolon between a determiner and the keyword name .."
                if b[i-1] in crules.onoun and b[i+1] in crules.vbz:
                    hint="Read the manual again, HINT:No need of a semicolon between a noun and [is/was] .."
                if b[i-1] in crules.vbz and b[i+1] in crules.onamelst:
                    hint="Read the manual again, HINT:No need of a semicolon between [is/was] and an object name like building name,name of a person etc. "
                    hintlst.append(hint)
                if b[i-1] in crules.onamelst and b[i+1] in crules.onamelst:
                    hint="Read the manual again, HINT:There is no  of items here, it has to be considered as a single entity..so please avoid semicolon here."
                    hintlst.append(hint)
                if b[i-1]=="The" and b[i+1]=="address":
                    hint="Read the manual again, HINT:No need of a semicolon between a determiner and the a propernoun 'address'"
                    hintlst.append(hint)
                if b[i-1] =="address" and b[i+1] in crules.vbz:
                    hint="Read the manual again, HINT:No need of a semicolon between the word 'address' and [is/was]"
                    hintlst.append(hint)
                if b[i-1] in crules.vbz and b[i+1] in crules.new_landmark:
                    hint="Read the manual again, HINT:No need of a semicolon after [is/was]"
                    hintlst.append(hint)
                if b[i-1] in crules.new_landmark and b[i+1] in crules.new_landmark:
                    hint="Read the manual again, HINT:There is no listing of items here, it has to be considered as a single entity..so please avoid semicolon here."
                    hintlst.append(hint)
                if b[i-1].isalpha() and b[i+1].isalpha():
                    hint="Read the manual again, HINT:No need of a semicolon here as it is an abbreviation"
                    hintlst.append(hint)              
#---------------------------------------------------------<m> with no punctuation----------------------------------------------------------------------------------
        for i in range(0,len(b)):            
            if (b[i]=="<m>" and c[i]==" "):
    #----------------------------type6.py-----------------------------------------------------------------------------------
                if b[i-1] in crules.conjadv and b[i+1] in crules.pronoun:
                    
                    hint="InCorrect Answer:Put a Comma after the conjunctive adverb",b[i-1]
                
                    mandlst.append(hint) 
                    
               
##                if (b[i-1] in crules.onoun and b[i+1] in crules.conjadv) or (b[i-1] in crules.onoun and b[i]==" "):
##                    
##                    hint="InCorrect Answer.Put a fullstop to seperate two complete sentences."
##                
##                    mandlst.append(hint)
                
                if (b[i-1] in crules.pronoun) and c[-1]==" ":
                    
                    hint="InCorrect Answer.Always end a sentence with a FULLSTOP"
                
                    mandlst.append(hint)    
        
                    
                if (b[i-1] in crules.title) and (b[i+1] in crules.snoun):    
                    hint="Incorrect Answer: HINT: Put a FULLSTOP after the title",b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint=="Incorrect Answer: HINT: Put a Comma after the common noun",b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in crules.snoun) and (b[i+1] in crules.article):    
                    hint="Incorrect Answer: HINT: Put a Comma after the noun",b[i-1]
                    mandlst.append(hint)
                if (b[i-1] in crules.cnoun) and (b[i+1] in crules.hverb):    
                    hint="Incorrect Answer: HINT: Put a Comma after the noun",b[i-1]
                    mandlst.append(hint)
                onounlst=list(set(crules.onoun) & set(b))
                #print(onounlst)
                if len(onounlst) > 2:
                    if (b[i-1] in crules.onoun and (b[i+1] in crules.article)):
                
                        hint="Read The manual again, HINT:Put a comma aftr the noun",b[i-1]
                        mandlst.append(hint)
               
               
        #---------------------------type10comma.py----------------------------------------------------------------
                if b[i-1] =="Rs" and b[i+1].isdigit():
                    hint="Incorrect Answer,HINT:Put a FULLSTOP after the keyword {Rs]"
                    mandlst.append(hint)     
                phrase="".join(b)
                oned=re.findall("\d+",phrase)
                #print("oned",oned[0],oned[1])
                if b[i-3]=="Rs" and b[i-1]==oned[0] and b[i+1]==oned[1]:
                    hint="Incorrect Answer, HINT:Put a Comma after" + " "+b[i-1]
                    mandlst.append(hint)
                    
                if b[i-3]=="Rs" and b[i-1].isdigit() and c[-1]==" ":
                    hint="Incorrect Answer, HINT:Put a FULLSTOP at the end of the sentence"
                    mandlst.append(hint)
          #---------------------------------------------type11date.py----------------------------------------------------------------    
                
                
                if b[i-3] in crules.months and b[i-1]==str(parse(co,fuzzy=True).day) and b[-1]!="<m>":
                    hint="Incorrect Answer:Put a Comma after the date",b[i-1]
                    mandlst.append(hint)
                if b[i-1]==str(parse(co,fuzzy=True).day) and b[-1]=="<m>":
                    hint="Incorrect Answer:Put a FULLSTOP after the date",b[i-1]
                    mandlst.append(hint)   
                if b[i-1]==str(str(parse(co, fuzzy=True).year)) and c[-1]==" ":
                    hint="Incorrect Answer:Sentence should be ended with a FULLSTOP"
                    mandlst.append(hint)
                if b[i-1] in crules.months and b[i+1]==str(parse(co,fuzzy=True).day):
                    hint="InCorrect Answer:Put a comma just after the month, " +b[i-1]+" when it is followed by just a date(no year mentioned)."
                    mandlst.append(hint)
                if b[i-3]==str(parse(co,fuzzy=True).day) and b[i-1] in crules.months and b[i+1]==str((parse(co, fuzzy=True).year)):
                    hint="InCorrect Answer:Put a comma just after the month, " +b[i-1]+"  if the date format is date-month-year"
                    mandlst.append(hint)    
##                if b[i-3] in crules.months and b[i-1]==str(parse(co,fuzzy=True).day) and c[-1]==" ":
##                    hint="Incorrect Answer:Sentence should be ended with a FULLSTOP"
##                    mandlst.append(hint)    
               
                    
                if b[i-1] in crules.weekdays and b[i+1] in crules.months :
                    hint="Incorrect Answer:Put A comma should be used after the weekday ",b[i-1]," when it is followed by a month and date."
                    mandlst.append(hint)
                                                                 
           #-----------------------------type12.py---------------------------------------------------------------------------------------------------------------------
                if b[i-1] in crules.snoun and b[i+1] in crules.verb1:
                    hint="Read the manual again, HINT:No need of a comma between a noun and a verb"
                    
                if b[i-1] in crules.verb1 and b[i+1] in crules.prep:
                    hint="Read the manual again, HINT:No need of a comma between a verb and a prep"
                if b[i-1] in crules.prep and b[i+1] in crules.article:
                    hint="Read the manual again, HINT:No need of a comma between a prep and an article"
                if b[i-1] in crules.article and b[i+1] in crules.onoun:
                    hint="Read the manual again, HINT:No need of a comma between an article and a noun"               
                    
                if b[i-1] in crules.pronoun1 and b[i+1]=="address":
                    hint="Read the manual again, HINT:No need of a comma between a noun and the word 'address'"
                if b[i-1] =="address" and b[i+1] in crules.vbz:
                    hint="Read the manual again, HINT:No need of a comma between the word 'address' and [is/was]"         
                if b[i-1] in crules.vbz and b[i+1]=="C/O":
                    hint="Read the manual again, HINT:No need of a comma after [is/was]"
                if b[i-1]=="C/O" and b[i+1] in crules.title:
                    hint="Read the manual again, HINT:No need of a comma addresstag [C/O,S/O]"

                name=['Esmail Bagani']
                
                for i in name:
                    name1=i.split(" ")
                  
                if b[i-1]==name1[0] and b[i+1]==name1[1]:
                    hint="Read the manual again, HINT:Don't split the name with any punctuaion"
                    correctlst.append(hint)
                if b[i-1]==name1[1] and b[i+1]==name1[0]:
                    hint="Read the manual again, HINT:Don't split the name with any punctuaion"
                    correctlst.append(hint)
                    
                if b[i-1] in crules.societyl and b[i+1] in crules.societyl:
                    hint="Correct Answer,HINT:Don't split the society name with any punctuaion"
                    correctlst.append(hint)
                if b[i-1] in crules.roadl and b[i+1] in crules.roadl:
                    hint="Correct Answer,HINT:Don't split the road name with any punctuaion"
                    correctlst.append(hint)
                if b[i-1] in crules.statel and b[i+1] in crules.statel:
                    hint="Correct Answer,HINT:Don't split the state name with any punctuaion"
                    correctlst.append(hint)
                
#-----------------------------type12stay.py-----------------------------------
                if b[i-1] in crules.verb1 and b[i+1] in crules.article:
                    hint="Read the manual again, HINT:No need of any punctuation between a verb and an article.."
                    correctlst.append(hint)
                if b[i-1] in crules.article and b[i+1]=="organisation"+".":
                    hint="Read the manual again, HINT:No need of any punctuation between a aricle and a noun.."
                    correctlst.append(hint)
                if b[i-1] =="The" and b[i+1]=="name":
                    hint="Read the manual again, HINT:No need of any punctuation between a determiner and the keyword name .."
                    correctlst.append(hint)
                if b[i-1] =="name" and b[i+1]=="of":
                    hint="Read the manual again, HINT:No need of any punctuation between and keyword name and a preposition .."
                    correctlst.append(hint)
                if b[i-1] =="of" and b[i+1] in crules.det:
                    hint="Read the manual again, HINT:No need of any punctuation between a preposition and a determiner"
                    correctlst.append(hint)
                if b[i-1] in det and b[i+1] in crules.onoun:
                    hint="Read the manual again, HINT:No need of any punctuation between a determiner and the keyword name .."
                    correctlst.append(hint)
                if b[i-1] in crules.onoun and b[i+1] in crules.vbz:
                    hint="Read the manual again, HINT:No need of any punctuation between a noun and [is/was] .."
                    correctlst.append(hint)
                if b[i-1] in crules.vbz and b[i+1] in crules.onamelst:
                    hint="Read the manual again, HINT:No need of any punctuation between [is/was] and an object name like building name,name of a person etc. "
                    correctlst.append(hint)
                if b[i-1] in crules.onamelst and b[i+1] in crules.onamelst:
                    hint="Read the manual again, HINT:There is no listing of items here, it has to be considered as a single entity.So no punctuation needed"
                    correctlst.append(hint)
                if b[i-1]=="The" and b[i+1]=="address":
                    hint="Correct Answer, HINT:No need of a punctuation after the determiner 'The'"
                    correctlst.append(hint)
                if b[i-1] =="address" and b[i+1] in crules.vbz:
                    hint="Correct Answer, HINT:No need of a punctuation after address"
                    correctlst.append(hint)
                if b[i-1] in crules.vbz and b[i+1] in crules.new_landmark:
                    hint="Correct Answer, HINT:No need of a punctuation after [is/was]"
                    correctlst.append(hint)
                if b[i-1] in crules.new_landmark and b[i+1] in crules.new_landmark:
                    hint="Correct Answer, HINT:There is no listing of items here, it has to be considered as a single entity..so no punctaution needed."
                    correctlst.append(hint)
                if b[i-1].isalpha() and b[i+1].isalpha():
                    hint="Read the manual again, HINT:A fullstop needed as it is an abbreviation"
                    mandlst.append(hint)    
        return(hintlst,mandlst,correctlst)
