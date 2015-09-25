from flask import Flask, request, jsonify
import os
import requests, json

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def index(): 
	if request.values.get('trigger_word') == "weather":
		weather = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=94109,us&APPID=' + os.environ['WEATHER_TOKEN'])
		weather_dict = json.loads(weather.content)
		degree = str((weather_dict.get("main").get("temp")) * 9/5 - 459.67 )
		#kelvin t(f) = t(k) * 9/5 - 459.67
		response = "The weather for San Francisco right now is: " +  degree + " degrees fahrenheit"
	elif request.values.get('trigger_word') == "hello":
		response = "Hi to you too!"
	return jsonify(text = response)



if __name__=="__main__": 
	app.run(debug=True)