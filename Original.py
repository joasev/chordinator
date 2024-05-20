
"""
import pygame
import mido
import rtmidi


pygame.init()

BLACK = [  0,   0,   0]
WHITE = [255, 255, 255]
note_list = []
note_list_off = []

outport=mido.open_output()
inport=mido.open_input()

SIZE = [380, 380]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Python MIDI Adaptation")
clock = pygame.time.Clock()
done = False

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    screen.fill(BLACK)
    for msg in inport.iter_pending():
        n = msg.note
        print(n)
        x=(n-47)*10 
        if msg.velocity > 0:
           note_list.append([x, 0])
        else:       
           note_list_off.append([x, 0])           
    for i in range(len(note_list)):
        pygame.draw.circle(screen, WHITE, note_list[i], 10)
        note_list[i][1] += 1
    pygame.display.flip()
    for i in range(len(note_list_off)):
        pygame.draw.circle(screen, BLACK, note_list_off[i], 10)
        note_list_off[i][1] += 1   
    clock.tick(200)

print('awake')
pygame.quit ()

"""


"""
print('Start')
outport=mido.open_output()
inport=mido.open_input()

notes_on = set()

listen = True
should_play = get_random_chord_tuple()
print("Play this ya' idiot: "+should_play[0]+" Inversion: "+should_play[1])
while listen:
    for msg in inport.iter_pending():
        if msg.note == 11:
            listen = False
            break
        if msg.velocity != 0:
            notes_on.add(msg.note)
        else:
            notes_on.remove(msg.note)
        #print(notes_on)
         #print(get_solfege_note_num(msg.note))
         #print(is_chord(notes_on,{3,7,10}))
         #print(get_solfege_note_num_octave(msg.note))
        
        #pressed_chord = get_chord(notes_on)
        #pressed_inversion = get_shape(notes_on)
        #if pressed_chord != None:
        #    print("Chord: " + str(pressed_chord))
        #if pressed_inversion != None:
        #    print("Shape: " + str(pressed_inversion))
        
        pressed_root = get_root(notes_on)
        pressed_inversion = get_shape(notes_on)
        if note_number_names[should_play[0]] == pressed_root and should_play[1] == pressed_inversion:
            print("Well played!")
            should_play = get_random_chord_tuple()
            print("Now play this: "+should_play[0]+" Inversion: "+should_play[1])
    
"""