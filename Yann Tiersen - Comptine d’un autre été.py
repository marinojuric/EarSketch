#		python code
#		script_name: Yann Tiersen - Comptine d'un autre été
#
#		author: Marino
#		description: classical music
#

from earsketch import *

init()
setTempo(170)

#left hand:
#functions:

def uno(n):
    for i in range (n, n+1):
        fitMedia(MARINO_E3, 1, i, i + 0.25)
        fitMedia(MARINO_B3, 2, i + 0.25, i + 0.5)
        fitMedia(MARINO_G3, 3, i + 0.5, i + 1)
        
def due(n):
    for i in range (n+2, n+3):
        fitMedia(MARINO_D3, 4, i, i + 0.25)
        fitMedia(MARINO_B3, 2, i + 0.25, i + 0.5)
        fitMedia(MARINO_G3, 3, i + 0.5, i + 1)
        
def tre(n):
    for i in range (n+4, n+5):
        fitMedia(MARINO_D3, 4, i, i + 0.25)
        fitMedia(MARINO_B3, 2, i + 0.25, i + 0.5)
        fitMedia(MARINO_F_3, 6, i + 0.5, i + 1)
        
def quattro(n):
    for i in range (n+6, n+7):
        fitMedia(MARINO_D3, 4, i, i + 0.25)
        fitMedia(MARINO_A3, 5, i + 0.25, i + 0.5)
        fitMedia(MARINO_F_3, 6, i + 0.5, i + 1)
        
def lungoUno(n):
    for i in range(n, n+1):
        fitMedia(MARINO_E3, 1, i, i + 1)
        fitMedia(MARINO_B3, 2, i, i + 1) 

def lungoDue(n):
    for i in range(n+2, n+3):
        fitMedia(MARINO_D3, 4, i, i + 1)
        fitMedia(MARINO_B3, 2, i, i + 1) 
        
def lungoTre(n):
    for i in range(n+4, n+5):
        fitMedia(MARINO_D3, 4, i, i + 1)
        fitMedia(MARINO_B3, 2, i, i + 1) 
        
def lungoQuattro(n):
    for i in range(n+6, n+7):
        fitMedia(MARINO_D3, 4, i, i + 1)
        fitMedia(MARINO_A3, 5, i, i + 1)
        
def parteA(n):
    uno(n)
    uno(n+1)
    due(n)
    due(n+1)
    tre(n)
    tre(n+1)
    quattro(n)
    quattro(n+1)

def parteB(n):
    lungoUno(n)
    uno(n+1)
    lungoDue(n)
    due(n+1)
    lungoTre(n)
    tre(n+1)
    lungoQuattro(n)
    quattro(n+1)

def parteC(n):
    fitMedia(MARINO_E3, 1, n, n + 2)
    fitMedia(MARINO_B3, 2, n, n + 2)
    fitMedia(MARINO_D3, 4, n + 2, n + 4)
    fitMedia(MARINO_B3, 2, n + 2, n + 4)
    fitMedia(MARINO_D3, 4, n + 4, n + 6)
    fitMedia(MARINO_B3, 2, n + 4, n + 6)
    fitMedia(MARINO_D3, 4, n + 6, n + 8)
    fitMedia(MARINO_A3, 5, n + 6, n + 8)
    
for m in range(1,7):
    setEffect(m, BANDPASS, BANDPASS_FREQ, 150)
for m in range(1,6):
    setEffect(m, VOLUME, GAIN, 5.0)

setEffect(6, VOLUME, GAIN, -5.0)

#songLeft:

parteA(1)
parteB(9)
parteB(17)
parteA(25)
parteA(33)
parteC(41)
parteC(49)
parteB(57)
parteA(65)
parteA(73)
parteC(81)
parteC(89)
fitMedia(MARINO_E3, 1, 97, 100)
fitMedia(MARINO_B3, 2, 97, 100)


#right hand:
#functions:

def first(n, a, b, c, d, nra, nrb, nrc, nrd):
    for i in range (n, n+1):
        fitMedia(a, nra, i + 0.25, i + 0.375)
        fitMedia(c, nrc, i + 0.375, i + 0.5)
        fitMedia(a, nra, i + 0.5, i + 0.75)
        fitMedia(b, nrb, i + 0.75, i + 0.875)
        fitMedia(d, nrd, i + 0.875, i + 1)
        fitMedia(b, nrb, i + 1, i + 2)

def secondA(n, a, b, c, nra, nrb, nrc):
    for i in range (n, n+1):
        fitMedia(a, nra, i , i + 0.75)
        fitMedia(b, nrb, i + 0.75, i + 2)
    for i in range (n+2, n+3):
        fitMedia(c, nra, i, i + 0.75)
        fitMedia(b, nrc, i + 0.75, i + 2)

def secondB(n, a, b, c, nra, nrb, nrc):
    for i in range (n, n+1):
        fitMedia(a, nra, i , i + 0.75)
        fitMedia(b, nrb, i + 0.75, i + 2)
    for i in range (n+2, n+3):
        fitMedia(a, nra, i, i + 0.75)
        fitMedia(c, nrc, i + 0.75, i + 2)

def secondC(n, a, b, c, d, nra, nrb, nrc, nrd):
    for i in range (n, n+1):
        fitMedia(a, nra, i , i + 0.75)
        fitMedia(b, nrb, i , i + 0.75)
        fitMedia(c, nrc, i + 0.75, i + 2)
    for i in range (n+2, n+3):
        fitMedia(a, nra, i , i + 0.75)
        fitMedia(b, nrb, i , i + 0.75)
        fitMedia(d, nrd, i + 0.75, i + 2)

def secondD(n, a, b, c, d, nra, nrb, nrc, nrd):
    for i in range (n, n+1):
        fitMedia(a, nra, i , i + 0.75)
        fitMedia(b, nrb, i , i + 0.75)
        fitMedia(c, nrc, i + 0.75, i + 2)
    for i in range (n+2, n+3):
        fitMedia(d, nrd, i , i + 0.75)
        fitMedia(b, nrb, i , i + 0.75)
        fitMedia(c, nrc, i + 0.75, i + 2)

def third(n, a, b, c, d, nra, nrb, nrc, nrd):
    for i in range (n, n+1):
        fitMedia(a, nra, i, i + 0.125)
        fitMedia(b, nrb, i + 0.125 , i + 0.25)
        fitMedia(c, nrc, i + 0.25, i + 0.375)
        fitMedia(a, nra, i + 0.375, i + 0.5)
        fitMedia(b, nrb, i + 0.5 , i + 0.625)
        fitMedia(c, nrc, i + 0.625, i + 0.75)
        fitMedia(a, nra, i + 0.75, i + 0.875)
        fitMedia(b, nrb, i + 0.875 , i + 1)
    for i in range (n+1, n+2):
        fitMedia(c, nrc, i , i + 0.5)
        fitMedia(a, nrb, i + 0.5, i + 0.75)
        fitMedia(d, nrd, i + 0.75, i + 1)

#songRight:

for i in range (1, 3):
    fitMedia(MARINO_E4, 7, i, i + 0.5)
    fitMedia(MARINO_E4, 7, i + 0.5, i + 1)
for i in range (3, 9):
    fitMedia(MARINO_D4, 8, i, i + 0.5)
    fitMedia(MARINO_D4, 8, i + 0.5, i + 1)    

first(9, MARINO_G4, MARINO_B4, MARINO_F_4, MARINO_C5, 9, 10, 11, 12)
first(11, MARINO_F_4, MARINO_G4, MARINO_G4, MARINO_A4, 11, 9, 9, 13)
first(13, MARINO_F_4, MARINO_B4, MARINO_E4, MARINO_C5, 11, 10, 7, 12)

for i in range (15, 16):
    fitMedia(MARINO_F_4, 11, i + 0.25, i + 0.375)
    fitMedia(MARINO_E4, 7, i + 0.375, i + 0.5)
    fitMedia(MARINO_F_4, 11, i + 0.5, i + 2)

first(17, MARINO_G4, MARINO_B4, MARINO_F_4, MARINO_C5, 9, 10, 11, 12)
first(19, MARINO_F_4, MARINO_G4, MARINO_G4, MARINO_A4, 11, 9, 9, 13)
first(21, MARINO_F_4, MARINO_B4, MARINO_E4, MARINO_C5, 11, 10, 7, 12)

for i in range (23, 24):
    fitMedia(MARINO_F_4, 11, i + 0.25, i + 0.375)
    fitMedia(MARINO_E4, 7, i + 0.375, i + 0.5)
    fitMedia(MARINO_F_4, 11, i + 0.5, i + 2)

secondA(25, MARINO_E5, MARINO_B4, MARINO_D5, 14, 10, 15)
secondB(29, MARINO_F_5, MARINO_B4, MARINO_A4, 16, 10, 13)
secondC(33, MARINO_B4, MARINO_G5, MARINO_E5, MARINO_D5, 10, 17, 14, 15)
secondD(37, MARINO_B4, MARINO_F_5, MARINO_D5, MARINO_A4, 10, 16, 15, 13)

third(41, MARINO_B4, MARINO_E5, MARINO_G5, MARINO_C5, 10, 14, 17, 12)
third(43, MARINO_B4, MARINO_D5, MARINO_G5, MARINO_A4, 10, 15, 17, 13)
third(45, MARINO_F_4, MARINO_B4, MARINO_D5, MARINO_G4, 11, 10, 15, 9)
third(47, MARINO_A4, MARINO_D5, MARINO_F_5, MARINO_G4, 13, 15, 16, 9)
 
third(49, MARINO_B4, MARINO_E5, MARINO_G5, MARINO_C5, 10, 14, 17, 12)
third(51, MARINO_B4, MARINO_D5, MARINO_G5, MARINO_A4, 10, 15, 17, 13)
third(53, MARINO_F_4, MARINO_B4, MARINO_D5, MARINO_G4, 11, 10, 15, 9)

for i in range (55, 56):
    fitMedia(MARINO_A4, 13, i, i + 0.125)
    fitMedia(MARINO_D5, 15, i + 0.125 , i + 0.25)
    fitMedia(MARINO_F_5, 16, i + 0.25, i + 0.375)
    fitMedia(MARINO_A4, 13, i + 0.375, i + 0.5)
    fitMedia(MARINO_D5, 15, i + 0.5 , i + 0.625)
    fitMedia(MARINO_F_5, 16, i + 0.625, i + 0.75)
    fitMedia(MARINO_A4, 13, i + 0.75, i + 0.875)
    fitMedia(MARINO_D5, 15, i + 0.875 , i + 1)
    fitMedia(MARINO_F_5, 16, i + 1, i + 1.125)
    fitMedia(MARINO_A4, 13, i + 1.125, i + 1.25)
    fitMedia(MARINO_D5, 15, i + 1.25 , i + 1.375)
    fitMedia(MARINO_F_5, 16, i + 1.375, i + 1.5)
    fitMedia(MARINO_A4, 13, i + 1.5, i + 1.625)
    fitMedia(MARINO_D5, 15, i + 1.625 , i + 1.75)
    fitMedia(MARINO_F_5, 16, i + 1.75, i + 2)

first(57, MARINO_G5, MARINO_B5, MARINO_F_5, MARINO_C6, 17, 18, 16, 19)
first(59, MARINO_F_5, MARINO_G5, MARINO_G5, MARINO_A5, 16, 17, 17, 20)
first(61, MARINO_F_5, MARINO_B5, MARINO_E5, MARINO_C6, 16, 18, 14, 19)

for i in range (63, 64):
    fitMedia(MARINO_F_5, 16, i + 0.25, i + 0.375)
    fitMedia(MARINO_E5, 14, i + 0.375, i + 0.5)
    fitMedia(MARINO_F_5, 16, i + 0.5, i + 2)

secondA(65, MARINO_E6, MARINO_B5, MARINO_D6, 21, 18, 22)
secondB(69, MARINO_F_6, MARINO_B5, MARINO_A5, 23, 18, 20)
secondC(73, MARINO_B5, MARINO_G6, MARINO_E6, MARINO_D6, 18, 24, 21, 22)
secondD(77, MARINO_B5, MARINO_F_6, MARINO_D6, MARINO_A5, 18, 23, 22, 20)

third(81, MARINO_B5, MARINO_E6, MARINO_G6, MARINO_C6, 18, 21, 24, 19)
third(83, MARINO_B5, MARINO_D6, MARINO_G6, MARINO_A5, 18, 22, 24, 20)
third(85, MARINO_F_5, MARINO_B5, MARINO_D6, MARINO_G5, 16, 18, 22, 17)
third(87, MARINO_A5, MARINO_D6, MARINO_F_6, MARINO_G5, 20, 22, 23, 17)
 
third(89, MARINO_B5, MARINO_E6, MARINO_G6, MARINO_C6, 18, 21, 24, 19)
third(91, MARINO_B5, MARINO_D6, MARINO_G6, MARINO_A5, 18, 22, 24, 20)
third(93, MARINO_F_5, MARINO_B5, MARINO_D6, MARINO_G5, 16, 18, 22, 17)

for i in range (95, 96):
    fitMedia(MARINO_A5, 20, i, i + 0.125)
    fitMedia(MARINO_D6, 22, i + 0.125 , i + 0.25)
    fitMedia(MARINO_F_6, 23, i + 0.25, i + 0.375)
    fitMedia(MARINO_A5, 20, i + 0.375, i + 0.5)
    fitMedia(MARINO_D6, 22, i + 0.5 , i + 0.625)
    fitMedia(MARINO_F_6, 23, i + 0.625, i + 0.75)
    fitMedia(MARINO_A5, 20, i + 0.75, i + 0.875)
    fitMedia(MARINO_D6, 22, i + 0.875 , i + 1)
    fitMedia(MARINO_F_6, 23, i + 1, i + 1.125)
    fitMedia(MARINO_A5, 20, i + 1.125, i + 1.25)
    fitMedia(MARINO_D6, 22, i + 1.25 , i + 1.375)
    fitMedia(MARINO_F_6, 23, i + 1.375, i + 1.5)
    fitMedia(MARINO_A5, 20, i + 1.5, i + 1.625)
    fitMedia(MARINO_D6, 22, i + 1.625 , i + 1.75)
    fitMedia(MARINO_F_6, 23, i + 1.75, i + 2)

fitMedia(MARINO_G5, 17, 97, 100)
fitMedia(MARINO_E6, 21, 97, 100)

finish()
