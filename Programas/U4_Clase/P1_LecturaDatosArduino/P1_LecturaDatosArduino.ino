int  led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(100);
}
void loop() {
  if(Serial.available()>0){
    int r = Serial.readString().toInt();
    digitalWrite(led, r);
  }
  delay(100);
}