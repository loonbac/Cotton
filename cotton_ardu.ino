#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

String linea1 = "";
String linea2 = "";
bool actualizar = false;
unsigned long ultimaActualizacion = 0;
int offset1 = 0;
int offset2 = 0;

void setup() {
  lcd.begin(16, 2);
  Serial.begin(9600);
  
  // Mensaje de bienvenida
  lcd.setCursor(0, 0);
  lcd.print("  COTTON TELAR  ");
  lcd.setCursor(0, 1);
  lcd.print("   Esperando... ");
  delay(2000);
  lcd.clear();
}

void loop() {
  static String input = "";
  static bool recibiendoLinea1 = true;

  // Leer datos desde Serial
  while (Serial.available() > 0) {
    char c = Serial.read();
    
    if (c == '\n') {
      if (recibiendoLinea1) {
        linea1 = input;
        recibiendoLinea1 = false;
      } else {
        linea2 = input;
        recibiendoLinea1 = true;
        actualizar = true;
        offset1 = 0;
        offset2 = 0;
      }
      input = "";
    } else if (c != '\r') {  // Ignorar retorno de carro
      input += c;
    }
  }

  // Actualizar pantalla con scroll
  if (actualizar) {
    scrollLCD();
  }
}

void scrollLCD() {
  if (millis() - ultimaActualizacion >= 300) {
    lcd.clear();
    
    // Línea 1
    lcd.setCursor(0, 0);
    if (linea1.length() <= 16) {
      lcd.print(linea1);
    } else {
      String scrollText1 = linea1 + "   ";
      int maxOffset1 = scrollText1.length() - 16;
      if (offset1 > maxOffset1) offset1 = 0;
      lcd.print(scrollText1.substring(offset1, offset1 + 16));
      offset1++;
    }
    
    // Línea 2
    lcd.setCursor(0, 1);
    if (linea2.length() <= 16) {
      lcd.print(linea2);
    } else {
      String scrollText2 = linea2 + "   ";
      int maxOffset2 = scrollText2.length() - 16;
      if (offset2 > maxOffset2) offset2 = 0;
      lcd.print(scrollText2.substring(offset2, offset2 + 16));
      offset2++;
    }
    
    ultimaActualizacion = millis();
  }
}