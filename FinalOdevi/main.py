from insan import insan
from issiz import issiz
#from calisan import calisan
#from maviyaka import maviyaka
#from beyazyaka import beyazyaka
#import pandas as pd

insan1 = insan("11223344556", "Kerem", "Yılmaz", 30, "Erkek", "Türk")
insan2 = insan("12312312345", "Selin", "Kaya", 27, "Kadın", "Türk")

print(insan1)
print(insan2)

gecmis_tecrubeler_1 = {"Mavi Yakalı": 4, "Beyaz Yakalı": 7, "Yönetici": 2}
issiz_1 = issiz("12121314156", "Ali", "Demir", 34, "Erkek", "Türk", gecmis_tecrubeler_1)

gecmis_tecrubeler_2 = {"Mavi Yakalı": 6, "Beyaz Yakalı": 3, "Yönetici": 1}
issiz_2 = issiz("98765432109", "Ayşe", "Güler", 32, "Kadın", "Türk", gecmis_tecrubeler_2)

gecmis_tecrubeler_3 = {"Mavi Yakalı": 2, "Beyaz Yakalı": 3, "Yönetici": 5}
issiz_3 = issiz("45678912310", "Osman", "Çelik", 35, "Erkek", "Türk", gecmis_tecrubeler_3)

issizler = [issiz_1, issiz_2, issiz_3]

for issiz in issizler:
    print(f"{issiz}")