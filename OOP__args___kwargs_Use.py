def kuvvet_al(x,y): # Positional Arguments hepsi tam olarak girilmeli ki komut çalışsın.
    return x ** y

#print(kuvvet_al(3,4))

def bilgi_ver(isim,soyisim,yas ):
    return f"Ad: {isim} , Soyad: {soyisim} , Yaş {yas}"
#print(bilgi_ver("Alp","Düzgün",25))
# Burda mesela yas kısmına hic bir şey girilmeyip en üstte def bilgi_ver kısmında "yas = "Girilmedi"" yazarsam hata vermyecektir.
# Çünkü biz yas kısmına varsayılan bir değer atadık.Ve bu tür argümanlara Keyword Argument deniliyor.
# Hemen allta bir örnekle açıklayalım.

def bilgi_ver2(isim,soyisim = "Girilmedi",yas = "Girilmedi"):
    return f"Ad: {isim}, Soyad:{soyisim}, Yaş {yas}"
print(bilgi_ver2("Yakup","Düzgün")) # Evet gördüğümüz gibi "yas" kısmına bir sey girmedik ama ona bir deger verdigimiz icin sonuc olarak yazdı.
print(bilgi_ver2("Mert","Kara",25)) # Ama eğer bakın burda yas kısmına yasını yazarsak onu kabul alıyor.Bunu aslında bir formu dolduruyoruz gibi düşünebiliriz.Eğer yas kısmını bos bırakırsak bize "girilmedi" dicek ama yasımızı yazarsak kabul edecektir.
print(bilgi_ver2("Ali",yas = 36)) # Burdada aslında eğer sadece isim kısmını doldursaydık hata verecekti ama biz gidipte yine yukarıda soyisim = "Girilmedi" yazdık. Ve printte bunu yazarken soyisim kısmı bos olcagı icin python bu sırayı bilemez ve karısacaktı bunun önüne gecmek icinde "isim" kısmından sonra yas = 36 diyerek karısıklıgı engellemis olduk.

def topla2(x,y):
    return x + y
# Bu sayılar herhangi iki sayı değilde üç sayı olsaydı..... İşte bugün bunun bir çözüm yolunu öğrenicez.

def topla(*args):
    for arg in args:
        print(args)
    

topla(1,2,3,4,5) # "*args" dersek istediğimiz kadar parametre yazdırabiliriz.

def carp(*args):
    carpim = 1
    for arg in args:
        carpim *= arg
    return carpim 
 # Bu yukarıda yazdıgım bir carpma döngüsü olup bize istediğimiz kadar yazdıgımız sayıları carpıcak.
 # (Mantıgı ise aslında carpim=1 diyerek bir eşitlik olusturuyoruz sonra for dongusunden yararlanarak carpim yani 1 ile arg(yazdıgımız sayılar) ı carpıp return ettirip sonuca yazdırıyor.)
 # *args bizim istediğimiz kadar parametre yazmamızı saglıyor

def ortalama(*args):
    return sum(args) / len(args) # Bu ortalama bulma kodu diyebiliriz en sade halde. args bir demet oldugu sum ve len den yararlandık sum burda toplama olup len ise miktar (kaç sayı ?) gibi düşenebilliriz.


# print(carp(2,4,5,6,7,5,4,3))
print(ortalama(3,4,5,6))

def selamla(mesaj,*args):
    sonuc = ""
    sonuc += mesaj
    sonuc += " "
    for arg in args:
        sonuc += arg
        sonuc += " "
    return sonuc

print(selamla("merhaba","naber","iyi misin"))

# Evet aslında *args bu kadardı bu bizim istdiğimiz kadar parametre yazamamızı saglıyor.

def fonk(**kwargs): # İstediğimiz kadar kword yazmamızı saglar.
    print(kwargs)

fonk(ad = "mahmut" , soyad = "yasar", yas = 35) # Sonucta cıkan seyler {} le oldugu icin aslında bunları sozluk olarak sakladıgı anlamına gelir.

def fonk2(zorunlu,*args,**kwargs):
    print(zorunlu)
    print("*************")
    for arg in args:
        print(arg)
    print("************")
    for kwarg in kwargs:
        print(kwarg)

fonk2(2,3,4,5,6,7,ad = "mahmut", yas = 35) # Run yaptıgımızda ilk yazan "2" zorunlu olup yıldızdan sonraki 3,4,5,6,7 ise *args olup kalan ise ad yas onlarda **kwargs oldu.
# Not: Evet terminal de mahmut yerine ad , 35 yerinede yas yazdıgını görebilirsiniz. **Kwargs sadece key leri alıyor bu = sonrakiler value oldugu icin onları almıyor.
# for k,v in kwargs.items():
    #print(k,v) diyerek düzeltebiliriz.