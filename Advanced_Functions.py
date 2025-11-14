# Bugün ki konumuz iç içe fonksiyonlar yani ---> Bir fonksiyonumuz olucak ve onun içinde fonksiyonlar olucak.

def dış_fonk():
    print("Dış Fonk çalışıyor")
    def iç_fonk():
        print("İç Fonk çalışıyor") # Böyle düz bırakırsak çalıştır dediğimizde bize sadece 1 ve 3. de ki "" ları gösterecek.Çünkü biz "iç fon calısıyor" yazsını çalıştırmadık sadece oluşturduk.
    iç_fonk() # Bunu yazarsak eğer şimdi "iç fonk calısıyor" yazacaktır.
    print("Dış Fonk Sonlanıyor")

#dış_fonk()

def işlemler(x):
    def kare_al(a):
        return a ** 2
    def karekok_al(a):
        return a ** 0.5 # Bu karekök al demektir.
    def faktoriyel_al(a): # Bu alttakide faktoriyel almadır.
        carpim = 1
        for i in range(1,a+1):
            carpim *= i
        return carpim
    kare = kare_al(x) 
    karekök = karekok_al(x) 
    faktoriyel = faktoriyel_al(x)
    return f"Karesi: {kare}, Karekökü: {karekök}, Faktoriyel: {faktoriyel}"    

print(işlemler(9))

# Evet yukarıda örnekte gördüğümüz gibi iç içe kullanmak bir bakıma böyledir.Burda sonda kare = , karekök = , gibi şeyler yaptık.Çünkü o işlemlere çalıştırmak içindi.
# Yani kısaca aslında en yukarıda yazarken bu fonskiyonları yazdık sadece ama çalıştırmadık bunun için dediğim gibi sonda return ü kulnnarak çalıştırma işlemine geçtik.

# Şimdi *args larla ilgili yapalım.

def toplam_carpım(*args):
    def toplama(z):
        return sum(z) # Burdaki "sum" toplamak demek unutmayalım.
    def carpma(z):
        carpma = 1
        for i in z:
            carpma *= i
        return carpma
    return f"Toplamları: {toplama(args)}, Çarpımları: {carpma(args)}"

print(toplam_carpım(4,6,5,9))

# Bugunlük bu kadardı herkese iyi çalışmalar dilerim.