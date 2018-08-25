import time
import Adafruit_MCP3008

while True:
# Configuracion tipo SOFTWARE SPI:
    CLK  = 18
    MISO = 23
    MOSI = 24
    CS   = 25
    mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

    voltaje_digital = mcp.read_adc(0)
    voltaje_analogico = 5*voltaje_digital/1024

    v = voltaje_analogico
    
    if v < 4.7 and v > 4.4:
        direccion = 'Este'
    elif v < 2.9 and v > 2.5:
        direccion = 'Noreste'
    elif v < 1.3 and v > 1:
        direccion = 'Norte'
    elif v < 0.8 and v > 0.5:
        direccion = 'Noroeste'
    elif v < 0.4 and v > 0.2 :
        direccion = 'Oeste'
    elif v < 2 and v > 1.8:
        direccion = 'Suroeste'
    elif v < 3.7 and v > 3.4:
        direccion = 'Sur'
    elif v < 4.3 and v > 4 :
        direccion = 'Sureste'

    print(direccion)
    

    time.sleep(1)


