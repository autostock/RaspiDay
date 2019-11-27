# Thema KI

## Beschreibung einiger Dateien

- nn.ods: Spreadsheet zum hands-on design einfacher NNs (perceptron für AND, NAND, OR und 3 layer NN für XOR).
-- Visualisierung von signum, sigmoid, Gauss (als Ableitung der sigmoid) und simplified-sigmoid
-- Visiualisierung des gradient descent bei der automatischen Findung von NN Gewichten.
- activate.bas: Im obigen Spreadsheet wird eine selbst definierte Funktion genutzt. Dies ist der Quellcode dazu.
- fünf.png: Orginalfoto der 5 vor der Bearbeitung nach dig5.png
- dig5.png: 28x28 große weiss auf schwarz handgeschrieben 5
- xor.c: Ist ein C++ Programm mit fertig trainierten NN für XOR. [Try it online](https://tio.run/##ZVLBcpswED2jr9hJphkDMkjYbtJi0nMu7rEHlwMGxVYGCwaEk4yHb3dXwjhOOmMj7e7bt7tPm9f1dJvnp9OtVHnZFQKWrS5kFeweySdXKTeffftM74yH6PdaFOIZWt10uYajVBoKUetdDOZaZu@iWXOWxlBU3aYU8CrkdqfXM3T1sFrFJK9Uq8eoSKLgnj9ED@Y/X/xg8wUFLfa1aDLdNSJhAXuIyS2WlEo4rdzuK1lM3lyY8ICF5uPX1etEUJi@hVeJrusSMhTxQByyssu0mKxWcKeEpmP5XJTlOnXhSBzT/R/ba8Io/O7wiAlxnqsGJnYycRAlJMDj83UJyBScZ7cu37dMlupJIRZZYrTxAD@x8EEfi57yNHYcDF9KvGAKi/FYfsWinC8ju3PuvYWB8izw0LvvIzQMYSOz1mAv3HLglv9zmz5AGvZ27PIrJXiDUk/Kl6mZyLEmzuW/pEg8PkvrmmBPzK8R@AwK7kZkCjHpUdEDAuGtalYr21dG7d5s7GytzrTMcUtMF8lxRiH0bKdeCMeIRpT3FAscQ08qJRoOqipEZIdNvHDKApvxytDwWXBvDT5E7k0ifEqcXSXOL4lofL8kIsvinFh1WjSRTZxfJS4sNjJYHnBrzAZjQXuc17netMiPfJ4mx4xuTKhucPTnyc03KwjgMX3E7191Q40uG/qxuHZpDYe7ZukSy/5iPzmg3D0hRr99JtWgZ7PNEbnLGs/cD@ftHgRnlJkXGg3@YfDrCLeR/nT6Bw)
- MNIST fur Einsteiger.ipynb: Notebook für Keras zum trainieren eines NN auf MNIST Basis
- MNIST fur Einsteiger.py: Wie oben nur als direktes python Programm.
- use1.py: Minimalprogramm um das durch tensorflow berechnete NN zum Erkennen (siehe oben) zu nutzen. (Hier soll unsere Zahl 5 erkannt werden.)

## KI Google Colab

KI lernen, ganz einfach und umsonst mit Google's TPU
Hardware für Jedermann. Dies wird als "Google Colab" in:<br>
- https://colab.research.google.com/notebooks/welcome.ipynb

zur Verfügung gestellt. (Dazu braucht man einen Gmail Account. Reicht
auch temporär.) Dort geht es weiter mit Python und dem Keras Framework
was wiederum eine Abstraktionsebene für Tensorflow ist.

## In c't 21 war KI  Thema
In der c't 21 war KI mit Python und dem Keras Framework das Thema,
inklusive hands on im c't Artikel ""Hallo Welt" der KI".

## Agenda
### Aufwärmen
Wir programmieren ein einfaches neuronales Netz (NN) welches die
boolsche XOR Funktion nach bildet. Zwei Eingangsneurone, ein
Zwischenlayer und ein Ausgangsneuron. (Hier ist verwendete
Programmiersprache für jeden frei wählbar.) Hierbei führe ich durch
verschiedene Varianten zur Umsetzung:

a) Was ist ein NN. Wie repräsentiere ich das/ein NN im Code.<br>
b) Die Gewichte des XOR NN werden "händig" erraten (educated guess).<br>
c) Die Gewichte des XOR NN werden irgendwie algorithmisch entwickelt.<br>
d) Die Gewichte des XOR NN werden mittels (error) back propagation ermittelt.<br>
e) Sonstiges/Fragen.<br>

### Googles Tensorflow (hier zur Ziffernerkennung)
a) Im Google Lab werden wir mittels Python->Keras->Tensorflow anhand
vorgegebener MNIST Daten die handgeschriebene Ziffernerkennung
trainieren lassen. "MNIST" handwritten digit recognition model:<br>
- https://github.com/tensorflow/tpu/blob/r1.13/tools/colab/keras_mnist_tpu.ipynb

b) Wer will kann das NN auch alternativ/zusätzlich entlang des c't 21 KI
Artikels (wer den hat, bitte mit bringen) auf dem eigenen Laptop
trainieren lassen. (Ob ein Raspberry das schafft?) Das Beispiel zur
Ziffernerkennung findet sich hier:<br>
- http://ct.de/ycnd

#### Voraussetzungen

```bash
sudo apt-get update

# https://linoxide.com/linux-how-to/install-mongodb-ubuntu/
# Step 1) Installing MongoDB on Ubuntu 18.04
#Ubuntu's official package repositories comes with the latest version of MongoDB, which means we can install the necessary packages using apt-get.
#we will install MongoDB package that includes several other packages such as mongo-tools, mongodb-clients, mongodb-server and mongodb-server-core.
########
# does not work on raspian OS because it needs 64bit environment.
# So proceeded to Ubuntu Mate on raspberrypi. But see below when installing tensorflow :-(
########
sudo apt-get install -y mongodb

# Step 2) Checking the Service and Database of MongoDB
#The MongoDB service will start automatically via systemd and the process listens on port 27017. You can verify its status using the systemctl command as shown below.
sudo systemctl status mongodb

#Also we can verify this Installing by connecting to the database server and executing a diagnostic command.
mongo --eval 'db.runCommand({ connectionStatus: 1 })'
#WICHTIG: muss wg. PyMongo mindestens 2.6 sein

# the virtual environment enabler
sudo apt-get install python3-venv

# install GIT
sudo apt install git
```

#### jetzt kann's los gehen auf der Commandline

```bash
git clone https://github.com/pinae/Sacred-MNIST/
cd Sacred-MNIST/

#We strongly recommend to use a virtualenv:
python3 -m venv env
source env/bin/activate

#Install the requirements:
pip install wheel ## Nötig? Denn enthalten in requirements.txt .
pip install -r requirements.txt

#Install TensorFlow in the CPU-Version:
########
# does not work on Raspian hardware. ERROR: No matching distribution found for tensorflow :-(
########
pip install tensorflow
#or GPU-Version:
#pip install tensorflow-gpu

#Training
#To train the network simply run:
python train_convnet.py

```

#### Voraussetzungen für das Arbeiten mit dem jupyter notebook

```bash
pip install IPython ## Nötig?
pip install -r visualisation_requirements.txt

# Bei mir hat der Umlaut gestört (Bei Andern nicht!)
mv MNIST\ für\ Einsteiger.ipynb MNIST\ fur\ Einsteiger.ipynb 
python -m notebook

```


#### Bildverarbeitung

```bash
sudo apt-get install imagemagick

dir=/tmp
src=foto5.png
dst=dig5.png
convert -threshold 40% -negate -extract '500x500+1400+1000' -resize 28x28 $dir/$src $dir/$dst
#or
#convert -threshold 40% -negate -extract '500x500+1450+1000' -resize 28x28 $dir/$src $dir/$dst

```

### Das trainierte NN auf dem Raspberry anwenden
VORAB:
Es stellt sich heraus, dass der Raspberry (noch) nicht dazu in der Lage ist. Denn (siehe auch oben):
- mongoDB wird nicht mehr für 32 Bit (Raspian OS) gepflegt.
- Im 64 Bit OS (hier Ubuntu Mate) scheitert die Installation von tensorflow

So war der Plan:
Das trainierte NN wird auf meinen bzw. den mitgebrachten Raspberrys
runter geladen. Jeder schreibt in seiner Handschrift einige Ziffern auf.
Diese werden fotografiert und normiert. Mit denen gefüttert, sollte der
Raspberry die Ziffern (hoffentlich) richtig erkennen.

Letztendlich haben wir es auf einem Ubuntu Laptop hin bekommen. Die Ziffer 5 wurde Hand geschrieben und davon ein Foto (foto5.png) gemacht. Dann ein wenig Bildverarbeitung (siehe oben) um es an das von MNIST geforderte Format an zu passen.
Das Resultat wurde in dig5.png abgespeichert, dem von uns trainierten Netz zum Analysieren angeboten und - siehe da - es hat die 5 erkannt! :-)


## Literatur

- Codebeispiele stehen unter: https://github.com/autostock/RaspiDay/tree/master/day4
- http://neuralnetworksanddeeplearning.com/index.html
- https://codelabs.developers.google.com/codelabs/cloud-tensorflow-mnist/
- https://keras.io/
- Schöne 3D-Visualisierung eines Convolutional Networks für MNIST: http://scs.ryerson.ca/~aharley/vis/conv/



