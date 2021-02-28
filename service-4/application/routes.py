from application import app
from flask import Flask, Response
import random 
import requests



@app.route("/Melee_Prowess", methods=["GET","POST"])
def Melee_Prowess():
    Melee_Prowess_List =(0, 1)
    Melee_Prowess = Melee_Prowess_List[random.randrange(0,1)]
    return str(Melee_Prowess)




@app.route("/Archery_Prowess", methods=["GET"])
def Archery_Prowess():
    Archery_Prowess_List =(0, 1)
    Archery_Prowess = Archery_Prowess_List[random.randrange(0,1)]
    return str(Archery_Prowess)



@app.route("/Strength", methods=["GET"])
def Strength():
    Strength_List =(0, 1)
    Strength = Strength_List[random.randrange(0,1)]
    return str(Strength)



@app.route("/Endurance", methods=["GET"])
def Endurance():
    Endurance_List =(0, 1)
    Endurance = Endurance_List[random.randrange(0,1)]
    return str(Endurance)



@app.route("/Intelligence", methods=["GET"])
def Intelligence():
    Intelligence_List =(0, 1)
    Intelligence = Intelligence_List[random.randrange(0,1)]
    return str(Intelligence)



@app.route("/Awareness", methods=["GET"])
def Awareness():
    Awareness_List =(0, 1)
    Awareness = Awareness_List[random.randrange(0,1)]
    return str(Awareness)



@app.route("/Dexterity", methods=["GET"])
def Dexterity():
    Dexterity_List =(0, 1)
    Dexterity = Dexterity_List[random.randrange(0,1)]
    return str(Dexterity)



@app.route("/Dodge", methods=["GET"])
def Dodge():
    Dodge_List =(0, 1)
    Dodge = Dodge_List[random.randrange(0,1)]
    return str(Dodge)