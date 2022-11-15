from flask import Flask,render_template, request, redirect, url_for, session
import ibm_db
app = Flask(__name__)
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=21fecfd8-47b7-4937-840d-d791d0218660.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31864;SECURITY=SSL;SSLServiceCertificate=DigiCertGlobalRootCA.crt;UID=jhs68731;PWD=IA0K22DLUUq1ncnj",'','')


@app.route('/')
def home():
  return render_template('index.html')

@app.route('/register')
def register():
  return render_template('register.html')

@app.route('/login')
def login():
  return render_template('login.html')


@app.route('/donor')
def donor():
  return render_template('donor.html')

@app.route('/needer')
def needer():
  return render_template('needer.html')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
  if request.method == 'POST':
    name = request.form['name']
    lname = request.form['lname']
    email = request.form['email']
    phnum = request.form['phnum']
    age=request.form['age']
    bloodgrp = request.form['bloodgrp']
    

    sql = "SELECT * FROM user WHERE name =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,name)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      return render_template('index.html', msg="You are already a member, please login using your details")
    else:
      insert_sql = "INSERT INTO user VALUES (?,?,?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, name)
      ibm_db.bind_param(prep_stmt, 2, lname)
      ibm_db.bind_param(prep_stmt, 3, email)
      ibm_db.bind_param(prep_stmt, 4, phnum)
      ibm_db.bind_param(prep_stmt, 5, age)
      ibm_db.bind_param(prep_stmt, 6, bloodgrp)
    
      ibm_db.execute(prep_stmt)
    
    return render_template('index.html', msg="Student Data saved successfuly.")


@app.route('/loginpage',methods=['POST'])

def loginpage():
    user = request.form['user']
    passw = request.form['passw']
    sql = "SELECT * FROM user WHERE name =? AND email=?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,user)
    ibm_db.bind_param(stmt,2,passw)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)
    if account:
            return render_template('index.html')
    else:
        return render_template('login.html', pred="Login unsuccessful. Incorrect username / password !") 

@app.route('/donorpage',methods = ['POST', 'GET'])
def addrec():
  if request.method == 'POST':
    name = request.form['name']
    lname = request.form['lname']
    email = request.form['email']
    phnum = request.form['phnum']
    bloodgrp = request.form['bloodgrp']
    location=request.form['location']
    donated=request.form['donated']

    sql = "SELECT * FROM donor WHERE name =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,name)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      return render_template('index.html', msg="You are already a member, please login using your details")
    else:
      insert_sql = "INSERT INTO donor VALUES (?,?,?,?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, name)
      ibm_db.bind_param(prep_stmt, 2, lname)
      ibm_db.bind_param(prep_stmt, 3, email)
      ibm_db.bind_param(prep_stmt, 4, phnum)
      ibm_db.bind_param(prep_stmt, 5, bloodgrp)
       ibm_db.bind_param(prep_stmt,6, location)
      ibm_db.bind_param(prep_stmt, 7, donated)
    
      ibm_db.execute(prep_stmt)
    
    return render_template('index.html', msg="Student Data saved successfuly.")
