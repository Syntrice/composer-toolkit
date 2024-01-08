import music21 as m21
from composer_toolkit import isorhythm, lyric_tools, tools, transformations, canon

# --------
# Setup lyric objects
# --------

VERSE_1_TEXT = "Plan-ge qua-si vir-go, plebs me-a u-lu-la-te, pas-to-res, in ci-ne-re et ci-li-ci-o."
VERSE_2_TEXT = "Ac-cin-gi-te vos, sa-cer-do-tes, et plan-gi-te, mi-ni-stri al-ta-ris, as-per-gi-te vos ci-ne-re."   
CHORUS_TEXT = "Qui-a ve-ni-et di-es Do-mi-ni mag-na et a-ma-ra val-de."

verse1 = lyric_tools.text_to_lyrics(VERSE_1_TEXT)
verse2 = lyric_tools.text_to_lyrics(VERSE_2_TEXT)
chorus = lyric_tools.text_to_lyrics(CHORUS_TEXT)

part1 = m21.stream.Part()
part2 = m21.stream.Part()
part3 = m21.stream.Part()
part4 = m21.stream.Part()

part1.insert(0, m21.instrument.Violin())
part2.insert(0, m21.instrument.Violin())
part3.insert(0, m21.instrument.Viola())
part4.insert(0, m21.instrument.Violoncello())

# -------- 
# Verse 1
# --------

pitches = ["C4","D4","E4","C4","B3","C4","A3","B3","G3","F#3","B3","G3","C4","D4","E4","B3","A#3","G3","A3","C4","F4","E4","D4","Bb3","A3"]
talea = [8]
key_space = m21.scale.MajorScale("C4")

melody1a = isorhythm.create_isorhythm(pitches, talea, color_offset=0, talea_offset=0,length=len(verse1))
melody2a = isorhythm.create_isorhythm(pitches, talea, color_offset=1, talea_offset=0,length=len(verse1))
melody3a = isorhythm.create_isorhythm(pitches, talea, color_offset=2, talea_offset=0,length=len(verse1))
melody4a = isorhythm.create_isorhythm(pitches, talea, color_offset=3, talea_offset=0,length=len(verse1))

melody1a = lyric_tools.apply_lyrics_to_stream(melody1a, verse1, 1)
melody3a = lyric_tools.apply_lyrics_to_stream(melody3a, verse1, 1)
melody4a = lyric_tools.apply_lyrics_to_stream(melody4a, verse1, 1)
melody2a = lyric_tools.apply_lyrics_to_stream(melody2a, verse1, 1)

canon.canonize(melody1a, melody2a, melody3a, melody4a, delay_duration=2, in_place=True)

# # Apply transpositions
# transformations.scalar_transposition(melody1a, 7, key_space, in_place=True)
# transformations.scalar_transposition(melody2a, 4, key_space, in_place=True)
# transformations.scalar_transposition(melody3a, 0, key_space, in_place=True)
# transformations.scalar_transposition(melody4a, -4, key_space, in_place=True)

# Apply transpositions
transformations.scalar_transposition(melody1a, 7, key_space, in_place=True)
transformations.scalar_transposition(melody2a, 4, key_space, in_place=True)
transformations.scalar_transposition(melody3a, 0, key_space, in_place=True)
transformations.scalar_transposition(melody4a, -4, key_space, in_place=True)

tools.append_stream(part1, melody1a)
tools.append_stream(part2, melody2a)
tools.append_stream(part3, melody3a)
tools.append_stream(part4, melody4a)

part1.append(m21.note.Rest(8))
part2.append(m21.note.Rest(6))
part3.append(m21.note.Rest(4))
part4.append(m21.note.Rest(2))

# --------
# Verse 2
# --------

# pitches = ["C4","C4","D4","D4","E4","E4","C4","C4","B3","B3","C4","C4","A3","A3","B3","B3"]
# talea = [4]
# key_space = m21.scale.MajorScale("E4")

# melody1b = isorhythm.create_isorhythm(pitches, talea, color_offset=0, talea_offset=0,length=len(verse2)).transpose('M3')
# melody2b = isorhythm.create_isorhythm(pitches, talea, color_offset=2, talea_offset=0,length=len(verse2)).transpose('M3')
# melody3b = isorhythm.create_isorhythm(pitches, talea, color_offset=4, talea_offset=0,length=len(verse2)).transpose('M3')
# melody4b = isorhythm.create_isorhythm(pitches, talea, color_offset=6, talea_offset=0,length=len(verse2)).transpose('M3')

# melody1b = lyric_tools.apply_lyrics_to_stream(melody1b, verse2, 1)
# melody3b = lyric_tools.apply_lyrics_to_stream(melody3b, verse2, 1)
# melody4b = lyric_tools.apply_lyrics_to_stream(melody4b, verse2, 1)
# melody2b = lyric_tools.apply_lyrics_to_stream(melody2b, verse2, 1)

# canon.canonize(melody1b, melody2b, melody3b, melody4b, delay_duration=2, in_place=True)

# # Apply transpositions
# transformations.scalar_transposition(melody1b, 7, key_space, True)
# transformations.scalar_transposition(melody2b, 4, key_space, True)
# transformations.scalar_transposition(melody3b, 0, key_space, True)
# transformations.scalar_transposition(melody4b, -4, key_space, True)

# tools.append_stream(part1, melody1b)
# tools.append_stream(part2, melody2b)
# tools.append_stream(part3, melody3b)
# tools.append_stream(part4, melody4b)

# part1.append(m21.note.Rest(8))
# part2.append(m21.note.Rest(6))
# part3.append(m21.note.Rest(4))
# part4.append(m21.note.Rest(2))

# --------
# Chorus
# --------

# pitches = ["C4","C4","D4","D4","E4","E4","C4","C4","B3","B3","C4","C4","A3","A3","B3","B3"]
# talea = [4]
# key_space = m21.scale.MajorScale("B3")

# melody1c = isorhythm.create_isorhythm(pitches, talea, color_offset=0, talea_offset=0,length=len(chorus)).transpose('m2')
# melody3c = isorhythm.create_isorhythm(pitches, talea, color_offset=2, talea_offset=0,length=len(chorus)).transpose('m2')
# melody2c = isorhythm.create_isorhythm(pitches, talea, color_offset=4, talea_offset=0,length=len(chorus)).transpose('m2')
# melody4c = isorhythm.create_isorhythm(pitches, talea, color_offset=6, talea_offset=0,length=len(chorus)).transpose('m2')

# melody1c = lyric_tools.apply_lyrics_to_stream(melody1c, chorus, 1)
# melody3c = lyric_tools.apply_lyrics_to_stream(melody3c, chorus, 1)
# melody4c = lyric_tools.apply_lyrics_to_stream(melody4c, chorus, 1)
# melody2c = lyric_tools.apply_lyrics_to_stream(melody2c, chorus, 1)

# canon.canonize(melody1c, melody2c, melody3c, melody4c, delay_duration=2, in_place=True)

# # Apply transpositions
# transformations.scalar_transposition(melody1c, 7, key_space, True)
# transformations.scalar_transposition(melody2c, 4, key_space, True)
# transformations.scalar_transposition(melody3c, 0, key_space, True)
# transformations.scalar_transposition(melody4c, -4, key_space, True)

# tools.append_stream(part1, melody1c)
# tools.append_stream(part2, melody2c)
# tools.append_stream(part3, melody3c)
# tools.append_stream(part4, melody4c)

score = tools.streams_to_score(part1, part2, part3, part4)
score.show()
