# ElectroGeeks
Burkert afterwork geeks
- session du 2016 04 27 :

 Utiliser une Raspberry py pour lire une sonde Dallas
 - Configuration :
   - Dans /etc/modules ajouter w1-therm et w1-gpio
   - Dans /boot/config.txt ajouter dtoverlay=w1-gpio,gpiopin=3
   - Eteindre et cabler 3v3 pin 1, data pin 3, GND pin 5
   - Démarrer
- utilisation:
   - Dans le dossier /sys/devices/w1_bus_master1/10-0008024b67ca se trouvent les donnes lues
