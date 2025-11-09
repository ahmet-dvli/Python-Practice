# Bu methodların "dunder" olması sebebi ise bir tane "__" ile başlamasıdır.

#print(3 + 5)
#print(int.__add__(3,5)) # Burda göründüğü üzere "int" in yanındaki "__add__" methodu 3 ile 5 topladı.

#print("ali","mehmet")
#print(str.__add__("ali","mehmet"))

#print([1,2,3] + [4,5,6])
#print(list.__add__([1,2,3],[4,5,6]))

# Evet aslında fark edeceğimiz üzere belirli terimlerin bir anlama geldiğini görüyoruz.Mesela eğer yazdığımız şey bir "int" ise;
# add = (+) , sub = (-) , mul = (*) , floordiv = (//) , truediv = (/) , mod = (%) , lshift = (<<) , rshift = (>>) anlamlarına gelir.

class Benimlistem(list):
    def __add__(self, other): # Burda yaptığımız şey ise, iki listedeki elemanların birbirine karşılıklı gelen elemanlarını toplar.Ama yazdığımız kod sayesinde de eğer eleman sayıları eşit değilse "(uyarı mesajı)" verecektir.
        if len(self) != len(other):
            return "Bu elemanlar toplanamaz."
        else:
            sonuc = Benimlistem()
            for i in range(len(self)):
                sonuc.append(self[i] + other[i])
        return sonuc
    
    def __sub__(self, other): # Burayada bunun zıttı olan ("-") olanını yapalım.
        if len(self) != len(other):
            return "Bu elemanlar çıkarılamaz."
        else:
            sonuc = Benimlistem()
            for i in range(len(self)):
                sonuc.append(self[i] - other[i])
            return sonuc
        
    def __eq__(self,other): # Buda eşit mi değil mi sorusunun cevabını öğreniriz.
        if sum(self) == sum(other):
            return True
        return False
    
    def __abs__(self):  # Mutlak değer anlamına gelir ve negatifleri pozitif yapmasını isticez.
        sonuc = Benimlistem()
        for i in self:
            if i >= 0:
               sonuc.append(i)
            else:
                sonuc.append(-1 * i)
            return sonuc # Bunu unutmayın sonda yazmayı yoksa "none" alırsınız.

        

liste1 = Benimlistem([1,2,-3])
liste2 = Benimlistem([-4,5,-6])

#print(liste1 + liste2)
#print(liste1 - liste2)
#print(liste1 == liste2)
#print(abs(liste1))
#print(abs(liste2))
 
class Basketbolcu:
    def __init__(self,isim,soyisim,yaş):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş

    def __eq__(self,other):
        if self.isim == other.isim and self.soyisim == other.soyisim:
            return True
        return False
    
    def __add__(self,other):
        isim = self.isim[0] + other.isim[0]
        soyisim = self.soyisim[1] + other.soyisim[1]
        yaş = self.yaş + other.yaş
        return Basketbolcu(isim,soyisim,yaş)
    
    def __lt__(self,other):
        if self.yaş < other.yaş:
            return True
        return False
    
    def __gt__(self,other):
        if self.yaş > other.yaş:
            return True
        return False

        
basketbolcu1 = Basketbolcu("Alperen","Şengün",23)
basketbolcu2 = Basketbolcu("Mert","Yılmaz",27)

#print(basketbolcu1 == basketbolcu2) # Bunu yaparsak evet "false" alıcaz.

basketbolcu3 = basketbolcu1 + basketbolcu2
#print(basketbolcu3) # Bunu böyle yazarsak beklediğimiz sonucu alamayız buda diğer konumuz aslında...Ama tek tek bakmak için basketbolcu3.isim,soyisim gibi yazabiliriz.
print(basketbolcu1 > basketbolcu2)
        