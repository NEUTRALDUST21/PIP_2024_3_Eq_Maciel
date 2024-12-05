int  sensor = A0; // Fotoresistencia/ LDR - Potenciometro

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

int valor_sensor;

void loop() {
  valor_sensor = analogRead(sensor);
  Serial.println(valor_sensor);
  delay(100);
}