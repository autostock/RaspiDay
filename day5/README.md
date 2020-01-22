# Thema KI auf dem Raspberry 3 und 4

## HelloWorld: Trainieren und anschließend Anwenden eines NN auf einem Raspi mit tensorflow.

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

#### jetzt kann's los gehen auf der Commandline

Trainieren benötigt ca. 3000 sek auf dem Raspberry 3 (und ca. 1400 sek auf dem Raspberry 4) bei nur 2 Epochen. Also ca. 1500 sek pro Epoche. Zwei Epochen reichen aber für die Güte des NN erst Mal aus.

``` bash
python lauf2.py 
#Using TensorFlow backend.
#2019-12-14 19:53:34.283380: E tensorflow/core/platform/hadoop/hadoop_file_system.cc:132] HadoopFileSystem load error: libhdfs.so: cannot open shared object file: No such file or directory
#Downloading data from https://s3.amazonaws.com/img-datasets/mnist.npz
#11493376/11490434 [==============================] - 5s 0us/step
#WARNING:tensorflow:From /home/pi/KI/env/lib/python3.7/site-packages/tensorflow_core/python/ops/resource_variable_ops.py:1630: calling BaseResourceVariable.__init__ (from tensorflow.python.ops.resource_variable_ops) with constraint is deprecated and will be removed in a future version.
#Instructions for updating:
#If using Keras pass *_constraint arguments to layers.
#WARNING:tensorflow:From /home/pi/KI/env/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4070: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.
#
#WARNING:tensorflow:From /home/pi/KI/env/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.
#
#Train on 60000 samples, validate on 10000 samples
#Epoch 1/2
#2019-12-14 19:54:32.464040: W tensorflow/core/framework/cpu_allocator_impl.cc:81] Allocation of 11075584 exceeds 10% of system memory.
#2019-12-14 19:54:36.963308: W tensorflow/core/framework/cpu_allocator_impl.cc:81] Allocation of 18874368 exceeds 10% of system memory.
#2019-12-14 19:54:43.404929: W tensorflow/core/framework/cpu_allocator_impl.cc:81] Allocation of 9437184 exceeds 10% of system memory.
#2019-12-14 19:54:43.408007: W tensorflow/core/framework/cpu_allocator_impl.cc:81] Allocation of 18874368 exceeds 10% of system memory.
#2019-12-14 19:54:44.196058: W tensorflow/core/framework/cpu_allocator_impl.cc:81] Allocation of 11075584 exceeds 10% of system memory.
#60000/60000 [==============================] - 1473s 25ms/step - loss: 0.2082 - accuracy: 0.9359 - val_loss: 0.0479 - val_accuracy: 0.9840
#Epoch 2/2
#60000/60000 [==============================] - 1611s 27ms/step - loss: 0.0717 - accuracy: 0.9782 - val_loss: 0.0395 - val_accuracy: 0.9860
```

Anwenden

``` bash
python use1.py 
#Using TensorFlow backend.
#2019-12-14 20:47:16.444781: E tensorflow/core/platform/hadoop/hadoop_file_system.cc:132] HadoopFileSystem load error: libhdfs.so: cannot open shared object file: No such file or directory
#WARNING:tensorflow:From /home/pi/KI/env/lib/python3.7/site-packages/tensorflow_core/python/ops/resource_variable_ops.py:1630: calling BaseResourceVariable.__init__ (from tensorflow.python.ops.resource_variable_ops) with constraint is deprecated and will be removed in a future version.
#Instructions for updating:
#If using Keras pass *_constraint arguments to layers.
#WARNING:tensorflow:From /home/pi/KI/env/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4070: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.
#
#WARNING:tensorflow:From /home/pi/KI/env/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.
#
#[4]
#[[2.6218304e-06 2.5204520e-06 9.7428328e-06 1.5765105e-05 9.9699748e-01
#  1.2196848e-03 1.4060701e-03 1.8572458e-04 5.3766740e-05 1.0665286e-04]]
```


## Wetter: pm-Prognose mit NN 
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

## Tensorflow: Mal selbst die Tensorflow Library compilieren.

Problem: TensorFlow aus den Ubuntu-binaries läßt sich auf Notebook mit Core2Duo-Prozessor nicht betreiben, da AVX(?)-Maschinencode nicht ausgeführt werden kann.


#### Kompilierung aus Quellen nach tensorflow.org mit bazel-1.1.0

Ist mehrfach nach mehreren Stunden abgebrochen. Zu wenig Ressourcen? (4GB RAM, 15GB SSD frei) Ungenügender Prozessor? (Core2Duo 64bit)


#### Aktueller Prozessor: Auf VPS mit 1GB RAM, 1core, 8GB HDD

Schnell abgebrochen, wohl Speichermangel.


#### Mehr Ressourcen: Kompilieren auf t3a.2xlarge-EC2-Instanz (unlimited, 8cores, 32GB RAM) bei AWS.amazon.com:

1. Umgebung nach tensorflow.org, ohne virtual environment
2. target-Option für bazel: --cops=-march=core2

-> FAILED: Build did NOT complete successfully, evtl. Python2/3 Inkompatibilität?

bazel --host_force_python=PY3 build --copt=-march=core2 //tensorflow/tools/pip_package:build_pip_package &

-> Fatal error: can't close bazel-out/host/bin/external/llvm/_objs/selection_dag/DAGCombiner.pic.o: No space left on device

-> Platte (8GB) voll!


#### c5d4xl-Instanz, 320GB Platte 32GB RAM

``` bash
sudo apt update
sudo apt upgrade 
sudo apt install build-essential
sudo apt install python3-dev python3-pip
pip install -U --user pip six numpy wheel setuptools mock 'future>=0.17.1'
pip install -U --user keras_applications --no-deps
pip install -U --user keras_preprocessing --no-deps
pip install -U --user keras_applications --no-deps
sudo apt install curl
curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -
echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
sudo apt update && sudo apt install bazel-1.1.0
git clone https://github.com/tensorflow/tensorflow.git
cd tensorflow
sudo ln /usr/bin/bazel-1.1.0 /usr/bin/bazel
./configure 
bazel build --copt=-march=core2 //tensorflow/tools/pip_package:build_pip_package &
```

-> kompiliert

-> auf PC nicht installierbar, PyCObject-Problem: Probleme zwischen Python 2 und 3 ?!

Anstatt dem auf den Grund zu gehen, aus dem Gelernten noch ein Mal auf PC versuchen:


#### PC (4GB RAM, 15GB SSD frei, Core2Duo 64bit) mit 5GB Auslagerungsdatei kompiliert es in 16h.

-> Erfolg.

-> Training lauf2.py dauert ca. 25 Minuten je Epoche. Z.Vgl. Raspi3 - 25min, Raspi4 - 3min.



