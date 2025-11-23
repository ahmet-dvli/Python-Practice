# Evet bu konumuzda ise değişkenlerin kapsama alanları (Scope) | local , enclosing , global , built-in , nonlocal
# Bir değişkeni kullanmadan önce kesinlikle tanımlamalıyız.

x = "global x" # Global = Bu değişken programın en dış katmanında tanımlandıgı için her katmanda geçerlidir.

def fonk():
    y = "local y" # Local = Bu değişken programın alt katmanlarından biri olan def fonk() ta tanımlanır.
    print(y)

#fonk()
#print(y) # Bakın bunu yazmaya calıstıgımızda bize hata vericek. Çünkü "y" bir fonk. içinde tanımlandıgı icin biz buna dışarıdan istedigimiz gibi direkt ulasamayız.

x = "global x"

def outer():
    x = "enclosing x" # İç içe fonksiyonlar varsa en içteki "local" olurken onun üstündeki "enclosing" onunda üstündeki "global" oluyor.
    print(x)
    def inner():
        x = "local x" # Mesela bunun başına "#" koyduk diyelim. Kalan her şey sabit duruyor. Çalıştırıp terminale baktıgımız zaman "local x" yerine "global x" yazıcak.
        print(x)
    inner()

outer() 
print(x)
# Terminalde yazma sırası tesadüf değildir.
# Baska bir örnege gecelim.

z = "global z"

def fonk2():
    # global z  (Buraya bunu yazarsak artık z eşittir 10 degeri oldu yani dıştaki ile içteki katman artık ikiside z=5 durumu söz konusudur.
    z = 10

fonk2()
print(z) # Bakın burda dış katmandaki z ile fonksiyonun içindeki z aynı DEĞİL.
# Baska bir örnege bakalım.

q = "global q"

def outer2():
    q = "enclosing q"
    print(q)
    def inner2():
        nonlocal q # Bunun anlamı ise bu fonksiyon için olusturulmus q değeri değilde bundan bir önceki fonksiyonun kullandıgı değeri alır. Bir önceki q değerini alır ve ona yazdıgımız sayı olan 15 değerini atar.
        q = 15
    inner2()
    print(q)
outer2()

# Built-in bunlar sum,max,len,lambda ----> Pythonda anlamı olan degerlerdir. Yani bir degisken olusturup sum = "x" yapamazsanız.