from typing import List
from music21 import note

class Lyrics:
    def __init__(self, text: str):
        """A class which represents some lyrics.

        Args:
            text (str): the text of the lyrics. For now, this should be manually syllabized
            by means of hyphens, i.e. each syllable should be separated by a "-" symbol.
        """

        self._text = text

    def text(self, syllablized: bool = False) -> str:
        """
        Returns the text of the lyrics.

        Parameters:
            syllablized (bool): Indicates whether the text should include syllables or not.
                If True, the text will include syllables represented by hyphens ("-").
                If False (default), the text will not include syllables.

        Returns:
            str: The text of the lyrics.
        """
        if syllablized:
            return self._text

        return self._text.replace("-", "")

    def words(self, syllablized: bool = False) -> List[str]:
        """
        Returns a list of words in the lyrics.

        Parameters:
            syllablized (bool): Indicates whether the words should include syllables or not.
                If True, the words will include syllables represented by hyphens ("-").
                If False (default), the words will not include syllables.

        Returns:
            List[str]: A list of words in the lyrics.
        """
        if syllablized:
            return self._text.split(" ")

        return self._text.replace("-", "").split(" ")

    def syllables(self) -> List[str]:
        """
        Returns a list of syllables in the lyrics.

        Returns:
            List[str]: A list of syllables in the lyrics.
        """
        return self._text.replace("-", " ").split(" ")