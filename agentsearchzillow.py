import requests

url = "https://realtor.p.rapidapi.com/properties/list-sold"

querystring = {"radius":"10","sort":"relevance","state_code":"District of Columbia","city":"Washington D.C.","offset":"4","limit":"200"}

headers = {
    'x-rapidapi-host': "realtor.p.rapidapi.com",
    'x-rapidapi-key': "f3a6ef546fmshab1c7b55c324e2bp1232d0jsne80675d3acb2"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)