# Class
Class'lar, obje üretmemizi sağlayan data type'lardır. Class yapısı bizi, belli obje ve fonksiyon gruplarını her seferinde en baştan yazma zahmetinden kurtarır. Çünkü bir main class'dan, main class'ın bütün içeriğine sahip subclass'lar üreterek, main class'ın yeteneklerine sahip birçok yapıyı kolayca elde edebiliriz.

## Class Definition
`class <class_name>` statement kullanılarak class tanımlayabilirsiniz. Örnek:
```py
class Class():
    pass

class Class: # Class ile aynı şey.
    pass
```
VSC debugger ile yukarıdaki koda baktığımızda `Class` class'ının hafızada `__main__.Class` şeklinde tanımlandığını görürüz. Bunun anlamı şudur: Bulunduğunuz Python dosyasının adı, o dosyanın içindeyken `__main__`'dir. Bunu bulunduğunuz dosyada `print(__name__)` kodunu çalıştırarak görebilirsiniz. Python'da class'ların class attribute'lerini ifade ederken `class.attribute` şeklinde ifade ederiz. Python dosyamızı da bütünüyle bir class olarak düşünürsek, `Class`' class'ı da python dosyamızın (temsili olarak) bir attribute'si olarak düşünebiliriz. Bu yüzden bulunduğunuz Python dosyasının içindeki class `__main__.class_name` şeklinde ifade edilir. Bu class'dan oluşturulan `<__main__.class_name object at 0x0000022782837730>` gibi objelere de **instance** denir (object = instance = obje = nesne). `<__main__.class_name object at 0x0000022782837730>` bunun anlamı: `0x0000022782837730` bellek numaralı obje `__main__.class_name` class'ından türetilmiş bir instance'dir.

## Class Instantiation
Daha önce `class` statement ile tanımlanmış bir main class'dan (`__main__.class_name`), `<__main__.class_name object at 0x0000022782837730>` gibi objeler türetme işlemine **Instantiation** denir. Türetilen objeye ise **Instance** denir. Örnek:
```py
class Class(): # __main__.Class
    pass

Class() # <__main__.Class object at 0x0000022782837730>
```
Bu işlem, `def func():` gibi tanımladığımız bir fonksiyonu `func()` gibi çağırmaya (call) benzerdir. `Class()` ile oluşturulan instance, programın geri kalanında kullanılmak isterseniz, bu objeyi bir variable'a atayabilirsiniz. Böylece bu instance, programın run-time'ı (çalıştığı süre) boyunca bellekte kullanıma hazır bir şekilde depolanır. Ama `Class()` ile oluşturulan instance bir variable'da depolanmazsa, python bir sonraki satıra geçtiğinde bu instance bellekten silinir.

## Class Attributes
Class'ların içine, `__init__` ya da herhangi bir fonksiyonun kapsamının dışında tanımlanan, değer tutan/depolayan variable'lara **class attribute** denir. Örnek:
```py
class Class():
    attribute_1 = "Attribute 1"
    attribute_2 = ["Attribute 2"]
```
Buradaki `attribute_1` ve `attribute_2` variable'ları bir class attribute'dir.

Python'un class'ları okuma ve class'lara davranma şekli fonksiyonları okuma ve fonksiyonlara davranma şeklinden farklıdır.
- Python `def func():` şeklinde tanımladığınız fonksiyonu okuyup bu fonksiyonun objesini oluşturulduğunda, bu fonksiyonun objesinin içindeki variable'lara sadece o fonksiyon çağırıldığında ulaşılabilir. Çünkü python, ancak bu fonksiyon çağırıldığında bu fonksiyonun bulunduğu line'a gidip fonksiyonu çalıştırır ve içeriğini okur. Bu "içeriğini okuma" sürecindeki bütün variable'lar local variable'lardır ve fonksiyon çalışmayı sonlandırdığında bu local variable'lar bellekten silinir. Yani pyhon, bir fonksiyonla karşılaştığında sadece o fonksiyonun objesini oluşturur (create), içeriğini okumaz.
- Ama Class'larda içerik okunur. `class Class():` gibi bir class oluşturduğunuzda (create), python, programı yukarıdan aşağıya okurken, fonksiyonlardaki gibi class objesini yaratıp, class'ın içeriği okumayı atlamaz. Class'ın içeriğini de okur. Bu yüzden bu okuma işlemi sırasında class'ın içinde tanımlanmış variable'lar (class attribute) hafızada tutulur ve fonksiyonlar (`print()` gibi) okunduktan hemen sonra çalıştırılır. Örnek:
```py
# modul.py dosyası
class Class():
    attribute_1 = "Attribute 1"
    attribute_2 = ["Attribute 2"]
    print(attribute_1,attribute_2,sep="\n")
```
**Output:**
```
Attribute 1
['Attribute 2']
```
**Not:** Bu durum bu python dosyası import edildiğinde de yaşanır. Çünkü bu python dosyasını import ettiğinizde, python, o python dosyasını yukarıdan aşağı okumaya başlar ve yukarıda anlattığım olay yaşanır. Örnek:
```py
# main.py dosyası
import modul
```
**Output:**
```
Attribute 1
['Attribute 2']
```
**Not:** Bir modul dosyasındaki bir class'ı kullanmak için o modülü `import modul` şeklinde import ettikten sonra `modul.Class` şeklinde kullanabileceğiniz gibi `form modul import Class` şeklinde class'ı import edip class'ı `modul` prefix'i olmadan da kullanabilirsiniz. Örnek:
```py
# modul.py
class Class():
    print("modul.class çalıştı.")
    var = "modul.class.var çalıştı."
```
```py
# dosya_1.py
import modul # Output: modul.class çalıştı.
print(modul.Class().var) # Output: modul.class.var çalıştı.
```
```py
# dosya_2.py
from modul import Class # Output: modul.class çalıştı.
print(Class().var) # Output: modul.class.var çalıştı.
```
**Not:** Eğer python class'ın bloğunu okurken `print()` ile karşılaştığı için sizin kontrolünüz dışında ekrana bir şeyler bastırmasını istemiyorsanız pratik bir çözüm olarak bu class attribute'leri class'ın dışında bastırabilirsiniz. Bu sayede bu class attribute'leri bastırmak ya da bastırmamak sizin kontrolünüzde olur. Örnek:
```py
class Class():
    attribute_1 = "Attribute 1"
    attribute_2 = ["Attribute 2"]

print(Class.attribute_1,
      Class.attribute_2, sep="\n")
```
**Output:**
```
Attribute 1
['Attribute 2']
```
Instantiation işleminde, main class'ın şablonu kullanılarak türetilen instance'lar özelleştirilebilir. Yani içerdiği instance attribute'larin veya class attribute'larin değerleri değiştirilebilir. Örnek:
```py
class Class():
    attribute_1 = 1

instance_1 = Class()
instance_1.attribute_1 = 2
print(instance_1.attribute_1) # Output: 2
print(Class.attribute_1) # Output: 1
```
Main class'dan türetilmiş instance'larda bulunan class attribute'lerinin davranışları farklı olabilir. Class attribute'ler değiştirilemez (immutable (`bool`, `int`, `float`, `complex`, `tuple`, `frozenset` vb.)) data type'lar ise, bu class'dan türetilmiş farklı instance'larda bu değerleri değiştirmek için bu class attribute'ları yeniden tanımlamanız (redefinition) gerekmektedir. Zaten daha önce de öğrendiğiniz gibi, immutable bir data type'ın value'sini değiştirmenin tek yolu onu yeniden tanımlamaktır (redefinition).
```py
class Class():
    exp_attribute_1 = "String"
    exp_attribute_2 = 1
    exp_attribute_3 = 1.1234
    exp_attribute_4 = 5+5j
    exp_attribute_5 = tuple([1,2,3])
    exp_attribute_6 = frozenset([1,2,3])

a = Class()
b = Class()

b.exp_attribute_1 = "Değiştirilmiş String"
b.exp_attribute_2 = 9
b.exp_attribute_3 = 9.9876
b.exp_attribute_4 = 9+9j
b.exp_attribute_5 = tuple([9,8,7])
b.exp_attribute_6 = frozenset([6,5,4])

for i in dir(a):
    if "exp_attribute_" in i:
        eval(f"print('a.{i}:', a.{i}), id(i)")

print("-"*40)

for i in dir(b):
    if "exp_attribute_" in i:
        eval(f"print('b.{i}:', b.{i}), id(i)")
```
**Output:**
```
a.exp_attribute_1: String
a.exp_attribute_2: 1
a.exp_attribute_3: 1.1234
a.exp_attribute_4: (5+5j)
a.exp_attribute_5: (1, 2, 3)
a.exp_attribute_6: frozenset({1, 2, 3})
----------------------------------------
b.exp_attribute_1: Değiştirilmiş String
b.exp_attribute_2: 9
b.exp_attribute_3: 9.9876
b.exp_attribute_4: (9+9j)
b.exp_attribute_5: (9, 8, 7)
b.exp_attribute_6: frozenset({4, 5, 6})
```
Gördüğünüz gibi `b` variable'ına atanmış instance'nin immutable class attribute'larını yeniden tanımlayarak değiştirip main class'dan ve `a` variable'ına atanmış instance'dan farklı değerlere sahip bir şablon elde etmiş olduk.

Bir instance'daki class attribute'ları yeniden tanımladığımızda bu class attribute'lar, main class'daki class attribute'lar ve diğer instance'daki class attribute'lardan farklı bir objeye dönüşür (ID'si farklı olur). Örnek:
```py
class Class():
    a = 1

var1 = Class()
var2 = Class()
print("var1.a:    ", var1.a, "id:", id(var1.a))
print("var2.a:    ", var2.a, "id:", id(var2.a))
var1.a = 2
print("var1.a new:", var1.a, "id:", id(var1.a))
var2.a = 3
print("var2.a new:", var2.a, "id:", id(var2.a))
```
**Output:**
```
var1.a:     1 id: 1616316492080
var2.a:     1 id: 1616316492080
var1.a new: 2 id: 1616316492112
var2.a new: 3 id: 1616316492144
```
Gördüğünüz gibi `var1` ve `var2` instance'larinin ilk başta `a` class attribute'ünün ID'si aynıydı çünkü bu iki class attribute objesi de main class'ın class attribute'ünü işaret ediyordu. Sonra bu instance'ların class attribute'larını yeniden tanımlayınca (redefinition), bu instance'ların class attribute'ları main class'ın class attribute'undan farklı bir objeye dönüştü. Kanıt olarak bu instance'ların class attribute'larının son durumdaki (new) ID'lerine bakabilirsiniz.

Class attribute'ler değiştirilebilir (mutable (`list`, `set`, `dict` vb.)) data type'lar ise, bu class'dan türetilmiş farklı instance'lardaki class attribute'ların değerlerini değiştirmek için bu data type'ların methodları kullanılırsa, main class'dan türetilmiş instance'lerin class attribute objeleri, main class'daki class attribute'lere işaret edeceği (aynı ID'ye sahip olacağı) için bu değişiklik main class ve bütün bu main class'dan türetilmiş instance'larda geçerli olur. Örnek:
```py
class Class():
    exp_attribute_1 = [1,2,3]
    exp_attribute_2 = set([4,5,6])
    exp_attribute_3 = {"yedi":7, "sekiz":8, "dokuz":9}

a = Class()
b = Class()

b.exp_attribute_1.append("new_item")
b.exp_attribute_2.add("new_item")
b.exp_attribute_3.update({"new":"item"})

for i in dir(a):
    if "exp_attribute_" in i:
        eval(f"print('a.{i}:', a.{i})")
print("-"*69)
for i in dir(b):
    if "exp_attribute_" in i:
        eval(f"print('b.{i}:', b.{i})")
```
**Output:**
```
a.exp_attribute_1: [1, 2, 3, 'new_item']
a.exp_attribute_2: {4, 5, 6, 'new_item'}
a.exp_attribute_3: {'yedi': 7, 'sekiz': 8, 'dokuz': 9, 'new': 'item'}
---------------------------------------------------------------------
b.exp_attribute_1: [1, 2, 3, 'new_item']
b.exp_attribute_2: {4, 5, 6, 'new_item'}
b.exp_attribute_3: {'yedi': 7, 'sekiz': 8, 'dokuz': 9, 'new': 'item'}
```
Eğer immutable data type'lardaki gibi mutable data type class attribute'ları yeniden tanımlarsak (redefinition), bu sorun ortadan kalkar. Örnek:
```py
class Class():
    exp_attribute_1 = [1,2,3]
    exp_attribute_2 = set([4,5,6])
    exp_attribute_3 = {"yedi":7, "sekiz":8, "dokuz":9}

a = Class()
b = Class()

b.exp_attribute_1 = [1, 2, 3, 'new_item']
b.exp_attribute_2 = {4, 5, 6, 'new_item'}
b.exp_attribute_3 = {'yedi': 7, 'sekiz': 8, 'dokuz': 9, 'new': 'item'}

for i in dir(a):
    if "exp_attribute_" in i:
        eval(f"print('a.{i}:', a.{i})")
print("-"*69)
for i in dir(b):
    if "exp_attribute_" in i:
        eval(f"print('b.{i}:', b.{i})")
```
**Output:**
```
a.exp_attribute_1: [1, 2, 3]
a.exp_attribute_2: {4, 5, 6}
a.exp_attribute_3: {'yedi': 7, 'sekiz': 8, 'dokuz': 9}
---------------------------------------------------------------------
b.exp_attribute_1: [1, 2, 3, 'new_item']
b.exp_attribute_2: {5, 4, 'new_item', 6}
b.exp_attribute_3: {'yedi': 7, 'sekiz': 8, 'dokuz': 9, 'new': 'item'}
```

## Instance Attributes
**Instance Attribute**'lar ve **Class Attribute**'lar gibidir. Tek farkı bu attribute'lara sadece instance'lar ulaşabilir. Yani instance attribute'lara main class'dan direkt ulaşamazsın. Örnek:
```py
class Class():
    exp1 = 1
    def __init__(self):
        self.exp2 = 2

print(Class.exp1) # Output: 1
print(Class.exp2) # Output: AttributeError: type object 'Class' has no attribute 'exp2'
print(Class().exp1) # Output: 1
print(Class().exp2) # Output: 2
```
Dolayısıyla instance attribute'lar, instance'lara özel attribute'lardır diyebiliriz.

### `__init__` Fonksiyonu ve `self`
`__init__`, class'lara özgü bir fonksiyondur. `__init__` fonksiyonunun görevi, main class'dan instance oluşturulurken, instance için oluşturulacak instance attribute'leri (`self.a` gibi) ve işlevleri (`print()` gibi) tanımlamaktır. `__init__` fonksiyonu, main class'dan instance türetildiği anda çalışır. Başka bir deyişle, main class'dan instance türetilmeden önce main class okunurken, `__init__` fonksiyonunu okumaya sıra gelince python sadece `def __init__(self):` kısmını okuyup `__init__` fonksiyon objesini oluşturur. Dolayısıyla python bu sırada `__init__` fonksiyonunu çalıştırmaz ve içeriğini okumaz. Örnek:
```py
class Class():
    def __init__(self):
        self.check = "Class() ile instance oluşturulduğu anda __init__ Çalıştı." # instance attribute

print(Class.check) # AttributeError: type object 'Class' has no attribute 'check'
var = Class() 
print(var.check) # Output: Class() ile instance oluşturulduğu anda __init__ Çalıştı.
```
Gördüğünüz gibi `var = Class()` kodundaki gibi bir instance oluşturulmadan önce `__init__` fonksiyonu çalıştırılmadığı ve içeriği okunmadığı için `Class` main class objesi direkt `__init__` fonksiyonu içindeki `check` instance attribute'una ulaşamadı. Instance objesi oluşturulduktan sonra `print(Class.check)` kodunu çalıştırsak bile aynı hatayı alırdık çünkü `self.check` instance attribute'ü sadece instance'lere özeldir, sadece instance'lar ulaşabilir. Kanıtı:
```py
class Class():
    def __init__(self):
        self.check = "Class() ile instance oluşturulduğu anda __init__ Çalıştı." # instance attribute


var = Class() 
print(Class.check) # AttributeError: type object 'Class' has no attribute 'check'
print(var.check) # Output: Class() ile instance oluşturulduğu anda __init__ Çalıştı.
```
Bir main class içerisinde sadece instance'lerin ulaşabildiği `__init__` fonksiyonunun kapsamında veya user-defined (kullanıcı tanımlı) fonksiyonunun kapsamında bir işlem (örneğin `print()` gibi bir fonksiyon) tanımlarsak, program başlatıldığında python'un main class'ın içeriğini okurken karşılaştığı `print()` fonksiyonlarını çalıştırması gibi, main class'dan bir instance oluşturulduğu için `__init__` fonksiyonu çalıştırıldığında da python karşılaştığı işlemleri (örneğin `print()` gibi bir fonksiyon) çalıştırır. Örnek:
```py
class Class():
    def __init__(self):
        self.check = "Class() ile instance oluşturulduğu anda __init__ Çalıştı." # instance attribute
        print(self.check) # işlev

var = Class() # Output: Class() ile instance oluşturulduğu anda __init__ Çalıştı.
```
Yukarıdaki kodda, `var = Class()` kodu ile main class'dan bir instance türetildiğinde `__init__` fonksiyonu çalıştığı için `__init__` fonksiyonunun içeriği okunuyor ve bu sırada python `print(self.check)` kodu ile karşılaşıp, bu kodu çalıştırıp, ekrana `Class() ile instance oluşturulduğu anda __init__ Çalıştı.` bastırılıyor.

**Not:** Bir main class'dan her instance türetildiğinde, türetilen instance, kendine özel bir `__init__` fonksiyon objesine ve user-defined (kullanıcı tanımlı) fonksiyon objelerine sahip olur. Bu sayede herhangi bir çakışmaya maruz kalmadan yeniden tanımlama (redefinition) ya da aynı obje üzerinde işlem yapmaya (`Class().attribute.append` gibi) izin verir.

Main class'dan türetilmiş bir instance'dan bir attribute talep ettiğinizde, python main class içinde o attribute'ü önce instance attribute olarak arar, bulamazsa class attribute olarak arar, yine bulamazsa hata verir. Örnek:
 ```py
class Class1():
    a = 1
    def __init__(self):
        self.a = 2

class Class2():
    a = 1
    def __init__(self):
        a = 2

class Class3():
    pass
    def __init__(self):
        pass

print(Class1().a) # Output: 2
print(Class2().a) # Output: 1
print(Class3().a) # Output: AttributeError: 'Class3' object has no attribute 'a'
```
Eğer class ve instance attribute'lerinin isimleri aynıysa ve siz spesifik olarak class attribute'e erişmek istiyorsanız, bu class attribute'ü direkt main class objesinden talep edin. Örnek:
```py
class Class1():
    a = 1
    def __init__(self):
        self.a = 2

print(Class1().a) # Output: 2
print(Class1.a) # Output: 1
```
`__init__` fonksiyonunun ilk parametresine her instance attribute'leri temsil edecek parametre tanımlanır çünkü bu bir syntax kuralıdır. Bu parametre herhangi bir şey olabilir ama `self`, programcılar camiasında kalıplaşmış bir kullanım olduğu için tercih edilmelidir. Örnek:
```py
class Class1():
    def __init__(self):
        self.a = "Class1.a"

class Class2():
    def __init__(parametre):
        parametre.a = "Class2.a"

class Class3():
    def __init__(at_arabasi):
        at_arabasi.a = "Class3.a"

print(Class1().a) # Output: Class1.a
print(Class2().a) # Output: Class2.a
print(Class3().a) # Output: Class3.a
```
`self` kelimesinin, class'ın kapsamındaki `__init__` ve bütün user-defined (kullanıcı tanımlı) fonksiyonların ilk parametresinde kullanılmak zorunda olan, instance attribute'leri işaret eden bir prefix'dir. Yani bir main class'ın içinde instace attribute tanımlayacağınız zaman, her zaman `self` prefix'ini kullanmak zorundasınız. Kısaca `self = instace attribute`. Örnek:
```py
class Class1():
    a = 1
    def __init__(self):
        self.a
exp = Class1()
print("Class1.a:    ", Class1.a, " id:", id(Class1.a))
print("exp.a:       ", exp.a, " id:", id(exp.a))
exp.a = 2
print("exp.a new:   ", exp.a, " id:", id(exp.a))
```
**Output:**
```
Class1.a:     1  id: 2267102406960
exp.a:        1  id: 2267102406960
exp.a new:    2  id: 2267102406992
```
Gördüğünüz gibi en başta `self.a` instance attribute'sine değer atamamış olsak bile, main class'un `a` class attribute'si ile `exp` instance'sinin `self.a` instance attribute'sinin değerlerinin ve ID'lerinin aynı olduğunu görüyoruz. Buradan yola çıkarak, `self.a` instance attribute'si `a` class attribute'sine referanstır diyebiliriz. Başka bir örnek:
```py
class Class():
    liste = []
    def __init__(self):
        self.liste.append("F")

print(Class.liste) # Output: []
exp = Class()
print(Class.liste) # Output: ['F']
print(exp.liste) # Output: ['F']
```
Gördüğünüz gibi `self.liste` instance attribute'ü, `liste` class attribute'üne referans olduğu için `liste` class attribute'üne hata almadan `append` methodunu uygulayabildik. Burada dikkat edilmesi gereken şey, ilk başda `Class` class'ının `liste` class attribute'ü boşken, `exp = Class()` kodu ile instantiation işlemi yaptıktan sonra `__init__` fonksiyonu çalıştırıldığı için `self.liste.append("F")` kodu da çalıştı ve bellekte bulunan `__main__.Class` objesine etki ederek, class attribute olan `liste`'nin değerini değiştirdi. Bu yüzden `exp = Class()` işleminden sonra `print(Class.liste)` kodu boş liste yerine `['F']` listesini döndürüyor (yani `liste` ile eski `liste` aynı id'ye sahip, sadece içeriği değişti).

`self` kelimesinin instance attribute'lara özel bir prefix olduğunu söylemiştik. Dolayısıyla `self` kelimdesini class attribute tanımlarken prefix olarak kullanamazsınız. Aynı zamanda `self` kelimesini, class methodlarının ilk parametresinde kullandığınız gibi class objesinin de ilk parametresine yazarsanız yine `NameError: name 'self' is not defined` hatası alırsınız. Kısaca `self` kelimesi, instance attribute'lara özel bir prefix'dir, class attribute prefix'i olarak kullanılamaz. Örnek:
```py
class Class1(self): # NameError: name 'self' is not defined
    self.a = 1 # NameError: name 'self' is not defined
    def __init__(self):
        self.a = 2
```
Instance attribute'ların diğer önemli özelliği, instance attribute'lara yaptığınız herhangi bir müdahele sadece ilgili instace'yi etkileyecektir. Bunun sebebi, main class'dan oluşturulan her instance'nin instance attribute'ları, diğer instance'ların instance attribute'larından farklı bir obje (ID'leri farklı) olmasıdır. Yani class attribute'lardaki gibi çakışmalar yaşanmadığı gibi instance attribute'larda yeniden tanımlama (redefinition) yapmak zorunda değilsiniz. Örnek:
```py
class Class():
    def __init__(self):
        self.liste = []
        self.sayi = 1

exp1 = Class()
exp2 = Class()

print("exp1.liste:    ", exp1.liste, "   | id:", id(exp1.liste))
print("exp2.liste:    ", exp2.liste, "   | id:", id(exp2.liste))
exp1.liste.append("F")
print("exp1.liste new:", exp1.liste, "| id:", id(exp1.liste), end="\n\n")

print("exp1.sayi:     ", exp1.sayi, "| id:", id(exp1.sayi))
print("exp2.sayi:     ", exp2.sayi, "| id:", id(exp2.sayi))
exp1.sayi = 2
print("exp1.sayi new: ", exp1.sayi, "| id:", id(exp1.sayi))
```
**Output:**
```
exp1.liste:     []    | id: 1433189451072
exp2.liste:     []    | id: 1433189465536
exp1.liste new: ['F'] | id: 1433189451072

exp1.sayi:      1 | id: 1433183545648
exp2.sayi:      1 | id: 1433183545648
exp1.sayi new:  2 | id: 1433183545680
```
Gördüğünüz gibi `exp1.liste` ile `exp2.liste` liste en başta farklı instance attribute objesi (ID'leri farklı) olduğu için class attribute'lardaki gibi çakışma yaşanmadı. 

`self` kelimesinin instance attribute'lara özel bir prefix olduğunu ve `self` kullanılmadan instance attribute tanımlanamayacağını söylemiştik. Main class içindeki `__init__` fonksiyonunun veya user-defined (kullanıcı tanımlı) fonksiyonların içinde tanımladığınız bütün variable'lar instance attribute olarak (yani `self` prefix'i ile) tanımlanmak zorunda değildir. Örnek:
```py
class Class():
    def __init__(self):
        sayi_1 = 4
        sayi_2 = 5
        self.sayi_3 = sayi_1 + sayi_2

print(Class().sayi_1) # Output: AttributeError: 'Class' object has no attribute 'sayi_1'
print(Class().sayi_2) # Output: AttributeError: 'Class' object has no attribute 'sayi_2'
print(Class().sayi_3) # Output: 3
```
Gördüğünüz gibi `sayi_1` ve `sayi_2` variable'larının başına `self` prefix'i getirmediğimiz için python bunları bir instance attribute olarak kabul etmiyor ve bu yüzden variable'lara `Class().sayi_1` ve `Class().sayi_2` şeklinde ulaşamıyoruz , hata veriyor. Ama bu variable'ları isteğe ve duruma göre `__init__` fonksiyonunun veya user-defined (kullanıcı tanımlı) fonksiyonların içinde kullanabiliriz.

### Instance Methods
Bir main class'a, `__init__` fonksiyonu dışında çeşitli user-defined (kullanıcı tanımlı) fonksiyonlar tanımlayabiliriz. Bu tanımlanan user-defined (kullanıcı tanımlı) fonksiyonlara **Instance Methods** denir. Örnek:
```py
class Class():
    def __init__(self):
        print("__init__ Çalıştı...")

    def a_yazdir(self):
        print("a_yazdir() Çalıştı...")

    def b_yazdir(self):
        print("b_yazdir() Çalıştı...")

    def c_yazdir(self):
        print("c_yazdir() Çalıştı...")

var = Class() # Output: __init__ Çalıştı...
var.a_yazdir() # Output: a_yazdir() Çalıştı...
var.b_yazdir() # Output: b_yazdir() Çalıştı...
var.c_yazdir() # Output: c_yazdir() Çalıştı...
```
**Not:** Instance method'lara class method denmemesinin sebebi, bu methodları `__main__.Class` objesiyle beraber **bu şekilde** doğrudan kullanamazsınız. Örnek:
```py
class Class():
    def __init__(self):
        print("__init__ Çalıştı...")

    def a_yazdir(self):
        print("a_yazdir() Çalıştı...")

Class.a_yazdir() # TypeError: a_yazdir() missing 1 required positional argument: 'self'
```
"**bu şekilde** doğrudan kullanamazsınız." dememin sebebi, main class'ı aşağıdaki gibi oluşturursanız `Class.a_yazdir()` çalışır.
```py
class Class():
    def __init__(self):
        print("__init__ Çalıştı...")
    @staticmethod
    def a_yazdir():
        print("a_yazdir() Çalıştı...")

Class.a_yazdir()
```
Buradaki `@staticmethod` daha sonra açıklanacaktır.

Normal şartlarda, global scope'da tanımlanmış iki fonksiyon, global scope'daki variable'lara erişebilir ama birbirinin local variable'larına erişemez. Çünkü bu local variable'lar adı üstünde local variable oldukları için o fonksiyon çalıştırıldığında python bu local variable'ları okuyup bellekte depolar ve fonksiyon sonlandığında silinirler. Örnek:
```py
def func1():
    a = "local a"
    print(a) # Output: local a
    print(b) # Output: NameError: name 'b' is not defined

def func2():
    b = "local b"
    print(a) # Output: NameError: name 'a' is not defined
    print(b) # Output: local b
```
Ama class'larda tanımlanan `__init__` fonksiyonu bu kuralı yıkıyor. Çünkü `__init__` fonksiyonu içinde tanımlanan instance attribute'lara, main class'ın içindeki **her yerden** erişilebilir. Örnek:
```py
class Class():
    def __init__(self):
        print("__init__ Çalıştı...")
        self.a = "self.a"
        self.b = []
        self.c = 100

    def a_yazdir(self):
        self.a = "new self.a"
        print(self.a)

    def b_yazdir(self):
        self.b.append("new self.b")
        print(self.b)

    def c_yazdir(self):
        self.c += 50
        print(self.c)

var = Class() # Output: __init__ Çalıştı...
var.a_yazdir() # Output: new self.a
var.b_yazdir() # Output: ['new self.b']
var.c_yazdir() # Output: 150
```

######## `__init__` de user-defined func tanımlamayı falan yazacaksın.