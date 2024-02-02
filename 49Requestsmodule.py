import requests
r = requests.get("https://financialmodelingprep.com/api/v3/income-statement/AAPL?limit=120&apikey=YOUR_API_KEY")
print(r.text,r.status_code)