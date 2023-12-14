import music21 as m21
from composer_toolkit import tools, isorhythm, transformations
import copy

if __name__ == "__main__":
    dur = [4]
    pitches = tools.notes_to_stream(["C4","B3","C4","A3","B3","G3","A3"])
    durations = tools.durations_to_stream([i*4 for i in dur])
    

    melody1 = isorhythm.create_isorhythm(pitches, durations).transpose(24)
    melody2 = isorhythm.create_isorhythm(pitches, durations, color_offset=0, talea_offset=1).transpose(12)
    melody3 = isorhythm.create_isorhythm(pitches, durations, color_offset=0, talea_offset=2).transpose(0)
    melody4 = isorhythm.create_isorhythm(pitches, durations, color_offset=0, talea_offset=3).transpose(-12)
    
    melody1[0].augmentOrDiminish(0.25, inPlace=True)
    melody2[0].augmentOrDiminish(0.5, inPlace=True)
    melody3[0].augmentOrDiminish(0.75, inPlace=True)
    melody4[0].augmentOrDiminish(1, inPlace=True)
    
    melody1.insert(0, m21.instrument.Organ())
    melody2.insert(0, m21.instrument.Organ())
    melody3.insert(0, m21.instrument.Organ())
    melody4.insert(0, m21.instrument.Organ())
    
    score = tools.streams_to_score(melody1, melody2, melody3, melody4)
    score.show()