# Bugün bu dersimizde pythonda decorator komutunu öğrenicez. Bunu daha rahat anlamak için fonksiyoonlarınn özelliklerini bilmemiz gerekir.
# Bizim var olan fonksiyonlarımıza özellikler eklememizi sağlar.

# Basit bir örnekle açıklayalım. 

def decorator(fonk):
    def wrapper():
        print("fonksiyon çalışmadan önceki işlemler")
        fonk()
        print("fonksiyon çalıştıktan sonraki işlemler")
    return wrapper 
# Yukarıda yazdıgımız komutlar aslında decorator fonksiyonumuz genel bir yapısı. "wrapper" kullanılıyor aslındaa sarmak anlamına gelir.

@decorator # Bunun sayesinde aslında burdaki fonksiyonu al ve decorator a gönder anlamına gelir.
def ilerifonk():
    print("fonskiyon çalısıyor")

#ilerifonk()

import time
def zaman_hesapla(fonk):
    def wrapper(*args,**kwargs):  # Buraya *args ve **kwargs yazdık. Çünkü fonksiyonlarımızın içine herhangi bir şey gelebilir.
        baslangıc = time.time() # Unutmayın time.time geçen zamandır.
        fonk(*args,**kwargs)
        bitis = time.time()
        print(f"işlem {bitis - baslangıc} saniye sürdü.")
    return wrapper
    
@zaman_hesapla
def kareleri_al(liste):
    for i in liste:
        print(i * i)
kareleri_al(range(10))
@zaman_hesapla
def küpleri_al(liste):
    for i in liste:
        print(i ** 3)
@zaman_hesapla
def topla(a,b):
    time.sleep(1)
    
    return a + b 

#kareleri_al(range(10000))

# Baska bir örneği gecelim.
import time 

def zaman_hesapla(fonk):
    def wrapper(*args,**kwargs):
        baslangic = time.time()
        sonuc= fonk(*args,**kwargs)
        bitis = time.time()
        print(f"işlem {bitis - baslangic} sürdü.")
        return sonuc
    return wrapper
@zaman_hesapla
def kareleri_al(liste):
    sonuc = []
    for i in liste:
        sonuc.append(i * i)
    return sonuc
@zaman_hesapla
def küpleri_al(liste):
    sonuc = []
    for i in liste:
        sonuc.append(i ** 3)
    return sonuc
@zaman_hesapla
def topla(*args):
    time.sleep(1)
    return sum(args)

print(kareleri_al(range(1000)))