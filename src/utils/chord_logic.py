import src.utils.data as Data


def get_solfege_note_num(note_absolute_num):
    return (note_absolute_num - 21) % 12

def get_solfege_note_num_octave(note_absolute_num):
    solfege_note_num = get_solfege_note_num(note_absolute_num)
    octave = ((note_absolute_num - 21) // 12) # +1
    return (solfege_note_num,octave)

def increase_solfege_note_by_semitones(note_num,semitones):
    return (note_num+semitones) % 12

def get_chord(pressed_notes):
    pressed_notes_solf = set()
    for item in pressed_notes:
        pressed_notes_solf.add(get_solfege_note_num(item))
    for k,v in Data.chords.items():
        if pressed_notes_solf == v:
            return k

def get_root(pressed_notes):
    pressed_notes_solf = set()
    for item in pressed_notes:
        pressed_notes_solf.add(get_solfege_note_num(item))
    for k,v in Data.roots.items():
        if pressed_notes_solf == set(k):
            return v

def get_shape(pressed_notes):
    if len(pressed_notes) < 3:
        return
    sorted_notes_list = sorted(pressed_notes)
    for k,v in Data.upper_shapes.items():
        if sorted_notes_list[1]==sorted_notes_list[0]+v[0] and sorted_notes_list[2]==sorted_notes_list[0]+v[1]:
            return v

def is_chord(pressed_set, chord_set):
    solfege_set = set()
    for abs_num in pressed_set:
        solfege_set.add(get_solfege_note_num(abs_num))
    return solfege_set == chord_set


