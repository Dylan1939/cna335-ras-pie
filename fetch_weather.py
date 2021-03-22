from pprint import pprint

from requests import get

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestwsdata/1648902'
weather = get(url).json()['items']
pprint(weather)
