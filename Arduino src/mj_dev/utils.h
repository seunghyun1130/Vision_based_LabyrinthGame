#include <Arduino.h> 

unsigned long long int uS_TO_S_FACTOR = 1000000ULL;
unsigned long long int TIME_TO_SLEEP = 0;
RTC_DATA_ATTR int bootCount = 0;

struct errcnt {
    unsigned short success = 0;
    unsigned short fail = 0;
};
struct errcnt err_api;
struct errcnt err_wt901_1;
struct errcnt err_wt901_2;

void reboot()
{
    Serial.println("system reboot");
    ESP.restart();
}

void errcnt_countup(struct errcnt* count, int fail)
{
    if (fail) {
        count->success = 0;
        count->fail++;
        if (count->fail == ERRCNT_FAIL_THRESHOLD)

            reboot();
    } else {
        count->success++;
        if (count->success >= ERRCNT_SUCCESS_THRESHOLD) {
            count->success--;
            count->fail = 0;
        }
    }
}



void print_wakeup_reason() {
  esp_sleep_wakeup_cause_t wakeup_reason;

  wakeup_reason = esp_sleep_get_wakeup_cause();

  switch (wakeup_reason)
  {
    case ESP_SLEEP_WAKEUP_EXT0 : Serial.println("Wakeup caused by external signal using RTC_IO"); break;
    case ESP_SLEEP_WAKEUP_EXT1 : Serial.println("Wakeup caused by external signal using RTC_CNTL"); break;
    case ESP_SLEEP_WAKEUP_TIMER : Serial.println("Wakeup caused by timer"); break; //should always be this
    case ESP_SLEEP_WAKEUP_TOUCHPAD : Serial.println("Wakeup caused by touchpad"); break;
    case ESP_SLEEP_WAKEUP_ULP : Serial.println("Wakeup caused by ULP program"); break;
    default : Serial.printf("Wakeup was not caused by deep sleep: %d\n", wakeup_reason); break;
  }
}

void config_sleep_mode() {
  esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR);
  Serial.print("Setup ESP32 to sleep for every ");
  Serial.print(TIME_TO_SLEEP);
  Serial.println(" Seconds");
  print_wakeup_reason();
}
