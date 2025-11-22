# Parametre olarak yine bir fonk. ve bir tane liste alır
# Fark olarak bu reduce bize bir tane deger döndürüyor.
# Bu reduce functools modulundedir.
# Map fonksiyonuyla aynı gelebilir ama map fonk. bize formattan nesne yapıyor(liste , küme gibi) ancak reduce sadece tek bir deger döndürüyor.

from functools import reduce
liste = [3,4,5,6,21]

def toplam(x,y):
    return x + y
def çarpım(x,y):
    return x * y

sonuc = reduce(toplam,liste)
print(sonuc)
sonuc2 = reduce(çarpım,liste)
print(sonuc2)

# Pythonda ebob var ama ekok bulma yoktur. Biz onu bulalım.

from math import gcd 

liste1 = [2,4,6,7,5,3] #ebob(a,b)*ekok(a,b) = a*b yani ----> ekok(a,b) = a * b / ebob(a,b)

def ekok(x,y):
    return int((x * y) / gcd(x,y)) # gcd = ebob

print(ekok(5,6))

ekok_ = reduce(ekok,liste1)
print(ekok_) # Ekok alma sırası burda x ve y yi aldı sonra cıkan sonucla diger bir sayıylada bu dongu devam edioyr.

# Baska bir örnekten devam edelim

def tas_makas(x, y):
    küme = {x, y}
    if x == y:
        return x
    if küme == {"taş", "makas"}:
        return "taş"
    if küme == {"taş", "kagıt"}:
         return "kagıt"
    if küme == {"kagıt", "makas"}:
        return "makas"        

liste2 = ["taş","kagıt","makas","taş","makas","taş"]
sonuc3 = reduce(tas_makas, liste2)
print(sonuc3) # Evet böyle yaptıgımızda da sonuc gördüğümüz gibi terminalde yazıyor.

# Bu dersimizde bu kadardı iyi çalışmalar herkese.