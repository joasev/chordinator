import Data
import Chord

class ChordFlashcard:
    
    def __init__(self,chord_root,chord_quality,upper_triad_position,degree=None):
        #Direct settings dependent
        self.chord_root = chord_root
        self.chord_quality = chord_quality
        self.upper_triad_position = upper_triad_position #inversion
        self.degree = degree
        #Derived
        self.chord_root_num = Data.note_number_names[self.chord_root]
        self.upper_triad_root_num = Chord.increase_solfege_note_by_semitones(self.chord_root_num, Data.upper_triad_root_by_quality[self.chord_quality])
        self.upper_triad_quality = Data.upper_triad_quality_by_quality[self.chord_quality]
        self.upper_triad_semitones_shapes = []
        if upper_triad_position is not None:
            self.upper_triad_semitones_shapes.append(Data.upper_shapes[(self.upper_triad_position,self.upper_triad_quality)])
        else:
            # Aca tiene que seleccionar todas las posibilidades de upper shapes
            for k,v in Data.upper_shapes.items():
                if k[1] == self.upper_triad_quality:
                    self.upper_triad_semitones_shapes.append(v)
        #other
        self.count=0
    """
    def decrease_show_weight(self):
        if self.show_weight > 0:
            self.show_weight = self.show_weight - 1
            """
    def increase_show_weight(self):
        self.count = self.count + 1

    def detect_right_hand_notes(self,notes_on):
        right_hand_notes_on = set()
        if len(notes_on) >= 3: # and should_play[1][1] == "m7"
            notes_on_temp = notes_on.copy()
            for i in range (3):
                max_aux = max(notes_on_temp)
                notes_on_temp.remove(max_aux)
                right_hand_notes_on.add(max_aux)
            return right_hand_notes_on
        else:
            return notes_on

    def detect_root(self,notes_on):
        #para poder identificar acordes de >4, tenemos que empezar a hablar de chord_root y upper_triad_root
        if len(notes_on) >= 4:
            print(notes_on)
            print(min(notes_on))
            return Chord.get_solfege_note_num(min(notes_on)) ## Mejorar, si haces una right hand sola de acorde con 7 invertido da mal.
        else:
            return Chord.get_root(notes_on) 
        
    def is_played_chord(self,notes_on):
        right_hand_notes_on = self.detect_right_hand_notes(notes_on)
        chord_root_on = self.detect_root(notes_on)
        upper_triad_root_on = Chord.get_root(right_hand_notes_on)
        upper_triad_inversion = Chord.get_shape(right_hand_notes_on)
        #(Y la logica del pressed root es la nota mas grave si mas de 4 teclas, si no, analiza la triada superior, si hay menos de 3 no se pero funca)

    # AHORA QUE ME PONGO A PENSAR.. LO DE LAS 3 NOTAS DE ARRIBA TAMBIEN ES LOGICA VALIDA PARA TRIADAS NORMALES...
        if chord_root_on is not None and upper_triad_root_on is not None:
            if (upper_triad_inversion in self.upper_triad_semitones_shapes):
                print("Buen upper triad inversion and quality")
            if (upper_triad_root_on == self.upper_triad_root_num):
                print("buen upper triad root")
            if (Data.note_number_names[self.chord_root] == chord_root_on):
                print("buen chord root absoluto")

            if (Data.note_number_names[self.chord_root] == chord_root_on and 
                    upper_triad_inversion in self.upper_triad_semitones_shapes and 
                    upper_triad_root_on == self.upper_triad_root_num):
                return True
            else:
                return False

    def get_display_string(self):
        if self.chord_quality == "M":
            return self.chord_root
        return self.chord_root + self.chord_quality

    def get_degree_string(self):
        return self.degree