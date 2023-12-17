import music21 as m21
from composer_toolkit import tools, isorhythm

if __name__ == "__main__":
    
    pitches = tools.notes_to_stream(["C4","B3","C4","A3","B3","G3","A3"])
    durations = tools.durations_to_stream([1, 2, 4, 1, 0.5])

    melody1 = isorhythm.create_isorhythm(pitches, durations).transpose(12)

    melody1.show()