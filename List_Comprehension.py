# Bu konumuzda ise elimizde var olan bir listeyle belirli kurallar kullanarak yeni bir liste oluşturacaz.

sayılar = [1,2,3,4,5,6,7,8,9]
#liste2 = []
#for sayı in sayılar:
#  liste2.append(sayı*sayı)
#print(liste2)

# ! Bu yukarıdaki gördüğümüz gibi eskiden yaptığımız bir şeyken alttaki ise tek bir satırda yazıldığını görebiliyoruz.

#liste3 = [sayı*sayı for sayı in sayılar]
#print(liste3)
# Evet test ederseniz göreceksiniz ki bu komut formatındada aynı sonucları alacaksınız ama tabiki bu daha kısa ve daha düzenli.


#liste2 = []
#for sayı in sayılar:
    #if sayı %2 == 0:   #(2 ye tam bölünme demek)
        #liste2.append(sayı)
#print(liste2)

# ! Bu yukarıdaki yine eski olan.



#liste3 = [sayı for sayı in sayılar if sayı %2 == 0]
#print(liste3)
 # Burda ise yeni olan yazıyor.Dikkat burda ikinci kısma koşul ekledik "if" koşulu burdanda aslında koşul olursa ikinci yere ekleriz sonucu ortaya çıkıyor.


#liste2 = []
#for sayı in sayılar:
    #if sayı %2 == 0:
        #liste2.append(sayı*sayı)
#print(liste2)

# ! Bu yukarıdaki eski.



#liste3 = [sayı*sayı for sayı in sayılar if sayı %2 == 0]
#print(liste3)
 # Burda ise yeni olan yazıyor.Sayı * sayı başa yazdık sonra gerisi klasik ve sondada koşlumuzu ekledik.


#liste2 = []
#for sayı in sayılar:
    #if sayı > 4 and sayı %2 == 0:
        #liste2.append(sayı **2)
#print(liste2)
 
# ! Bu yukarıdaki eski


#liste3 = [sayı * sayı for sayı in sayılar if sayı > 4 and sayı %2 == 0]
#print(liste3)


sayılar2 = [1,2,3,4]
harfler = "abcd"

#liste2 = []
#for sayı in sayılar2:
    #for harf in harfler:
        #liste2.append((sayı,harf))
#print(liste2)

# ! Yukarıdaki eski.


#liste2 = [(sayı,harf) for sayı in sayılar2 for harf in harfler]
#print(liste2)
 # Burda gördüğümüz "sayı" ve "harf" bir tuple olduğu için onları ayrı bir parantez içinde yazdık.


liste1 = [1,2,3,4,5,6,7,8]
liste2 = [2,3,4,5]
#liste3 = []
#for i in liste1:
    #if i not in liste2:
        #liste3.append(i * i)
#print(liste3)
 # Yukarıdaki eski.


#liste3 = [i * i for i in liste1 if not i in liste2]
#print(liste3)
 # Burda ise gördüğünüz gibi yenisi olan.

liste_ = [[1,2,3],[4,5,6,7],[8,9,10,11,12]]
#liste2_ = []
#for i in liste_:
    #for j in i:
        #liste2_.append(j)
#print(liste2_)
 # Bu eskisi olup burda aslında yukarıdaki listeleri tek bir liste yapmayı gösterdik burda i= listeler olup j ise listelerdeki sayıları temsil eder.


#liste2_ = [j for i in liste_ for j in i]
#print(liste2_)
 # Bu ise yenisi olup burda mesela en başa "j for j in i" yazarsak hata verir.Önce bunu tanımlamak için "for i in liste2_" yazıp for a geçtik.



