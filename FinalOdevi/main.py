from insan import insan
from issiz import issiz
from calisan import calisan
from maviyaka import maviyaka
from beyazyaka import beyazyaka
import pandas as pd

#insan
insan1 = insan("11223344556", "Kerem", "Yılmaz", 30, "Erkek", "Türk"); print(insan1)
insan2 = insan("12312312345", "Selin", "Kaya", 27, "Kadın", "Türk"); print(insan2)


#issiz
gecmis_tecrubeler_1 = {"Mavi Yakalı": 4, "Beyaz Yakalı": 7, "Yönetici": 2}
issiz_1 = issiz("12121314156", "Ali", "Demir", 34, "Erkek", "Türk", gecmis_tecrubeler_1)

gecmis_tecrubeler_2 = {"Mavi Yakalı": 6, "Beyaz Yakalı": 3, "Yönetici": 1}
issiz_2 = issiz("98765432109", "Ayşe", "Güler", 32, "Kadın", "Türk", gecmis_tecrubeler_2)

gecmis_tecrubeler_3 = {"Mavi Yakalı": 2, "Beyaz Yakalı": 3, "Yönetici": 5}
issiz_3 = issiz("45678912310", "Osman", "Çelik", 35, "Erkek", "Türk", gecmis_tecrubeler_3)

issizler = [issiz_1, issiz_2, issiz_3]

for issiz in issizler:
    print(f"{issiz}")

#çalışan
calisan1 = calisan("16154181231", "Can", "Öztürk", 27, "Kadın", "Türk", "Teknoloji", 22, 18000); calisan1.zam_hakki();print(calisan1)
calisan2 = calisan("98723622108", "Kemal", "Akgün", 32, "Erkek", "Türk", "Muhasebe", 38, 14880);  calisan2.zam_hakki();print(calisan2)
calisan3 = calisan("45820161234", "Nazlı", "Yıldırım", 35, "Kadın", "Türk", "İnşaat", 68, 23450); calisan3.zam_hakki();print(calisan3)


#maviyaka
maviyaka1 = maviyaka("17481275232", "Emir", "Şahin", 35, "Erkek", "Mavi Yakalı", "Türk", 36, 14500, 0.2);   maviyaka1.zam_hakki();print(maviyaka1)
maviyaka2 = maviyaka("67418928364", "Cemile", "Lale", 28, "Kadın", "Mavi Yakalı", "Türk", 21, 12000, 0.5);  maviyaka2.zam_hakki();print(maviyaka2)
maviyaka3 = maviyaka("12748192012", "Servet", "Sayar", 42, "Erkek", "Mavi Yakalı", "Türk", 51, 18000, 0.3); maviyaka3.zam_hakki();print(maviyaka3)


#beyazyaka
beyazyaka1 = beyazyaka("15648520522", "Elif", "Kılıç", 33, "Kadın", "Beyaz Yakalı", "Türk", 21, 12200, 2500);  beyazyaka1.zam_hakki(); print(beyazyaka1)
beyazyaka2 = beyazyaka("56176379112", "Mert", "Demir", 39, "Erkek", "Beyaz Yakalı", "Türk", 35, 14700, 500);   beyazyaka2.zam_hakki(); print(beyazyaka2)
beyazyaka3 = beyazyaka("61426731232", "Emine", "Aksoy", 26, "Kadın", "Beyaz Yakalı", "Türk", 61, 22320, 3000); beyazyaka3.zam_hakki(); print(beyazyaka3)


# Çalışan Nesnelerini DataFrame'e Dönüştürme
calisan_data = []
for calisan_obj in [calisan1, calisan2, calisan3]:
    calisan_row = [
        "Çalışan",
        calisan_obj._insan__tc_no,
        calisan_obj._insan__ad,
        calisan_obj._insan__soyad,
        calisan_obj._insan__yas,
        calisan_obj._insan__cinsiyet,
        calisan_obj._insan__uyruk,
        calisan_obj.get_sektor(),
        '{:.1f}'.format(float(calisan_obj.get_tecrube() / 12)),  # Tecrübeyi yıla çevirme
        calisan_obj.get_maas(),
        0,  # Yıpranma Payı (Çalışan için 0)
        0,  # Teşvik Prim (Çalışan için 0)
        calisan_obj.zam_hakki()
    ]
    calisan_data.append(calisan_row)

# Mavi Yaka Nesnelerini DataFrame'e Dönüştürme
maviyaka_data = []
for maviyaka_obj in [maviyaka1, maviyaka2, maviyaka3]:
    maviyaka_row = [
        "Mavi Yaka",
        maviyaka_obj._insan__tc_no,
        maviyaka_obj._insan__ad,
        maviyaka_obj._insan__soyad,
        maviyaka_obj._insan__yas,
        maviyaka_obj._insan__cinsiyet,
        maviyaka_obj.get_sektor(),
        maviyaka_obj._insan__uyruk,
        '{:.1f}'.format(float(maviyaka_obj.get_tecrube() / 12)),  # Tecrübeyi yıla çevirme
        maviyaka_obj.get_maas(),
        maviyaka_obj.get_yipranma_payi(),
        0,  # Teşvik Prim (Mavi Yaka için 0)
        maviyaka_obj.zam_hakki()
    ]
    maviyaka_data.append(maviyaka_row)

# Beyaz Yaka Nesnelerini DataFrame'e Dönüştürme
beyazyaka_data = []
for beyazyaka_obj in [beyazyaka1, beyazyaka2, beyazyaka3]:
    beyazyaka_row = [
        "Beyaz Yaka",
        beyazyaka_obj._insan__tc_no,
        beyazyaka_obj._insan__ad,
        beyazyaka_obj._insan__soyad,
        beyazyaka_obj._insan__yas,
        beyazyaka_obj._insan__cinsiyet,
        beyazyaka_obj.get_sektor(),
        beyazyaka_obj._insan__uyruk,
        '{:.1f}'.format(float(beyazyaka_obj.get_tecrube() / 12)),  # Tecrübeyi yıla çevirme
        beyazyaka_obj.get_maas(),
        0,  # Yıpranma Payı (Beyaz Yaka için 0)
        beyazyaka_obj.get_tesvik_primi(),
        beyazyaka_obj.zam_hakki()
    ]
    beyazyaka_data.append(beyazyaka_row)

# DataFrame Oluşturma
df = pd.DataFrame(calisan_data + maviyaka_data + beyazyaka_data,
                  columns=["Statü", "TC no", "Ad", "Soyad", "Yaş", "Cinsiyet", "Uyruk", "Sektör", "Tecrübe(yıl)", "Maaş", "Yıpranma Payı", "Teşvik Primi", "Yeni Maaş"])
# Boş değerleri 0 atama
df.fillna(0, inplace=True)
print(df.to_string())



# DataFrame'i Excel'e Dönüştürme
#df.to_excel('proje.xlsx', index=False)

