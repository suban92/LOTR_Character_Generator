from flask import Flask, Response, request
import random 
import requests

app = Flask(__name__)


# Service-3 Character Imports

@app.route("/Grade", methods=["GET", "POST"])
def Grade():
    Weapon = request.data.decode('utf-8')
    
    Grade_Response = requests.get("http://service-3:5002/Grade")
    Grade_String = (Grade_Response.text)

    if Weapon == "FoeHammer":
        Grade_String = "Eleven Mastercrafted"

    elif Weapon == "Sting":
        Grade_String = "Eleven Mastercrafted"
    
    elif Weapon == "Narsil":
        Grade_String = "Eleven Mastercrafted"

    elif Weapon == "Goblin Cleaver":
        Grade_String = "Eleven Mastercrafted"

    elif Weapon == "Andúril":
        Grade_String = "Eleven Mastercrafted"

    Grade = Grade_String
    return Response(Grade, mimetype="text/plain")



# Service-4 Character Imports

@app.route("/Melee_Prowess", methods=["GET", "POST"])
def Melee_Prowess():
    # Request for the Profession Data to perform if statements to modify Values
    Profession = request.data.decode('utf-8')
    
    Melee_Prowess_Response = requests.get("http://service-4:5003/Melee_Prowess")
    Melee_Prowess_String = (Melee_Prowess_Response.text)
    Melee_Prowess_Int = int(Melee_Prowess_String)
    
    if Profession == "FootSoldier":
        Melee_Prowess_Int += 300
    
    elif Profession == "Duelist":
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

    elif Profession == "Raider":
        Melee_Prowess_Int += 1000

    elif Profession == "Mercenary":
        Melee_Prowess_Int += 1000
         
    Melee_Prowess = str(Melee_Prowess_Int)
    return Response(Melee_Prowess, mimetype="text/plain")



@app.route("/Archery_Prowess", methods=["GET", "POST"])
def Archery_Prowess():
    Profession = request.data.decode('utf-8')
    
    Archery_Prowess_Response = requests.get("http://service-4:5003/Archery_Prowess")
    Archery_Prowess_String = (Archery_Prowess_Response.text)
    Archery_Prowess_Int = int(Archery_Prowess_String)

    if Profession == "FootSoldier":
        Archery_Prowess_Int += 300
    
    elif Profession == "Duelist":
        Archery_Prowess_Int += 600
    
    elif Profession == "Berserker":
        Archery_Prowess_Int += 700
    
    elif Profession == "Knight":
        Archery_Prowess_Int += 500

    elif Profession == "Wizard":
        Archery_Prowess_Int -= 400

    elif Profession == "Assassin":
        Archery_Prowess_Int += 100

    elif Profession == "Ranger":
        Archery_Prowess_Int += 200

    elif Profession == "Druid":
        Archery_Prowess_Int -= 800
    
    elif Profession == "Scout":
        Archery_Prowess_Int += 1000

    elif Profession == "Raider":
        Archery_Prowess_Int += 1000

    elif Profession == "Mercenary":
        Archery_Prowess_Int += 1000
         
    Archery_Prowess = str(Archery_Prowess_Int)
    return Response(Archery_Prowess, mimetype="text/plain")



@app.route("/Strength", methods=["GET", "POST"])
def Strength():
    Profession = request.data.decode('utf-8')
    
    Strength_Response = requests.get("http://service-4:5003/Strength")
    Strength_String = (Strength_Response.text)
    Strength_Int = int(Strength_String)

    if Profession == "FootSoldier":
        Strength_Int += 300
    
    elif Profession == "Duelist":
        Strength_Int += 600
    
    elif Profession == "Berserker":
        Strength_Int += 700
    
    elif Profession == "Knight":
        Strength_Int += 500

    elif Profession == "Wizard":
        Strength_Int -= 400

    elif Profession == "Assassin":
        Strength_Int += 100

    elif Profession == "Ranger":
        Strength_Int += 200

    elif Profession == "Druid":
        Strength_Int -= 800
    
    elif Profession == "Scout":
        Strength_Int += 1000

    elif Profession == "Raider":
        Strength_Int += 1000

    elif Profession == "Mercenary":
        Strength_Int += 1000
         
    Strength = str(Strength_Int)
    return Response(Strength, mimetype="text/plain")



@app.route("/Endurance", methods=["GET", "POST"])
def Endurance():
    Profession = request.data.decode('utf-8')
    
    Endurance_Response = requests.get("http://service-4:5003/Endurance")
    Endurance_String = (Endurance_Response.text)
    Endurance_Int = int(Endurance_String)

    if Profession == "FootSoldier":
        Endurance_Int += 300
    
    elif Profession == "Duelist":
        Endurance_Int += 600
    
    elif Profession == "Berserker":
        Endurance_Int += 700
    
    elif Profession == "Knight":
        Endurance_Int += 500

    elif Profession == "Wizard":
        Endurance_Int -= 400

    elif Profession == "Assassin":
        Endurance_Int += 100

    elif Profession == "Ranger":
        Endurance_Int += 200

    elif Profession == "Druid":
        Endurance_Int -= 800
    
    elif Profession == "Scout":
        Endurance_Int += 1000

    elif Profession == "Raider":
        Endurance_Int += 1000

    elif Profession == "Mercenary":
        Endurance_Int += 1000
         
    Endurance = str(Endurance_Int)
    return Response(Endurance, mimetype="text/plain")



@app.route("/Intelligence", methods=["GET", "POST"])
def Intelligence():
    Profession = request.data.decode('utf-8')
    
    Intelligence_Response = requests.get("http://service-4:5003/Intelligence")
    Intelligence_String = (Intelligence_Response.text)
    Intelligence_Int = int(Intelligence_String)

    if Profession == "FootSoldier":
        Intelligence_Int += 300
    
    elif Profession == "Duelist":
        Intelligence_Int += 600
    
    elif Profession == "Berserker":
        Intelligence_Int += 700
    
    elif Profession == "Knight":
        Intelligence_Int += 500

    elif Profession == "Wizard":
        Intelligence_Int -= 400

    elif Profession == "Assassin":
        Intelligence_Int += 100

    elif Profession == "Ranger":
        Intelligence_Int += 200

    elif Profession == "Druid":
        Intelligence_Int -= 800
    
    elif Profession == "Scout":
        Intelligence_Int += 1000

    elif Profession == "Raider":
         Intelligence_Int += 1000
    
    elif Profession == "Mercenary":
         Intelligence_Int += 1000
         
    Intelligence= str(Intelligence_Int)
    return Response(Intelligence, mimetype="text/plain")



@app.route("/Awareness", methods=["GET", "POST"])
def Awareness():
    Profession = request.data.decode('utf-8')
    
    Awareness_Response = requests.get("http://service-4:5003/Awareness")
    Awareness_String = (Awareness_Response.text)
    Awareness_Int = int(Awareness_String)

    if Profession == "FootSoldier":
        Awareness_Int += 300
    
    elif Profession == "Duelist":
        Awareness_Int += 600
    
    elif Profession == "Berserker":
        Awareness_Int += 700
    
    elif Profession == "Knight":
        Awareness_Int += 500

    elif Profession == "Wizard":
        Awareness_Int -= 400

    elif Profession == "Assassin":
        Awareness_Int += 100

    elif Profession == "Ranger":
        Awareness_Int += 200

    elif Profession == "Druid":
        Awareness_Int -= 800
    
    elif Profession == "Scout":
        Awareness_Int += 1000

    elif Profession == "Raider":
         Awareness_Int += 1000

    elif Profession == "Mercenary":
         Awareness_Int += 1000
         
    Awareness= str(Awareness_Int)
    return Response(Awareness, mimetype="text/plain")



@app.route("/Dexterity", methods=["GET", "POST"])
def Dexterity():
    Profession = request.data.decode('utf-8')
    
    Dexterity_Response = requests.get("http://service-4:5003/Dexterity")
    Dexterity_String = (Dexterity_Response.text)
    Dexterity_Int = int(Dexterity_String)

    if Profession == "FootSoldier":
        Dexterity_Int += 300
    
    elif Profession == "Duelist":
        Dexterity_Int += 600
    
    elif Profession == "Berserker":
        Dexterity_Int += 700
    
    elif Profession == "Knight":
        Dexterity_Int += 500

    elif Profession == "Wizard":
        Dexterity_Int -= 400

    elif Profession == "Assassin":
        Dexterity_Int += 100

    elif Profession == "Ranger":
        Dexterity_Int += 200

    elif Profession == "Druid":
        Dexterity_Int -= 800
    
    elif Profession == "Scout":
        Dexterity_Int += 1000
    
    elif Profession == "Raider":
       Dexterity_Int += 1000

    elif Profession == "Mercenary":
       Dexterity_Int += 1000
         
    Dexterity= str(Dexterity_Int)
    return Response(Dexterity, mimetype="text/plain")

@app.route("/Dodge", methods=["GET", "POST"])
def Dodge():
    Profession = request.data.decode('utf-8')
    
    Dodge_Response = requests.get("http://service-4:5003/Dodge")
    Dodge_String = (Dodge_Response.text)
    Dodge_Int = int(Dodge_String)

    if Profession == "FootSoldier":
        Dodge_Int += 300
    
    elif Profession == "Duelist":
        Dodge_Int += 600
    
    elif Profession == "Berserker":
        Dodge_Int += 700
    
    elif Profession == "Knight":
        Dodge_Int += 500

    elif Profession == "Wizard":
        Dodge_Int -= 400

    elif Profession == "Assassin":
        Dodge_Int += 100

    elif Profession == "Ranger":
        Dodge_Int += 200

    elif Profession == "Druid":
        Dodge_Int -= 800
    
    elif Profession == "Scout":
        Dodge_Int += 1000

    elif Profession == "Raider":
        Dodge_Int += 1000

    elif Profession == "Mercenary":
        Dodge_Int += 1000
         
    Dodge = str(Dodge_Int)
    return Response(Dodge, mimetype="text/plain")




if __name__ =="__main__":
    app.run(debug=True, host ="0.0.0.0", port=5004)