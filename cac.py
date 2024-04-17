import requests

def get_company_rc(name):
	res = requests.post(
		url="https://searchapp.cac.gov.ng/searchapp/api/public-search/company-business-name-it",
		data={"searchTerm": name})
	return res.json()

print(get_company_rc("ZST TECHNOLOGIES LIMITED"))
