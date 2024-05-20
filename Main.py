"""
Python MIDI input
Dec, 2021
"""
import pygame
import mido
from pygame.constants import KEYDOWN, RESIZABLE
import rtmidi
from pynput import keyboard

pygame.init()


#from Data import upper_shapes, chords, roots
from Settings import Settings
import PhysicalPiano
import constants
from FlashcardGame import FlashcardGame
from SoloPianito import SoloPianito



inport = PhysicalPiano.try_opening_ports()

def get_piano_status_caption(inport):
    if inport is None:
        #print('Piano no conectado durante inicializacion')
        return "Joaco's Chord Game - Keyboard Not Connected"
    else:
        return "Joaco's Chord Game - Keyboard Connected"



#Console menu
#print("Welcome to the Chord game. Yes. So fun.")
#print("Choose option. Make sure the Settings.txt file has your preferences set.")
#print("1. Chord game")
#print("2. Progressions")
#print("3. Improvising") 
#                       (El random/setting es la tonalidad... quiza que module si son varios)  
#                       (Te tira los grados y tenes que tocar ese grado y pentatonic siempre pero grados 
#                       sensibles que resuelvan. Alguna forma de indicar un countdown de tiempo para
#                       tocar notas que hace rato no tocas. Como un countdown?)
#print("4. Progressions by ear")
#                       Gives key. (You play root or play for a little while all ok)
#                       Gives sound of next chord or next armonic circle and then you need to play it

#Hecho:
#   Ir agregando de a poco del maso. Cuando apreto "N". Y la probabilidad de que salga sea inversamente prop
#   al count de las veces que salio la tarjeta.

#Next:
#   Investigar como son los metodos estaticos para jusntar pygame custom utils y ChordGame
#   Lograr que haya otro game (progressions)

#Mejoras:
#   Time statistics
#   Jueguito move to left
#   miMa lio por el acorde aumentado simetrico no puedo hayar root. Pero dejarlo para cuando Ppb lo necesite...

    ## IDEA !!! RECORD TIME STATISTICS Y LAS QUE TENGAN MAYOR AVERAGE QUE SALGAN CON MAS PROBABILIDAD!!!!
    ## guardar cuanto te llevo cada press y con las funciones de data de python mostrar grafica de time statistics.

settings = Settings()
settings.load_settings()

game = SoloPianito() 
#game = FlashcardGame(settings)

notes_on = set()
note_list = []
note_list_off = []

#pygame.init()
screen = pygame.display.set_mode(game.renderer.SIZE) #constants.SIZE
pygame.display.set_caption(get_piano_status_caption(inport))
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

    game.render(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                settings.load_settings()
                #game.chord_deck = ChordDeck(settings)
            if event.key == pygame.K_k or event.key == pygame.K_l:
                game.on_press_key_notes(set(),True)
            if event.key == pygame.K_1:
                game.deck.increase_pullable_pool()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_k or event.key == pygame.K_l:
                game.on_press_key_notes(set(),False)
        
        if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
            process_keyboard_events(event)
            print(notes_on)
            game.on_press_key_notes(notes_on,False)

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
            game.on_press_key_notes(notes_on,False)



    else:
        inport = PhysicalPiano.try_opening_ports()
        pygame.display.set_caption(get_piano_status_caption(inport))

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
