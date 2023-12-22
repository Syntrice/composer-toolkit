from copy import deepcopy
from typing import List
from music21.note import Lyric
from music21 import stream


def text_to_lyrics(text: str) -> List[Lyric]:
    """Converts a string of text into a list of music21 lyrics. It does this by splitting the text into syllables and then converting each syllable into a lyric.

    Args:
        text (str): The text to convert into lyrics. Should be in syllable format, with syllables separated by hyphens.

    Returns:
        List[Lyric]: A list of music21 lyrics.
    """

    # split text into words
    words = text.split(" ")
    lyrics = []

    for word in words:
        # split word into syllables
        syllables = word.split("-")
        num_syllables = len(syllables)

        # convert each syllable into a lyric and add it to the list of lyrics
        for i, syllable in enumerate(syllables):
            syllabic = (
                "single"
                if num_syllables == 1
                else (
                    "begin"
                    if i == 0
                    else ("end" if i == num_syllables - 1 else "middle")
                )
            )
            lyrics.append(Lyric(syllable, syllabic=syllabic))

    return lyrics

def apply_lyrics_to_melody(melody: stream.Stream, lyrics: Lyric, min_lyric_interval: int = 1, in_place: bool = False) -> stream.Stream:
    """Applies the lyrics to the melody.

    Args:
        melody: The melody to apply the lyrics to.
        lyrics: The lyrics to apply to the melody.
        min_lyric_interval: The threshold for skipping a note, so minimum interval in quarter notes between lyrics.
    """
    
    if not in_place:
        melody = deepcopy(melody)
    
    i = 0
    skip = False
    for note in melody.notes:
        try:
            if skip:
                skip = False
                continue
            if note.duration.quarterLength < min_lyric_interval:
                skip = True
            note.lyric = lyrics[i]
        except IndexError as e:
            break
        
        i += 1
        
    return melody