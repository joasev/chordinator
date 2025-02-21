import mido

def open_ports():
    try:
        #outport=mido.open_output()
        puerto_abierto = mido.open_input()
        print("Piano conectado")
        return puerto_abierto
    except:
        #piano_conectado=False
        #print('Piano no conectado')
        return None