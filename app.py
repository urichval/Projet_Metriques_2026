import requests
from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.get("/paris")
def api_paris():
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()

    times = data.get("hourly", {}).get("time", [])
    temps = data.get("hourly", {}).get("temperature_2m", [])

    n = min(len(times), len(temps))
    result = [
        {"datetime": times[i], "temperature_c": temps[i]}
        for i in range(n)
    ]

    return jsonify(result)

# Déposez votre code à partir d'ici :
@app.route("/contact")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route("/rapport")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme")
def monhistogramme():
    return render_template("histogramme.html")

@app.get("/vent")
def api_vent():
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&hourly=windspeed_10m"
    response = requests.get(url)
    data = response.json()
    times = data.get("hourly", {}).get("time", [])
    winds = data.get("hourly", {}).get("windspeed_10m", [])
    n = min(len(times), len(winds))
    result = [
        {"datetime": times[i], "windspeed": winds[i]}
        for i in range(n)
    ]
    return jsonify(result)

@app.route("/atelier")
def monatelier():
    return render_template("atelier.html")


# Ne rien mettre après ce commentaire

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
