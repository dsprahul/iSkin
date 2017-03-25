
String readstring,alpha,beta;
int alphan,betan;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Connection OK! :) ");
  pinMode(13,OUTPUT);


}

void loop() {
  // put your main code here, to run repeatedly:
  
while(!Serial.available()) {}
  // serial read section
  while (Serial.available())
  {
    if (Serial.available() >0)
    {
      char c = Serial.read();  //gets one byte from serial buffer
      readstring += c; //makes the string readString
      delay(5);
    }
  }

if (readstring.length() >0)
{

if (readstring == "344\n")
{
  
 while (Serial.available())
  {
    if (Serial.available() >0)
    {
      char c = Serial.read();  //gets one byte from serial buffer
      alpha += c; //makes the string readString
      delay(5);
    }
  }
  
alphan = alpha.toInt();
Serial.print ("Into alpha");
Serial.println (alphan);

}

else if (readstring == "44\n")
{
while (Serial.available())
  {
    
    if (Serial.available() >0)
    {
      char c = Serial.read();  //gets one byte from serial buffer
      beta += c; //makes the string readString
      delay(5);
    }
  }
  
  
betan = beta.toInt();
Serial.print ("Into beta");
Serial.println (betan);
}
}


  if (readstring.length() >0)
  {
    
    //Serial.println(readstring); //see what was received
    //Serial.println(alphan);
    //Serial.println(betan);
  }
for(int d = 0;d<10;d++){
  digitalWrite(13,HIGH);
  delay(alphan);
digitalWrite(13,LOW);
  delay(betan);}
  

  //delay(50);
  readstring = "";
  beta = "";
  alpha = "";




}

