import constants
import Chord
import Data
import pygame

class Pianito:
    key_width = 18
    key_intersp = 2
    key_height = 100
    total_piano_width = (3 + 7 * 7) * (key_width + key_intersp) - key_intersp
    SIZE = [total_piano_width, key_height]

    def __init__(self,screen_size) -> None:
        if screen_size is None:
            screen_size = Pianito.SIZE
        self.piano_keys = self.build_piano_draw_structure(screen_size)

    def build_piano_draw_structure(self,screen_size):
        piano_keys = dict()
        key_w = self.key_width
        key_interspace = self.key_intersp
        key_h = self.key_height
        top_dist = screen_size[1] - key_h
        
        for i in range(21,109):
            #Note.abs_to_rel_note_num(i)
            (solfege_note_num,octave) = Chord.get_solfege_note_num_octave(i)
            print((solfege_note_num,octave))
            whites = Data.piano_key_whites_counter[solfege_note_num] + octave * 7
            left = (key_w + key_interspace) * whites
            if Data.piano_key_color[solfege_note_num] == "WHITE":
                piano_key = {'rect': pygame.Rect(left      ,top_dist,key_w    ,key_h    ),
                            'color':constants.WHITE,
                            'original color': constants.WHITE,
                            'pressed': False}
            else:
                left_black = left + key_w/2 + key_w*(0.2/2) + key_interspace/2
                piano_key = {'rect': pygame.Rect(left_black,top_dist,key_w*0.8,key_h*0.7), 
                            'color':constants.BLACK,
                            'original color': constants.BLACK,
                            'pressed': False,
                            'pressed subrect': {
                                'rect': pygame.Rect(left_black + key_interspace,top_dist,key_w*0.8 - key_interspace*2,key_h*0.7 - key_interspace),
                                'color': constants.RED
                                }
                            }
            piano_keys[i] = piano_key
        return piano_keys
    
    def set_notes_on(self,notes_on):
        for piano_key in self.piano_keys.values():
            piano_key['color'] = piano_key['original color']
            piano_key['pressed'] = False
        for note_on in notes_on:
            if self.piano_keys[note_on]['color'] == constants.WHITE:
                self.piano_keys[note_on]['color'] = constants.RED
            self.piano_keys[note_on]['pressed'] = True

    def render(self,screen):
        for piano_key in self.piano_keys.values():
            if piano_key['original color'] == constants.WHITE:
                pygame.draw.rect(screen, piano_key['color'], piano_key['rect'])
        for piano_key in self.piano_keys.values():
            if piano_key['original color'] == constants.BLACK:
                pygame.draw.rect(screen, piano_key['color'], piano_key['rect'])
                if piano_key['pressed'] == True:
                    pygame.draw.rect(screen,piano_key['pressed subrect']['color'],piano_key['pressed subrect']['rect'])
    