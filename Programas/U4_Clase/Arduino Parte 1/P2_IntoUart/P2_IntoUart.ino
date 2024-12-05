int led = 2;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT); // lo confiuguras como salida
  Serial.begin(9000);
  Serial.setTimeout(10);
  // intervalo de los segundos en lo que el buffer pueda leer y si esta en el intervalo
  // toma todos en ese intervalor y lo toma como si fuera u valor :DDD
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.avalible()>0){
    int v = Serial.readString().toInt();
    digitalwrite(led, v);
  }
  
}