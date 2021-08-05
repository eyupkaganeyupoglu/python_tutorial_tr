# Class
Class'lar, obje yaratmak için kullanılan bir code template'dir (kod şablonu). Class'lar bizi belli obje ve fonksiyon gruplarını her seferinde en baştan yazma zahmetinden kurtarır. Çünkü bir class'dan, bu class'ın bütün içeriğine sahip istediğimiz sayıda **instance** adı verilen objeler üretilebilir.

## Class Definition
`class <class_name>` statement kullanılarak class tanımlayabilirsiniz. Örnek:
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
```

<img src="https://i.ibb.co/T8yYpbG/image.png" alt="image" border="0">

**Not:** Bu durum bu, import işlemlerinde de yaşanır çünkü import edilen dosya baştan sona kadar okunur, class'ların içerikleri de dahil.

**Not:** `modul.py` dosyasındaki `A` class'ını kullanmak için `modul.py` dosyasını `import modul` statement ile import ettikten sonra `modul.A` şeklinde kullanabileceğiniz gibi, `form modul import A` şeklinde class'ı import edip `modul` prefix'i olmadan da kullanabilirsiniz. Örnek:
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
Yukarıdaki kodları anlamadıysanız buradan sonraki **Instantiation** başlığındakileri öğrendikten sonra buraya tekrar bakınız.

## Instantiation
Main class'dan türetilen, türetildiği class'ın method (class'a tanımlanan fonksiyonlar) ve attribute'larına (class'a tanımlanan variable'lar) sahip olan objelere **instance** denir ("object = instance = obje = nesne" hepsi aynı şey). Bu işleme de **Instantiation** denir. Örnek:
```py
class A:
    pass

var = A()
```
Gördüğünüz gibi `A` class'ını (`__main__.A`) `A()` şeklinde çağırdığımızda (call), elimize bir instance geçiyor (`<__main__.A object at 0x0000022782837730>`). Bu instance'ı bir variable'a atayarak programınızda kullanabilirsiniz. Bu instance'ı bir variable'a atamadan da kullanabilirsiniz. Örnek:
```py
class A:
    pass

A()
```
Python `A()` kodunun bulunduğu statement'ı okuduğunda bir instance yaratır ama bir sonraki statement'a geçtiğinde yarattığı bu instance bellekten silinir. Bu yüzden tek kullanımlıktır.

## Class Attributes
Class methodların (daha sonra anlatılacak) veya doğrudan class'ların içinde, `__init__` ya da (class method hariç) herhangi bir user-defined fonksiyonun kapsamının dışında tanımlanan, değer tutan/depolayan variable'lara **class attribute** denir. Örnek:
```py
class A:
    class_attribute = "Class Attribute"

var = A()
print(var.class_attribute) # Output: Class Attribute
```

Main class'ın class attribute'ları ile, main class'dan türetilen instance'ların class attribute'ları ilk başta aynı objeye bağlıdır.

Main class'dan türetilen instance'lar ilk başta main class ile aynı class attribute'a sahiptir (yani bu class attribute'lar aynı objedir. ID'leri aynıdır). Ama sonradan bu instance'ların class attribute'larını yeniden tanımlarsanız (redefinition), bu class attribute ilgili instance için instance attribute'a dönüşür.
```py
class A():
    class_attribute = "Class Attribute"

var = A()

print(A.class_attribute) # Output: Class Attribute
print(var.class_attribute) # Output: Class Attribute
print(var.__dict__) # Output: {}

A.class_attribute = "New Class Attribute"
print(A.class_attribute) # Output: New Class Attribute
print(var.class_attribute) # Output: New Class Attribute
print(var.__dict__) # Output: {}

var.class_attribute = "Instance attribute"
print(A.class_attribute) # Output: Class Attribute
print(var.class_attribute) # Output: Instance Attribute
print(var.__dict__) #Output: {'class_attribute': 'Instance attribute'}
```
`__dict__` methodunun ne işe yaradığını daha sonra daha detaylı anlatacağım. Şimdilik `__dict__` methodunun ilgili class ya da instance'ın içerdiği methodların objelerinin ve attribute'ların value'larının depolandığı bir `dict` olarak düşünebilirsiniz. İlk başta `class_attribute`, `A` class'ında ve `var` instance'ında aynı class attribute objesi olarak bulunmaktaydı. Bu class attribute'un value'sunu `A` class'ı üzerinden değiştirdiğimizde `var` instance'ı da bundan etkileniyordu çünkü hala aynı class attribute objesini kullanıyorlar. Ama aynı şeyi `var` instance üzerinden yaptığımızda `var` instance'ının `class_attribute` class attribute'u bir instance attribute'a dönüşüyor ve `A` class'ının class attribute'una bağımlılığı ortadan kalkıyor (farklı bir obje oluyor).

**Not:** Class attribute'lar, instance'larda `__class__` adında bir method'da depolanırlar (`__class__` methodunun ne olduğu daha sonra anlatılacak).

Üzerinde yeniden tanımlama (redefinition) işlemi yapılan her class attribute farklı bir objeye dönüşür (ID'leri değişir). Sahip olduğu value'yu değiştirmek için yeniden tanımlama (redefinition) işleminin zorunlu olduğu değiştirilemez (immutable (`bool`, `int`, `float`, `complex`, `tuple`, `frozenset` vb.)) data type'larda bu durumun önüne geçemeyiz ama değiştirilebilir (mutable (`list`, `set`, `dict` vb.)) data type'larda geçebiliriz. Örnek:
```py
class A:
    class_attribute_1 = "String"
    class_attribute_2 = 1
    class_attribute_3 = 1.1234
    class_attribute_4 = 5+5j
    class_attribute_5 = tuple([1,2,3])
    class_attribute_6 = frozenset([1,2,3])
    class_attribute_7 = [1,2,3]
    class_attribute_8 = set([4,5,6])
    class_attribute_9 = {"yedi":7, "sekiz":8, "dokuz":9}

var1 = A()
var2 = A()

var2.class_attribute_1 = "Değiştirilmiş String"
var2.class_attribute_2 = 9
var2.class_attribute_3 = 9.9876
var2.class_attribute_4 = 9+9j
var2.class_attribute_5 = tuple([9,8,7])
var2.class_attribute_6 = frozenset([6,5,4])
var2.class_attribute_7.append("new_item")
var2.class_attribute_8.add("new_item")
var2.class_attribute_9.update({"new":"item"})

for i in dir(var1):
    if "class_attribute_" in i:
        eval(f"print('var1.{i}:', var1.{i})")
print("-"*69)
for i in dir(var2):
    if "class_attribute_" in i:
        eval(f"print('var2.{i}:', var2.{i})")
```
**Output:**
```
var1.class_attribute_1: String
var1.class_attribute_2: 1
var1.class_attribute_3: 1.1234
var1.class_attribute_4: (5+5j)
var1.class_attribute_5: (1, 2, 3)
var1.class_attribute_7: [1, 2, 3, 'new_item']
var1.class_attribute_8: {4, 5, 6, 'new_item'}
var1.class_attribute_9: {'yedi': 7, 'sekiz': 8, 'dokuz': 9, 'new': 'item'}
---------------------------------------------------------------------
var2.class_attribute_1: Değiştirilmiş String
var2.class_attribute_2: 9
var2.class_attribute_3: 9.9876
var2.class_attribute_4: (9+9j)
var2.class_attribute_5: (9, 8, 7)
var2.class_attribute_6: frozenset({4, 5, 6})
var2.class_attribute_7: [1, 2, 3, 'new_item']
var2.class_attribute_8: {4, 5, 6, 'new_item'}
var2.class_attribute_9: {'yedi': 7, 'sekiz': 8, 'dokuz': 9, 'new': 'item'}
```
**ID'ler:**
```

          Class Attri 1  Class Attri 2  Class Attri 3  Class Attri 4  Class Attri 5  Class Attri 6  Class Attri 7  Class Attri 8  Class Attri 9
Class A : 2193358095600  2193355729200  2193358170704  2193358170128  2193358391744  2193358336736  2193358095680  2193358339424  2193358020864
var1    : 2193358095600  2193355729200  2193358170704  2193358170128  2193358391744  2193358336736  2193358095680  2193358339424  2193358020864
var2    : 2193358212528  2193355729456  2193358170608  2193358170672  2193358391872  2193358338976  2193358095680  2193358339424  2193358020864
```
Mutable data type'ların methodlarını kullanmak yerine yeniden tanımlama (redefinition) işlemi uygulasaydık, mutable data type'lar da farklı bir objeye dönüşecekti (ID'leri değişecekti).

## Instance Attributes
Sadece instance methodların (daha sonra anlatılacak) veya `__init__` constructor'ının içinde tanımlanabilen, değer tutan/depolayan variable'lara **instance attribute** denir. Instance attribute'lara sadece instance'lar ulaşabilir, main class üzerinden ulaşılamaz. Örnek:
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


## Instance Methods
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
Gördüğünüz gibi aksi belirtilmediği için `func1` fonksiyonu ve `__init__` constructor'ı instance methoddur.

Main class'ın instance method'larında yapılan değişiklikler, bu main class'dan türetilen instance'ların instance method'larını da etkiler. Örnek:
```py
class A:
    def __init__(self):
        pass

    def func1(self):
        pass

var = A()

print(var.__init__) #Output: <bound method A.__init__ of <__main__.A object at 0x0000022E5FFA3FD0>>
A.__init__ = 1
print(var.__init__) #Output: 1


print(var.func1) #Output: <bound method A.func1 of <__main__.A object at 0x0000022E5FFA3FD0>>
A.func1 = 1
print(var.func1) #Output: 1
```

Instance methodların ve `__init__` constructor'ının ilk parametresi özel bir anlama sahip olan `self` olmak zorundadır çünkü bu bir syntax kuralıdır. Aksi halde `TypeError: func() takes 0 positional arguments but 1 was given` gibi bir hata alırsınız. `self` parametresi instance attribute'lara özel kabul edildiği için class attribute'larda kullanılamaz. Örnek:
```py
class A:
    self.attri = 1 # NameError: name 'self' is not defined
    def __init__(self):
        self.attri = 2
```
Bu parametreye farklı isimler de verebilirsiniz ama `self`, programcılar camiasında kalıplaşmış bir kullanım olmasından dolayı tercih edilir. Örnek:
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

Self parametresi, main class'dan türetilen geçerli (current) instance'ı atıfta bulunur. Kanıtı:
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
`__init__` constructor'ında herhangi bir instance attribute tanımlı olmamasına rağmen var instance'ı `var.a = 1`, `var.b = 2` ve `var.c = 3` statement'larından sonra 3 farklı instance attribute'a sahip oldu. Kanıtı:

<img src="https://i.ibb.co/2sSjmq9/image.png" alt="image" border="0">

Instantiation işlemi de tam da bu şekilde çalışır. Instantiation işleminde ilk `__init__` constructor'ı çağırılır ve yukarıdaki olayın aynısı gerçekleşir. Örnek:
```py
class A:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

var = A()
print(var.a, var.b, var.c) # Output: 1 2 3
```
Buradaki `self` parametresine Python tarafından `var = A()` kodundaki `A()` kodunun yarattığı instance argüman olarak girilir. Bu argümana temsili olarak `X` dersek, `self.a = 1`, `self.b = 2`, `self.c = 3` kodları `X.a = 1`, `X.b = 2`, `X.c = 3` anlamına gelmektedir. Yukarıdaki olayı `setattr()` (daha sonra anlatılacak) build-in fonksiyonunu kullanarak da yapabilirsiniz.

İlk olarak `__init__` constructor'ından bahsedelim. `__init__`, yapıcı (constructor) olarak bilinen, main class'dan instance türetilirken ilk çağırılan temel aşırı yükleme (overloading) methoddur. 

`__init__` constructor'ı tanımlanmamış `A` ismindeki bir class'ı ele alalım. `A` class'ı `object` base class'ından biras aldığı (daha sonra anlatılacak) için `A` class'ına debugger ile baktığınızda `__init__` constructor'ının special variables sekmesinde `<slot wrapper '__init__' of 'object' objects>` şeklinde depolandığını görürsünüz. Kanıt:
```py
class A:
    pass
```

<img src="https://i.ibb.co/Vv7zvzw/image.png" alt="image" border="0">

<img src="https://i.ibb.co/XC7s4y5/image.png" alt="image" border="0">

C'de uygulanan (implemented) bir special method'a erişmek (access) için bir extension type'ın dict'ine bir [slot wrapper](https://stackoverflow.com/questions/24708203/what-is-a-slot-wrapper-in-python#:~:text=A%20slot%20wrapper%20is%20installed,variant%20called%20method-wrapper) kurulur. Bu sayede C programlama dilinde yazılmış special methodları Python'da kullanabiliyoruz.

`A` class'ından türetilen instance'a debugger ile baktığınızda `__init__` constructor'ının function variables değil, special variables sekmesinde `<method-wrapper '__init__' of A object at 0x000002288B12D430>` şeklinde depolandığını görürsünüz. Kanıt:
```py
class A:
    pass

var = A()
```

<img src="https://i.ibb.co/YX198Dv/image.png" alt="image" border="0">

Slot wrapper her zaman unbound'dur ve method wrapper, slot wrapper ile ilişkilidir (bound). Bunları, slot wrapper ve method wrapper kavramlarını gördüğünüzde yadırgamamanız için anlattım.

`__init__` constructor'ı tanımlanmış `A` ismindeki bir class'ı ele alalım. Bu durumda `A` class'ının kendi `__init__` constructor'ı, object base class'ın `__init__` constructor'ını geçersiz kıldığı (override) (daha sonra anlatılacak) için `<function A.__init__ at 0x000001D36879A430>` şeklinde depolanır.
```py
class A:
    def __init__(self):
        pass
```

<img src="https://i.ibb.co/749ZxJX/image.png" alt="image" border="0">

`A` class'ından türetilen instance'lardaki `__init__` constructor'ları, `A` class'ının init constructor'ı ile ilişkilidir (bound) ve `<bound method A.__init__ of <__main__.A object at 0x000001D3687A13D0>>` şeklinde depolanır. Bu yüzden `A` class'ının `__init__` constructor'ına yaptığımız müdahaleler, `A` class'ından türetilen instance'ları da etkiler. Kanıtı:
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

Bir main class'dan her instance türetildiğinde, türetilen her instance kendisine özel instance attribute'lara sahip olur. Örnek:
```py
class A:
    attri = 1
    def __init__(self):
        self.attri2 = 2

var1 = A()
```
`var1` instance'ına debugger ile aşağıdaki gibi baktığımızda instance ve class attribute'ları ayırt edemeyiz.

<img src="https://i.ibb.co/C7YsqcS/image.png" alt="image" border="0">

Ama ilgili instance'ın special variables sekmesindeki `__dict__` methoduna baktığımızda instance attribute'ları ayırt edebiliriz.

<img src="https://i.ibb.co/Q6qwGZM/image.png" alt="image" border="0">

Gördüğünüz gibi `attri2` attribute'unun bir instance attribute olduğunu bu şekilde ayırt edebildik. Her instance, kedisine özel instance attribute'ları bu şekilde depolar.

Aynı şey instance methodlar'da da geçerlidir. Instance methodların `__init__`'den farkı; instance methodlar `__init__` gibi instantiation işleminde otomatik olarak çağırılmadığı için içindeki instance attribute'ların bellekte depolanması için instance methodları elle 1 kere çağırmamız gerekmektedir. Örnek:
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
**Not:** `func()` fonksiyonunun içindeki `self.attri2` instance attribute'una `var.func().attri2` şeklinde ulaşmaya çalışırsanız `AttributeError: 'NoneType' object has no attribute 'attri2'` hatası alırsınız. Örnek:
```py
class A():

    def func(self):
        self.attri2 = "func attribute"
        
var = A()
print(var.func().attri2) # AttributeError: 'NoneType' object has no attribute 'attri2'
```
Python dahil çoğu programlama dili [aritmetik işlem mantığıyla](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_kavramlar.md#pythonun-çalışma-mantığı) kodları çalıştırır. `var.func().attri2` kodu şu sırayla çalışır:
1. Python önce `var` instance'ı üzerinden `func` methodunu çağırır.
2. `func` method'unda herhangi bir `return` statement olmadığı için `func` method'u `NoneType` (`<class 'NoneType'>`) döndürür.
3. Bu işlemlerden sonra `var.func().attri2` kodu Python gözünde `NoneType.attri2` koduna dönüşür.
4. `NoneType` objesinin `attri2` adında bir methodu olmadığı için `AttributeError: 'NoneType' object has no attribute 'a_yazdir_attribute'` hatası yükseltilir.

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
3. Bu işlemlerden sonra `var.func().attri2` kodu Python gözünde `"func attribute".attri2` koduna dönüşür.
4. `"func attribute"` string objesinin `attri2` adında bir methodu olmadığı için `AttributeError: 'str' object has no attribute 'attri2'` hatası yükseltilir.

**Not:** Class attribute'lar, instance'ların special variables sekmesindeki `__class__` methodunda tanımlıdır. Kanıt:

<img src="https://i.ibb.co/Yb0WsY8/image.png" alt="image" border="0">

Bu yüzden main class üzerinden class attribute'ların value'su değiştirdiğinde, bu değişiklik instance'lara da yansıyor. `__class__` methodunda tanımlı olan class objesi, bu instance'ın türetildiği main class objesidir.

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
Buradaki `attri_1` ve `attri_2` instance attribute'lardır (`__dict__` methodunda saklanır). Bu yüzden `var1`'de yapılan değişiklikler `var2`'yi etkilemez. Burada dikkat edilmesi gereken şey; her instance'ın kendi instance attribute'larına sahip olması, her instance'ın kendi `__init__` constructor objesine de sahip olduğu anlamına gelmez. Instance'lardaki `__init__`  constructor objeleri main class'ın `__init__` constructor objesi ile ilişkilidir (bound). Kanıtı:
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

Bir instance'da `__init__` constructor'ının içinde instance attribute olarak ve dışında class attribute olarak aynı isimde iki attribute varsa, bu instance, `__init__` constructor'ının içindeki instance attribute'u tanır. Örnek:
```py
class A:
    attri_1 = 2
    def __init__(self):
        print("init çalıştı...")
        self.attri_1 = 1

var = A() # Output: init çalıştı...
print(var.attri_1) # Output: 1
```
Bu senaryoda eğer özellikle class attribute olan `attri_1`'e erişmek istiyorsanız, bu class attribute'u direkt main class üzerinden çağırın. Örnek:
```py
class A:
    a = 2
    def __init__(self):
        print("init çalıştı...")
        self.a = 1

var = A() # Output: init çalıştı...
print(A.a) # Output: 2
```

`self` parametresi ile sıfırdan bir instance attribute tanımlayabileceğiniz gibi, class attribute'lara da atıfta bulunabilirsiniz. Ama bu size herhangi bir kolaylık sağlamaz. Örnek:
```py
class A():
    attri = 1
    def __init__(self):
        self.attri

var = A()
print("A attribute:  ", A.attri, "|", id(A.attri))
print("var attribute:", var.attri, "|", id(var.attri))
```
**Output:**
```
A attribute:   1 | 1893013285168
var attribute: 1 | 1893013285168
```
`var` variable'ına atanan instance'a temsili olarak `X` dersek: Buradaki `self.attri`, `X.attri` anlamına gelmektedir. `X.attri`'de direkt `attri` class attribute objesine atıfta bulunduğu için hata yükseltmez. Bu yüzden `self.attri` yazmakla yazmamak arasında işlevsel olarak herhangi fark yoktur. Başka bir örnek:
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
`var1` variable'ına atanan instance'a temsili olarak `X`, `var2` variable'ına atanan instance'a temsili olarak `Y` dersek: Benzer şekilde buradaki `self.liste`, `var1` instance'ı için `X.liste`, `var2` instance'ı için `Y.liste` anlamına gelmektedir. `X.liste` ve `Y.liste`'de direkt `liste` class attribute objesine atıfta bulunduğu için hata yükseltmez ve üzerinde `append` methodu uygulanabilir. Bu yüzden `A` main class'ından her instance türetildiğinde `__init__` ve beraberinde `self.liste.append("New Item")` çalıştığı için her seferinde `liste` class attribute'una `"New Item"` stringi ekleniyor. Bunlar instance methodlar için de geçerlidir. Örnek:
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
Gördüğünüz gibi buradaki `sayi_1` ve `sayi_2` local variable'larını `self` ile kullanmadığımız için Python bunları instance attribute olarak değerlendirmiyor. Bu yüzden bu local variable'lara doğrudan ulaşamayız ama `__init__` constructor'ı içinde kullanabiliriz. Aynı şey instance methodlar'da da geçerlidir. Örnek:
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
Gördüğünüz gibi instance method veya `__init__` constructor'a argüman girerken `self`'i görmezden gelerek argüman giriyoruz çünkü instance üzerinden instance method çağırırken Python `self` parametresine ilgili argümanı otomatik olarak girdiği için elle argüman girmemiz gerekmez. Ama bir main class üzerinden instance method çağırırken `self` parametresine elle argüman girmemiz gerekiyor (nedenini daha önce anlattım). Örnek:
```py
class A:
    def __init__(self):
        self.a = "self.a attribute"
    
    def func(self):
        print("Instance method func():", self.a)

A().func() # Output: Instance method func(): self.a attribute
A.func() # TypeError: func() missing 1 required positional argument: 'self'
A.func(A()) # Output: Instance method func(): self.a attribute
```

## Class Methods
Python'da `@` işareti kullanılanılarak oluşturulan yapılara **decorator** denir. Python'da class method tanımlamak için `@classmethod` decorator'u kullanılır. `@classmethod` decorator'u, kendinden sonraki fonksiyonun bir class method olduğunu Python'a bildirir. `classmethod` aslında bir class'dır. Kanıtı:

<img src="https://i.ibb.co/StXg8Q9/image.png" alt="image" border="0">

Bu yüzden `@classmethod` decorator'u ile decore edilen methodlar main class'ın `__dict__` methodunda `<classmethod object at 0x0000021910BB3430>` şeklinde depolanır. Örnek:
```py
class A:
    @classmethod
    def class_method_exp(cls):
        pass

print(A.__dict__["class_method_exp"]) # Output: <classmethod object at 0x0000021910BB3430>
```

Main class'ın class method'larında yapılan değişiklikler, bu main class'dan türetilen instance'ların class method'larını da etkiler. Örnek:
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

cls parametresi, main class'a atıfta bulunur. Kanıtı:
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

<img src="https://i.ibb.co/2Kg6ks7/image.png" alt="image" border="0">

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
Python otomatik olarak `func` class method'undaki `cls` parametresine argüman olarak `A` class'ını girer. Bu yüzden `cls.attri_1 = 1`, `cls.attri_2 = 2`, `cls.attri_3 = 3` kodları `A.attri_1 = 1`, `A.attri_2 = 2`, `A.attri_3 = 3` anlamına gelmektedir. Tabii bu class attribute'ların yaratılması (create) için `func` class method'unun bir kere çağırılması gerekmektedir. Bu yüzden class attribute'ları aşağıdaki gibi tanımlamanız daha doğru olacaktır:
```py
class A:
    attri_1 = 1
    attri_2 = 2
    attri_3 = 3

print(A.attri_1, A.attri_2, A.attri_3) # Output: 1 2 3
```
Yukarıdaki olayı `setattr()` (daha sonra anlatılacak) build-in fonksiyonunu kullanarak da yapabilirsiniz.

**Not:** Bir method class method olarak tanıtılmamışsa, o methodun `cls` parametresi instance methodlar'daki `self` parametresi gibi davranır.

Instance methodlara main class'dan erişemeyiz ama class methodlara hem main class'dan hem de instance'dan erişebiliriz. Örnek:
```py
class A:
    @classmethod
    def func(cls):
        return "Class Method Çalıştı."

var = A()
print(A.func()) # Output: Class Method Çalıştı.
print(var.func()) # Output: Class Method Çalıştı.
```

Aynı instance methodlarda olduğu gibi, class methodlarda da class attribute'lara atıfta bulunabilirsiniz. Örnek:
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

print(A.attri, id(A.attri))         # Output: class attribute 3200897484016
print(A().func1(), id(A().func1())) # Output: class attribute 3200897484016
print(A.func2(), id(A.func2()))     # Output: class attribute 3200897484016
```

**Not:** Class methodlara illa main class'dan (`A.func2()` gibi) ulaşacaksınız diye bir kural yok. Class methodlara instance'lardan da ulaşabilirsiniz (`var.func2()` gibi). Ama hata riskini en aza indirmek için class methodlara main class'dan ulaşmak daha akıllıca bir seçimdir.

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
Bu kodda `len(self.liste)`'nin `0` olduğu bir durum yoktur çünkü `liste_uzunluğu` methodunu sadece bir instance üzerinden çağırabileceğiniz için instantiation işlemi yapmak zorundasınız. Instantiation işlemi yapınca da `__init__` çağırılır ve dolayısıyla `self.listeye_ekle()` kodu yüzünden `listeye_ekle` fonksiyonu çağırılır ve `len(self.liste)`'nin değeri `1` olur. Bu yüzde bu gibi durumlarda class method'lar kullanılabilir. Örnek:
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
- `liste_uzunluğu()` fonksiyonu `A` class'ının dışında tanımlandığı için başka bir dosyada (Örneğin `Modul_B` isimli bir dosyada) tanımlanmış `A` class'ını `form Modul_B import A` şeklinde import ettiğimizde, `liste_uzunluğu()` fonksiyonu `A` class'ının dışında tanımlandığı için içeri import edilmez ve dolayısıyla bu fonksiyonu ayrıyetten `form Modul_B import liste_uzunluğu` şeklinde import etmeden kullanamayız.

## Alternative Constructor
Direkt bir örnekle anlatayım. Örnek:
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

A.yas() # Output: Lütfen bir isim girin.
A.yas("Ayşe") # Output: Girdiğiniz isim listede yok.
A.yas("Ali") # Output: 23
A.yas("Veli") # Output: 25
A.yas("Hasan") # Output: 32
```
Yukarıdaki `cls(name)` kodu `A(name)` anlamına gelmektedir ve `A(name)`'de bir instantiation işlemidir. Buradaki `cls(name)` gibi kodlara **alternative constructor** denir.

## Static Methods
Python'da static method tanımlamak için `@staticmethod` decorator'u kullanılır. `@staticmethod` decorator'u, kendinden sonraki fonksiyonun bir static method olduğunu Python'a bildirir. `staticmethod` aslında bir class'dır. Kanıtı:

<img src="https://i.ibb.co/NNhn86H/image.png" alt="image" border="0">

Bu yüzden `@staticmethod` decorator'u ile decore edilen methodlar main class'ın `__dict__` methodunda `<staticmethod object at 0x0000021910BB33D0>` şeklinde depolanır. Örnek:
```py
class A:
    @staticmethod
    def static_method_exp():
        pass

print(A.__dict__["static_method_exp"]) # Output: <staticmethod object at 0x0000021910BB33D0>
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
Gördüğünüz gibi static methodlara hem main class hem de instance üzerinden erişebiliryoruz. Static methodların herhangi bir class veya instance methoda erişmesi gerekmediği için ilk parametresi `self` ya da `cls` gibi özel bir parametre olmak zorunda değildir (yani static methodların içinde herhangi bir class ve instance attribute tanımlayamazsınız). Static methodların bütün parametreleri normal bir parametre muamelesi görür.

Main class'ın static method'larında yapılan değişiklikler, bu main class'dan türetilen instance'ların static method'larını da etkiler. Örnek:
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