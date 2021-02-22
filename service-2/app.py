from flask import Flask, Response
import random 

app = Flask(__name__)


@app.route("/Race", methods=["GET"])
def Race():
    Races = ["Orc", "Woodland Elf", "Human", "Dwarf", "Goblin", "High Elf", "Ent", "Hobbit", "Ringwraith", "Uruk-hai"]
    return Response(random.choices(Races), mimetype="text/plain")


@app.route("/Stature", methods=["GET"])
def Stature():
    Statures = ["Tiny", "Small", "Average", "Large", "Massive", "Gigantic", "Colossal"]
    return Response(random.choices(Statures), mimetype="text/plain")
    

@app.route("/Location", methods=["GET"])
def Location():
    Locations = ["The Shire", "Erebor", "Gondor", "Helm's Deep", "Isengard", "Lothlórien", "Mordor", "Mirkwood", "Rivendell", "Rohan", "Fangorn Forest", "Moria"]
    return Response(random.choices(Locations), mimetype="text/plain")


@app.route("/Rank", methods=["GET"])
def Rank():
    Ranks = ["Novice", "Apprentice", "Adept", "Master", "Grand-Master"]
    return Response(random.choices(Ranks), mimetype="text/plain")

@app.route("/Profession", methods=["GET"])
def Profession():
    Professions = ["Berserker", "Knight", "Wizard", "Assassin", "Woodland Archer",]
    return Response(random.choices(Professions), mimetype="text/plain")


if __name__ =="__main__":
    app.run(debug=True, host ="0.0.0.0", port=5001)