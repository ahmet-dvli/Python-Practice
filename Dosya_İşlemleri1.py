# Bu yapıcağım örnekleri sizde yaparsanız eğer, bunların sonucunu görmek için .txt uzantılı dosya açmanızı tavsiye ederim.
# ! İşlem yapmadan önce dosyayı açmalıyız.


# f = open("Dosyaislem.txt" , "r")  ----> dosyayı açar iki tane parametre gireriz. "r" sadece okurken "r+" hem okur hemde yazmayı sağlar.
# icerik = f.read() Bütün dosyayı okur.
# print(icerik)
# f.close()  Dosyayı kapatır (işimiz bitince.)

# with open("Dosyaislem.txt", "r") as f:  #Dosya işlemleri genellikle böyle yapılır ve manuel olarak kapatılır. 
  #  icerik = f.read()
  # print(icerik) 

# with open("Dosyaislem.txt") as f:
    # icerik = f.readlines() burda f.readline yazarsakta tek bir satırı bize gösterir.
    # print(icerik)             Burda yazdığımız readlines ise bize satır satır verecek. (\n ise burda enter anlamına gelir.)
    # for satır in icerik:    Böyle yazarsakta vereceği sonuç daha toplu şekilde verir.
      #print(satır,end="")

# pozisyon = f.tell()
# print(pozisyon)     Dersekte hangi karakterde olduğumuzu gösterir.

# f.seek(0) dersekte imleç 0. satıra yani en başa gelecek.

# with open("Dosyaislem.txt") as f:
    # icerik = f.read(10) Eğer read in içine (X) kadar sayı yazarsak o kadar sayıyı okuyup sonuçlandıracktır.Bu komutu alta alta yazarsakta x kadar harf okumaya devam edicek.
    # print(f.read(10),end="")

# with open("Dosyaislem.txt") as f:
    # okunacak_harf = 15
    # icerik = f.read(okunacak_harf) 
    # while len(icerik) > 0:
       # print(icerik,end="") 
       # icerik = f.read(okunacak_harf)             

# Bu yukarıda verdiğimiz örnekte ise büyüklüğü fazla olan dosyalarda parça parça olarak okumamızı sağlayan komut örneğidir.

# -------Dosya Yazma-------- Burda "w" parametresini kullanıcaz.Eğer yazı yazcağımız dosya yoksa sorun yok çünkü kendisi otomaatik dosya oluşturuyor.

# with open("Dosyaislem2.txt","w") as f:
   # f.write("nmap") 
# Burda "w" parametresiyle yazdığımız için tüm yazıları siler ve yerine yazdığımız şey gelir
# AMA burda "a" parametresiyle yazarsak eğer dosyanın sonuna yazdığımız şeyleri ekler.