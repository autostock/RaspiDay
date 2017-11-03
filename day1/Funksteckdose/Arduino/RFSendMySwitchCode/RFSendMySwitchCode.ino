/*
  Modified from Example for different sending methods in  
  https://github.com/sui77/rc-switch/ 
*/
#include <RCSwitch.h>

RCSwitch mySwitch = RCSwitch();

void setup() {
  // Transmitter is connected to Arduino Pin #10  
  mySwitch.enableTransmit(10);

  // Optional set pulse length.
  // mySwitch.setPulseLength(320);
  
  // Optional set protocol (default is 1, will work for most outlets)
  // mySwitch.setProtocol(2);
  
  // Optional set number of transmission repetitions.
  //mySwitch.setRepeatTransmit(5);
  
}

void loop() {

  mySwitch.setPulseLength(346);
  mySwitch.setRepeatTransmit(15);

  /* channel 4; dev 3; on */ 
  mySwitch.sendTriState("FFF0FF0FFFFF");
  delay(1000);  
  /* channel 4; dev 3; off */ 
  mySwitch.sendTriState("FFF0FF0FFFF0");

  delay(1000);
}
