import requests
import json

def main():
	send_url = 'http://freegeoip.net/json'
	r = requests.get(send_url)
	j = json.loads(r.text)
	lat = j['latitude']
	lon = j['longitude']
	response=requests.get("https://api.darksky.net/forecast/111e4f7717fa64ee5ce959c21bf213ce/{},{}?units=si&exclude=currently,minutely,hourly,alerts,flags".format(lat,lon))
	weather= response.json()
	print ('The sky was {}' .format(weather['daily']['data'][0]['summary']))
	print ('The highest temperature in your location today was {} degrees Celcius.' .format(weather['daily']['data'][0]['temperatureHigh']))
	print ('The lowest temperature in your location today was {} degrees Celcius.' .format(weather['daily']['data'][0]['temperatureLow']))
	print ('The humidity in your location today was {}.' .format(weather['daily']['data'][0]['humidity']))
												 
if __name__ == '__main__':
	main()