from flask import Flask, request, render_template
from flask_mysqldb import MySQL
import bcrypt


app = Flask(__name__)
app.config.update(
    MYSQL_HOST="10.2.4.70",
    MYSQL_USER='app_user',
    MYSQL_PASSWORD='1234',
    MYSQL_DB='users_db'
)
mysql = MySQL(app)

@app.route("/login.html")
def login_page():
    return render_template("login.html")

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/signup.html")
def signup_page():
    return render_template("signup.html")

@app.route("/login")
def login():
    user = request.args.get("user")
    password = request.args.get("pass")
    if not (user and password):
        return render_template("login.html")
    cur = mysql.connection.cursor()
    cur.execute("SELECT password FROM users WHERE username = %s", (user,))
    result = cur.fetchone()
    cur.close()
    if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
        return "<h2>✅ Velkommen!</h2>"
    return "<h2>❌ Feil brukernavn eller passord</h2>"

@app.route("/signup")
def signup():
    user = request.args.get("user")
    password = request.args.get("pass")
    mobile = request.args.get("mobile")
    
    if not (user and password and mobile):
        return "<h2>❌ Må fylle ut begge felt</h2>"
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (username, password, mobile) VALUES (%s, %s, %s)", (user, password, mobile))
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    if cur.fetchone():
        cur.close()
        return "<h2>❌ Brukernavn finnes allerede</h2>"
    mysql.connection.commit()
    cur.close()
    return f"<h2>✅ Registrert! Velkommen {user}</h2>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000) 