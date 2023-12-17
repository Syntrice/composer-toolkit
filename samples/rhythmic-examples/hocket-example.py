from json import tool
import music21 as m21
from composer_toolkit import tools, isorhythm, hocket, canon

def augment_into_rests(stream: m21.stream.Stream):
    """function that takes a stream, and eliminates all rests AFTER THE FIRST PITCH
    by augmenting the previous pitch to take up the duration of the rest before the next pitch comes in

    """
    # do nothing until the first note is found
    found_first_note = False
    
    for n in stream.notesAndRests:
        if isinstance(n, m21.note.Note):
            found_first_note = True
        elif isinstance(n, m21.note.Rest) and found_first_note:
            # augment the previous note to take up the duration of the rest
            prev_note = stream.notesAndRests.getElementBeforeOffset(n.offset)
            prev_note.duration.quarterLength += n.duration.quarterLength
            # remove the rest
            stream.remove(n)

pitches = [
    ["C4", "E4", "G4"],
    ["D4", "F4", "A4"],
    ["A3", "C4", "E4"],
    ["G3", "B3", "D4"],
    ]

times_each = 4

durations = [1,2,0.5,1]

melody = m21.stream.Stream()

for pitchset in pitches:
    for i in range(times_each):
        tools.append_stream(melody, isorhythm.create_isorhythm(pitchset, durations))

part1, part3, part2, part4 = hocket.hocket_melody(4, melody)

augment_into_rests(part1)
augment_into_rests(part2)
augment_into_rests(part3)
augment_into_rests(part4)

canon.canonize(part1, part2, part3, part4, delay_duration=4, in_place=True)

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
