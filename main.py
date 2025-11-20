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
        return (f"Značka: {self.znacka}/nRok: {self.rok}/nModel: {self.model}/n"
                f"CPU: {self.cpu}/nRam: {self.ram}/nCena: {self.cena} Kč/n"
                f"Cena bez DPH: {self.cena_bez_dph()}/n")

class notebook(pocitac):
    def __init__(self, znacka, rok, model, cpu, ram, cena, baterie, gpu):
        super().__init__(znacka, rok, model, cpu, ram, cena, baterie)
        self.gpu = gpu

    def vypis(self):
        return super().vypis()
    
    def cena_bez_dph(self):
        return f" {self.cena * 0.79} kč"

class herninotebook(notebook):
    def __init__(self, znacka, rok, model, cpu, ram, cena, baterie, gpu):
        super().__init__(znacka, rok, model, cpu, ram, cena, baterie)
        self.gpu = gpu

    def vypis(self):
        return super().vypis() + f"Typ:herni - GPU: {self.gpu}/n"


seznam_pc = {
    pocitac("HP", 2022, "ProDesk", "Intel i5", 16, 15000),
    notebook("Dell", 2021, "Inspiron", "Intel i7", 16, 22000, 8),
    herninotebook("Asus", 2022,"ROG", "Ryzen 7", 32, 42000, 5, "RTX 4060"),
    pocitac("AlzaPc", 2023,"AlzaPc", "intel i7", 32, 15000),
    notebook("Dell", 2022,"Inspiron")
}