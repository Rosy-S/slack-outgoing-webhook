from flask import Flask, request, jsonify
import os
import requests, json

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def index(): 
	""" the only route to handle our outgoing webhook. We are going to have three trigger words with different commands each"""
	
	if request.values.get('trigger_word') == "weather":

		#using the Open Weather Map API to get current weather as a Response object
		weather = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=94109,us&APPID=' + os.environ['WEATHER_TOKEN'])
		weather_dict = json.loads(weather.content)
		#converting kelvin (default for weather API) to fahrenheit: kelvin t(f) = t(k) * 9/5 - 459.67
		degree = str((weather_dict.get("main").get("temp")) * 9/5 - 459.67 )
		response = "The weather for San Francisco right now is: " +  degree + " degrees fahrenheit"
		response = payload={"text": "The weather for San Francisco right now is: " +  degree + " degrees fahrenheit" }
		
	elif request.values.get('trigger_word') == "hello":
		# simple response showing basic functionality of responding back to web-hook
		response = payload={"text": "Hi to you too!"}

	elif request.values.get('trigger_word') == "tengo":
		# you can change the username and user picture through payload object
		response = payload={"text": "yo tambien...", "username": "friendly-neighborhood-bot-man", "icon_emoji": ":turtle:"}
	
	else: 
		response = payload={"text": "Hi! This is not connected to Slack right now"}

	return jsonify(response)


if __name__=="__main__": 
	app.run(debug=True)