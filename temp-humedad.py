import RPi.GPIO as GPIO
import sys
import Adafruit_DHT

while True:
    humedad, temperatura = Adafruit_DHT.read_retry(11,4)
    print ('Temp: {0:0.1f} C  Humidity:{1:0.1f} %'.format(temperatura, humedad))
