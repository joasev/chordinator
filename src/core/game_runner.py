import pygame
import src.input.physical_piano as physical_piano
import config.constants as constants 




class GameRunner:
    def __init__(self, game_type):
        self.game_type = game_type

    def get_piano_status_caption(inport):
        if inport is None:
            return "Chordinator - Keyboard Not Connected"
        else:
            return "Chordinator - Keyboard Connected"

    def run(self):
        inport = physical_piano.open_ports()
        
        notes_on = set()
        note_list = []
        note_list_off = []

        screen = pygame.display.set_mode(self.game_type.renderer.SIZE) #constants.SIZE
        pygame.display.set_caption(GameRunner.get_piano_status_caption(inport))
        clock = pygame.time.Clock()

        def process_key_on(event,note_num):
            if event.type == pygame.KEYDOWN:
                notes_on.add(note_num)
            elif event.type == pygame.KEYUP:
                notes_on.remove(note_num)

        def process_keyboard_events(event):
            if event.key == pygame.K_z:
                process_key_on(event,36)
            if event.key == pygame.K_s:
                process_key_on(event,37)
            if event.key == pygame.K_x:
                process_key_on(event,38)
            if event.key == pygame.K_d:
                process_key_on(event,39)
            if event.key == pygame.K_c:
                process_key_on(event,40)
            if event.key == pygame.K_v:
                process_key_on(event,41)
            if event.key == pygame.K_g:
                process_key_on(event,42)
            if event.key == pygame.K_b:
                process_key_on(event,43)
            if event.key == pygame.K_h:
                process_key_on(event,44)
            if event.key == pygame.K_n:
                process_key_on(event,45)
            if event.key == pygame.K_j:
                process_key_on(event,46)
            if event.key == pygame.K_m:
                process_key_on(event,47)
            
            if event.key == pygame.K_q:
                process_key_on(event,60)
            if event.key == pygame.K_2:
                process_key_on(event,61)
            if event.key == pygame.K_w:
                process_key_on(event,62)
            if event.key == pygame.K_3:
                process_key_on(event,63)
            if event.key == pygame.K_e:
                process_key_on(event,64)
            if event.key == pygame.K_r:
                process_key_on(event,65)
            if event.key == pygame.K_5:
                process_key_on(event,66)
            if event.key == pygame.K_t:
                process_key_on(event,67)
            if event.key == pygame.K_6:
                process_key_on(event,68)
            if event.key == pygame.K_y:
                process_key_on(event,69)
            if event.key == pygame.K_7:
                process_key_on(event,70)
            if event.key == pygame.K_u:
                process_key_on(event,71)
            if event.key == pygame.K_i:
                process_key_on(event,72)
            if event.key == pygame.K_9:
                process_key_on(event,73)
            if event.key == pygame.K_o:
                process_key_on(event,74)
            if event.key == pygame.K_0:
                process_key_on(event,75)
            if event.key == pygame.K_p:
                process_key_on(event,76)


        done = False
        while done == False:

            self.game_type.render(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        self.settings.load_settings()
                        #game.chord_deck = ChordDeck(settings)
                    if event.key == pygame.K_k or event.key == pygame.K_l:
                        self.game_type.on_press_key_notes(set(), True)
                    if event.key == pygame.K_1:
                        self.game_type.deck.increase_pullable_pool()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_k or event.key == pygame.K_l:
                        self.game_type.on_press_key_notes(set(), False)
                
                if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                    process_keyboard_events(event)
                    print(notes_on)
                    self.game_type.on_press_key_notes(notes_on, False)

            if inport is not None:
                for msg in inport.iter_pending():
                    try:
                        if msg.velocity != 0:
                            notes_on.add(msg.note)
                        else:
                            notes_on.remove(msg.note)

                        #funcionalidad del chino
                        n = msg.note
                        x=(n-47)*10 
                        if msg.velocity > 0:
                            note_list.append([x, 0])
                        else:       
                            note_list_off.append([x, 0])
                    except:
                        pass
                    print(notes_on)
                    self.game_type.on_press_key_notes(notes_on,False)

            else:
                inport = physical_piano.open_ports()
                pygame.display.set_caption(GameRunner.get_piano_status_caption(inport))

            for i in range(len(note_list)):
                pygame.draw.circle(screen, constants.WHITE, note_list[i], 10)
                note_list[i][1] += 1
            pygame.display.flip()
            for i in range(len(note_list_off)):
                pygame.draw.circle(screen, constants.BLACK, note_list_off[i], 10)
                note_list_off[i][1] += 1   
            clock.tick(200)



        print('Program finished')
        pygame.quit ()