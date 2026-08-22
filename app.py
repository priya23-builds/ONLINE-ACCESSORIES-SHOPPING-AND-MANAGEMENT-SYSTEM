import os
from functools import wraps
from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_mysqldb import MySQL

load_dotenv()

app = Flask(__name__)
app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST", "localhost")
app.config["MYSQL_PORT"] = int(os.getenv("MYSQL_PORT", "3306"))
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER", "root")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD", "")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DB", "oa")
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.secret_key = os.getenv("FLASK_SECRET_KEY", "change-this-secret-key")

mysql = MySQL(app)


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "user_email" not in session:
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    return wrapped


def admin_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("is_admin"):
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    return wrapped


@app.route("/")
def landing():
    return render_template("landing1.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        mail = request.form.get("mail", "").strip()
        password = request.form.get("pass", "")

        if mail == "admin@gmail.com" and password == "admin@123":
            session.clear()
            session["is_admin"] = True
            session["user_email"] = mail
            return redirect(url_for("admin"))

        cur = mysql.connection.cursor()
        try:
            cur.execute("SELECT email, password FROM user WHERE email = %s", (mail,))
            user = cur.fetchone()
        finally:
            cur.close()

        if user and mail == user["email"] and password == user["password"]:
            session.clear()
            session["is_admin"] = False
            session["user_email"] = mail
            flash("Login successful")
            return redirect(url_for("userdashboard"))

        return render_template("login.html", error="Invalid Email or Password")

    return render_template("login.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        fn = request.form.get("fullname", "").strip()
        mail = request.form.get("mail", "").strip()
        password = request.form.get("password", "")
        phone = request.form.get("phone", "").strip()

        cur = mysql.connection.cursor()
        try:
            cur.execute(
                "INSERT INTO user (name, email, password, phone) VALUES (%s, %s, %s, %s)",
                (fn, mail, password, phone),
            )
            mysql.connection.commit()
        except Exception:
            mysql.connection.rollback()
            flash("Registration failed. Please check your details.")
            return redirect(url_for("registration"))
        finally:
            cur.close()

        flash("Registration successful. Please log in.")
        return redirect(url_for("login"))

    return render_template("registration.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("landing"))


@app.route("/admin")
@admin_required
def admin():
    return render_template("admin.html")


@app.route("/admin_home")
@admin_required
def admin_home():
    return render_template("admin_home.html")


@app.route("/add_item")
@admin_required
def add_item():
    return render_template("add_item.html")


@app.route("/allorders")
@admin_required
def allorders():
    return render_template("allorders.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/userdashboard")
@login_required
def userdashboard():
    return render_template("userdashboard.html")


@app.route("/my_orders")
@login_required
def my_orders():
    return render_template("my_orders.html")


@app.route("/my_profile")
@login_required
def my_profile():
    return render_template("my_Profile.html")


@app.route("/products")
@login_required
def products():
    return render_template("products.html")


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG", "1") == "1")
