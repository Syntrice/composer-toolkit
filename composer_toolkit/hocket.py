import enum
import numbers
from copy import deepcopy
from typing import Union, Sequence, Optional
from music21 import duration
from music21 import note
from music21 import stream
from music21 import pitch
from music21 import chord



def hocket_melody(
    num_voices: int,
    melody: stream.Stream
) -> list[stream.Stream]:
    
    streams = [stream.Stream() for _ in range(num_voices)]
    
    for i, n in enumerate(melody.notes):
        streams[i % num_voices].append(deepcopy(n))
        # all other voices get rests
        for j in range(0, num_voices):
            if i % num_voices != j:
                streams[j].append(note.Rest(duration=deepcopy(n.duration)))
        
    return streams