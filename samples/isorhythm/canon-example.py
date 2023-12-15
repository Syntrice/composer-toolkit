from copy import deepcopy
import music21 as m21
from composer_toolkit import tools, isorhythm, canon

if __name__ == "__main__":
    pitches = ["C4","D4","E4","C4","B3","C4","A3","B3"]
    durations = [8]


    melody1 = isorhythm.create_isorhythm(pitches, durations, color_offset=0).transpose(24)
    melody2 = isorhythm.create_isorhythm(pitches, durations, color_offset=1).transpose(12)
    melody3 = isorhythm.create_isorhythm(pitches, durations, color_offset=2).transpose(0)
    melody4 = isorhythm.create_isorhythm(pitches, durations, color_offset=3).transpose(-12)

    melody1.append(deepcopy(melody1))
    melody2.append(deepcopy(melody2))
    melody3.append(deepcopy(melody3))
    melody4.append(deepcopy(melody4))
    
    melody1.insert(0, m21.instrument.Violin())
    melody2.insert(0, m21.instrument.Violin())
    melody3.insert(0, m21.instrument.Viola())
    melody4.insert(0, m21.instrument.Violoncello())
    
    canon.canonize(melody1, melody2, melody3, melody4, delay_duration=2)
    score = tools.streams_to_score(melody1, melody2, melody3, melody4)

    score.write("midi", fp="./output/canon-example.mid")
    score.show()