from calisan import calisan

class maviyaka(calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.yipranma_payi = yipranma_payi
        self.statu = sektor


    def get_yipranma_payi(self):
        return self.yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.yipranma_payi = yipranma_payi

    def zam_hakki(self):
        zam_miktari = None
        try:
            tecrube = float(self.tecrube)
            maas = float(self.maas)
            yipranma_payi = float(self.yipranma_payi)
            if tecrube < 24:
                zam_miktari = (maas*(yipranma_payi*10))/100
            elif tecrube >= 24 and tecrube <= 48 and maas < 15000:
                zam_miktari = (maas*((maas%tecrube)/2+(yipranma_payi*10)))/100
            elif tecrube > 48 and maas < 25000:
                zam_miktari = maas*(((maas%tecrube)/3+(yipranma_payi*10)))/100
            return zam_miktari
        except ValueError:
            print("Hatalı değerler!")
            return zam_miktari

    def __str__(self):
        zam_miktari = self.zam_hakki()
        if zam_miktari is not None:
            zamli_maas = int(self.maas + zam_miktari)
            return f"Kimlik No: {self.tc_no}, Ad: {self.ad}, Soyad: {self.soyad}, Yaş: {self.yas}, Cinsiyet: {self.cinsiyet}, Uyruk: {self.uyruk}, Statü: {self.statu}, Tecrübe: {self.tecrube} ay, Maaş: {self.maas} > {zamli_maas}, Yıpranma Payı: {self.yipranma_payi}"
        else:
            return f"Kimlik No: {self.tc_no}, Ad: {self.ad}, Soyad: {self.soyad}, Yaş: {self.yas}, Cinsiyet: {self.cinsiyet}, Uyruk: {self.uyruk}, Statü: {self.statu}, Tecrübe: {self.tecrube} ay, Maaş: {self.maas} > Hatalı değerler!, Yıpranma Payı: {self.yipranma_payi}"
