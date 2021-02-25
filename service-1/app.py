from flask import Flask, render_template, Response, request
import requests
import os 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db=SQLAlchemy(app)

PicFolder = os.path.join("static","pics")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@service-6/lotr'

app.config["UPLOAD_FOLDER"] = PicFolder
app.config['SECRET_KEY'] = "emwgfn2489ghfn240nf203nfg9gnb2f"

# Setting the Homepage for my Service
@app.route('/')
@app.route('/Home',methods=["GET"])
def Home():
    Background = os.path.join(app.config["UPLOAD_FOLDER"],"LOTR_Background.jpg")
   
   # Requesting the first set of standard objects from service-2
    Race = requests.get("http://service-2:5001/Race")
    Stature = requests.get("http://service-2:5001/Stature")
    Location = requests.get("http://service-2:5001/Location")
    Rank = requests.get("http://service-2:5001/Rank")
    Profession = requests.get("http://service-2:5001/Profession")
    
   
    # Requesting the second set of semi-modified objects from service-3
    Weapon = requests.get("http://service-3:5002/Weapon")
    Grade = requests.post("http://service-5:5004/Grade", data=Weapon.text)
    Stance = requests.get("http://service-3:5002/Stance")
    Trait_1 = requests.get("http://service-3:5002/Trait_1")
    Trait_2 = requests.get("http://service-3:5002/Trait_2")
    Trait_3 = requests.get("http://service-3:5002/Trait_3")


    # Requesting lasr set modified objects from service-5 
    Melee_Prowess = requests.post("http://service-5:5004/Melee_Prowess", data=Profession.text)
    Archery_Prowess = requests.post("http://service-5:5004/Archery_Prowess", data=Profession.text)
    Strength = requests.post("http://service-5:5004/Strength", data=Profession.text)
    Endurance = requests.post("http://service-5:5004/Endurance",data=Profession.text )
    Intelligence = requests.post("http://service-5:5004/Intelligence", data=Profession.text)
    Awareness = requests.post("http://service-5:5004/Awareness", data=Profession.text)
    Dexterity = requests.post("http://service-5:5004/Dexterity", data=Profession.text)
    Dodge = requests.post("http://service-5:5004/Dodge", data=Profession.text)   
    
    
    return render_template("Home.html",Background=Background,
    Race=Race.text, Stature=Stature.text, Location=Location.text,
    Rank=Rank.text, Profession=Profession.text, Grade=Grade.text, Weapon=Weapon.text, Stance=Stance.text, 
    Trait_1=Trait_1.text, Trait_2=Trait_2.text, Trait_3=Trait_3.text, Melee_Prowess=Melee_Prowess.text,
    Archery_Prowess=Archery_Prowess.text, Strength=Strength.text, Endurance=Endurance.text,
    Intelligence=Intelligence.text, Awareness=Awareness.text, Dexterity=Dexterity.text, Dodge=Dodge.text)

















if __name__ =="__main__":
    app.run(debug=True, host ="0.0.0.0")



