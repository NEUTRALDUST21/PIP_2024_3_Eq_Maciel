int led[] = {2,3,4,5,6,7,8,9};
bool estados[] = {false,false,false,false,false,false,false,false};

void setup() {
  // put your setup code here, to run once:
  for (int i=0; i<8; i++){
    pinMode(led[i], OUTPUT);
  }

  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.avalible()>0){
    int idx_led = Serial.readString().toInt()-1;
    estados[idx_led] = !estados[idx_led];
    digitalWrite(led[idx_led],estados[idx_led]);
    if (estados[idx_led]){
      Serial.println("LED " + String(idx_led + 1) + " encendido");
    }else{
      Serial.println("LED " + String(idx_led + 1) + " apagado");
    }
  }

  delay(100);
  
}