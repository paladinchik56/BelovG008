import bs4 as bs
import requests
import json
# {"bounds":{"bottomLeft":{"lat":55.81125000638905,"lng":49.0942425944959},"topRight":{"lat":55.82671338419883,"lng":49.16295006062138}},"filters":{"banks":["tcs"],"showUnavailable":true,"currencies":["USD"],"amounts":[{"currency":"USD","amount":100}]},"zoom":15}
js =  {"bounds":{"bottomLeft":{"lat":55.81125000638905, "lng":49.0942425944959}, "topRight":{"lat":55.82671338419883, "lng":49.16295006062138}}, "filters":{"banks":["tcs"], "showUnavailable":True, "currencies":["USD"], "amounts":[{"currency": "USD", "amount":100}]}, "zoom":13}


headers = {
"Host": "api.tinkoff.ru",
"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
"Accept": "*/*",
"Accept-Language": "en-GB,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br",
"Content-Type": "application/json",
"Content-Length": '261',
'Origin':'https://www.tinkoff.ru',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-site',
'Referer': 'https://www.tinkoff.ru/',
'Connection': 'keep-alive',
"TE": "trailers"}
url = "https://api.tinkoff.ru/geo/withdraw/clusters"

res = requests.post(url, data=json.dumps(js), headers=headers)

jsn_statem = json.loads(res.text.replace("'", '"'))
clusters = jsn_statem["payload"]["clusters"]
ATMs = []
for cluster in clusters:
    points = cluster["points"]
    for point in points:
        ATM = [point["address"], point['limits']]
        ATMs.append(ATM)
# print(res.text)
