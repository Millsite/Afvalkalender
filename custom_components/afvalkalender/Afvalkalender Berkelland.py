import requests
import json
from datetime import datetime

hostname = 'https://afvalkalender.gemeenteberkelland.nl'
postcode = '7151WC'
huisnummer = '9'
huisnummerToevoeging = ''

url = f'{hostname}/rest/adressen/{postcode}-{huisnummer}'

print(url)

response = requests.get(url)

bagId = response.json()[0]['bagId']

print(response.json()[0])

url = f'{hostname}/rest/adressen/{bagId}/afvalstromen'

print(url)
wasteDataRaw = requests.get(url).json()

print(wasteDataRaw[0])
print(wasteDataRaw[1])

wasteData = []

for item in wasteDataRaw:
    if not item['ophaaldatum']:
        continue
    wasteType = item['menu_title']
    if not wasteType:
        continue
    temp = {'type': (item['page_title'])}
    temp['date'] = datetime.strptime(item['ophaaldatum'], '%Y-%m-%d').strftime('%Y-%m-%d')
    wasteData.append(temp)

print(wasteData)

for x in wasteData:
    print(f"{x['type']}: {x['date']}")
