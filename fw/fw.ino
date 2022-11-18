//------------------------------//
// GB SI  | Ardu MOSI | Pin 3   //
// GB SO  | Ardu MISO | Pin 2   //
// GB CLK | Ardu CLK  | Pin 5   //
// GB SD  | 5V        | Pin 4   //
//----------------------------- //


#include <SPI.h>
uint8_t temp = 0xFD;
uint8_t data_in = 0xFE;//dumb temp vars
uint8_t last_out = 0xFF;

void setup() {
    Serial.begin(19200);
    Serial.setTimeout(100);
    SPI.beginTransaction(SPISettings(17000, MSBFIRST, SPI_MODE3)); //Double default clock speed, MSB and mode 3 are gameboy spi modes
    SPI.setClockDivider(SPI_CLOCK_DIV8);
    SPI.begin();
}

void loop() {
    temp = Serial.readString().toInt();
    if(temp != 0) { //TODO: change to unused num to 0s can be sent
      Serial.print("Sent: ");
      Serial.println(temp);
      last_out=temp;
      data_in = SPI.transfer(temp);
    } else {
      Serial.print("Sent: ");
      Serial.println(last_out);
      data_in = SPI.transfer(last_out);
    }
    Serial.print("Got: ");
    Serial.println(data_in, HEX);
    delay(60);
}
