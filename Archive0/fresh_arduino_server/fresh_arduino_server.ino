String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

void setup()
{
  Serial.begin(9600);
  Serial.println("Arduino Mega integrated. :]");
  Serial.flush();
  inputString.reserve(200);


  
}

void loop()
{
    // print the string when a newline arrives:
  if (stringComplete) {
    Serial.println(inputString); 
    Serial.flush();
    // clear the string:
    inputString = "";
    stringComplete = false;
  }



}


void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    } 
  }
}
