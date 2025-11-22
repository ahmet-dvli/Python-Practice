# Bu fonksiyonumuz ise bir bakıma map fonksiyonumuzun kardesi diyebiliriz. Yine bir fonksiyon ve liste alıyor ama fonksiyonun true yada false değerini döndürmesi lazım.
# True yu döndüren degerlerle bize yeni bir liste olusturuyor.

Sunum_Sayfaları = [1,2,3,4,5,6,11,16,24,432,530,543]

def cift_mi(x):
    if x %2 == 0:
        return True
    return False

cift_sayfalar = list(filter(lambda x : x %2 == 0,Sunum_Sayfaları)) # lambda şeklinde yazılışıdır. 
cift_sayfalar2 = list(filter(cift_mi,Sunum_Sayfaları)) # Buda normal yukarıda ki yazdıgımız komut listesine göre yazılısıdır.
#print(cift_sayfalar)
#print(cift_sayfalar2)

def üç_basamaklı(x):
    if x >= 100 and x <= 1000:
        return True
    return False
üç_basamaklılar = list(filter(lambda x : x >= 100 and x <= 1000,Sunum_Sayfaları)) # Yine ben lambda şeklinde yazmak istedim.
#print(üç_basamaklılar)

# Baska bir örnekten devam edelim.

Yiyecekler = ["Makarna","Köfte","Bonfile","Ahtapot","Antrikot","Sushi"]
A_ile_baslayanlar = list(filter(lambda Yiyecek: Yiyecek.startswith("A"),Yiyecekler))
#print(A_ile_baslayanlar)
icinde_a_veya_A_gecenler = list(filter(lambda Yiyecek: Yiyecek.startswith("A") or "a" in Yiyecek,Yiyecekler)) # Burdada gördüğünüz gibi lambda ile A ile baslayan yada icinde a gecen kelimeleri yazdırdık.
#print(icinde_a_veya_A_gecenler)

# Örnekteklerden devam edelim.

liste = [1,2,(1,2,3,4,5,),True,"string","Deneme",{1,2,5,6,7}]
stringler = list(filter(lambda x: isinstance(x,str),liste)) # (x nesnesi str classından ise true değerini döndür.)
print(stringler) # Evet gördüğünüz gibi oldu yada oraya "bool" yazarsak True yu gösterecek.

# Not pythonda 1 == True olup 0 == False dur.
# Son bir örneğe gecelim.

bilgiler = [{"Ad": "Ahmet", "Yaş": 25},{"Ad": "Sinan", "Yaş": 29},{"Ad": "Mehmet", "Yaş": 19},{"Ad": "Sabri", "Yaş": 30}]
s_ile_baslayanlar = list(filter(lambda kisi: kisi["Ad"].startswith("S"),bilgiler))
print(s_ile_baslayanlar)
yirmiden_buyuk_olanlar = list(filter(lambda kisi: kisi ["Yaş"] > 20,bilgiler))
print(yirmiden_buyuk_olanlar)

# Evet bu konuda genel olarak bu kadardı.

