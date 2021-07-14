# Inheritance (Miras Alma)
Bir class'ın, başka bir class'ın method ve class attribute'larına miras alma yoluyla erişip kullanabilmesine **Inheritance (Miras Alma)** denir. Method ve class attribute'ları miras alınan class'a parent class, super class, base class olarak isimlendirilir. Base class'ın method ve class attribute'larını miras alan class'da child class, derived class, subclass olarak isimlendirilir. Ben tutorial boyunca bunlardan **base class** ve **subclass** olarak bahsedeceğim. Inheritance (Miras Alma), belli method'ları ya da class attribute'ları her class'a tekrar tekrar yazma zahmetinden bizi kurtarır. Örnek:
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

Gördüğünüz gibi `Class2` subclass'ı, `Class1` base class'ın method (`__init__` ve dolayısıyla `__init__`'deki instance attribute'lar dahil) ve class attribute'larını miras almış.

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

Gördüğünüz gibi `Class2` subclass'ındaki instance method objesinde `function Class1.func1` yazmaktadır. Buradaki `Class1.func1` ifadesi, `func1` fonksiyonunun `Class1`'in instance method objesi olduğunu söylemektedir. Yani `Class2` subclass'ındaki `func1` objesi, `Class1` base class'ındaki `func1` objesine atıfta bulunur. atıfta bulunma durumu söz konusu olduğu için base class'da bir değişiklik yapıldığında bundan subclass'da etkilenir. Örneğin Yukarıdaki koda `Class1.cs1 = "Yeni Class Attribute 1"` kodunu ekleyip çalıştırırsak, hem `Class1` base class'ının hem de `Class2` subclass'ının `cs1` class attribute'unun değeri değişir. Kanıtı:

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

**Not:** Bir subclass'ın üzerinde, bir base class'ın her şeyini miras almak dışında ekstra method veya class attribute tanımlamak gibi bir işlem yapmayacaksanız, bu subclass'ı yukarıdaki koddaki gibi tanımlamak yerine `Class2 = Class1()` şeklinde doğrudan instance olarak oluşturmak daha pratiktir.

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

print(dir(Class1) == dir(Class2)) # Output: True
var1 = Class1() # Output: Class1 init çalıştı...
var2 = Class2() # Output: Class1 init çalıştı...
var1.func1() # Output: func1 Çalıştı...
var2.func1() # Output: Class2'deki func1 Çalıştı...
```
Gördüğünüz gibi `Class2` subclass'ında `func1` instance methodu zaten tanımlı olduğu için inheritance (miras alma) işleminden sonra `Class1` base class'ının `func1` instnace methodu override edildi ve `var.func1()` kodu `Class1` base class'ının `func1` instnace methodundaki `print("func1 Çalıştı...")` kodunu değil, `Class2` base class'ının `func1` instnace methodundaki `print("Class2'deki func1 Çalıştı...")` kodunu çalıştırdı. Aynı şey class attribute'lar için de geçerlidir. Örnek:
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
Bir subclass'da, base class'dan miras alınan methodların içeriğine ufak eklemeler yapmak veya içeriğindeki bir attribute'un değerini değiştirmek istediğinizde, bu methodları override etmiş sayıldığınız için veri kaybı yaşarsınız. Örnek:
```py
class Class1():
    def __init__(self):
        print("init çalıştı...")
        self.a = 1
        self.b = 2
        self.c = 3

class Class2(Class1):
    def __init__(self):
        self.a = 4
        
var1 = Class1() # Output: init çalıştı...
var2 = Class2()
print(var1.a) # Output: 1
print(var1.b) # Output: 2
print(var1.c) # Output: 3
print(var2.a) # Output: 4
print(var2.b) # AttributeError: 'Class2' object has no attribute 'b'
print(var2.c) # AttributeError: 'Class2' object has no attribute 'c'
```
Yukarıdaki kodda `Class1` base class'ından miras aldığımız `self.a` instance attribute'unun değerini `4` olarak yeniden tanımlamak (redefinition) istedik ama bunu yaparak `Class2` subclass'ında `__init__` tanımlamış olduğumuz için `Class1` base class'ındaki `__init__` override edildi. Bu yüzden `Class2` subclass'ında `b` ve `c` instance attribute'larına ulaşamayıp veri kaybı yaşadık. Bu sorunu yaşamamak için `super()` fonksiyonu kullanılır.

#### `super(<subclass>, <subclass object>)` Fonksiyonu
**Başlamadan önce oku:** `super()` fonksiyonu **MRO** (Method Resolution Order) ile çalışan bir mekanizmaya dayanır. Bu fonksiyonun nasıl çalıştığını daha detaylı öğrenebilmek için MRO'yu (Method Resolution Order) ve `super()` fonksiyonunu parametreleri ile birlikte kendiniz de araştırmalısınız. Ben baya araştırdım ama çalışma prensibini bütün ayrıntılarıyla anlatan bir kaynak bulamadım. Bu yüzden `super()` fonksiyonunu anlatırken, bu fonksiyonun farklı senaryolardaki davranışlarını size göstererek `super()` fonksiyonunu anlatmaya çalışacağım.

`super()` build-in fonksiyonu, base class'ın istediğimiz bir method'una erişmemizi sağlayan bir proxy objesi (base class'ın geçici (temporary) objesi) döndürür. Bu sayede subclass methodlarının içeriğini değiştirirken override sorununun yolumuza çıkmasını engellemiş oluyoruz. Örnek:
```py
class Class1():
    def __init__(self, p1, p2, p3):
        print("init çalıştı...")
        self.a = p1
        self.b = p2
        self.c = p3

class Class2(Class1):
    def __init__(self, p1, p2, p3, p4):
        super().__init__(p1, p2, p3)
        self.d = p4

var1 = Class1(1,2,3) # Output: init çalıştı...
var2 = Class2(1,2,3,4) # Output: init çalıştı...
print(var1.a) # Output: 1
print(var1.b) # Output: 2
print(var1.c) # Output: 3
print(var2.a) # Output: 1
print(var2.b) # Output: 2
print(var2.c) # Output: 3
print(var2.d) # Output: 4
```
Gördüğünüz gibi  `Class2` subclass'ından türetilmiş `var2` instance'sini kullanarak, `Class2` subclass'ının `__init__` methoduna elle tanımlamadığımız instance attribute'lara bile erişebiliyoruz. Bunu, `super()` build-in fonksiyonunun döndürdüğü proxy objesine borçluyuz. Başka bir örnek:
```py
class Class1():
    def __init__(self, p1, p2, p3):
        print("init çalıştı...")
        self.a = p1
        self.b = p2
        self.c = p3

class Class2(Class1):
    def __init__(self, p4, *args):
        super().__init__(*args)
        self.d = p4

var1 = Class1(1,2,3) # Output: init çalıştı...
var2 = Class2(1,2,3,4) # Output: init çalıştı...
print(var1.a) # Output: 1
print(var1.b) # Output: 2
print(var1.c) # Output: 3
print(var2.a) # Output: 1
print(var2.b) # Output: 2
print(var2.c) # Output: 3
print(var2.d) # Output: 4
```
Eğer parametreleri tek tek tanımlamak istemiyorsanız, yukarıdaki gibi bir tane base class'daki method'un parametreleri için, bir tane de subclass'daki method'un parametreleri için `*args` (`p1 = "Falan Filan"` gibi default value'ya sahip parametreler varsa `*args` yerine `**kwargs`) tanımlamanız yeterlidir. Başka bir örnek:
```py
class Class1():
    def __init__(self, p1, p2, p3):
        print("init çalıştı...")
        self.a = p1
        self.b = p2
        self.c = p3

class Class2(Class1):
    def __init__(self, a1):
        super().__init__(a1, a1, a1)
        self.d = a1

var1 = Class1(1,2,3) # Output: init çalıştı...
var2 = Class2(1) # Output: init çalıştı...
print(var1.a) # Output: 1
print(var1.b) # Output: 2
print(var1.c) # Output: 3
print(var2.a) # Output: 1
print(var2.b) # Output: 1
print(var2.c) # Output: 1
print(var2.d) # Output: 1
```
Gördüğünüz gibi `super()` fonksiyonunu ilk koddaki gibi `super().__init__(p1, p2, p3)` şeklinde yazamıyoruz. Çünkü `super().__init__(p1, p2, p3)` kodundaki `__init__(p1, p2, p3)` kodu fonksiyon tanımlama (function definition) olarak değerlendirilmediği için `p2` ve `p3` isimleri (identifier) parametre olarak değerlendirilmiyor. Bu yüzden Python, `p2` ve `p3` kısımlarını okuduğunda `NameError: name 'p2' is not defined` ve `NameError: name 'p3' is not defined` hatalarını döndürür. Bu sorunla karşılaşmamak için `super().__init__(p1, p2, p3)` kodundaki `p2` ve `p3` isimleri (identifier) yerine, bulunduğunuz scope'da tanımlı olan (`a1` gibi) isimleri (identifier) kullanmalısınız.

`super()` build-in fonksiyonu `__init__` instance methodunda olduğu gibi diğer instance, class ve static methodlarda da kullanabiliriz. Örnek:
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

------------------------------------------------------------------->

<-------------------------------------------------------------------

**Not:** Genelde parametresiz super() kullanımı tavsiye edilir. Eğer parametresiz kulanamıyorsanız, programınızda büyük tasarım hataları var demektir.

`super()` fonksiyonu Python'a sonradan eklenmiştir. `super()` fonksiyonu eklenmeden önce bu fonksiyonun yerine doğrudan base class'ın adı kullanılıyordu. Örnek:
```py
class Class1():
    def instance_method(self):
        self.instance_attribute = "Class1'in Instance Attribute'u"
        print("Class1'in instance_method'u çalıştı:", end=" ")

class Class2(Class1):
    def instance_method(self):
        super().instance_method()
        print(self.instance_attribute)

class Class3(Class1):
    def instance_method(self):
        Class1.instance_method(self)
        print(self.instance_attribute)

var1 = Class2()
var2 = Class3()
var1.instance_method() # Output: Class1'in instance_method'u çalıştı: Class1'in Instance Attribute'u
var2.instance_method() # Output: Class1'in instance_method'u çalıştı: Class1'in Instance Attribute'u
```
Gördüğünüz gibi `super().instance_method()` kodu yerine `Class1.instance_method(self)` kullanabiliyoruz. `Class1.instance_method(self)` kodunun `super().instance_method()` kodundan en önemli farkı, `self` instance objesini method'a parametre olarak tanımlamak zorunda olmamız. Tüm method type'larından örnek:
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
        super(Class2, self).__init__()

    def instance_method(self):
        super(Class2, self).instance_method()
        print(self.instance_attribute)

    @classmethod
    def class_method(cls):
        super(Class2, cls).class_method()
        print(cls.class_attribute)

    @staticmethod
    def static_method():
        print(super(Class2, Class2()).static_method())

class Class3(Class1):
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
        
var1 = Class2() # Output: init çalıştı...
var2 = Class3() # Output: init çalıştı...
var1.instance_method() # Output: Class1'in instance_method'u çalıştı: Class1'in Instance Attribute'u
var1.class_method() # Output: Class1'in class_method'u çalıştı: Class1'in Class Attribute'u
var1.static_method() # Output: "init çalıştı...\nClass1'in static_method'u çalıştı: Class1'in Static Attribute'u"
var2.instance_method() # Output: Class1'in instance_method'u çalıştı: Class1'in Instance Attribute'u
var2.class_method() # Output: Class1'in class_method'u çalıştı: Class1'in Class Attribute'u
var2.static_method() # Output: Class1'in static_method'u çalıştı: Class1'in Static Attribute'u
```
Bu kodda `var1.static_method()` kodunun `Class1` class'ındaki `__init__` constructor'ını neden çalıştırdığını daha önce anlatmıştık. Özet:
- `var1.static_method()` kodu `Class2`'deki `static_method()`'u çalıştırır.
- `Class2` deki `static_method()` çalıştığı için bu methodun bloğundaki `super(Class2, Class2()).static_method()` kodu çalışır.
- `super(Class2, Class2()).static_method()` kodu çalıştığı için bu koddaki `Class2()` çalışır.
- `Class2()` çalıştığı için `Class2` class'ının `__init__` constructor'ı çalışır.
- `Class2` class'ının `__init__` constructor'ı çalıştığı için bu constructor'ın bloğundaki `super(Class2, self).__init__()` kodu çalışır.
- `super(Class2, self).__init__()` kodu çalıştığı için `Class1` class'ının `__init__` constructor'ı çalışır.
- `Class1` class'ının `__init__` constructor'ı çalışıtığı için bu constructor'ın bloğundaki `print("init çalıştı...")` çalışır.
- `print("init çalıştı...")` çalıştığı için `init çalıştı...` yazdırılır.

`Class3`'ün `class_method()`'unun bloğundaki `Class1.class_method()` kodunun parantezinin içine, `instance_method()` method'unun bloğundaki `Class1.instance_method(self)` kodunun parantezinin içine `self` yazdığımız gibi `cls` yazamamızın sebebi; nasıl bir instance'ın üzerinden bir instance method çağırırken (`var1.instance_method()` gibi) instance methodlarda kullanılan `self` parametresini tanımlamıyorsan (`var1.instance_method(self)` gibi), bir main class'ın üzerinden bir class method çağırırken (`Class2.instance_method()` gibi) de class methodlarda kullanılan `cls` parametresini tanımlayamazsın (`varClass21.instance_method(cls)` gibi).

## Object Class
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
Python'ın' 3.x öncesi sürümlerinde, yeni tip class'larla birlikte gelen bazı özellikler vardı (Örneğin `@property` decorator'u). Bir class'da yeni tip özellikleri kullanmak istediğinizde, bu class'ın `object` adındaki bir class'da miras alması gerekiyordu. Eski tip class'lar `object` adındaki bir class'da miras almadıkları için bu yeni tip özellikleri kullanamıyorlardı. Python 3'den sonra, bütün class'lar yeni tip class olarak güncellenmiştir. Bu yüzden Python 3'den sonra bir class, `object` adındaki bir class'da miras alsa da almasa da yeni tip özellikleri kullanabilir. Yani Python 3'den sonra aşağıdaki class tanımlamaları arasında hiçbir fark yoktur:
```py
class Sınıf:
    pass

class Sınıf():
    pass

class Sınıf(object):
    pass
```