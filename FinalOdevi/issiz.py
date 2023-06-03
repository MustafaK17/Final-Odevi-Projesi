from insan import insan

class issiz(insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, gecmis_tecrubeler):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.gecmis_tecrubeler = gecmis_tecrubeler

    def statu_bul(self):
        katsayilar = {"Mavi Yakalı": 0.20, "Beyaz Yakalı": 0.35, "Yönetici": 0.45}
        max_tecrube = max(self.gecmis_tecrubeler.values())
        uygun_statu = max(self.gecmis_tecrubeler, key=lambda x: self.gecmis_tecrubeler[x] * katsayilar[x])
        return uygun_statu

    def __str__(self):
        return f"{super().__str__()}, Uygun Statü: {self.statu_bul()}"
