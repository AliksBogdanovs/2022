class Transportlidzeklis():
    def __init__(self,modelis,krasa,motoraTilpums,atrumkarba):
        self.modelis = modelis
        self.krasa = krasa
        self.motoraTilpums = motoraTilpums
        self.atrumkarba = atrumkarba

    def dati():
        print(f"Modelis: {self.modelis}")
        print(f"Krasa: {self.krasa}")
        print(f"Motora tilpums: {self.motoraTilpums}")
        primt(f"Atrumkarba: {self.atrumkarba}")

auto = Transportlidzeklis("Outlander","melna","10","Manuālā")
auto.dati()

