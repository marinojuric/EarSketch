#		python code
#		script_name: The Weeknd - Blinding Lights
#
#		author: Marino
#		description: modern music
#

from earsketch import *

init()
setTempo(171)

#functions:

def melody1(n):
    for i in range (n, n+4, 2): 
        fitMedia(MARINO_F4, 26, i, i + 0.5)
        fitMedia(MARINO_F4, 26, i + 0.5, i + 0.875)
        fitMedia(MARINO_D_4, 27, i + 0.875, i + 1)
    
    for i in range (n+1, n+4, 2):
        fitMedia(MARINO_F4, 26, i, i + 0.175)
        fitMedia(MARINO_D_4, 27, i + 0.625, i + 1)
        fitMedia(MARINO_G4, 28, i + 0.125, i + 0.4)
        fitMedia(MARINO_C4, 29, i + 0.375, i + 0.625)
        
def melody2(n):
    for i in range (n, n+2): 
        fitMedia(MARINO_F4, 30, i + 0.375, i + 0.625)
        fitMedia(MARINO_D_4, 31, i + 0.625, i + 1)
        fitMedia(MARINO_G4, 32, i + 0.125, i + 0.375)
        fitMedia(MARINO_A_4, 33, i , i + 0.125)
    
    for i in range (n+1, n+2, 2):
        fitMedia(MARINO_F4, 34, i + 0.875, i + 2)

for i in range(26, 35):
    setEffect(i, VOLUME, GAIN, 10)
    setEffect(i, PITCHSHIFT, PITCHSHIFT_SHIFT, 0.01)
        
def chords1(n):
    for i in range (n, n+15, 8):
        fitMedia(MARINO_F3, 5, i, i + 1.625)
        fitMedia(MARINO_D_4, 6, i + 1.625, i + 1.75)
        fitMedia(MARINO_F4, 7, i + 1.75, i + 1.875)
        fitMedia(MARINO_C3, 8, i + 1.875, i + 4)
        fitMedia(MARINO_D_3, 9, i + 4, i + 5.75)
        fitMedia(MARINO_A_2, 10, i + 5.8, i + 7)
        fitMedia(MARINO_A_3, 11, i + 7, i + 7.375)
        fitMedia(MARINO_G_3, 12, i + 7.35, i + 7.75)
        fitMedia(MARINO_G3, 13, i + 7.75, i + 8)

for i in range(5,14):
    setEffect(i, FILTER, FILTER_FREQ, 1000.0)
    
def chords2(n):
    for i in range(n, n+17, 8):
        fitMedia(MARINO_F4, 14, i, i+2)
        fitMedia(MARINO_C4, 15, i, i+2)
        fitMedia(MARINO_G_4, 16, i, i+2)
        fitMedia(MARINO_C4, 17, i+2, i+4)
        fitMedia(MARINO_G4, 18, i+2, i+4)
        fitMedia(MARINO_D_3, 19, i+2, i+4)
        fitMedia(MARINO_G3, 20, i+4, i+6)
        fitMedia(MARINO_A_3, 21, i+4, i+6)
        fitMedia(MARINO_D_4, 22, i+4, i+6)
        fitMedia(MARINO_D4, 23, i+6, i+8)
        fitMedia(MARINO_F3, 24, i+6, i+8)
        fitMedia(MARINO_A_3, 25, i+6, i+8)

for i in range(14,26):
   if(i % 2 == 1):
        setEffect(i, PAN, LEFT_RIGHT, 100)
   else:
      setEffect(i, PAN, LEFT_RIGHT, -100)

for i in range(14,26):
   	setEffect(i, TREMOLO, MIX, 0.2)

def arpeggio(n, m):
    while n < m:
        i = n;
        fitMedia(MARINO_C4, 35, i, i + 0.125)
        fitMedia(MARINO_D_4, 36, i + 0.125, i + 0.25)
        fitMedia(MARINO_C4, 35, i + 0.25, i + 0.375)
        fitMedia(MARINO_D_4, 36, i + 0.375, i + 0.5)
        fitMedia(MARINO_F4, 37, i + 0.5, i + 0.625)
        fitMedia(MARINO_G4, 38, i + 0.625, i + 0.75)
        fitMedia(MARINO_C4, 35, i + 0.75, i + 0.875)
        fitMedia(MARINO_D_4, 36, i + 0.875, i + 1)
        n = n + 1
    
#beat:

kick = MARINO_VEH1_HARD_KICK_037_WAV
snare = MARINO_VEH1_SNARES_CLAPS_020_WAV
hihat = MARINO_VEH1_CLOSED_HIHAT_67_WAV
clap = MARINO_CLAP_REVERB

kickBeat = "0++++---0++++---0++++---0+0++---"
snareBeat = "++++0+++++++0+++"
hihatBeat = "0-0-0-0-0-0-0-0-"
clapBeat = "--------------------------0+++0+++"

for i in range (1, 54, 2):
    makeBeat(kick, 1, i, kickBeat)
    makeBeat(clap, 4, i, clapBeat)
    
for i in range (1, 54):
    makeBeat(snare, 2, i, snareBeat)
    makeBeat(hihat, 3, i, hihatBeat)
    setEffect(3, VOLUME,GAIN, -20)
    
melody1(1)
melody2(5)
chords1(8)
arpeggio(8,24)
chords2(24)
chords1(32)
arpeggio(32,40)
melody1(48)
melody2(52)

fitMedia(MARINO_A_3, 11, 55, 55.375)
fitMedia(MARINO_G_3, 12, 55.35, 55.75)
fitMedia(MARINO_G3, 13, 55.75, 56)
finish()
