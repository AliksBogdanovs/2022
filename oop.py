#class - definē klasi 

class Auto():
    def _init_(self,modelis,krasa)
    self.modelis = modelis
    self.krasa = krasa

bmw = Auto(modelis = "X5", krasa = "Sarkana")

print(bmw.modelis)

class Auto():
    def _init_(self,modelis,krasa):
        self.modelis = modelis
        self.krasa = krasa

    def   dati(self):
        print(f"Modelis ir {self.modelis}, krāsa - {self.krasa}")
        
    def krasas_maina(self, jaunaKrasa):
        print(f"iepriekšēja auto krāsa - {self.krasa}")
        print(f"Jaunā auto krāsa - {jaunaKrasa}")

audi = Auto(modelis="Q6",krasa="zila")

audi.dati()
audi.krasas_maina("melna")
