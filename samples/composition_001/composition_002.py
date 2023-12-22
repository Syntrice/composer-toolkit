import music21 as m21
from composer_toolkit import tools, isorhythm, canon, minimalism, scales, transformations

scale = scales.PentatonicScale(mode=5, tonic="C4")
rhythm = [1,3,2,0.5,0.5,1.5,2,3,0.5,1]
pitches = tools.notes_to_stream(scale.getPitches())

stream = stream = m21.stream.Stream()

for i in range(10):
    tools.append_stream(stream, transformations.scalar_transposition(pitches, i, scale))

melody = isorhythm.create_isorhythm(stream, rhythm)

melody.show()