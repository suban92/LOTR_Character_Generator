from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# set database URI, disable SQLALCHEMY warning messages and set a secret key

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@service-6/lotr'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = "emwgfn2489ghfn240nf203nfg9gnb2f"

db = SQLAlchemy(app)

from application import routes