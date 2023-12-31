import pytest
from music21 import converter
from composer_toolkit import isorhythm


@pytest.fixture
def pitches_sequence():
    return converter.parse("tinyNotation: C D E F G")


@pytest.fixture
def durations_sequence():
    c = [1, 1, 2]
    return c


def test_create_isorhythm(pitches_sequence, durations_sequence):
    result = isorhythm.create_isorhythm(pitches_sequence, durations_sequence)
    intended_result = converter.parse(
        """
        tinyNotation: C4 D4 E2 F4 G4 C2 D4 E4 F2 G4 C4 D2 E4 F4 G2 
        """
    )
    assert list(result.flat.notes) == list(intended_result.flat.notes)


def test_create_isorhythm_length(pitches_sequence, durations_sequence):
    result = isorhythm.create_isorhythm(pitches_sequence, durations_sequence, 18)
    intended_result = converter.parse(
        """
        tinyNotation: C4 D4 E2 F4 G4 C2 D4 E4 F2 G4 C4 D2 E4 F4 G2 C4 D4 E2
        """
    )
    assert list(result.flat.notes) == list(intended_result.flat.notes)
