# Metronóm / Metronome

![Preview](preview.png)

## Jednoduchy Metronom

Win:   
Nakopiruj VSETKy tri subory (exe, wav, ttf) niekam do pocitaca (do toho isteho priecinka).   
Spusti metron.exe   
Linux:   
Je potrebne mat nainstalovany Python3 a moduly pygame a numpy.   
Spusti python3 metron.pyw


Ovladanie:
 - Klavesnica
   - plus, minus              : hlasitost
   - sipka vpravo, sipka vlavo : zvysenie/znizenie BPM o 10
   - sipka hore, sipka dole    : zvysenie/znizenie BPM o 1
   - q                         : koniec programu
  - Mys
    - kliknutim na BPM zvysujete/znuzijete BPM o 10 (lave alebo prave tlacidlo)
    - kliknutim na + a - upravujete hlasitost

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
    - click on BPM to increase/decrease BPM by 10 (left or right button)
    - click on + or - to increase/decrease volume

Poznamky/Notes:   
ttf downloaded from http://www.freefontsdownload.net   
exe created by: pyinstaller --onefile metron.pyw (on W10)

Credits to: vladonix@gmail.com  :)
