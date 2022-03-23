# Metronóm / Metronome

![Preview](preview.png)

## Jednoduchy Metronom

Win:   
Nakopírujte VŠETKY tri súbory (exe, wav, ttf) niekam do počítača (do toho istého priečinka).   
Spustite metron.exe   
Linux:   
Je potrebné mať nainštalovaný Python3 a moduly pygame a numpy.   
Spustite python3 metron.pyw


Ovládanie:
 - Klávesnica
   - plus, mínus               : hlasitosť
   - šípka vpravo, šípka vľavo : zvýšenie/zníženie BPM o 10
   - šípka hore, šípka dole    : zvýšenie/zníženie BPM o 1
   - q                         : koniec programu
  - Myš
    - kliknutím na BPM zvyšujete/znžujete BPM o 10 (ľavé alebo pravé tlačidlo myšky)
    - kliknutím na + a - upravujete hlasitosť

Rytmus:   
Program môže zobrazovať rytmus a zmeniť zvuk pri dobe/takte v rytme, na ktorej je dôraz. Spustite metronóm s parametrom nazavoSuboruSRytmom, alebo potiahnite súbor s rytmom cez exe súbor (pre  Win).

Súbor s rytmom:   
Súbor môže mať jeden alebo dva riadky. Na prvom riadku musí byť rytmus, na drohom môže byť číslo s požadovaným BPM pre uvedený rytmus. V prvom riadku je akceptovaných prvých 32 znakov.   
Všetky znaky x v prvom riadku sú považované za takt s dôrazom. Ostatné znaky môžu byť ľubovoľné (pre takty bez dôrazu).   
Príklad súboru pre Soleá (s prízvkom na 3, 6, 8, 10 a 12 takte):      
nnxnnxnxnxnx   
115   

## Simple metronome

Win:   
Copy all three files (exe, wav, ttf) to your computer (to the same directory).   
Run metron.exe    

Linux:    
Required python3 and modules pygame and numpy.   
Run python3 metron.pyw

Controls:
 - Keyboard
   - plus, minus              : volume
   - arrow left, arrow right  : increase/decrease BPM by 10
   - arrow up, arrow down     : increase/decrease BPM by 1
   - q                        : quit 
  - Mouse
    - click on BPM to increase/decrease BPM by 10 (left or right mouse button)
    - click on + or - to increase/decrease volume

Rhythm:   
The program can display the rhythm and change the sound at the time/beat in the rhythm that is emphasized. Run the metronome with the parameter FilenWithRhythm, or drag the rhythm file via the exe file (for Win).

Rhythm file:   
The file can have one or two lines. The first line must contain a rhythm, the 2nd may contain a number with the required BPM for the specified rhythm. The first 32 characters are accepted in the first line.
All x characters in the first line are considered accented. Other characters can be arbitrary (for beats without emphasis).   
Example file for Soleá (accents at 3, 6, 8, 10 and 12 ):   
nnxnnxnxnxnx   
115    


Poznamky/Notes:   
ttf downloaded from http://www.freefontsdownload.net   
exe created by: pyinstaller --onefile metron.pyw (on W10)

Credits to: vladonix@gmail.com  :)
