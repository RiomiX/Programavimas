class Kursas():
    def __init__(self, pavadinimas, destytojas, trukme):
        self.pavadinimas = pavadinimas
        self.destytojas = destytojas
        self.trukme = trukme
        print(f'Pavadinimas {pavadinimas} destytojas {destytojas} trukme {trukme}')

    def destyti(self):
        print('Vyksta mokymas')