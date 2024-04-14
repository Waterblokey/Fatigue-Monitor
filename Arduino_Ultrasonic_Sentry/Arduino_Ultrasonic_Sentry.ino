//initializes ultrasonic sensor pins
const int trigPin = 10;
const int echoPin = 9;

//initializes variables
float duration, distance;

void setup() {
  //sets up pins to output and input
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  //transmitter sends signals
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
//receives time it takes for signal to travel back
  duration = pulseIn(echoPin, HIGH);
  //calculates distance in cm from duration
  distance = (duration*.0343)/2;
  Serial.print("Distance: ");
  Serial.println(distance);
  delay(100);
}