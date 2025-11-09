# Burda yine gecenki örneğimizden devam edicem.Bu örnek üstüne yeni bir şeyler ekleyerek devam edelim.
# Bugünki dersimizde ise "Yönetici" class ını olusturacaz ve o class e ozel yetkiler olucak ve "calısan" class ını da miras alıcak.

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


class Yönetici(Calısan):

    def __init__(self, isim, soyisim, gelir,çalışanlar = None):
        super().__init__(isim,soyisim,gelir)
        if çalışanlar == None:
            self.çalışanlar = []
        else:
            self.çalışanlar = çalışanlar

    def çalışan_ekle(self,çalışan): # Burda "çalışan" ekleme fonksiyonunu yazdık.
        if çalışan not in self.çalışanlar: # (Bu yöneticinin çalışanlar listesinde "çalışan" yoksa..)
            self.çalışanlar.append(çalışan)

    def çalışan_sil(self,çalışan): # Burda "çalışan" silme fonksiyonunu yazdık.
        if çalışan in self.çalışanlar:
            self.çalışanlar.remove(çalışan)

    def çalışan_göster(self,çalışan):
        for çalışan in self.çalışanlar:
            print(çalışan.bilgileri_goster())

yönetici1 = Yönetici("Tekin","Güney",20000)

yönetici1.çalışan_ekle(calisan1)
yönetici1.çalışan_ekle(calisan2)
yönetici1.çalışan_göster(calisan1)
print("*************")
yönetici1.çalışan_sil(calisan1) # "Çalışan1" sildik ve bir çalışan kaldı.
yönetici1.çalışan_göster(calisan1)
yönetici2 = Yönetici("Adnan","Koç",15000,[calisan1,calisan2]) # Bu ise kendimiz "yönetici2" nin yanına yazarak çalışan ekledik
yönetici2.çalışan_göster(calisan1)

print(isinstance(yönetici2,Calısan)) # Burdaki "isinstance" ise bize yönetici2 nin "Calısan" class ında mı olduğunu gösteriyor.
print(issubclass(Yazılımcı,Calısan))
         


 