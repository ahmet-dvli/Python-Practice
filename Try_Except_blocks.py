# Hata Yakalama.
# Programın herhangi bir aşamasında hata alırsak tüm kod çalışmaz.
# Bunu engellemek için aslında bir kaç yöntem vardır. Bugün onlara bakalım.


#try:
#    a = 6
#    b = 3
#    c = a / b
#    d = z 
#except:
#    print("Bir hata oldu.")
#    print("Hatayı düzelten kodlar çalışır")

#print(a,b,c,sep="-")
 # Burda baktığımız zaman d = z gibi bir değişken verdik ve python bu değişkeni bilmediği için hata vermesi lazımdı.Hata verdi ama bunu kırmızı yazıyla terminale göstermek yerine except komutu sayesinde hata vermedi.Ve burda expect komutu altına yazdığımız şeyler çalışacaktır.

#Şimdi ise birden fazla hata alırsak ne yapmalıyız ona bakalım.

#try:
#    a = 5
#    b = 0
#    c = a / b
#    d = z
#    isim = "Ahmet"
#    karakter = isim[10]
#except ZeroDivisionError:
#    print("Payda sıfırdan farklı olmalı")
 # Bu örnekte aslında except diyip ZeroDivisionError hatasını görürsek onu terminalde yazıp tüm kodu bozmak yerine "Payda sıfırdan farklı olmalı." yazsın
 # Şimdi altaki örnekte ise payda sıfırdan farklı olucak ama bu seferde "NameError" hatasını alcaz bunu almamak icinde devam ettiricez.

try:
    a = 5
    b = 6
    c = a / b
    d = x
    isim = "Ahmet"
    karakter = isim[2]
except ZeroDivisionError:
      print("Payda sıfırdan farklı olmalı")
except NameError:
     print("Bu değişken önceden tanımlanmamış.")
except IndexError:
     print("Karakter sayısı hatalı.")
except Exception: # Bu komut ise bizim gözümüzden kaçan hataları kendisi otomatik olarak buluyor ve yazdırıyor.
     print("Blinmeyen bir hata oluştu.")

else:
     print("Else blouğu çalışıyor") # Try bloğunda hiç hata yoksa bu "Else" bloğu çalışır.
finally:
     print("finally bloğu çalışıyor") # 