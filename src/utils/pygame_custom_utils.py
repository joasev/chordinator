
def get_chord_to_render(font1,color,chord_flashcard):
    chord_quality = str(chord_flashcard.chord_quality)
    if chord_quality == "M":
        chord_quality=""
    return font1.render(str(chord_flashcard.chord_root+chord_quality),True, color)

def get_instruction_to_render(font1,color,chord_flashcard):
    return font1.render(str(chord_flashcard.upper_triad_position),True, color)
#Wow, no se como RECONOCIA font1 si esta definido despues...

def get_instruction_n_chord_to_render(font1,color,chord_flashcard):
    return (get_instruction_to_render(font1,color,chord_flashcard),get_chord_to_render(font1,color,chord_flashcard))

