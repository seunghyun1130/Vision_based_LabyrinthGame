#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <PubSubClient.h>
#include <Arduino.h> //for ethernet
// #include <ETH.h>
// #include <ESPmDNS.h>
// #include "WiFi.h"
#include "time.h"

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsgTime = 0;


// void WiFiEvent(WiFiEvent_t event)
// {
//   switch (event) {
//     case ARDUINO_EVENT_ETH_START:
//       Serial.println("ETH Started");
//       //set eth hostname here
//       ETH.setHostname("esp32-ethernet");
//       break;
//     case ARDUINO_EVENT_ETH_CONNECTED:
//       Serial.println("ETH Connected");
//       break;
//     case ARDUINO_EVENT_ETH_GOT_IP:
//       Serial.print("ETH MAC: ");
//       Serial.print(ETH.macAddress());
//       Serial.print(", IPv4: ");
//       Serial.print(ETH.localIP());
//       if (ETH.fullDuplex()) {
//         Serial.print(", FULL_DUPLEX");
//       }
//       Serial.print(", ");
//       Serial.print(ETH.linkSpeed());
//       Serial.println("Mbps");
//       eth_connected = true;
//       break;
//     case ARDUINO_EVENT_ETH_DISCONNECTED:
//       Serial.println("ETH Disconnected");
//       eth_connected = false;
//       break;
//     case ARDUINO_EVENT_ETH_STOP:
//       Serial.println("ETH Stopped");
//       eth_connected = false;
//       break;
//     default:
//       break;
//   }
// }


void setupWiFi(){
    IPAddress ip (192, 168, 0, 50); 
    IPAddress gateway (192, 168, 0, 1);
    IPAddress subnet (255, 255, 255, 0);

    WiFi.config (ip, gateway, subnet);
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);

    // Wait for connection
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    
    Serial.println("");
    Serial.print("Connected to ");
    Serial.println(ssid);
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());
}


void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == 'A') {
    digitalWrite(BUILTIN_LED, LOW);
    for(int i; i<length; i++){
      mqtt_sub[i] = (char)payload[i];
    }
  } else {
    digitalWrite(BUILTIN_LED, HIGH);  // Turn the LED off by making the voltage HIGH
  }

}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("ESP8266Client")) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("outTopic", "hello world");
      // ... and resubscribe
      client.subscribe("inTopic");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(3000);
    }
  }
}

void mqtt_publish(){
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  long now = millis();
  if (now - lastMsgTime > 2000) {
    lastMsgTime = now;

    char packet[50];
    //mqtt publishing이 char형으로만 보낼 수 있기때문에 toCharArray로 변환한다.
    Serial.print("Publish message: ");
    Serial.println(mqtt_pub);
    client.publish("maze/arduino/reply", mqtt_pub);
  }
  delay(5000); //5초 단위로 Publishing (조정가능)
}

void setupMQTTCLient(){
    // WiFi.onEvent(WiFiEvent);
    setupWiFi();
    client.setServer(mqtt_server, 1883);
    client.subscribe("maze/server/command");
    client.setCallback(callback);
}

/*
void loop() {

  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}
*/