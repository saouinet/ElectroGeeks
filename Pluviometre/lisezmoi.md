
# Principes:
Mesurer la pluviométrie avec un système à bascule.
Une carte ESP8266 transmet un message MQTT à un broker mosquitto sur une Raspberry pi chaque basculement (0.73l l/m^2).

## Mecanique:
 - Modèle impression 3D bascule
 - Ampoule reed + Aimant

## Electronique:
- Materiel:
 - Raspberry pi zero W
  - Alimentation 5V 2A
 - Esp8266
  - Alimentation 3v3
 - panneaux solaires sunna+batteries 1.2v 
 - Questions:
Combien consomme la carte 8266 ?
Comment réduire la consommation ?
A quelle fréquence, les pluses sont-ils générés

## Logiciel:
 - Outils:
  - Raspberry pi:
   - mosquitto: broker MQTT
   - node-red: pour faciliter l'usage
   
  - ESP8266:
   - Atom/PlateformIO:
  Editeur de texte et environement de developpement
   - PubSubClient:
  Bibliothèque MQTT pour ESP8266
 - Quesstions:
  - Comment gerer le temps?
  - Y a-t-il des rebonds
