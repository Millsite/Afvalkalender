import logging

logger = logging.getLogger(__name__)

API = 'api'
NAME = 'afvalwijzer'
VERSION = '2023-01-06'
ISSUE_URL = 'https://github.com/Millsite/Afvalkalender/issues'

SENSOR_COLLECTORS_OPZET = {
    "alkmaar": "https://www.stadswerk072.nl",
    "alphenaandenrijn": "https://afvalkalender.alphenaandenrijn.nl",
    "berkelland": "https://afvalkalender.gemeenteberkelland.nl",
    "blink": "https://mijnblink.nl",
    "cranendonck": "https://afvalkalender.cranendonck.nl",
    "cyclus": "https://afvalkalender.cyclusnv.nl",
    "dar": "https://afvalkalender.dar.nl",
    "denhaag": "https://huisvuilkalender.denhaag.nl",
    "gad": "https://inzamelkalender.gad.nl",
    "hvc": "https://inzamelkalender.hvcgroep.nl",
    "lingewaard": "https://afvalwijzer.lingewaard.nl",
    "middelburg-vlissingen": "https://afvalwijzer.middelburgvlissingen.nl",
    "montfoort": "https://afvalkalender.cyclusnv.nl",
    "peelenmaas": "https://afvalkalender.peelenmaas.nl",
    "prezero": "https://inzamelwijzer.prezero.nl",
    "purmerend": "https://afvalkalender.purmerend.nl",
    "rmn": "https://inzamelschema.rmn.nl",
    "schouwen-duiveland": "https://afvalkalender.schouwen-duiveland.nl",
    "spaarnelanden": "https://afvalwijzer.spaarnelanden.nl",
    "sudwestfryslan": "https://afvalkalender.sudwestfryslan.nl",
    "suez": "https://inzamelwijzer.prezero.nl",
    "venray": "https://afvalkalender.venray.nl",
    "voorschoten": "https://afvalkalender.voorschoten.nl",
    "waalre": "https://afvalkalender.waalre.nl",
    "zrd": "https://afvalkalender.zrd.nl",
}

CONF_COLLECTOR = "provider"
CONF_API_TOKEN = "api_token"
CONF_POSTAL_CODE = "postal_code"
CONF_STREET_NUMBER = "street_number"
CONF_SUFFIX = "suffix"
CONF_DATE_FORMAT = "date_format"
CONF_EXCLUDE_PICKUP_TODAY = "exclude_pickup_today"
CONF_DEFAULT_LABEL = "default_label"
CONF_ID = "id"
CONF_EXCLUDE_LIST = "exclude_list"