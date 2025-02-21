import config.constants as constants
import src.utils.pygame_custom_utils as pygame_custom_utils
from src.ui.pianito_renderer import Pianito

class SimpleChordRenderer:
    SIZE = constants.SIZE

    def __init__(self,initial_flashcard) -> None:
        self.set_display_flashcard(initial_flashcard)
        self.pianito = Pianito(SimpleChordRenderer.SIZE)

    def set_notes_on(self,notes_on):
        self.pianito.set_notes_on(notes_on)

    def set_display_flashcard(self,flashcard):
        #self.current_flaschard = flashcard
        if flashcard is not None:
            print("Play this: " + flashcard.chord_root + "" + str(flashcard.chord_quality) + " Upper triad position: " + str(flashcard.upper_triad_position))
            #Esto es de rendereo de flashCard
            (self.instruction,self.text) = pygame_custom_utils.get_instruction_n_chord_to_render(constants.get_font(), constants.WHITE,flashcard)
        else:
            (self.instruction, self.text) = (None, None)
            print("Empty flashcard cannot be displayed")

    def set_success_message(self):
        print("Well done!")
        self.text = constants.get_font().render("Well played!", True, constants.WHITE)

    def set_skipped_message(self):
        print("Skipped!")
        self.text = constants.get_font().render("Skipped!", True, constants.WHITE)

    def render(self,screen):
        screen.fill(constants.BLACK)
        screen.blit(self.instruction, (screen.get_width()/2 - self.instruction.get_rect().width /2, screen.get_height()/2 - 150))
        screen.blit(self.text, (screen.get_width()/2 - self.text.get_rect().width /2, screen.get_height()/2 - 30))

        self.pianito.render(screen)