# Object Class
Class'lar, Python'ın' 3.x öncesi sürümlerinde **yeni tip class'lar** ve **eski tip class'lar** olmak üzere ikiye ayrılıyordu. Eski tip class'lara örnek:
```py
class Class1():
    pass

class Class2(Class1):
    pass
```
Yeni tip class'lara örnek:
```py
class Class1(object):
    pass

class Class2(Class1):
    pass
```
Python'ın 3.x öncesi sürümlerinde, yeni tip class'larla birlikte gelen bazı özellikler vardı (Örneğin `@property` decorator'u). Bir class'ın yeni tip özellikleri kullanabilmesi için `object` adındaki class'ından miras alması gerekiyordu. Eski tip class'lar `object` class'ından miras almadıkları için bu yeni tip özellikleri kullanamıyorlardı. Python 3'den sonra, bütün class'lar yeni tip class olarak güncellenmiştir. Bu yüzden Python 3'den sonra bir class, `object` class'ından miras alsa da almasa da yeni tip özellikleri kullanabilir. Yani Python 3'den sonra aşağıdaki class tanımlamaları arasında hiçbir fark yoktur:
```py
class Sınıf:
    pass

class Sınıf():
    pass

class Sınıf(object):
    pass
```

# MRO (Method Resolution Order)
Method resolution order (kısaca MRO), "method çözümleme sırası" anlamına gelmektedir. MRO, **[directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)**'dan (kısaca DAG) türetilen, **[C3 linearization algorithm](https://en.wikipedia.org/wiki/C3_linearization)** tarafından oluşturulan **[total order](https://en.wikipedia.org/wiki/Total_order)**'dır.

Bir class'ın inheritance hierarchy'sini temsil eden, "yönlendirilmiş döngüsel olmayan grafik" anlamına gelen graph'a (graph'ın ne olduğunu bilmiyorsanız araştırın) **Directed Acyclic Graph (DAG)** denir. Kısacası class'ların inheritance konusunda birbirleriyle olan bağlantılarının gösterildiği grafiktir. Örnek:
```py
O = object
class F(O): pass
class E(O): pass
class D(O): pass
class C(D,F): pass
class B(E,D): pass
class A(B,C): pass
```

<img src="https://i.ibb.co/X5XstLP/A.png" alt="A" border="0">

Bu graph bize sadece hangi class'ın hangi class'dan miras aldığını söyler, single ya da multiple inheritance'ın MRO'su hakkında bir bilgi vermez.

Multiple inheritance'ın MRO'su 2 kurala göre belirlenir:
1. Subclass her zaman ilk sıradadır.
2. Subclass'ın miras aldığı base class'ların subclass'a tanımlanma sırasına saygı gösterilir. (örneğin `class A(B, C)` kodunda `B`, `C`'den önce gelir.)

MRO'ya ulaşmak için ilgili class'ın `__mro__` ya da `mro()` methodlarından faydalanabilirsiniz. Örnek:
```py
O = object
class F(O): pass
class E(O): pass
class D(O): pass
class C(D,F): pass
class B(E,D): pass
class A(B,C): pass

print(A.__mro__) # A -> B -> E -> C -> D -> F -> object
print(B.__mro__) # B -> E -> D -> object
print(C.__mro__) # C -> D -> F -> object
print(D.__mro__) # D -> object
print(E.__mro__) # E -> object
print(F.__mro__) # F -> object
```
**Output:**
```
(<class '__main__.A'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.F'>, <class 'object'>)
(<class '__main__.B'>, <class '__main__.E'>, <class '__main__.D'>, <class 'object'>)
(<class '__main__.C'>, <class '__main__.D'>, <class '__main__.F'>, <class 'object'>)
(<class '__main__.D'>, <class 'object'>)
(<class '__main__.E'>, <class 'object'>)
(<class '__main__.F'>, <class 'object'>)
```

**Not:** MRO'yu anlamak için inheritance bilgisi, inheritance'ı anlamak için de MRO bilgisi gerekmektedir. Bu yüzden inheritance ve multiple inheritance bölümlerini iyice öğrendikten sonra tekrardan MRO'yu araştırmanızda fayda var. Inheritance ve multiple inheritance konu başlıklarında bol bol MRO kavramıyla karşılaşacaksınız. Bu konu başlıklarında MRO kavramıyla ilgili bol bol örnek verildiği için MRO'yu ayriyetten araştırmadan önce bu başlıkları okumayı bitirin. Buna rağmen MRO'yu hala anlamadıysanız, yukarıdaki linklerden de yararlanarak kendi başınıza MRO'nun ne olduğunu öğreniniz.

MRO hakkında daha fazla bilgi için:
- **[Python history blogspot](https://python-history.blogspot.com/2010/06/method-resolution-order.html)**
- **[Stackoverflow](https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance)**

# Inheritance (Miras Alma)
Bir class'ın, başka bir class'ın method ve class attribute'larına miras alma yoluyla erişip kullanabilmesine **Inheritance (Miras Alma)** denir. Method ve class attribute'ları miras alınan class'a parent class, super class, base class olarak isimlendirilir. Base class'ın method ve class attribute'larını miras alan class'da child class, derived class, subclass olarak isimlendirilir. Ben tutorial boyunca bunlardan **base class** ve **subclass** olarak bahsedeceğim. Inheritance (Miras Alma), aynı kodları her class'a tekrar tekrar yazma zahmetinden bizi kurtarır. Örnek:
```py
class Class1():
    cs1 = "Class Attribute 1"
    def __init__(self):
        pass

    def func1(self):
        pass

class Class2(Class1):
    pass
```
`Class1` class'ını `Class2` class'ının parantezine yazarak, `Class2` class'ın `Class1` class'ındaki bütün method ve class attribute'larını miras almasını sağladık. Kanıtı:

<img src="https://i.ibb.co/BVRW73Q/image.png" alt="image" border="0">

Gördüğünüz gibi `Class2` subclass'ı, `Class1` base class'ın method ve class attribute'larını miras almış.

Inheritance (Miras Alma) işleminde subclass, base class'ın method ve class attribute'larının kopyasını kendi class objesinde oluşturmaz, base class'daki method ve class attribute'lara atıfta bulunur. Örnek:
```py
class Class1():
    cs1 = "Class Attribute 1"

    def __init__(self):
        print("init çalıştı...")

    def func1(self):
        print("func1 Çalıştı...")

class Class2(Class1):
    pass
```
`Class2` subclass'ının miras aldığı `func1` instance method objesi, `Class1` base class'ındaki `func1` instance method objesidir. Kanıtı:

<img src="https://i.ibb.co/VwQgtXv/image.png" alt="image" border="0">

Gördüğünüz gibi `Class2` subclass'ındaki instance method objesinde `<function Class1.func1 ... >` yazmaktadır. Buradaki `Class1.func1` ifadesi, `func1` fonksiyonunun `Class1`'in instance method objesi olduğunu söylemektedir. Yani `Class2` subclass'ındaki `func1` objesi, `Class1` base class'ındaki `func1` objesine atıfta bulunur (refers). Atıfta bulunma durumu söz konusu olduğu için base class'da bir değişiklik yapıldığında bundan subclass'da etkilenir. Örneğin yukarıdaki koda `Class1.cs1 = "Yeni Class Attribute 1"` kodunu ekleyip çalıştırırsak, hem `Class1` base class'ının hem de `Class2` subclass'ının `cs1` class attribute'unun değeri değişir. Kanıtı:

<img src="https://i.ibb.co/CwZGwxM/image.png" alt="image" border="0">

**Not:** En başta `Class1` ve `Class2` birbirinden üstün olmamasına rağmen, inheritance (miras alma) işleminden sonra `Class2` class'ının subclass rütbesine düştüğünü, `Class1` class'ının da base class rütbesine yükseldiğini söyleyebiliriz. Tabii bu, lafta böyle. Python bunları base class ya da subclass olarak değerlendirmez. `Class2` class'ı, `Class1` class'ından miras almış subclass olarak değerlendirir.

## Types of Inheritance (Miras Alma Türleri)
Inheritance (Miras Alma)'nın çeşitleri vardır.

### Her şeyi miras almak
Bir subclass, bir base class'ın bütün method ve class attribute'larını olduğu gibi miras alabilir. Örnek:
```py
class Class1():
    def __init__(self, p1, p2):
        print("init çalıştı...")
        self.a = p1
        self.b = p2
        self.c = 0

    def func1(self):
        print("func1 Çalıştı...")

    def func2(self):
        print("func2 Çalıştı...")

    def func3(self):
        print("func3 Çalıştı...")

class Class2(Class1):
    pass

var = Class2("parametre 1", "parametre 2") # Output: init çalıştı...
print(var.a) # Output: parametre 1
print(var.b) # Output: parametre 2
print(var.c) # Output: 0
var.func1() # Output: func1 Çalıştı...
var.func2() # Output: func2 Çalıştı...
var.func3() # Output: func3 Çalıştı...
```
Gördüğünüz gibi `Class2` subclass'ı, `Class1` base class'ının sahip olduğu bütün method ve class attribute'ları değiştirmeden direkt miras aldı.

**Not:** Bir subclass'ın üzerinde, bir base class'ın her şeyini miras almak dışında ekstra method veya class attribute tanımlamak gibi bir işlem yapmayacaksanız, `Class2` subclass'ını yukarıdaki koddaki gibi tanımlamak yerine `Class2 = Class1()` şeklinde doğrudan instance olarak oluşturmak daha pratiktir. Örnek:
```py
class Class1():
    pass

Class2 = Class1()
```

### Miras alınan method ve attribute'ları override etmek
Bir subclass'da tanımlanmış method veya class attribute'lar (kısaca item diyelim), subclass'ın miras aldığı base class'daki item'larla çakışıyorsa (yani ikisinde de aynı isimde item'lar varsa), inheritance (miras alma) işleminden sonra subclass'ın item'ları base class'daki item'ların üzerine yazıldığı için base class'ın item'ları geçersiz kılınır (**override**) ve subclass'ın item'ları kullanılır. Örnek: 
```py
class Class1():
    def __init__(self):
        print("Class1 init çalıştı...")

    def func1(self):
        print("func1 Çalıştı...")

class Class2(Class1):
    def func1(self):
        print("Class2'deki func1 Çalıştı...")

var1 = Class1() # Output: Class1 init çalıştı...
var2 = Class2() # Output: Class1 init çalıştı...
var1.func1() # Output: func1 Çalıştı...
var2.func1() # Output: Class2'deki func1 Çalıştı...
```
Gördüğünüz gibi `Class2` subclass'ında `func1` instance methodu zaten tanımlı olduğu için inheritance (miras alma) işleminden sonra `Class1` base class'ının `func1` instance methodu override edildi ve `var.func1()` kodu `Class1` base class'ının `func1` instnace methodundaki `print("func1 Çalıştı...")` kodunu değil, `Class2` base class'ının `func1` instnace methodundaki `print("Class2'deki func1 Çalıştı...")` kodunu çalıştırdı. Aynı şey class attribute'lar için de geçerlidir. Örnek:
```py
class Class1():
    cs1 = "Class Attribute 1"
    def __init__(self):
        print("init çalıştı...")
        pass

class Class2(Class1):
    cs1 = "Class2'nin Class Attribute 1"

var = Class2() # Output: init çalıştı...
print(Class1.cs1) # Output: Class Attribute 1
print(var.cs1) # Output: Class2'nin Class Attribute 1
```
Gördüğünüz gibi `Class2` subclass'ında `cs1` class attribute'u zaten tanımlı olduğu için inheritance (miras alma) işleminden sonra `Class1` base class'ının `cs1` class attribute'u override edildi ve `print(var.cs1)` kodu `Class1` base class'ının `cs1` class attribute'undaki `"Class Attribute 1"` value'sunu değil, `Class2` base class'ının `cs1` class attribute'undaki `"Class2'nin Class Attribute 1"` value'sunu yazdırdı.

**Not:** Yukarıdaki durum class ve static methodlar için de geçerlidir. Yani bir subclass'da, base class'dan miras alınan class ve static methodlar override edilebilir. Örnek:
```py
class Class1():
    class_attribute = "Class1'in Class Attribute'u"
    def __init__(self):
        print("init çalıştı...")

    @classmethod
    def class_method(cls):
        print(f"Class1'in class_method'u çalıştı: {cls.class_attribute}")

    @staticmethod
    def static_method():
        static_attribute = "Class1'in Static Attribute'u"
        print(f"Class1'in static_method'u çalıştı: {static_attribute}")

class Class2(Class1):

    @classmethod
    def class_method(cls):
        cls.class_attribute = "Class2'in Class Attribute'u"
        print(f"Class2'in class_method'u çalıştı: {cls.class_attribute}")

    @staticmethod
    def static_method():
        static_attribute = "Class2'in Static Attribute'u"
        print(f"Class2'in static_method'u çalıştı: {static_attribute}")
        
var1 = Class1() # Output: init çalıştı...
var2 = Class2() # Output: init çalıştı...
var1.class_method() # Output: Class1'in class_method'u çalıştı: Class1'in Class Attribute'u
var2.class_method() # Output: Class2'in class_method'u çalıştı: Class2'in Class Attribute'u
var1.static_method() # Output: Class1'in static_method'u çalıştı: Class1'in Static Attribute'u
var2.static_method() # Output: Class2'in static_method'u çalıştı: Class2'in Static Attribute'u
```

### Miras alınan methodları içeriğini bozmadan değiştirmek
Bir subclass'da, base class'dan miras alınan methodların içeriğine ufak eklemeler yapmak veya bir attribute'un değerini yeniden tanımlamak (redefinition) istediğinizde, bu methodları override etmiş sayıldığınız için veri kaybı yaşarsınız. Örnek:
```py
class Class1():
    def __init__(self):
        print("init çalıştı...")
        self.a = 1
        self.b = 2

class Class2(Class1):
    def __init__(self):
        self.a = 4
        
var1 = Class1() # Output: init çalıştı...
var2 = Class2()
print(var1.a) # Output: 1
print(var1.b) # Output: 2
print(var2.a) # Output: 4
print(var2.b) # AttributeError: 'Class2' object has no attribute 'b'
```
Yukarıdaki kodda `Class1` base class'ından miras aldığımız `self.a` instance attribute'unun değerini `4` olarak yeniden tanımlamak (redefinition) istedik ama bunu yaparak `Class1` base class'ından miras alınan `__init__`'i override etmiş olduk. Bu yüzden `Class2` subclass'ında `b` instance attribute'una ulaşamayıp veri kaybı yaşadık. Bu sorunun önüne geçmek için `super()` fonksiyonu kullanılabilir.

#### `super(<subclass>, <subclass object>)` Fonksiyonu
**Başlamadan önce oku:** `super()` fonksiyonunu baya araştırdım ama çalışma prensibini bütün ayrıntılarıyla anlatan bir kaynak bulamadığım için birçok yazılı, video kaynaktan ve bilir kişilerden yararlanarak bu bilgileri topladım. Bu bilgileri kullanarak ancak `super()` fonksiyonunun farklı senaryolardaki davranışlarını size göstermekle yetinebildim. Öğreneceğiniz şeylerin doğruluğundan %90 emin olsam da, bu kısım bittikten sonra bu konuyu kendiniz de araştırırsanız daha sağlıklı olur.

`super()` build-in fonksiyonu (bundan sonra direkt `super()` fonksiyonu olarak bahsedilecek) **MRO**'ya (Method Resolution Order) göre çalışan bir mekanizmaya dayanır. `super()` build-in fonksiyonu, istediğimiz base class'ın proxy objesini (base class'ın geçici (temporary) objesini) oluşturup döndürür. Bu proxy objesini kullanarak override sorununun önüne geçebiliriz. Örnek:
```py
class Class1():
    def __init__(self, p1, p2, p3):
        print("init çalıştı...")
        self.a = p1 + p2 + p3

class Class2(Class1):
    def __init__(self, p1, p2, p3, p4):
        super().__init__(p1, p2, p3)
        self.d = p4 + self.a

var1 = Class1(1,2,3) # Output: init çalıştı...
var2 = Class2(1,2,3,4) # Output: init çalıştı...
print(var1.a) # Output: 6
print(var2.a) # Output: 6
print(var2.d) # Output: 10
```
Buradaki `super()` fonksiyonu, `Class1` base class'ının bir proxy objesi oluşturup döndürdü. Bu proxy objesini kullanıp `Class1` base class'ının `__init__` methodunu çağırarak (call) miras alma işlemini gerçekleştirdik. Bu sayede `Class2` subclass'ından türetilmiş `var2` instance'ının üzerinden, `Class2` subclass'ının `__init__` methoduna elle tanımlamadığımız instance attribute'lara bile erişebiliyoruz. Bunu, `super()` fonksiyonunun döndürdüğü proxy objesine borçluyuz. Başka bir örnek:
```py
class Class1():
    def __init__(self, p1, p2, p3):
        print("init çalıştı...")
        self.a = p1 + p2 + p3

class Class2(Class1):
    def __init__(self, p4, *args):
        super().__init__(*args)
        self.d = p4 + self.a

var1 = Class1(1,2,3) # Output: init çalıştı...
var2 = Class2(4,1,2,3) # Output: init çalıştı...
print(var1.a) # Output: 6
print(var2.a) # Output: 6
print(var2.d) # Output: 10
```
Eğer `Class1` ve `Class2` class'larının `__init__` methodlarının parametrelerini tek tek elle tanımlamak istemiyorsanız, bu parametreler yerine yukarıdaki gibi `*args` (`p1 = "Falan Filan"` gibi default value'ya sahip parametreler varsa `*args` yerine `**kwargs`) yıldızlı parametresini kullanmanız yeterlidir. Bu bütün method türleri için de geçerlidir. Başka bir örnek:
```py
class Class1():
    def __init__(self, p1, p2, p3):
        print("init çalıştı...")
        self.a = p1 + p2 + p3

class Class2(Class1):
    def __init__(self, a1):
        super().__init__(a1, a1, a1)
        self.d = a1 + self.a

var1 = Class1(1,2,3) # Output: init çalıştı...
var2 = Class2(4) # Output: init çalıştı...
print(var1.a) # Output: 6
print(var2.a) # Output: 12
print(var2.d) # Output: 16
```
`super().__init__(a1, a1, a1)` kodundaki `__init__(a1, a1, a1)` kısmını `Class1` base class'ındaki gibi `__init__(p1, p2, p3)` şeklinde yazamayız. Bunun sebebi `super().__init__(a1, a1, a1)` kodundaki `a1`'lerin parametre değil argüman olmasından kaynaklanıyor. Burada parametre tanımlamıyorsunuz, `super()` fonksiyonunun döndürdüğü `Class1` base class'ının proxy objesi üzerinden çağırdığınız (call) `__init__` methoduna argüman giriyorsunuz. `super().__init__(a1, a1, a1)` yerine `super().__init__(p1, p2, p3)` yazarsanız, `p1`, `p2` ve `p3` argümanları `Class2` subclass'ının `__init__` methodunun scope'unda tanımlı olmadığı için `NameError: name 'p1' is not defined` hatası yükseltilir. Bu yüzden bulunduğunuz scope'da tanımlı objeleri argüman olarak tercih edin.

`super()` fonksiyonunu instance, class ve static methodlarda kullanabiliriz. Örnek:
```py
class Class1():
    class_attribute = "Class1'in Class Attribute'u"

    def instance_method(self):
        self.instance_attribute = "Class1'in Instance Attribute'u"
        print("Class1'in instance_method'u çalıştı:", end=" ")

    @classmethod
    def class_method(cls):
        cls.class_attribute
        print("Class1'in class_method'u çalıştı:", end=" ")

    @staticmethod
    def static_method():
        static_attribute = "Class1'in Static Attribute'u"
        print("Class1'in static_method'u çalıştı:", end=" ")
        return static_attribute

class Class2(Class1):
    def instance_method(self):
        super().instance_method()
        print(self.instance_attribute)

    @classmethod
    def class_method(cls):
        super().class_method()
        print(cls.class_attribute)

    @staticmethod
    def static_method():
        print(super(Class2, Class2()).static_method())
        
var2 = Class2()
var2.instance_method() # Output: Class1'in instance_method'u çalıştı: Class1'in Instance Attribute'u
var2.class_method() # Output: Class1'in class_method'u çalıştı: Class1'in Class Attribute'u
var2.static_method() # Output: Class1'in static_method'u çalıştı: Class1'in Static Attribute'u
```

`Class2` subclass'ının `static_method` static methodunun bloğundaki `super(Class2, Class2()).static_method()` kodunda da gördüğünüz gibi `super()` fonksiyonunun `<subclass>` (birinci parametre) ve `<subclass object>` (ikinci parametre) olmak üzere 2 parametresi vardır:

**`<subclass>`**: `<subclass>` parametresine argüman olarak sadece class (`Class1`, `Class2` vb.) verilebilir. `super()` fonksiyonu, `<subclass>` parametresinde belirtilen subclass'ın MRO'suna göre ilk sırada olan base class'ı kullanarak oluşturuduğu proxy objesini döndürür. Örneğin `C` subclass'ını MRO'su `C -> B -> A -> object` ise, `super()` fonksiyonu `B` base class'ını kullanarak oluşturduğu proxy objesini döndürür.

**`<subclass object>`**: `<subclass object>` parametresine verilen argüman subclass ya da instance olabilir. `<subclass object>` parametresine argüman olarak subclass girilirse, bu subclass'ın MRO'su `<subclass>` parametresine argüman olarak girilen class'ı içermelidir. Aksi halde, `TypeError: super(type, obj): obj must be an instance or subtype of type` hatası yükseltilir. Örnek:
```py
class A:
    def print_msg(self):
        print("Class A")

class B:
    def print_msg(self):
        print("Class B")

class C(B, A):
    def print_msg(self):
        print("Class C")

class E(A, B):
    def print_msg(self):
        super(A, E).print_msg(self) # Output: Class B
        super(B, C).print_msg(self) # Output: Class A

var = E()
print(E.__mro__) # Output: (<class '__main__.E'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(C.__mro__) # Output: (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
var.print_msg()
```
Gördüğünüz gibi, `E` subclass'ının MRO'su (`E.__mro__`) `E -> A -> B -> object` şeklindedir. `E` subclass'ının MRO'su `A` base class'ını içerdiği için `super(A, E).print_msg(self)` kodu çalıştı. `C` subclass'ının MRO'su (`C.__mro__`) `C -> B -> A -> object` şeklindedir. `C` subclass'ının MRO'su `B` base class'ını içerdiği için `super(B, C).print_msg(self)` kodu da çalıştı.

**Not:** `super()` fonksiyonunun `<subclass object>` parametresine argüman olarak subclass girecekseniz, bu fonsiyonun döndürdüğü proxy objesi üzerinden çağırdığınız instance methodların ilk parametresine argüman olarak `self` (ya da `self` yerine hangi ismi (identifier) kullanıyorsanız onu) girmeniz gerekmektedir. Aksi halde `TypeError: print_msg() missing 1 required positional argument: 'self'` hatası alırsınız.

`<subclass object>` parametresine argüman olarak girilen instance'ın türetildiği subclass'ın MRO'su, `<subclass>` parametresine argüman olarak girilen class'ı içermelidir. Aksi halde, `TypeError: super(type, obj): obj must be an instance or subtype of type` hatası yükseltilir. Örnek:
```py
class A:
    def print_msg(self):
        print("Class A")

class B:
    def print_msg(self):
        print("Class B")

class C(B, A):
    def print_msg(self):
        print("Class C")

class E(A, B):
    def print_msg(self):
        super(A, E()).print_msg() # Output: Class B
        super(B, C()).print_msg() # Output: Class A

var = E()
print(E.__mro__) # Output: (<class '__main__.E'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(C.__mro__) # Output: (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
var.print_msg()
```
Gördüğünüz gibi, `E()` instance'ın türetildiği `E` subclass'ının MRO'su (`E.__mro__`) `E -> A -> B -> object` şeklindedir. `E` subclass'ının MRO'su `A` base class'ını içerdiği için `super(A, E()).print_msg()` kodu çalıştı. `C()` instance'ın türetildiği `C` subclass'ının MRO'su (`C.__mro__`) `C -> B -> A -> object` şeklindedir. `C` subclass'ının MRO'su `B` base class'ını içerdiği için `super(B, C()).print_msg()` kodu da çalıştı.

**Not:** `super()` fonksiyonunun `<subclass object>` parametresine argüman olarak instance girecekseniz, bu fonsiyonun döndürdüğü proxy objesi üzerinden çağırdığınız instance methodların ilk parametresine argüman olarak `self` (ya da `self` yerine hangi ismi (identifier) kullanıyorsanız onu) girmeniz gerekmemektedir. Girerseniz `TypeError: print_msg() takes 1 positional argument but 2 were given` hatası alırsınız.

`super()` fonksiyonunun döndürdüğü proxy objesi üzerinden class method çağırsanır, bu methodun parantezinin içine `cls` argümanı giremezsiniz (nedenini daha önce anlattım). Girerseniz `TypeError: print_msg() takes 1 positional argument but 2 were given` hatası alırsınız. Örnek:
```py
class A:
    @classmethod
    def print_msg(cls):
        print("Class A")

class B:
    @classmethod
    def print_msg(cls):
        print("Class B")

class C(B, A):
    @classmethod
    def print_msg(cls):
        print("Class C")

class E(A, B):
    @classmethod
    def print_msg(cls):
        super(A, E).print_msg() # Output: Class B
        super(B, C).print_msg() # Output: Class A
        super(A, E()).print_msg() # Output: Class B
        super(B, C()).print_msg() # Output: Class A

var = E()
print(E.__mro__) # Output: (<class '__main__.E'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(C.__mro__) # Output: (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
var.print_msg()
```

`super()` fonksiyonunun döndürdüğü proxy objesi üzerinden static method çağırsanır, bu methodun parantezinin içine `self`, `cls` ya da herhangi bir argüman giremezsiniz (nedenini daha önce anlattım). Örnek:
```py
class A:
    @staticmethod
    def print_msg():
        print("Class A")

class B:
    @staticmethod
    def print_msg():
        print("Class B")

class C(B, A):
    @staticmethod
    def print_msg():
        print("Class C")

class E(A, B):
    @staticmethod
    def print_msg():
        super(A, E).print_msg() # Output: Class B
        super(B, C).print_msg() # Output: Class A
        super(A, E()).print_msg() # Output: Class B
        super(B, C()).print_msg() # Output: Class A

var = E()
print(E.__mro__) # Output: (<class '__main__.E'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(C.__mro__) # Output: (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
var.print_msg()
```

**Not:** Örneklerdeki miras alma olayı multiple inheritance (çoklu miras alma) başlığında anlatılacak. Bu yüzden yukarıdaki kodları anlamadıysanız multiple inheritance öğrendikten sonra burayı tekrar okuyun. 

`super()` fonksiyonunun `<subclass object>` parametresine argüman olarak instance girebileceğimizi öğrenmiştik. Bu instance yerine, instance methodlarda `self`, class methodlarda `cls` isimlerini (identifier) kullanabilirsiniz. Örnek:
```py
class Class1():
    class_attribute = "Class1'in Class Attribute'u"

    def __init__(self):
        self.instance_attribute = "Class1'in Instance Attribute'u"

    def instance_method(self):
        print("Class1'in instance_method'u çalıştı:", end=" ")

    @classmethod
    def class_method(cls):
        print("Class1'in class_method'u çalıştı:", end=" ")

class Class2(Class1):
    def instance_method(self):
        super(Class2, self).instance_method()
        print(self.instance_attribute)

    @classmethod
    def class_method(cls):
        super(Class2, cls).class_method()
        print(cls.class_attribute)

class Class3(Class1):
    def instance_method(self):
        super(Class3, Class3()).instance_method()
        print(self.instance_attribute)

    @classmethod
    def class_method(cls):
        super(Class3, Class3()).class_method()
        print(cls.class_attribute)
        
var1 = Class2()
var2 = Class3()

var1.instance_method() # Output: Class1'in instance_method'u çalıştı: Class1'in Instance Attribute'u
var1.class_method() # Output: Class1'in class_method'u çalıştı: Class1'in Class Attribute'u

var2.instance_method() # Output: Class1'in instance_method'u çalıştı: Class1'in Instance Attribute'u
var2.class_method() # Output: Class1'in class_method'u çalıştı: Class1'in Class Attribute'u
```
Bu kodda `super()` fonksiyonunun `<subclass object>` parametresine bir instance ya da `self`/`cls` kullanmamız bir sıkıntı çıkarmadı. Ama `Class1` base class'ının `__init__` methodunun içinde tanımlı `instance_attribute` instance attribute'unu buradan alıp `instance_method` instance methodunun içine tanımlarsak sıkıntı çıkar. Örnek:
```py
class Class1():
    class_attribute = "Class1'in Class Attribute'u"

    def __init__(self):
        pass

    def instance_method(self):
        self.instance_attribute = "Class1'in Instance Attribute'u"
        print("Class1'in instance_method'u çalıştı:", end=" ")

    @classmethod
    def class_method(cls):
        print("Class1'in class_method'u çalıştı:", end=" ")

class Class2(Class1):
    def instance_method(self):
        super(Class2, self).instance_method()
        print(self.instance_attribute)

    @classmethod
    def class_method(cls):
        super(Class2, cls).class_method()
        print(cls.class_attribute)

class Class3(Class1):
    def instance_method(self):
        super(Class3, Class3()).instance_method()
        print(self.instance_attribute) # AttributeError: 'Class3' object has no attribute 'instance_attribute'

    @classmethod
    def class_method(cls):
        super(Class3, Class3()).class_method()
        print(cls.class_attribute)
        
var1 = Class2()
var2 = Class3()

var1.instance_method() # Output: Class1'in instance_method'u çalıştı: Class1'in Instance Attribute'u
var1.class_method() # Output: Class1'in class_method'u çalıştı: Class1'in Class Attribute'u

var2.instance_method() # Error
var2.class_method() # Output: Class1'in class_method'u çalıştı: Class1'in Class Attribute'u
```
Burada `super(Class2, self).instance_method()` kodu çalışınca `Class1` base class'ının `instance_method` instance methodunun scope'unda tanımlı olan `instance_attribute` instance attribute'u belleğe kaydediliyor ve bu sayede `var1` instance'ı, `instance_attribute` instance attribute'una sahip olmuş oluyor. Ama aynı şey ne hikmetse `super(Class3, Class3()).instance_method()` kodunda gerçekleşmiyor ve bu yüzden `var2` instance'ı, `instance_attribute` instance attribute'una sahip olamıyor. Bu yüzden `print(self.instance_attribute)` kodu `AttributeError: 'Class3' object has no attribute 'instance_attribute'` hatası yükseltiyor. Benzer sorunun `class_method` class methodunda olmamasının sebebi; Python, `Class1` class'ını okurken `class_attribute` class attribute'unu belleğe kaydettiği için inheritance işleminde `Class2` ve `Class3` subclass'ları `class_attribute` class attribute'unu `Class1` base class'ından direkt miras alıp kullanabiliyor ve kendilerinden türetilen instance'lara aktarabiliyor olmasındandır. `AttributeError` hatasına çözüm olarak `Class1` class'ının `instance_method` instance methodunun bloğunun en sonuna `return self.instance_attribute` statement tanımlamak işe yaramaz. Kesin çözüm olarak, `super()` fonksiyonunun `<subclass object>` parametresine `self` argümanını girmeye devam edebilir ya da eski inheritance yöntemini kullanabilirsiniz. Örnek:
```py
class Class1():
    class_attribute = "Class1'in Class Attribute'u"

    def __init__(self):
        pass

    def instance_method(self):
        self.instance_attribute = "Class1'in Instance Attribute'u"
        print("Class1'in instance_method'u çalıştı:", end=" ")

    @classmethod
    def class_method(cls):
        print("Class1'in class_method'u çalıştı:", end=" ")

class Class2(Class1):
    def instance_method(self):
        super(Class2, self).instance_method()
        print(self.instance_attribute)

    @classmethod
    def class_method(cls):
        super(Class2, cls).class_method()
        print(cls.class_attribute)

class Class3(Class1):
    def instance_method(self):
        Class1.instance_method(self)
        print(self.instance_attribute)

    @classmethod
    def class_method(cls):
        super(Class3, Class3()).class_method()
        print(cls.class_attribute)
        
var1 = Class2()
var2 = Class3()

var1.instance_method() # Output: Class1'in instance_method'u çalıştı: Class1'in Instance Attribute'u
var1.class_method() # Output: Class1'in class_method'u çalıştı: Class1'in Class Attribute'u

var2.instance_method() # Output: Class1'in instance_method'u çalıştı: Class1'in Instance Attribute'u
var2.class_method() # Output: Class1'in class_method'u çalıştı: Class1'in Class Attribute'u
```
Gördüğünüz gibi eski inheritance yöntemi olan `Class1.instance_method(self)` kodu, doğrudan `Class1` class'ının `instance_method` instance methodunu çalıştırdığı için bu methodun içindeki `instance_attribute` instance attribute'u belleğe kaydedilir ve bu sayede `var2` instance'ında kullanılabilir. "Bütün olay `Class1` class'ındaki `instance_method` methodunu doğrudan çalıştırmak ise neden `Class1`'in `__init__` methoduna `self.instance_method()` tanımlamıyoruz ki? Böylece `Class2` ve `Class3` subclass'larından instance'lar türetilince `Class1` base class'ının `__init__` methodundaki `self.instance_method()` kodu sayesinde `instance_method` methodu çağırılacağı (call) için `instance_attribute` belleğe kaydedilmiş olur." tarzı bir fikir gelmiş olabilir aklınıza. Ben denedim ve `RecursionError: maximum recursion depth exceeded while calling a Python object` hatası aldım. Bu fikrin işe yarayacağını düşünüyorsanız, aşağıdaki kod üzerinde bu fikir doğrultusunda değişiklikler yapabilir ve aldığınız olumlu sonuçları yorumlarda paylaşabilirsiniz:
```py
class Class1():
    class_attribute = "Class1'in Class Attribute'u"

    def __init__(self):
        self.instance_method() # Error

    def instance_method(self):
        self.instance_attribute = "Class1'in Instance Attribute'u"
        print("Class1'in instance_method'u çalıştı:", end=" ")

    @classmethod
    def class_method(cls):
        print("Class1'in class_method'u çalıştı:", end=" ")

class Class2(Class1):
    def instance_method(self):
        super(Class2, self).instance_method()
        print(self.instance_attribute)

    @classmethod
    def class_method(cls):
        super(Class2, cls).class_method()
        print(cls.class_attribute)

class Class3(Class1):
    def instance_method(self):
        super(Class3, Class3()).instance_method() # RecursionError: maximum recursion depth exceeded while calling a Python object
        print(self.instance_attribute)

    @classmethod
    def class_method(cls):
        super(Class3, Class3()).class_method()
        print(cls.class_attribute)
        
var1 = Class2()
var2 = Class3()

var1.instance_method() # Output: Class1'in instance_method'u çalıştı: Class1'in Instance Attribute'u
var1.class_method() # Output: Class1'in class_method'u çalıştı: Class1'in Class Attribute'u

var2.instance_method() # Error
var2.class_method() # Output: Class1'in class_method'u çalıştı: Class1'in Class Attribute'u
```

`<subclass object>` parametresinde `self`/`cls` kullanacaksanız, illa bu isimleri (identifier) kullanmak zorunda değilsiniz. Örnek:
```py
class Class1():
    class_attribute = "Class1'in Class Attribute'u"

    def __init__(self):
        pass

    def instance_method(self):
        self.instance_attribute = "Class1'in Instance Attribute'u"
        print("Class1'in instance_method'u çalıştı:", end=" ")

    @classmethod
    def class_method(cls):
        print("Class1'in class_method'u çalıştı:", end=" ")

class Class2(Class1):
    def instance_method(instance_exp):
        super(Class2, instance_exp).instance_method()
        print(instance_exp.instance_attribute)

    @classmethod
    def class_method(class_exp):
        super(Class2, class_exp).class_method()
        print(class_exp.class_attribute)
        
var1 = Class2()
var1.instance_method() # Output: Class1'in instance_method'u çalıştı: Class1'in Instance Attribute'u
var1.class_method() # Output: Class1'in class_method'u çalıştı: Class1'in Class Attribute'u
```
Buradaki önemli nokta; `super()` fonksiyonunun `<subclass object>` parametresine girilen argümanın isminin (identifier), `super()` fonksiyonunun bulunduğu methodun ilk parametresinin ismi (identifier) ile aynı olmasıdır.

Static methodların scope'undaki local variable'lara ulaşabilmek için bu variable'ları `return` keyword'ü ile döndürmek gerekir. Çünkü bu local variable'lar, static method sonlandıktan sonra bellekten silinir, instance ve class methodlardaki instance ve class attribute'lar gibi bellekte kalmaya devam etmez. Aynı zamanda static methodlarda instance ve class methodlardaki gibi `<subclass object>` parametresinde `self`/`cls` isimeri (identifier) kullanamayacağımız için bu parametreye instance tanımlanır. Örnek:
```py
class Class1():
    @staticmethod
    def static_method():
        static_attribute = "Class1'in Static Attribute'u"
        print("Class1'in static_method'u çalıştı:", end=" ")
        return static_attribute

class Class2(Class1):
    @staticmethod
    def static_method():
        static_attribute = super(Class2, Class2()).static_method()
        print(static_attribute)
        
var2 = Class2() # Output: init çalıştı...
var2.static_method() # Output: Class1'in static_method'u çalıştı: Class1'in Static Attribute'u
```

Instance, class ve static methodlarda inheritance işlemi yaparken kullanılan `super()` fonksiyonunun `<subclass object>` parametresine argüman olarak `self`/`cls` isimleri (identifier) yerine instance girildiğinde, Python istenmeyen davranışlar sergileyebilir. Örnek:
```py
class Class1():
    class_attribute = "Class1'in Class Attribute'u"

    def __init__(self):
       print("...İnit Çalıştı...", end=" | ")
       self.instance_attribute = "Class1'in Instance Attribute'u"

    def instance_method(self):
        print("Class1'in instance_method'u çalıştı:", end=" ")

    @classmethod
    def class_method(cls):
        print("Class1'in class_method'u çalıştı:", end=" ")

    @staticmethod
    def static_method():
        static_attribute = "Class1'in Static Attribute'u"
        print("Class1'in static_method'u çalıştı:", end=" ")
        return static_attribute

class Class2(Class1):
    def instance_method(self):
        super(Class2, self).instance_method()
        print(self.instance_attribute)

    @classmethod
    def class_method(cls):
        super(Class2, cls).class_method()
        print(cls.class_attribute)

    @staticmethod
    def static_method():
        static_attribute = super(Class2, Class2()).static_method()
        print(static_attribute)

class Class3(Class1):
    def instance_method(self):
        super(Class3, Class3()).instance_method()
        print(self.instance_attribute)

    @classmethod
    def class_method(cls):
        super(Class3, Class3()).class_method()
        print(cls.class_attribute)

    @staticmethod
    def static_method():
        static_attribute = super(Class3, Class3()).static_method()
        print(static_attribute)
        
var1 = Class2() # Output: ...İnit Çalıştı... |
print("\n")
var2 = Class3() # Output: ...İnit Çalıştı... |
print("\n")

var1.instance_method() # Output: Class1'in instance_method'u çalıştı: Class1'in Instance Attribute'u
var1.class_method() # Output: Class1'in class_method'u çalıştı: Class1'in Class Attribute'u
var1.static_method() # Output: ...İnit Çalıştı... | Class1'in static_method'u çalıştı: Class1'in Static Attribute'u 

var2.instance_method() # Output: ...İnit Çalıştı... | Class1'in instance_method'u çalıştı: Class1'in Instance Attribute'u
var2.class_method() # Output: ...İnit Çalıştı... | Class1'in class_method'u çalıştı: Class1'in Class Attribute'u   
var2.static_method() # Output: ...İnit Çalıştı... | Class1'in static_method'u çalıştı: Class1'in Static Attribute'u 
```
Yukarıdaki kodda, `super()` fonksiyonunun `<subclass object>` parametresine argüman olarak `self`/`cls` yerine `Class2()` ve `Class3()` instance'larını girince Python'un davranışlarını `super(Class3, Class3()).instance_method()` kodu üzeriden açıklamak gerekirse:
- Python, `super(Class3, Class3()).instance_method()` kodunun `Class3()` kısmını okuduktan hemen sonra `Class3` class'ından bir instance türetir.
- `Class3` class'ından bir instance türetildiğinde, `Class3` subclass'ında `__init__` methodu olmadığı için `Class3` subclass'ının miras aldığı `Class1` base class'nın `__init__` methodu çalışır.
- `Class1` base class'nın `__init__` methodu çalıştığı için bu methodun bloğundaki `print("...İnit Çalıştı...", end=" | ")` fonksiyonu çalışır ve `...İnit Çalıştı... | ` yazdırılır.

Bu sorunu, instance ve class methodlarda kullanılan `super()` fonksiyonunun `<subclass object>` parametresinde argüman olarak `self` ve `cls` isimlerini (identifier) girerek, static methodlarda da `super()` fonksiyonu yerine eski inheritance yöntemini olan `Class1.static_method()` kodunu kullanarak çözebiliriz. Kanıtı:
```py
class Class1():
    class_attribute = "Class1'in Class Attribute'u"

    def __init__(self):
        print("...İnit Çalıştı...", end=" | ")
        self.instance_attribute = "Class1'in Instance Attribute'u"

    def instance_method(self):
        print("Class1'in instance_method'u çalıştı:", end=" ")

    @classmethod
    def class_method(cls):
        print("Class1'in class_method'u çalıştı:", end=" ")

    @staticmethod
    def static_method():
        static_attribute = "Class1'in Static Attribute'u"
        print("Class1'in static_method'u çalıştı:", end=" ")
        return static_attribute

class Class2(Class1):
    def instance_method(self):
        super(Class2, self).instance_method()
        print(self.instance_attribute)

    @classmethod
    def class_method(cls):
        super(Class2, cls).class_method()
        print(cls.class_attribute)

    @staticmethod
    def static_method():
        static_attribute = Class1.static_method()
        print(static_attribute)

var1 = Class2() # Output: ...İnit Çalıştı... |
print("\n")

var1.instance_method() # Output: Class1'in instance_method'u çalıştı: Class1'in Instance Attribute'u
var1.class_method() # Output:Class1'in class_method'u çalıştı: Class1'in Class Attribute'u
var1.static_method() # Output: Class1'in static_method'u çalıştı: Class1'in Static Attribute'u
```

**Not:** Instance ve class method'larında inheritance işlemi yaparken kullandığımız `super()` fonksiyonunun parametrelerine argüman tanımlayarak kullanmakla argüman tanımlamadan kullanmak arasında hiçbir fark yoktur. Yani yukarıdaki örnekte olduğu gibi `super()` fonksiyonunu `super(Class2, self)` ve `super(Class2, cls)` ile `super()` şeklinde kullanmak arasında hiçbir fark yoktur. Bu durum Python'ın, instance ve class methodlarda kullanılan `super()` fonksiyonunun parametrelerine doğru argümanları otomatik olarak girmesinden kaynaklanır. Bu yüzden özel durumlar dışında `super()` fonksiyonunun parametresiz kullanılması tavsiye edilir. Eğer parametresiz kulanamıyorsanız, programınızda büyük tasarım hatalar var demektir.

`super()` fonksiyonu Python'a sonradan eklenmiştir. `super()` fonksiyonu eklenmeden önce bu fonksiyonun yerine doğrudan base class'ın ismi (identifier) kullanılıyordu. Örnek:
```py
class Class1():
    class_attribute = "Class1'in Class Attribute'u"
    
    def __init__(self):
        print("init çalıştı...")

    def instance_method(self):
        self.instance_attribute = "Class1'in Instance Attribute'u"
        print("Class1'in instance_method'u çalıştı:", end=" ")

    @classmethod
    def class_method(cls):
        cls.class_attribute
        print("Class1'in class_method'u çalıştı:", end=" ")

    @staticmethod
    def static_method():
        static_attribute = "Class1'in Static Attribute'u"
        print("Class1'in static_method'u çalıştı:", end=" ")
        return static_attribute

class Class2(Class1):
    def __init__(self):
        Class1.__init__(self)

    def instance_method(self):
        Class1.instance_method(self)
        print(self.instance_attribute)

    @classmethod
    def class_method(cls):
        Class1.class_method()
        print(cls.class_attribute)

    @staticmethod
    def static_method():
        print(Class1.static_method())
        
var = Class2() # Output: init çalıştı...
var.instance_method() # Output: Class1'in instance_method'u çalıştı: Class1'in Instance Attribute'u
var.class_method() # Output: Class1'in class_method'u çalıştı: Class1'in Class Attribute'u
var.static_method() # Output: Class1'in static_method'u çalıştı: Class1'in Static Attribute'u
```
Bu kodda dikkat çekilmesi gereken şey; `var` instance'ı üzerinden `instance_method` instance methodunu çağırırken kullanılan `var.instance_method()` kodunun parantezlerine (instance'ı temsil eden) `self` yazamadığımız gibi, `Class1` base class'ı üzerinden `class_method` class methodunu çağırırken kullanılan `Class2.class_method()` kodunun parantezlerine (class'ı temsil eden) `cls` yazamayız (nedenini daha önce anlattım).

# Multiple Inheritance (Çoklu Miras Alma)
Bir subclass'ın birden fazla base class'dan miras almasına **Multiple Inheritance (Çoklu Miras Alma)** denir. Örnek:
```py
class A():
    def a(self):
        print("A a()")

class B():
    def b(self):
        print("B b()")

class C():
    def c(self):
        print("C c()")

class D(A, B, C):
    pass

var = Class4()
var.a() # Output: A a()
var.b() # Output: B b()
var.c() # Output: C c()
```
Buradaki `D` subclass'ı sırasıyla `A`, `B` ve `C` class'larından miras almıştır.

Bir subclass'ın miras aldığı class'larda aynı isme (identifier) sahip method veya attribute'lar varsa, bu subclass, bu method veya attribute'ları miras alma konusunda, kendi MRO'sundaki (kendisi hariç) soldan ilk sırada bulunan class'a öncelik verir. Örnek:
```py
class A():
    def method_exp(self):
        print("Class A")

class B():
    def method_exp(self):
        print("Class B")

class C():
    def method_exp(self):
        print("Class C")

class D(A, B, C):
    pass

var = D()
print(D.__mro__) # Output: (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)
var.method_exp() # Output: Class A
```
`D` subclass'ının MRO'su `D -> A -> B -> C -> object` şeklindedir. `D` subclass'ı `method_exp()` methodunu, `D` subclass'ının MRO'suna göre öncelikli olan `A` class'ından alıp, diğer class'lardaki `method_exp()` methodlarını görmezden geldi. Eğer `A` class'ında `method_exp()` methodu olmasaydı, `D` subclass'ı bu methodu bulana kadar kendi MRO'sunda soldan sağa doğru bütün class'lara bakacaktı. Eğer `D` subclass'ının MRO'sunda belirtilen class'ların hiçbirinde `method_exp()` methodu bulunamazsaydı, `AttributeError: 'D' object has no attribute 'method_exp'` hatası yükseltilirdi.

İlla MRO'da belirtilen sıraya uymak zorunda değilsiniz. Bu MRO'da belirtilen sıranın herhangi bir yerindeki class'dan method çekip kullanabilirsiniz. Örnek:
```py
class A:
    def print_msg(self):
        print("Class A")

class B:
    def print_msg(self):
        print("Class B")

class C:
    def print_msg(self):
        print("Class C")

class D(A, B, C):
    def print_msg(self):
        super(D, self).print_msg() # Output: Class A
        super(A, self).print_msg() # Output: Class B
        super(B, self).print_msg() # Output: Class B

var1 = D()
print(D.__mro__) # Output: (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)
var1.print_msg()
```
Yukarıdaki `super()` fonksiyonlarının hepsinin `<subclass object>` parametresine girilen `self` argümanı, `D` subclass'ının MRO'sunu (`D -> A -> B -> C -> object`) ifade etmektedir. Buradaki `super()` fonksiyonlarının nasıl davrandığını açıklayalım:

- `super(D, self).print_msg()` kodundaki `super(D, self)` fonksiyonu, `A -> B -> C -> object` MRO'sunu dikkate alır. `super(D, self)` fonksiyonu, bu MRO'ya göre öncelikli olan `A` base class'ının proxy objesini oluşturur. `super(D, self).print_msg()` kodu sayesinde `A` base class'ının proxy objesindeki `print_msg` methodu miras alınır. Bu yüzden `var1.print_msg()` kodu `Class A` output'unu verir.

- `super(A, self).print_msg()` kodundaki `super(A, self)` fonksiyonu, `B -> C -> object` MRO'sunu dikkate alır. `super(A, self)` fonksiyonu, bu MRO'ya göre öncelikli olan `B` base class'ının proxy objesini oluşturur. `super(A, self).print_msg()` kodu sayesinde `B` base class'ının proxy objesindeki `print_msg` methodu miras alınır. Bu yüzden `var1.print_msg()` kodu `Class B` output'unu verir.

- `super(B, self).print_msg()` kodundaki `super(B, self)` fonksiyonu, `C -> object` MRO'sunu dikkate alır. `super(B, self)` fonksiyonu, bu MRO'ya göre öncelikli olan `C` base class'ının proxy objesini oluşturur. `super(B, self).print_msg()` kodu sayesinde `C` base class'ının proxy objesindeki `print_msg` methodu miras alınır. Bu yüzden `var1.print_msg()` kodu `Class C` output'unu verir.

- Eğer `super(C, self).print_msg()` olsaydı, bu koddaki `super(C, self)` fonksiyonu, `object` MRO'sunu dikkate alırdı. `super(C, self)` fonksiyonu, bu MRO'ya göre öncelikli olan `object` base class'ının proxy objesini oluştururdu. `super(C, self).print_msg()` kodu sayesinde `object` base class'ının proxy objesindeki `print_msg` methodu miras alınmaya çalışırdı ama `object` base class'ının proxy objesinde `print_msg` adında bir method olmadığı için `AttributeError: 'super' object has no attribute 'print_msg'` hatası yükseltecekti.

`super()` fonksiyonunu kullanarak bir subclass'ın miras almadığı (yani parantezine yazılmayan) class'lardan bile miras alabilirsiniz. Örnek:
```py
class A:
    def print_msg(self):
        print("Class A")

class B:
    def print_msg(self):
        print("Class B")

class C:
    def print_msg(self):
        print("Class C")

class D(C):
    def print_msg(self):
        super(D, self).print_msg() # Output: Class C

class E(A, B, C):
    def print_msg(self):
        super(D, D()).print_msg() # Output: Class C

var = E()
print(E.__mro__) # Output: (<class '__main__.E'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)
print(D.__mro__) # Output: (<class '__main__.D'>, <class '__main__.C'>, <class 'object'>)
var.print_msg()
```
Gördüğünüz gibi `E` subclass'ı `D` subclass'ını miras almasa (`E` subclass'ının parantezine yazılı olmasa) bile `super(D, D()).print_msg()` kodu çalıştı ve miras alma işlemi başarıyla gerçekleşti. Bu işlem sırasıyla şöyle gerçekleşti:

- `super(D, D()).print_msg()` kodundaki `super()` fonksiyonu, bu fonksiyonun `<subclass object>` parametresine argüman olarak girilen `D()` instance'ının türetildiği `D` subclass'ının MRO'sunu (`D -> C -> object`) dikkate alarak, `<subclass>` parametresine argüman olarak girilen `D` class'ından sonrasını (`C -> object`) miras aldı.

- Python, `C -> object` MRO'suna göre `print_msg` methodu ilk `C` class'ında bulunduğu için `super(D, D()).print_msg()` kodundaki `super(D, D())` fonksiyonu, `C` class'ının proxy objesini döndürdü.

- Python bu proxy objesinin üzerinde `print_msg()` methodunu çağırdı ve sonuç olarak `Class C` yazdırıldı.

Subclass'ın miras almadığı (subclass'ın parantezine yazılmamış) class'lardan miras almak için `super()` yerine eski yöntemi de kullanabilirsiniz. Örnek:
```py
class A:
    def print_msg(self):
        print("Class A")

class B:
    def print_msg(self):
        print("Class B")

class C:
    def print_msg(self):
        print("Class C")

class D(C):
    def print_msg(self):
        C.print_msg(self)

class E(A, B, C):
    def print_msg(self):
        D.print_msg(self)

var = E()
print(E.__mro__) # Output: (<class '__main__.E'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)
print(D.__mro__) # Output: (<class '__main__.D'>, <class '__main__.C'>, <class 'object'>)
var.print_msg()
```
**Dikkat:** Yukarıdaki kodda `D` subclass'ında `C.print_msg(self)` yerine `super(D, self).print_msg()` kullanırsanız, `super(D, self).print_msg()` kodundan dolayı Python `TypeError: super(type, obj): obj must be an instance or subtype of type` hatası yükseltir. Kanıtı:
```py
class A:
    def print_msg(self):
        print("Class A")

class B:
    def print_msg(self):
        print("Class B")

class C:
    def print_msg(self):
        print("Class C")

class D(C):
    def print_msg(self):
        super(D, self).print_msg() # TypeError: super(type, obj): obj must be an instance or subtype of type

class E(A, B, C):
    def print_msg(self):
        D.print_msg(self) # Error

var = E()
print(E.__mro__) # Output: (<class '__main__.E'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)
print(D.__mro__) # Output: (<class '__main__.D'>, <class '__main__.C'>, <class 'object'>)
var.print_msg() # Error
```
`D.print_msg(self)` kodundaki `self`, `E` subclass'ının instance'ını temsil etmektedir. Bu yüzden `D.print_msg(self)` kodundaki `self` argümanı, `D` class'ında tanımlı olan `def print_msg(self):` kodundaki `self` parametresine girilmiş oluyor. Dolayısıyla bu argüman `print_msg` fonksiyonunun bloğunda tanımlı olan `super(D, self).print_msg()` kodundaki `self`'e de girilmiş oluyor. `<subclass>` parametresine girilen subclass, `<subclass object>` parametresine girilen subclass'ın MRO'sunda bulunmadığı için `TypeError: super(type, obj): obj must be an instance or subtype of type` hatası yükseltilir.

**Not:** `super()` fonksiyonunu kullanırken `RuntimeError: super(): no arguments` hatası alıyorsanız, büyük ihtimal ya bir instance veya class method'a `self` veya `cls` parametresi eklemeyi unuttunuz ya da `super()` fonksiyonunun parametrelerine yanlış argümanlar girdiniz.

**Not:** `<subclass object>` parametresinin ne olduğunu ve nasıl kullanıldığını anlamadıysanız, OOP konusunun en başında `self` ve `cls`'nin ne olduğunu anlattığım kısımları okuyup sonra bu kısmı tekrardan okuyunuz.

**Not:** Tekrar söyleyeyim; burada anlatılan şeyler deneysel olduğu için inheritance konusunu farklı kaynaklardan da çalışmanızda fayda var.

# Abstract Class
Abstract class'lar, aynı özellikleri taşıyan objeleri aynı çatı altında toplayıp bir template (şablon) oluşturmamızı ve bu abstract class'dan miras alan bütün subclass'ları bu template'e uymak zorunda bırakabilmemizi sağlıyor. Buradaki template olayına şöyle açıklayabilirim; Bütün insanlar uyumak, yemek, nefes almak gibi temel işlevleri yapar. Daha özele indiğimizde ise bazı insanlar bu işlevlere ek olarak futbol oynamak, kitap yazmak gibi daha özel işlevleri yapar. O zaman buradaki uyumak, yemek, nefes almak gibi temel işlevler, insanların template'idir.

## Abstract Class Özellikleri:
- Abstract class'lar, en az bir tane abstract method içermelidir.
- 

https://www.geeksforgeeks.org/abstract-classes-in-python/

https://startupvadisi.com/python-oop-soyutlama-abstraction/

https://www.obenseven.com.tr/yazilim/python/nesne-tabanli-programlama/python-kompozisyon-composition/

https://www.sinanerdinc.com/python-abc-modulu-kullanimi