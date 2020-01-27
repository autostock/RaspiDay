# Thema KI (Keras/tensorflow) anwenden

## Aufgaben trainieren und anschließend anwenden

#### Falls Raspberry: Voraussetzungen

``` bash
uname -a
# Linux raspberrypi4 4.19.75-v7+ #1270 SMP Tue Sep 24 18:45:11 BST 2019 armv7l GNU/Linux

cat /etc/issue
# Raspbian GNU/Linux 10 \n \l

getconf LONG_BIT
# 32

python --version
# Python 3.7.3
```

#### Installation

``` bash
sudo apt update
sudo apt install python3-pip
sudo apt install python3-venv
sudo apt install libjpeg-dev libtiff-dev libopenjp2-7-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk libharfbuzz-dev libfribidi-dev
sudo apt install libatlas-base-dev
sudo apt install libhdf5-dev


mkdir KI
cd KI
python3 -m venv env
source env/bin/activate
pip3 install keras
pip3 install tensorflow
# pip3 install wheel
# pip install Pillow
pip3 install imageio

```

#### Aufgaben

##### 1. Zahlenfolgen
Funktion:<br>
Wir trainieren das NN mit 50 x aus [0, 100[ für f(x) = 5*x^2 - 3*x + 4.<br>
Wir trainieren das NN mit 50 x aus [-10, +10[ für f(x) = sin(x).<br>

Fibonacci:<br>
Wir trainieren das NN mit 50 n aus [2, 100[ für a(n)=a(n-1)+a(n-2) mit a(0)=0, a(1)=1.

##### 2. Wochentag: dow in 0 ... 6 (0 == Sonntag)
Wir trainieren das NN mit einem Datum aus 2020 d.h. zwei Input Nodes (Monat, Tag) und das NN soll lernen welcher Wochentag das ist. Dazu bedient es 7 Output Nodes. Beispiel, der 25 Januar ist ein Samstag: ( 1, 25) -> 6


##### 3. Wetterprognose
Andreas und ich haben 2019 für Nippes Wetterdaten inkl. Feinstaubbelastung gesammelt. (Siehe https://github.com/autostock/RaspiDay/tree/master/day6/Wetter) Die KI soll aus den Wetterdaten für 6 Uhr die Feinstaubbelastung für 12 Uhr des selben Tages prognostizieren.

Könnte ein NN aus unseren Wetterdaten: tmp, hum, bmp, pm25 Daten und Wochentag von morgens um 6Uhr auf die pm25 Werte von 12Uhr des selben Tages schließen?<br>
(tmp, hum, bmp, pm25, dow)[06] -> (pm25)[12]

Beispiel:

``` bash
changes	date			tmp	hum	bmp	pm25	dow	map to	pm25
10	2019-12-10 06:00:31.0	3,8	82,0	1024,0	3,5	3	-> 	5,5
3	2019-12-09 06:00:32.0	7,0	72,0	997,0	1,5	2	-> 	1,5
6	2019-12-08 06:00:32.0	9,5	71,0	1007,0	3,0	1	-> 	0,5
1	2019-12-07 06:00:26.0	9,0	84,0	1011,0	3,5	7	-> 	3,0
8	2019-12-06 06:00:26.0	1,0	80,0	1015,0	17,0	6	-> 	8,5
0	2019-12-05 06:00:32.0	0,8	83,0	1021,0	36,5	5	-> 	36,5
0	2019-12-03 06:00:33.0	6,8	86,0	1029,0	36,5	3	-> 	36,5
2	2019-12-02 06:00:32.0	1,0	83,0	1024,0	11,5	2	-> 	36,5
3	2019-12-01 06:00:32.0	2,5	78,0	1014,0	2,0	1	-> 	2,5
6	2019-11-30 06:00:32.0	3,0	83,0	1017,0	9,0	7	-> 	11,5
1	2019-11-29 06:00:31.0	8,0	82,0	999,0	3,0	6	-> 	2,5
2	2019-11-28 06:00:32.0	11,0	74,0	985,0	1,0	5	-> 	1,5
17	2019-11-27 06:00:32.0	9,5	85,0	986,0	3,5	4	-> 	1,0
0	2019-11-26 06:00:32.0	7,5	87,0	1000,0	12,0	3	-> 	12,0
0	2019-11-25 06:00:31.0	6,8	82,0	1003,0	12,0	2	-> 	12,0
12	2019-11-24 06:00:32.0	6,0	81,0	998,0	8,0	1	-> 	10,0
9	2019-11-23 06:00:32.0	5,3	79,0	993,0	7,0	7	-> 	4,5
11	2019-11-22 06:00:33.0	6,0	83,0	1000,0	15,5	6	-> 	13,0
18	2019-11-21 06:00:32.0	0,8	85,0	1005,0	11,5	5	-> 	12,5
...
```


##### 4. Garagentor auf oder zu?
Ich habe Fotos einer fest installierten WEB Cam die eine Garage Tag und Nacht (IR Licht) überwacht. Die KI soll unabhängig von den Lichtverhältnissen lernen ob das abgebildete Garagentor auf oder zu ist.

## Beschreibung einiger Dateien

XOR: mit Keras/Tensorflow lernen und anwenden
- xor.py: NN für die boolsche Funktion XOR. Mit epochs=200
- xor2.py: Wie xor.py allerdings mit epochs=2000 UND zusätzlicher Abruchbedingung wenn binary_accuracy>0.8

f(x) = 5*x^2 - 3*x + 4: mit Keras/Tensorflow lernen und anwenden
- regression1.py: NN für obige Funktion. Mit epochs=20000; python array
- regression1_a.py: Mit epochs=10000 aber inkrementel bis mean_squared_error < 10
- regression1_b.py: Mit epochs=10000 aber fahre 20 Ansätze und vertiefe besten Ansatz; numpy array

f(x) = sin(x)
- regression2.py: wie regression1_b.py

f(i) = fib(i)
- regression3.py: wie regression2.py 

Wochentag
- 2020dow.csv: 366 Tupel (Monat, Tag, dow) für alle Tage in 2020
``` bash
01,01,3
01,02,4
...
01,26,0
01,27,1
01,28,2
01,29,3
01,30,4
01,31,5
02,01,6
02,02,0
...
12,30,3
12,31,4
```
- wochentag-tf.py: Versuch mit Keras/Tensorflow die Abbildung (Monat, Tag) -> (dow) zu lernen. Da hatten wir wenig Erfolg.
- wochentag-tf2.py: Aber so geht's easy! (Monat, Tag) wird in eine 12 + 31 langen 0-Vektor gemapt. Mit einer 1 am Monatsindex und einer 1 am Tagindex. 

## Links
- xor: https://blog.thoughtram.io/machine-learning/2016/11/02/understanding-XOR-with-keras-and-tensorlow.html
- regression: https://machinelearningmastery.com/regression-tutorial-keras-deep-learning-library-python/
- Eigene Bilder klassifizieren: https://www.pyimagesearch.com/2018/09/10/keras-tutorial-how-to-get-started-with-keras-deep-learning-and-python/

- Guide to reinforcement learning: https://blog.thoughtram.io/machine-learning/2018/02/28/a-simple-guide-to-reinforcement-learning.html


