from flask import Flask, Response
import random 
import requests
app = Flask(__name__)


#Service-2 Imports

Race = requests.get("http://service-2:5001/Race")

Stature = requests.get("http://service-2:5001/Stature")

Location = requests.get("http://service-2:5001/Location")

Rank = requests.get("http://service-2:5001/Rank")

Profession = requests.get("http://service-2:5001/Profession")


#Service-3 Imports

Grade = requests.get("http://service-3:5002/Grade")

Weapon = requests.get("http://service-3:5002/Weapon")

Stance = requests.get("http://service-3:5002/Stance")

Trait_1 = requests.get("http://service-3:5002/Trait_1")

Trait_2 = requests.get("http://service-3:5002/Trait_2")

Trait_3 = requests.get("http://service-3:5002/Trait_3")


#Service-4 Imports

Melee_Prowess = requests.get("http://service-4:5003/Melee_Prowess")

Archery_Prowess = requests.get("http://service-4:5003/Archery_Prowess")

Strength = requests.get("http://service-4:5003/Strength")

Endurance = requests.get("http://service-4:5003/Endurance")

Intelligence = requests.get("http://service-4:5003/Intelligence")

Awareness = requests.get("http://service-4:5003/Awareness")

Dexterity = requests.get("http://service-4:5003/Dexterity")

Dodge = requests.get("http://service-4:5003/Dodge")














if __name__ =="__main__":
    app.run(debug=True, host ="0.0.0.0", port=5004)