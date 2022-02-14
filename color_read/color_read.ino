// Define pins for LED
int red_light_pin= 11;
int green_light_pin = 10;
int blue_light_pin = 9;

int color[3];

void setup() {
  pinMode(red_light_pin, OUTPUT);
  pinMode(green_light_pin, OUTPUT);
  pinMode(blue_light_pin, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  while(Serial.available() >= 3){ 
    for(int i = 0; i < 3; i++){
      color[i] = Serial.read();
    }
    RGB_color(color[0], color[1], color[2]);
  }
} 

void RGB_color(int red_light_value, int green_light_value, int blue_light_value)
 {
  analogWrite(red_light_pin, red_light_value);
  analogWrite(green_light_pin, green_light_value);
  analogWrite(blue_light_pin, blue_light_value);
}
