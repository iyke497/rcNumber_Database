import requests
import time
from openpyxl import load_workbook
from datetime import datetime

#Pause program for 950ms for ethical scraping
sleep_interval = 2500

#Corporate Affairs Commision Company Business Name API
url = "https://searchapp.cac.gov.ng/searchapp/api/public-search/company-business-name-it"

#Headers set to spoof the server that requests come from a web browser
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

def get_rc(name):
	paylaod = {"searchTerm": name}
	company_info = {}

	res  = requests.post(url, json = paylaod, headers=headers)

	res_dict = res.json()

	#This is a list within the dictionary response that contains a dictionary with company data.
	dict_list = res_dict['data']

	if dict_list is None:
		com_info_na = {'rc': 'N/A', 'email': 'N/A', 'status': 'N/A', 'name': 'N/A'}
		return com_info_na

	company_info['rc'] = dict_list[0]['rcNumber']
	company_info['name'] = dict_list[0]['approvedName']
	
	if dict_list[0]['email'] is not None:
		company_info['email'] = dict_list[0]['email']
	else:
		company_info['email'] = "N/A"

	if dict_list[0]['companyStatus']:
		company_info['status'] = dict_list[0]['companyStatus']


	return company_info


#Load Workbook and select active worksheet
print(f"[{datetime.now()}] Opening Workbook updatedContractors.xlsx......")
workbook = load_workbook(filename='updatedContractors14k-15k.xlsx')
sheet = workbook.active

#Loop through Contractor name column
for row in range(14595, 15472):
	contractor_name = sheet[f'A{row}'].value
	if contractor_name is not None:
		contractor_name = str(contractor_name)  # Convert to string
		print(f"[{datetime.now()}] Updating ({row}): {contractor_name}")
		try:
			x = get_rc(contractor_name)  # Call your function

			sheet[f'D{row}'] = x['rc']
			sheet[f'E{row}'] = x['email']
			sheet[f'F{row}'] = x['status']
			sheet[f'G{row}'] = x['name']

		except requests.exceptions.ConnectionError:
			print(f"Connection error at iteration  row {row}. Retrying............")
			time.sleep(10)
			continue
		
		except KeyError:
			print(f"[{datetime.now()}] Handling KeyError.........")
			sheet[f'D{row}'] = "KeyError"
			sheet[f'E{row}'] = "KeyError"
			sheet[f'F{row}'] = "KeyError"
			sheet[f'G{row}'] = "KeyError"
			continue

		except requests.exceptions.JSONDecodeError:
			print(f"JSONDecodeError at iteration row {row}. Retrying..........")
			time.sleep(2)
			continue

	time.sleep(sleep_interval / 1000)

	print(f"[{datetime.now()}] Saving Excel workbook.....\n")
	workbook.save('updatedContractors14k-15K_2.xlsx')