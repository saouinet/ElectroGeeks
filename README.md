# ElectroGeeks
Burkert afterwork geeks
- session du 2016 10 05:
 - il est midi à 17H30 ...
  - PFe a apporté du matériel midi, un clavier, un ampli ... et toute son experience.
   - pour les nostalgiques : http://pfeuh.free.fr/shared/odmc/mp3/pot_pourri_videogames.mp3
  - montage d'une arduino UNO jouant une étrange music.
   - merci à PFe
   - Source : http://www.devsector.ch/cavimaster/2013/12/4-knobs-controleur-midi-arduino/
- session du 2016 09 21:
 - Discussions à propos de l'usure de la FLASH des Raspberry pi.
  - différences entre RAM/FLASH entre Disques dur et SSD (Solid State Drive)
  - un petit tour avec google et les réponses se clarifies mais il faut lire plusieurs articles ;)
 - Choix de projets possibles:
  - Notamment un miroir connecté : http://mirrormirror.tech/t/members-gallery/185 
  
- session du 2016 09 14:
 - mise en marche d'un ESP2688 (module wifi)
 - après cablage de l'alimentation (3.3V)  et des communications sur un cable (RS232) FTDI
 - le terminal communique à 9600 baud !!!
 - il est possible de "flasher" des programmes 
 - à voir : https://espressif.com/en/products/hardware/esp8266ex/overview
 - ce module est utilisé sur une prise connectée : https://www.itead.cc/smart-home/smart-socket-eu.html
 - et pour les modifier ... http://captain-slow.dk/2016/07/08/itead-smart-socket-wifi-smart-socket-eu-plug-first-impressions/
 
- session du 2016 08 31:
 - opértion sur site:
 Chez JM. mise en route de la récupération des données du compteur électrique.
 Avec une connection direct de l'UART à la RBpi3.
 - l'adresse ip est forcée dans /etc/network/interfaces pour eth0.
 - attention à l'alimentation en 3v3.
 - désactiver le terminal ttyAMA0 avec les options avancées du port Serie.
 - utilisation de mosquitto et node-red 
- session du 2016 06 22:
 - utiliser la raspberry py comme diaporama et videoplayer
  - installer fbi:
sudo apt update
sudo apt install fbi
  - se placer dans le dossier des photos
cd dossier_photos_jpg/
  - lancer le player 
fbi -a --noverbose -t 2 *.jpg
 - pour les videos:
 
- session du 2016 05 25 :
 - Install party Ubuntu 16.04
   - machine HP Pavilion
   - le démarrage à partir de la clé USB ne marche pas.
   - Modifier le BIOS pour démarrer en priorité sur les clés USB
   - Le test d'Ubuntu fonctionne.
   - sur HP, les quatres partition primaires sont utilisées...
    - Sauvegarde des données du disque HP-TOOLS, 
    - Avec gparted supression de la partition HP-TOOLS et redimentionnement de la partition principale
    - Libérer de l'espace pour créer une partition logique
    - créer une partition linux "/" ext4, une partition linux-swap, et 100Mo en FAT32 pour restaurer HP-TOOLS
   - Installation de Ubuntu 
   - Mise à jours

- session du 2016 05 12 :
 - 
- session du 2016 04 27 :

 Utiliser une Raspberry py pour lire une sonde Dallas
 - Configuration :
   - Dans /etc/modules ajouter w1-therm et w1-gpio
   - Dans /boot/config.txt ajouter dtoverlay=w1-gpio,gpiopin=3
   - Eteindre et cabler 3v3 pin 1, data pin 3, GND pin 5
   - Démarrer
 - utilisation:
   - Dans le dossier /sys/devices/w1_bus_master1/10-0008024b67ca se trouvent les données lues
   - Lancement de node-red
   - lecture des données de température avec une conversion du text en nombre
   - repetition toutes les 2 sec 
   - essai d'écriture dans un fichier 
