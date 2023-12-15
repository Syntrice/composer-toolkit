import music21 as m21
from composer_toolkit import tools, isorhythm, canon

if __name__ == "__main__":
    pitches = ["C4", "C4", "G4", "G4", "A4", "A4", "G4", "F4", "F4", "E4", "E4", "D4", "D4", "C4"]
    durations = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2]


    melody1 = isorhythm.create_isorhythm(pitches, durations).transpose(24)
    melody2 = isorhythm.create_isorhythm(pitches, durations).transpose(12)
    melody3 = isorhythm.create_isorhythm(pitches, durations).transpose(0)
    melody4 = isorhythm.create_isorhythm(pitches, durations).transpose(-12)
    
    canon.canonize(melody1, melody2, melody3, melody4, delay_duration=2)

    score = tools.streams_to_score(melody1, melody2, melody3, melody4)
    score.show()
