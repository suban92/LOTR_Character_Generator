from application import app
from flask import Flask, Response
import random 
import requests




# Defining a route that will randomly pick a characters Melee_Prowess via a entry from the given list (0-1)
@app.route("/Melee_Prowess", methods=["GET","POST"])
def Melee_Prowess():
    Melee_Prowess_List =(0, 1)
    Melee_Prowess = Melee_Prowess_List[random.randrange(0,1)]
    return str(Melee_Prowess)



# Defining a route that will randomly pick a characters Archery_Prowess via a entry from the given list (0-1)
@app.route("/Archery_Prowess", methods=["GET"])
def Archery_Prowess():
    Archery_Prowess_List =(0, 1)
    Archery_Prowess = Archery_Prowess_List[random.randrange(0,1)]
    return str(Archery_Prowess)



# Defining a route that will randomly pick a characters Strength via a entry from the given list (0-1)
@app.route("/Strength", methods=["GET"])
def Strength():
    Strength_List =(0, 1)
    Strength = Strength_List[random.randrange(0,1)]
    return str(Strength)



# Defining a route that will randomly pick a characters Endurance via a entry from the given list (0-1)
@app.route("/Endurance", methods=["GET"])
def Endurance():
    Endurance_List =(0, 1)
    Endurance = Endurance_List[random.randrange(0,1)]
    return str(Endurance)

  

# Defining a route that will randomly pick a characters Intelligence via a entry from the given list (0-1)
@app.route("/Intelligence", methods=["GET"])
def Intelligence():
    Intelligence_List =(0, 1)
    Intelligence = Intelligence_List[random.randrange(0,1)]
    return str(Intelligence)


  
# Defining a route that will randomly pick a characters Awareness via a entry from the given list (0-1)
@app.route("/Awareness", methods=["GET"])
def Awareness():
    Awareness_List =(0, 1)
    Awareness = Awareness_List[random.randrange(0,1)]
    return str(Awareness)

  

# Defining a route that will randomly pick a characters Dexterity via a entry from the given list (0-1)
@app.route("/Dexterity", methods=["GET"])
def Dexterity():
    Dexterity_List =(0, 1)
    Dexterity = Dexterity_List[random.randrange(0,1)]
    return str(Dexterity)



# Defining a route that will randomly pick a characters Dodge via a entry from the given list (0-1)
@app.route("/Dodge", methods=["GET"])
def Dodge():
    Dodge_List =(0, 1)
    Dodge = Dodge_List[random.randrange(0,1)]
    return str(Dodge)