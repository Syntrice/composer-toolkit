import music21 as m21
from composer_toolkit import tools, isorhythm, canon, minimalism

#pitches = ["C4","D4","E4","C4","B3","C4","A3","B3"]
#rhythm = [1,2,0.5,0.5,1.5,0.5,0.5,1.5,2]

pitches = ["C4","D4","E4","C4","B3","C4","A3","B3"]
rhythm = [1,3,2,0.5,0.5,1.5,2,3,0.5,1]

melody = minimalism.additive_process(tools.notes_to_stream(pitches), direction=minimalism.Direction.OUTWARD, repetitions=2 )

melody = isorhythm.create_isorhythm(melody, rhythm)

melody.show()