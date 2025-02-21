import src.utils.data as Data
import src.utils.chord_logic as chord_logic

class ChordFlashcard:
    """
    The ChordFlashcard class represents an individual chord flashcard in the music-related flashcard game.
    It:
    
    - Stores information about the chord's root, quality, and upper triad position.
    - Determines the chord structure and inversion based on music theory data.
    - Provides functionality to track the flashcard's selection count.
    - Contains logic for detecting if the correct chord has been played.
    """
    
    def __init__(self, chord_root,chord_quality, upper_triad_position,degree=None):
        """
        Initializes a ChordFlashcard with its chord properties.
        
        :param chord_root: The root note of the chord.
        :param chord_quality: The quality of the chord (major, minor, diminished, etc.).
        :param upper_triad_position: The inversion of the upper triad.
        :param degree: (Optional) The scale degree of the chord.
        """

        #Direct settings dependent
        self.chord_root = chord_root
        self.chord_quality = chord_quality
        self.upper_triad_position = upper_triad_position #chord inversion
        self.degree = degree

        #Derived
        self.chord_root_num = Data.note_number_names[self.chord_root]
        self.upper_triad_root_num = chord_logic.increase_solfege_note_by_semitones(self.chord_root_num, Data.upper_triad_root_by_quality[self.chord_quality])
        self.upper_triad_quality = Data.upper_triad_quality_by_quality[self.chord_quality]
        self.upper_triad_semitones_shapes = []
        if upper_triad_position is not None:
            self.upper_triad_semitones_shapes.append(Data.upper_shapes[(self.upper_triad_position, self.upper_triad_quality)])
        else:
            # Here it has to select all possibilities of upper shapes
            for k,v in Data.upper_shapes.items():
                if k[1] == self.upper_triad_quality:
                    self.upper_triad_semitones_shapes.append(v)
        self.count = 0

    def increase_show_weight(self):
        """
        Increases the flashcard's selection count.
        """
        self.count = self.count + 1

    def detect_right_hand_notes(self, notes_on):
        """
        Identifies the right-hand notes in a played chord.
        Returns the top 3 notes when more than 3 are played.
        
        :param notes_on: A set of notes currently being played.
        :return: A subset of the notes representing the right-hand chord.
        """
        right_hand_notes_on = set()
        if len(notes_on) >= 3: 
            notes_on_temp = notes_on.copy()
            for i in range (3):
                max_aux = max(notes_on_temp)
                notes_on_temp.remove(max_aux)
                right_hand_notes_on.add(max_aux)
            return right_hand_notes_on
        else:
            return notes_on

    def detect_root(self, notes_on):
        """
        Determines the root note of the played chord.
        
        :param notes_on: The set of notes currently played.
        :return: The detected root note.
        """
        if len(notes_on) >= 4:
            print(notes_on)
            print(min(notes_on))
            return chord_logic.get_solfege_note_num(min(notes_on)) 
        else:
            return chord_logic.get_root(notes_on) 
        
    def is_played_chord(self, notes_on):
        """
        Determines if the played notes match the flashcard's chord.
        
        :param notes_on: The set of notes currently played.
        :return: True if the correct chord is played, otherwise False.
        """
        right_hand_notes_on = self.detect_right_hand_notes(notes_on)
        chord_root_on = self.detect_root(notes_on)
        upper_triad_root_on = chord_logic.get_root(right_hand_notes_on)
        upper_triad_inversion = chord_logic.get_shape(right_hand_notes_on)
        
        if chord_root_on is not None and upper_triad_root_on is not None:
            if (upper_triad_inversion in self.upper_triad_semitones_shapes):
                print("Good upper triad inversion and quality")
            if (upper_triad_root_on == self.upper_triad_root_num):
                print("Good upper triad root")
            if (Data.note_number_names[self.chord_root] == chord_root_on):
                print("Good chord root absoluto")

            if (Data.note_number_names[self.chord_root] == chord_root_on and 
                    upper_triad_inversion in self.upper_triad_semitones_shapes and 
                    upper_triad_root_on == self.upper_triad_root_num):
                return True
            else:
                return False

    def get_display_string(self):
        """
        Returns a string representing the chord (e.g., 'C' or 'Cm').
        """
        if self.chord_quality == "M":
            return self.chord_root
        return self.chord_root + self.chord_quality

    def get_degree_string(self):
        """
        Returns the chord's scale degree as a string.
        """
        return self.degree