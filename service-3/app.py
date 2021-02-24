from flask import Flask, Response
import random 

app = Flask(__name__)


@app.route("/Grade", methods=["GET"])
def Grade():
    Grade = ["Broken", "Rusty", "Shoddy", "Blunt", "Average", "Well Maintained", "Freshy Forged" ,"Eleven Mastercrafted" ,"Dwarven Mastercrafted"]
    return Response(random.choices(Grade), mimetype="text/plain")


@app.route("/Weapon", methods=["GET"])
def Weapon():
    Weapon = ["Barefist", "Dagger", "ShortSword", "LongSword", "Morning star", "Two-Handed GreatSword" , "Two-Handed BattleAxe","Dual-Wield Daggers", 
    "Dual-Wield Short Axes", "Dual-Wield Short Swords", "Dual-Wield Long Swords", "ShortBow", "Longbow", "Crossbow", "ShortSword And Shield", 
    "LongSword And Shield", "Morning Star And Shield", "Short Axe And Shield", "FoeHammer", "Sting", "Morgul Blade", "Narsil", "Goblin Cleaver" "Andúril"]
    return Response(random.choices(Weapon), mimetype="text/plain")


@app.route("/Stance", methods=["GET"])
def Stance():
    Stance = ["Clumsy", "Light-Footed", "Lightning Fast", "Rock Solid", "Immovable"]
    return Response(random.choices(Stance), mimetype="text/plain")


@app.route("/Trait_1", methods=["GET"])
def Trait_1():
    Trait_1 = ["Odin Force Disease Resist", "Sickly", "Built Different", "Pigeon Chest", "Massive Natural Biceps", "Kleptomaniac"]
    return Response(random.choices(Trait_1), mimetype="text/plain")


@app.route("/Trait_2", methods=["GET"])
def Trait_2():
    Trait_2 = ["Orc Hater", "Human Hater", "Elf Hater", "Dwarf Hater", "Goblin Hater", "Hobbit Hater", "Idiot", "Genius", "Odin Force Healing", "Expert Horse Rider"]
    return Response(random.choices(Trait_2), mimetype="text/plain")


@app.route("/Trait_3", methods=["GET"])
def Trait_3():
    Trait_3 = ["Natural Sprinter", "Low Stamina", "Unending Stamina", "Grand-Master Strategist", "Weak"]
    return Response(random.choices(Trait_3), mimetype="text/plain")



















if __name__ =="__main__":
    app.run(debug=True, host ="0.0.0.0", port=5002)