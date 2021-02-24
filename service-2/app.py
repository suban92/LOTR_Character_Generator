from flask import Flask, Response
import random 

app = Flask(__name__)


@app.route("/Race", methods=["GET"])
def Race():
    Race = ["Orc", "Woodland Elf", "Human", "Dwarf", "Goblin", "High Elf", "Ent", "Hobbit", "Nazgûl", "Uruk-Hai", "Dúnedain"]
    return Response(random.choices(Race), mimetype="text/plain")


@app.route("/Stature", methods=["GET"])
def Stature():
    Stature = ["Tiny", "Small", "Average", "Large", "Massive", "Gigantic", "Colossal"]
    return Response(random.choices(Stature), mimetype="text/plain")
    

@app.route("/Location", methods=["GET"])
def Location():
    Location = ["The Shire", "Erebor", "Gondor", "Helm's Deep", "Isengard", "Lothlórien", "Mordor", "Mirkwood", "Rivendell", "Rohan", "Fangorn Forest", "Moria"]
    return Response(random.choices(Location), mimetype="text/plain")


@app.route("/Rank", methods=["GET"])
def Rank():
    Rank = ["Novice", "Apprentice", "Adept", "Master", "Grand-Master"]
    return Response(random.choices(Rank), mimetype="text/plain")

@app.route("/Profession", methods=["GET", "POST"])
def Profession():
    Profession = ["FootSoldier","Swordsmen", "Berserker", "Knight", "Wizard", "Assassin", "Ranger", "Druid", "Scout"]
    return Response(random.choices(Profession), mimetype="text/plain")


if __name__ =="__main__":
    app.run(debug=True, host ="0.0.0.0", port=5001)