from math import degrees
import constants
import PygameCustomUtils

class ProgressionRenderer:

    def __init__(self,initial_flashcard) -> None:
        self.set_display_flashcard(initial_flashcard)

    def set_display_flashcard(self,flashcard):
        #self.current_flaschard = flashcard
        if flashcard is not None:
            #print("Play this: "+flashcard.chord_root+""+str(flashcard.chord_quality)+" Upper triad position: "+str(flashcard.upper_triad_position))
            #Esto es de rendereo de flashCard
            self.instruction = constants.font1.render(str(flashcard.get_instruction_string()),True, constants.WHITE)
            
            self.degrees = []
            for index, chFl in enumerate(flashcard.progression_chords):
                if flashcard.fc_index > index:
                    color = constants.RED
                else:
                    color = constants.WHITE
                self.degrees.append(constants.font1.render(str(chFl.get_degree_string()),True, color))
        else:
            (self.instruction,self.text) = (None,None)
            print("Empty flashcard cannot be displayed")

    def set_success_message(self):
        print("Well done!")
        #self.degrees[0] = constants.font1.render("",True, constants.WHITE)
        #self.degrees[1] = constants.font1.render("Well played!",True, constants.WHITE)
        #self.degrees[2] = constants.font1.render("",True, constants.WHITE)

    def set_skipped_message(self):
        print("Skipped!")
        self.text = constants.font1.render("Skipped!",True, constants.WHITE)

    def render(self,screen):
        screen.fill(constants.BLACK)
        screen.blit(self.instruction, (screen.get_width()/2 - self.instruction.get_rect().width /2, screen.get_height()/2 - 150))

        #Funciona solo para 3. Averiguar como hacer compound Surfaces...
        if len(self.degrees) == 1:
            screen.blit(self.degrees[0], (screen.get_width()/2 - self.degrees[0].get_rect().width /2, screen.get_height()/2))
        else:
            screen.blit(self.degrees[0], (screen.get_width()/2 - self.degrees[0].get_rect().width /2 -40, screen.get_height()/2))
            screen.blit(self.degrees[1], (screen.get_width()/2 - self.degrees[1].get_rect().width /2, screen.get_height()/2))
            screen.blit(self.degrees[2], (screen.get_width()/2 - self.degrees[2].get_rect().width /2 +40, screen.get_height()/2))
    