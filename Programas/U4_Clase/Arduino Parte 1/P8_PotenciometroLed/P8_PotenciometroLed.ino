// voltaje de referencia: 5v
int potenciometro = A0; // pin donde esta conectado el potenciometro
int led = 9; // pin PUM donde esta conectado el Led
int valor; // Variables par6a almacenar el valor leido del potenciometro
int brillo; // variable para almacenar el valor ajustado del brillo

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); // Inicializa la comunicacion serial
  pinMode(led, OUTPUT); // Configura el pin del Led como salida

}
void loop() {
  valor = analogRead(potenciometro); // Lee el valor del potencio
  brillo = map(valor, 0 , 1023, 0, 255)

  analogWrite(led, brillo);
  Serial.println(valor);
  delay(100);

}

