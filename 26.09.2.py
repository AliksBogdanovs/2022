import datetime
import csv
from re import S

class Rekins():
    def __init__(self, izmers, veltijums, klients, materials):
        self.klients = izmers
        self.veltijums = veltijums
        self.izmers = klients.split(',')
        self.materials = float(materials)
        self.laiks = datetime.datetime.now()
        
        self.aprekins()
    
    def aprekins(self):
        darba_samaksa = 15
        PVN = 21
        produkta_cena = len(self.veltijums)*1.2+(int(self.izmers[0])/100*int(self.izmers[1])/100*int(self.izmers[2])/100)/3*self.materials
        PVN_summa = (produkta_cena+darba_samaksa)*PVN/100
        rekina_summa = (produkta_cena+darba_samaksa)+PVN_summa
        return rekina_summa

    def izdrukat(self):
        print(f'Izmers: {self.izmers}')
        print(f'Veltijums: {self.veltijums}')
        print(f'Klients: {self.klients}')
        print(f'Materials: {self.materials}')
        print(f'Laiks: {self.laiks}')
        print(f'Rekina Summa: {self.aprekins()}')

    def saglabat(self):
        with open('rekini.csv', 'a',encoding="utf-8",newline='') as fails:
            csvwrite = csv.writer(fails)
            csvwrite.writerow(['klienta vārds','veltījums','izmēri','materiāla cena','laiks','cena)
            csvwrite.writerow([self.klients,self.veltijums,self.izmers,self.materials,self.laiks,self.aprekins()])



