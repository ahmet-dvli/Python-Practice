# Bu konu biraz karısık bu yüzden örneklerimize ve notlarımza dikkatli bir şekilde bakalım.
# iterator , iterable , iteration nedir ?
# Döngülerde kullanabildiğimiz her şey iterable dır.
# Adımlama işini yapan elemana iterator.(Nerde kaldıgını unutmaz.)
# __iter__() bir iterator geri döndürür.

rakamlar = [1,2,3,4,5]

#print(dir(rakamlar)) # Bir nesnenin icinde "iter" methodu varsa bu nesne döngülerde kullanılabilir.

a_rakamlar = rakamlar.__iter__()
a_rakamlar = iter(rakamlar) 
# Bu yukarıda yazdıgım iki sey aynıdır.

#print(dir(a_rakamlar)) # Burda next metodu var bu ise diger asamaya gec anlamına gelir.
print(next(a_rakamlar))
print(next(a_rakamlar))
print(next(a_rakamlar))
print(next(a_rakamlar))
print(next(a_rakamlar))
# Evet bakın bunları sırayla tek tek yazarsanız next komutu sayesinde aslında devam edebildiğini görüyoruz.
# Temel olarak döngülerin çalışma mantıgı bu şekildedir.
# Baska bir örnege gecelim.

while True:
    try:
        rakam = next(a_rakamlar)
        print(rakam)
    except StopIteration:
        break
# Bir döngüde arka planda olan şey bu aslında.(Hata olustugu anda hatayı yakaladık ve döngüden cıkardık.)
# Döngü önce iter i çağırıyor ordan iterator u alıyor ve hata gelene kadar iterator ın next metodunu cagırıyor. Sayılar bitince hata vericek ama vermemesi icin bu while true yu döndürüyor ve işlem bitmiş oluyor.
# Devam edelim...

class Deneme:
    def __init__(self,start,end):
        self.yazılacak = start
        self.end = end
    def __iter__(self): # ıterator döndürmeli ve ıteratorda da next methodu olması lazım.
        return self
    def __next__(self):
        if self.yazılacak >= self.end:
            raise StopIteration # raise = (fırlatmak)
        deger = self.yazılacak
        self.yazılacak += 1 # (+1)
        return deger
    
sayılar = Deneme(35,45)
for i in sayılar:
    print(i)
# Bunun üstüne
#print(next(sayılar)) # yazarsak hata alırız. Çünkü bitti artık 

# Şimdi kendimize bir iterator yazalım.(custom iterator)

Deneme2 = "Her galaksinin merkezinde kara delik vardır."

for i in Deneme2:
    print(i) # Böyle yazarsak bize tüm harfleri tek tek gösterir. Bunu düzeltmek icin kendi iterator umuzu olusturucaz.

class Cumle:
    def __init__(self,cumle):
        self.cumle = cumle
        self.index = 0 # (İlk kelimeyi yazdırmak icin)
        self.kelimeler = self.cumle.split() # (Ayırma işlemini yapar.)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.kelimeler): # (Mesela bizim 6 kelimemiz var index imiz 0 dan 5 e kadar olunca bitsin. E kelimemiz 6 niye 5 olunca bitsin DİKKAT 0 dan basladık 0 ile 5 dahil kaç sayı var 6 :))
            raise StopIteration
        döndürülecek = self.index # Burası döndürelecek 0 oldu sonra alta gec bir arttır.
        self.index += 1
        return self.kelimeler[döndürülecek]
        
yenicumle = Cumle("Her galaksinin merkezinde kara delik vardır.")

for kelime in yenicumle:
    print(kelime) # Evet gördüğünüz üzere kodumuz çalıştı. Kendi class ımızı for döngünde kullanılabilecek bir duruma getirdik.