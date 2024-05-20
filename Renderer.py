
from SimpleChordRenderer import SimpleChordRenderer
from ProgressionRenderer import ProgressionRenderer

def get_renderer(settings,initial_flashcard):
    if list(settings.mode)[0] == "progressions":
        return ProgressionRenderer(initial_flashcard)
    else:
        return SimpleChordRenderer(initial_flashcard)