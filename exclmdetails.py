from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import datetime
from flask import flash

app = Flask(__name__)
level=1
correct_attempts=0
# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# Enter your database connection details below
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rohith@123'
app.config['MYSQL_DB'] = 'pythonlogin'

# Intialize MySQL
mysql = MySQL(app)

class exclmrules:
    def exclmdetails1(b,c,correct,category,level,username,userid,eid,submittedtext):
               #----------------------------------#print no:of attempts--------------------------------------------------------------------------------------------------
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            sql_select_query = 'select max(nattempts) from exercisedetails where userid= %s and exerciseid=%s'
            cursor.execute(sql_select_query, (session['id'],eid,))
            na= cursor.fetchone()             
            no_at=na.get("max(nattempts)")
            print("no_attempts at commarulesfinal", no_at)
            mysql.connection.commit() 

            from exclmrules import exclmrules as exr
            if no_at==0:
                hintls1t1=[]
                mandlst1=[]
                correctlst1=[]
                submittedtext = request.form.get("text")
                hintlst1,mandlst1,correctlst1,mandatory=exr.exclmone(b,c,correct,category,level,session['username'],session['id'], eid,submittedtext)
                print(hintlst1,mandlst1,correctlst1,mandatory)
                for hint in hintlst1:
                    
                    #print("allhints1",hint)
                    flash(hint,"warning")
                    score1=0
                    cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,1))
                    mysql.connection.commit()
                for hint in mandlst1:
                    #print(hint)
                    flash(hint,"warning")
                    score1=0
                    cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,1))
                    mysql.connection.commit()
                for hint in correctlst1:
                    #print(hint)
                    flash(hint,"success")
                    score1=0
                    cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,0,1,score1,datetime.datetime.now(),category,level,1))
                    mysql.connection.commit()
        #-----------------------------------------------max score of previous click--------------------
             #-------------------------------------------delete failure=0 and success===0-----------------------------------------
                sql_select_query1='delete from exercisedetails where exerciseid=%s and success=0 and failure=0'
                cursor.execute(sql_select_query1,(eid,))
                sql_select_query1='select max(score) from exercisedetails'
                cursor.execute(sql_select_query1)
                ms= cursor.fetchone()
                maxscore=ms.get("max(score)")
                
                if maxscore==None:
                    score1=0
                else:
                    score1=maxscore+0
                no_at1=no_at+1    
                sql_select_query1='select sum(failure),sum(success) from exercisedetails where exerciseid=%s and nattempts=%s'
                cursor.execute(sql_select_query1,(eid,no_at1,))
                fs= cursor.fetchone()
                failure=fs.get("sum(failure)")
                success=fs.get("sum(success)")
                mysql.connection.commit()
                #print("SUCCESS1111",failure,success)
                
                if success==mandatory and failure>0:
                   score1=score1+3
                if success==mandatory and failure==0:
                   score1=score1+5
                if (success<mandatory and success!=0)  and failure >0:
                    score1=score1+3
                if (success<mandatory and success!=0)  and failure==0:
                    score1=score1+3
                if (success==0)  and failure>=0:
                    score1=score1+0   
                sql_select_query1='update exercisedetails set score=%s where exerciseid=%s and nattempts=%s'
                cursor.execute(sql_select_query1,(score1,eid,no_at1,))
                mysql.connection.commit() 
                
               #-------------------------next question based on the failure and success-------------------------------------------------------------
            

                if failure== 0:
                    sql_select_query2='update sentencedb set displayorder="0" where exerciseid=%s'
                    cursor.execute(sql_select_query2,(eid,))  
                    mysql.connection.commit()
                else:
                    sql_select_query2='update sentencedb set displayorder="1" where exerciseid=%s'
                    cursor.execute(sql_select_query2,(eid,))    
                    mysql.connection.commit()
#-----------------------------------------------------------------------2nd attempt--------------------------------------------------------------------------
            elif no_at==1:
               
                submittedtext = request.form.get("text")
                hintlst2=[]
                mandlst2=[]
                correctlst2=[]
                hintlst2,mandlst2,correctlst2,mandatory=exr.exclmtwo(b,c,correct,category,level,session['username'],session['id'], eid,submittedtext)
                print("mandatory",mandatory)
                for hint in correctlst2:
                    
                    flash(hint,"success")
                    score1=0
                    cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,0,1,score1,datetime.datetime.now(),category,level,2))
                    mysql.connection.commit()
                for hint in hintlst2:
                    
                    flash(hint,"warning")
                    score1=0
                    cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,2))
                    mysql.connection.commit()
                for hint in mandlst2:
                    score1=0
                    flash(hint,"warning")
                    cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,2))
                    mysql.connection.commit()
 #-----------------------------------------------max score of previous click--------------------------------------------------------------------------------------------------------------------
           
                sql_select_query1='select max(score) from exercisedetails'
                cursor.execute(sql_select_query1)
                ms= cursor.fetchone()
                maxscore=ms.get("max(score)")
                sql_select_query1='delete from exercisedetails where exerciseid=%s and success=0 and failure=0'
                cursor.execute(sql_select_query1,(eid,))
                if maxscore==None:
                    score1=0
                else:
                    score1=maxscore+0
                no_at1=no_at+1    
                sql_select_query1='select sum(failure),sum(success) from exercisedetails where exerciseid=%s and nattempts=%s'
                cursor.execute(sql_select_query1,(eid,no_at1,))
                fs= cursor.fetchone()
                failure=fs.get("sum(failure)")
                success=fs.get("sum(success)")
                mysql.connection.commit()
                #print("success at 2nd attempt",success,failure)
                  
                #---------------------check similarity for response of prev attempt and then update the score------------------------------------------------------
                    
                    
                sql_select_query1='select distinct(response1) from exercisedetails where exerciseid=%s and nattempts=%s'
                cursor.execute(sql_select_query1,(eid,no_at,))
                records = cursor.fetchone()
                response11=records.get("response1")
                print("response",response11)
                res11=re.findall(r"[\w']+|[.,!?;]", response11)
                    
                sql_select_query1='select distinct(response1) from exercisedetails where exerciseid=%s and nattempts=%s'
                cursor.execute(sql_select_query1,(eid,no_at1,))
                records2 = cursor.fetchone()
                response2=records2.get("response1")
                #print("response2",response2)
                res21=re.findall(r"[\w']+|[.,!?;]", response2)
                #print("res11 and res12 at attempt 2",res11,res21)    
                
                
                if res11==res21:
                   #print("equal")
                   score1=score1+0
                else:
                    #print("non equal")
                    if failure>=1 and success==0:
                        score1==score1+0
                    if failure>0 and success>=1:
                        score1==score1+1
                    if failure==0 and success>=1:
                        score1=score1+3
               
                sql_select_query1='update exercisedetails set score=%s where exerciseid=%s and nattempts=%s'
                cursor.execute(sql_select_query1,(score1,eid,no_at1,))
                mysql.connection.commit() 
                #-------------------------next question based on the failure and success-------------------------------------------------------------
            
                if failure== 0:
                    sql_select_query2='update sentencedb set displayorder="0" where exerciseid=%s'
                    cursor.execute(sql_select_query2,(eid,))  
                    mysql.connection.commit()
                else:
                    sql_select_query2='update sentencedb set displayorder="1" where exerciseid=%s'
                    cursor.execute(sql_select_query2,(eid,))    
                    mysql.connection.commit()          
#------------------------------------------------------------------3rd attempt---------------------------------------------------------------------------------------------                
            elif no_at==2:
                submittedtext = request.form.get("text")
                hintlst3=[]
                mandlst3=[]
                correctlst3=[]
                hint=""
                hintlst3,mandlst3,correctlst3,mandatory=exr.exclmthree(b,c,correct,category,level,session['username'],session['id'], eid,submittedtext)
                print("hintlst3",hintlst3)
                print("mandlst3",mandlst3)
                print("correctlst3",correctlst3)      
                for hint in correctlst3:
                    print("hint1",hint)
                    flash(hint,"success")
                    score1=0
                    cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,0,1,score1,datetime.datetime.now(),category,level,3))
                    mysql.connection.commit()
                for hint in hintlst3:
                    
                    print("allhints2",hint)
                    flash(hint,"warning")
                    score1=0
                    cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,3))
                    mysql.connection.commit()
                for hint in mandlst3:
                    print("hint3",hint)
                    flash(hint,"success")
                    score1=0
                    cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,3))
                    mysql.connection.commit()
 #-----------------------------------------------max score of previous click--------------------------------------------------------------------------------------------------------------------
           
                sql_select_query1='select max(score) from exercisedetails'
                cursor.execute(sql_select_query1)
                ms= cursor.fetchone()
                maxscore=ms.get("max(score)")
                sql_select_query1='delete from exercisedetails where exerciseid=%s and success=0 and failure=0'
                cursor.execute(sql_select_query1,(eid,))
                if maxscore==None:
                    score1=0
                else:
                    score1=maxscore+0
                no_at1=no_at+1    
                sql_select_query1='select sum(failure),sum(success) from exercisedetails where exerciseid=%s and nattempts=%s'
                cursor.execute(sql_select_query1,(eid,no_at1,))
                fs= cursor.fetchone()
                failure=fs.get("sum(failure)")
                success=fs.get("sum(success)")
                mysql.connection.commit()
                #print("success at 3rd attempt",success,failure)
                  
                     #---------------------check similarity for response of prev attempt and then update the score------------------------------------------------------
                    
                    
                sql_select_query1='select distinct(response1) from exercisedetails where exerciseid=%s and nattempts=%s'
                cursor.execute(sql_select_query1,(eid,no_at,))
                records = cursor.fetchone()
                response11=records.get("response1")
                #print("response",response11)
                res11=re.findall(r"[\w']+|[.,!?;]", response11)
                    
                sql_select_query1='select distinct(response1) from exercisedetails where exerciseid=%s and nattempts=%s'
                cursor.execute(sql_select_query1,(eid,no_at1,))
                records2 = cursor.fetchone()
                response2=records2.get("response1")
                #print("response2",response2)
                res21=re.findall(r"[\w']+|[.,!?;]", response2)
                #print("res11 and res12 at attempt 2",res11,res21)    
                
                
                if res11==res21:
                   #print("equal")
                   score1=score1+0
                else:
                    #print("non equal")
                    if failure>=1 and success==0:
                        score1==score1+0
                    if failure>0 and success>=1:
                        score1==score1+1
                    if failure==0 and success>=1:
                        score1=score1+2
                        
               
                sql_select_query1='update exercisedetails set score=%s where exerciseid=%s and nattempts=%s'
                cursor.execute(sql_select_query1,(score1,eid,no_at1,))
                mysql.connection.commit() 
                #-------------------------next question based on the failure and success-------------------------------------------------------------
            
                if failure== 0:
                    sql_select_query2='update sentencedb set displayorder="0" where exerciseid=%s'
                    cursor.execute(sql_select_query2,(eid,))  
                    mysql.connection.commit()
                else:
                    sql_select_query2='update sentencedb set displayorder="1" where exerciseid=%s'
                    cursor.execute(sql_select_query2,(eid,))    
                    mysql.connection.commit()          
                          
            elif no_at==3:
                #print("correctanswer at attempt 4",correct)
                disp = "Correct Answer is: "+correct
                flash(disp,"success")
                #-------------------------------------------delete failure=0 and success===0-----------------------------------------
                sql_select_query1='delete from exercisedetails where exerciseid=%s and success=0 and failure=0'
                cursor.execute(sql_select_query1,(eid,))
                sql_select_query1='select max(score) from exercisedetails'
                cursor.execute(sql_select_query1)
                ms= cursor.fetchone()
                maxscore=ms.get("max(score)")
                
                if maxscore==None:
                    score1=0
                else:
                    score1=maxscore+0
                hint=disp
                
                cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,disp,0,1,score1,datetime.datetime.now(),category,level,4))
                sql_select_query2='update sentencedb set displayorder="0" where exerciseid=%s'
                cursor.execute(sql_select_query2,(eid,))    
                mysql.connection.commit()
            return(score1)          
              
