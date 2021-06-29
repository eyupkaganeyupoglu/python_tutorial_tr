# Class
Class'lar, obje üretmemizi sağlayan data type'lardır. Class yapısı bizi, belli obje ve fonksiyon gruplarını her seferinde en baştan yazma zahmetinden kurtarır. Çünkü bir main class'dan, main class'ın bütün içeriğine sahip subclass'lar üreterek, main class'ın yeteneklerine sahip birçok yapıyı kolayca elde edebiliriz.

## Class Definition
`class <class_name>` statement kullanılarak class tanımlayabilirsiniz. Örnek:
```py
class Exp_Class():
    pass

class Exp_Class_2: # Exp_Class ile aynı şey.
    pass
```
Tanımladığımız bu class'a debugger ile bakarsak `__main__.Exp_Class` şeklinde olduğunu farkedeceğiz. Bunun anlamı şudur: Python dosyasının adı `__main__`'dir. Python'da class'ların attribute'lerini ifade ederken `class.attribute` şeklinde ifade ederiz. Python dosyamızı da bütünüyle bir class olarak düşünürsek, `Exp_Class`'de python dosyamızın bir attribute'si olur. Bu yüzden bir python dosyasının içindeki class `__main__.class_name` şeklinde ifade edilir. Bu class'dan oluşturulan instance'lar `<__main__.class_name object at 0x0000022782837730>` şeklinde ifade edilir. Bunun anlamı: `0x0000022782837730` bellek numaralı obje `__main__.class_name` class'ından oluşturulmuş bir objedir.

## Class Attributes
Class'ların içine tanımlanan, değer tutan/depolayan yapılara **class attribute** denir.
```py
class Exp_Class():
    attri_1 = "Attribute 1"
    attri_2 = ["Attribute 2"]
```
Class'lar fonksiyonlara benzerdir ama en önemli farklarından birisi, bir fonksiyonun çalışabilmesi için o fonksiyonu çağırmamız gerekmektedir. Ama class'ları çağırmasak bile içindekileri çalıştırır. Çünkü python kodu yukarıdan aşağıya okurken `class Exp_Class():` satırının altındaki `print(attri_1,attri_2,sep="\n")` kodunu gördüğünda bu `print` fonksiyonunu çalıştırır. Örnek:
```py
# modul.py dosyası
class Exp_Class():
    attribute_1 = "Attribute 1"
    attribute_2 = ["Attribute 2"]

    print(attribute_1,attribute_2,sep="\n")
```
**Output:**
```
Attribute 1
['Attribute 2']
```
**Not:** Bu durum bu python dosyası import edildiğinde de yaşanır. Örnek:
```py
import modul
```
**Output:**
```
Attribute 1
['Attribute 2']
```
Eğer class'ın attribute'lerinin, class okunurken ekrana bastırılmasını istemiyorsanız, bu class attribute'leri method gibi çağırarak kullanabilirsiniz. Örnek:
```py
class Exp_Class():
    attribute_1 = "Attribute 1"
    attribute_2 = ["Attribute 2"]

print(Exp_Class.attribute_1,
      Exp_Class.attribute_2,sep="\n")
```
**Output:**
```
Attribute 1
['Attribute 2']
```
**Not:** Bir modul dosyasındaki bir class'ı kullanmak için o modülü `import modul` şeklinde import ettikten sonra `modul.Class` şeklinde kullanabileceğiniz gibi `form modul import Class` şeklinde class'ı import edip class'ı modul prefix'i olmadan da kullanabilirsiniz. Örnek:
```py
# modul.py
class Class():
    print("modul.class çalıştı.")
```
```py
# dosya_1.py
import modul
modul.Class() # Output: modul.class çalıştı.
```
```py
# dosya_2.py
from modul import Class
Class() # Output: modul.class çalıştı.
```

## Class Instantiation
`class` statement ile tanımlanmış bir class'ı bir variable'a atadığın zaman, bu işleme **instantiation**, class'ı atadığınız variable'a **instance** denir. Bu işlem fonksiyonlardaki **call** `çağırma` işlemi gibidir. Fonksiyonlardaki gibi class'ları da çağırdığımızda, o class'ın özelliklerini taşıyan farklı bir class objesi oluşur. Ana class'dan türetilen bu yeni class'ların attribute'lerine yeni değerler atanarak özelleştirilebilir. Zaten class'ların en büyük artısı budur, ana şablondan özelleştirilebilir yeni objeler yaratmak ve bu sayede bizi aynı şeyi tekrar tekrar yazmaktan kurtarmak.

**Dikkat:** Main Class'dan üretilmiş **instance**'larda bulunan class attribute'lerinin davranışları farklı olabilir. Bu class attribute'ler değiştirilemez (immutable (`bool`, `int`, `float`, `complex`, `tuple`, `frozenset`)) data type'lar ise, bu class attribute'lere bir veri atamak istediğimizde bu class attribute'leri yeniden tanımlamamız (definition) gerekmektedir. Çünkü bunlar değiştirilemez (immutable) data type'lardır. Yani:
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
        eval(f"print('a.{i}:', a.{i})")
print("--------------------------------------")
for i in dir(b):
    if "exp_attribute_" in i:
        eval(f"print('b.{i}:', b.{i})")
```
**Output:**
```
a.exp_attribute_1: String
a.exp_attribute_2: 1
a.exp_attribute_3: 1.1234
a.exp_attribute_4: (5+5j)
a.exp_attribute_5: (1, 2, 3)
a.exp_attribute_6: frozenset({1, 2, 3})
--------------------------------------
b.exp_attribute_1: Değiştirilmiş String
b.exp_attribute_2: 9
b.exp_attribute_3: 9.9876
b.exp_attribute_4: (9+9j)
b.exp_attribute_5: (9, 8, 7)
b.exp_attribute_6: frozenset({4, 5, 6})
```
Gördüğünüz gibi `b` instance'ının class attribute'lerini yeniden tanımlayarak `b` instance'larının içeriğini değiştirmiş olduk. Ama benzer şeyi değiştirilebilir (mutable (`list`, `set`, `dict`)) data type'larda yaparsak, bu eylemin diğer instance'leri de etkileme olasılığı var. Örnek:
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
print("-----------------------------------------------------")
for i in dir(b):
    if "exp_attribute_" in i:
        eval(f"print('b.{i}:', b.{i})")
```
**Output:**
```
a.exp_attribute_1: [1, 2, 3, 'new_item']
a.exp_attribute_2: {'new_item', 4, 5, 6}
a.exp_attribute_3: {'yedi': 7, 'sekiz': 8, 'dokuz': 9, 'new': 'item'}
-----------------------------------------------------
b.exp_attribute_1: [1, 2, 3, 'new_item']
b.exp_attribute_2: {'new_item', 4, 5, 6}
b.exp_attribute_3: {'yedi': 7, 'sekiz': 8, 'dokuz': 9, 'new': 'item'}
```
Gördüğünüz gibi methodlarla class attribute'lerde yaptığımız değişiklikler diğer instance'ları da etkileri. Bu yüzden aynı değiştirilemez (immutable) data type'larda yaptığımız gibi, değiştirilebilir (mutable) data type'larda da atama işlemi yapmalıyız. Yani:
```py
class Class():
    exp_attribute_1 = [1,2,3]
    exp_attribute_2 = set([4,5,6])
    exp_attribute_3 = {"yedi":7, "sekiz":8, "dokuz":9}

a = Class()
b = Class()

b.exp_attribute_1 = [4,5,6]
b.exp_attribute_2 = set([7,8,9])
b.exp_attribute_3 = {"altı":6, "beş":5, "dört":4}


for i in dir(a):
    if "exp_attribute_" in i:
        eval(f"print('a.{i}:', a.{i})")
print("-----------------------------------------------------")
for i in dir(b):
    if "exp_attribute_" in i:
        eval(f"print('b.{i}:', b.{i})")
```
**Output:**
```
a.exp_attribute_1: [1, 2, 3]
a.exp_attribute_2: {4, 5, 6}
a.exp_attribute_3: {'yedi': 7, 'sekiz': 8, 'dokuz': 9}
-----------------------------------------------------
b.exp_attribute_1: [4, 5, 6]
b.exp_attribute_2: {8, 9, 7}
b.exp_attribute_3: {'altı': 6, 'beş': 5, 'dört': 4}
```

## Instance Attributes
**Instance Attribute**'ları, **Class Attribute**'ları birbiri ile farklı ama alakalı şeylerdir.

### `__init__` Fonksiyonu ve `self`
`__init__`, class'lara özgü bir fonksiyondur ve main class'dan instance oluşturulduğu anda çalışır. Örnek:
```py
class Class():
    def __init__(self):
        self.check = "__init__ Çalıştı."
        print(self.check)
var = Class() # Output: __init__ Çalıştı.
```
Görevi, main class'dan instance oluşturulurken, oluşturulacak instance attribute'leri ve işlemleri tanımlamaktır. `__init__` fonksiyonunun ilk parametresi her instance attribute'leri temsil etmektedir çünkü bu bir syntax kuralıdır. `__init__` fonksiyonunun ilk parametresine yazılan `self`, instance attribute'leri temsil eder. Yani bir instance için instance attribute tanımlamak istiyorsanız, `__init__` block'una o attribute'yi `self` prefix'i ile tanımlamanız gerekmektedir. Bu attribute daha önce class attribute olarak tanımlanmış olsa bile `__init__` içinde kullanabilmek için `self`ile tanımlamalısınız. Örnek:
```py
class Class():
    xxx = []
    def __init__(self):
        a = 1
        b = 2
        self.c = a+b
        self.xxx.append("exp1")

print(Class().a) # Output: AttributeError: 'Class' object has no attribute 'a'
print(Class().b) # Output: AttributeError: 'Class' object has no attribute 'b'
print(Class().c) # Output: 3
print(Class().xxx) # Output: ['exp1']
```
Gördüğünüz gibi `xxx` attribute'sini bir instance'de kullanabilmek için `__init__` içinde `self` prefix'i ile kullandık. Buradan anlamamız gereken şey, Bir instance'de kullanmak istediğimiz bütün attribute'leri `self` ile tanımlamak zorundayız. Bu `__init__` gibi main class'da tanımlanmış bütün fonksiyonlar için geçerli. `__init__` gibi bütün fonksiyonların içindeki attribute'leri instance'de kullanabilmek için bu fonksiyonların ilk parametresini `self` yapıp, bloğundaki attributeleri `self` prefix'i ile tanımlamalıyız. Yani `self = instace attribute`. Örnek:
```py
class Class():
    class_attribute = "Class Attribute"

    def __init__(self):
        self.class_attribute = "__init__ Instance Attribute"

    def func1(self):
        self.class_attribute = "func1 Instance Attribute"
        print(self.class_attribute, end="\n\n")
    
    def func2(self):
        self.class_attribute = "func2 Instance Attribute"
        print(self.class_attribute)

print(Class.class_attribute, "\n")
print(Class().class_attribute, "\n")
Class().func1()
Class().func2()
```
**Output:**
```
Class Attribute 

__init__ Instance Attribute

func1 Instance Attribute

func2 Instance Attribute
```
Eğer `print(self.class_attribute)`'lar olmasaydı, methodların içindeki attribute'lere ulaşmak için 2 yöntem var:
```py
class Class:
    def __init__(self):
        self.a = 1
        self.func()
        print(self.b)    
    def func(self):
        self.b = self.a
var = Class() # Output: 1
```
```py
class Class:
    def __init__(self):
        self.a = 1 
    def func(self):
        self.b = self.a
var = Class()
var.func()
print(var.b) # Output: 1
```
Python `Class().a` kodunda, `Class()` kodu ile oluşturulmuş instance'den istenilen `a` instance attribute'e ulaşmak için şu yolu izler: Önce `__init__` içine bakar. `__init__` içinde bulamazsa class attribute'lere bakar. Yine bulamazsa hata verir. Kanıtı:
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
Direkt class attribute'e erişmek isterseniz, bu attribute'u direkt class'ın kendisinden çağırın:
```py
class Class1():
    a = 1
    def __init__(self):
        self.a = 2

print(Class1().a) # Output: 2
print(Class1.a) # Output: 1
```
Ayrıca `self` prefix'ini `__init__` dışında kullanamazsınız. Çünkü bu prefix `__init__`'e özgüdür. Kullanmaya çalışırsanız `NameError: name 'self' is not defined` hatası alırsınız. Çünkü `self`'i tanımlamamışsınızdır. `class Class1(self)` şeklinde de kullanırsanız aynı hatayı verir. Tanımlamaya uğraşırsanız kullanırsınız da kim uğraşacak? Oyunu kuralına göre oynayın.
```py
class Class1(self): # NameError: name 'self' is not defined
    self.a = 1 # NameError: name 'self' is not defined
    def __init__(self):
        self.a = 2
```
**Not:** `self` yerine istediğiniz herhangi bir şey kullanabilirsiniz. Buradaki önemli olan şey, `__init__` fonksiyonuna tanımlanan ilk parametrenin instance attribute'leri temsil etmesidir. Örnek:
```py
class Class():
    def __init__(a,b=1,c=2):
        a.toplam = b + c

print(Class().toplam) # Output: 3
```
**Dikkat:** Böyle bir özgürlüğünüz olsa bile `self` kullanmayı tercih edin. Çünkü `self` kullanmak ciddi derecede yaygındır.


Bir main class içine aşağıdaki gibi class attribute tanımlarsak, python kodları yukarıdan aşağıya doğru okurkan `class Class():` satırının altındaki `print` fonksiyonu ile karşılaştığında bu `print` fonksiyonunu direkt çalışır.
```py
class Class():
    exp_1 = 1
    exp_2 = 2
    exp_3 = 3
    print(exp_1, exp_2, exp_3) # Output: 1 2 3
```
Ama bu class attribute'ler ve işlemler `__init__` fonksiyonu içerisinde belirtilirse, `print` fonksiyonunun çağrılması için main class'dan bir instance üreterek (yani `Class()` class instance'sini bir variable'a atayarak) ya da direkt `Class()` ile tek kullanımlık bir class instance üreterek `Class()`'ın çalışmasını sağlamanız yeterlidir. Çünkü `__init__` içindeki `self` ile kullanılan attribute'ler main class'ın değil, instance class'ın attribute'leridir. Bu yüzden bunlara **Instance Attribute** denir. Örnek:
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
Gördüğünüz gibi `exp2` instance attribute olduğu için main class olan `Class`, bu attribute'e ulaşamıyor ama `Class()` ile üretilen tek kullanımlık instance `exp1` class attribute'üne ve `exp2` instance attribute'üne ulaşabiliyor. Benzer şekilde `__init__` içine tanımlanan `print` fonksiyonlar da her `Class()` kodu ile main class'dan tek kullanımlık instance oluşturulduğunda çalışır. Örnek:
```py
class Class():
    print("init dışı,", end=" ") # Output: init dışı, 
    def __init__(self):
        print("init içi,", end=" ")
        
Class() # Output: init içi,
Class() # Output: init içi,
Class() # Output: init içi,
```
**Output:**
```
init dışı, init içi, init içi, init içi, 
```
Yukarıda kod yukarıdan aşağı okunurken python `class Class():` satırının altındaki `print("init dışı,", end=" ")` çalışır. Daha sonra `def __init__(self):` satırı okunur be `__init__` fonksiyonu objesi oluşturulur. Her `Class()` kodu ile tek kullanımlık bir instance oluşturulduğunda `__init__` fonksiyonu çalışır ve dolayısıyla aynı altındaki `print("init dışı,", end=" ")` kodunda olduğu gibi `print("init içi,", end=" ")` kodu çalışır. Bu durum her `Class()` kodu çalıştığında tekrarlanır.

**Not:** `Class()` ile oluşturulan tek kullanımlık her instance, kendi `__init__` fonksiyon objesini çalıştırır.

Daha önce bir instance'nin mutable data type'ların bulunduğu attribute'lerinde, bu data type'ların methodlarını kullanarak yapılan değişikliklerin diğer instance'leri de etkilediğini söylemiştik. Bunun önüne geçmenin bir diğer yolu da bu attribute'leri `__init__` bloğunda tanımlamaktır.
```py
class Class():
    def __init__(self):
        self.instance_liste = []

instance_1 = Class()
instance_2 = Class()

instance_1.instance_liste.append("asd")
print(instance_1.instance_liste) # Output: ['asd']
print(instance_1.instance_liste) # Output: []
```

### Instance Methods
Main Class'ın içine tanımlanmış her fonksiyon, bu main class'dan üretilen instance'lerin methodlarıdır. Örnek:
<img src="https://i.ibb.co/gWWNHhh/code.png" alt="code" border="0">
Buradaki olayları teker teker açıklamak gerekirse:
- Bir main class'daki bütün fonksiyonların ilk parametresi, instance attribute'lere işaret ettiği için `self` olmalıdır.
- `Ahmet = Çalışan("Ahmet")` kodundaki `"Ahmet"`, `__init__` fonksiyonunun bloğunda tanımlı olan `self.isim` instance attribute'üne işaret eder.
- Bir instance'nin methodlarının içindeki attribute'lere ulaşamazsınız. Yani eğer `def personele_ekle(self):` bloğunda `self.a = 1` şeklinde bir instance attribute tanımlı olsaydı, buna`Çalışan().personele_ekle().a` şeklinde ulaşamazdık. `__init__` bloğunda o fonksiyona atifta bulunursak ``self.func()` gibi`, o fonksiyonun içindeki attribute'leri sanki `__init__`'den çağırıyormuş gibi çağırabiliriz.
```py
class Class():
    def __init__(self):
        self.a = "a"
        self.func()
    def func(self):
        self.b = self.a
print(Class().b) # Output: a
```
- Farklı iki instance'nin instance attribute'lerinin üzerinde yapılan işlemler instance'ye özgü olsa da mutable class attribute'lerinin üzerinde yapılan işlemler bütün instance'leri etkiler.
- `__init__` içinde tanımlanan instance attribute'lere main class'ın her yerinden erişilebilir.
- `personel` bir class attribute ise, bir method içinde belirttiğimiz `self.personel.append(self.isim)` ile `Çalışan.personel.append(self.isim)` aynı şeydir.