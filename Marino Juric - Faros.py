#		python code
#		script_name: Faros
#
#		author: Marino
#		description: original music 
#

from earsketch import *

init()
setTempo(120)

fitMedia(HOUSE_SFX_WHOOSH_006, 1, 1, 3)
fitMedia(HOUSE_MAIN_BEAT_003, 2, 3.5, 7.5)
setEffect(2, VOLUME, GAIN, -40, 3.5, -10, 7.5)
fitMedia(HOUSE_MAIN_BEAT_004, 3, 7.5, 11.5)
setEffect(3, VOLUME, GAIN, -10, 7.5, 0, 10.5)

fitMedia(HOUSE_MAIN_BEAT_001, 4, 11.5, 15.5)
fitMedia(HOUSE_MAIN_BEAT_008, 5, 15.5, 19.5)
fitMedia(HOUSE_MAIN_BEAT_011, 6, 19.5, 23.5)
fitMedia(HOUSE_ACOUSTIC_PIANO_003, 7, 11.5, 23.5)

fitMedia(HOUSE_MAIN_BEAT_006, 1, 23.5, 24.5)

fitMedia(HOUSE_MAIN_BEAT_011, 6, 24.5, 28.5)
fitMedia(HOUSE_ACOUSTIC_PIANO_003, 7, 24.5, 28.5)

fitMedia(HOUSE_MAIN_BEAT_006, 1, 28.5, 29.5)

fitMedia(HOUSE_MAIN_BEAT_011, 6, 29.5, 33.5)
fitMedia(HOUSE_ACOUSTIC_PIANO_003, 7, 29.5, 33.5)

fitMedia(HOUSE_MAIN_BEAT_006, 1, 33.5, 34.5)

fitMedia(RD_UK_HOUSE_MAINBEAT_2, 8, 34.5, 48.5)
fitMedia(HOUSE_BREAKBEAT_022, 7, 40.5, 41)
fitMedia(HOUSE_BREAKBEAT_022, 7, 41.5, 42)
fitMedia(HOUSE_BREAKBEAT_022, 7, 42.5, 44)
fitMedia(HOUSE_BREAKBEAT_022, 7, 44.5, 45)
fitMedia(HOUSE_BREAKBEAT_022, 7, 45.5, 46)
fitMedia(HOUSE_BREAKBEAT_022, 7, 46.5, 48)

fitMedia(RD_UK_HOUSE_SOLODRUMPART_1, 9, 48.5, 58.5)
fitMedia(HOUSE_BREAKBEAT_022, 7, 48.5, 49.5)
fitMedia(HOUSE_BREAKBEAT_022, 7, 50.5, 51.5)
fitMedia(HOUSE_BREAKBEAT_022, 7, 52.5, 54.5)
fitMedia(HOUSE_BREAKBEAT_022, 7, 54.5, 56.5)

fitMedia(RD_UK_HOUSE_MAINBEAT_2, 8, 58.5, 63.5)
fitMedia(HOUSE_MAIN_BEAT_006, 1, 63.5, 65.5)

fitMedia(HOUSE_MAIN_BEAT_011, 5, 65.5, 69.5)
fitMedia(HOUSE_MAIN_BEAT_008, 6, 69.5, 75.5)
setEffect(6, VOLUME, GAIN, 0, 69.5, -20, 75.5)
fitMedia(HOUSE_ACOUSTIC_PIANO_003, 7, 65.5, 73.5)
setEffect(7, VOLUME, GAIN, 0, 65.5, -30, 73.5)

fitMedia(HOUSE_MAIN_BEAT_004, 3, 75.5, 76.5)
setEffect(3, VOLUME, GAIN, -20, 75.5, -21, 76.5)
fitMedia(HOUSE_MAIN_BEAT_003, 2, 76.5, 77.5)
setEffect(2, VOLUME, GAIN, -20, 76.5, -21, 77.5)
fitMedia(RD_UK_HOUSE__SFX_CRITTLES_1, 10, 77.5, 78.5)

finish()
