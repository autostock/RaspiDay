#include <LobotServoController.h>

#define rxPin 10
#define txPin 11

SoftwareSerial mySerial(rxPin, txPin);
LobotServoController myse(mySerial);   



void block(int t) {
  myse.moveServo(1,1500,t); //move No. 0 Servo in 1000ms to 1500 position
  delay(t-200);
  myse.moveServo(1,100,t); //move No.2 servo in 1000ms to 800 position
  delay(t-200);
}


#define TRIG0 A0
#define ECHO0 A1

void setup() {
  pinMode(13,OUTPUT);
  mySerial.begin(9600);  //opens software serial port, sets data rate to 9600 bps
  Serial.begin(115200);
  block(2000);
  //Control 5 servos, action time is 1000ms, move No.0 servo to 1300 position, move No.2 servo to 700 position, move No.4 servo to 600 position
  //Move No.6 servo to 900 position, move No.8 servo to 790 position
  //myse.moveServos(5,1000,0,1300,2,700,4,600,6,900,8,790); 
  //delay(2000);
  
  pinMode(ECHO0, INPUT);
  pinMode(TRIG0, OUTPUT);
  Serial.println("> ");
}

#define PROBES 2000

float t2cm=0.18;
int delta0=0;

/*
 * laufzeit <=22 ms für loop
 */
int readUS() { // run over and over
  static long t0;

  int delta=millis()-t0;
  if (delta>60) {
    t0+=delta;
    int v=0;
    digitalWrite(TRIG0, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG0, LOW);
    for(int i=0; i<PROBES; i++) {
      v+=digitalRead(ECHO0);
    }
    delta0=(5*delta0+v/13)/6;
    /*
    Serial.print(delta0); Serial.print(" "); 
    Serial.print(160); Serial.print(" "); 
    Serial.println(); 
    */
  }
  return delta0;
}

int parseInt() {
  int v=0;
  while(true) {
    while (Serial.available() > 0) {
      int c=Serial.read();
      //Serial.print((char)c);
      switch (c) {
        case '0':
        case '1':
        case '2':
        case '3':
        case '4':
        case '5':
        case '6':
        case '7':
        case '8':
        case '9':
          v=10*v +(c-'0');
          break;
        default:
          return v;
      }
    }
  }
  return -9;
}

/**
 * Arduino serial line usage
 * sS // set No. of Servo in [0, 6]; 0 is pseudo servo (used for setting of all servos)
 * tT // set Time t[S] (in ms)
 * pP // set Position p[S] in [30, 990]
 * x  // execute all servos
 * g  // go for one servo S
 * wT // wait
 * 
 * r  // read all Positions and remaining Time -> P1 T1 P2 T2 P3 T3 P4 T4 P5 T5 P6 T6
 * 
 * examples

  // set servo 1 to position 500 in time 1000 and go
  s1 p500 t1000 g
  s1 p0 t1000 g

  // set every servo to position 500 in time 2000 ms and execute
  s1 t2000 p500 s2 t2000 p500 s3 t2000 p500 s4 t2000 p500 s5 t2000 p500 s6 t2000 p500 x

  // as shortcut for above commands use pseudo servo 0
  s0 t2000 p500 x

  // set all servo positions to 0 and execute
  s0 p0 x

  // wait for 1000 ms (Warning!! all communication is blocked for this time)
  w1000

 */
void loop() {
  static int test=2 ;
  static int v, s, p[7], t[7], u, oldu;
  static long t0[7], m ;

  //init
  if (test==2) {
    test=1;
    for (int i=1; i<7; i++) {
      p[i]=500;
      t[i]=2000;
    }
  }
  
    u=readUS();
    if (oldu!=u) {
      oldu=u;
      Serial.print("d 1 ");
      Serial.println(u);
    }
    
  // if there's any serial available, read it:
    while (Serial.available() > 0) {
      int c=Serial.read();
      //Serial.print((char)c);
      switch (c) {
        case 'T':
          v = parseInt(); test = constrain(v, 0, 1);
          Serial.print("Testmode="); Serial.println(test);
          break;
        case 'x':
          if (test) {
            Serial.print("execute ");
            for (int i=1; i<7; i++) {
              t0[i]=m;
              Serial.print(p[i]);
              Serial.print(" "); 
              Serial.print(t[i]);
              Serial.print(i==6?"\n":" "); 
            }
          } else {
            m=millis();
            for (int i=1; i<7; i++) {
              t0[i]=m;
              myse.moveServo(i,p[i],t[i]); //move No. S Servo in T ms to P position
            }
          //myse.moveServos(6, t, 1, p[1], 2, p[2], 3, p[3], 4, p[4], 5, p[5], 6, p[6]);
          }
          break;
        case 'p':
          v = parseInt(); v = constrain(v, 30, 980);
          if (s==0) {
            for (int i=1; i<7; i++) {
              p[i]=v;
            }
          } else {
            p[s]=v;
          }
          break;
        case 't':
          v = parseInt(); v = constrain(v, 1, 30000);
          if (s==0) {
            for (int i=1; i<7; i++) {
              t[i]=v;
            }
          } else {
            t[s]=v;
          }
          break;
        case 's':
          s = parseInt(); s = constrain(s, 0, 6);
          break;
        case 'g':
          v=constrain(s, 1, 6);
          t0[v]=millis();
          if (test) {
            Serial.print("go ");
            Serial.print(v);
            Serial.print(" ");
            Serial.print(p[v]);
            Serial.print(" ");
            Serial.println(t[v]);
          } else {
            myse.moveServo(v,p[v],t[v]); //move No. S Servo in T ms to P position
          }
          break;
        case 'r':
          m=millis();
          for (int i=1; i<7; i++) {
            Serial.print(p[i]);
            Serial.print(" "); 
            Serial.print(constrain((t0[i]+t[i])-m, 0, 10000));
            Serial.print(i==6?"\n":" "); 
          }
          break;
        case 'u':
          Serial.println(u);
          break;
        case 'w':
          v = parseInt(); v = constrain(v, 1, 10000);
          Serial.print("wait ");
          Serial.println(v);
          delay(v);
          break;
        case '\n':
          Serial.println("> ");
          break;
        default:
        ;
      }
    }
}
