import src.utils.data as Data
from src.core.chord_flashcard import ChordFlashcard
from src.utils.note import Note

class ProgressionFlashcard:

    def __init__(self,root,progression):
        #Direct settings dependent
        self.root = root
        self.progression = progression
        #Derived
        progression_data = Data.progressions[progression]
         #List of chord flashcards!!
        self.progression_chords = [ChordFlashcard(Note(root).increase_by(degree[0]),degree[1],None,degree[2]) for degree in progression_data]
        #for degree in progression_data:
        #    ChordFlashcard(root + degree[0],degree[1],None) ## Are arguments in Python optional??

        #other
        self.count=0
        self.fc_index = 0
    
    def process_attempt(self,notes_on):
        if self.progression_chords[self.fc_index].is_played_chord(notes_on):
            print("Correct chord! Progression item: "+ str(self.fc_index))
            if self.fc_index +1 >= len(self.progression_chords):
                return True
            else:
                self.fc_index = self.fc_index + 1
                return False
            

    def get_display_string(self):
        return [chFl.get_display_string() for chFl in self.progression_chords[self.fc_index:]]

    def get_instruction_string(self):
        return self.root

    def reset(self):
        self.fc_index = 0