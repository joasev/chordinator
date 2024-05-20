from chordDeck import ChordDeck
from ProgressionDeck import ProgressionDeck

def get_flashcard_deck(settings):
    if list(settings.mode)[0] == "progressions":
        return ProgressionDeck(settings)
    else:
        return ChordDeck(settings,3)