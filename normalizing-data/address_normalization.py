import urllib
import urllib2
import json
import httplib2

def address_normalization(num, street, zip):
	secret_id = '0864f4e1'
	secret_key = '1d17d4c00f243f5a55fac908c0ce68a6'
	webbrowser = httplib2.Http("tmp/", disable_ssl_certificate_validation=True)
	url = 'https://api.cityofnewyork.us/geoclient/v1/address.json?' + urllib.urlencode({
		'app_id':      secret_id,
		'app_key':     secret_key,
		'houseNumber': num,
		'street': street,
		'zip': zip
		})
	try:
		response, content_json = webbrowser.request( url, "GET")
		content = json.loads(content_json)
	except:
		pass
	try:
		houseNum = content['address']['houseNumber']
		streetName = content['address']['boePreferredStreetName']
		zipcode = content['address']['zipCode']
		return houseNum + ' ' + streetName + ' ' + zipcode
	except:
		return None		

if __name__ == "__main__":
	norm_address(num, street, zip)