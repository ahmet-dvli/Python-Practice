# Bugün property , setter ve deleter decoratorlarımza bakıcaz.
# Burda genel mantık aslında metot olarak yazdıgımız şeyleri bir özelliğe çevirerek işimizi kolaylaştırıyoruz.

class insan:
    def __init__(self,isim,soyisim):
        self.isim = isim
        self.soyisim = soyisim
        #self.isimsoyisim = isim + " " + soyisim
    
    def isimsoyisim(self):
        return f"{self.isim} {self.soyisim}"


    def email(self):
        return f"{self.isim}.{self.soyisim}@sirketmail.com"
    
insan1 = insan("Mehmet","Kızgın")
insan1.isim = "Ahmet"


#print(insan1.isim)
#print(insan1.isimsoyisim())
#print(insan1.email()) # Burda sonda parantez varken digerlerinde yok. Çünkü biz self.isim gibi özellik oluşturdum. Ama email e özel bir durum olmadıgı için mecbur "()" koyduk.

# Eğer insan1.isim = "x" diyerek baska bir degisken olusturursanız sonuc beklediğimiz gibi gelmeyebilir. Bunu engellemek için ise biz yukarıya def isimsoyisim(self): diye yeni komut bölümü olusturduk. Ve printtede yazarken print(insan1.isimsoyisim())
# yine ekstradan "()" koyduk. 
# Evet göründüğü üzere çok uğraştırıcı hele ki bu durumdan basınıza 10 tane geldiğinni düşünün. Bunun için işte "property" den faydalanırız.


class insan:
    def __init__(self,isim,soyisim):
        self.isim = isim
        self.soyisim = soyisim
        #self.isimsoyisim = isim + " " + soyisim
    @property
    def isimsoyisim(self):
        return f"{self.isim} {self.soyisim}"
    
    @property
    def email(self):
        return f"{self.isim}.{self.soyisim}@sirketmail.com"
    
insan1 = insan("Mehmet","Kızgın")
insan1.isim = "Ahmet"

#print(insan1.isimsoyisim) # Bakın ekstradan "()" koymadık. Burdan da aslında property özelliğinin bize içerde oluşturdugumuz metotlara bir isim soyissim özelliğimiş gibi kullanılmemizi sağladı.
#print(insan1.email)

# eğer gidipte mesela insan1.isimsoyisim = "Mahmut Düz" yazarsak hata alıcaz çünkü bu yazdıgımız bir özellik değil sadece bir metot.
# Bunu yapmak için ise "setter" decorator ı kullanıcaz.

class insan:
    def __init__(self,isim,soyisim):
        self.isim = isim
        self.soyisim = soyisim
        #self.isimsoyisim = isim + " " + soyisim
    @property
    def isimsoyisim(self):
        return f"{self.isim} {self.soyisim}"
    
    @property
    def email(self):
        return f"{self.isim}.{self.soyisim}@sirketmail.com"
    
    @isimsoyisim.setter 
    def isimsoyisim(self,isim):
        isim,soyisim = isim.split(" ") # ! İsim soyisim in arasına boşluk bırak anlamına gelir.
        self.isim = isim
        self.soyisim = soyisim
    @isimsoyisim.deleter # Bakın burda deleter decorator ımız
    def isimsoyisim(self):
        print("silinmiştir.")
        self.isim = None
        self.soyisim = None


    
insan1 = insan("Mehmet","Kızgın")
insan1.isim = "Ahmet"
insan1.isimsoyisim = ("Alper Düzgün")
del insan1.isimsoyisim

print(insan1.isimsoyisim)
print(insan1.isimsoyisim)
print(insan1.email)
# Göründüğü gibi en güncel olan bu oldu.

# Birde del (x).isim dersekte sadece ismini sileriz. Del in mantıgı silme işlemi.
# (isimsoyisim.deleter)
