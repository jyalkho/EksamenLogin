from flask import Flask, request, render_template
from flask_mysqldb import MySQL

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
    if user == "admin" and password == "1234":
        return "<h2>✅ Velkommen!</h2>"
    if user or password:
        return "<h2>❌ Feil brukernavn eller passord</h2>"
    return render_template("login.html")

@app.route("/signup")
def signup():
    user = request.args.get("user")
    password = request.args.get("pass")
    if not (user and password):
        return "<h2>❌ Må fylle ut begge felt</h2>"
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (user, password))
    mysql.connection.commit()
    cur.close()
    return f"<h2>✅ Registrert! Velkommen {user}</h2>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)