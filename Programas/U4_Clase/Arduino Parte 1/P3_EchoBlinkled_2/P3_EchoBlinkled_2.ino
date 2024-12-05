int led= 13; // parte positiva al pin 13
ini led2 = 2;
// parte positiva al pin y parte negativa va a la tierra
// dentro del led parte mas grate
void setup() {
  Serial.begin(9600);
  
  pinMode(led,OUTPUT);
  pinMode(led2,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalwrite(led,HIGH); // despues de un segundo
  delay(3000); // tres segundo
  digitalwrite(led,LOW); // despues de un segundo
  delday(1000);// un segundo

    digitalwrite(led2,HIGH); // despues de un segundo
  delay(5000); // cinco segundo
  digitalwrite(led2,LOW); // despues de un segundo
  delday(1000);// un segundo
}
