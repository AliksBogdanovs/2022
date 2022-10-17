class Ballite():
    def __init__(self,dekoracijas, ciemini, ediens, vel_davanas):
        self.dekoracijas = dekoracijas
        self.ciemini = ciemini
        self.ediens = ediens
        self.velDavanas = vel_davanas

    def pirkumi(self):
        print('\nJānopērk sekojošās dekorācijas:')
        for i in self.dekoracijas:
            print(i)
        print('\nJānopērk ekojošos ēdienus:')
        for i in self.ediens:
            print(i)

    def Davanas(self):
        print('\nVajadzīgais dāvanu saraksts:')
        for i in self.velDavanas:
            print(i)

dzD = Ballite(["Baloni","Virtene","Salvetes"],["Anna","Pēteris","Zeltīte","Valters"],["Kartupeļi","Gurķi","Burkāni","Kūka","Sula"],["Grāmata","Krājkase","Termokrūze"])
print(dzD.ediens)
dzD.pirkumi()
dzD.Davanas()
