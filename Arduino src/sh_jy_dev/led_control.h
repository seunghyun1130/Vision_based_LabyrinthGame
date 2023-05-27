#include <Adafruit_NeoPixel.h>
#include "config.h"

Adafruit_NeoPixel pixels(NUMPIXELS, PIXELPIN, NEO_GRB + NEO_KHZ800);

void setupLED(){
    pixels.begin();
}

void turnON(){
   pixels.setPixelColor(0,0,255,0);
   pixels.show();
   pixels.setPixelColor(1,255,0,0);
   pixels.show();
    for(int i=2; i<NUMPIXELS; i++){
        // G R B order
        pixels.setPixelColor(i,180,180,180);
        pixels.show();
  }
}


if (WiFi.status() == WL_CONNECTED){
   pixels.setPixelColor(0,0,0,255);
   pixels.show();
}

else{
  pixels.setPixelColor(0,0,255,0);
  pixels.show();
}


if ((char)payload[0] == 'A'){
   pixels.setPixelColor(0,0,0,255);
   pixels.show();
}

else{
  pixels.setPixelColor(0,0,255,0);
  pixels.show();
}
