from insan import insan

class calisan(insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.sektor = sektor
        self.tecrube = tecrube
        self.maas = maas

    def get_sektor(self):
        return self.sektor

    def set_sektor(self, sektor):
        self.sektor = sektor

    def get_tecrube(self):
        return self.tecrube

    def set_tecrube(self, tecrube):
        self.tecrube = tecrube

    def get_maas(self):
        return self.maas

    def set_maas(self, maas):
        self.maas = maas


    def zam_hakki(self):
        zam_miktari = None
        try:
            tecrube = float(self.tecrube)
            maas = float(self.maas)
            if tecrube < 24:
                zam_miktari = 0
            elif tecrube >= 24 and tecrube <= 48 and maas < 15000:
                zam_miktari = (maas * (maas%tecrube)/100.0)
            elif tecrube > 48 and maas < 25000:
                zam_miktari = (maas * ((maas%tecrube)/2.0)/100.0)
            return zam_miktari
        except ValueError:
            print("Hatalı değerler!")
            return zam_miktari

    def __str__(self):
        zam_miktari = self.zam_hakki()
        if zam_miktari is not None:
            zamli_maas = int(self.maas + zam_miktari)
            return f"Kimlik No: {self.tc_no}, Ad: {self.ad}, Soyad: {self.soyad}, Yaş: {self.yas}, Cinsiyet: {self.cinsiyet}, Uyruk: {self.uyruk}, Sektor: {self.sektor}, Tecrübe: {self.tecrube} ay, Maaş: {self.maas} > {zamli_maas}"
        else:
            return f"Kimlik No: {self.tc_no}, Ad: {self.ad}, Soyad: {self.soyad}, Yaş: {self.yas}, Cinsiyet: {self.cinsiyet}, Uyruk: {self.uyruk}, Sektor: {self.sektor}, Tecrübe: {self.tecrube} ay, Maaş: {self.maas} > Hatalı değerler!"