import serial as ser
## para que funciones primero hay que cargar los datos en arduino y luego ir al programa y correrlo
arduino = ser.Serial(port="COM4", baudrate=9600, timeout=1) ##port el es puerto que nos sale

while True:
   estado_led = input("Ingresa el estado del led: 1 = ON, 0 = OFF")
   arduino.write(estado_led.encode())
   print("Estado Actualizado")