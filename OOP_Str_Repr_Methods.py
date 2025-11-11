# __str__   ve   __repr__       methods.

a = "Python"
#print(str(a))
#print(repr(a))
 # Aralarındaki fark aslında str olanda " sız yazarken repr de ise " lı yazıyor.Ama eğer buraya bir işlem (5/13) gibi bir şey yazarsanız sonuc ikisinde de aynı olacaktır.

from datetime import date
import datetime

bugun = date.today()
#print(bugun)
#print(str(bugun))
#print(repr(bugun))

# Evet burdada sonuclar farklı ve burada fark etmemiz gerekiyor ki; str methodu kullanıcın görmesini istediğimiz yani bi bakıma sadece sonucu gösterir.İşte yok bilmem hangi parametreyle yazılmıs datetime mi baska bir sey mi bunu bilemeyiz. Ama gidipte repr komutuyla yazarsak bu az once yazdıklarımı öğreniriz.
# Daha cok developer ların kullandıkları "repr" komutu olur.

class futbolcu:
    def __init__(self,isim,soyisim,gelir):
        self.isim = isim
        self.soyisim = soyisim
        self.gelir = gelir

    def __str__(self): # __str__ methodu sayesinde artık print("") diyince sonuc alabiliyoruz.
        return f"Ad : {self.isim}, Soyad : {self.soyisim}, Gelir : {self.gelir}"
    
    def __repr__(self):
        return f"futbolcu({self.isim},{self.soyisim}, {self.gelir})"

futbolcu1 = futbolcu("Mahmut","Lekeli",100000)

print(futbolcu1)

# NOT: Yukarıda aynı zamanda __repr__ yide yazdırdım ama ikiside aynanda yazılırsa python ilk önce str ye bakıyor o yoksa eğer gidip repr ye bakıyor aklınızda bulunsun.
print(futbolcu1.__repr__()) # Ekstradan böyle bir şey yazarsam o zaman repr yide sonuc terminalinde görmüş oluruz.



# Bugunluk bu kadardı.Basit örneklerle konuyu acıklamaya calıstım.Umarum faydalı olmustur.İyi calısmalar herkese.