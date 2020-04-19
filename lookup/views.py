from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode='+zipcode+'&distance=5&API_KEY=47459E6A-0BE5-47C1-98D0-96B714EEE79D')
		
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		if api[0]["AQI"] >= 0 and api[0]["AQI"] <= 50:
		  	category_description = "Air quality is satisfactory, and air pollution poses little or no risk."
		  	category_color = "good"
		elif api[0]["AQI"] > 50 and api[0]["AQI"] <= 100:
		  	category_description = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
		  	category_color = "moderate"
		elif api[0]["AQI"] > 100 and api[0]["AQI"] <= 150:
		  	category_description = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
		  	category_color = "usg"
		elif api[0]["AQI"] > 150 and api[0]["AQI"] <= 200:
		  	category_description = "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
		  	category_color = "unhealthy"
		elif api[0]["AQI"] > 200 and api[0]["AQI"] <= 300:
		  	category_description = "Health alert: The risk of health effects is increased for everyone."
		  	category_color = "very-unhealthy"
		elif api[0]["AQI"] > 300:
		  	category_description = "Health warning of emergency conditions: everyone is more likely to be affected."
		  	category_color = "hazardous"
	   

		return render(request,'home.html',{'api':api,
			'category_description':category_description,
			'category_color':category_color,
			})
	else:

		api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=47459E6A-0BE5-47C1-98D0-96B714EEE79D')
		
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		if api[0]["AQI"] >= 0 and api[0]["AQI"] <= 50:
		  	category_description = "Air quality is satisfactory, and air pollution poses little or no risk."
		  	category_color = "good"
		elif api[0]["AQI"] > 50 and api[0]["AQI"] <= 100:
		  	category_description = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
		  	category_color = "moderate"
		elif api[0]["AQI"] > 100 and api[0]["AQI"] <= 150:
		  	category_description = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
		  	category_color = "usg"
		elif api[0]["AQI"] > 150 and api[0]["AQI"] <= 200:
		  	category_description = "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
		  	category_color = "unhealthy"
		elif api[0]["AQI"] > 200 and api[0]["AQI"] <= 300:
		  	category_description = "Health alert: The risk of health effects is increased for everyone."
		  	category_color = "very-unhealthy"
		elif api[0]["AQI"] > 300:
		  	category_description = "Health warning of emergency conditions: everyone is more likely to be affected."
		  	category_color = "hazardous"
	   

		return render(request,'home.html',{'api':api,
			'category_description':category_description,
			'category_color':category_color,
			})

def about(request):
	return render(request,'about.html',{})