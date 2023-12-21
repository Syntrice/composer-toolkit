"""
Convenient helper functions for quickly manipulating and combining music21 elements.

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
from typing import Union, Sequence, Optional, Type
from copy import deepcopy
from music21 import duration
from music21 import note
from music21 import stream
from music21 import pitch
from music21 import chord

__all__ = [
    "convert_stream",
    "notes_to_stream",
    "durations_to_stream",
    "merge_streams",
    "append_stream",
]


def convert_stream(
    original_stream: stream.Stream,
    stream_class: Type[Union[stream.Voice, stream.Part, stream.Score]],
) -> stream.Stream:
    """Converts a stream to a the specified type

    Args:
        original_stream: The Stream to convert.
        stream_class: The type of stream to convert to (Score, Part or Voice).

    Returns:
        Converted stream.
    """
    if stream_class is stream.Score:
        post_stream = stream.Score()
    elif stream_class is stream.Part:
        post_stream = stream.Part()
    elif stream_class is stream.Voice:
        post_stream = stream.Voice()

    for element in original_stream.elements:
        post_stream.append(element)
    return post_stream


def notes_to_stream(
    pitches: Sequence[Union[numbers.Number, str, pitch.Pitch, note.Note, chord.Chord]]
) -> stream.Stream:
    """Creates a stream from a sequence of pitches.

    Args:
        pitches: Sequence of pitches to convert to a stream. Sequence can consist of pitch classes
          (0-11), midi note numbers (12+), note names (str), music21 Pitch objects, music21
          Note objects or music21 Chord objects.

    Returns:
        Stream containing a sequence of notes with the corresponding pitches.
    """
    post_stream = stream.Stream()
    for pitch_ in pitches:
        if isinstance(pitch_, (str, pitch.Pitch)):
            post_stream.append(note.Note(pitch_))
        elif isinstance(pitch_, numbers.Number):
            note_ = note.Note(pitch_)
            if note_.pitch.accidental.name == "natural":
                note_.pitch.accidental = None
            post_stream.append(note_)
        elif isinstance(pitch_, (note.Note, chord.Chord)):
            post_stream.append(pitch_)
    return post_stream


def durations_to_stream(
    durations: Sequence[Union[numbers.Number, duration.Duration, note.Note]]
):
    """Converts a sequence of durations to a Stream containing note objects of that duration.

    Args:
        durations: Sequence of durations to convert to a stream. Sequence can consist of numeric
          values (1 = quarter note), music21 Duration objects or music21 Note objects.

    Returns:
        Stream containing a sequence of notes with the corresponding durations.
    """
    post_stream = stream.Stream()
    for duration_ in durations:
        if isinstance(duration_, numbers.Number):
            new_note = note.Note()
            new_note.duration = duration.Duration(duration_)
            post_stream.append(new_note)
        elif isinstance(duration_, duration.Duration):
            new_note = note.Note()
            new_note.duration = duration_
            post_stream.append(new_note)
        elif isinstance(duration_, note.Note):
            post_stream.append(duration_)
    return post_stream


def merge_streams(
    *streams: stream.Stream,
    stream_class: Optional[Type[Union[stream.Voice, stream.Part, stream.Score]]] = None
) -> stream.Stream:
    """

    Creates a new stream by combining streams vertically.

    Args:
        *streams: Streams to merge.
        stream_class: Optional; The type of stream to convert to (Score, Part or Voice). By
        default, a generic Stream is returned.

    Returns:

    """
    if stream_class is None:
        post_stream = stream.Stream()
    if stream_class is stream.Score:
        post_stream = stream.Score()
    elif stream_class is stream.Part:
        post_stream = stream.Part()
    elif stream_class is stream.Voice:
        post_stream = stream.Voice()
    for stream_ in streams:
        post_stream.insert(0, stream_)
    return post_stream


def append_stream(original_stream: stream.Stream, *streams: stream.Stream):
    """

    Appends all elements of one or more streams at the end of a stream.

    Args:
        original_stream: The stream to append to.
        *streams: Any number of streams to be appended to the original stream.
    """
    for stream_ in streams:
        h_offset = original_stream.highestTime
        for element in stream_.elements:
            original_stream.insert(element.offset + h_offset, element)


def streams_to_score(*streams: stream.Stream) -> stream.Score:
    """

    Combines multiple streams into a single score.

    Args:
        *streams: Any number of streams to be add to a score.

    Returns:
        stream.Score: A new music21 Score containing all streams.
    """
    score = stream.Score()
    parts = []
    for s in streams:
        part = stream.Part()
        for element in s.elements:
            part.append(element)
        parts.append(part)

    for part in parts:
        score.insert(0, part)
    return score

def augment_into_rests(*streams: stream.Stream, in_place: bool = False) -> stream.Stream:
    """Function that takes a stream, and eliminates all rests AFTER THE FIRST PITCH
    by augmenting the previous pitch to take up the duration of the rest before the next pitch comes in


    Args:
        stream (stream.Stream): Any number of streams to perform the operation on
        in_place (bool, optional): Whether to perform the operation in place or not. Defaults to False.

    Returns:
        stream.Stream: Returns instances of the streams with the operation performed, or a new streams if in_place is False
    """
    
    if not in_place:
        streams = deepcopy(streams)
    
    for stream in streams:
    
        # do nothing until the first note is found
        found_first_note = False
        
        for n in stream.notesAndRests:
            if isinstance(n, note.Note):
                found_first_note = True
            elif isinstance(n, note.Rest) and found_first_note:
                # augment the previous note to take up the duration of the rest
                prev_note = stream.notesAndRests.getElementBeforeOffset(n.offset)
                prev_note.duration.quarterLength += n.duration.quarterLength
                # remove the rest
                stream.remove(n)
                
    return streams