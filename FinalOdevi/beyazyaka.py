from calisan import calisan

class beyazyaka(calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.tesvik_primi = tesvik_primi

    def zam_hakki(self):
        zam_miktari = None
        try:
            tecrube = float(self.tecrube)
            maas = float(self.maas)
            tesvik_primi = float(self.tesvik_primi)
            if tecrube < 24:
                zam_miktari = tesvik_primi
            elif tecrube >= 24 and tecrube <= 48 and maas < 15000:
                zam_miktari = (maas % tecrube)*5 + tesvik_primi
            elif tecrube > 48 and maas < 25000:
                zam_miktari = (maas % tecrube)*4 + tesvik_primi
            return zam_miktari
        except ValueError:
            print("Hatalı değerler!")
            return zam_miktari

    def __str__(self):
        zam_miktari = self.zam_hakki()
        if zam_miktari is not None:
            yeni_maas = int(self.maas + zam_miktari)
            return f"Ad: {self.ad}, Soyad: {self.soyad}, Tecrübe: {self.tecrube} ay,  Maaş: {yeni_maas}"
        else:
            return f"Ad: {self.ad}, Soyad: {self.soyad}, Tecrübe: {self.tecrube} ay,  Maaş: {self.maas}"