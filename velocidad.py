import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.IN)
GPIO.add_event_detect(15, GPIO.RISING)

velocidad_1 = 2.4
contador = 0
tiempo_muestreo = 10

def contador_():
    global contador
    contador = contador + 1

    
    
while True:

    tiempo_inicio = int(time.strftime("%S",time.localtime()))
    tiempo_fin = int(time.strftime("%S",time.localtime()))

    while (abs(tiempo_inicio - tiempo_fin) < tiempo_muestreo):

        if GPIO.event_detected(15):
            contador_()
        tiempo_fin = int(time.strftime("%S", time.localtime()))
        

    print('Velocidad del viento: ' + str(contador*velocidad_1/10) + 'km/h')
    contador = 0
