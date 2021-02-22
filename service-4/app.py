from flask import Flask, Response
import random 
import requests
app = Flask(__name__)


@app.route("/Melee_Prowess", methods=["GET"])
def Melee_Prowess():
    Melee_Prowess =(random.randint(0, 10))
    return str(Melee_Prowess)


@app.route("/Archery_Prowess", methods=["GET"])
def Archery_Prowess():
    Archery_Prowess =(random.randint(0, 10))
    return str(Archery_Prowess)



@app.route("/Strength", methods=["GET"])
def Strength():
    Strength =(random.randint(0, 10))
    return str(Strength)



@app.route("/Endurance", methods=["GET"])
def Endurance():
   Endurance =(random.randint(0, 10))
   return str(Endurance)




@app.route("/Intelligence", methods=["GET"])
def Intelligence():
    Intelligence =(random.randint(0, 10))
    return str(Intelligence)



@app.route("/Awareness", methods=["GET"])
def Awareness():
    Awareness =(random.randint(0, 10))
    return str(Awareness)



@app.route("/Dexterity", methods=["GET"])
def Dexterity():
    Dexterity =(random.randint(0, 10))
    return str(Dexterity)




@app.route("/Dodge", methods=["GET"])
def Dodge():
    Dodge =(random.randint(0, 10))
    return str(Dodge)











if __name__ =="__main__":
    app.run(debug=True, host ="0.0.0.0", port=5003)