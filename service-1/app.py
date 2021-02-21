from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/", methods=["GET"])
def Home():
    #Retrived a Generated race
    Race = requests.get("http://service-2:5001/Race")
    
    #Retrived a Generated Stature
    Stature = requests.get("http://service-2:5001/Stature")
    
    
    return render_template("Home.html", Race=Race.text, Stature=Stature.text)




















if __name__ =="__main__":
    app.run(debug=True, host ="0.0.0.0")



