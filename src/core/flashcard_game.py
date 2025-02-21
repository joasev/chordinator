import src.core.flashcard_deck as flashcard_deck
import src.ui.render_picker as render_picker

class FlashcardGame:

    def __init__(self, settings) -> None:
        self.deck = flashcard_deck.get_flashcard_deck(settings) #ChordDeck(settings,3)
        self.deck.new_pick()
        self.renderer = render_picker.get_renderer(settings, self.deck.current_flashcard)
        self.renderer.set_display_flashcard(self.deck.current_flashcard)

        self.waiting_for_key_release = False
        ## ESTO NO LO ARREGLO !!!!

    def on_press_key_notes(self, notes_on, skip):
        if skip:
            self.renderer.set_skipped_message()
            self.deck.new_pick()
            
        elif notes_on == set():
            self.waiting_for_key_release == False
            self.renderer.set_display_flashcard(self.deck.current_flashcard)

        elif self.waiting_for_key_release == False:
            success = self.deck.process_attempt_input(notes_on)
            if success:
                self.not_released_yet = True
                self.renderer.set_success_message()
        self.renderer.set_notes_on(notes_on)
    
        #elif len(notes_on) >= 5:
        #    print("Mal!")
        #    text = font1.render("Puto",True, WHITE)
        #    return (should_play,instruction,text)
            


    def render(self, screen):
        self.renderer.render(screen)