int v; // declarar variable
void setup() {
  Serial.begin(9600); // iniciazar para todo 9600
  Serial.setTimeout(2000); // el tiempo que se va a a esperar a leer todo los bytes que puedan dentro del rango de tiempo
  // todos los datos que se manden dentro de esos 2 segundos 1,2,3,4,5 los junta porque esta dentro del rango 12345.

  //Serial.setTimeout(2000); Intervalo de los segundos en lo que el buffer pueda leer y  si esta en el intervalo
  // toma todos en este intervalo y la toma com si fuera un valor :DDD
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){ // si serial es mayor a 0

    // read String leera a todos los bytes que le sea posible antes de querer por defecto el timeuot es de 1 segundo

    v= Serial.readString().toInt(); // lo lee como un string
    Serial.println(v); // imprime la variable

  }
}
