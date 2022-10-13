# İçindekiler

- [Class](#1)
    - [Class Definition](#1.1)   
    - [Instantiation](#1.2)      
- [Attributes](#2)
    - [Class Attributes](#2.1)   
    - [Instance Attributes](#2.2)
- [Methods](#3)
    - [Instance Methods](#3.1)
      - [`__init__` Constructor](#3.1.1)   
    - [Class Methods](#3.2)
    - [Static Methods](#3.3)
- [Ekstralar](#4)
    - [Alternative Constructor](#4.1)
    - [`hasattr(obj, name)` Fonksiyonu](#4.2)
    - [`getattr(obj, name, default)` Fonksiyonu](#4.3)
    - [`setattr(obj, name, value)` Fonksiyonu](#4.4)
    - [`delattr(obj, name)` Fonksiyonu](#4.5)
    - [`__dict__` Methodu](#4.6)
    - [`__doc__` Methodu](#4.7)
    - [`__name__` Methodu](#4.8)
    - [`__module__` Methodu](#4.9)
    - [`__bases__` Methodu](#4.10)
    - [`__del__(self)` Methodu](#4.11)
    - [`__repr__(self)` Methodu](#4.12)
    - [`__str__(self)` Methodu](#4.13)
    - [`__add__(self)` Methodu](#4.14)
    - [`__new__(cls, *args, **kwargs)` Methodu](#4.15)

<h1 id="1">Class</h1>

Class'lar, obje yaratmak için kullanılan bir code template'dir (kod şablonu). Class'lar bizi belli obje ve fonksiyon gruplarını her seferinde en baştan yazma zahmetinden kurtarır. Çünkü bir class'dan, bu class'ın bütün içeriğine sahip istediğimiz sayıda **instance** adı verilen objeler üretilebilir. Instance Türkçede 'örnek', 'oluşum' anlamlarına gelmektedir.

**Not:** "Class'lar, obje yaratmak için kullanılan bir code template'dir (kod şablonu)." dedim diye class'lar obje değildir diye düşünmeyin. Python'da keyword'ler, statement'lar ve operator'lar hariç her şey (class'lar dahil) bir objedir. Bunlara ulaşmak için [tıklayınız](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/statements_expressions_keywords.md "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/statements_expressions_keywords.md").

<h2 id="1.1">Class Definition</h2>

`class <class_name>` statement kullanılarak class tanımlayabilirsiniz (definition). Örnek:
```py
class A():
    pass

class B:
    pass
```
Class tanımlarken parantez kullanmak ve kullanmamak arasında (yukarıdaki gibi) bir fark yoktur. Bu class'lar bellekte `__main__.A` ve `__main__.B` isimleriyle depolanır (bundan sonra bu tarz class'lardan yer yer "main class" olarak bahsedilecek). Buradaki `__main__`, o an bulunduğunuz python dosyasını temsil eden bir isimdir. (bunu `print(__name__)` kodunu çalıştırarak test edebilirsiniz).

Python, `class` statement ile tanımlanan class'ları okurken içeriğini de okur. Bu sayede main class objesi yaratılırken (create), main class objesinin içine tanımlanmış attribute, method vb. diğer objeler de yaratılmış olur. Bu "okuma" olayını, class'ın içine bir `print()` fonksiyonu ekleyerek kanıtlayabiliriz. Örnek:
```py
class A:
    class_attribute = "Class Attribute"

    def method_exp1(self):
        pass

    @classmethod
    def method_exp2(self):
        pass

    @staticmethod
    def method_exp3(self):
        pass

    print("A class'ının içi.")
```
**Output:**
```
A class'ının içi.
```

![](https://i.ibb.co/T8yYpbG/image.png)

**Not:** Bu durum, import işlemlerinde de yaşanır çünkü import edilen dosya baştan sona okunur, dolayısıyla class'ların içi de okunur.

**Not:** Bir `modul.py` dosyasındaki `A` class'ını kullanmak için `modul.py` dosyasını `import modul` statement ile import ettikten sonra `modul.A` şeklinde kullanabileceğiniz gibi, `form modul import A` şeklinde direkt class'ı import edip `modul` prefix'i olmadan da kullanabilirsiniz. Örnek:
```py
# modul.py
class A:
    print("modul.A çalıştı.")
    class_attribute = "Class Attribute"
```
```py
# dosya_1.py
import modul # Output: modul.A çalıştı.
print(modul.Class().class_attribute) # Output: Class Attribute
```
```py
# dosya_2.py
from modul import Class # Output: modul.A çalıştı.
print(Class().class_attribute) # Output: Class Attribute
```
Yukarıdaki kodları anlamadıysanız buradan sonraki **Instantiation** başlığını bitirdikten sonra buraya tekrar bakınız.

<h2 id="1.2">Instantiation</h2>

Main class'dan türetilen, türetildiği class'ın method, attribute, property vb. objelerine sahip olan objelere **instance** denir ("object = instance = obje = nesne" hepsi kelime olarak aynı anlama geliyor). Bu işleme de **Instantiation** denir. Örnek:
```py
class A:
    pass

var = A()
```
Gördüğünüz gibi `A` class'ını (`<class '__main__.A'>`) `A()` şeklinde çağırdığımızda (call) bir instance objesi yaratmış (create) oluyoruz (`<__main__.A object at 0x0000022782837730>`). `<__main__.A object at 0x0000022782837730>` yazısı "`0x0000022782837730` konumundaki (`at`) `A` class'ının (`__main__.A`) nesnesi (`object`) (yani A class'ından türetilmiş instance)" anlamına gelmektedir. Bu instance'ı bir variable'a atayarak (veya atamadan da) programınızda kullanabilirsiniz. Örnek:
```py
class A:
    pass

var = A()

print(A) # Output: <class '__main__.A'>
print(A()) # Output: <__main__.A object at 0x0000015D8A9CFCD0>
print(var) # Output: <__main__.A object at 0x0000015D8A9CF6A0>
```
Python, `A()` kodunu okuduğunda bir instance yaratır ama bir sonraki statement'a geçtiğinde, yarattığı bu instance herhangi bir variable'a atanmadığı için bellekten silinir. Bu yüzden tek kullanımlıktır.

**Not:** Şimdiye kadar anlattığım, type dönüşümlerinde kullandığımız `int()`, `str()`, `list()` vs. her şey aslında bir class. Bunları size "`int()` fonksiyonu", "`str()` fonksiyonu" olarak sunmuştum ama aslında bunlar `int`, `str` vs. class'larını kullanarak yaptığımız bir instantiation işlemidir. Mesela daha sonra anlatacağım ve "`property()` fonksiyonu" olarak bahsedeceğim şey de aslında `property` class'ını kullanarak yaptığımız bir instantiation işlemidir. Bu bilgi aklınızın bir köşesinde dursun çünkü Python'u anlamanız açısından önemli.

<h1 id="2">Attributes</h1>

Belli bir değeri/özelliği belirten, variable'lar gibi kullanılan class elemanlarına **Attribute** denir. Attribute'lar class ve instance attribute olmak üzere 2 çeşittir.

<h2 id="2.1">Class Attributes</h2>

Class methodların (daha sonra anlatılacak) veya doğrudan class'ların kapsamında, `__init__` constructor'ının veya (class method hariç) herhangi bir user-defined methodun kapsamı dışında tanımlanan variable'lara **class attribute** denir. Örnek:
```py
class A:
    class_attri = "Class Attribute"

var = A()
print(var.class_attri) # Output: Class Attribute
```

Main class'ın class attribute'ları ile, main class'dan türetilen instance'ların class attribute'ları ilk başta aynı objeye bağlıdır. Yani instace'daki class attribute, main class'da tanımlanan class attribute'a atıfta bulunur (refers to) (ID'leri aynıdır). Ama sonradan bu instance'ların class attribute'larını yeniden tanımlarsanız (redefinition), bu class attribute artık main class'daki class attribute'a atıfta bulunmaz (refers to) ve ilgili instance için instance attribute'a dönüşür.
```py
class A():
    class_attri = "Class Attribute"

var = A()

print(A.class_attri) # Output: Class Attribute
print(var.class_attri) # Output: Class Attribute
print(id(var.class_attri)==id(A.class_attri)) # Output: True
print(var.__dict__) # Output: {}

A.class_attri = "New Class Attribute"
print(A.class_attri) # Output: New Class Attribute
print(var.class_attri) # Output: New Class Attribute
print(id(var.class_attri)==id(A.class_attri)) # Output: True
print(var.__dict__) # Output: {}

var.class_attri = "Instance attribute"
print(A.class_attri) # Output: Class Attribute
print(var.class_attri) # Output: Instance Attribute
print(id(var.class_attri)==id(A.class_attri)) # Output: False
print(var.__dict__) #Output: {'class_attri': 'Instance attribute'}
```
`__dict__` methodunun ne işe yaradığını daha sonra daha detaylı anlatacağım. Şimdilik `__dict__` methodunun ilgili class ya da instance'ın içerdiği objelerin (method, property, attribute vs.) bulunduğu bir `dict` olarak düşünebilirsiniz. Yukarıdaki koddan çıkarmanız gereken sonuçlar:
- Main class'ın class attribute'larında yapılan herhangi bir değişiklik, bu main class'dan türetilen instance'ları da etkiler.
- Main class'dan türetilen instance'ın class attribute'unda yapılan bir değişiklik, main class'ı ve diğer instance'ları etkilemez çünkü ilgili instance'ın class attribute'u artık main class'ın class attribute'undan farklı bir objedir (artık instance attribute'dur da denilebilir).

**Not:** Class attribute'lar, instance'larda `__class__` adında bir method'da depolanırlar (`__class__` methodunun ne olduğu daha sonra anlatılacak). Bu yüzden instance'ların `__dict__` methodunda class attribute'lar yoktur. Main class'larda class attribute'lar `__dict__` methodunda bulunur. Kanıt:
```py
class A():
    class_attri = "Class Attribute"

var = A()

print(A.__dict__["class_attri"]) # Output: Class Attribute
print(var.__dict__["class_attri"]) # KeyError: 'class_attri'
```

**Not:** `__class__` methodu, bulunduğu objenin türetilirken kullanınan class'a atıfta bulunur. Örnek:
```py
class A():
    pass

var = A()

print(A.__class__) # Output: <class 'type'>
print(var.__class__) # Output: <class '__main__.A'>
```
`var` `A` class'ından, `A` `type` class'ından türetildi. Sanırım en basit böyle açıklanır.

Üzerinde yeniden tanımlama (redefinition) işlemi yapılan her class attribute farklı bir objeye dönüşür (ID'leri değişir). İçerdiği value'yu değiştirmek için yeniden tanımlama (redefinition) işlemi gerektiren değiştirilemez (immutable (`bool`, `int`, `float`, `complex`, `tuple`, `frozenset`, `bytes`, `str`, `range` vb.)) data type'larda bu durumun önüne geçemeyiz ama değiştirilebilir (mutable (`list`, `set`, `dict`, `bytearray` vb.)) data type'larda geçebiliriz. Örnek:
```py
class A:
    class_attri_1 = "String"
    class_attri_2 = 1
    class_attri_3 = 1.1
    class_attri_4 = 1+1j
    class_attri_5 = tuple([1,2,3])
    class_attri_6 = frozenset([1,2,3])

    class_attri_7 = [1,2,3]
    class_attri_8 = set([4,5,6])
    class_attri_9 = {"yedi":7, "sekiz":8, "dokuz":9}

var1 = A()
var2 = A()

var2.class_attri_1 = "Değiştirilmiş String"
var2.class_attri_2 = 9
var2.class_attri_3 = 9.9
var2.class_attri_4 = 9+9j
var2.class_attri_5 = tuple([9,8,7])
var2.class_attri_6 = frozenset([6,5,4])

var2.class_attri_7.append("new_item")
var2.class_attri_8.add("new_item")
var2.class_attri_9.update({"new":"item"})

for i in dir(var1):
    if "class_attri_" in i:
        eval(f"print('var1.{i}:', var1.{i})")
print("-"*69)
for i in dir(var2):
    if "class_attri_" in i:
        eval(f"print('var2.{i}:', var2.{i})")
```
**Output:**
```
var1.class_attri_1: String
var1.class_attri_2: 1
var1.class_attri_3: 1.1
var1.class_attri_4: (1+1j)
var1.class_attri_5: (1, 2, 3)
var1.class_attri_6: frozenset({1, 2, 3})
var1.class_attri_7: [1, 2, 3, 'new_item']
var1.class_attri_8: {'new_item', 4, 5, 6}
var1.class_attri_9: {'yedi': 7, 'sekiz': 8, 'dokuz': 9, 'new': 'item'}
---------------------------------------------------------------------
var2.class_attri_1: Değiştirilmiş String
var2.class_attri_2: 9
var2.class_attri_3: 9.9
var2.class_attri_4: (9+9j)
var2.class_attri_5: (9, 8, 7)
var2.class_attri_6: frozenset({4, 5, 6})
var2.class_attri_7: [1, 2, 3, 'new_item']
var2.class_attri_8: {'new_item', 4, 5, 6}
var2.class_attri_9: {'yedi': 7, 'sekiz': 8, 'dokuz': 9, 'new': 'item'}
```
**ID'ler:**
```py
print(id(A.class_attri_1)==id(var1.class_attri_1), id(A.class_attri_1)==id(var2.class_attri_1)) # Output: True False
print(id(A.class_attri_2)==id(var1.class_attri_2), id(A.class_attri_2)==id(var2.class_attri_2)) # Output: True False
print(id(A.class_attri_3)==id(var1.class_attri_3), id(A.class_attri_3)==id(var2.class_attri_3)) # Output: True False
print(id(A.class_attri_4)==id(var1.class_attri_4), id(A.class_attri_4)==id(var2.class_attri_4)) # Output: True False
print(id(A.class_attri_5)==id(var1.class_attri_5), id(A.class_attri_5)==id(var2.class_attri_5)) # Output: True False
print(id(A.class_attri_6)==id(var1.class_attri_6), id(A.class_attri_6)==id(var2.class_attri_6)) # Output: True False
print(id(A.class_attri_7)==id(var1.class_attri_7), id(A.class_attri_7)==id(var2.class_attri_7)) # Output: True True
print(id(A.class_attri_8)==id(var1.class_attri_8), id(A.class_attri_8)==id(var2.class_attri_8)) # Output: True True
print(id(A.class_attri_9)==id(var1.class_attri_9), id(A.class_attri_9)==id(var2.class_attri_9)) # Output: True True
```

Mutable data type'ların methodlarını kullanmak yerine yeniden tanımlama (redefinition) işlemi uygulasaydık, mutable data type'lar da farklı bir objeye dönüşecekti (ID'leri değişecekti).

<h2 id="2.2">Instance Attributes</h2>

Sadece instance methodların (daha sonra anlatılacak) veya `__init__` constructor'ının kapsamında tanımlanabilen variable'lara **instance attribute** denir. Örnek:
```py
class A:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

    def func(self):
        self.a = 4
        self.b = 5
        self.c = 6
```

Instance attribute'lara sadece instance'lar üzerinden ulaşabilir, main class üzerinden ulaşılamaz. Çünkü python, main class'ı okurken `__init__` constructor'ını ve instance methodları okuyup bu methodların objelerini oluşturur (create) ve bırakır, içeriğini okumaz (bildiğimiz fonksiyonlarda olduğu gibi). Bu yüzden instance attribute'lara main class'dan ulaşamayız. Instance attribute'lar kapsamında tanımlandıkları method çalıştırıldığında erişilebilir olur. `__init__` constructor'ı ilgili main class'dan instance oluşturulduğunda çalıştırıldığı için kapsamında tanımlanan instance attribute'lara o zaman erişilebilir. Instance methodların kapsamında tanımlanan instance attribute'lara da ilgili instance üzerinden ilgili instance method en az bir kere çalıştırıldığında erişilebilir. Örnek:
```py
class A:
    def __init__(self):
        self.instance_attri1 = 1
        self.instance_attri2 = 2
        self.instance_attri3 = 3

    def func(self):
        self.instance_attri4 = 4
        self.instance_attri5 = 5
        self.instance_attri6 = 6

var = A()
print(var.instance_attri1) # Output: 1
print(var.instance_attri2) # Output: 2
print(var.instance_attri3) # Output: 3
print(var.instance_attri4) # AttributeError: 'A' object has no attribute 'instance_attri4'
print(var.instance_attri5) # AttributeError: 'A' object has no attribute 'instance_attri5'
print(var.instance_attri6) # AttributeError: 'A' object has no attribute 'instance_attri6'
var.func()
print(var.instance_attri4) # Output: 4
print(var.instance_attri5) # Output: 5
print(var.instance_attri6) # Output: 6
```
Her instance kendine özel instance attribute'lara sahiptir ve bunları kendi `__dict__` methodlarında depolarlar. Örnek:
```py
class A:
    def __init__(self):
        self.attri1 = 1
        self.func()

    def func(self):
        self.attri2 = 2

var1 = A()
var2 = A()

print(var1.__dict__,var2.__dict__) # Output: {'attri1': 1, 'attri2': 2} {'attri1': 1, 'attri2': 2}
var2.attri1,var2.attri2=3,4
print(var1.__dict__,var2.__dict__) # Output: {'attri1': 1, 'attri2': 2} {'attri1': 3, 'attri2': 4}
```

<h1 id="3">Methods</h1>

Bir class'ın kapsamında tanımlanan fonksiyonlara **Method** denir. Class'a işlevsellik katar. Class method, instance method ve static method olmak üzere 3 çeşittir.

<h2 id="3.1">Instance Methods</h2>

Bir class içinde tanımlanan user-defined (kullanıcı tanımlı) fonksiyonlar, aksi belirtilmediği (`@classmethod` ya da `@staticmethod` decorator'ları ile decore edilmedikleri) sürece Python tarafından **instance method** olarak kabul edilir. Örnek:
```py
class A:
    attri = 1
    def __init__(self):
        self.attri2 = 2

    def func1(self):
        return "asd"
    
    @classmethod
    def func2():
        pass

    @staticmethod
    def func3():
        pass

print(A.__dict__.get("__init__")) # Output: <function A.__init__ at 0x00000245394560D0>
print(A.__dict__.get("func1")) # Output: <function A.func1 at 0x000002BAF9B26160>
print(A.__dict__.get("func2")) # Output: <classmethod object at 0x000002BAF9B23FD0>
print(A.__dict__.get("func3")) # Output: <staticmethod object at 0x000002BAF9B23FA0>
```
Gördüğünüz gibi aksi belirtilmediği için `func1` fonksiyonu ve `__init__` constructor'ı instance methoddur. Bir class'ın `__dict__` methodunda, bu class içinde bulunan objelerin en salt hallerini (obje isimlerini) bulabilirsiniz. Instance methodlar birer fonksiyon objesi (`function`) (`builtins.pyi`'de `class function`) olarak depolanırken, class methodlar classmethod objesi (`classmethod object`) (`builtins.pyi`'de `class classmethod`), static methodlar staticmethod objesi (`staticmethod object`) (`builtins.pyi`'de `class staticmethod`) depolanır.

`__init__` constructor'ı ve instance method kapsamında tanımlanan şeyler dışındaki her şey main class'dan erişilebilir ve değiştirilebilir. Bu değişiklik ilgili main class'dan türetilen instance'ları da etkiler (çünkü instance'lardaki bu objeler main class'dakilere atıfta bulunur). Örnek:
```py
class A:
    def __init__(self):
        pass

    def func1(self):
        pass

    def func2(self):
        pass

var = A()

print(A.func1) #Output: <function A.func1 at 0x0000020D701880D0>
print(var.func1) #Output: <bound method A.func1 of <__main__.A object at 0x0000020D70184FD0>>
A.func1 = 1
print(A.func1) #Output: 1
print(var.func1) #Output: 1

print(A.func2) #Output: <function A.func1 at 0x0000020D701880D0>
print(var.func2) #Output: <bound method A.func1 of <__main__.A object at 0x0000020D70184FD0>>
var.func2 = 1
print(A.func2) #Output: <function A.func1 at 0x00000246483180D0>
print(var.func2) #Output: 1
```
Gördüğünüz gibi `A` class'ının `__init__` methodunda yapılan bir değişiklik `A` class'ından türetilen `var` instance'ını da etkilerken, benzer şeyin `var` instance'ında yapılması `A` class'ını etkilemez.

Instance methodların ve `__init__` constructor'ının ilk parametresi özel bir anlama sahiptir. Bu parametreye farklı isimler de verebilirsiniz ama `self` programcılar camiasında kalıplaşmış bir kullanım olmasından dolayı tercih edilir. Örnek:
```py
class A:
    def __init__(self):
        self.attri = "A.attri"

class B:
    def __init__(parametre):
        parametre.attri = "B.attri"

class C:
    def __init__(at_arabasi):
        at_arabasi.attri = "C.attri"

print(A().a) # Output: A.attri
print(B().a) # Output: B.attri
print(C().a) # Output: C.attri
```
`self` parametresi, main class'dan türetilen geçerli (current) instance'a atıfta bulunur (refers to). Kanıtı:
```py
class A:
    def __init__(self):
        print("Address of self        :", id(self), self)

var = A()
print("Address of class object:", id(var), var)
```
**Output:**
```
Address of self        : 1464086224848 <__main__.A object at 0x00000154E256DFD0>
Address of class object: 1464086224848 <__main__.A object at 0x00000154E256DFD0>
```
Buradan yola çıkarak, örneğin `self.a = 1` kodunun `A().a = 1` anlamına geldiği sonucunu çıkarabiliriz. `self.a = 1` kodunun `A().a = 1` anlamına gelmesi, instantiation işlemini anlamada önemli bir yere sahiptir. Bu durumu kanıtlayan bir örnek:
```py
class A:
    def __init__(self):
        pass

var = A()
var.a = 1
var.b = 2
var.c = 3
print(var.__dict__) # Output: {'a': 1, 'b': 2, 'c': 3}
print(var.a, var.b, var.c) # Output: 1 2 3
```
`__init__` constructor'ında herhangi bir instance attribute tanımlı olmamasına rağmen `var` instance, `var.a = 1`, `var.b = 2` ve `var.c = 3` statement'larından sonra 3 farklı instance attribute'a sahip oldu. Böylece yukarıdaki koddan önceki kodda bahsettiğim `self.a = 1` kodunun `A().a = 1` anlamına gelmesi olayının nasıl/neden böyle olduğunu açıklamış olduk.

Instantiation işlemi kısaca bu şekilde çalışır. Instantiation işleminde otomatik olarak `__init__` constructor'ı çağırılır ve yukarıda anlattığım olaylar gerçekleşir. Örnek:
```py
class A:
    def __init__(self):
        print("`__init__` constructor'ı çağırıldı.")
        self.a = 1
        self.b = 2
        self.c = 3

var = A() # Output: `__init__` constructor'ı çağırıldı.
print(var.a, var.b, var.c) # Output: 1 2 3
```
Buradaki `self` parametresine, Python tarafından `var = A()` kodundaki `A()` kodunun yarattığı instance, argüman olarak girilir. Bu argümana temsili olarak `X` dersek, `self.a = 1`, `self.b = 2`, `self.c = 3` kodları `X.a = 1`, `X.b = 2`, `X.c = 3` anlamına gelmektedir. Yukarıdaki olayı `setattr()` (daha sonra anlatılacak) build-in fonksiyonunu kullanarak da yapabilirsiniz.

`self` main class kapsamında kullanılamaz çünkü tanımlanmamıştır. Kullanılırsa `NameError: name 'self' is not defined` hatası yükseltilir. `__init__` constructor'ının ve Instance methodların ilk parametresi tanımlanmazsa `TypeError: func() takes 0 positional arguments but 1 was given` hatası yükseltilir. Örnek:
```py
class A:
    def __init__():
        self.attri = 1
A() # TypeError: __init__() takes 0 positional arguments but 1 was given

class B:
    self.attri = 2 # NameError: name 'self' is not defined
    def __init__(self):
        self.attri = 2
```

instance methodlar class attribute'lara atıfta bulunabilirsiniz (refers to). Örnek:
```py
class A:
    attri = "class attribute"

    def func1(self):
        temp = self.attri
        return temp

var = A()
print(A.attri, id(A.attri))         # Output: class attribute 3046034465712
print(var.func1(), id(var.func1())) # Output: class attribute 3046034465712
print(A.attri==var.func1())         # Output: True
```

<h3 id="3.1.1"> <code>__init__</code> Constructor </h3>

`__init__`, yapıcı (constructor) olarak bilinen, main class'dan instance türetilirken ilk çağırılan temel aşırı yükleme (overloading) methodudur. `__init__(self, *args, **kwargs)` syntax'ına sahiptir. `__init__` constructor'ı **initialization** (başlatma, ilklendirme) işleminden sorumludur. `__new__` methodunda yapılabilecek hemen hemen her şeyi `__init__` methodunda da yapılabildiği için  `__new__` methodu yerine `__init__` methoduna 'constructor' denmektedir.

`__init__` constructor'ı tanımlanmamış `A` ismindeki bir class'ı ele alalım. `A` class'ı `object` base class'ından biras aldığı (daha sonra anlatılacak) için `A` class'ına debugger ile baktığınızda `__init__` constructor'ının special variables sekmesinde `<slot wrapper '__init__' of 'object' objects>` şeklinde depolandığını görürsünüz. Kanıt:
```py
class A:
    pass
```

![](https://i.ibb.co/XC7s4y5/image.png)

`A` class'ından türetilen instance'a debugger ile baktığınızda `__init__` constructor'ının function variables değil, special variables sekmesinde `<method-wrapper '__init__' of A object at 0x000002288B12D430>` şeklinde depolandığını görürsünüz. Kanıt:
```py
class A:
    pass

var = A()
```

![](https://i.ibb.co/YX198Dv/image.png)

C'de uygulanan (implemented) bir special method'a erişmek (access) için bir extension type'ın dict'ine bir [slot wrapper](https://stackoverflow.com/questions/24708203/what-is-a-slot-wrapper-in-python#:~:text=A%20slot%20wrapper%20is%20installed,variant%20called%20method-wrapper "https://stackoverflow.com/questions/24708203/what-is-a-slot-wrapper-in-python#:~:text=A%20slot%20wrapper%20is%20installed,variant%20called%20method-wrapper") kurulur. Bu sayede C programlama dilinde yazılmış special methodları Python'da kullanabiliyoruz. Slot wrapper her zaman unbound'dur ve method wrapper, slot wrapper ile ilişkilidir (bound). Bunları, slot wrapper ve method wrapper kavramlarını gördüğünüzde yadırgamamanız için anlattım.

`__init__` constructor'ı tanımlanmış `A` ismindeki bir class'ı ele alalım. Bu durumda `A` class'ının kendi `__init__` constructor'ı, object base class'ın `__init__` constructor'ını geçersiz kıldığı (override) (daha sonra anlatılacak) için `<function A.__init__ at 0x000001D36879A430>` şeklinde depolanır.
```py
class A:
    def __init__(self):
        pass
```

![](https://i.ibb.co/749ZxJX/image.png)

`A` class'ından türetilen instance'lardaki `__init__` constructor'ları, `A` class'ının init constructor'ı ile ilişkilidir (bound) ve `<bound method A.__init__ of <__main__.A object at 0x000001D3687A13D0>>` şeklinde depolanır. `<bound method A.__init__ of <__main__.A object at 0x000001D3687A13D0>>` bu "`0x000001D3687A13D0` konumundaki `__main__.A`'dan (yani `A` class'ının) türetilen instance'ındaki, `A.__init__`'e (yani `A` class'ının `__init__` methoduna) bağlı method" anlamına gelmektedir.

**Not:** `__init__` constructor'ının mekanizması, Python geliştiricileri tarafından titizlikle ayarlanmıştır. Bu yüzden bu methodu kurcalamayın (redefinition falan yapmayın). Bu methodu amacı doğrultusunda kullandığınız sürece sorun yaşamazsınız.


<h3><code>__init__</code> Constructor'ının ve Instance Methodların Kullanım Alanlarını ve Özellikleri</h3>

Daha önce `__init__` constructor'ının main class'dan instance türetilirken otomatik çalıştırıldığını, böylece kapsamındaki instance attribute'ların ilgili instance'da yaratıldığını (create), instance methodların kapsamındaki instance attribute'ların da ilgili instance'da yaratılması (create) için ilgili instance methodun en az bir kere çağırılması gerektiğini, instance attribute'ların `__dict__` methodunda depolandığını söylemiştim.

Instance methodların `__init__` constructor'ı gibi main class'dan instance türetilirken otomatik çağırılmasını istiyorsanız, instance methodları `__init__` constructor'ı kapsamında çağırabilirsiniz. Örnek:
```py
class A:
    def __init__(self):
        self.attri1 = 123
        self.func()
    
    def func(self):
        self.attri2 = 12334

var = A()
print(var.__dict__) # Output: {'attri1': 123, 'attri2': 12334}
```
**Not:** `func()` fonksiyonunun içindeki `attri2` instance attribute'una `var.func().attri2` şeklinde ulaşmaya çalışmak düşününce mantıklı gelse de (bana da mantıklı gelmişti zamanında) `AttributeError: 'NoneType' object has no attribute 'attri2'` hatası yükseltilir. Örnek:
```py
class A():

    def func(self):
        self.attri2 = "func attribute"
        
var = A()
print(var.func().attri2) # AttributeError: 'NoneType' object has no attribute 'attri2'
```

Python dahil çoğu programlama dili [aritmetik işlem mantığıyla](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/basic_concepts.md#2 "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/basic_concepts.md#2") kodları çalıştırır. Aritmetik işlem mantığına göre Python `var.func().attri2` kodunu şöyle yorumlar:
1. Python önce `var` instance'ı üzerinden `func` methodunu çağırır.
2. `func` method'unda herhangi bir `return` statement olmadığı için çalıştıktan sonra bellekten silinir.
3. Python'da varolmayan bir şey `None` değeriyle ifade edilir. `None` değeri `NoneType` (`<class 'NoneType'>`) bir objedir.
4. `var.func().attri2` işlemlerden sonra `var.func().attri2` kodu Python'ın gözünde `NoneType.attri2` koduna dönüşür.
5. `NoneType` class'ının `attri2` adında bir methodu olmadığı için `AttributeError: 'NoneType' object has no attribute 'a_yazdir_attribute'` hatası yükseltilir.

Peki `func` methoduna `return self.attri2` statement eklersek? Örnek:
```py
class A():

    def func(self):
        self.attri2 = "func attribute"
        return self.attri2
        
var = A()
print(var.func().attri2) # AttributeError: 'str' object has no attribute 'attri2'
```
Python `var.func().attri2` kodunu şöyle yorumlar:
1. Python önce `var` instance'ı üzerinden `func` methodunu çağırır.
2. `func` method'u `self.attri2` instance attribute'unun value'su olan `"func attribute"` string'ini (`<class 'str'>`) döndürür.
3. `var.func().attri2` işlemlerden sonra `var.func().attri2` kodu Python'ın gözünde `"func attribute".attri2` koduna dönüşür.
4. `"func attribute"` bir string (`str`) objesidir. Bu string objesinin `attri2` adında bir methodu olmadığı için `AttributeError: 'str' object has no attribute 'attri2'` hatası yükseltilir.

[Fonksiyonlar (Functions)](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/functions/functions.md "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/functions/functions.md") konusunu anlayan, yukarıda anlattığım durumların nedenini zaten anlamıştır.

Instance'lardaki `__init__` constructor objeleri instance'a özel değildir, main class'ın `__init__` constructor objesi ile ilişkilidir (bound). Örnek:
```py
class A:
    def __init__(self):
        self.attri = 1

var = A()
print(A.__init__) # Output: <function A.__init__ at 0x0000021F8ECAF160>
print(var.__init__) # Output: <bound method A.__init__ of <__main__.A object at 0x0000021F8ECB1FD0>>

print(var.attri) # Output: 1
var.attri = 2
var.attri2 = 3
print(var.attri) # Output: 2
print(var.attri2) # Output: 3
var.__init__()
print(var.attri) # Output: 1
print(var.attri2) # Output: 3
```
Gördüğünüz ilgili instance üzerinde `__init__` constructor'ını tekrar çağırdığımızda `__init__` constructor'ı kapsamında tanımlanan instance attribute'ların içerdiği değerler eski haline dönerken sonradan eklenen (`attri2` gibi) instance attribute'lar da mevcudiyetini korumaya devam edebiliyor.

Bir instance'da instance attribute olarak ve class attribute olarak aynı isimde iki attribute varsa, instance attribute dikkate alınır. Bu durumun instance attribute'un class attribute'u geçersiz kılmasından (overrite) kaynaklandığını düşünebilirsiniz ama hala class attribute'a erişebilirsiniz. Örnek:
```py
class A:
    attri_1 = 2
    def __init__(self):
        self.attri_1 = 1

var = A()
print(var.attri_1) # Output: 1
print(var.__class__.attri_1) # Output: 2
print(A.attri_1) # Output: 2
```

`__init__` constructor'ı içine tanımlayacağınız variable'ların hepsini `self` ile kullanmak zorunda olduğunu düşünüyorsanız, böyle bir zorunluluk yok. Örnek:
```py
class A():
    def __init__(self):
        sayi_1 = 4
        sayi_2 = 5
        self.sayi_3 = sayi_1 + sayi_2

print(A().sayi_1) # Output: AttributeError: 'Class' object has no attribute 'sayi_1'
print(A().sayi_2) # Output: AttributeError: 'Class' object has no attribute 'sayi_2'
print(A().sayi_3) # Output: 3
```
Gördüğünüz gibi `self` prefix'i ile kullandığınız variable'lar instance attribute olarak instance'ın `__dict__` methodunda depolanabilirken prefixsiz variable'lar normal fonksiyonlarda olduğu gibi fonksiyon sonlandıktan sonra bellekten silinir.

instance methodlara ve `__init__` constructor'ına `self` dışında parametreler de tanımlayabilirsiniz. Örnek:
```py
class A():
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def func(self, secname, note):
        print("Full Name:", self.name, secname, f"({note})")

var = A("Eyüp", 175)
print(var.name) # Output: Eyüp
print(var.size) # Output: 175
var.func("Kağan", "Python Dev.") # Output: Full Name: Eyüp Kağan (Python Dev.)
```
`__init__` constructor'ında `self` dışında parametreler de tanımlıysa, bu parametrelere argüman girerken yukarıdaki gibi `self`'i görmezden gelmelisiniz. Çünkü Python, instantiation işleminde `self` parametresine gerekli argümanı kendisi otomatik olarak giriyor. Ama bu sadece instantiation işleminde geçerlidir. Main class üzerinden herhangi bir instance method veya `__init__` constructor çağırırken `self` parametresine gerekli argümanı elle girmemiz gerekmektedir çünkü bu bir instantiation işlemi değildir, dolayısıyla python `self` parametresine gerekli argümanı otomatik olarak girmez. Örnek:
```py
class A:
    def __init__(self):
        self.a = "a attribute"
    
    def func(self):
        print("Instance method func():", self.a)

A().func() # Output: Instance method func(): a attribute
A.func() # TypeError: func() missing 1 required positional argument: 'self'
A.func(A()) # Output: Instance method func(): a attribute
```

Main class üzerinden çağırılan instance method'un veya `__init__` constructor'ının `self` parametresine argüman olarak girilen instance'a göre kodunuz farklı davranabilir. Örnek:
```py
class A:
    def __init__(self):
        self.a = "A"

    def func(self):
        return self.a

var = A()
var.a = "B"
print(A.func(A())) # Output: A
print(A.func(var)) # Output: B
```
Gördüğünüz gibi `self` parametresine argüman olarak girilen instance, sonucu etkiliyor. `self` parametresinin aslında ne olduğunu daha önce anlatmıştım. Anlattıklarımdan yola çıkarak yukarıdaki durumun sebebini anlayabilirsiniz. Anlamadıysanız comment falan bırakın, dönüş yaparım.

<h2 id="3.2">Class Methods</h2>

Python'da `@` işareti kullanılanılarak oluşturulan yapılara **decorator** denir (daha önce anlattım). Python'da class method tanımlamak için `@classmethod` decorator'u kullanılır. Bu sayede decode edilen method, `classmethod` class'ının (`builtins.pyi`'de `class classmethod`) işlevselliğini kazanır. Başka bir deyişle, `@classmethod` decorator'u kendinden sonraki fonksiyonun bir class method olduğunu Python'a bildirir.

`@classmethod` decorator'u ile decore edilen methodlar, main class'ın `__dict__` methodunda `<classmethod object at 0x0000021910BB3430>` şeklinde depolanmışken, function olarak `<bound method A.class_method_exp of <class '__main__.A'>>` şeklinde depolanmıştır. `<bound method A.class_method_exp of <class '__main__.A'>>` yazısı "`A` class'ının, `A` class'ının `class_method_exp` objesine bağlı method" anlamına gelmektedir. Örnek:
```py
class A:
    @classmethod
    def class_method_exp(cls):
        pass

print(A.__dict__["class_method_exp"]) # Output: <classmethod object at 0x0000021910BB3430>
print(A.class_method_exp) # Output: <bound method A.class_method_exp of <class '__main__.A'>>
print(type(A.__dict__["class_method_exp"])) # Output: <class 'classmethod'>
print(callable(A.__dict__["class_method_exp"])) # Output: False
print(callable(A.class_method_exp)) # Output: True
```
Yukarıda da gördüğünüz gibi `<bound method A.class_method_exp of <class '__main__.A'>>` objesi çağırılabilirdirken (callable) `<classmethod object at 0x0000021910BB3430>` objesi çağırılabilir (callable) değildir. Bu yüzden python `A` class'ının, `A` class'ının `class_method_exp` objesine bağlı methodu (`<bound method A.class_method_exp of <class '__main__.A'>>`) kullanır.

**Not:** Main class'ın class method'larında yapılan değişiklikler, bu main class'dan türetilen instance'ların class method'larını da etkiler (aynı instance method'lardaki gibi). Bunun nedenini [Instance Methods](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/OOP/beginning_of_classes.md#3.1 "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/OOP/beginning_of_classes.md#3.1") kısmında anlattım. İlgili kısım:

> ... `__init__` constructor'ı ve instance method kapsamında tanımlanan şeyler dışındaki her şey main class'dan erişilebilir ve değiştirilebilir. Bu değişiklik ilgili main class'dan türetilen instance'ları da etkiler (çünkü instance'lardaki bu objeler main class'dakilere atıfta bulunur). ...

Örnek:
```py
class A:
    @classmethod
    def func1(self):
        pass

var = A()

print(var.func1) #Output: <bound method A.func1 of <class '__main__.A'>>
A.func1 = 1
print(var.func1) #Output: 1
```

Class methodların ilk parametresi özel bir anlama sahiptir. Bu parametreye farklı isimler de verebilirsiniz ama `cls` programcılar camiasında kalıplaşmış bir kullanım olmasından dolayı tercih edilir. Örnek:
```py
class A:
    @classmethod
    def func1(cls):
        cls.attri1 = "A.attri1"

class B:
    @classmethod
    def func2(parametre):
        parametre.attri2 = "B.attri2"

class C:
    @classmethod
    def func3(at_arabasi):
        at_arabasi.attri3 = "C.attri3"

A.func1();B.func2();C.func3()
print(A.attri1) # Output: A.attri1
print(B.attri2) # Output: B.attri2
print(C.attri3) # Output: C.attri3
```

`cls` parametresi, main class'a atıfta bulunur (refers to). Kanıtı:
```py
class A:
    @classmethod
    def func(cls):
        print("Address of cls      :", id(cls), cls)

A.func()
print("Address of 'A' class:", id(A), A)
```
**Output:**
```
Address of cls      : 1967578676944 <class '__main__.A'>
Address of 'A' class: 1967578676944 <class '__main__.A'>
```
Buradan yola çıkarak, örneğin `cls.attri_1 = 1` kodunun `A.attri_1 = 1` anlamına geldiği sonucunu çıkarabiliriz. `cls.attri_1 = 1` kodunun `A.attri_1 = 1` anlamına gelmesi, class attribute create işlemini anlamada önemli bir yere sahiptir. Örnek:
```py
class A:
    pass

A.attri_1 = 1
A.attri_2 = 2
A.attri_3 = 3

print([f"{i}:{A.__dict__[f'{i}']}" for i in A.__dict__ if i.startswith("attri")]) # Output: ['attri_1:1', 'attri_2:2', 'attri_3:3']
```
Yukarıdaki örnekteki olayın nasıl/neden gerçekleştiğini instance method başlığı altında anlattım. Başka bir örnek:
```py
class A:
    @classmethod
    def func(cls):
        cls.attri_1 = 1
        cls.attri_2 = 2
        cls.attri_3 = 3

print([f"{i}:{A.__dict__[f'{i}']}" for i in A.__dict__ if i.startswith("attri")]) # Output: []
A.func()
print([f"{i}:{A.__dict__[f'{i}']}" for i in A.__dict__ if i.startswith("attri")]) # Output: ['attri_1:1', 'attri_2:2', 'attri_3:3']
```
Yukarıdaki örnekteki olayın nasıl/neden gerçekleştiğini instance method başlığı altında anlattım. Python `A` class'ını okurken `A` class'ının kapsamındaki fonksiyonların içeriğini okumaz (`def` statement ile tanımladığımız her şey özünde fonksiyondur), sadece fonksiyon objelerini yaratır (daha önce anlattım). Bu yüzden class attribute'ları aşağıdaki gibi tanımlamanız daha doğru olacaktır:
```py
class A:
    attri_1 = 1
    attri_2 = 2
    attri_3 = 3

print(A.attri_1, A.attri_2, A.attri_3) # Output: 1 2 3
```
Yukarıdaki olayı `setattr()` (daha sonra anlatılacak) build-in fonksiyonunu kullanarak da yapabilirsiniz.

`cls` main class kapsamında kullanılamaz çünkü tanımlanmamıştır. Kullanılırsa `NameError: name 'cls' is not defined` hatası yükseltilir. Class methodların ilk parametresi tanımlanmazsa `TypeError: func() takes 0 positional arguments but 1 was given` hatası yükseltilir. Örnek:
```py
class A:
    cls.attri = 1 # NameError: name 'cls' is not defined

class B:
    @classmethod
    def func():
        cls.attri = 2

B.func() # TypeError: func() takes 0 positional arguments but 1 was given
```

Instance methodlara main class üzerinden erişemeyiz ama class methodlara hem main class hem de instance üzerinden erişebiliriz. Örnek:
```py
class A:
    @classmethod
    def func(cls):
        print("Class Method Çalıştı.")

var = A()
A.func() # Output: Class Method Çalıştı.
var.func() # Output: Class Method Çalıştı.
```

Aynı instance methodlarda olduğu gibi, class methodlarda da class attribute'lara atıfta bulunabilirsiniz (refers to). Örnek:
```py
class A:
    attri = "class attribute"

    def func1(self):
        temp = self.attri
        return temp

    @classmethod
    def func2(cls):
        temp = cls.attri
        return temp

var = A()
print(A.attri, id(A.attri))         # Output: class attribute 2432006980784
print(var.func1(), id(var.func1())) # Output: class attribute 2432006980784
print(A.func2(), id(A.func2()))     # Output: class attribute 2432006980784
print(A.attri==A.func2()==var.func1()==var.func2()) # Output: True
```

**Not:** Class methodlara illa main class'dan (`A.func2()` gibi) ulaşacaksınız diye bir kural yok. Class methodlara instance'lardan da ulaşabilirsiniz (`var.func2()` gibi). Ama hata (exception) riskini en aza indirmek için class methodlara main class'dan ulaşmak daha akıllıca bir seçimdir.

Class methodlar yerine göre kullanışlı olabilir. Örnek:
```py
class A():
    liste = []

    def __init__(self, list_item):
        self.list_item = list_item
        self.listeye_ekle()

    def liste_uzunluğu(self):
        print(len(self.liste))

    def listeye_ekle(self):
        self.liste.append(self.list_item)

A.liste_uzunluğu(A("Item_1")) # Output: 1
var1 = A("Item_1")
var1.liste_uzunluğu() # Output: 2
var2 = A("Item_1")
var1.liste_uzunluğu() # Output: 3
```
Bu kodda `len(self.liste)`'nin `0` olduğu bir durum yoktur çünkü `liste_uzunluğu` methodunu çağırmak için instantiation işlemi yapmak zorundasınız. Instantiation işlemi yapınca da `__init__` çağırılır ve `liste` class attribute'una belirtilen öğe eklenir. Bu yüzden `liste` listesinin uzunluğu `1` olur. Bu gibi durumların önüne geçmek için class method'lar kullanılabilir. Örnek:
```py
class A():
    liste = []

    def __init__(self, list_item):
        self.list_item = list_item
        self.listeye_ekle()

    @classmethod
    def liste_uzunluğu(self):
        print(len(self.liste))

    def listeye_ekle(self):
        self.liste.append(self.list_item)

A.liste_uzunluğu() # Output: 0
var = A("Item_1")
var.liste_uzunluğu() # Output: 1
```
Bunun dışında alternatif çözümler vardır ama tavsiye edilmez. Örnek:
```py
def liste_uzunluğu():
    print(len(Class.liste))

class A():
    liste = []

    def __init__(self, list_item):
        self.list_item = list_item
        self.listeye_ekle()

    def listeye_ekle(self):
        self.liste.append(self.list_item)

liste_uzunluğu() # Output: 0
var = A("Item_1")
liste_uzunluğu() # Output: 1
```
`liste_uzunluğu` fonksiyonunu `A` class'ının dışına tanımlayarak sorunu çözebilirsiniz ama böyle yaparsanız `A` class'ının bütünlüğünü bozarsınız. Bir main class'ın bütünlüğünü bozulması aşağıdaki sorunlara yol açar:
- `liste_uzunluğu()` fonksiyonu `A` class'ının dışında tanımlandığı için `dir(A)` kodunun döndürdüğü liste içerisinde `liste_uzunluğu()` fonksiyonu bulunmaz. Bu da bazı durumlarda dezavantaja neden olur.
- `liste_uzunluğu()` fonksiyonu `A` class'ının dışında tanımlandığı için başka bir dosyada (Örneğin `Modul_B` isimli bir dosyada) tanımlanmış `A` class'ını `from Modul_B import A` örneğindeki gibi import ettiğimizde `liste_uzunluğu()` fonksiyonu `A` class'ının dışında tanımlandığı için içeri import edilmez ve dolayısıyla bu fonksiyonu ayrıyetten `from Modul_B import liste_uzunluğu` şeklinde import etmeden kullanamayız.

<h2 id="3.3">Static Methods</h2>

Python'da `@` işareti kullanılanılarak oluşturulan yapılara **decorator** denir (daha önce anlattım). Python'da class method tanımlamak için `@staticmethod` decorator'u kullanılır. Bu sayede decode edilen method, `staticmethod` class'ının (`builtins.pyi`'de `class staticmethod`) işlevselliğini kazanır. Başka bir deyişle, `@staticmethod` decorator'u kendinden sonraki fonksiyonun bir static method olduğunu Python'a bildirir.

`@staticmethod` decorator'u ile decore edilen methodlar, main class'ın `__dict__` methodunda `<staticmethod object at 0x0000019A1FBF12E0>` şeklinde depolanmışken, function olarak `<function A.static_method_exp at 0x0000019A1FBE9940>` şeklinde depolanmıştır. `<function A.static_method_exp at 0x0000019A1FBE9940>` yazısı "`A` class'ının `static_method_exp` methodu" anlamına gelmektedir. Örnek:
```py
class A:
    @staticmethod
    def static_method_exp():
        pass

print(A.__dict__["static_method_exp"]) # Output: <staticmethod object at 0x0000019A1FBF12E0>
print(A.static_method_exp) # Output: <function A.static_method_exp at 0x0000019A1FBE9940>
print(type(A.__dict__["static_method_exp"])) # Output: <class 'staticmethod'>
print(callable(A.__dict__["static_method_exp"])) # Output: False
print(callable(A.static_method_exp)) # Output: True
```
Yukarıda da gördüğünüz gibi `<function A.static_method_exp at 0x0000019A1FBE9940>` objesi çağırılabilirdirken (callable) `<staticmethod object at 0x0000019A1FBF12E0>` objesi çağırılabilir (callable) değildir. Bu yüzden python `A` class'ının, `A` class'ının `static_method_exp` objesine bağlı methodu (`<function A.static_method_exp at 0x0000019A1FBE9940>`) kullanır.

**Not:** Main class'ın class method'larında yapılan değişiklikler, bu main class'dan türetilen instance'ların static method'larını da etkiler (aynı instance method'lardaki gibi). Bunun nedenini [Instance Methods](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/OOP/beginning_of_classes.md#3.1 "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/OOP/beginning_of_classes.md#3.1") kısmında anlattım. İlgili kısım:

> ... `__init__` constructor'ı ve instance method kapsamında tanımlanan şeyler dışındaki her şey main class'dan erişilebilir ve değiştirilebilir. Bu değişiklik ilgili main class'dan türetilen instance'ları da etkiler (çünkü instance'lardaki bu objeler main class'dakilere atıfta bulunur). ...

Örnek:
```py
class A:
    @staticmethod
    def func1(self):
        pass

var = A()

print(var.func1) #Output: <function A.func1 at 0x0000018A33AB0040>
A.func1 = 1
print(var.func1) #Output: 1
```

Bir methodun herhangi bir class veya instance attribute'a erişmesi gerekmiyorsa, bu method static method olarak tanımlanıp kullanılabilir. Örnek:
```py
class A():
    
    @staticmethod
    def static_method_exp():
        print("Static method tanımlandı.")

A.static_method_exp() # Output: Static method tanımlandı.
A().static_method_exp() # Output: Static method tanımlandı.
```
Gördüğünüz gibi static methodlara hem main class hem de instance üzerinden erişebiliryoruz. Static methodların herhangi bir class veya instance attribute'a erişmesi gerekmediği için ilk parametresi `self` ya da `cls` gibi özel bir parametre muamelesi görmez, normal bir parametre muamelesi görür. Ama bu, static methodların içinde herhangi bir class ya da instance methoda erişemeyiz veya tanımlayamayız anlamına gelmez. Örnek:
```py
class A:

    def __init__(self):
        pass

    @staticmethod
    def instance_def(self):
        self.a = "A"

    @staticmethod
    def class_def(cls):
        cls.b = "B"
    
    @staticmethod
    def ic_print(self, cls):
        print(self.a, cls.b)

var = A()
var.instance_def(var)
var.class_def(A)
var.ic_print(var, A) # Output: A B
A.ic_print(var, A) # Output: A B
```
Static methodların ilk parametresi `self` ya da `cls` gibi özel bir parametre muamelesi görmediği için `self` ve `cls`'ye ilgili instance ve class'ı argüman olarak vermemiz gerekmektedir.

<h1 id="4">Ekstralar</h1>

<h2 id="4.1">Alternative Constructor</h2>

`__init__` methoduna constructor diyorduk. Alternative Constructor "Constructor'a alternatif" "`__init__` constructor'ına alternatif" anlamına gelmektedir. Direkt bir örnekle anlatayım. Örnek:
```py
class A:
    def __init__(self, name = None):
        self.names = {"Ali": 23,
                      "Veli": 25,
                      "Hasan": 32}
        if not name:
            print("Lütfen bir isim girin.")
        elif not name in self.names:
            print("Girdiğiniz isim listede yok.")
        elif name:
            print(self.names[name])

    @classmethod
    def yas(cls, name = None):
        cls(name)

var = A() # Output: Lütfen bir isim girin.
var_Ayşe = A("Ayşe") # Output: Girdiğiniz isim listede yok.
var_Ali = A("Ali") # Output: 23
var_Veli = A("Veli") # Output: 25
var_Hasan = A("Hasan") # Output: 32

A.yas() # Output: Lütfen bir isim girin.
A.yas("Ayşe") # Output: Girdiğiniz isim listede yok.
A.yas("Ali") # Output: 23
A.yas("Veli") # Output: 25
A.yas("Hasan") # Output: 32
```
Buradaki `cls(name)` gibi kodlara **alternative constructor** denir. Yukarıdaki `cls(name)` kodu `A(name)` anlamına gelmektedir ve `A(name)`'de bir instantiation işlemidir. `A(name)` işleminden sonra tekrar `__init__` constructor'ı çalışır.

<h2 id="4.2"><code>hasattr(obj, name)</code> Fonksiyonu</h2>

`obj` parametresine argüman olarak girilen objenin (instance, main class vs.) `name` parametresinde string type olarak belirtilen isimde bir objeye (attribute, function, property vs.) sahip olup olmadığını sorgular. Varsa `True`, yoksa `False` değerini döndürür. Örnek:
```py
class A:
    xxx = 1

var = A()
print(hasattr(A, "xxx")) # Output: True
print(hasattr(var, "xxx")) # Output: True
print(hasattr(A, "yyy")) # Output: Falsa
print(hasattr(var, "yyy")) # Output: False
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#hasattr "https://docs.python.org/3/library/functions.html#hasattr").

<h2 id="4.3"><code>getattr(obj, name, default)</code> Fonksiyonu</h2>

`obj` parametresine argüman olarak girilen objenin (instance, main class vb.) `name` parametresinde string type olarak belirtilen isimde bir objeye (attribute, function, property vs.) sahip olup olmadığını sorgular. Varsa objeyi, yoksa `default` parametresine argüman olarak girilen string'i döndürür. `default` parametresine argüman girilmezse, olası durumlarda `AttributeError` hatası yükseltilir. Örnek:
```py
class A:
    xxx = "class attribute"

var = A()
print(getattr(A, "xxx", "xxx A'da yok")) # Output: class attribute
print(getattr(var, "xxx", "xxx var'da yok")) # Output: class attribute
print(getattr(A, "yyy", "yyy A'da yok")) # Output: yyy A'da yok
print(getattr(var, "yyy", "yyy var'da yok")) # Output: yyy var'da yok
print(getattr(A, "yyy")) # Output: AttributeError: type object 'A' has no attribute 'yyy'
print(getattr(var, "yyy")) # Output: AttributeError: 'A' object has no attribute 'yyy'
```
`getattr(object, name, default)` fonksiyonunun eşdeğeri `object.name`'dir. Örnek:
```py
class A:
    xxx = "xxx class attribute"

var = A()
print(A.xxx) # Output: class attribute
print(var.xxx) # Output: class attribute
print(A.yyy) # Output: AttributeError: type object 'A' has no attribute 'yyy'
print(var.yyy) # Output: AttributeError: 'A' object has no attribute 'yyy'
```

**Not:** Class'lardaki `__getattribute__` methodu bu build-in fonksiyonu kullanır. `__getattribute__` methodunun `__doc__` methoduna bakarsanız `'Return getattr(self, name).'` görürsünüz.

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#getattr "https://docs.python.org/3/library/functions.html#getattr").

<h2 id="4.4"><code>setattr(obj, name, value)</code> Fonksiyonu</h2>

`obj` parametresine argüman olarak girilen objenin (instance, main class vb.) `name` parametresinde string type olarak belirtilen isimde bir obje (attribute, function, property vs.) varsa, bu objeye `value` parametresinde argüman olarak girilen değeri ya da objeyi atar; yoksa `name` parametresinde string olarak belirtilen isimde bir obje yaratır ve bu objeye `value` parametresinde argüman olarak girilen değeri ya da objeyi atar. `obj` parametresine argüman olarak girilen objede (attribute, function, property vs.) `__dict__` methodu uygulanmadıysa (implements) (yani bu obje `__dict__` methoduna sahip değilse) `setattr()` fonksiyonu çalışmaz. Örnek:
```py
class A:
    xxx = "1. xxx class attribute"

var = A()
print(A.xxx) # Output: 1. xxx class attribute
print(var.xxx) # Output: 1. xxx class attribute

setattr(A, "xxx", "2. xxx class attribute")
print(A.xxx) # Output: 2. xxx class attribute
print(var.xxx) # Output: 2. xxx class attribute

setattr(var, "xxx", "3. xxx class attribute")
print(A.xxx) # Output: 2. xxx class attribute
print(var.xxx) # Output: 3. xxx class attribute

setattr(A, "yyy", "1. yyy class attribute")
print(A.yyy) # Output: 1. yyy class attribute
print(var.yyy) # Output: 1. yyy class attribute

setattr(var, "yyy", "2. yyy class attribute")
print(A.yyy) # Output: 1. yyy class attribute
print(var.yyy) # Output: 2. yyy class attribute

setattr(var, "zzz", "1. zzz class attribute")
print(var.zzz) # Output: 1. zzz class attribute
print(A.zzz) # AttributeError: type object 'A' has no attribute 'zzz'
```

`setattr(object, name, value)` fonksiyonunun eşdeğeri `object.name = value`'dur. Örnek:
```py
class A:
    xxx = "1. xxx class attribute"

var = A()
print(A.xxx) # Output: 1. xxx class attribute
print(var.xxx) # Output: 1. xxx class attribute

A.xxx = "2. xxx class attribute"
print(A.xxx) # Output: 2. xxx class attribute
print(var.xxx) # Output: 2. xxx class attribute

var.xxx = "3. xxx class attribute"
print(A.xxx) # Output: 2. xxx class attribute
print(var.xxx) # Output: 3. xxx class attribute

A.yyy = "1. yyy class attribute"
print(A.yyy) # Output: 1. yyy class attribute
print(var.yyy) # Output: 1. yyy class attribute

var.yyy = "2. yyy class attribute"
print(A.yyy) # Output: 1. yyy class attribute
print(var.yyy) # Output: 2. yyy class attribute

var.zzz = "1. zzz class attribute"
print(var.zzz) # Output: 1. zzz class attribute
print(A.zzz) # AttributeError: type object 'A' has no attribute 'zzz'
```
Gördüğünüz gibi yeni eklenen `yyy` ve `zzz` class attribute gibi davranıyor.

**Not:** Class'lardaki `__setattr__` methodu bu build-in fonksiyonu kullanır. `__setattr__` methodunun `__doc__` methoduna bakarsanız `'Implement setattr(self, name, value).'` yazdığını görürsünüz.

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#setattr "https://docs.python.org/3/library/functions.html#setattr").

<h2 id="4.5"><code>delattr(obj, name)</code> Fonksiyonu</h2>

`obj` parametresine argüman olarak girilen objenin (instance, main class vb.) `name` parametresinde string type olarak belirtilen isimde bir objeye (attribute, function, property vs.) sahipse, bu objeyi siler; değilse `AttributeError` hatası yükseltir. Örnek:
```py
class A:
    class_attri1 = "Class Attribute 1"
    def __init__(self):
        self.instance_attri1 = "Insance Attribute 1"

var = A()
print(var.instance_attri1) # Output: Insance Attribute 1
delattr(var, "instance_attri1")
print(var.instance_attri1) # AttributeError: 'A' object has no attribute 'instance_attri1'

print(A.class_attri1) # Output: Class Attribute 1
delattr(A, "class_attri1")
print(A.class_attri1) # AttributeError: type object 'A' has no attribute 'class_attri1'
```

**Not:** Class'lardaki `__delattr__` methodu bu build-in fonksiyonu kullanır. Bu methodun `__doc__` methoduna bakarsanız `'Implement delattr(self, name).'` yazdığını görürsünüz.

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#delattr "https://docs.python.org/3/library/functions.html#delattr").

<h2 id="4.6"><code>__dict__</code> Methodu</h2>

`__dict__` methodu, bulunduğu objenin içerdiği kendisine ait objelerin bulunduğu bir dictionary objesidir. Örnek:
```py
class A:
    class_attri1 = "Class Attribute 1"
    def __init__(self) -> None:
        self.instance_attri1 = "Instance Attribute 1"

def func():
    pass

var=A()
print(A.__dict__) # Output: {'__module__': '__main__', 'class_attri1': 'Class Attribute 1', '__init__': <function A.__init__ at 0x00000204AB97F160>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
print(var.__dict__) # Output: {'instance_attri1': 'Instance Attribute 1'}
print(func.__dict__) # Output: {}
```

<h2 id="4.7"><code>__doc__</code> Methodu</h2>

Teknik dilde, üç tırnak `""" Falan Filan """` içinde gösterilen karakter dizilerine belge dizisi (docstring) veya belgelendirme dizisi (documentation string) adı verilir. Class'ların `__doc__` niteliğini kullanarak, class'ın belgelendirme dizilerine erişebiliriz. Bu belgelendirme dizileri ilgili class'a tanımladığınız/tanımlanan açıklamalar içerir.

<h2 id="4.8"><code>__name__</code> Methodu</h2>

Class'ın adını (identifier) içeren methoddur.

<h2 id="4.9"><code>__module__</code> Methodu</h2>

Class'un tanımlandığı modülün adını içeren methoddur. Class'ın tanımlandığı modül dosyasında bu method'un sahip olduğu değer `"__main__"`'dir.

<h2 id="4.10"><code>__bases__</code> Methodu</h2>

Bir class'ın miras aldığı base class'ları listeler. MRO'dan (daha sonra anlatılacak) farklıdır. Örnek:
```py
class A:
    pass

class B(A):
    pass

class C(B,A):
    pass

var = "selam"
print(C.__mro__) # Output: (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
print(C.__bases__) # Output: (<class '__main__.B'>, <class '__main__.A'>)
```

<h2 id="4.11"><code>__del__(self)</code> Methodu</h2>

**Destructor** (yıkıcı) olarak bilinen temel aşırı yükleme (overloading) methodudur. Bu methodda bir objenin silinme anında yapılacak işlemlerin belirlenir. Eşdeğeri `del <object>`'dir. Bu method, garbage collector tarafından nesne toplandığında çalışır. Bu yüzden herhangi bir nesneye debugger ile baktığınızda `__del__` methodunu görmezseniz şaşırmayın.

<h2 id="4.12"><code>__repr__(self)</code> Methodu</h2>

Bir temel aşırı yükleme (overloading) methodudur. `repr(obj)` fonksiyonunun yaptığı işi yapar. `__repr__` olarak kullanılacaksa instance üzerinden çağırılması daha sağlıklı olur. Bir class üzerinden çağıralacaksa `self` parametresine argüman girmek zorunludur. Instance `print` fonksiyonu ile kullanıldığında çalışır.

<h2 id="4.13"><code>__str__(self)</code> Methodu</h2>

Bir temel aşırı yükleme (overloading) methodudur. `str(obj)` fonksiyonunun yaptığı işi yapar. `__str__` olarak kullanılacaksa instance üzerinden çağırılması daha sağlıklı olur. Bir class üzerinden çağıralacaksa `self` parametresine argüman girmek zorunludur. Instance `print` fonksiyonu ile kullanıldığında çalışır.

<h2 id="4.14"><code>__add__(self)</code> Methodu</h2>

`+` operatoru ile instance'lar arasında toplama işlemi yapabilmek için `__add__` methodu tanımlamalısınız. Örnek:
```py
class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Vektör ({}, {})'.format(self.x, self.y)

    def __add__(self,other):
        return Vektor(self.x + other.x, self.y + other.y)

v1 = Vektor(2,10)
v2 = Vektor(5,-2)
print(v1 + v2) # Output: Vektör (7, 8)
```

<h2 id="4.15"><code>__new__(cls, *args, **kwargs)</code> Methodu</h2>

Instantiation işleminde `__init__` constructor'ından önce çağırılan methoddur. Kanıtı:
```py
class A:
    def __new__(cls):
        pass

    def __init__(self):
        print("init çalıştı...")

var = A()
```
Gördüğünüz `__new__` methodunu geçersiz kıldığım (override) için işlevselliğini kaybetti. İşlevselliğini kaybettiği için işlevleri arasında `__init__` methodu ile ilgili olan kısmı da kaybetti. Bu yüzden `__init__` methodu düzgün çalışmadı. Düzgün hali:
```py
class A:
    def __new__(cls):
        return object.__new__(cls)

    def __init__(self):
        print("init çalıştı...")

var = A() # Output: init çalıştı...
```
Burada `__new__` methodu `object.__new__(cls)` koduyla object base class'ının `__new__` methodunu miras alarak `__new__` methodunun işlevselliğini geri kazandırmış olduk. Bu yüzden `__init__` methodu düzgün çalıştı.