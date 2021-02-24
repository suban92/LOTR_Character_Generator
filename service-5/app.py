from flask import Flask, Response, request
import random 
import requests

app = Flask(__name__)

"""
# Service-2 Character Imports

@app.route("/Race", methods=["GET"])
def Race():
    Race_Base = requests.get("http://service-2:5001/Race")
    Race = (Race_Base.text)
    return Response(Race, mimetype="text/plain")


@app.route("/Stature", methods=["GET"])
def Stature(): 
    Stature_Base = requests.get("http://service-2:5001/Stature")
    Stature = (Stature_Base.text)
    return Response(Stature, mimetype="text/plain")
    

@app.route("/Location", methods=["GET"])
def Location(): 
    Location_Base = requests.get("http://service-2:5001/Location")
    Location = (Location_Base.text)
    return Response(Location, mimetype="text/plain")
    

@app.route("/Rank", methods=["GET"])
def Rank():
    Rank_Base = requests.get("http://service-2:5001/Rank")
    Rank = (Rank_Base.text)
    return Response(Rank, mimetype="text/plain")
   

@app.route("/Profession", methods=["GET"])
def Profession():
    Profession_Base = requests.get("http://localhost:5001/Profession")
    Profession = (Profession_Base.text)
    return Response(Profession, mimetype="text/plain")

# Service-3 Character Imports

@app.route("/Grade", methods=["GET"])
def Grade():
    Grade_Base = requests.get("http://service-3:5002/Grade")
    Grade = (Grade_Base.text)
    return Response(Grade, mimetype="text/plain")


@app.route("/Weapon", methods=["GET"])
def Weapon():
    Weapon_Base = requests.get("http://service-3:5002/Weapon")
    Weapon = (Weapon_Base.text)
    return Response(Weapon, mimetype="text/plain")


@app.route("/Stance", methods=["GET"])
def Stance():
    Stance_Base = requests.get("http://service-3:5002/Stance")
    Stance = (Stance_Base.text)
    return Response(Stance, mimetype="text/plain")


@app.route("/Trait_1", methods=["GET"])
def Trait_1():
    Trait_1_Base = requests.get("http://service-3:5002/Trait_1")
    Trait_1 = (Trait_1_Base.text)
    return Response(Trait_1, mimetype="text/plain") 


@app.route("/Trait_2", methods=["GET"])
def Trait_2():
    Trait_2_Base= requests.get("http://service-3:5002/Trait_2")
    Trait_2 = (Trait_2_Base.text)
    return Response(Trait_2, mimetype="text/plain")


@app.route("/Trait_3", methods=["GET"])
def Trait_3():
    Trait_3_Base = requests.get("http://service-3:5002/Trait_3")
    Trait_3 = (Trait_3_Base.text)
    return Response(Trait_3, mimetype="text/plain")
"""

# Service-4 Character Imports

@app.route("/Melee_Prowess", methods=["GET", "POST"])
def Melee_Prowess():
    # Request for the Profession Data to perform if statements to modify Values
    Profession_Response = requests.get("http://localhost:5001/Profession")
    Profession = (Profession_Response.text)
    
    Melee_Prowess_Response = requests.get("http://localhost:5003/Melee_Prowess")
    Melee_Prowess_String = (Melee_Prowess_Response.text)
    Melee_Prowess_Int = int(Melee_Prowess_String)
    
    if Profession == "FootSoldier":
        Melee_Prowess_Int += 300
    
     
    elif Profession == "Swordsmen":
        Melee_Prowess_Int += 600
    
   
    elif Profession == "Berserker":
        Melee_Prowess_Int += 700
    
   

    elif Profession == "Knight":
        Melee_Prowess_Int += 500

    

    elif Profession == "Wizard":
        Melee_Prowess_Int -= 400

    


    elif Profession == "Assassin":
        Melee_Prowess_Int += 100



    elif Profession == "Ranger":
        Melee_Prowess_Int += 200



    elif Profession == "Druid":
        Melee_Prowess_Int -= 800

   

    elif Profession == "Scout":
        Melee_Prowess_Int += 1000
         
    Melee_Prowess = str(Melee_Prowess_Int)
    return Response(Melee_Prowess, mimetype="text/plain")

"""
@app.route("/Archery_Prowess", methods=["GET"])
def Archery_Prowess():
    Archery_Prowess_Base = requests.get("http://service-4:5003/Archery_Prowess")
    Archery_Prowess = (Archery_Prowess_Base.text)
    return Response(Archery_Prowess, mimetype="text/plain")


@app.route("/Strength", methods=["GET"])
def Strength():
    Strength_Base = requests.get("http://service-4:5003/Strength")
    Strength = (Strength_Base.text)
    return Response(Strength, mimetype="text/plain")


@app.route("/Endurance", methods=["GET"])
def Endurance():
    Endurance_Base = requests.get("http://service-4:5003/Endurance")
    Endurance = (Endurance_Base.text)
    return Response(Endurance, mimetype="text/plain")


@app.route("/Intelligence", methods=["GET"])
def Intelligence():
    Intelligence_Base = requests.get("http://service-4:5003/Intelligence")
    Intelligence = (Intelligence_Base.text)
    return Response(Intelligence, mimetype="text/plain")

@app.route("/Awareness", methods=["GET"])
def Awareness():
    Awareness_Base = requests.get("http://service-4:5003/Awareness")
    Awareness = (Awareness_Base.text)
    return Response(Awareness, mimetype="text/plain")
    

@app.route("/Dexterity", methods=["GET"])
def Dexterity():
    Dexterity_Base = requests.get("http://service-4:5003/Dexterity")
    Dexterity = (Dexterity_Base.text)
    return Response(Dexterity, mimetype="text/plain")

@app.route("/Dodge", methods=["GET"])
def Dodge():
    Dodge_Base = requests.get("http://service-4:5003/Dodge")
    Dodge = (Dodge_Base.text)
    return Response(Dodge, mimetype="text/plain")


"""
if __name__ =="__main__":
    app.run(debug=True, host ="0.0.0.0", port=5004)