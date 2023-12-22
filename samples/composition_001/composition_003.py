from pickle import FALSE
import music21
from pytest import skip
from composer_toolkit import isorhythm, lyric_tools


# Setup the lyrics of the composition

VERSE_1_TEXT = "Plan-ge qua-si vir-go, plebs me-a u-lu-la-te, pas-to-res, in ci-ne-re et ci-li-ci-o."
VERSE_2_TEXT = "Ac-cin-gi-te vos, sa-cer-do-tes, et plan-gi-te, mi-ni-stri al-ta-ris, as-per-gi-te vos ci-ne-re."   
CHORUS_TEXT = "Qui-a ve-ni-et di-es Do-mi-ni mag-na et a-ma-ra val-de."

#Setup the pitches of the composition

pitches = ["C4","D4","E4","C4","B3","C4","A3","B3"]
rhythm = [1,0.5,0.5,1,3]


lyrics = lyric_tools.text_to_lyrics(VERSE_1_TEXT)

melody = isorhythm.create_isorhythm(pitches, rhythm)

melody = lyric_tools.apply_lyrics_to_melody(melody, lyrics, 2)
    
melody.show()