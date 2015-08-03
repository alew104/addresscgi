#!/usr/bin/python
import cgi
import cgitb
import geopy
cgitb.enable()
form = cgi.FieldStorage()
address=form.getvalue("address")
street = form.getvalue("street")
city = form.getvalue("city")
state = form.getvalue("state")
zipcode = form.getvalue("zip")


def checkVal():
	print"Content-Type: text/html"
	print
	if not address:
		print"<h1>ERROR ADDRESS VALUE EMPTY</h1>"
		return False

	if not street:
		print"<h1>ERROR STREET VALUE EMPTY</h1>"
		return False

	if not city:
		print"<h1>ERROR CITY VALUE EMPTY</h1>"
		return False

	if not state:
		print"<h1>ERROR STATE VALUE EMPTY</h1>"
		return False

	if not zipcode:
		print"<h1>ERROR ZIPCODE VALUE EMPTY</h1>"
		return False

	return True





def getLatLng(address, street, city, state, zipcode):
	fullAddress = address + ' ' + street + ' ' + city + ' ' + state + ' ' + zipcode
	from geopy.geocoders import Bing
	geocoder = Bing(api_key ='AiLKeLoEcoIYjSYqbfCmHPTzpMa2m_UWqGuNehGs-Kf6xRKo3Yl0t4HKm2CEAcrA')
	loc = geocoder.geocode(fullAddress)
	county = loc.raw['address']['adminDistrict2']
	lat = str(loc.latitude)
	lng = str(loc.longitude)
	print"<p>Latitude: " + lat +  "</p>"
	print"<p>Longitude: " + lng + "</p>"


check = checkVal()
if (check):
	getLatLng(address, street, city, state, zipcode)


