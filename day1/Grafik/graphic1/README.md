### Sammel CO2 Daten in _sensor_CO2
```bash
mosquitto_sub -h raspberrypi3 -t '/sensor/CO2' | while read -r
do
    echo `date +%Y%m%d%H%M%S` "$REPLY" | awk '{print $1";"$NF}'
done >>_sensor_CO2
```
Erzeugt solche Daten in _sensor_CO2
```bash
...
20171029114450;598
20171029114500;598
20171029114510;598
20171029114520;598
20171029114530;594
20171029114540;588
20171029114550;594
20171029114600;592
...
```

### Gnu Plot Skript graphic1.gp

```bash
# Erzeugt eine PNG Datei aus Datei _sensor_CO2 in /var/www/html/graphic1/output.png
set term png
set output '/var/www/html/graphic1/output.png'
set size 1, 1
set title "Graphic1"
set xlabel "Date"
set ylabel "CO2"

set xdata time
set timefmt "%Y%m%d%H%M%S"
set format x "%H:%M:%S"

set datafile separator ";"
plot "_sensor_CO2" using 1:2 title "CO2" with lines
```
Und starten:
```bash
gnuplot -c graphic1.gp
```
Display it http://192.168.5.47/graphic1/output.png
