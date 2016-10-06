/* arduino midi controler */
/* http://www.devsector.ch/cavimaster/2013/12/4-knobs-controleur-midi-arduino/ */

#define NOTE_ON 0x90
#define NOTE_OFF 0x80
#define CHANNEL 1
#define VELOCITY 0x7f
#define SONG_SIZE 6
#define BLANCHE 1000
#define NOIRE 500
#define CROCHE 250
#define LED_PIN 13

const char NOTES[SONG_SIZE] = {59, 45, 64, 61, 71, 68};
const int DURATIONS[SONG_SIZE] = {NOIRE, NOIRE, NOIRE, CROCHE, CROCHE, BLANCHE};
//const int DURATIONS[SONG_SIZE] = {20,20,20,20,20,20};

void noteOn(char channel, char note, char velocity)
{
    Serial.write(NOTE_ON + channel - 1);
    Serial.write(note);
    Serial.write(velocity);
}
void noteOff(char channel, char note)
{
    Serial.write(NOTE_OFF + channel - 1);
    Serial.write(note);
    Serial.write(0);
}
 
void setup()
{
    Serial.begin(31250);  
    pinMode(LED_PIN, OUTPUT);
}
 
void loop()
{
    char x = 0;
    for(x = 0; x < 200; x++)
    {
        noteOn(CHANNEL, x, VELOCITY);
        if(x & 1 == 1)
        {
            digitalWrite(LED_PIN, HIGH);
        }
        else
        {
            digitalWrite(LED_PIN, LOW);
        }
        delay(20);//DURATIONS[x]);
        noteOff(CHANNEL, x);//NOTES[x]);
    }
        for(x = 150; x > 0; x--)
    {
        noteOn(CHANNEL, x, VELOCITY);
        if(x & 1 == 1)
        {
            digitalWrite(LED_PIN, HIGH);
        }
        else
        {
            digitalWrite(LED_PIN, LOW);
        }
        delay(20);//DURATIONS[x]);
        noteOff(CHANNEL, x);//NOTES[x]);
    }
}

