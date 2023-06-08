from insan import insan

class issiz(insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, gecmis_tecrubeler):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__gecmis_tecrubeler = gecmis_tecrubeler

    def statu_bul(self):
        myaka = self.__gecmis_tecrubeler.get("Mavi Yakalı")
        byaka = self.__gecmis_tecrubeler.get("Beyaz Yakalı")
        yonetici = self.__gecmis_tecrubeler.get("Yönetici")

        myaka_etki = myaka * 0.2
        byaka_etki = byaka * 0.35
        yonetici_etki = yonetici * 0.45

        max_etki = max(myaka_etki, byaka_etki, yonetici_etki)

        if max_etki == myaka_etki:
            return "Mavi Yakalı"
        elif max_etki == byaka_etki:
            return "Beyaz Yakalı"
        else:
            return "Yönetici"

    def __str__(self):
        return f"Ad: {self._insan__ad}, Soyad: {self._insan__soyad}, Uygun Statü: {self.statu_bul()}"
