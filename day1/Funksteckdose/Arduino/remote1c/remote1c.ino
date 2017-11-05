// spielt codes für Funksteckdosen "Type Nr. RC 402 / GXA2867"
// für Arduino UNO

int RF = 4;  // Sender
int LED = 13;
int bits = 20;  // Anzahl bits im Funksignal (lang=1,kurz=0)
int anzahl = 5;  // Anzahl Wiederholungen der Quartette
int i,j,k;
int kurzH = 600;  // Dauer µs
int kurzL = 1200;  // Dauer µs
int langH = 1200;  // Dauer µs
int langL = 600;  // Dauer µs
int pause1 = 35;  // Pause innerhalb 4er-Block
int pause4 = 20;  // Pause zwischen 4er-Blocks

unsigned long code;

unsigned long s1ein = 0b00100110001000010001;  // 0: kurz high, 1: lang high
unsigned long s1aus = 0b00100110001000000000;
unsigned long s2ein = 0b00100110001010010011;
unsigned long s2aus = 0b00100110001010000010;
unsigned long s3ein = 0b00100110001001010000;
unsigned long s3aus = 0b00100110001001000001;
unsigned long s4ein = 0b00100110001011010010;
unsigned long s4aus = 0b00100110001011000011;

void setup() {
  code = s2ein;
  pinMode(RF,OUTPUT);
  pinMode(LED,OUTPUT);
  delay(600);
  digitalWrite(LED,1);
  delay(1000);
  digitalWrite(LED,0);
  Serial.begin(9600);
  Serial.println("start");
}

void loop() {
  for (k=0;k<anzahl;k++) {
  for (j=0;j<4;j++) {
  i = bits;
  digitalWrite(RF,1);
  delayMicroseconds(langL);
  while (i>0) {
    if (bitRead(code,i-1)==0) {
      Serial.print("0");
      digitalWrite(RF,0);
      delayMicroseconds(kurzH);
      digitalWrite(RF,1);
      delayMicroseconds(kurzL);
    }
    if (bitRead(code,i-1)==1) {
      Serial.print("1");
      digitalWrite(RF,0);
      delayMicroseconds(langH);
      digitalWrite(RF,1);
      delayMicroseconds(langL);
    }
    i--;
  }
  digitalWrite(RF,0);
  Serial.println();
  delay(pause1);
  }
  delay(pause4);
  }
  digitalWrite(LED,1);
  delay(1000);
  digitalWrite(LED,0);
  while(1);
}

