# İçindekiler

- [Class](#1)
    - [Class Definition](#1.1)   
    - [Instantiation](#1.2)      
- [Attributes](#2)
    - [Class Attributes](#2.1)   
    - [Instance Attributes](#2.2)
- [Methods](#3)
    - [Instance Methods](#3.1)   
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

**Not:** "Class'lar, obje yaratmak için kullanılan bir code template'dir (kod şablonu)." dedim diye class'lar obje değildir diye düşünmeyin. Python'da `if`, `def`, `and`, `or` gibi keyword, statement ve operator'lar hariç her şey (class'lar dahil) bir objedir. Bunlara ulaşmak için [tıklayınız](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/statements/statements_and_keywords.md "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/statements/statements_and_keywords.md").

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

**Not:** Bu durum, import işlemlerinde de yaşanır çünkü import edilen dosya baştan sona kadar okunur, class'ların içerikleri de dahil.

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

Main class'dan türetilen, türetildiği class'ın method, attribute, property vb. objelerine sahip olan objelere **instance** denir ("object = instance = obje = nesne" hepsi aynı şey). Bu işleme de **Instantiation** denir. Örnek:
```py
class A:
    pass

var = A()
```
Gördüğünüz gibi `A` class'ını (`__main__.A`) `A()` şeklinde çağırdığımızda (call) bir instance objesi yaratmış (create) oluyoruz (`<__main__.A object at 0x0000022782837730>`). `<__main__.A object at 0x0000022782837730>` yazısı "`0x0000022782837730` konumundaki `A` class'ının nesnesi (yani A class'ından türetilmiş instance)" anlamına gelmektedir. Bu instance'ı bir variable'a atayarak (veya atamadan da) programınızda kullanabilirsiniz. Örnek:
```py
class A:
    pass

A()
var = A()

print(A) # Output: <class '__main__.A'>
print(var) # Output: <__main__.A object at 0x0000016B43BFDFD0>
```
Python, `A()` kodunun bulunduğu statement'ı okuduğunda bir instance yaratır ama bir sonraki statement'a geçtiğinde, yarattığı bu instance herhangi bir variable'a atanmadığı için bellekten silinir. Bu yüzden tek kullanımlıktır.

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
print(var.__dict__) # Output: {}

A.class_attri = "New Class Attribute"
print(A.class_attri) # Output: New Class Attribute
print(var.class_attri) # Output: New Class Attribute
print(var.__dict__) # Output: {}

var.class_attri = "Instance attribute"
print(A.class_attri) # Output: Class Attribute
print(var.class_attri) # Output: Instance Attribute
print(var.__dict__) #Output: {'class_attri': 'Instance attribute'}
```
`__dict__` methodunun ne işe yaradığını daha sonra daha detaylı anlatacağım. Şimdilik `__dict__` methodunun ilgili class ya da instance'ın içerdiği objelerin (method, property, attribute vs.) bulunduğu bir `dict` olarak düşünebilirsiniz. Yukarıdaki koddan çıkarmanız gereken sonuçlar:
- Main class'ın class attribute'larında yapılan herhangi bir değişiklik, bu main class'dan türetilen instance'ları da etkiler.
- Main class'dan türetilen instance'ın class attribute'unda yapılan bir değişiklik, main class'ı ve diğer instance'ları etkilemez çünkü ilgili instance'ın class attribute'u artık main class'ın class attribute'undan farklı bir objedir (artık instance attribute'dur da denilebilir).

**Not:** Class attribute'lar, instance'larda `__class__` adında bir method'da depolanırlar (`__class__` methodunun ne olduğu daha sonra anlatılacak).

Üzerinde yeniden tanımlama (redefinition) işlemi yapılan her class attribute farklı bir objeye dönüşür (ID'leri değişir). İçerdiği value'yu değiştirmek için yeniden tanımlama (redefinition) işleminin zorunlu olduğu değiştirilemez (immutable (`bool`, `int`, `float`, `complex`, `tuple`, `frozenset`, `bytes`, `str`, `range` vb.)) data type'larda bu durumun önüne geçemeyiz ama değiştirilebilir (mutable (`list`, `set`, `dict`, `bytearray` vb.)) data type'larda geçebiliriz. Örnek:
```py
class A:
    class_attri_1 = "String"
    class_attri_2 = 1
    class_attri_3 = 1.1234
    class_attri_4 = 5+5j
    class_attri_5 = tuple([1,2,3])
    class_attri_6 = frozenset([1,2,3])

    class_attri_7 = [1,2,3]
    class_attri_8 = set([4,5,6])
    class_attri_9 = {"yedi":7, "sekiz":8, "dokuz":9}

var1 = A()
var2 = A()

var2.class_attri_1 = "Değiştirilmiş String"
var2.class_attri_2 = 9
var2.class_attri_3 = 9.9876
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
var1.class_attri_3: 1.1234
var1.class_attri_4: (5+5j)
var1.class_attri_5: (1, 2, 3)
var1.class_attri_7: [1, 2, 3, 'new_item']
var1.class_attri_8: {4, 5, 6, 'new_item'}
var1.class_attri_9: {'yedi': 7, 'sekiz': 8, 'dokuz': 9, 'new': 'item'}
---------------------------------------------------------------------
var2.class_attri_1: Değiştirilmiş String
var2.class_attri_2: 9
var2.class_attri_3: 9.9876
var2.class_attri_4: (9+9j)
var2.class_attri_5: (9, 8, 7)
var2.class_attri_6: frozenset({4, 5, 6})
var2.class_attri_7: [1, 2, 3, 'new_item']
var2.class_attri_8: {4, 5, 6, 'new_item'}
var2.class_attri_9: {'yedi': 7, 'sekiz': 8, 'dokuz': 9, 'new': 'item'}
```
**ID'ler:**
|  | Class Attri 1 | Class Attri 2 | Class Attri 3 | Class Attri 4 | Class Attri 5 | Class Attri 6 | Class Attri 7 | Class Attri 8 | Class Attri 9 |
| :-: |-|-|-|-|-|-|-|-|-|
| A | 2193358095600 | 2193355729200 | 2193358170704 | 2193358170128 | 2193358391744 | 2193358336736 | 2193358095680 | 2193358339424 | 2193358020864 |
| var1 | 2193358095600 | 2193355729200 | 2193358170704 | 2193358170128 | 2193358391744 | 2193358336736 | 2193358095680 | 2193358339424 | 2193358020864 |
| var2 | 2193358212528 | 2193355729456 | 2193358170608 | 2193358170672 | 2193358391872 | 2193358338976 | 2193358095680 | 2193358339424 | 2193358020864 |

Mutable data type'ların methodlarını kullanmak yerine yeniden tanımlama (redefinition) işlemi uygulasaydık, mutable data type'lar da farklı bir objeye dönüşecekti (ID'leri değişecekti).

<h2 id="2.2">Instance Attributes</h2>

Sadece instance methodların (daha sonra anlatılacak) veya `__init__` constructor'ının kapsamında tanımlanabilen variable'lara **instance attribute** denir. Instance attribute'lara sadece instance'lar üzerinden ulaşabilir, main class üzerinden ulaşılamaz. Örnek:
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

print(A.a) # AttributeError: type object 'A' has no attribute 'a'

var = A()
print(var.a, var.b, var.c) # Output: 1 2 3

var.func()
print(var.a, var.b, var.c) # Output: 4 5 6

print(A.a) # AttributeError: type object 'A' has no attribute 'a'
```
Gördüğünüz gibi instance attribute'lara instance üzerincen ulaşılabilirken, main class üzerinden, `A.a` methodunu `A()` kodundan önce veya sonra talep etmemiz farketmeksizin ulaşılamadı.

**Not:** Python `A` class'ını ilk kez okurken `__init__`, `func` gibi fonksiyonların da içeriğini okumaz. Fonksiyonları okuduktan sonra fonksiyon objelerini oluşturur ve öyle bırakır. Instance attribute'ların oluşturulabilmesi için bu attribute'ların tanımlandığı `__init__` veya user-definition fonksiyonların en az bir kere çağırılması (call) gerekmektedir. Örnek:
```py
class A:
    def __init__(self) -> None:
        pass

    def func(self):
        self.a = "A"

var = A()
try:
    print(id(var.a),var.a) # AttributeError: 'A' object has no attribute 'a'
except:
    pass
var.func()
print(id(var.a),var.a) # Output: 2525676855472 A
var.a = "D"
print(id(var.a),var.a) # Output: 2525677165680 D
var.func()
print(id(var.a),var.a) # Output: 2525676855472 A
```
Gördüğünüz gibi `func` user-defined fonksiyonunu çağırmadan `a` instance attribute'una ulaşamıyoruz. Bu fonksiyonu her çağırdığımızda da `a` instance attribute'u eski değerine ve ID'sine sahip oluyor (yani ilk obje oluyor).

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
Bir class'ın `__dict__` methodunda, bu class içinde bulunan objelerin en salt hallerini (obje isimlerini) bulabilirsiniz. Gördüğünüz gibi `classmethod` ya da `staticmethod` decorator'ı ile decore edilen fonksiyonlar `classmethod object` ya da `staticmethod object` şeklide depolanırken, instance methodlar direkt fonksiyon objesi olarak depolanır. Yani fonksiyon objesi olarak depolananlara literatürde instance method diyoruz. Gördüğünüz gibi aksi belirtilmediği için `func1` fonksiyonu ve `__init__` constructor'ı instance methoddur.

**Not:** Instance methodlar birer fonksiyon objesi (`builtins.pyi`'de `class function`) olarak depolanırken, class methodlar classmethod objesi (`builtins.pyi`'de `class classmethod`), static methodlar staticmethod objesi (`builtins.pyi`'de `class staticmethod`) depolanır.

Main class'ın instance method'larında yapılan değişiklikler, bu main class'dan türetilen instance'ların instance method'larını da etkiler. Bu durum class attribute'larınkine benziyor. Buradan, class method'lar hariç bütün methodların kapsamında tanımlanan her şey instance'lara özelken, direkt olarak main class'ın kapsamında (enclosing scope) tanımlanan (class attribute'lar, class-instance-static method'lar, property objeleri vs.) objelerin üzerinde yapılan değişiklikler bu class'dan türetilen instance'ları da etkiler. Örnek:
```py
class A:
    def __init__(self):
        pass

    def func1(self):
        pass

var = A()

print(A.__init__) #Output: <function A.__init__ at 0x000002A120928040>
print(var.__init__) #Output: <bound method A.__init__ of <__main__.A object at 0x000002A120924FD0>>
A.__init__ = 1
print(A.__init__) #Output: 1
print(var.__init__) #Output: 1

print(A.func1) #Output: <function A.func1 at 0x0000020D701880D0>
print(var.func1) #Output: <bound method A.func1 of <__main__.A object at 0x0000020D70184FD0>>
var.func1 = 1
print(A.func1) #Output: <function A.func1 at 0x00000246483180D0>
print(var.func1) #Output: 1
```
Gördüğünüz gibi `A` class'ının `__init__` methodunda yapılan bir değişiklik `A` class'ından türetilen `var` instance'ını da etkilerken, benzer şeyin `var` instance'ında yapılması `A` class'ını etkilemez.

Instance methodların ve `__init__` constructor'ının ilk parametresi özel bir anlama sahiptir. Bu parametre `self` olmalıdır çünkü bu bir syntax kuralıdır. Aksi halde `TypeError: func() takes 0 positional arguments but 1 was given` gibi bir hata alırsınız. Örnek:
```py
class A:
    self.attri = 1 # NameError: name 'self' is not defined
    def __init__(self):
        self.attri = 2
```
Bu parametreye farklı isimler de verebilirsiniz ama `self`, programcılar camiasında kalıplaşmış bir kullanım olmasından dolayı tercih edilir. Örnek:
```py
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
Buradan şunu çıkarabilirsiniz; instance methodların ilk parametresi olan `self` identifier'ı sadece bir identifier'dan ibaret. Asıl önemli olan instance methodların ilk parametresinin kendisidir.

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
Buradan yola çıkarak, örneğin `self.a = 1` kodunun `A().a = 1` anlamına geldiği sonucunu çıkarabiliriz. `self.a = 1` kodunun `A().a = 1` anlamına gelmesi, instantiation işlemini anlamada önemli bir yere sahiptir. Örnek:
```py
class A:
    def __init__(self):
        pass

var = A()
var.a = 1
var.b = 2
var.c = 3
print(var.a, var.b, var.c) # Output: 1 2 3
```
`__init__` constructor'ında herhangi bir instance attribute tanımlı olmamasına rağmen `var` instance, `var.a = 1`, `var.b = 2` ve `var.c = 3` statement'larından sonra 3 farklı instance attribute'a sahip oldu. Kanıtı:

![](https://i.ibb.co/2sSjmq9/image.png)

Instantiation işlemi de tam da bu şekilde çalışır. Instantiation işleminde otomatik olarak `__init__` constructor'ı çağırılır ve yukarıdaki olayın aynısı gerçekleşir. Örnek:
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
Buradaki `self` parametresine Python tarafından `var = A()` kodundaki `A()` kodunun yarattığı instance argüman olarak girilir. Bu argümana temsili olarak `X` dersek, `self.a = 1`, `self.b = 2`, `self.c = 3` kodları `X.a = 1`, `X.b = 2`, `X.c = 3` anlamına gelmektedir. Yukarıdaki olayı `setattr()` (daha sonra anlatılacak) build-in fonksiyonunu kullanarak da yapabilirsiniz.

<hr>

İlk olarak `__init__` constructor'ından bahsedelim.

`__init__`, yapıcı (constructor) olarak bilinen, main class'dan instance türetilirken ilk çağırılan temel aşırı yükleme (overloading) methodudur. `__init__(self, *args, **kwargs)` syntax'ına sahiptir. `__init__` constructor'ı initialization (başlatma, ilklendirme) işleminden sorumludur. `__new__` methodunda yapılabilecek hemen hemen her şeyi `__init__` methodunda da yapılabildiği için  `__new__` methodu yerine `__init__` methoduna 'constructor' denmektedir.

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

`A` class'ından türetilen instance'lardaki `__init__` constructor'ları, `A` class'ının init constructor'ı ile ilişkilidir (bound) ve `<bound method A.__init__ of <__main__.A object at 0x000001D3687A13D0>>` şeklinde depolanır. `<bound method A.__init__ of <__main__.A object at 0x000001D3687A13D0>>` bu "`0x000001D3687A13D0` konumundaki `A` class'ının nesnesinin (yani A class'ından türetilmiş instance'ının), `A` class'ının `__init__` objesine bağlı method" anlamına gelmektedir. "`A` class'ının `__init__` methoduna bağlı method" olduğu için `A` class'ının `__init__` constructor'ına yaptığımız müdahaleler, `A` class'ından türetilen instance'ları da etkiler (daha önce söylemiştim). Kanıtı:
```py
class A:
    def __init__(self):
        pass

var1 = A()
var2 = A()

A.__init__ = "Hello"
print(var1.__init__) # Output: "Hello"
print(var2.__init__) # Output: "Hello"
```
**Not:** `__init__` constructor'ının mekanizması, Python geliştiricileri tarafından titizlikle ayarlanmıştır. Bu yüzden yukarıdaki gibi bu methodu kurcalamayın. Bu methodu işlevi doğrultusunda kullandığınız sürece sorun yaşamazsınız. Artık buradan sonraki kısımlarda `__init__` constructor'ının ve instance methodların kullanım alanlarını ve özelliklerini göreceğiz.

<hr>

Bir main class'dan her instance türetildiğinde, türetilen her instance kendisine özel instance attribute'lara sahip olur. Örnek:
```py
class A:
    attri = 1
    def __init__(self):
        self.attri2 = 2

var1 = A()
```
`var1` instance'ına debugger ile aşağıdaki gibi baktığımızda instance ve class attribute'ları ayırt edemeyiz.

![](https://i.ibb.co/C7YsqcS/image.png)

Ama ilgili instance'ın special variables sekmesindeki `__dict__` methoduna baktığımızda instance attribute'ları ayırt edebiliriz.

![](https://i.ibb.co/Q6qwGZM/image.png)

Gördüğünüz gibi `attri2` attribute'unun bir instance attribute olduğunu bu şekilde ayırt edebildik. Her instance, kedisine özel instance attribute'ları bu şekilde saklar Instance methodlarda tanımlanmış instance attribute'lar için de bu geçerlidir. Instance methodlar `__init__` gibi instantiation işleminde otomatik olarak çağırılmadığı (call) için içindeki instance attribute'ların bellekte depolanması için en az 1 kere elle çağırmamız gerekmektedir (daha önce anlattım). Örnek:
```py
class A:
    def __init__(self):
        self.attri1 = 123
    
    def func(self):
        self.attri2 = 12334

var = A()
print(var.__dict__) # Output: {'attri1': 123}
var.func()
print(var.__dict__) # Output: {'attri1': 123, 'attri2': 12334}
```
Bu işlemin otomatik gerçekleşmesini istiyorsanız, ilgili instance methodu `__init__` içinde çağırabilirsiniz. Böylece instantiation işleminde `__init__` otomatik olarak çağırılınca ilgili instance method da otomatik çağırılmış olur. Örnek:
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
**Not:** `func()` fonksiyonunun içindeki `attri2` instance attribute'una `var.func().attri2` şeklinde ulaşmaya çalışırsanız `AttributeError: 'NoneType' object has no attribute 'attri2'` hatası alırsınız. Örnek:
```py
class A():

    def func(self):
        self.attri2 = "func attribute"
        
var = A()
print(var.func().attri2) # AttributeError: 'NoneType' object has no attribute 'attri2'
```
[Fonksiyonlar (Functions)](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/fonksiyonlar/functions.md "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/fonksiyonlar/functions.md") konusunu anlayan, yukarıdaki hatanın sebebini zaten biliyordur. Bilmeyenler için anlatayım. Python dahil çoğu programlama dili [aritmetik işlem mantığıyla](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/basic_concepts.md#2 "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/basic_concepts.md#2") kodları çalıştırır. `var.func().attri2` kodu şu sırayla çalışır:
1. Python önce `var` instance'ı üzerinden `func` methodunu çağırır.
2. `func` method'unda herhangi bir `return` statement olmadığı için `func` method'u `NoneType` (`<class 'NoneType'>`) döndürür.
3. Bu işlemlerden sonra `var.func().attri2` kodu Python'ın gözünde `NoneType.attri2` koduna dönüşür.
4. `NoneType` class'ının `attri2` adında bir methodu olmadığı için `AttributeError: 'NoneType' object has no attribute 'a_yazdir_attribute'` hatası yükseltilir.

Peki `func` methoduna `return self.attri2` statement eklersek? Örnek:
```py
class A():

    def func(self):
        self.attri2 = "func attribute"
        return self.attri2
        
var = A()
print(var.func().attri2) # AttributeError: 'str' object has no attribute 'attri2'
```
`var.func().attri2` kodu şu sırayla çalışır:
1. Python önce `var` instance'ı üzerinden `func` methodunu çağırır.
2. `func` method'u `self.attri2` instance attribute'unun value'su olan `"func attribute"` string'ini (`<class 'str'>`) döndürür.
3. Bu işlemlerden sonra `var.func().attri2` kodu Python'ın gözünde `"func attribute".attri2` koduna dönüşür.
4. `"func attribute"` bir string (`str`) objesidir. `str` class'ının `attri2` adında bir methodu olmadığı için `AttributeError: 'str' object has no attribute 'attri2'` hatası yükseltilir.

**Not:** Instance'larda bulunan `__class__` methodu, bu instance'ın türetildiği main class objesini içermektedir. Class attribute'lar vb. diğer bütün objelere buradan ulaşabilirsiniz.

Class attribute'lar, instance'ların special variables sekmesindeki `__class__` methodunda tanımlıdır. Kanıt:
```py
class A:
    attri = 1
    def __init__(self):
        pass

var1 = A()
```

![](https://i.ibb.co/Yb0WsY8/image.png)

Her instance'ın kendisine özel instance attribute'lara sahip olması bize herhangi bir çakışmaya maruz kalmadan yeniden tanımlama (redefinition) ve aynı obje üzerinde (`A().attribute.append` gibi) işlem yapma özgürlüğü sağlar. Örnek:
```py
class A:
    def __init__(self):
        print("init çalıştı...")
        self.attri_1 = 1
        self.attri_2 = []

var1 = A() # Output: init çalıştı...
var2 = A() # Output: init çalıştı...

var1.attri_2.append("item1")
print(var1.attri_2) # Output: ['item1']
print(var2.attri_2) # Output: []
```
Buradaki `attri_1` ve `attri_2` instance attribute'lardır (`__dict__` methoduna bakabilirsiniz). Bu yüzden `var1`'de yapılan değişiklikler `var2`'yi etkilemez. Burada dikkat edilmesi gereken şey; her instance'ın kendi instance attribute'larına sahip olması, her instance'ın kendi `__init__` constructor objesine de sahip olduğu anlamına gelmez. Instance'lardaki `__init__`  constructor objeleri, main class'ın `__init__` constructor objesi ile ilişkilidir (bound). Kanıtı:
```py
class A:
    def __init__(self):
        self.attri = 1

var = A()
print(var.attri) # Output: 1

var.attri = 2
print(var.attri) # Output: 2

var.__init__()
print(var.attri) # Output: 1
```
Gördüğünüz gibi `var` instance'ının `attri` instance attribute'unun value'sunu `2` olarak değiştirsek bile, `var.__init__()` koduyla `var` instance'ı üzerinden `A` class'ının `__init__` constructor'ı ile ilişkili `__init__` constructor'ını (bound method) çağırdığımızda, `attri` instance attribute'unun value'su tekrar `1` oluyor.

Bir instance'da `__init__` constructor'ının içinde instance attribute olarak ve dışında class attribute olarak aynı isimde iki attribute varsa, bu instance, `__init__` constructor'ının içindeki instance attribute'u dikkate alır. Bu durum büyük ihtimal instance attribute'un class attribute'u geçersiz kılmasından (overrite) kaynaklanmaktadır. Ama hala class attribute'a erişilebilir. Örnek:
```py
class A:
    attri_1 = 2
    def __init__(self):
        print("init çalıştı...")
        self.attri_1 = 1

var = A() # Output: init çalıştı...
print(var.attri_1) # Output: 1
print(var.__class__.attri_1) # Output: 2
print(A.attri_1) # Output: 2
```
Gördüğünüz gibi class attribute'a, `var` instance'ın `__class__` methodundan veya direkt `A` class'ından erişebiliriz.

Sıfırdan bir instance attribute tanımlayabileceğiniz gibi, class attribute'lara da atıfta bulunabilirsiniz (refers to). Örnek:
```py
class A():
    attri = 1
    def __init__(self):
        self.attri

var = A()
print("A attribute:  ", A.attri, "|", id(A.attri))
print("var attribute:", var.attri, "|", id(var.attri))

A.attri = 2
print("A attribute:  ", A.attri, "|", id(A.attri))
print("var attribute:", var.attri, "|", id(var.attri))

var.attri = 3
print("A attribute:  ", A.attri, "|", id(A.attri))
print("var attribute:", var.attri, "|", id(var.attri))
```
**Output:**
```
A attribute:   1 | 2488037894448
var attribute: 1 | 2488037894448
A attribute:   2 | 2488037894480
var attribute: 2 | 2488037894480
A attribute:   2 | 2488037894480
var attribute: 3 | 2488037894512
```
`var` variable'ına atanan instance'a temsili olarak `X` dersek; Buradaki `self.attri`, `X.attri` anlamına gelmektedir. `X.attri`'de direkt `attri` class attribute'a atıfta bulunduğu (refers to) için hata yükseltmez. Başka bir örnek:
```py
class A():
    liste = []
    def __init__(self):
        self.liste.append("New Item")

print(A.liste) # Output: []

var1 = A()
print(A.liste) # Output: ['New Item']
print(var1.liste) # Output: ['New Item']

var2 = A()
print(A.liste) # Output: ['New Item', 'New Item']
print(var1.liste) # Output: ['New Item', 'New Item']
print(var2.liste) # Output: ['New Item', 'New Item']
```
`var1` variable'ına atanan instance'a temsili olarak `X`, `var2` variable'ına atanan instance'a temsili olarak `Y` dersek: Benzer şekilde buradaki `self.liste` `var1` instance'ı için `X.liste`, `var2` instance'ı için `Y.liste` anlamına gelmektedir. `X.liste` ve `Y.liste`'de direkt `liste` class attribute'a atıfta bulunduğu (refers to) için hata yükseltmez ve üzerinde `append` methodu uygulanabilir. Farklı instance'larda uygulanan `append` methodu aynı class attribute'u etkilediği için yukarıdaki durum oluşur. Başka bir örnek:
```py
class A():
    liste = []
    attri = 1
    def __init__(self):
        self.func()

    def func(self):
        print(self.attri)
        self.liste.append("New Item")

print(A.liste) # Output: []

var1 = A() # Output: 1
print(A.liste) # Output: ['New Item']
print(var1.liste) # Output: ['New Item']

var2 = A() # Output: 1
print(A.liste) # Output: ['New Item', 'New Item']
print(var1.liste) # Output: ['New Item', 'New Item']
print(var2.liste) # Output: ['New Item', 'New Item']
```
Burada `append` işleminin yapıldığı bir instance methodu `__init__` kapsamında çağırdığımız için her instance türetildiğinde `liste` class attribute'a `"New Item"` öğresi ekleniyor.

`__init__` constructor'ı içine tanımlayacağınız variable'ların hepsini `self` ile kullanmak zorunda değilsiniz. Örnek:
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
Gördüğünüz gibi buradaki `sayi_1` ve `sayi_2` local variable'larını `self` ile kullanmadığımız için instance attribute olarak belleğe kaydedilmiyorlar. Bu yüzden bu local variable'lara doğrudan ulaşamayız ama `__init__` constructor'ı kapsamında kullanabiliriz. Aynı şey diğer methodlar'da da geçerlidir. Bu durumu, bir fonksiyonun local variable'larının fonksiyon sonlandıktan sonra bellekten silinmesi olarak düşünebilirsiniz. Örnek:
```py
class A():
    attri1 = 1
    def __init__(self):
        self.attri2 = 2

    def func(self):
        a = 1
        b = 2
        self.attri2 += a + b
        return self.attri2

var = A()
print(var.func()) # Output: 5
```

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
Bir main class'dan instance türetirken eğer `__init__` constructor'ında `self` dışında parametreler de tanımlıysa, yukarıdaki gibi argümanları `self` parametresini atlayarak girmeye başlamalıyız. Python, instance türetirken `self` parametresine gerekli argümanı kendisi otomatik olarak girdiği için böyle yapıyoruz. Ama bu sadece instance'larda geçerlidir. Main class üzerinden herhangi bir instance method veya `__init__` constructor çağırırken `self` parametresine gerekli argümanı elle girmemiz gerekmektedir (nedenini daha önce anlattım). Örnek:
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

**Not:** Yukarıdaki kodda main class üzerinden çağırılan instance method'un veya `__init__` constructor'ının `self` parametresine argüman olarak girilen instance'a göre kodunuz farklı davranabilir. Örnek:
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
Gördüğünüz gibi `self` parametresine argüman olarak girilen instance önemli. `self` parametresinin aslında ne olduğunu daha önce anlatmıştım. Anlattıklarımdan yola çıkarak yukarıdaki durumun sebebini anlayabilirsiniz. Anlamadıysanız comment falan bırakın, dönüş yaparım.

<h2 id="3.2">Class Methods</h2>

Python'da `@` işareti kullanılanılarak oluşturulan yapılara **decorator** denir (daha önce anlattım). Python'da class method tanımlamak için `@classmethod` decorator'u kullanılır. Bu sayede decode edilen method, `classmethod` class'ının (`builtins.pyi`'de `class classmethod`) işlevselliğini kazanır. Başka bir deyişle, `@classmethod` decorator'u kendinden sonraki fonksiyonun bir class method olduğunu Python'a bildirir.

`@classmethod` decorator'u ile decore edilen methodlar, main class'ın `__dict__` methodunda `<classmethod object at 0x0000021910BB3430>` şeklinde bulunur ama function variables kısmında `<bound method A.class_method_exp of <class '__main__.A'>>` şeklinde bulunurlar. `<bound method A.class_method_exp of <class '__main__.A'>>` yazısı "`A` class'ının, `A` class'ının `class_method_exp` objesine bağlı method" anlamına gelmektedir. Örnek:
```py
class A:
    @classmethod
    def class_method_exp(cls):
        pass

print(A.__dict__["class_method_exp"]) # Output: <classmethod object at 0x0000021910BB3430>
print(A.class_method_exp) # Output: <bound method A.class_method_exp of <class '__main__.A'>>
print(callable(A.__dict__["class_method_exp"])) # Output: False
print(callable(A.class_method_exp)) # Output: True
```
Yukarıda da gördüğünüz gibi `<classmethod object at 0x0000021910BB3430>` objesi çağırılabilir (callable) değilken, `<bound method A.class_method_exp of <class '__main__.A'>>` objesi çağırılabilirdir (callable).

Main class'ın class method'larında yapılan değişiklikler, bu main class'dan türetilen instance'ların class method'larını da etkiler (aynı instance method'lardaki gibi). Bunun nedenini [Instance Methods](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/OOP/beginning_of_classes.md#3.1 "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/OOP/beginning_of_classes.md#3.1") kısmında anlattım.

> ... class method'lar hariç bütün methodların kapsamında tanımlanan her şey instance'lara özelken, direkt olarak main class'ın kapsamında (enclosing scope) tanımlanan (class attribute'lar, class-instance-static method'lar, property objeleri vs.) objelerin üzerinde yapılan değişiklikler bu class'dan türetilen instance'ları da etkiler. ...

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

print(A.attri_1, A.attri_2, A.attri_3) # Output: 1 2 3
```
`A` class'ında herhangi bir class attribute tanımlı olmamasına rağmen `A` class'ı `A.attri_1 = 1`, `A.attri_2 = 2` ve `A.attri_3 = 3` statement'larından sonra 3 farklı class attribute'a sahip oldu. Kanıtı:

![](https://i.ibb.co/2Kg6ks7/image.png)

Class attribute create işlemi de tam da bu şekilde çalışır. Örnek:
```py
class A:
    @classmethod
    def func(cls):
        cls.attri_1 = 1
        cls.attri_2 = 2
        cls.attri_3 = 3

print(A.attri_1, A.attri_2, A.attri_3) # AttributeError: type object 'A' has no attribute 'attri_1'
A.func()
print(A.attri_1, A.attri_2, A.attri_3) # Output: 1 2 3
```
Python otomatik olarak `func` class method'undaki `cls` parametresine argüman olarak `A` class'ını girer. Bu yüzden `cls.attri_1 = 1`, `cls.attri_2 = 2`, `cls.attri_3 = 3` kodları `A.attri_1 = 1`, `A.attri_2 = 2`, `A.attri_3 = 3` anlamına gelmektedir. Tabii bu class attribute'ların yaratılması (create) için `func` class method'unun bir kere çağırılması gerekmektedir çünkü Python `A` class'ını okurken `A` class'ının kapsamındaki fonksiyonların içeriğini okumaz, sadece fonksiyon objelerini yaratır (daha önce anlattım). Bu yüzden class attribute'ları aşağıdaki gibi tanımlamanız daha doğru olacaktır:
```py
class A:
    attri_1 = 1
    attri_2 = 2
    attri_3 = 3

print(A.attri_1, A.attri_2, A.attri_3) # Output: 1 2 3
```
Yukarıdaki olayı `setattr()` (daha sonra anlatılacak) build-in fonksiyonunu kullanarak da yapabilirsiniz.

**Not:** Bir method class method olarak tanıtılmamışsa, o methodun `cls` parametresi instance methodlar'daki `self` parametresi gibi davranır. Çünkü `cls` de `self` gibi sadece bir identifier'dır. Bu parametreye farklı isimler de verebilirsiniz ama `cls`, programcılar camiasında kalıplaşmış bir kullanım olmasından dolayı tercih edilir. Örnek: Örnek:
```py
class A:

    @classmethod
    def class_func(ghjk):
        ghjk.b = 2

A.class_func()
print(A.b) # Output: 2
```
Buradan şunu çıkarabilirsiniz; class methodların ilk parametresi olan `cls` identifier'ı sadece bir identifier'dan ibaret. Asıl önemli olan class methodların ilk parametresinin kendisidir.

Instance methodlara main class üzerinden erişemeyiz ama class methodlara hem main class hem de instance üzerinden erişebiliriz. Örnek:
```py
class A:
    @classmethod
    def func(cls):
        return "Class Method Çalıştı."

var = A()
print(A.func()) # Output: Class Method Çalıştı.
print(var.func()) # Output: Class Method Çalıştı.
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

var1 = A("Item_1")
var1.liste_uzunluğu() # Output: 1
```
Bu kodda `len(self.liste)`'nin `0` olduğu bir durum yoktur çünkü `liste_uzunluğu` methodunu sadece bir instance üzerinden çağırabileceğiniz için instantiation işlemi yapmak zorundasınız. Instantiation işlemi yapınca da `__init__` çağırılır ve dolayısıyla `self.listeye_ekle()` kodu yüzünden `listeye_ekle` fonksiyonu çağırılır ve `len(self.liste)`'nin değeri `1` olur. Bu gibi durumların önüne geçmek için class method'lar kullanılabilir. Örnek:
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
- `liste_uzunluğu()` fonksiyonu `A` class'ının dışında tanımlandığı için `dir(A)` kodunun döndürdüğü liste içerisinde `liste_uzunluğu()` fonksiyonunu göremezsiniz. Bu da `dir(A)` kullandığımız kısımlarda bize dezavantaj sağlar.
- `liste_uzunluğu()` fonksiyonu `A` class'ının dışında tanımlandığı için başka bir dosyada (Örneğin `Modul_B` isimli bir dosyada) tanımlanmış `A` class'ını `from Modul_B import A` şeklinde import ettiğimizde, `liste_uzunluğu()` fonksiyonu `A` class'ının dışında tanımlandığı için içeri import edilmez ve dolayısıyla bu fonksiyonu ayrıyetten `from Modul_B import liste_uzunluğu` şeklinde import etmeden kullanamayız.

<h2 id="3.3">Static Methods</h2>

Python'da `@` işareti kullanılanılarak oluşturulan yapılara **decorator** denir (daha önce anlattım). Python'da class method tanımlamak için `@staticmethod` decorator'u kullanılır. Bu sayede decode edilen method, `staticmethod` class'ının (`builtins.pyi`'de `class staticmethod`) işlevselliğini kazanır. Başka bir deyişle, `@staticmethod` decorator'u kendinden sonraki fonksiyonun bir static method olduğunu Python'a bildirir.

`@staticmethod` decorator'u ile decore edilen methodlar, main class'ın `__dict__` methodunda `<staticmethod object at 0x0000019A1FBF12E0>` şeklinde bulunur ama function variables kısmında `<function A.static_method_exp at 0x0000019A1FBE9940>` şeklinde bulunurlar. `<function A.static_method_exp at 0x0000019A1FBE9940>` yazısı "`A` class'ının `static_method_exp` methodu" anlamına gelmektedir. Örnek:
```py
class A:
    @staticmethod
    def static_method_exp():
        pass

print(A.__dict__["static_method_exp"]) # Output: <staticmethod object at 0x0000019A1FBF12E0>
print(A.static_method_exp) # Output: <function A.static_method_exp at 0x0000019A1FBE9940>
print(callable(A.__dict__["static_method_exp"])) # Output: False
print(callable(A.static_method_exp)) # Output: True
```
Yukarıda da gördüğünüz gibi `<staticmethod object at 0x0000019A1FBF12E0>` objesi çağırılabilir (callable) değilken, `<function A.static_method_exp at 0x0000019A1FBE9940>` objesi çağırılabilirdir (callable).

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

Main class'ın static method'larında yapılan değişiklikler, bu main class'dan türetilen instance'ların static method'larını da etkiler. (aynı instance method'lardaki gibi). Bunun nedenini [Instance Methods](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/OOP/beginning_of_classes.md#3.1 "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/OOP/beginning_of_classes.md#3.1") kısmında anlattım.

> ... class method'lar hariç bütün methodların kapsamında tanımlanan her şey instance'lara özelken, direkt olarak main class'ın kapsamında (enclosing scope) tanımlanan (class attribute'lar, class-instance-static method'lar, property objeleri vs.) objelerin üzerinde yapılan değişiklikler bu class'dan türetilen instance'ları da etkiler. ...

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

`obj` parametresine argüman olarak girilen objenin (instance, main class vb.) `name` parametresinde string type olarak belirtilen isimde bir objeye sahip olup olmadığını sorgular. Varsa `True`, yoksa `False` değerini döndürür. Örnek:
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

`obj` parametresine argüman olarak girilen objenin (instance, main class vb.) `name` parametresinde string type olarak belirtilen isimde bir objeye sahip olup olmadığını sorgular. Varsa objeyi, yoksa `default` parametresine argüman olarak girilen string'i döndürür. `default` parametresine argüman girilmezse, olası durumlarda `AttributeError` hatası yükseltilir. Örnek:
```py
class A:
    xxx = "xxx class attribute"

var = A()
print(getattr(A, "xxx", "xxx A'da yok")) # Output: xxx class attribute
print(getattr(var, "xxx", "xxx var'da yok")) # Output: xxx class attribute
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
print(A.xxx) # Output: xxx class attribute
print(var.xxx) # Output: xxx class attribute
print(A.yyy) # Output: AttributeError: type object 'A' has no attribute 'yyy'
print(var.yyy) # Output: AttributeError: 'A' object has no attribute 'yyy'
```

**Not:** Class'lardaki `__getattribute__` methodu bu build-in fonksiyonu kullanır. Bu methodun `__doc__` methoduna bakarsanız `'Return getattr(self, name).'` görürsünüz.

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#getattr "https://docs.python.org/3/library/functions.html#getattr").

<h2 id="4.4"><code>setattr(obj, name, value)</code> Fonksiyonu</h2>

`obj` parametresine argüman olarak girilen objenin (instance, main class vb.) `name` parametresinde string type olarak belirtilen isimde bir obje varsa, bu objeye `value` parametresinde argüman olarak girilen değeri ya da objeyi atar; yoksa `name` parametresinde string type olarak belirtilen isimde bir obje yaratır ve bu objeye `value` parametresinde argüman olarak girilen değeri ya da objeyi atar. `obj` parametresine argüman olarak girilen objede `__dict__` methodu uygulanmadıysa (implements) (yani bu obje `__dict__` methoduna sahip değilse) `setattr()` fonksiyonu çalışmaz. Örnek:
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

**Not:** Class'lardaki `__setattr__` methodu bu build-in fonksiyonu kullanır. Bu methodun `__doc__` methoduna bakarsanız `'Implement setattr(self, name, value).'` yazdığını görürsünüz.

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#setattr "https://docs.python.org/3/library/functions.html#setattr").

<h2 id="4.5"><code>delattr(obj, name)</code> Fonksiyonu</h2>

`obj` parametresine argüman olarak girilen objenin (instance, main class vb.) `name` parametresinde string type olarak belirtilen isimde bir objeye sahipse, bu objeyi siler; değilse `AttributeError` hatası yükseltir. Örnek:
```py
class A:
    xxx = "1. xxx class attribute"

var = A()
delattr(A, "xxx") # xxx attribute silindi.
delattr(var, "xxx") # AttributeError: xxx
```

**Not:** Class'lardaki `__delattr__` methodu bu build-in fonksiyonu kullanır. Bu methodun `__doc__` methoduna bakarsanız `'Implement delattr(self, name).'` yazdığını görürsünüz.

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#delattr "https://docs.python.org/3/library/functions.html#delattr").

<h2 id="4.6"><code>__dict__</code> Methodu</h2>

Daha önce `__dict__` methodunun, bulunduğu class'ın içerdiği objelerin bulunduğu sözlük olduğunu söylemiştik. Kısaca `__dict__` methodu, bulunduğu class'ın namespace'inde bulunan objeleri içeren dictionary'dir (namespace'in ne olduğu daha önce anlatıldı).

<h2 id="4.7"><code>__doc__</code> Methodu</h2>

Teknik dilde, üç tırnak `""" Falan Filan """` içinde gösterilen karakter dizilerine belge dizisi (docstring) veya belgelendirme dizisi (documentation string) adı verilir. Class'ların `__doc__` niteliğini kullanarak, class'ın belgelendirme dizilerine erişebiliriz. Bu belgelendirme dizileri, class ilgili açıklamalar içerir.

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

**Destructor** (yıkıcı) olarak bilinen temel aşırı yükleme (overloading) methodudur. Bu methodda bir objenin silinme anında yapılacak işlemlerin belirlenir. Eşdeğeri `del <object>`'dir. Bu method garbage collector tarafından nesne toplandığında çalışır. Bu yüzden herhangi bir nesneye debugger ile baktığınızda `__del__` methodunu görmezseniz şaşırmayın.

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