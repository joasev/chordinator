#import Data
import random
from ProgressionFlashcard import ProgressionFlashcard

class ProgressionDeck:

    def __init__(self,settings):
        flashcards_aux = []
        for chord_root in settings.roots:
            for progression in settings.progressions:
                flashcards_aux.append(ProgressionFlashcard(chord_root,progression))
        self.deck = flashcards_aux
        
        #print([(flashcard.chord_root,flashcard.chord_quality) for flashcard in self.deck])
        self.current_flashcard = None
        #self.max_flashcard_count=0
    

    def new_pick(self):
        if self.deck is None: ## Quiza esto al pedo porque si el random.choice devuelve none cuando la lista esta vacia??
            return None
        for i in range(10):
            #print([(flashcard.chord_root,flashcard.chord_quality) for flashcard in self.sub_deck])
            #print([el.count for el in self.sub_deck])
            
            # random_pick = random.choices(self.sub_deck, weights=self.get_calculated_weights(), k=1)[0]
            random_pick = random.choice(self.deck)
            if random_pick != self.current_flashcard:
                break
                #self.current_flashcard = random_pick
                #return random_pick
        print("New card!")
        random_pick.reset()
        self.current_flashcard = random_pick
        return random_pick

    def process_attempt_input(self,notes_on):
        all_flashcard_finished = self.current_flashcard.process_attempt(notes_on)
        if all_flashcard_finished:
            self.new_pick()
            return True
        return False