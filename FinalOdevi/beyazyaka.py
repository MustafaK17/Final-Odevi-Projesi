from calisan import calisan

class beyazyaka(calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi
        self.__statu = sektor

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def zam_hakki(self):
        try:
            tecrube = float(self._calisan__tecrube)
            maas = float(self._calisan__maas)
            tesvik_primi = float(self.__tesvik_primi)
            if tecrube < 24:
                zam_miktari = tesvik_primi
                self.__yeni_maas = (self._calisan__maas + tesvik_primi)
                return self.__yeni_maas
            elif tecrube >= 24 and tecrube <= 48 and maas < 15000:
                zam_miktari = (maas % tecrube) * 5 + tesvik_primi
                self.__yeni_maas = (self._calisan__maas + tesvik_primi)
                return self.__yeni_maas
            elif tecrube > 48 and maas < 25000:
                zam_miktari = (maas % tecrube) * 4 + tesvik_primi
            self.__yeni_maas = int(self._calisan__maas + zam_miktari)
            return self.__yeni_maas
        except ValueError:
            print("Hatalı değerler!")
            return None

    def __str__(self):
        return f"Ad: {self._insan__ad}, Soyad: {self._insan__soyad}, Tecrübe: {self._calisan__tecrube} ay, Maaş: {self.__yeni_maas}"