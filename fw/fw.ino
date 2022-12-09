//------------------------------//
// GB SI  | Ardu MOSI | Pin 3   //
// GB SO  | Ardu MISO | Pin 2   //
// GB CLK | Ardu CLK  | Pin 5   //
// GB SD  | 5V        | Pin 4   //
//----------------------------- //


#include <SPI.h>
int temp = 0xFE;
int data_in = 0xFE;//dumb temp vars
int last_out = 0xFE;

void setup() {
    Serial.begin(19200);
    Serial.setTimeout(1);
    SPI.beginTransaction(SPISettings(17000, MSBFIRST, SPI_MODE3)); //Double default clock speed, MSB and mode 3 are gameboy spi modes
    SPI.setClockDivider(SPI_CLOCK_DIV8);
    SPI.begin();
}

void loop() {
    temp = Serial.readString().toInt();
    if(temp != 254) { //TODO: change to unused num to 0s can be sent, also allow changing it via py
      last_out=temp;
      data_in = SPI.transfer(temp);
      Serial.println(last_out + "," + data_in);
    } else {
      data_in = SPI.transfer(last_out);
      Serial.println(last_out + "," + data_in);
    }
    delay(60);
}
