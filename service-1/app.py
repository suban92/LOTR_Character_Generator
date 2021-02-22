from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/", methods=["GET"])
def Home():
    Race = requests.get("http://service-2:5001/Race")
    
    Stature = requests.get("http://service-2:5001/Stature")
    
    Location = requests.get("http://service-2:5001/Location")
    
    Rank = requests.get("http://service-2:5001/Rank")
    
    Profession = requests.get("http://service-2:5001/Profession")
    
    
    
    Grade = requests.get("http://service-3:5002/Grade")
    
    Weapon = requests.get("http://service-3:5002/Weapon")
    
    Stance = requests.get("http://service-3:5002/Stance")
    
    Trait_1 = requests.get("http://service-3:5002/Trait_1")
    
    Trait_2 = requests.get("http://service-3:5002/Trait_2")
    
    Trait_3 = requests.get("http://service-3:5002/Trait_3")
    
    
    
    Melee_Prowess = requests.get("http://service-4:5003/Melee_Prowess")
    
    Archery_Prowess = requests.get("http://service-4:5003/Archery_Prowess")
    
    Strength = requests.get("http://service-4:5003/Strength")
    
    Endurance = requests.get("http://service-4:5003/Endurance")
    
    Intelligence = requests.get("http://service-4:5003/Intelligence")
    
    Awareness = requests.get("http://service-4:5003/Awareness")
    
    Dexterity = requests.get("http://service-4:5003/Dexterity")
    
    Dodge = requests.get("http://service-4:5003/Dodge")
    
    return render_template("Home.html", Race=Race.text, Stature=Stature.text, Location=Location.text, 
   
    Rank=Rank.text, Profession=Profession.text, Grade=Grade.text, Weapon=Weapon.text, Stance=Stance.text, 
    
    Trait_1=Trait_1.text, Trait_2=Trait_2.text, Trait_3=Trait_3.text, Melee_Prowess=Melee_Prowess.text,
    
    Archery_Prowess=Archery_Prowess.text, Strength=Strength.text, Endurance=Endurance.text, Intelligence=Intelligence.text,
    
    Awareness=Awareness.text, Dexterity=Dexterity.text, Dodge=Dodge.text)




















if __name__ =="__main__":
    app.run(debug=True, host ="0.0.0.0")



