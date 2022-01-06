# Thema Feinstaubsensor und python/jupyter auf dem Raspberry

Der IKEA Vindriktning FeinstaubSensor wurde (auch) von uns gehackt und
sendet dadurch via MQTT und WLAN seine Daten ins Netz.
https://www.cnx-software.com/2021/11/10/ikea-pm2-5-air-quality-sensor-esp8266-wifi-hack-mqtt-tasmota/

Wir wollten Erfahrung mit dem python/jupyter notebook machen.
https://jupyter.org/try

Die Aufgabe war, damit obige MQTT Daten zu sammeln und zu visualisieren.

## Tasmota auf ESP01 bringen

Voraussetztung ist eine vorhanden Pyhton Installation.

``` bash
pip install esptool
```

Download tasmota for esp32 from:

https://github.com/tasmota/install/blob/main/firmware/unofficial/tasmota-allsensors.bin

Tasmota Firmware auf ESP01 flashen:

``` bash
esptool --port /dev/ttyUSB0 write_flash -fm dout -fs 1MB 0x00000 tasmota-allsensors.bin
```

## Das jupyter notebook auf dem Raspberry installieren

``` bash
# pip install notebook
pip3 install notebook
pip3 install paho-mqtt

pip3 install matplotlib
# jupyter notebook

.local/bin/jupyter notebook password

.local/bin/jupyter notebook --port=7777

```

``` bash
# On the other client ssh to 192.168.179.2 via:
# ssh -L 7777:localhost:7777 pi@192.168.179.2
# and start browser with: http://localhost:7777
```

## pms5003 Verdrahtung

https://www.vueville.com/wp-content/uploads/2020/03/Arduino-Air-Quality-Sensor-Connection-Diagram-VueVille-2048x938.jpg

## Auslesen der Mehr Ressourcen: Kompilieren auf t3a.2xlarge-EC2-Instanz (unlimited, 8cores, 32GB RAM) bei AWS.amazon.com:

1. Umgebung nach tensorflow.org, ohne virtual environment
2. target-Option für bazel: --cops=-march=core2

-> FAILED: Build did NOT complete successfully, evtl. Python2/3 Inkompatibilität?

bazel --host_force_python=PY3 build --copt=-march=core2 //tensorflow/tools/pip_package:build_pip_package &

-> Fatal error: can't close bazel-out/host/bin/external/llvm/_objs/selection_dag/DAGCombiner.pic.o: No space left on device

-> Platte (8GB) voll!


-> kompiliert

-> auf PC nicht installierbar, PyCObject-Problem: Probleme zwischen Python 2 und 3 ?!

Anstatt dem auf den Grund zu gehen, aus dem Gelernten noch ein Mal auf PC versuchen:


## Hilfreiche Links

https://www.cnx-software.com/2021/11/10/ikea-pm2-5-air-quality-sensor-esp8266-wifi-hack-mqtt-tasmota/
https://github.com/tasmota/install/blob/main/firmware/unofficial/tasmota-allsensors.bin
https://jupyter.org/try
https://stackoverflow.com/questions/50982686/what-is-the-difference-between-jupyter-notebook-and-jupyterlab#52392304
https://stackoverflow.com/questions/4098131/how-to-update-a-plot-in-matplotlib
https://jupyter-notebook.readthedocs.io/en/stable/security.html
https://docs.anaconda.com/anaconda/user-guide/tasks/remote-jupyter-notebook/
https://pypi.org/project/paho-mqtt
https://www.tutorialspoint.com/jupyter/jupyter_notebook_plotting.htm


