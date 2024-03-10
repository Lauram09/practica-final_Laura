from flask import Flask, request, render_template, redirect, url_for, session
import mysql.connector
app = Flask(__name__)



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="basedatos_laura"
)



@app.route("/",methods = ['POST', 'GET'])
def index():
   return render_template("paginaweb.html")



@app.route("/pagina_privada")
def private_page():
   if request.method == "GET" and session.get("username"):
      return render_template("paginaweb_priv.html")
   else:
      return render_template("paginaweb_pub.html")



@app.route("/login",methods = ['POST', 'GET'])
def login():
      if request.method == 'POST':
         mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="basedatos_laura"
         )
         username = request.form["username"]
         password = request.form["password"]
         cursor = mydb.cursor()
         users = cursor.execute(f"SELECT * FROM datos WHERE nombre = '{username}' AND password_yes = '{password}'")
         users = cursor.fetchall()
         if len(users) > 0:
            session["username"] = username + password
            return render_template("PEIniciprivate.html")
         else:
            return render_template("PEerror.html")
      if request.method == "GET":
         return render_template('PELogin.html')

@app.route("/logout")
def logout():
   if session.get('username'):
      session.pop('username', default=None)
      return redirect("/")