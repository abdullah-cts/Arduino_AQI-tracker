import time
import geocoder
import requests
import schedule
import serial
import struct

API_KEY = '8cc077ec-db9b-43c3-b342-07cfbb0bb3e5'
BASE_URL = 'http://api.airvisual.com/v2/nearest_city'
arduino = serial.Serial(port='COM7', baudrate=9600, timeout=.1)

COLOR_GREEN = (0, 255, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_ORANGE = (255, 165, 0)
COLOR_RED = (255, 0, 0)
COLOR_PURPLE = (128, 0, 128)
COLOR_MAROON = (128, 0, 0)

# getting user's location based on IP address

g = geocoder.ip('me')
lat, lng = g.latlng[0], g.latlng[1]

FINAL_URL = BASE_URL + f'?lat={lat}&lon={lng}&key={API_KEY}'


def job(FINAL_URL):
    response = requests.get(FINAL_URL)
    data = response.json()
    # grabbing the aqi data from the api
    aqius = data['data']['current']['pollution']['aqius']

    if 0 <= aqius <= 50:
        # creating a struct with big-endian format,data type is unsigned char
        arduino.write(struct.pack('>BBB', COLOR_GREEN[0], COLOR_GREEN[1], COLOR_GREEN[2]))
    elif 50 < aqius <= 100:
        arduino.write(struct.pack('>BBB', COLOR_YELLOW[0], COLOR_YELLOW[1], COLOR_YELLOW[2]))
    elif 100 < aqius <= 150:
        arduino.write(struct.pack('>BBB', COLOR_ORANGE[0], COLOR_ORANGE[1], COLOR_ORANGE[2]))
    elif 150 < aqius <= 200:
        arduino.write(struct.pack('>BBB', COLOR_RED[0], COLOR_RED[1], COLOR_RED[2]))
    elif 200 < aqius <= 300:
        arduino.write(struct.pack('>BBB', COLOR_PURPLE[0], COLOR_PURPLE[1], COLOR_PURPLE[2]))
    else:
        arduino.write(struct.pack('>BBB', COLOR_MAROON[0], COLOR_MAROON[1], COLOR_MAROON[2]))


# schedule the job function to run in every 10 mins
schedule.every(10).minutes.do(job, FINAL_URL)

while True:
    schedule.run_pending()
    time.sleep(1)







