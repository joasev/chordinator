import json

class Settings:
    ##NO ESTOY MUY SEGURO COMO ESTA ESTO FUNCIONANDO... LAS ESTOY MODIFICANDO SON SELF.
       ##QUIZA CUANDO PONGO SELF. LAS ESTOY DEFINIENDO PARA LA CLASE/INSTANCIA??
    qualities = set()
    upper_triad_positions = set()
    roots = set()

    def extract_positives(self,settings_sub_dict):
        positives_set = set()
        for k,v in settings_sub_dict.items():
            if v == 1:
                positives_set.add(k)
        return positives_set

    def load_settings(self):
        #global qualities ## No se si esto es good practice jeje.
        #global upper_triad_inversions
        #global roots
        with open('settings.txt') as f:
            data = f.read()
            settings_dictionary = json.loads(data)
            self.mode = self.extract_positives(settings_dictionary["mode"])
            self.qualities = self.extract_positives(settings_dictionary["quality"])
            self.upper_triad_positions = self.extract_positives(settings_dictionary["upper_triad_inversion"])
            if (settings_dictionary["mode"]["progressive"] == 1):
                self.roots = settings_dictionary["root"].keys()
            else:
                self.roots = self.extract_positives(settings_dictionary["root"])
            self.progressions = self.extract_positives(settings_dictionary["progressions"])
            print(self.mode)
            print(self.qualities)
            print(self.upper_triad_positions)
            print(self.roots)
            print(self.progressions)
    
## CON ESTOS SETTINGS FILTRAR LAS FLASHCARDS Y HACER UN MAZO. ASI LA LOGICA DE
## FLASHCARDS ES INDEPENDIENTE DE QUE SEA MUSICAL.