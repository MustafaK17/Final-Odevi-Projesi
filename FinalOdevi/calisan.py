from insan import insan

class calisan(insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas
        self.__yeni_maas = None

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas


    def zam_hakki(self):
        zam_miktari = None
        try:
            tecrube = float(self.__tecrube)
            maas = float(self.__maas)
            if tecrube < 24:
                zam_miktari = 0
                self.__yeni_maas = self.__maas
                return self.__yeni_maas
            elif tecrube >= 24 and tecrube <= 48 and maas < 15000:
                zam_miktari = (maas * (maas%tecrube)/100.0)
                self.__yeni_maas = (self.__maas + zam_miktari)
                return self.__yeni_maas
            elif tecrube > 48 and maas < 25000:
                zam_miktari = (maas * ((maas%tecrube)/2.0)/100.0)
                self.__yeni_maas = (self.__maas + zam_miktari)
                return self.__yeni_maas
        except ValueError:
            print("Hatalı değerler!")
            return zam_miktari

    def __str__(self):
        return f"Ad: {self._insan__ad}, Soyad: {self._insan__soyad}, Tecrübe: {self.__tecrube} ay, Maaş: {self.__yeni_maas}"