void setup(){
  //start serial connection
  Serial.begin(9600);
  //configure pin2 as an input and enable the internal pull-up resistor
  pinMode(5, INPUT_PULLUP);
  pinMode(6, OUTPUT);
  pinMode(2, OUTPUT);
 
}
 
void loop(){
  //read the pushbutton value into a variable
  int sensorVal = digitalRead(5);
  //print out the value of the pushbutton
  Serial.println(sensorVal);
 
  if (sensorVal == HIGH) {
    //digitalWrite(6, LOW);
  }
  else {
    digitalWrite(6, HIGH);
    digitalWrite(2, HIGH);
    delay(70000);
    digitalWrite(6, LOW);
    digitalWrite(2, LOW);
  }
  delay(1000);
}
