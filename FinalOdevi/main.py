from insan import insan
from issiz import issiz
from calisan import calisan
from maviyaka import maviyaka
#from beyazyaka import beyazyaka
#import pandas as pd

#insan
insan1 = insan("11223344556", "Kerem", "Yılmaz", 30, "Erkek", "Türk")
insan2 = insan("12312312345", "Selin", "Kaya", 27, "Kadın", "Türk")

print(insan1)
print(insan2)

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
calisan1 = calisan("16154181231", "Can", "Öztürk", 27, "Kadın", "Türk", "Teknoloji", 22, 18000)
calisan2 = calisan("98723622108", "Kemal", "Akgün", 32, "Erkek", "Türk", "Muhasebe", 38, 14880)
calisan3 = calisan("45820161234", "Nazlı", "Yıldırım", 35, "Kadın", "Türk", "İnşaat", 68, 23450)

calisan1.zam_hakki()
calisan2.zam_hakki()
calisan3.zam_hakki()

print(calisan1)
print(calisan2)
print(calisan3)

#maviyaka
maviyaka1 = maviyaka("174812752", "Emir", "Şahin", 35, "Erkek", "Mavi Yakalı", "Türk", 36, 14500, 0.2)
maviyaka2 = maviyaka("674189283", "Cemile", "Lale", 28, "Kadın", "Mavi Yakalı", "Türk", 21, 12000, 0.5)
maviyaka3 = maviyaka("127481920", "Servet", "Sayar", 42, "Erkek", "Mavi Yakalı", "Türk", 51, 18000, 0.3)

maviyaka1.zam_hakki()
maviyaka2.zam_hakki()
maviyaka3.zam_hakki()

print(maviyaka1)
print(maviyaka2)
print(maviyaka3)