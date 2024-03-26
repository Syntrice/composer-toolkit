import itertools
from matplotlib.pylab import normal
from music21 import stream, chord, interval, pitch
from typing import List, Union, Sequence
import numbers

import music21

from composer_toolkit.transformations import octave_shift


def identify_prime_forms(
    s: Sequence[Union[chord.Chord, Sequence[Union[int, str]]]],
    transposed: bool = True,
) -> stream.Stream:

    st = stream.Stream()

    for i in range(len(s)):

        if not isinstance(s[i], chord.Chord):
            c = chord.Chord(s[i])
        else:
            c = s[i]
        
        prime_form = c.primeForm
        
        if not transposed:
            transposition = c.root().pitchClass
            prime_form = [pitch.Pitch(midi = (pc + 60 + transposition)) for pc in prime_form]
            
        c = chord.Chord(prime_form)

        # add details
        c.lyric = c.primeFormString
        c.lyric += "\n" + c.forteClassTnI
        c.lyric += "\n" + c.intervalVectorString

        # append to stream
        st.append(c)

    return st

def identify_normal_orders(
    s: Sequence[Union[chord.Chord, Sequence[Union[int, str]]]],
    tranposed: bool = False,
) -> stream.Stream:

    st = stream.Stream()

    for i in range(len(s)):

        if not isinstance(s[i], chord.Chord):
            c = chord.Chord(s[i])
        else:
            c = s[i]
            
        normal_order = c.normalOrder
        t = normal_order[0]
        if tranposed:
            normal_order = [(pc - t) % 12 for pc in normal_order]
        else:
            # convert pitch classes to strings, including octave register
            highest = 0
            _ = []
            for pc in normal_order:
                if pc < highest:
                    pc += 12
                
                highest = pc
                
                _.append(pitch.Pitch(midi = pc + 60))
                normal_order = _
                    
        c = chord.Chord(normal_order)        
        
        # add details
        c.lyric = c.normalOrderString
        c.lyric += "\n" + c.forteClass
        c.lyric += "\n" + c.intervalVectorString
        c.lyric += "\n" + "t = " + str(t)

        # append to stream
        st.append(c)

    return st

def identify_subsets(
    s: Sequence[Union[chord.Chord, Sequence[Union[int, str]]]],
    tranposed: bool = False,
) -> stream.Score:

    st = stream.Stream()
    
    for i in range(len(s)):

        if not isinstance(s[i], chord.Chord):
            c = chord.Chord(s[i])
        else:
            c = s[i]
        
        found = set()
        for cardinal in range(len(c.pitches)+1, 2, -1):
            for combination in itertools.combinations(c.pitches, cardinal):
                subset = chord.Chord(chord.Chord(combination))
                
                subset.lyric = subset.normalOrderString
                subset.lyric += "\n" + subset.forteClassTnI
                subset.lyric += "\n" + subset.intervalVectorString
                
                if subset.primeFormString not in found:
                    found.add(subset.primeFormString)
                    st.append(subset)
                
        # remove duplicates
        
        
    return st

def identify_complement(
    s: Sequence[Union[chord.Chord, Sequence[Union[int, str]]]],
    tranposed: bool = False,
) -> stream.Score:

    st = stream.Stream()
    
    for i in range(len(s)):

        if not isinstance(s[i], chord.Chord):
            c = chord.Chord(s[i])
        else:
            c = s[i]
        
        
        if tranposed:
            prime_form = c.primeForm
        
        
        prime_form = c.normalOrder 
        complement = []
    
        for pc in set(range(12)):
            if pc not in prime_form:
                complement.append(pc)
        
        complement = chord.Chord(complement)
        complement.lyric = complement.normalOrderString
        complement.lyric += "\n" + complement.forteClass
        complement.lyric += "\n" + complement.intervalVectorString
        
        st.append(complement)
                    
    return st