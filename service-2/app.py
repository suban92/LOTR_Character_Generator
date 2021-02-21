from flask import Flask, Response
import random 
app = Flask(__name__)


@app.route("/Race", methods=["GET"])
def Race():
    Races = ["Orc", "High Elf", "Human", "Dwarf"]
    return Response(random.choices(Races), mimetype="text/plain")


@app.route("/Stature", methods=["GET"])
def Stature():
    Statures = ["Tiny", "Massive", "Built different"]
    return Response(random.choices(Statures), mimetype="text/plain")
    







if __name__ =="__main__":
    app.run(debug=True, host ="0.0.0.0", port=5001)