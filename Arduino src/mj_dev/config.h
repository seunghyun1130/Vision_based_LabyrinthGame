const int servo1Pin = 10; // 서보 핀
const int servo2Pin = 9; // 서보 핀
const int ledR = 11;
const int ledB = 12;

const int buttonPin2 = 2;
const int buttonPin3 = 3;
const int buttonPin4 = 4;
const int buttonPin5 = 5;

const int Address = 0x50;

const char* ssid = "U+Net850C";
const char* password = "C87568BJ$F";
const char* mqtt_server = "pc IP";


#define SENSOR_ACC1_X 600
#define SENSOR_ACC1_Y 601
#define SENSOR_ACC1_Z 602
#define SENSOR_ANG1_X 603
#define SENSOR_ANG1_Y 604
#define SENSOR_ANG1_Z 605
#define SENSOR_ANGVEL1_X 606
#define SENSOR_ANGVEL1_Y 607
#define SENSOR_ANGVEL1_Z 608
#define ERRCNT_FAIL_THRESHOLD 10
#define ERRCNT_SUCCESS_THRESHOLD 3

#define ETH_POWER_PIN   16
#define ETH_MDC_PIN     23
#define ETH_MDIO_PIN    18
#define ETH_ADDR        1
#define ETH_CLK_MODE    ETH_CLOCK_GPIO0_IN
#define ETH_TYPE        ETH_PHY_LAN8720
static bool eth_connected = false;

#define RXD2_PIN 5
#define TXD2_PIN 17

#define NUMPIXELS 60
#define PIXELPIN 13

// GLOBAL BUFFERS
// for ino & network_fn
int state = 1;
// for network_fn
char mqtt_sub[50];
char mqtt_pub[50];