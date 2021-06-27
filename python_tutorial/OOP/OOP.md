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
Class'lar fonksiyonlara benzerdir ama en önemli farklarından birisi, bir fonksiyonun çalışabilmesi için o fonksiyonu çağırmamız gerekmektedir. Ama class'ları çağırmasak bile içindekileri çalıştırır. Örnek:
```py
# modul.py dosyası
class Exp_Class():
    attri_1 = "Attribute 1"
    attri_2 = ["Attribute 2"]

    print(attri_1,attri_2,sep="\n")
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
Eğer class'ın attribute'lerinin, class okunurken ekrana bastırılmasını istemiyorsanız, bu attribute'leri method gibi çağırarak kullanabilirsiniz. Örnek:
```py
class Exp_Class():
    attri_1 = "Attribute 1"
    attri_2 = ["Attribute 2"]

print(Exp_Class.attri_1,
      Exp_Class.attri_2,sep="\n")
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

**Dikkat:** Main Class'dan üretilmiş **instance**'larda bulunan attribute'lerin davranışları farklı olabilir. Bu attribute'ler değiştirilemez (immutable (`bool`, `int`, `float`, `complex`, `tuple`, `frozenset`)) data type'lar ise, bu attribute'lere bir veri atamak istediğimizde bu attribute'leri yeniden tanımlamamız (definition) gerekmektedir. Çünkü bunlar değiştirilemez (immutable) data type'lardır. Yani:
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
Gördüğünüz gibi `b` instance'ının attribute'lerini yeniden tanımlayarak `b` instance'larının içeriğini değiştirmiş olduk. Ama benzer şeyi değiştirilebilir (mutable (`list`, `set`, `dict`)) data type'larda yaparsak, bu eylemin diğer instance'leri de etkileme olasılığı var. Örnek:
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
Gördüğünüz gibi methodlarla attribute'lerde yaptığımız değişiklikler diğer instance'ları da etkileri. Bu yüzden aynı değiştirilemez (immutable) data type'larda yaptığımız gibi, değiştirilebilir (mutable) data type'larda da atama işlemi yapmalıyız. Yani:
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
**Instance Attribute**'ları, **Class Attribute**'ları ile farklı ama alakalı şeylerdir.

### `__init__` Fonksiyonu ve `self`
