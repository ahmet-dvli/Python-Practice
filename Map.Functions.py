# Bu bölümüzde ise "map" fonksiyonumuzu kullanıcaz. Bu fonksiyonumuzun amacı ise yazdıgımız kodun daha kısa ve düzenli gözükmesini saglar.
# Kafanız karışmasın diye printlerin başına "#" ekleyebilirsiniz.
liste = [1,2,3,4,5,6]
def kare_al(x):
    return x * x

liste2 = []
for i in liste:
    liste2.append(kare_al(i))
print(liste2) 
# Evet burda ilk hic bir şey kullanmadan yapmayı gördük.(list deki sonucları list2 ye aktardık.)

liste3 = tuple(map(kare_al,liste))
print(liste3)
# !!! Burda eğer liste3 = diyip "list" i yazmazsanız beklediğimiz sonucu alamayız. Oraya mesela list , set , tuple yazarak istediğimze cevirebiliriz
# (list = liste görünümü , set = küme görünümü , tuple = demet görünümü)

# Baska bir örnege gecelim...

Sıra = [1,2,3,4,5,6,8,9]
Sıra2 = list(map(lambda x : x * x,Sıra)) # Tekrardan hatırlayalım map oldugu icin orda lambdan sonra diger parametre olarak "Sıra" yı yazdık.
print(Sıra2)

Sıra3 = set(map(lambda x : x ** 3,Sıra2))
print(Sıra3)
# Bakın gördugunuz gibi "map" ve "lambda" komutunu kullanarak ne kadar kısalttık. Ve ayrıca çokta uzun yazmamıza gerek kalmadı.
# Diger bir örnege bakalım...

Düzen1 = [1,3,4,7,8]
Düzen2 = [3,5,9,0,1]

def toplam(x,y):
    return x + y
Sonuc = list(map(toplam,Düzen1,Düzen2))
print(Sonuc) # Bakın burda da x + y topladık ama map yazarken parametre kısmını x ve y den eleman lazım oldugu icin "Düzen1" ve "Düzen2" yazdık.
# "z" degiskeni eklemek isterseniz de yine aynı mantık. Yalnız şöyle bir durum da var: sizin mesela liste1 ve liste2 niz 5 elemanlı , siz liste3 eklediniz ama o 3 elemanlı o zaman durum değişiyor.
# Yine alt alta toplama işlemleri soldan sağa yapılıyor ama en az elemanlı liste nin baska elemanı kalmayınca işlem sona eriyor. Bunu kendiniz deneyip görebilirsiniz.
# Diger bir örnege gecelim.

hasılatlar = [["Gömlek", 170],["Kazak", 150],["Mont", 200],["Gözlük",90]]
def indirim_uygula(x):
    hasılat,fiyat = x[0],x[1] # Dikkat pythonda 0 dan baslanır bu yüzden hasılat = 0 , fiyat = 1 olarak düşünün.
    fiyat = fiyat * (5/10)
    return [hasılat,fiyat]

sonuc1 = list(map(indirim_uygula,hasılatlar))
print(sonuc1) # Bakın göründüğü gibi istediğimiz gibi calıstı.
# Son örnegımze gecelim.

isimler = ["mERt","SabRİ","YASaR","ONur"] # Mesela bunlar sitemize kayıt olan isimler biz bunları hepsini büyük veya kücük harfe cevirmek istiyoruz.

isimler2 = list(map(lambda x : x.lower(),isimler)) # "lower" tüm harfleri kücük yapar.
print(isimler2)
# x.capitalize() yazarsakta sadece ilk harfi büyük yapar.
# Bu ders bu kadardı kendinize dikkat edin.