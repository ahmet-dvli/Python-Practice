# Belirlenen özelliklerin diğer nesnelerede aktarılması olayına İnheritance(kalıtım) denir.
# Neslerin kendine has özellikleri de olabilir.

class Calısan:
    zam_miktarı = 1.5
    def __init__(self,isim,soyisim,gelir):
        self.isim = isim
        self.soyisim = soyisim
        self.gelir = gelir
        self.email = isim + soyisim + "@sirket.com"
    def bilgileri_goster(self):
        return "Ad: {} Soyad: {} Gelir {} E-mail {}".format(self.isim,self.soyisim,self.gelir,self.email)

calisan1 = Calısan("Mehmet","Gider",4000)
calisan2 = Calısan("Mert","Güney",5000)

class Yazılımcı(Calısan): # Burda iste kalıtım yani miras özelliğimiz devreye giriyor."Yazılımcı" class`ımız "Calisan" class`ın özelliklerini içericek.
    def __init__(self,isim,soyisim,gelir,bildigi_programlama):
        self.isim = isim
        self.soyisim = soyisim
        self.gelir = gelir
        self.email = isim + soyisim + "@sirket.com"
        self.bildigi_programlama = bildigi_programlama
    zam_miktarı =  1.2
    def bilgileri_goster(self):
        return "Ad: {} Soyad: {} Gelir {} E-mail {} Bildigi_Programlama {}".format(self.isim,self.soyisim,self.gelir,self.email,self.bildigi_programlama)


yazilimci1 = Yazılımcı("Berk","Yasar",9000,"Java")
yazilimci2 = Yazılımcı("Ay","Su",7000,"C+")
#print(yazilimci2.email) # Evet burda miras özelliğimizi kullanarak bir yazılımcının e-mail ini çıkartmış olduk.
#print(yazilimci1.zam_miktarı) # Eğer "yazılımcı" class ının altında baska bir sey olmazsa direkt "calısan" class ındaki zam oranına göre yazılıyor.Ama "yazılımcı" class ında zam miktarı olsaydı ona göre yazılacaktı.
#print(calisan2.bilgileri_goster())
#print(yazilimci1.bilgileri_goster()) # Yine aynı mantık --> Kendi classında "bilgileri_goster" olmadığı icin miras aldığı class tan aldı.
print(yazilimci1.bilgileri_goster())

# Eğer "yazılımcı" class ına yeni bir özellik eklemek istiyorsam onun "__init__" parametresini bastan tanımlamamız gerekiyor.
# "yazılımcı" class ına aslında tüm sel."""" ı yazmamıza gerek yok :) Sadece altına "super().__init__(isim,soyisim,gelir,email)" yazarsakta kabul olurdu bu bize böyle yukarıdaki gib 3-4 satırlık için değilde 100 tane satırlık islerde kolaylık saglar.
