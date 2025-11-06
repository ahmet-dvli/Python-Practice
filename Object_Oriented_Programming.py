# Nesne yönelimli programlamaya giriş
# Class oluşturma
# Özellik ve metotlar(attributes and methods)
# ınstance = herhangi bir "class"tan üretilen bir örnektir.
 

class çalışan:
    def __init__(self,name,surname,age): # Buradaki "__init__" başlat gibi anlama gelir.
        self.name = name # Kendi anlamına gelir ve print te yazarken yazmamıza gerek yok.
        self.surname = surname
        self.age = age
    def show_info(self): # Bu ise dahada bilgilendirilmek amacıyla yapılır.Çalışanın "adı" "soyadı" "yaşı" gibi şeylerde yazılarak sonuçlar gösterilir.
        print(f"İsim: {self.name} Soyad: {self.surname}  Yaş: {self.age}")

çalışan1 = çalışan("Ahmet","Yılmaz","21")
print(çalışan1.name,çalışan1.surname,çalışan1.age)

çalışan2 = çalışan("Mehmet","Güneş","45")
print(çalışan2.name,çalışan2.surname,çalışan2.age)

çalışan1.show_info()
çalışan2.show_info()

# NOT: Eğer "age" diye bir kısım olup orayı boş bırakırsanız hata vericek ama en yukarıda def __init__("") olan yere "age=0" yazarsanız yaş girilmediği için "0" olarak alıcaktır.Yani hata vermicektir.

