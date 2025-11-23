# Bu konumuzda ise gayet anlaşılabilir olan zip fonskiyonunu öğreticem.
# Temel anlamda birden fazla listenin elemanları birbirleriyle eşleştiriyor.

Kitap_Baslık_Sayfaları = [1,22,65,99,125]
Kitap_Baslıkları = ["Peri","Soyağaç","Kader","Yaklaşım","Ölüm"]
Kitap_Baslık_Kelime_Sayısı = [432,443,543,512,321]

Sonuc = zip(Kitap_Baslık_Sayfaları,Kitap_Baslıkları,Kitap_Baslık_Kelime_Sayısı)
print(list(Sonuc)) # ! Burda "list" - tupple ,set gibi bunlarda olur. - ile yazdık yoksa burda beklediğimiz sonucu alamayız.
