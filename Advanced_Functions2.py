# Bugün ki konumuzda fonksiyonları döndürücez. Yani fonksiyonumuzun içinde yine bir fonksiyon olacak ama bunu içindeki çalıştırmıcaz "return" komutuyla döndürücez.
# NOT: Fonksiyonları döndüreceğimiz için return kisi_sec yazcaz ama yanına. ekstradan "()" koymıcaz.

def fonk(x):
    return x*x

a = fonk(2)
b = fonk
#print(b(5)) # Aslında bakın burda b = fonk dedik ve "()" koymadık print ettiğimizde ise python bunun bu bir fonksiyon cevabını verdi ben o zaman print(b(5)) dersemde bana yine 5 in karesini vericek.
 # Yukarıdaki örnek temel bir örnekti şimdi başlayabiliriz.

def islem_yap(islem):
    def toplam(*args):
        return sum(args) # Bakın unutmayın fonksiyon *args ı bir demet olarak aldıgı icin altta sum yazdık.

    def carpım(*args):
        carpım = 1
        for arg in args:
            carpım *= arg 
        return carpım
    
    def ortalama(*args):
        return sum(args) / len(args)
    
    if islem == "toplam":
        return toplam # Bakın burda fonskyionun kendisini geri döndürüyoruz.
    elif islem == "carpım":
        return carpım
    elif islem == "ortalama":
        return ortalama
    
toplama_fonk = islem_yap("toplam")
print(toplama_fonk(4,3,2,5))
carpma_fonk = islem_yap("carpım")
print(carpma_fonk(4,3,5,6))   
ortalama_fonk = islem_yap("ortalama") 
print(ortalama_fonk(3,4,5,3,2,4,5))

 # Evet yukarıda yaptıgımız aslında fonksiyonları döndürmüş olmamız.


def kisi_sec(kisi):
    def takım_sec(takım):
        return f"{kisi} {takım} takımını tutuyor"
    return takım_sec

a = kisi_sec("Ahmet")
b = kisi_sec("Melih")

print(a("Galatasaray"))
print(b("Beşiktaş")) 
# Biz burda aslında a parametresinde ahmet dediğimiz zaman return kısmında ahmet ismi direkt gitti.


# Şimdi yeni konumuza geçelim.Bu konuda çok uzun olmadıgı icin fazladan dosya açmak istemedim burdan devam edelim.
# Bu konumuzda ise fonksiyonlara parametre olarak fonksiyon göndermeyi öğreneceğiz.

def topla2(x,y):
    return x + y
def carpma2(x,y):
    return x * y

def islem_yap2(fonk,a,b): # Burda fonksiyon gönderdik.
    return fonk(a,b) 

print(islem_yap2(topla2,4,3)) # Parantez koymadık cünkü return yazdık.

# Baska bir örnege gecelim.

#liste = [1,2,3,4,5,6,7,8,9]
#fonk = x * x
#sonuc = [1,4,9,16,25,49,64,81]

liste1 = [1,2,3,4,5]
liste2 = [1,2,3,4,5,6,7,8,9]

def kare_al(x):
    return x * x
def kup_al(x):
    return x ** 3

def map_fonk(fonk,liste):
    sonuc = []
    for i in liste:
        sonuc.append(fonk(i))
    return sonuc

print(map_fonk(kup_al,liste2)) # Bakın burda ilk yazdıgımız "kare_al" bu bir fonksiyondur ister bunu değiştirip oraya kup_al da yazabiliriz yada listeyi değiştirebiliriz.
# Bu fonksiyon zaten pythonda var map_fonk diye geciyor. Ama burda öğrenmis olduk.