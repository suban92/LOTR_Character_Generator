from application import app
from flask import Flask, Response
import random 



@app.route("/Race", methods=["GET"])
def Race():
    Race = ["Orc", "Woodland Elf", "Human", "Dwarf", "Goblin", "High Elf", "Ent", "Hobbit", "Nazgûl", "Uruk-Hai", "Dúnedain", "Orge", "Troll", "Ghost Pirate"]
    return Response(random.choices(Race), mimetype="text/plain")


@app.route("/Stature", methods=["GET"])
def Stature():
    Stature = ["Tiny", "Small", "Average", "Large", "Massive", "Gigantic", "Colossal", "Stocky"]
    return Response(random.choices(Stature), mimetype="text/plain")
    

@app.route("/Location", methods=["GET"])
def Location():
    Location = ["The Shire", "Erebor", "Gondor", "Helm's Deep", "Isengard", "Lothlórien", "Mordor", "Mirkwood", "Rivendell", "Rohan", "Fangorn Forest", "Moria"]
    return Response(random.choices(Location), mimetype="text/plain")


@app.route("/Rank", methods=["GET"])
def Rank():
    Rank = ["Novice", "Apprentice","Journeyman", "Adept", "Master", "Grand-Master"]
    return Response(random.choices(Rank), mimetype="text/plain")


@app.route("/Profession", methods=["GET"])
def Profession():
    Profession = ["FootSoldier","Duelist", "Berserker", "Knight", "Wizard", "Assassin", "Ranger", "Druid", "Scout", "Raider", "Mercenary"]
    return Response(random.choices(Profession), mimetype="text/plain")