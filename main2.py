from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import datetime
from subprocess import call
##from type16neutral import declneutral 
##from type16decl import type16decl
##from imperativenum import type17num 
##from type7write import type7w
##from acronymwork import acronymwork
##-----------comma exercises------------------------------
##from type4 import type4
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

# Views

@app.route('/', methods=['GET', 'POST'])
def login():
            # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
                # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()


                # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'                        
    return render_template('index.html', msg='')





@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)



@app.route('/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))



@app.route('/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        username=account.get("username")
        email=account.get("email")
        sql_select_query1='delete from score_details where userid=%s '
        cursor.execute(sql_select_query1,(session['id'],))
        mysql.connection.commit()
        sql_select_query1='select distinct exerciseid from exercisedetails where userid=%s '
        cursor.execute(sql_select_query1,(session['id'],))
        employeeid= cursor.fetchall()
       #--------------------------------------------------------performance details--------------------------------------------------------------------
        
        for i in employeeid:
            eid=i.get('exerciseid')
            print("eid at performance level",eid)
       ##--------------------------------------------------------select max(nattempts),max(score) from exercisedetails---------------------------------------
            sql_select_query1='select max(nattempts),max(score) from exercisedetails where exerciseid=%s and userid=%s '
            cursor.execute(sql_select_query1,(eid,session['id'],))
            nat= cursor.fetchall()
            for i in nat:
                n_att=i.get("max(nattempts)")
                print("max no:of attempts",n_att)
                max_sc=i.get("max(score)")
                print("max_score",max_sc,eid,session['id'])
            
                sql_select_query1='select min(time1) from exercisedetails where exerciseid=%s and userid=%s and nattempts=1'
                cursor.execute(sql_select_query1,(eid,session['id'],))
                st= cursor.fetchone()
                print("st",st)
                start_time=st.get("min(time1)")
                if start_time is None:
                    start_time="00:00:00"
                print("start_time",start_time)
                sql_select_query1='select max(time1) from exercisedetails where exerciseid=%s and userid=%s and nattempts=%s'
                cursor.execute(sql_select_query1,(eid,session['id'],n_att,))
                et= cursor.fetchone()
                end_time=et.get("max(time1)")
                print("end_time",end_time)
               #calculate the time elapsed------------------------------------------------------------
            
                import datetime as dt

                start_dt = dt.datetime.strptime(str(start_time), '%H:%M:%S')
                end_dt = dt.datetime.strptime(str(end_time), '%H:%M:%S')
                duration = (end_dt - start_dt) 
               
                print("timedifference",duration)
                score2=max_sc
                if duration=="0":
                    duration1=start_dt
                else:
                    duration1=duration

                print("score2",score2)                
                category="fullstop"
            
                cursor.execute('insert into score_details(userid,username,exerciseid,score,category,duration,maxattempts) values(%s,%s, %s, %s, %s, %s, %s)', (session['id'], session['username'], eid, score2,category,duration1, n_att,))       
                mysql.connection.commit()         
        return render_template('profile.html', username=username,email=email)
    # Us#return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))

##@app.route("/viewlevel",methods=["POST","GET"])
##def genlevel():
##    
##    if 'visits' in session:
##        session['visits'] = session.get('visits') + 1  # reading and updating session data
##    else:
##        session['visits'] = 1 # setting session data
##    return "Total visits: {}".format(session.get('visits'))

@app.route("/view",methods=["POST","GET"])  

def getvalue():
    if 'loggedin' in session:
        if request.method=="POST":
            displayorder="0"
            username=session['username']
          
           # call(["python", "type16neutral.py"]) #---------------first question on loading the page
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)  
            sql_select_query = 'select min(exerciseid) from sentencedb where displayorder="1" and exerciseid > 0'
            cursor.execute(sql_select_query)
            exid = cursor.fetchone()
        
            for key,value in exid.items():
                    eid=value
            mysql.connection.commit()          
            
            sql_select_query2='select nopunct from sentencedb where exerciseid=%s'
            cursor.execute(sql_select_query2,(eid,))
            np= cursor.fetchone()
            for key,value in np.items():
                    inputtext=value    
            print("inputtext is",inputtext)

           
            #-------------------------select taggedsent,correctans,category from sentencedb
            sql_select_query = 'select taggedsent,correctans,category,level from sentencedb where exerciseid = %s'
            cursor.execute(sql_select_query, (eid,))
       
            trows = cursor.fetchall()
            for i in trows:
                tagsent=i # {'taggedsent': 'James<w>opened<w>a<w>small<w>box<m>'}

                tagged1=tagsent.get('taggedsent')
                correct=tagsent.get('correctans')
                category=tagsent.get('category')
                level=tagsent.get('level')
            #print("getvaluetaggedsent",tagged1,correct,category,level)
            
            cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (session['id'], session['username'], eid,correct,inputtext,0,0,0,0,datetime.datetime.now(),category,level,0))              
            mysql.connection.commit()

            #--------------------------go to comma exercises if 5 exercises of category fullstop and level 5 is done---------------------------
            sql_query='select count(distinct(exerciseid)) from exercisedetails'
            cursor.execute(sql_query)
            mf=cursor.fetchone()
            mfullstop=mf.get("count(distinct(exerciseid))")
            print("mfullstop",mfullstop)



        if mfullstop in range(1,26):#------1-26
            return render_template('fullstop.html',inputtext=inputtext,eid=eid, username=session['username'])
##        elif mfullstop in range(1,6):    #----26
##            return render_template('comma.html',inputtext=inputtext,eid=eid, username=session['username'])
##                    
        

@app.route('/submit', methods=["GET", "POST"])
def submit_textarea():
    from subprocess import call
   
    snoun=['Mary','James','John','Alice','A. Roy', 'K. Singh', 'R. K. Narayan', 'R. Kushner' ]
    verb=['lift','stand','answered','won','got','secured','achieved','hurt','lost','opened','closed','cooked','met','read','wrote','drew','drank','paid','bought','stayed','worked','joined','taught','married','dated','intracted','consulted','visited','debated','argued','fought','lived','seperated']
    verb1=[]
    boolst=['The God of Small Things','Train to Pakistan','The Malgudi Days','The Mars Room']
    alpha=['T','C','S','I','B','M']
    for i in verb:
        verb1.append(i.capitalize())
    article=['a','an']
    det=['the']
    adj=['confident','adorable','generous','charming','clever','huge','red','small','heavy','beautiful','fantastic','mesmerising','well-defined','hot','cold','warm','strong-flavored','delicious','tasty','mind-blowing','spicy','excellent','lovely','thrilled','elated','difficult','intelligent','rapid-fire','open-ended','lovely','fascinating','short','precise','interesting','selective','magnificent','high-grade','exceptional','focused','ambitious','demanding','competetive','exciting','brilliant','amazing','three-room','luxurious','spacious','own','modern','adorable','favorite','new','worthy','valuable','expensive','precious','limpy','twisted','sprained','fractured','considerate','attractive','amusing','jovial']
    onoun=['box','book','cage','scenary','house','building','tea','water','coffee','biriyani','pulav','kichdi','novel','story','match','race','ankle','leg','first-prize','second-prize','job','position','keys','books','poem','story','furniture','vegetables','fruits','bicycles','house','organisation','school','college','flat','question']
    prep=['in','for','with','from']
    title=['Dr','Prof','Mr','Mrs','Sr','Bro','Major','Capt','Miss']
    vbz=['is','has']
    helpingverbs=["could","will","would","might","can"]
    hintlst=[]
    correctlst=[]
    mandlst=[]
    pronoun=['his','her','he','she']
    cnoun=["man","gentleman","orator","woman","lady"]
    conj=['and','but']
    conjadv=['however','morever']
    coverb=['lift']
    neg="not"
    with open("D:\\evakya\\dataset\\tense.txt") as nd:
        for word in nd:                        
            dh=word.split(':')
            for i in verb:
                if i==dh[1]:
                    presentverb=dh[0]
                    presentverb1=presentverb.capitalize()
    if request.method == 'POST':
               
        #----------- store the given text in a variable--------------------------------------------------------------
        submittedtext = request.form['text']
        #level=request.form['output']
      
        
        #---------open the database to retrieve the tagged sentence---------------------------------------------------
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        sql_select_query = 'select min(exerciseid)from sentencedb where displayorder="1" and exerciseid > 0'
        cursor.execute(sql_select_query)
        exid = cursor.fetchone()
    
        for key,value in exid.items():
                eid=value
                
        mysql.connection.commit()
        
        #---------select the level---------------------------------------------------
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        sql_select_query = 'select level from sentencedb where exerciseid=%s'
        cursor.execute(sql_select_query,(eid,))
        levelid = cursor.fetchone()
    
        for key,value in levelid.items():
                level=value
                
        mysql.connection.commit()
        #-------------------------select taggedsent,correctans,category from sentencedb-------------------------------
        sql_select_query = 'select taggedsent,correctans,category,level from sentencedb where exerciseid = %s'
        cursor.execute(sql_select_query, (eid,))
       
        trows = cursor.fetchall()
        for i in trows:
            tagsent=i # {'taggedsent': 'James<w>opened<w>a<w>small<w>box<m>'}

            tagged1=tagsent.get('taggedsent')
            correct=tagsent.get('correctans')
            category=tagsent.get('category')
            level=tagsent.get('level')
        print("taggedsent",tagged1,correct,category,level)
        mysql.connection.commit()
         
        tagged=re.split(r'(<w>|<m>)',tagged1)
           
        #-------------------processing the userinput to match with the tagged sentence-----------------------------------
        u=submittedtext.split()
        result=[]       
        r1 = re.findall(r'[A-Z]<w>[A-Z]<w>[A-Z]',tagged1)
        print("the matched substring",r1)
        #--------------------for acronyms---------------------------------split based on capital letters followed by comma/fullstop
        z = re.findall("[A-Z][.,?][A-Z][.,?][A-Z]|[A-Z][.,?][A-Z][A-Z]|[A-Z][A-Z][.,?][A-Z]|[A-Z][A-Z][A-Z]", submittedtext)
        if z:
            res=z[0]
        else:
            res="0"
        #print(res)    
        result1=[]
        for i in res:
            if i=="0":
               result1=[]
            else:
               result1.append(i)
        #print(result1)
        for elem in u:                
            result.append(elem)
            if elem.endswith(res):
                print("elem",elem)
                #result.append(elem[0:-1])
                print("r",result)
                for i in result:
                    if i==res:
                        result.remove(i)
                        result.extend(result1)
            elif elem.endswith(" "):
                result.append(elem[0:-1])
                for i in result:
                    if i==res:
                        result.remove(i)
                        result.extend(result1)
                result.append(elem[-1])
                result.remove(elem)
            
            elif elem.endswith(","):
                result.append(elem[0:-1])
                for i in result:
                    if i==res:
                        result.remove(i)
                        result.extend(result1)
                result.append(elem[-1])
                result.remove(elem)
            elif elem.endswith("."):
                
                result.append(elem[0:-1])
                for i in result:
                    if i==res:
                        result.remove(i)
                        result.extend(result1)
                result.append(elem[-1])
                result.remove(elem)

            elif elem.endswith("?"):
                result.append(elem[0:-1])
                for i in result:
                    if i==res:
                        result.remove(i)
                        result.extend(result1)
                result.append(elem[-1])
                result.remove(elem)
           
        print(result)    

            
          
        #------------------insert spaces------------------------------------------------------------------------------------------------------------------------
        userin=[]
        for i, element in enumerate(result):
              previous_element = result[i-1] if i > 0 else None
              current_element = element
              next_element = result[i+1] if i < len(result)-1 else None

              if next_element=="," or next_element=="." or next_element=="?" or element in [",",".","?"]:
                    userin.append(element)
                
              else:
                    userin.append(element)
                    userin.append(" ")
    
        print("userin",userin)
       # cursor.execute('INSERT INTO exercisedetails VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s)', (session['id'], session['username'], eid,correct,submittedtext,1,0,0,datetime.datetime.now(),category,))    
        #----------------------compare---------------------------------------------------------------------------------------------------------------------------

        b=tagged
        b=b[:-1]
        c=userin
        
        #print(b,"and",c)
        
        
        hint=""
        

        if eid>=1 and eid < 26:#------------------------fullstop-------------------------------------------------------------
##            #----------------------------------print no:of attempts--------------------------------------------------------------------------------------------------
##            sql_select_query = 'select max(nattempts) from exercisedetails where userid= %s and exerciseid=%s'
##            cursor.execute(sql_select_query, (session['id'],eid,))
##            na= cursor.fetchone()
##           
##              
##            no_at=na.get("max(nattempts)")
##            print("no_attempts", no_at)
##            mysql.connection.commit() 

##            from commarules import crules as cr
##            if no_at==0:
##                submittedtext = request.form.get("text")
##                hintlst,mandlst,correctlst=cr.commaone(b,c,correct,category,level,session['username'],session['id'], eid,submittedtext)
##                for i in hintlst:
##                    
##                    print("allhints",i)
##                    flash(i,"warning")
##                for j in mandlst:
##                    print(j)
##                    flash(j,"warning")
##                for k in correctlst:
##                    print(k)
##                    flash(k,"success")
##                                
##            elif no_at==1:
##                submittedtext = request.form.get("text")
##                hint=cr.commatwo(b,c,correct,session['username'],session['id'], eid)
##                flash(hint,"warning")
##                flash(hint,"success")
##                
##            elif no_at==2:
##                submittedtext = request.form.get("text")
##                hint=cr.commathree(b,c,correct,session['username'],session['id'], eid)
##                flash(hint,"warning")
##                flash(hint,"success")
                
##        elif eid in range(1,6):#---------------fullstop
##            
            #----------------------------------print no:of attempts--------------------------------------------------------------------------------------------------
            sql_select_query = 'select max(nattempts) from exercisedetails where userid= %s and exerciseid=%s'
            cursor.execute(sql_select_query, (session['id'],eid,))
            na= cursor.fetchone()
           
              
            no_at=na.get("max(nattempts)")
            print("no_attempts", no_at)
            mysql.connection.commit() 

            

                    
    #---------------------------------------------------<m> with fullstop--------------------------------------------------------------------------        
            for i in range(0,len(b)):
                if (b[i]=="<m>" and c[i]=="."):
                    
                    username=session['username']
                    userid=session['id']
                    submittedtext = request.form.get("text")
                        
                    hint="Correct Answer.Fullstop at appropriate place.Always end a sentence with a FULLSTOP"
                    flash(hint,"success")
                    correctlst.append(hint)
                               
                    
                    score1=0
                    #print("details",session['id'], session['username'], eid,correct,submittedtext,hint,score1,datetime.datetime.now(),category,level)
                     
                    cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,0,1,score1,datetime.datetime.now(),category,level,0))
                    mysql.connection.commit()
                    sql_select_query1='update sentencedb set displayorder="0" where exerciseid=%s'
                    cursor.execute(sql_select_query1,(eid,))
                    #print("UPDATED SUCCESS")
                    mysql.connection.commit()

                   
                    
    #--------------------------------------------------------<w> with comma-------------------------------------------------------------------------------------             
            for i in range(0,len(b)) :
              
                if (b[i]=="<w>" and c[i]==","):
                    username=session['username']
                    submittedtext = request.form.get("text")
                    #print("submitted text for w with comma",submittedtext)
                     #---------------first attempt------------------------------------
                    if no_at==0:
                    
                        hint="Please add fullstop at appropriate locations.Click the appropriate sidepane and read the manuals"
                        flash(hint,"warning")
                        hintlst.append(hint)
                        
                        for i in hintlst:
                            score1=0    
                            cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0))
                            mysql.connection.commit()
                        sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                        cursor.execute(sql_select_query1,(eid,))
                        #print("UPDATED SUCCESS")
                        mysql.connection.commit()

                    #---------------second attempt------------------------------------
                    if no_at==1:
                    
                        hint="WARNING:CHECK ONCE AGAIN:Is there a need of punctuation[COMMA]"
                        flash(hint,"warning")
                        hintlst.append(hint)
                        
                        for i in hintlst:
                            score1=0    
                            cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0))

                            mysql.connection.commit()
                        sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                        cursor.execute(sql_select_query1,(eid,))
                        #print("UPDATED SUCCESS")
                        mysql.connection.commit()

                      
                      
                    #----------------------third attempt----------------------------------------------------------------
                     
                    if no_at==2:
                        submittedtext = request.form.get("text")
                        if (b[i-1] in snoun) and (b[i+1]==verb):
                            hint=("WARNING:Is there a need of a COMMA after the noun",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")
                        
                        elif (b[i-1] in verb) and (b[i+1] in article) or (b[i-1] in verb) and (b[i+1] in prep) or (b[i-1] in verb) and (b[i+1] in det) or (b[i-1] in verb) and (b[i+1] in onoun):
                        
                            hint=("WARNING:Is there a need of a COMMA after the verb",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")

                        elif (b[i-1] in verb) and (b[i+1] in article) or (b[i-1] in verb1) and (b[i+1] in prep) or (b[i-1] in verb1) and (b[i+1] in det) or (b[i-1] in verb1) and (b[i+1] in onoun):
                        
                            hint=("WARNING:Is there a need of a COMMA after the verb",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")
                               
                        elif (b[i-1] in prep) and (b[i+1] in det) or (b[i-1] in prep) and (b[i+1] in onoun) or (b[i-1] in prep) and (b[i+1] in snoun):
                        
                            hint=("WARNING:Is there a need of a COMMA after the prep",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")

                        elif (b[i-1] in det) and (b[i+1] in onoun) :
                        
                            hint="WARNING:Is there a need of a COMMA after the Determiner",b[i-1]
                            hintlst.append(hint)
                            flash(hint,"warning")

                        elif (b[i-1] in article) and (b[i+1] in adj):
                        
                            hint=("WARNING:Is there a need of a COMMA after the article",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")

                        elif (b[i-1] in adj) and (b[i+1] in onoun):
                        
                            hint=("WARNING:Is there a need of a COMMA after the adjective",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif (b[i-1] in snoun) and (b[i+1] in vbz):
                        
                            hint=("WARNING:Is there a need of a COMMA after the noun",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif (b[i-1] in vbz) and (b[i+1] in verb):
                        
                            hint=("WARNING:Is there a need of a COMMA after [is/are/has/had etc.] when it is followed by a verb")
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif (b[i-1] in pronoun) and (b[i+1] in onoun):
                        
                            hint=("WARNING:Is there a need of a COMMA after the pronoun",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")    
                        
                        elif b[i-1] in alpha and b[i+1] in alpha:
                            hint="WARNING:It is an acronym,No need of a Fullstop here"
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif b[i-1] in prep and b[i+1] in alpha:
                            hint="WARNING:It is an acronym,No need of a Fullstop here"
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif b[i-1] in verb and b[i+1] in alpha:
                            hint="WARNING:It is an acronym,No need of a Fullstop here"
                            hintlst.append(hint)
                            flash(hint,"warning")
                       #-----------------rules for comma-----type3.py-----------------------------------
    ##                    from commarules import crules
    ##                    hint=checkcommarules(b)
    ##                    hintlst.append(hint)
    ##                    flash(hint,"warning")
                        elif b[i-1] in adj and b[i+1] in cnoun:
                            hint="WARNING:No need to seperate an adjective and a commoun noun with comma"
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif b[i-1] in helpingverbs and b[i+1] in verb:
                            hint="WARNING:No need to seperate an adjective and a commoun noun with comma"
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif b[i-1] in verb and b[i+1] in article:
                            hint="WARNING:No need to put a comma when a verb is followed by an article."
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif b[i-1] in onoun and b[i+1] in conj:
                            hint="WARNING:no need of a comma before a conjunction"
                            flash(hint,"warning")
                        elif b[i-1] in conj and b[i+1] in article:
                            hint="WARNING:no need of a comma after a conjunction"
                            flash(hint,"warning")    
    ##                   #-----------------rules for comma-----type4.py-----------------------------------
                        elif b[i-1] in article and b[i+1] in onoun:
                            hint="WARNING:Comma is generally used to show some enumeration/listing.Here a article followed by a noun represents one entity and hence no need of a comma"
                            flash(hint,"warning")
                         #-------------------type6.py---------------------------
                        elif b[i-1] in onoun and b[i+1] in conjadv:
                            hint="WARNING:Don't use a comma after the object noun,at the end of first clause. if the next clause is starting with a conjunctive adverb like morever/however[Note:if Conunctive adverb is starting with small letter], put a semicolon."
                            flash(hint,"warning")
                        elif b[i-1] in pronoun and b[i+1] in helpingverbs:
                            hint="WARNING:Don't use a comma after the pronoun like ['he','she'] which can cause a pause."
                            flash(hint,"warning")
                        elif b[i-1] in helpingverbs and b[i+1] ==neg:
                            hint="WARNING: would+not,could+not etc. is one entity. Don't put a comma and seperate a negation and a helping verb."
                            flash(hint,"warning")

                        elif b[i-1]==neg and b[i+1] in verb:
                            hint="WARNING: No need to use a comma before a verb, as there is no need to seperate a verb from its subject"
                            flash(hint,"warning")
                        elif b[i-1] in verb and b[i+1] in pronoun:
                            hint="WARNING: No need to use a comma after a verb, as there is no need to seperate a verb from its subject"
                            flash(hint,"warning")    
        #---------------------insert into db-----------------------------------------------------------------------------------------------------  
                        for i in hintlst:
                            score1=0
                            cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0))
                            mysql.connection.commit()

                            print("Insert")
                        sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                        cursor.execute(sql_select_query1,(eid,))
                        #print("UPDATED SUCCESS")
                        mysql.connection.commit()
                     
            #----------------------------------------------------------<w> with Question mark----------------------------------------------------------------------------
                elif (b[i]=="<w>" and c[i]=="?"):
                    username=session['username']
                    submittedtext = request.form.get("text")
                    #print("submitted text for w with comma",submittedtext)
                    #----------------------first attempt---------------------------------------------------------------------------------------------------------------------
                    if no_at==0:
                    
                        hint="Please add fullstop at appropriate locations.Click the FULLSTOP tab in the sidepane and read the manuals"
                        flash(hint,"warning")
                        hintlst.append(hint)
                        
                        for i in hintlst:
                            score1=0    
                            cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0))
                            mysql.connection.commit()
                        sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                        cursor.execute(sql_select_query1,(eid,))
                        #print("UPDATED SUCCESS")
                        mysql.connection.commit()
                    #---------------second attempt---------------------------------------------------------------------------------------------------------------------------
                    if no_at==1:
                    
                        hint="WARNING:CHECK ONCE AGAIN:Is there a need of punctuation[COMMA] there in--",[submittedtext]
                        flash(hint,"warning")
                        hintlst.append(hint)
                        
                        for i in hintlst:
                            score1=0    
                            cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0))
                            mysql.connection.commit()
                        sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                        cursor.execute(sql_select_query1,(eid,))
                        #print("UPDATED SUCCESS")
                        mysql.connection.commit()

                                        
                    #-----------------------second attempt-----------------------------------------------------------------------------------------------------------------
                    print("noof attempts at second attempts w with comma",no_at)    
                    if no_at==2:
                        submittedtext = request.form.get("text")
                        if (b[i-1] in snoun) and (b[i+1]==verb):
                            hint=("WARNING:Is there a need of a QUESTION MARK after the noun",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")
                        
                        elif (b[i-1] in verb) and (b[i+1] in article) or (b[i-1] in verb) and (b[i+1] in prep) or (b[i-1] in verb) and (b[i+1] in det) or (b[i-1] in verb) and (b[i+1] in onoun):
                        
                            hint=("WARNING:Is there a need of a QUESTION MARK after the verb",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")

                        elif (b[i-1] in verb) and (b[i+1] in article) or (b[i-1] in verb1) and (b[i+1] in prep) or (b[i-1] in verb1) and (b[i+1] in det) or (b[i-1] in verb1) and (b[i+1] in onoun):
                        
                            hint=("WARNING:Is there a need of a QUESTION MARK after the verb",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")
                               
                        elif (b[i-1] in prep) and (b[i+1] in det) or (b[i-1] in prep) and (b[i+1] in onoun) or (b[i-1] in prep) and (b[i+1] in snoun):
                        
                            hint=("WARNING:Is there a need of a QUESTION MARK after the prep",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")

                        elif (b[i-1] in det) and (b[i+1] in onoun) :
                        
                            hint="WARNING:Is there a need of a QUESTION MARK after the Determiner",b[i-1]
                            hintlst.append(hint)
                            flash(hint,"warning")

                        elif (b[i-1] in article) and (b[i+1] in adj):
                        
                            hint=("WARNING:Is there a need of a QUESTION MARK after the article",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")

                        elif (b[i-1] in adj) and (b[i+1] in onoun):
                        
                            hint=("WARNING:Is there a need of a QUESTION MARK after the adjective",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif (b[i-1] in snoun) and (b[i+1] in vbz):
                        
                            hint=("WARNING:Is there a need of a QUESTION MARK after the noun",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif (b[i-1] in vbz) and (b[i+1] in verb):
                        
                            hint=("WARNING:Is there a need of a QUESTION MARK after [is/are/has/had etc.] when it is followed by a verb")
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif (b[i-1] in pronoun) and (b[i+1] in onoun):
                        
                            hint=("WARNING:Is there a need of a QUESTION MARK after the pronoun",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")    
                        
                        elif b[i-1] in alpha and b[i+1] in alpha:
                            hint=("WARNING:It is an acronym,No need of a QUESTION MARK here")
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif b[i-1] in prep and b[i+1] in alpha:
                            hint=("WARNING:It is an acronym,No need of a QUESTION MARK here")
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif b[i-1] in verb and b[i+1] in alpha:
                            hint=("WARNING:It is an acronym,No need of a QUESTION MARK here")
                            hintlst.append(hint)
                            flash(hint,"warning")
                        #-----------------rules for questionmark----------------------------------------     
                        elif b[i-1] in adj and b[i+1] in cnoun:
                            hint="WARNING:No need to seperate an adjective and a commoun noun with QUESTION MARK"
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif b[i-1] in hverb and b[i+1] in verb:
                            hint="WARNING:No need to seperate an adjective and a commoun noun with QUESTION MARK"
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif b[i-1] in verb and b[i+1] in article:
                            hint="WARNING:No need to put a QUESTION MARK when a verb is followed by an article."
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif b[i-1] in onoun and b[i+1] in conj:
                            hint="WARNING:no need of a QUESTION MARK before a conjunction"
                            flash(hint,"warning")
                        elif b[i-1] in conj and b[i+1] in article:
                            hint="WARNING:no need of a QUESTION MARK after a conjunction"
                            flash(hint,"warning")        
                         
                        #---------------------insert into db-----------------------------------------------------------------------   
                        for i in hintlst:
                            score1=0
                            cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0))
                            mysql.connection.commit()

                            print("Insert")
                        sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                        cursor.execute(sql_select_query1,(eid,))
                        #print("UPDATED SUCCESS")
                        mysql.connection.commit()
                   
            #-------------------------------------------<w> with fullstop--------------------------------------------------------------
                elif (b[i]=="<w>" and c[i]=="."):
                    username=session['username']
                    submittedtext = request.form.get("text")
                    #----------retreive the 0 attempt ----------------------------------------------------------------------------------
                    sql_select_query = 'select max(nattempts) from exercisedetails where userid= %s and exerciseid=%s'
                    cursor.execute(sql_select_query, (session['id'],eid,))
                    na= cursor.fetchone()
                    no_at=na.get("max(nattempts)")
                    print("no_attempts", no_at)
                    #----------------------first attempt---------------------------------------------------------------------------------------------------------------------
                    if no_at==0:
                    
                        hint="Please add fullstop at appropriate locations.Click the FULLSTOP tab in the sidepane and read the manuals"
                        flash(hint,"warning")
                        hintlst.append(hint)
                        
                        for i in hintlst:
                            score1=0    
                            cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0))
                            mysql.connection.commit()
                        sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                        cursor.execute(sql_select_query1,(eid,))
                        #print("UPDATED SUCCESS")
                        mysql.connection.commit()
                    #---------------second attempt---------------------------------------------------------------------------------------
                    if no_at==1:
                    
                        hint="WARNING:CHECK ONCE AGAIN:Is there a need of punctuation[Full Stop] there in ",[submittedtext]
                        flash(hint,"warning")
                        hintlst.append(hint)
                
                    for i in hintlst:
                        score1=0    
                        cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0))
                        mysql.connection.commit()
                    sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                    cursor.execute(sql_select_query1,(eid,))
                    #print("UPDATED SUCCESS")
                    mysql.connection.commit()
                    
                    sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                    cursor.execute(sql_select_query1,(eid,))
                    #print("UPDATED SUCCESS")
                    mysql.connection.commit()
                    
                        
                        
                    #-----------------------third attempt----------------------------------------------------------------    
                    if no_at==2:
                        submittedtext = request.form.get("text")
                        if (b[i-1] in snoun) and (b[i+1] == verb):
                            hint=("WARNING:Is there a need of a COMMA after the noun",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")
                        
                        elif (b[i-1] in verb) and (b[i+1] in article) or (b[i-1] in verb) and (b[i+1] in prep) or (b[i-1] in verb) and (b[i+1] in det) or (b[i-1] in verb) and (b[i+1] in onoun):
                        
                            hint=("WARNING:Is there a need of a COMMA after the verb",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")

                        elif (b[i-1] in verb) and (b[i+1] in article) or (b[i-1] in verb1) and (b[i+1] in prep) or (b[i-1] in verb1) and (b[i+1] in det) or (b[i-1] in verb1) and (b[i+1] in onoun):
                        
                            hint=("WARNING:Is there a need of a COMMA after the verb",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")
                               
                        elif (b[i-1] in prep) and (b[i+1] in det) or (b[i-1] in prep) and (b[i+1] in onoun) or (b[i-1] in prep) and (b[i+1] in onoun):
                        
                            hint=("WARNING:Is there a need of a COMMA after the prep",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")

                        elif (b[i-1] in det) and (b[i+1] in onoun) :
                        
                            hint="WARNING:Is there a need of a COMMA after the Determiner",b[i-1]
                            hintlst.append(hint)
                            flash(hint,"warning")

                        elif (b[i-1] in article) and (b[i+1] in adj):
                        
                            hint=("WARNING:Is there a need of a COMMA after the article",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")

                        elif (b[i-1] in adj) and (b[i+1] in onoun):
                        
                            hint=("WARNING:Is there a need of a COMMA after the adjective",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif (b[i-1] in snoun) and (b[i+1] in vbz):
                        
                            hint=("WARNING:Is there a need of a COMMA after the noun",b[i-1])
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif (b[i-1] in vbz) and (b[i+1] in verb):
                        
                            hint=("WARNING:Is there a need of a COMMA after [is] and [are] when it is followed by a verb")
                            hintlst.append(hint)
    ##                    flash(hint,"warning")
                        elif b[i-1] in alpha and b[i+1] in alpha:
                            hint=("WARNING:It is an acronym,No need of a Fullstop here")
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif b[i-1] in prep and b[i+1] in alpha:
                            hint=("WARNING:It is an acronym,No need of a Fullstop here")
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif b[i-1] in alpha and b[i+1] in alpha:
                            hint=("WARNING:It is an acronym,No need of a Fullstop here")
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif b[i-1] in prep and b[i+1] in alpha:
                            hint=("WARNING:It is an acronym,No need of a Fullstop here")
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif b[i-1] in verb and b[i+1] in alpha:
                            hint=("WARNING:It is an acronym,No need of a Fullstop here")
                            hintlst.append(hint)
                            flash(hint,"warning")
                        #-----------------rules for fullstop----------------------------------------     
                        elif b[i-1] in adj and b[i+1] in cnoun:
                            hint="WARNING:No need to seperate an adjective and a commoun noun with Fullstop"
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif b[i-1] in hverb and b[i+1] in verb:
                            hint="WARNING:No need to seperate an adjective and a commoun noun with Fullstop"
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif b[i-1] in verb and b[i+1] in article:
                            hint="WARNING:No need to put a Fullstop when a verb is followed by an article."
                            hintlst.append(hint)
                            flash(hint,"warning")
                        elif b[i-1] in onoun and b[i+1] in conj:
                            hint="WARNING:no need of a Fullstop before a conjunction"
                            flash(hint,"warning")
                        elif b[i-1] in conj and b[i+1] in article:
                            hint="WARNING:no need of a Fullstop after a conjunction"
                            flash(hint,"warning")     
                        for i in hintlst:
                            score1=0    
                            cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0))
                            mysql.connection.commit()
                        sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                        cursor.execute(sql_select_query1,(eid,))
                        #print("UPDATED SUCCESS")
                        mysql.connection.commit()
                       
                       
                      
            #--------------------------------<m> with no punctuation----------------------------------------------------------------------------------
            for i in range(0,len(b)):            
                if (b[i]=="<m>" and c[i]==" "):
                    username=session['username']
                    submittedtext = request.form.get("text")
                    #print("submitted text for w with comma",submittedtext)
                    #----------------------first attempt---------------------------------------------------------------------------------------------------------------------
                    if no_at==0:
                    
                        hint="Please add fullstop at appropriate locations.Click the FULLSTOP tab in sidepane and read the manuals"
                        flash(hint,"warning")
                        mandlst.append(hint)
                        
                        for i in mandlst:
                            score1=0    
                            cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0))
                            mysql.connection.commit()
                        sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                        cursor.execute(sql_select_query1,(eid,))
                        #print("UPDATED SUCCESS")
                        mysql.connection.commit()

                    #---------------second attempt------------------------------------------------------------------------------------------------
                    if no_at==1:
                        submittedtext = request.form.get("text")
                        hint="WARNING: A period/Fullstop needed in          ",[submittedtext]
                        flash(hint,"warning")
                        mandlst.append(hint)
                      
                        for i in mandlst:
                            score1=0    
                            cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0))
                            mysql.connection.commit()
                        sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                        cursor.execute(sql_select_query1,(eid,))
                        #print("UPDATED SUCCESS")
                        mysql.connection.commit()                  
                      
                    #-----------------------third attempt------------------------------------------------------------------------------------------------------
                      
                    if no_at==2:
                        submittedtext = request.form.get("text")
                        if (b[i-1] in title) and (b[i+1] in snoun):
                            hint="WARNING:Always end a Abbreviation with a Fullstop as in Prof. Dr. Sr. etc"
                            mandlst.append(hint)
                            flash(hint,"warning")

                        if c[-1]==" ":
                          
                            hint="WARNING:A sentence has to be terminated by a Fullstop"
                            mandlst.append(hint)
                            flash(hint,"warning")
                   
                                           
                        for i in mandlst:
                            score1=0    
                            cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0))
                            mysql.connection.commit()
                        sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                        cursor.execute(sql_select_query1,(eid,))
                        #print("UPDATED SUCCESS")
                        mysql.connection.commit()
                       
                        
             #------------------------------------<m> with Comma-----------------------------------------------------------       
                elif (b[i]=="<m>" and c[i]==","):
                    username=session['username']
                    submittedtext = request.form.get("text")
                    #print("submitted text for w with comma",submittedtext)
                    #----------------------first attempt---------------------------------------------------------------------------------------------------------------------
                    if no_at==0:
                    
                        hint="Please add fullstop at appropriate locations.Click the FULSTOP Tab in the sidepane and read the manuals"
                        flash(hint,"warning")
                        hintlst.append(hint)
                        
                        for i in hintlst:
                            score1=0    
                            cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0))
                            mysql.connection.commit()
                        sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                        cursor.execute(sql_select_query1,(eid,))
                        #print("UPDATED SUCCESS")
                        mysql.connection.commit()
                    #---------------second attempt------------------------------------
                    if no_at==1:
                    
                        hint="WARNING: A period/Fullstop needed,not a Comma in,          ",[submittedtext]
                        flash(hint,"warning")
                        mandlst.append(hint)
                        
                        for i in mandlst:
                            score1=0    
                            cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0))
                            mysql.connection.commit()
                        sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                        cursor.execute(sql_select_query1,(eid,))
                        #print("UPDATED SUCCESS")
                        mysql.connection.commit()

                              
                      
                    #-----------------------third attempt----------------------------------------------------------------
                      
                    if no_at==2:
                        submittedtext = request.form.get("text")
                        if (b[i-1] in title) and (b[i+1] in snoun):
                            hint="WARNING:Always end a Abbreviation with a Fullstop.For e.g. Dr. Prof. Sr."
                            mandlst.append(hint)
                            flash(hint,"warning")

                        if c[-1]==" ":
                          
                            hint="WARNING:End of the sentence has reached.Put a fullstop"
                            mandlst.append(hint)
                            flash(hint,"warning")               
                       
                        for i in mandlst:
                            score1=0    
                            cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0))
                            mysql.connection.commit()
                        sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                        cursor.execute(sql_select_query1,(eid,))
                        #print("UPDATED SUCCESS")
                        mysql.connection.commit()
                       
                        
                #----------------------------------------------<m>  with Question Mark--------------------------------------------------------------    
                   
                    
                elif (b[i]=="<m>" and c[i]=="?"):
                    username=session['username']
                    submittedtext = request.form.get("text")
                    #print("submitted text for w with comma",submittedtext)
                    #----------------------first attempt---------------------------------------------------------------------------------------------------------------------
                    if no_at==0:
                    
                        hint="Please add fullstop at appropriate locations.Click the FULLSTOP sidepane and read the manuals"
                        flash(hint,"warning")
                        mandlst.append(hint)
                        
                        for i in hintlst:
                            score1=0    
                            cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0))
                            mysql.connection.commit()
                        sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                        cursor.execute(sql_select_query1,(eid,))
                        #print("UPDATED SUCCESS")
                        mysql.connection.commit()
                    #---------------second attempt------------------------------------
                    if no_at==1:
                    
                        hint="WARNING: A period/Fullstop needed, not a question mark in       ",[submittedtext]
                        flash(hint,"warning")
                        mandlst.append(hint)
                       
                        for i in mandlst:
                            score1=0    
                            cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0))
                            mysql.connection.commit()
                        sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                        cursor.execute(sql_select_query1,(eid,))
                        #print("UPDATED SUCCESS")
                        mysql.connection.commit()
                    #-----------------------third attempt----------------------------------------------------------------
                      
                    if no_at==2:
                        submittedtext = request.form.get("text")
                        if (b[i-1] in title) and (b[i+1] in snoun):
                            hint="WARNING:Always end a Abbreviation with a Fullstop-",b[i-1],"."
                            mandlst.append(hint)
                            flash(hint,"warning")

                        if c[-1]==" ":
                          
                            hint="WARNING:End of the sentence has reached.Put a fullstop"
                            mandlst.append(hint)
                            flash(hint,"warning")
                   
                        for i in mandlst:
                            score1=0    
                            cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,hintmsg,failure,success,score,time1,category,levelp,nattempts) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (session['id'], session['username'], eid,correct,submittedtext,hint,1,0,score1,datetime.datetime.now(),category,level,0))
                            mysql.connection.commit()
                        sql_select_query1='update sentencedb set displayorder="1" where exerciseid=%s'
                        cursor.execute(sql_select_query1,(eid,))
                        #print("UPDATED SUCCESS")
                        mysql.connection.commit()
      
        
       #------------------------------------------update the no:of attempts for the same response--------------------------------
        no_at=no_at+1  
        mysql.connection.commit()
        sql_select_query1='update exercisedetails set nattempts=%s where exerciseid=%s and nattempts="0" and response1=%s'
        cursor.execute(sql_select_query1,(no_at,eid,submittedtext))
        print("no:of attempts at the end",no_at)
        mysql.connection.commit()
       #-------------------------------------------delete failure=0 and success===0-----------------------------------------
        sql_select_query1='delete from exercisedetails where exerciseid=%s and success=0 and failure=0'
        cursor.execute(sql_select_query1,(eid,))
            #print("UPDATED SUCCESS")
        mysql.connection.commit()
       #------------------------------------------select the last inserted row---------------------------------------------------
        if no_at==1:
            
            sql_select_query1='select max(rid) from exercisedetails'
            cursor.execute(sql_select_query1)
            mid= cursor.fetchone()
            maxrid=mid.get("max(rid)")
            print("maximum rid",maxrid)
        #-----------------------------------------------max score of prevoius clickk--------------------------------------------
            print("nattempts for max(score)",no_at)
            sql_select_query1='select max(score) from exercisedetails where userid=%s'# where nattempts=%s'
            cursor.execute(sql_select_query1,(session['id'],))
            mx= cursor.fetchone()           
            maxscore=mx.get("max(score)")
            if maxscore==None:
                maxscore=0
            else:
                maxscore=maxscore+0
            print("maxscore for 1",maxscore)
               
        #-----------------------------------------------get the failure and success per click---------------------
        
            sql_select_query1='select failure,success from exercisedetails where rid=%s'
            cursor.execute(sql_select_query1,(maxrid,))
            fs= cursor.fetchone()
            failure=fs.get("failure")
            success=fs.get("success")
            mysql.connection.commit()
           
        #-----------------------------------------------update the score for first attempt based on failure and success per click---------------------
            
            if failure==0 and success==1:
                score1=maxscore+5
            elif failure==1 and success==0:
                score1=maxscore+0
            #print("score after first attempt",score1)    
            sql_select_query1='update exercisedetails set score=%s where rid=%s'
            cursor.execute(sql_select_query1,(score1,maxrid,))
                #print("UPDATED SUCCESS")
            mysql.connection.commit()
        
        if no_at==2 or no_at>2:
            
            sql_select_query1='select max(rid) from exercisedetails where exerciseid=%s and nattempts=%s'
            cursor.execute(sql_select_query1,(eid,no_at,))
            mid= cursor.fetchone()
            maxrid2=mid.get("max(rid)")
            print("maximum rid",maxrid2)
        #-----------------------------------------------max score of prevoius click--------------------
            no_at1=no_at-1
            sql_select_query1='select max(score) from exercisedetails where nattempts=%s'
            cursor.execute(sql_select_query1,(no_at1,))
            ms= cursor.fetchone()
            maxscore=ms.get("max(score)")
            if maxscore==None:
                maxscore=0
            else:
                maxscore=maxscore+0
            print("maxscore for 2",maxscore)
               
           
        #-----------------------------------------------get the failure and success per click---------------------
        
            sql_select_query1='select failure,success from exercisedetails where rid=%s'
            cursor.execute(sql_select_query1,(maxrid2,))
            fs= cursor.fetchone()
            failure=fs.get("failure")
            success=fs.get("success")
            mysql.connection.commit()
           
            #-----------------------------------------------update the score for first attempt based on failure and success per click---------------------
            
            if failure==0 and success==1:
                score1=maxscore+2
            elif failure==1 and success==0:
                score1=maxscore+0
            #print("score after first attempt",score1)    
            sql_select_query1='update exercisedetails set score=%s where rid=%s'
            cursor.execute(sql_select_query1,(score1,maxrid2,))
                #print("UPDATED SUCCESS")
            mysql.connection.commit()
        
        return render_template('fullstop.html',submittedtext=request.form.get("text"),eid=eid,score1=score1,userid=session['id'])



@app.route("/scoreview",methods=["POST","GET"])  

def getscore():
        

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)          
        sql_select_query1='select * from score_details where userid=%s'
        cursor.execute(sql_select_query1,(session['id'],))
        alldata= cursor.fetchall()
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        username=account.get("username")
        email=account.get("email")
        return render_template('profile.html',username=username,email=email,alldata=alldata)

                
if __name__ == '__main__':  
   app.run(debug = True) 
