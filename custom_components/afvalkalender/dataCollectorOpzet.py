import requests
import json
from datetime import datetime

from ..const.const import (
    logger,
    SENSOR_COLLECTORS_OPZET)

def getWasteData(
    provider,
    postalCode,
    houseNumber,
    suffix
):

    if provider not in SENSOR_COLLECTORS_OPZET.keys():
        raise ValueError(f'Invalid provider: {provider}, please verify')

    try:
        bagId = None
        suffix = suffix.strip().upper()
        url = f"{SENSOR_COLLECTORS_OPZET[provider]}/rest/adressen/{postalCode}-{houseNumber}"
        rawResponse = requests.get(url)
    except requests.exceptions.RequestException as err:
        raise ValueError(err) from err
    
    try:
        response = rawResponse.json()
    except ValueError as e:
        raise ValueError(f"Invalid or no data received from {url}") from e

    if not response:
        logger.error("No waste data found!")
        return
    
    try:
        if len(response) > 1 and suffix:
            for item in response:
                if (
                    item['huisletter'] == suffix
                    or item['huisnummerToevoeging'] == suffix
                ):
                    bag_id = item['bagId']
                    break
        else:
            bag_id = response[0]['bagId']
        
        url = f"{SENSOR_COLLECTORS_OPZET[provider]}/rest/adressen/{bag_id}/afvalstromen"
        wasteDataRaw = requests.get(url).json()
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

    except ValueError as exc:
        raise ValueError(f"Invalid and/or no data received from {url}") from exc

    return wasteData

if __name__ == "__main__":
    print(f"Valar morghulis, valar dohaeris!")