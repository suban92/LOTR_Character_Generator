from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@service-6/lotr'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = "emwgfn2489ghfn240nf203nfg9gnb2f"

db = SQLAlchemy(app)

from application import routes