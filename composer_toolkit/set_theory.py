""" 
A set of functions that are useful when performing the analysis of atonal works using set theory.

//TODO optimize and tidy code

"""

import itertools
from music21 import chord
from typing import List, Union, Sequence

def forte_class(
    pcset: Union[chord.Chord, Sequence[Union[int, str]]]
) -> str:
    """Returns the Forte class of a pitch class set.

    Args:
        pcset: The pitch class set to analyze. Can be a Chord object or a sequence of pitch classes.

    Returns:
        The Forte class of the pitch class set.
    """
    if not isinstance(pcset, chord.Chord):
        pcset = chord.Chord(pcset)

    return pcset.forteClass

def prime_form(
    pcset: Union[chord.Chord, Sequence[Union[int, str]]]
) -> List[int]:
    """Returns the prime form of a pitch class set.

    Args:
        pcset: The pitch class set to analyze. Can be a Chord object or a sequence of pitch classes.

    Returns:
        The prime form of the pitch class set.
    """
    if not isinstance(pcset, chord.Chord):
        pcset = chord.Chord(pcset)

    return pcset.primeForm
    

def normal_order(
    pcset: Union[chord.Chord, Sequence[Union[int, str]]],
    transposed: bool = False,
) -> List[int]:
    """Returns the normal order of a pitch class set.

    Args:
        pcset: The pitch class set to analyze. Can be a Chord object or a sequence of pitch classes.

    Returns:
        The normal order of the pitch class set.
    """
    if not isinstance(pcset, chord.Chord):
        pcset = chord.Chord(pcset)
        
    if transposed:
        transposition_interval = pcset.normalOrder[0]
        return [(pc - transposition_interval) % 12 for pc in pcset.normalOrder]

    return pcset.normalOrder

# chromatically invert all intervals of a pitch class set around the root of the normal order
def inverted(
    pcset: Union[chord.Chord, Sequence[Union[int, str]]],
    transposed: bool = False
) -> List[int]:
    """Inverts a pitch class set around the root of the normal order.

    Args:
        pcset: The pitch class set to invert. Can be a Chord object or a sequence of pitch classes.
        transposed: If True, the pitch class set is transposed to T=0 (C)

    Returns:
        The inverted pitch class set.
    """
    if not isinstance(pcset, chord.Chord):
        pcset = chord.Chord(pcset)
    
    # invert around the root of the normal order
    normal_order = pcset.normalOrder
    
    root = normal_order[0]
    inverted = [(root - pc) % 12 for pc in normal_order]
    
    inverted = chord.Chord(inverted)
            
    if transposed:
        transposition_interval = inverted.normalOrder[0]
        return [(pc - transposition_interval) % 12 for pc in inverted.normalOrder]

    return inverted.normalOrder

def complement(
    pcset: Union[chord.Chord, Sequence[Union[int, str]]],
    transposed: bool = False
) -> List[int]:
    """Returns the complement of a pitch class set. That is, the set created from of all pitch classes not in the original set.

    Args:
        pcset: The pitch class set to analyze. Can be a Chord object or a sequence of pitch classes.
        transposed: If True, the pitch class set is transposed to T=0 (C)
        
    Returns:
        The complement of the pitch class set.
    """
    
    if not isinstance(pcset, chord.Chord):
        pcset = chord.Chord(pcset)
    
    normal_order = pcset.normalOrder
    
    complement = []
    for pc in set(range(12)):
        if pc not in normal_order:
            complement.append(pc)
    
    complement = chord.Chord(complement)
    
    if transposed:
        transposition_interval = complement.normalOrder[0]
        return [(pc - transposition_interval) % 12 for pc in complement.normalOrder]
    
    return complement.normalOrder

def subsets(
    pcset: Union[chord.Chord, Sequence[Union[int, str]]]
) -> List[str]:
    """Returns all subsets of a pitch class set.

    Args:
        pcset: The pitch class set to analyze. Can be a Chord object or a sequence of pitch.
        transposed: If True, the pitch class set is transposed to T=0 (C).
        
    Returns:
        A list of all subsets of the pitch class set, given in forte numbers.
    """
    
    if not isinstance(pcset, chord.Chord):
        pcset = chord.Chord(pcset)
    
    subsets = []
    
    found = set()
    for cardinal in range(len(pcset.pitches)-1, 2, -1):
        for combination in itertools.combinations(pcset.pitches, cardinal):
            subset = chord.Chord(chord.Chord(combination))
            
            if subset.primeFormString in found:
                continue    
            
            found.add(subset.primeFormString)
            
            subsets.append(subset.forteClassTnI)
            
    return subsets

def t_operator(
    pcset1: Union[chord.Chord, Sequence[Union[int, str]]],
    pcset2: Union[chord.Chord, Sequence[Union[int, str]]],
) -> int:
    """Get the interval of transposition between two pitch class sets.

    Args:
        pcset1 (Union[chord.Chord, Sequence[Union[int, str]]]): First pitch class set.
        pcset2 (Union[chord.Chord, Sequence[Union[int, str]]]): Second pitch class set.

    Returns:
        int: the interval of transposition between the two pitch class sets.
    """
    
    if not isinstance(pcset1, chord.Chord):
        pcset1 = chord.Chord(pcset1)
        
    if not isinstance(pcset2, chord.Chord):
        pcset2 = chord.Chord(pcset2)
        
    return pcset2.normalOrder[0] - pcset1.normalOrder[0]
    