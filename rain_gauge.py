import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.IN)
GPIO.add_event_detect(15, GPIO.RISING)

tamanho_balancin = 0.2794
contador_hora = 0
contador_total = 0

def balancin_cae():
    global contador_total
    global contador_hora
    contador_total = contador_total + 1

    
    
while True:

    if GPIO.event_detected(15):
        balancin_cae()
        print('Cantidad Lluvia: ' + str(contador_total*tamanho_balancin))
