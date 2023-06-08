from calisan import calisan

class maviyaka(calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi
        self.__statu = sektor


    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        try:
            tecrube = float(self._calisan__tecrube)
            maas = float(self._calisan__maas)
            yipranma_payi = float(self.__yipranma_payi)
            if tecrube < 24:
                zam_miktari = (maas*(yipranma_payi*10))/100
                self.__yeni_maas = (self._calisan__maas + zam_miktari)
                return self.__yeni_maas
            elif tecrube >= 24 and tecrube <= 48 and maas < 15000:
                zam_miktari = (maas*((maas%tecrube)/2+(yipranma_payi*10)))/100
                self.__yeni_maas = (self._calisan__maas + zam_miktari)
                return self.__yeni_maas
            elif tecrube > 48 and maas < 25000:
                zam_miktari = maas*(((maas%tecrube)/3+(yipranma_payi*10)))/100
                self.__yeni_maas = (self._calisan__maas + zam_miktari)
                return self.__yeni_maas
        except ValueError:
            print("Hatalı değerler!")
            return None

    def __str__(self):
        return f"Ad: {self._insan__ad}, Soyad: {self._insan__soyad}, Tecrübe: {self._calisan__tecrube} ay, Maaş: {self.__yeni_maas}"
