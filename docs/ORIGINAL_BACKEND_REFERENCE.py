# This file preserves the student's supplied backend in readable form for reference.
# It is intentionally not used by the application. See ../app.py for the cleaned version.
from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "oa"
app.config['MYSQL_CURSORCLASS'] = "DictCursor"
mysql = MySQL(app)
app.secret_key = "Flask@890"

# Supplied routes:
# /, /login, /registration, /admin, /add_item, /about,
# /admin_home, /allorders, /my_orders, /my_profile, /products
