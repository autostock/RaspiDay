# Robot

Uns ist an diesem Tag tatsächlich ein improvisierter ferngesteuerter low tech Roboter (noch nicht autonom) auf Raspberry Basis gelungen.
Der Roboter steht auf einem Sektkorken mit Filzgleiter und zwei Conrad Motoren inklusive Getriebe. Des weiteren befinden sich
im Robotergehäuse (Karton) ein Adafruit Motor Shield v2 auf einem Arduino UNO und eine 5V Powerbank. Auf dem Robotergehäuse befindet
sich ein Raspberry Pi 3 (hier RPi Y genannt) und ein Breadboard welches über 3 LEDs den Zustand von Motor1 anzeigt und ein Ultraschall 
Entfernungsmesser. (Detailierter Fotos folgen.)

Die Architektur folgt nicht ganz dem Eingangs ewähnten Beispiel 2, sondern sieht wie folgt aus:

Die Motoren werden von einem Adafruit Motor Shield v2 angesteuert welches als Shield auf einem Arduino UNO sitzt. 
Die Spannungsversorgung des Motor Shields liefert der UNO über USB. Im UNO läuft das Programm
*DCAdafruitMotorShieldv2_3RaspiRobot1.ino* welches Kommandos an die Motoren in plain Text von der seriellen Schnittstelle annimmt und umsetzt.

Die Kommandos lauten:
```bash
[FfBb] <speed>
[Rr]
```

- F steht für FORWARD Motor1
- B steht für BACKWARD Motor1
- R steht für RELEASE Motor1

- Entsprechend f, b und r für Motor2.

- <speed> liegt zwischen 0 und 255.

Die Kommandos an den UNO schickt RPi Y via USB. Dazu läuft ein Phyton Programm, dass die Kommandos einer
Fernsteuerung via MQTT entgegen nimmt, subscribe topic: "/sensor/e-sky". Die MQTT Messages (/sensor/e-sky) transportieren 
im Prinzip rohe Analogwerte aller Steuerknüppel der Fernbedienung.

An einem zweiten Raspberry Pi 3 (hier RPi X genannt) ist die E-Sky Fernsteuerung via USB angeschlossen. Die Analogwerte aller Steuerknüppel werden in das MQTT Netz gespeist,
public "sensor/e-sky". (Genaueres siehe day1.)

Datenfluss:
(E-Sky)--USB-->(RPi X)--MQTT-->(WLAN)--MQTT-->(RPi Y)--USB-->(UNO)-->(MotorShield)-->(Motor 1+2)

Stromversorgung:
Das Powerpack versorgt direkt den RPi Y. Dieser versorgt über seine USB Schnittstelle den UNO 
und dieser das MotorShield und damit auch die Motoren. D.h. die Motoren haben z.Zt. keine unabhängige Spannungsversorgung.