# Aşağıda geçen konumuzla ilgili ufak bir özet yapalım.

class insan:
    zam_orani = 1.1
    insan_sayisi = 0
    def __init__(self,isim,yaş):
        self.isim = isim
        self.yaş = yaş
        insan.insan_sayisi += 1

#print(insan.insan_sayisi) # Burda insan sayısı ilk başta "0" olarak yazıcak ama biz her "insan" görünce bir arttır değidiğimiz için her seferinde print yazarken kişi sayısı "1" artacak.
insan1 = insan("Tekin",21)
insan2 = insan("Metin",25)


# Şimdi asıl konumuza geçelim

from datetime import date

class personel:
    zam_miktarı = 1.5
    personel_sayisi = 0
    def __init__(self,ad,yas):
        self.ad = ad
        self.yas = yas
        personel.personel_sayisi += 1

    def bilgilerini_soyle(self): # Instance Method
        return f"Ad: {self.ad} Yaş: {self.yas}"
    
    @classmethod # Class Method
    def personel_sayisini_soyle(cls): # cls = class anlamına gelmektedir.
        return cls.personel_sayisi
    
    @classmethod # Class Method
    def string_ile_olustur(cls,str_):
        ad,yas = str_.split("-")
        return cls(ad,yas)
    
    @classmethod # Class Method
    def dogum_yili_ile_olstur(cls,ad,dogum_yili):
        return cls(ad,date.today().year - dogum_yili) # Bu önemli burda "bir kişinin yaşını nasıl buluruz" adlı komut sistemi.
    
    @staticmethod # Static Method
    def dogum_hesapla(personel):
        return date.today().year - personel.yas



personel1 = personel("Gökhan",18)
personel2 = personel("Ahmet",19)
print(personel1.bilgilerini_soyle()) # Evet burda gördüğümüz gibi bilgilerin hepsini detaylıca söylüyor. 
personel3 = personel.string_ile_olustur("Mert-29")
personel4 = personel.dogum_yili_ile_olstur("Ayse",1995)
print(personel4.ad,personel4.yas) # Burdada 1995 dogumlu Ayse`nin yasını eklemis olduk 
print(personel.dogum_hesapla(personel1))
print(personel.personel_sayisini_soyle()) # Burda ise @class methodu sayesinde iki kişiyi üçe çıkarttık.