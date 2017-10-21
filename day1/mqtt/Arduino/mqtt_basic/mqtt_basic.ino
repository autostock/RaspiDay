/*
 Basic MQTT example

 This sketch demonstrates the basic capabilities of the library.
 It connects to an MQTT server then:
  - publishes "hello world" to the topic "outTopic"
  - subscribes to the topic "inTopic", printing out any messages
    it receives. NB - it assumes the received payloads are strings not binary

 It will reconnect to the server if the connection is lost using a blocking
 reconnect function. See the 'mqtt_reconnect_nonblocking' example for how to
 achieve the same result without blocking the main loop.
 
*/

#include <SPI.h>
#include <BridgeClient.h>
#include <PubSubClient.h>
#include <FastLED.h>

#define LED_PIN     3
//#define NUM_LEDS    265 unstable
#define NUM_LEDS    260
#define LED_TYPE    WS2812B
#define COLOR_ORDER GRB
CRGB leds[NUM_LEDS];

// Update these with values suitable for your network.
//byte mac[]    = {  0xDE, 0xED, 0xBA, 0xFE, 0xFE, 0xED };
//IPAddress ip(172, 16, 0, 100);
IPAddress server(192, 168, 178, 32);

void callback(char* topic, byte* payload, unsigned int length) {
  /*
  Console.print(F("Message arrived ["));
  Console.print(topic);
  Console.print(F("] "));
  for (int i=0;i<length;i++) {
    Console.print((char)payload[i]);
  }
  Console.println();
  */
  CRGB rgb= CRGB(0,0,0);
  switch (payload[0]) {
    case '4': rgb= CRGB(255,0,0);   break;
    case '5': rgb= CRGB(0,0,255);   break;
    case '6': rgb= CRGB(0,255, 0);   break;
    case '7': rgb= CRGB(0, 255, 255);   break;
    case '8': rgb= CRGB(255, 255, 0);   break;
    case '9': rgb= CRGB(255, 0, 255);   break;
    default: ;
  }
  for(int i=0; i<NUM_LEDS; i++) {
      leds[i]=rgb;
  }
}

BridgeClient  ethClient;
PubSubClient client(ethClient);

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Console.print(F("Attempting MQTT connection..."));
    // Attempt to connect
    if (client.connect("arduinoClient")) {
      Console.println(F("connected"));
      // Once connected, publish an announcement...
      client.publish("/sensor/outTopic","hello world");
      // ... and resubscribe
      client.subscribe("/actor/linoino");
    } else {
      Console.print(F("failed, rc="));
      Console.print(client.state());
      Console.println(F(" try again in 5 seconds"));
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup()
{
  Bridge.begin();
  Console.begin();

  client.setServer(server, 1883);
  client.setCallback(callback);

  // Allow the hardware to sort itself out
  delay(3000);
  Console.println(F("pubsubdemo demo"));
  FastLED.addLeds<LED_TYPE, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS);
}

void loop()
{
    if (!client.connected()) {
      reconnect();
    }
  client.loop();
//  Console.print(count);
//  Console.println(F(" pubsubdemo demo"));
    FastLED.show();
}
