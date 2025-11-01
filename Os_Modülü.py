import os

# print(os.getcwd()) ---- Aktif olduğumuz dizini gösterir
# os.chdir("Desktop/Python deneme") ---- İstediğimiz dosyaya gitme
# print(os.listdir()) ------- Dosyanın içeriğini görmek için
# (parantezin içine ne yazarsakta onun içindekini gösterir.)
# for dosya in os.listdir():
#  print(dosya) ------ bu ise "for" u kullanarak hangi listdir deysem onun içinde dosyaları bana düzenli bir şekilde sıralar.

# os.mkdir("DenemeKlasörüPYT") ---- Dosya Oluşturma
# os.makedirs("Deneme1/Deneme2/Deneme3") ------- Buda iç içe dosya oluşturmadır.

# os.rmdir("DenemeKlasörüPYT") ------- Dosya silme işlemini gerçekleştirir.
# os.removedirs("Deneme1/Deneme2/Deneme3") ------ Bu komut ise birbirine iç içe geçmiş olan dosyayı siler ama DİKKAT burda sadece içi boş olan klasörü silecektir.

# os.rename("Denem1.docs", "Deneme1.docs") ---- Dosyanın isminidi değiştirir ("orijinal dosta","yeni isim")
# print(os.stat("Deneme1.docs").(x)) ---- Bu ise dosya hakkında bilgi sahibi olmamızı sağlar.X işareti ise hangi konu hakkında bilgi almak istiyorsak onu yazarız.
# -- Burda bir şey demek istiyorum: X yerine mesela st.atime yazdınız ve verdiği sonuc 15694598 gibi bir şey oldu bunu tarihe çevirmek için;
# from datetime import datetime diyip altına time = datetime.fromtimestamp(os.stat("Deneme1.docs").st_atime) yazıp print(time) yazarak düzeltebilirsiniz.

# print(os.path.join("Deneme1","Deneme2")) ----- Bu ise bize dosya yolu oluşturur.Aralarından birinin başına"/" koyarsanız başlangıcı oradan alacaktır.
# print(os.path.isfile("Downloads/Fizik I_Bölüm_3.pdf")) --- Bu komutumuz ise bize bir şeyin klasör mü yoksa dosya mı olduğunu anlamamızı sağlar sonuç "TRUE" verirse bu bir dosyadır.
# Aynı mantık isfile yerine isdir yaparsakta bu bir klasör mü sorusunun cevabına ulaşırız.

# print(os.path.splitext("Downloads/Fizik I_Bölüm_3.pdf")) ---- Son olarak bu arkadaş ise splitext bize girdiğimiz dosyanın yerini ve uzantısını söyler.
