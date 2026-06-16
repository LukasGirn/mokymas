from dataclasses import dataclass

@dataclass
class Kursas:
    pavadinimas : str
    destytojas : str
    trukme : int
    def destyti(self):
        print("Vyksta mokymas!")