#define DEBUG

#define SPI_SS 10 //Slave Select

const int BUFSIZE = 64;

char buffer[BUFSIZE];
int bufPos = 0;

void setup() 
{  
  Serial.begin(9600);

  //SPI Bus setup
  DDRB |= (1<<2)|(1<<3)|(1<<5);    // SCK, MOSI and SS as outputs
  SPCR |= (1<<MSTR);               // Set as Master
  SPCR |= (1<<SPR0)|(1<<SPR1);     // divided clock by 128
  SPCR |= (1<<SPE);                // Enable SPI

  // Make sure matrix is deactivated
  digitalWrite(SPI_SS,HIGH); 
} 

 
void loop() 
{
  char pixel;
  
  while(Serial.available() > 0) {
    pixel = Serial.read();
    
    #ifdef DEBUG
    Serial.print(pixel,DEC);
    #endif

    if (bufPos <(BUFSIZE -1)) {
      buffer[bufPos] = pixel;
      bufPos++;
    } else {
      #ifdef DEBUG
      Serial.println("Buffer Full!");
      #endif
        
      processBuffer(buffer);
      bufPos = 0;
    }
  }
  
}

// Send buffer data to matrix
void processBuffer(const char *data){
  digitalWrite(SPI_SS, LOW);
  delay(100);
  for(int i=0; i<BUFSIZE; i++){
    spi_write(data[i]);
    Serial.print(data[i]);
   }
   digitalWrite(SPI_SS, HIGH);
   delay(100);
}

// Send single byte do matrix
void spi_write(volatile char data)
{
  SPDR = data;     
  // Wait for transmission to end  
  while (!(SPSR & (1<<SPIF)))     
  {};
}
