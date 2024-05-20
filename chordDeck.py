import random
import Data
import Chord
from chordFlashcard import ChordFlashcard

class ChordDeck:

    def __init__(self,settings,initial_subset_size):
        flashcards_aux = []
        self.roots_subset = dict(filter(lambda elem: elem[0] in settings.roots, Data.note_number_names.items()))
        for chord_root in settings.roots:
            for chord_quality in settings.qualities:
                for upper_triad_position in settings.upper_triad_positions:
                    flashcards_aux.append(ChordFlashcard(chord_root,chord_quality,upper_triad_position))
        self.deck = flashcards_aux
        
        print([(flashcard.chord_root,flashcard.chord_quality) for flashcard in self.deck])
        self.sub_deck = []
        for i in range(initial_subset_size):
            self.increase_pullable_pool()
        self.current_flashcard = None
        self.max_flashcard_count=0


    def new_pick(self):
        if self.deck is None: ## Quiza esto al pedo porque si el random.choice devuelve none cuando la lista esta vacia??
            return None
        for i in range(10):
            print([(flashcard.chord_root,flashcard.chord_quality) for flashcard in self.sub_deck])
            print([el.count for el in self.sub_deck])
            random_pick = random.choices(self.sub_deck, weights=self.get_calculated_weights(), k=1)[0]
            if random_pick != self.current_flashcard: ################## no se si este equals esta bien!! Repasar como funcan los equals in Python
                self.current_flashcard = random_pick
                self.adjust_pick_counts(random_pick)
                return random_pick
        return random_pick

    def get_calculated_weights(self):
        print([self.max_flashcard_count - el.count +1 for el in self.sub_deck])
        return [self.max_flashcard_count - el.count +1 for el in self.sub_deck]

    def adjust_pick_counts(self,random_pick):
        random_pick.increase_show_weight()
        if random_pick.count > self.max_flashcard_count:
            self.max_flashcard_count = random_pick.count

    def increase_pullable_pool(self):
        if len(self.deck) > 0:
            pulled_card = random.choice(self.deck)
            self.deck.remove(pulled_card)
            self.sub_deck.append(pulled_card)
            print([(flashcard.chord_root,flashcard.chord_quality) for flashcard in self.deck])
            print([(flashcard.chord_root,flashcard.chord_quality) for flashcard in self.sub_deck])

    def process_attempt_input(self,notes_on):
        if self.current_flashcard.is_played_chord(notes_on):
            self.new_pick()
            return True
        return False

        """
    def get_random_chord_dict(self,roots,qualities,upper_triad_inversions):
        ## ************** MISSING TO EXCLUDE PREVIOUS SELECTION *****************
        # subset all possibilities to keep only the ones in Settings.txt
        root_subset = dict(filter(lambda elem: elem[0] in roots, Data.note_number_names.items())) 
        root_abs = random.choice(list(root_subset))

        quality = random.choice(list(qualities))
        upper_shape_quality = Data.upper_triad_quality_by_quality[quality]
        upper_shapes_subset = dict(filter(lambda elem: elem[0][0] in upper_triad_inversions and elem[0][1] == upper_shape_quality, Data.upper_shapes.items()))

        #OOP! Esta logica iria en clase "Chord" en la funcion correspondiente!
        upper_triad_root_num = Chord.increase_solfege_note_by_semitones(Data.note_number_names[root_abs], Data.upper_triad_root_by_quality[quality])

        upper_triad_inversion_quality = random.choice(list(upper_shapes_subset)) 
        print(root_abs)
        print(upper_triad_inversion_quality)
        #return (root,upper_triad_inversion)
        return {
            "root_abs" : root_abs,
            "chord_quality" : quality,
            "upper_triad_root_num" : upper_triad_root_num,
            "upper_triad_inversion_n_quality" : upper_triad_inversion_quality        
        }

"""