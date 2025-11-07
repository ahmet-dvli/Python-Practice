# Sınıf ve Nesnelerin değişkenleri hakkında konuşacaz.

class çalışan:
    zam_miktarı = 2.2
    def __init__(self,isim,gelir,zam_miktarı):
        self.isim = isim
        self.gelir = gelir
        self.zam_miktarı = zam_miktarı

çalışan1 = çalışan("Mert", 3000, 2.2)
çalışan2 = çalışan("Güney",7000, 2.2)

#print(çalışan1.isim)
#print(çalışan2.gelir)

print(çalışan1.__dict__) # Bu çok öenmli aslında.Çünkü bana "çalısan1" hakkında tüm bilgileri detaylı bir şekilde sıralıyor.
# print(çalışan.zam_miktarı) # Burda class ım kendi üzerinden yada kendi ürettiğim nesnelerden erişebiliriz.

 # Yukarıda gördüğümüz gibi ekstra olarak "zam_miktarı" nı ekledik.Şimdi aşağıda yaptığım gibi bir yolu daha var.

class personel:
    def __init__(self,ad,maaş):
        self.ad = ad
        self.maaş = maaş

personel1 = personel("Ali", 1000)
personel2 = personel("Kuzey", 5000)

personel1.zam_oranı = 2.5 # Burda aslında gördüğünüz gibi "personel" classının içine yazmadan ayrı bir yerde sanki class ın içindeymiş gibi ekledik.
print(personel1.__dict__)
