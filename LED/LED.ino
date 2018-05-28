//Use this to define PIN controlling LEDs
#define LED_PIN 13
bool ledStatus = false;
char receivedChar;
boolean newData = false;
void setup() {
	//Setup LEDs and start Serial connection with specified baud rate (same as the one in Python)
	pinMode(LED_PIN, OUTPUT);
	Serial.begin(9600); 
	Serial.println("Ready");
}

void loop() {
  //Receive data from Serial connection
	recvOneChar();
  //Check data from Serial connection to control LEDs
	if(ledStatus == true){
		digitalWrite(LED_PIN, HIGH);
	}else{
		digitalWrite(LED_PIN, LOW);
	}
}

void recvOneChar() {
	if (Serial.available() > 0) {
		receivedChar = Serial.read();
  //Interpret data from Serial connection to control LEDs
		if (receivedChar == '1'){
			ledStatus = true;
		}
		else{
			ledStatus = false;
		}
	}
}
