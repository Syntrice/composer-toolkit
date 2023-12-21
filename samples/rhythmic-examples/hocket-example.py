from json import tool
import music21 as m21
from composer_toolkit import tools, isorhythm, hocket, canon

pitches = [["C4","D4","E4","C4","B3","C4","A3","B3"],
            ["C4","E4","B3","A3","G3","C4","D4","B3"]]

times_each = 1

durations = [2]

melody = m21.stream.Stream()

for pitchset in pitches:
    for i in range(times_each):
        tools.append_stream(melody, isorhythm.create_isorhythm(pitchset, durations))

part1, part3, part2, part4 = hocket.hocket_melody(4, melody)

part1, part2, part3, part4 = tools.augment_into_rests(part1, part2, part3, part4)

#canon.canonize(part1, part2, part3, part4, delay_duration=4, in_place=True)

part1.transpose(24, inPlace=True)
part2.transpose(12, inPlace=True)
part3.transpose(0, inPlace=True)
part4.transpose(-12, inPlace=True)

part1.insert(0, m21.instrument.Violin())
part2.insert(0, m21.instrument.Violin())
part3.insert(0, m21.instrument.Viola())
part4.insert(0, m21.instrument.Violoncello())

score = tools.streams_to_score(part1, part2, part3, part4)

score.show()
