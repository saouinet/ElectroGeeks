# ElectroGeeks
Burkert afterwork geeks
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
