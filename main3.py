

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import datetime
##from type16neutral import declneutral 
##from type16decl import type16decl
##from imperativenum import type17num 
##from type7write import type7w
from flask import flash

app = Flask(__name__)

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
        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))


@app.route("/view",methods=["POST","GET"])  

def getvalue():
    if 'loggedin' in session:
        category=request.form.get('category')
        print("category",category)
        if category=="fullstop":
            correct_attempts=0
            level = request.form['level']
            print("lebel",level)
            session['level']=level
            session['category']=category
            
            from subprocess import call
            
            
            if level=="1" and category=="fullstop":                
                call(["python", "type16neutral.py"])
                if correctlst==1:
                    call(["python", "type16neutral.py"])
                    
                
            if level=="2" and category=="fullstop":
                call(["python", "type16decl.py"])
              
            if level=="3" and category=="fullstop":
                call(["python", "imperativenum.py"])
                 
            if level=="4" and category=="fullstop":
                call(["python", "type7write.py"])
                  
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
            sql_select_query = 'select max(exerciseid) from sentencedb where level=%s and category=%s'
            cursor.execute(sql_select_query, (level,category,))
            #cursor.execute("SELECT max(exerciseid) FROM sentencedb where level='%s'
            exid = cursor.fetchone() 
            for key,value in exid.items():
                eid=value
            sql_select_query = 'select nopunct from sentencedb where exerciseid = %s'
            cursor.execute(sql_select_query, (eid,))
            rows= cursor.fetchall()
            for row in rows:
                print("row",row)
          
            return render_template('fullstop.html', rows=rows,level=level)
        return render_template('home.html',level=session['level'],category=session['category'],username=session['username'])
                    
        

@app.route('/submit', methods=["GET", "POST"])
def submit_textarea():
    snoun=['Mary','James','John','Alice','A. Roy', 'K. Singh', 'R. K. Narayan', 'R. Kushner' ]
    verb=['stand','answered','won','got','secured','achieved','hurt','lost','opened','closed','cooked','met','read','wrote','drew','drank','paid','bought','stayed','worked','joined','taught','married','dated','intracted','consultd','visited','debated','argued','fought','lived','seperated']
    verb1=[]
    boolst=['The God of Small Things','Train to Pakistan','The Malgudi Days','The Mars Room']

    for i in verb:
        verb1.append(i.capitalize())
    article=['a','an']
    det=['the']
    adj=['confident','adorable','generous','charming','clever','huge','red','small','heavy','beautiful','fantastic','mesmerising','well-defined','hot','cold','warm','strong-flavored','delicious','tasty','mind-blowing','spicy','excellent','lovely','thrilled','elated','difficult','intelligent','rapid-fire','open-ended','lovely','fascinating','short','precise','interesting','selective','magnificent','high-grade','exceptional','focused','ambitious','demanding','competetive','exciting','brilliant','amazing','three-room','luxurious','spacious','own','modern','adorable','favorite','new','worthy','valuable','expensive','precious','limpy','twisted','sprained','fractured','considerate','attractive','amusing','jovial']
    onoun=['box','book','cage','scenary','house','building','tea','water','coffee','biriyani','pulav','kichdi','novel','story','match','race','ankle','leg','first-prize','second-prize','job','position','keys','books','poem','story','furniture','vegetables','fruits','bicycles','house','organisation','school','college','flat','question']
    prep=['in','for','with','from']
    title=['Dr','Prof']
    vbz=['is','has']
    hintlst=[]
    correctlst=[]
    mandlst=[]
    if request.method == 'POST':
        
           
        #----------- store the given text in a variable--------------------------------------------
        submittedtext = request.form['text']
        level = session.get('level',None)
        category=session.get('category',None)
##        level = request.form['level']
##        category=request.form['category']
        print("level",level,category)
        #----------open the database to retrieve the taggged sentence------------------------------
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        sql_select_query = 'select max(exerciseid) from sentencedb where level=%s and category=%s'
        cursor.execute(sql_select_query, (level,category,))
        #cursor.execute("SELECT max(exerciseid) FROM sentencedb where level='%s'
        exid = cursor.fetchone() 
        for key,value in exid.items():
            eid=value
        sql_select_query = 'select nopunct from sentencedb where exerciseid = %s'
        cursor.execute(sql_select_query, (eid,))
        rows= cursor.fetchall()
        for row in rows:
            print("row",row)
        sql_select_query = 'select taggedsent,correctans,category from sentencedb where exerciseid = %s'
        cursor.execute(sql_select_query, (eid,))
       
        trows = cursor.fetchall()
        for i in trows:
            tagsent=i # {'taggedsent': 'James<w>opened<w>a<w>small<w>box<m>'}

            tagged1=tagsent.get('taggedsent')
            correct=tagsent.get('correctans')
            category=tagsent.get('category')
        #print("taggedsent",tagged1,correct,category)

        tagged=re.split(r'(<w>|<m>)',tagged1)
           
        #-------------------processing the userinput to match with the tagged sentence--------------
        u=submittedtext.split()
        result=[]

        for elem in u:
            #print(elem)
            
            result.append(elem)
            if elem.endswith(","):
                result.append(elem[0:-1])
                result.append(elem[-1])
                
                result.remove(elem)
            elif elem.endswith("."):
                result.append(elem[0:-1])
                result.append(elem[-1])
                
                result.remove(elem)

            elif elem.endswith("?"):
                result.append(elem[0:-1])
                result.append(elem[-1])
                
                result.remove(elem)     
        #print("result",result)
            
          
        #------------------insert spaces-------------------------------------------------------------------------------
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
        #----------------------compare------------------------------------------------------------------------------------

        b=tagged
        b=b[:-1]
        c=userin
        #print(b,"and",c)
        
        
        hint=""
        score=0
        counter=0
        for i in range(0,len(b)):
            if (b[i]=="<m>" and c[i]=="."):
                
               
                
                username=session['username']
                userid=session['id']
                submittedtext = request.form.get("text")
                hint="Correct Answer"
                flash(hint,"success")
        
                correctlst.append(hint)
                
                sql_select_query='select sum(score) from exercisedetails where userid = %s'
                cursor.execute(sql_select_query, (userid,))
                score= cursor.fetchone()
                score1=score.get("sum(score)")
                print("score1 is",score1)
                if score1==None:
                    score1=0
                else:
                    score1=score1+5
                print("score2 for corrrect ans is",score1)  
               
                cursor.execute('insert into exercisedetails(userid,username,exerciseid,correctans,response1,failure,success,score,time1,category) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (session['id'], session['username'], eid,correct,submittedtext,0,1,score1,datetime.datetime.now(),category))
                sql_select_query='select success from exercisedetails where userid = %s and exerciseid= %s'
                cursor.execute(sql_select_query, (userid,eid,))
                mysql.connection.commit()    
                
        for i in range(0,len(b)) :
            if (b[i]=="<w>" and c[i]==","):
                username=session['username']
                submittedtext = request.form.get("text")
                hint="WARNING:CHECK ONCE AGAIN:Is there a need of punctuation[COMMA] there"
                flash(hint,"warning")
                hintlst.append(hint)


            elif (b[i]=="<w>" and c[i]=="?"):
                username=session['username']
                submittedtext = request.form.get("text")
                hint="WARNING:CHECK ONCE AGAIN:Is there a need of punctuation[Question MArk] there"
                flash(hint,"warning")
                hintlst.append(hint)
                
            elif (b[i]=="<w>" and c[i]=="."):
                username=session['username']
                submittedtext = request.form.get("text")
                hint="WARNING:CHECK ONCE AGAIN:Is there a need of punctuation[Fullstop] there"
                flash(hint,"warning")
                hintlst.append(hint)
            if len(hintlst)>0:    
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                level = session.get('level', None)
                level=level+0
                sql_select_query='select sum(score) from exercisedetails where userid = %s'
                cursor.execute(sql_select_query, (userid,))
                score= cursor.fetchone()
                score1=score.get("sum(score)")
                print("score1 is",score1)
                session['level'] = level
                if score1==None:
                    score1=0
                else:
                    score1=score1+5
                print("score2 for corrrect ans is",score1)  
                cursor.execute('INSERT INTO exercisedetails VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s)', (session['id'], session['username'], eid,correct,submittedtext,0,1,score1,datetime.datetime.now(),category,))
                mysql.connection.commit()      
##                if (b[i-1] in snoun) and (b[i+1]==verb):
##                    hint="WARNING:CHECK ONCE AGAIN:Is there a need of punctuation"
##                    hintlst.append(hint)
##                    flash(hint,"warning")
##                
##                elif (b[i-1] in verb) and (b[i+1] in article) or (b[i-1] in verb) and (b[i+1] in prep) or (b[i-1] in verb) and (b[i+1] in det) or (b[i-1] in verb) and (b[i+1] in onoun):
##                
##                    hint="WARNING:CHECK ONCE AGAIN:Is there a need of punctuation"
##                    hintlst.append(hint)
##                    flash(hint,"warning")
##
##                elif (b[i-1] in verb) and (b[i+1] in article) or (b[i-1] in verb1) and (b[i+1] in prep) or (b[i-1] in verb1) and (b[i+1] in det) or (b[i-1] in verb1) and (b[i+1] in onoun):
##                
##                    hint="WARNING:CHECK ONCE AGAIN:Is there a need of punctuation"
##                    hintlst.append(hint)
##                    flash(hint,"warning")
##                       
##                elif (b[i-1] in prep) and (b[i+1] in det) or (b[i-1] in prep) and (b[i+1] in onoun):
##                
##                    hint="WARNING:CHECK ONCE AGAIN:Is there a need of punctuation"
##                    hintlst.append(hint)
##                    flash(hint,"warning")
##
##                elif (b[i-1] in det) and (b[i+1] in onoun) :
##                
##                    hint="WARNING:CHECK ONCE AGAIN:Is there a need of punctuation"
##                    hintlst.append(hint)
##                    flash(hint,"warning")
##
##                elif (b[i-1] in article) and (b[i+1] in adj):
##                
##                    hint="WARNING:CHECK ONCE AGAIN:Is there a need of punctuation"
##                    hintlst.append(hint)
##                    flash(hint,"warning")
##
##                elif (b[i-1] in adj) and (b[i+1] in onoun):
##                
##                    hint="WARNING:CHECK ONCE AGAIN:Is there a need of punctuation"
##                    hintlst.append(hint)
##                    flash(hint,"warning")
##               elif (b[i-1] in snoun) and (b[i+1] in vbz):
##                
##                    hint="WARNING:CHECK ONCE AGAIN:Is there a need of punctuation"
##                    hintlst.append(hint)
##                    flash(hint,"warning")
##                elif (b[i-1] in vbz) and (b[i+1] in verb):
##                
##                    hint="WARNING:CHECK ONCE AGAIN:Is there a need of punctuation"
##                    hintlst.append(hint)
##                    flash(hint,"warning")
                
        for i in range(0,len(b)):            
            if (b[i]=="<m>" and c[i]==" ") or (b[i]=="<m>" and c[i]==",") or (b[i]=="<m>" and c[i]=="?"):
                username=session['username']
                userid=session['id']
                print("userid",userid)
                submittedtext = request.form.get("text")
                hint="WARNING:CHECK ONCE AGAIN:Punctaute Properly."
                flash(hint,"warning")
                mandlst.append(hint)
                if len(mandlst)>0:
                    level = session.get('level', None)
                    level=level+0
                    sql_select_query='select sum(score) from exercisedetails where userid = %s'
                    cursor.execute(sql_select_query, (userid,))
                    score= cursor.fetchone()
                    score1=score.get("sum(score)")
                    print("score1 is",score1)
                    if score1==None:
                        score1=0
                    else:
                        score1=score1+0
                    print("score2 is",score1)  
                    session['level'] = level
                    cursor.execute('INSERT INTO exercisedetails VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s)', (session['id'], session['username'], eid,correct,submittedtext,1,0,score1,datetime.datetime.now(),category,))
                      
                    mysql.connection.commit()
                                
    
    return render_template('fullstop.html', score1=score1,level=level, correctlst=len(correctlst))
        
if __name__ == '__main__':  
   app.run(debug = True) 
