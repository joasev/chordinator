from PianitoRenderer import Pianito

class SoloPianito:

    def __init__(self) -> None:
        self.renderer = Pianito(None)


    def on_press_key_notes(self,notes_on,skip):
        self.renderer.set_notes_on(notes_on)

    
    def render(self,screen):
        self.renderer.render(screen)

