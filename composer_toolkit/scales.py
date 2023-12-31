"""
Module that extends music 21 scales system.

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

__all__ = ["AbstractPentatonicScale", "PentatonicScale"]

import music21
from music21.scale import intervalNetwork


class AbstractPentatonicScale(music21.scale.AbstractScale):
    def __init__(self, mode=None):
        super().__init__()
        self.type = "Abstract Pentatonic"
        # all pentatonic scales are octave duplicating
        self.octaveDuplicating = True
        # here, accept None
        self.buildNetwork(mode=mode)

    def buildNetwork(self, mode=None):
        src_list = ("M2", "M2", "m3", "M2", "m3")
        if mode in (None, 1, "major", "Major"):
            interval_list = src_list
            self.tonicDegree = 1
        elif mode == 2:
            interval_list = src_list[1:] + src_list[:1]
            self.tonicDegree = 1
        elif mode == 3:
            interval_list = src_list[2:] + src_list[:2]
            self.tonicDegree = 1
        elif mode == 4:
            interval_list = src_list[3:] + src_list[:3]
            self.tonicDegree = 1
        elif mode in (5, "minor", "Minor"):
            interval_list = src_list[4:] + src_list[:4]
            self.tonicDegree = 1
        else:
            raise music21.scale.ScaleException(
                f"cannot create a scale of the following mode: {mode}"
            )
        self._net = intervalNetwork.IntervalNetwork(
            interval_list,
            octaveDuplicating=self.octaveDuplicating,
            pitchSimplification="none",
        )
        # might also set weights for tonic and dominant here


class PentatonicScale(music21.scale.ConcreteScale):
    usePitchDegreeCache = True

    def __init__(self, tonic=None, mode=None):
        super().__init__(tonic=tonic)
        self._abstract = AbstractPentatonicScale(mode=mode)
        self.type = "Pentatonic"
