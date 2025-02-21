import src.utils.data as Data
import src.utils.chord_logic as chord_logic

class Note:

    def __init__(self, note_in_text) -> None:
        self.note_in_text = note_in_text

    def increase_by(self, interval):
        starting_degree = Data.degree_notes[self.note_in_text[0]]
        new_degree = (starting_degree + int(interval[0]) - 1) % 7

        new_note_num = chord_logic.increase_solfege_note_by_semitones(Data.note_number_names[self.note_in_text], Data.intervals[interval])
        difference = new_note_num - Data.note_number_names[Data.degree_notes_reverse[new_degree]]
        #Becuadros!!!! 
        alteraciones = {0:"", 1:"#", 2:"##", -1:"b", -2:"bb", 11:"b", 10:"bb"}
        alteracion = alteraciones[difference]

        return Data.degree_notes_reverse[new_degree]+alteracion

        #con intervalo sabes tecla. Y ya sabes que NAME. Despues es cuestion de bemolear para llegar.
        
"""
note = Note("C")
print(note.increase_by("1U"))
note = Note("C")
print(note.increase_by("2m"))
note = Note("C")
print(note.increase_by("2M"))
note = Note("C")
print(note.increase_by("3m"))
note = Note("C")
print(note.increase_by("3M"))
note = Note("C")
print(note.increase_by("4d"))
note = Note("C")
print(note.increase_by("4P"))
note = Note("C")
print(note.increase_by("4a"))
note = Note("C")
print(note.increase_by("5d"))
note = Note("C")
print(note.increase_by("5P"))
note = Note("C")
print(note.increase_by("5a"))
note = Note("C")
print(note.increase_by("6m"))
note = Note("C")
print(note.increase_by("6M"))
note = Note("C")
print(note.increase_by("7m"))
note = Note("C")
print(note.increase_by("7M"))
"""