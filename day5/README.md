# Thema KI auf dem Raspberry 3 und 4

## Trainieren und anschließend Anwenden eines NN auf einem Raspi mit tensorflow.

#### Voraussetzungen

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
sudo apt-get install python3-venv
sudo apt install libjpeg-dev libtiff-dev libopenjp2-7-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk libharfbuzz-dev libfribidi-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libhdf5-dev


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

#### jetzt kann's los gehen auf der Commandline

``` bash
python lauf2.py 
python use1.py 
```


## pm-Prognose mit NN 
Könnte ein NN aus unseren Wetterdaten: tmp, hum, bmp, pm25 Daten und Wochentag von morgens um 6Uhr auf die pm25 Werte von 12Uhr des selben Tages schließen?
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

