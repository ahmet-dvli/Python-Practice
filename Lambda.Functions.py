# Bu konumuz ise artık bir seyler ogrendigimiz icin daha ileriye seviyeler için gerekli olan bir fonksiyon.
# Bu lambda ları kullanma sebebimiz genellikle yazımı basit yer kaplamayan pratik olduğunu icin kullanırız.
kare_al = lambda x : x * x # (Bu fonksiyon x i alıyor ve x in karesini alıyor.)

kup_al = lambda x : x ** 3 

toplam = lambda x, y : x + y

genel_toplam = lambda *args : sum(args) # Unutmayın *args bir demet oldugu icin sum ile yazdık.
 
#print((lambda x,y,z : x * y + z)(3,4,5)) # Burda da gordugunuz gib print kısmından lambda yı kullanarak bir fonksiyon yazabiliyoruz.
#print((lambda *args : sum(args) / len(args))(2,3,4,5,6)) # Buda baska bir örnek gördüğünüz gibi ilk yazdıgımız fonksiyon olup sonradan da parametlerimizi ekiyoruz.

# Konumuza devam edelim.

list = [("Ahmet",26),("Mert",20),("Mahmut",35),("Sabri",40)]
#list.sort() # Unutmayın sort() --> Sıralamak demektir. Bu alfabeye göre sıralamadır.
list.sort(key = lambda x : x[1]) # Bu ise bize yaslarına göre sıralıcaktır.
#print(list)

#def yaslari_goster(x):  ========= Bu aslında lambda x : x[1] e eşittir ben list.sort(key = yaslari_goster) dersemde bu sefer aynı sonuc cıkacaktır.
#    return x[1]

list2 = [{"Ad":"Ahmet","Soyad" :"Düz","Yaş":25},{"Ad":"Soner","Soyad" :"Sol","Yaş":21},{"Ad":"Mert","Soyad" :"Yan","Yaş":29}]
list2.sort(key = lambda x : x["Soyad"])
print(list2)

# Bu konu genel hatlarıyla aslında bu kadardı bol bol pratik yapmak lazım ki bunlar kafada otursun. En basitinden hani aynıları bakmadan yazmaya çalısın ve değişkenleri değiştirin ve yazarken de kafanızda "ben şimdi bu kodu yazıcam" diyerek yazın. Herkese iyi çalışmalar.