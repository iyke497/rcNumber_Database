import requests
import time

def hit_api(rc_num, headers):
	paylaod = {"searchTerm": rc_num}
	res = requests.post(url, json = paylaod, headers=headers)

	res_dict = res.json()
	data = dict()

	data_list = res_dict['data']

	if data_list is None:
			return f"({x}) RC - {rc_num} No record found!"

	for i in data_list:
		data['rcNumber'] = i['rcNumber']
		data['name'] = i['approvedName']
		data['address'] = i['address']
		data['status'] = i['companyStatus']
		data['email'] = i['email']
		data['registrationDate'] = i['registrationDate']
		data['classificationId'] = i['classificationId']

	time.sleep(sleep_interval/1000)
	return data

sleep_interval = 1950

url = "https://searchapp.cac.gov.ng/searchapp/api/public-search/company-business-name-it"

#Spoof the API to mimick a web browser request
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

rc_num = 109601

#Mapping of classification ID to numbers
#1 - BN
#2 - RC
#3 - IT

for x in range(5):
	try:
		data = hit_api(rc_num, headers)
		
		if data['classificationId'] == 1: data['type'] = 'BN'
		if data['classificationId'] == 2: data['type'] = 'RC'
		if data['classificationId'] == 3: data['type'] = 'IT'

		print(data, '\n')
		rc_num = rc_num + 1
		

	except requests.exceptions.ConnectionError:
		print(f"Connection error at iteration {x}; rc{rc_num}. Retrying...")
		time.sleep(10)
		continue

	except KeyError:
		print(f'KeyError at iteration{(x)}')

	except requests.exceptions.JSONDecodeError:
			print(f"JSONDecodeError at iteration row {(x)}. Retrying..........")
			time.sleep(2)
			continue

	except TypeError:
		print(f"No record found for iteration {(x)}")
		continue

