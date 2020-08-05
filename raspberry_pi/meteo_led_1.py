from signal import pause
from requests import get
import matplotlib.pyplot as plt
from dateutil import parser
from gpiozero import LED

rouge = LED(4)
bleu = LED(22)
blanc = LED(21)

stationID = '505367'
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/' + stationID
weather = get(url).json()

temp        = weather['items'][0]['ambient_temp']
humidity    = weather['items'][0]['humidity']
print(temp)
print(humidity)

if(temp <= 12):
    bleu.on()
elif(temp > 12):
    rouge.on()
    
if(humidity > 50):
    blanc.on()
