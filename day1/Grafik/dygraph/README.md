## Zeige CO2 Daten mit dygraph (via Apache)

1. Kopiere dygraph.min.js nach /var/www/html/dygraph/dygraph.min.js
2. Kopiere dygraph.html (hier im Directory) nach /var/www/html/dygraph/dygraph.html
3. Erzeuge eine Datei /var/www/html/dygraph/testCO2.csv mit z.B. folgendem Inhalt:
```bash
Date, CO2
2017-10-30 21:31:01, 1102
2017-10-30 21:31:11, 1106
2017-10-30 21:31:21, 1108
2017-10-30 21:31:31, 1102
2017-10-30 21:31:41, 1106
2017-10-30 21:31:51, 1108
2017-10-30 21:32:01, 1102
2017-10-30 21:32:11, 1100
2017-10-30 21:32:21, 1092
2017-10-30 21:32:31, 1074
...
```
4. Test mit http://192.168.5.47/dygraph/dygraph.html
