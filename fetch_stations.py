from requests import get

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'

stations = get(url).json()['items']
