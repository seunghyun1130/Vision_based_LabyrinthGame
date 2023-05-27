#include <Adafruit_NeoPixel.h>
#include "config.h"

Adafruit_NeoPixel pixels(NUMPIXELS, PIXELPIN, NEO_GRB + NEO_KHZ800);

void setupLED(){
    pixels.begin();
}

void turnON(){
    for(int i=0; i<NUMPIXELS; i++){
        // G R B order
        pixels.setPixelColor(i,180,180,180);
        pixels.show();
  }
}

void red(){
    
}
