"""
Functions for generating canonic constructions from pitch and rhythm sequences.
"""

import enum
from music21 import duration
from music21 import note
from music21 import stream
from music21 import pitch
from music21 import chord


class FramingType(enum.Enum):
    """
    Determines whether to append silence to the beginnning of delayed voices to form a canon,
    or to augment the first note of the delayed voices.
    """

    SILENCE = 0
    AUGMENT = 1


def canonize(
    *streams: stream.Stream,
    delay_duration: float = 1,
    start_type: FramingType = FramingType.SILENCE
) -> None:
    """
    Creates a canonic construction from pitches and durations sequences.

    Args:
        delay_duration (int, optional): The time difference between each voices.
        start_type (StartType, optional): How the start of the delayed voices should be handled. Can be either FramingType.SILENCE or FramingType.AUGMENT.
        end_type (StartType, optional): How the end of the delayed voices should be handled. Can be either FramingType.SILENCE or FramingType.AUGMENT.
    """

    counter = 1

    if start_type is FramingType.SILENCE:
        for s in streams[1:]:
            s.insertAndShift(0, note.Rest(length=delay_duration * counter))
            counter += 1

    elif start_type is FramingType.AUGMENT:
        for s in streams[1:]:
            s.notes.first().duration.quarterLength += delay_duration * counter
            counter += 1
