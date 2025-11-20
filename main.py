class pocitac:
    """
    Třída, která slouží k dědičnosti pro zaměstnance a žáky
    """
    def __init__(self, znacka: str, rok: int, model: str, cpu: str, ram: int, cena: float):
        self.znacka = str(znacka)
        self.rok = int(rok)
        self.model= str(model)
        self.cpu = str(cpu)
        self.ram = int(ram)
        self.cena = float(cena)

    def cena_bez_dph(self):
        return f" {self.cena * 0.79} kč"

    def vypis(self):
        return (f"Značka: {self.znacka}/nRok: {self.rok}/nModel: {self.model}/n")
                f"CPU: {self.cpu}/nRam: {self.ram}/nCena: {self.cena} Kč/n"
                f"Cena bez DPH: {self.cena_bez_dph()}/n")