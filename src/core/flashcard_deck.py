from src.core.chord_deck import ChordDeck
from src.core.progressions.progression_deck import ProgressionDeck

def get_flashcard_deck(settings):
    if list(settings.mode)[0] == "progressions":
        return ProgressionDeck(settings)
    else:
        return ChordDeck(settings, 3)