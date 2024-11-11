// voltaje de referencia: 5v
int potenciometro = A0; // en el arduino sale A0,A1,A2

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  //pinmode no se utiliza para pines analogicos...
  // nota: un pin analogico solo es de entrada...
}
void loop() {
  int valor;
  // put your main code here, to run repeatedly:
  valor = analogRead(potenciometro);
  Serial.println(valor);
  delay(100);

}