import random
import src.utils.data as Data
from src.core.chord_flashcard import ChordFlashcard

class ChordDeck:
    """
    The ChordDeck class manages a deck of chord flashcards for a music-related flashcard game. It:

    - Initializes a deck of ChordFlashcard objects based on user settings.
    - Manages a subset of active flashcards (sub_deck).
    - Selects new flashcards dynamically, weighted based on how often they have been shown.
    - Processes user input to determine if the correct chord was played.
    """

    def __init__(self, settings, initial_subset_size):
        """
        Initializes the ChordDeck with flashcards based on user settings.

        :param settings: The user-defined settings for root notes, qualities, and upper triad positions.
        :param initial_subset_size: The number of initial flashcards in the active subset.
        """
        flashcards_aux = []
        self.roots_subset = dict(filter(lambda elem: elem[0] in settings.roots, Data.note_number_names.items()))
        for chord_root in settings.roots:
            for chord_quality in settings.qualities:
                for upper_triad_position in settings.upper_triad_positions:
                    flashcards_aux.append(ChordFlashcard(chord_root, chord_quality, upper_triad_position))
        self.deck = flashcards_aux
        
        print("ChordDeck init")
        print([(flashcard.chord_root, flashcard.chord_quality) for flashcard in self.deck])
        self.sub_deck = []
        for i in range(initial_subset_size):
            self.increase_pullable_pool()
        self.current_flashcard = None
        self.max_flashcard_count = 0


    def new_pick(self):
        """
        Selects a new flashcard randomly from the active subset, with weighting to avoid repetition.
        """
        if self.deck is None:
            return None
        for i in range(10):
            print([(flashcard.chord_root,flashcard.chord_quality) for flashcard in self.sub_deck])
            print([el.count for el in self.sub_deck])
            random_pick = random.choices(self.sub_deck, weights=self.get_calculated_weights(), k=1)[0]
            if random_pick != self.current_flashcard: 
                self.current_flashcard = random_pick
                self.adjust_pick_counts(random_pick)
                return random_pick
        return random_pick

    def get_calculated_weights(self):
        """
        Calculates selection weights based on how often each flashcard has been picked.
        """
        print([self.max_flashcard_count - el.count +1 for el in self.sub_deck])
        return [self.max_flashcard_count - el.count +1 for el in self.sub_deck]

    def adjust_pick_counts(self,random_pick):
        """
        Updates the selection count of the picked flashcard and adjusts the max flashcard count.
        """
        random_pick.increase_show_weight()
        if random_pick.count > self.max_flashcard_count:
            self.max_flashcard_count = random_pick.count

    def increase_pullable_pool(self):
        """
        Moves a flashcard from the main deck to the active subset.
        """
        if len(self.deck) > 0:
            pulled_card = random.choice(self.deck)
            self.deck.remove(pulled_card)
            self.sub_deck.append(pulled_card)
            print([(flashcard.chord_root, flashcard.chord_quality) for flashcard in self.deck])
            print([(flashcard.chord_root, flashcard.chord_quality) for flashcard in self.sub_deck])

    def process_attempt_input(self, notes_on):
        """
        Checks if the current flashcard’s chord matches the played notes.

        :param notes_on: The set of notes currently being played.
        :return: True if the correct chord is played, otherwise False.
        """
        if self.current_flashcard.is_played_chord(notes_on):
            self.new_pick()
            return True
        return False
