#include <Servo.h>
#include <NewPing.h>

const int VELOCITAT_COMUNICACIO_SERIAL = 9600;

const int EXTRA_VCC = 13;

const int PIN_SERVO = 11;

const int ULTRASONIC_TRIG = 8;
const int ULTRASONIC_ECHO = 9;
const int DISTANCIA_ULTRASONICA_MAXIMA = 200;

NewPing sonar(ULTRASONIC_TRIG, ULTRASONIC_ECHO, DISTANCIA_ULTRASONICA_MAXIMA);

const int POSICIO_SERVO_DEFAULT = 90;

Servo servo;

int posicioServo = POSICIO_SERVO_DEFAULT;
int direccioServo = -5; // ESQUERRA

void setup() {
  iniciarServo();
  Serial.begin(VELOCITAT_COMUNICACIO_SERIAL);
  pinMode(ULTRASONIC_TRIG, OUTPUT);
  pinMode(ULTRASONIC_ECHO, INPUT);
  digitalWrite(ULTRASONIC_TRIG, LOW);

  pinMode(EXTRA_VCC, OUTPUT);
  digitalWrite(EXTRA_VCC, HIGH);
}

void loop() {
  if(posicioServo < 9 || posicioServo > 170) {
    direccioServo = direccioServo * -1;
  }
  posicioServo += direccioServo;
  rotarAngle(posicioServo);

  calculDades();

  delay(300);
}

void rotarAngle(int direccio) {
  servo.write(direccio);
}

/**
 * Imprimeix un paquet JSON pel port serial amb les dades
 * 
 * @param int angle L'angle del servomotor
 * @param float  distance La distància mesurada en cm
 */
void imprimirDades(int angle, float distancia) {
  Serial.print("{\"angle\": ");
  Serial.print(angle);
  Serial.print(", \"distance\": ");
  Serial.print(distancia);
  Serial.print("}"); 
  Serial.println();
}

void iniciarServo() {
  pinMode(PIN_SERVO, OUTPUT);
  digitalWrite(PIN_SERVO, LOW);
  servo.attach(PIN_SERVO);
  servo.write(POSICIO_SERVO_DEFAULT);
}

void calculDades() {
  float distance = sonar.ping_cm();
  imprimirDades(posicioServo, distancia);
}
