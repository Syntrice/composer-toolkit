"""
Functions for generating isorhythmic constructions from pitch and rhythm sequences.

This file incorporates and extends code covered by the following license:

    MIT License

    Copyright (c) 2020 Georges Dimitrov https://github.com/georgesdimitrov/arvo

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
"""

import numbers
from typing import Optional, Union, Sequence
import math

from music21 import stream
from music21 import duration
from music21 import pitch
from music21 import note
from music21 import chord

from composer_toolkit import tools
import copy

__all__ = ["create_isorhythm"]

def create_isorhythm(
    pitches: Union[
        stream.Stream,
        Sequence[Union[numbers.Number, str, pitch.Pitch, note.Note, chord.Chord]],
    ],
    durations: Union[
        stream.Stream,
        Sequence[Union[numbers.Number, duration.Duration, note.Note, chord.Chord]],
    ],
    length: Optional[int] = None,
    color_offset: int = 0,
    talea_offset: int = 0,
    gap: int = 0,
) -> stream.Stream:
    """Creates an isorhythmic construction from pitches and durations sequences.

    Args:
        pitches: The stream or Sequence containing pitch information. Sequence can consist of
            pitch classes (0-11), midi note numbers (12+), note names (str), music21 Pitch objects
            or music21 Note objects.
        durations: The stream or Sequence containing duration information. Sequence can consist
            of numeric values (1 = quarter note), music21 Duration objects or music21 Note objects.
        length: Optional; The length of the resulting stream, expressed in isorhythmic elements.
            By default, the process continues until the cycle is completed. For example, provided a
            color of 5 pitches and a talea of 7 rhythms, this function will, by default, return an
            isorhythm of 35 elements.
        color_offset: Optional; The offset at which the color sequence should start.
        talea_offset: Optional; The offset at which the talea sequence should start.
        gap: Optional; The length of a rest in quarter notes to insert between each isorhythmic element.

    Returns:
        The stream created by the isorhythmic process.
    """

    result_stream = stream.Stream()

    # create pitches list
    if not isinstance(pitches, stream.Stream):
        pitches = tools.notes_to_stream(pitches)
    color = [p.pitch for p in pitches.flatten().notes]

    # create durations list
    if not isinstance(durations, stream.Stream):
        durations = tools.durations_to_stream(durations)
    talea = [d.duration for d in durations.flatten().notes]

    # calculate the length of a complete cylce of isorhythm before the sequence repeats
    if length is None:
        length = math.lcm(len(color), len(talea))

    for i in range(length):
        result_stream.append(
            note.Note(
                pitch=copy.deepcopy(color[(i + color_offset) % len(color)]),
                duration=copy.deepcopy(talea[(i + talea_offset) % len(talea)]),
            )        
        )
        
        if gap > 0:
            result_stream.append(note.Rest(duration=duration.Duration(gap)))

    return result_stream
