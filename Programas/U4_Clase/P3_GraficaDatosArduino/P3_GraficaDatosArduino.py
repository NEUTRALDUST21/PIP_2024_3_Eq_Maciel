import serial as ser
## para que funciones primero hay que cargar los datos en arduino y luego ir al programa y correrlo
arduino = ser.Serial(port="COM4", baudrate=9600, timeout=1) ##port el es puerto que nos sale

tot_lecturas = int(input("Ingresa el total de lecturas a procesar:"))

lecturas = []

while tot_lecturas>0:
    if arduino.inWaiting(): # equivale a Serial.available()
        cadena = arduino.readline()
        cadena = cadena.decode().strip()
        if cadena != "":
            print(cadena)
            lecturas.append(int(cadena))
            tot_lecturas -= 1
print("Lecturas obtenidas")