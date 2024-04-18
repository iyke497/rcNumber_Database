import requests
import time
import csv

def get_co_data(rc_num, headers):
	paylaod = {"searchTerm": rc_num}
	res = requests.post(url, json = paylaod, headers=headers)

	res_dict = res.json()

	data_list = res_dict['data']

	if data_list is None:
			return f"({x}) RC - {rc_num} No record found!"

	time.sleep(sleep_interval/1000)
	#Returns a list of dictionaries
	print(data_list)
	return data_list

def parse_dict_list_to_csv(data, csv_path):
    # Check the length of the list
    list_length = len(data)
    
    # Preparing to write to CSV
    if data:
        keys = data[0].keys()  # Get keys from the first dictionary to use as CSV headers
        with open(csv_path, 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
    else:
        print("The list is empty. No CSV file created.")

    return csv_path

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

csv_path = '../csv_files/file_2.csv'

#Mapping of classification ID to numbers
#1 - BN #2 - RC #3 - IT

for x in range(25):
	try:
		data = get_co_data(rc_num, headers)

		parse_dict_list_to_csv(data, csv_path)
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
