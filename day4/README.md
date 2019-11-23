# KI mit Google Colab

KI lernen, ganz einfach und umsonst mit Google's TPU
Hardware für Jedermann. Dies wird als "Google Colab" in:
- https://colab.research.google.com/notebooks/welcome.ipynb

zur Verfügung gestellt. (Dazu braucht man einen Gmail Account. Reicht
auch temporär.) Dort geht es weiter mit Python und dem Keras Framework
was wiederum eine Abstraktionsebene für Tensorflow ist.

# In c't 21 war KI  Thema
In der c't 21 war KI mit Python und dem Keras Framework das Thema,
inklusive hands on. Ich habe den c't Artikel ""Hallo Welt" der KI" hier.

# Agenda

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
trainieren lassen. "MNIST" handwritten digit recognition model:
- https://github.com/tensorflow/tpu/blob/r1.13/tools/colab/keras_mnist_tpu.ipynb

b) Wer will kann das NN auch alternativ/zusätzlich entlang des c't 21 KI
Artikels (wer den hat, bitte mit bringen) auf dem eigenen Laptop
trainieren lassen. (Ob ein Raspberry das schafft?) Das Beispiel zur
Ziffernerkennung findet sich hier:<br>
- http://ct.de/ycnd

```bash
sudo apt-get update
pip install keras
#Problem after 30mins:
# ('Loading library to get version:', 'libhdf5.so')
#  error: libhdf5.so: cannot open shared object file: No such file or directory
#  
#  ----------------------------------------
#  Failed building wheel for h5py



###############
# Voraussetzungen
###############

# https://linoxide.com/linux-how-to/install-mongodb-ubuntu/
# Step 1) Installing MongoDB on Ubuntu 18.04
#Ubuntu's official package repositories comes with the latest version of MongoDB, which means we can install the necessary packages using apt-get.
#we will install MongoDB package that includes several other packages such as mongo-tools, mongodb-clients, mongodb-server and mongodb-server-core.
# does not work on raspian OS because it needs 64bit environment.
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

#######################
# jetzt kann's los gehen
#######################
git clone https://github.com/pinae/Sacred-MNIST/
cd Sacred-MNIST/

#We strongly recommend to use a virtualenv:
python3 -m venv env
source env/bin/activate

#Install the requirements:
pip install wheel
pip install -r requirements.txt

#Install TensorFlow in the CPU-Version:
# does not work on Raspian hardware. ERROR: No matching distribution found for tensorflow 
pip install tensorflow
#or GPU-Version:
#pip install tensorflow-gpu

#Training
#To train the network simply run:
python train_convnet.py

############################
# step by step
# Voraussetzungen
############################
pip install IPython
pip install -r visualisation_requirements.txt
pip install imageio


pip install imageio
python my_tf.py
sudo apt install python-pydot python-pydot-ng graphviz # python-pydot-ng isn't in the 14.04 repos
#sudo apt install graphviz # python-pydot-ng isn't in the 14.04 repos
python my_tf.py
echo "digraph G {Hello->World}" | dot -Tpng >hello.png 

py -m notebook
mv MNIST\ für\ Einsteiger.ipynb MNIST\ fur\ Einsteiger.ipynb 
python -m notebook


dir=/tmp
src=foto5.png
dst=dig5.png
convert -threshold 40% -negate -extract '500x500+1400+1000' -resize 28x28 $dir/$src $dir/$dst
#or
#convert -threshold 40% -negate -extract '500x500+1450+1000' -resize 28x28 $dir/$src $dir/$dst

```

### Das trainierte NN auf dem Raspberry anwenden
Das trainierte NN wird auf meinen bzw. den mitgebrachten Raspberrys
runter geladen. Jeder schreibt in seiner Handschrift einige Ziffern auf.
Diese werden fotografiert und normiert. Mit denen gefüttert, sollte der
Raspberry die Ziffern (hoffentlich) richtig erkennen.

Dazu sollte jeder einen Laptop mit bringen (ein Raspberry sollte auch
gehen  Wer vor 09:00 Uhr da ist kann gerne mit Frühstücken wenn er
Brötchen mit bringt  Ich biete ein WLAN Gastnetz, zum Mittag
Gulaschsuppe mit Kidneybohnen, Nervenfutter und Getränke. Wer möchte
kann hier gerne übernachten.

Wo nötig wird es wieder Codebeispiele geben unter:<br>
- https://github.com/autostock/RaspiDay/tree/master/day4
