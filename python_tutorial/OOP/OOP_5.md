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

`Class2` subclass'ının `static_method` static methodunun bloğundaki `super(Class2, Class2()).static_method()` kodunda da gördüğünüz gibi `super()` fonksiyonunun `<subclass>` ve `<subclass object>` olmak üzere 2 parametresi vardır. Bu parametreleri tanımlamasanız bile 
- `<subclass>` parametresine argüman olarak `super()` fonksiyonunun tanımlı olduğu subclass objesi verilmelidir. `super()` fonksiyonunu `<subclass>` parametresinde belirtilen subclass'ın base class'ından miras alır (MRO (Method Resolution Order)).
- `<subclass object>` parametresine argüman olarak `super()` fonksiyonunun tanımlı olduğu subclass objesinin instance'ı (örneğin `Class1` adındaki subclass'ın instance'ı `Class1()`'dir) verilmelidir. Bunun yerine instance methodlarda `self`, class methodlarda `cls` kelimeleri de verilebilir. Örnek:
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
Gördüğünüz gibi subclass'dan türetilmiş instance ya da `self`/`cls` kullanmamız bir farklılığa neden olmadı. Ama `Class1` base class'ının `__init__` methodunun içinde tanımlı `instance_attribute` instance attribute'unu buradan alıp `instance_method` instance methodunun içine tanımlarsak sıkıntı çıkar. Örnek:
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
Gördüğünüz gibi `instance_attribute`'una ulaşamadığımız için `print(self.instance_attribute)` kodu hata verdi. Bunun çözümek için `Class1` base class'ının `instance_method` instance methodunun bloğuna `return self.instance_attribute` tanımlasak bile hata almaya devam ederiz. Buna çözüm olarak `self` kullanmaya devam edebilir ya da eski inheritance yöntemini kullanabilirsiniz. Örnek:
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
        print(self.instance_attribute) # AttributeError: 'Class3' object has no attribute 'instance_attribute'

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
Eski inheritance yöntemini olan `Class1.instance_method(self)` kodunun nasıl çalıştığı daha sonra anlatılacak.

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
instance ve class method'ları anlatırken, bu methodların ilk parametresine yazdığımız şeyin, bu methodların bloğuna tanımlanacak attribute'lara prefix olarak kullanılmak dışında bir önemi olmadığı için bu parametrenin isminin `self`/`cls` olmak zorunda olmadığını, herhangi bir ismin (identifier) kullanılabileceğini söylemiştik.

Static methodlar'da inheritance işlemi yaparken, static methodun bloğunda kullanılan `super()` fonksiyonunun `<subclass object>` parametresine `<subclass>` parametresindeki subclass'dan türetilen instance tanımlanır. Static methodların scope'undaki local variable'lara ulaşabilmek için bu variable'ları `return` keyword'ü ile döndürmek gerekir. Çünkü bu local variable'lar, instance ve class methodlardaki instance ve class attribute'lar gibi bellekten silinmez, static method sonlanınca bellekten silinir. Örnek:
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

Instance, class ve static methodlarda inheritance işlemi yaparken kullanılan `super()` fonksiyonunun ilk parametresi olan `<subclass object>` parametresine girilen argüman, `<subclass>` parametresine girilen subclass'dan türetilen instnace olduğunda Python istenmeyen davranışlar sergiler. Örnek:
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
Gördüğünüz gibi `self` ve `cls` yerine `Class2()`/`Class3()` kullanılan `<subclass object>` parametreleri, `Class1` base class'ındaki `__init__`'in tekrar çalışmasına sebep oldu. Bunun sebebi; örneğin Python `super(Class3, Class3()).static_method()` kodunu okurken `Class3()` kısmını okuduktan sonra bu kodu çalıştırıp `Class3` class'ından bir instance türetmesi sonucu, `Class3` subclass'ı miras aldığı `Class1` deki `__init__` fonksiyonunu çalıştırdı. `__init__` çalışınca da dolayısıyla `print("...İnit Çalıştı...", end=" | ")` çalıştı ve `...İnit Çalıştı... |` yazdırıldı. Bu sorunu, instance ve class methodlarda kullanılan `super()` fonksiyonunun `<subclass object>` parametresinde `self` ve `cls` isimlerini (identifier) kullanarak, static methodlarda da daha önce de anlattığımız gibi `super()` fonksiyonu yerine eski inheritance yöntemini olan `Class1.static_method()` kodunu kullanabilirsiniz.

**Not:** Yukarıdaki örnekte `Class2` subclass'ının `instance_method` ve `class_method` method'larında tanımlı super class'larını parametreli ve parametresiz kullanmak arasında hiçbir fark yoktur. Burada şunu çıkarabiliriz; Python, instance ve class methodlarda kullanılan `super()` fonksiyonun parametrelerine doğru argümanları otomatik atar. Yani `super(<subclass>, self)` ve `super(<subclass>, cls)` ile `super()` arasında hiçbir fark yoktur.

**Not:** Genelde parametresiz super() kullanımı tavsiye edilir. Eğer parametresiz kulanamıyorsanız, programınızda büyük tasarım hataları var demektir.

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
Yıkarıdaki kodda, `var.instance_method()` kodundaki `instance_method` methodunun parantez içine `self` yazmadığımız gibi, `Class2` subclass'ının `class_method` methodunu `Class2.class_method()` şeklinde çağırırken parantez içine `cls` yazmayız (nedenini daha önce anlattım). Bu yüzden `Class2` subclass'ının `class_method` methodunun bloğunda tanımlı `Class1.class_method()` kodunun parantezlerinde `cls` yazmıyor. Yani, bir instance üzerinden instance method çağırırken `self` parametresine argüman girmediğimiz gibi, bir class üzerinden class method çağırırken `cls` parametresine argüman girmeyiz.

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
Python'ın 3.x öncesi sürümlerinde, yeni tip class'larla birlikte gelen bazı özellikler vardı (Örneğin `@property` decorator'u). Bir class'da yeni tip özellikleri kullanmak istediğinizde, bu class'ın `object` adındaki class'ından miras alması gerekiyordu. Eski tip class'lar `object` class'ından miras almadıkları için bu yeni tip özellikleri kullanamıyorlardı. Python 3'den sonra, bütün class'lar yeni tip class olarak güncellenmiştir. Bu yüzden Python 3'den sonra bir class, `object` class'ından miras alsa da almasa da yeni tip özellikleri kullanabilir. Yani Python 3'den sonra aşağıdaki class tanımlamaları arasında hiçbir fark yoktur:
```py
class Sınıf:
    pass

class Sınıf():
    pass

class Sınıf(object):
    pass
```

# Multiple Inheritance (Çoklu Miras Alma)
**Başlamadan önce oku:** Burada bahsedilen MRO, `__mro__`, `mro()` gibi kavramların ne olduğu daha sonra MRO (Method Resolution Order) başlığında açıklanacak.

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

Python, bir subclass'ın miras aldığı base class'larda aynı isme (identifier) sahip fonksiyonlar varsa, bu subclass'ın MRO'sunda belirtilen sıraya göre öncelik verip diğer base class'lardaki aynı isme (identifier) sahip methodları görmezden gelir. Bu subclass'ın MRO sırasına ulaşmak için `print(subclass.__mro__)` veya `print(subclass.mro())` kodlarını kullanabilirsiniz. Örnek:
```py
class A():
    def a(self):
        print("Class A")

class B():
    def a(self):
        print("Class B")

class C():
    def a(self):
        print("Class C")

class D(A, B, C):
    pass

var = D()
print(D.__mro__) # Output: (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)
print(D.mro()) # Output: [<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
var.a() # Output: Class A
```
`D` subclass'ının MRO'su `D -> A -> B -> C -> object` şeklindedir. Bu yüzden `D` subclass'ı `a()` fonksiyonunu `A` base class'ından alıp diğer base class'lardaki `a()` methodlarını görmezden geldi.

Bu methodları MRO'dan sırasının herhangi bir yerinden çekip de kullanabilirsiniz. Örnek:
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
D class'ının MRO'su `D -> A -> B -> C -> object` şeklindedir.
- `super(D, self).print_msg()`'nin MRO'su `A -> B -> C -> object` şeklindedir. Bu yüzden `var1.print_msg()` kodu `Class A` output'unu verecekti.

- `super(A, self).print_msg()`'nin MRO'su `B -> C -> object` şeklindedir. Bu yüzden `var1.print_msg()` kodu `Class B` output'unu verecekti.

- `super(B, self).print_msg()`'nin MRO'su `C -> object` şeklindedir. Bu yüzden `var1.print_msg()` kodu `Class C` output'unu verecekti.

- Eğer `super(C, self).print_msg()` olsaydı, MRO'su `object` şeklinde olacaktı. `object` class'ında `print_msg` adında bir fonksiyon olmadığı için `AttributeError: 'super' object has no attribute 'print_msg'` hatası yükseltilecekti.

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
        super(E, self).print_msg() # Output: Class A
        super(A, self).print_msg() # Output: Class B
        super(B, self).print_msg() # Output: Class C
        super(D, D()).print_msg() # Output: Class C

var = E()
print(E.__mro__) # Output: (<class '__main__.E'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)
print(D.__mro__) # Output: (<class '__main__.D'>, <class '__main__.C'>, <class 'object'>)
var.print_msg()
```
Gördüğünüz gibi `E` subclass'ı `D` subclass'ını referans almasa (parantezine yazılı olmasa) bile `super(D, D()).print_msg()` kodu çalıştı. Buradan da şu sonucu çıkarabiliriz; `super()` fonksiyonu, `<subclass object>` parametresinde tanımlı instance'ın türetildiği subclass'ın MRO'sunun dikkate alarak, bu MRO'nun `<subclass>` parametresinde tanımlı class'dan sonrasını miras alır. Yani `super(D, D()).print_msg()` kodundaki `super()` fonksiyonu, `<subclass object>` parametresinde belirtilen `D()` instance'ının türetildiği `D` subclass'ının MRO'sunu (`D -> C -> object`) dikkate alarak `<subclass>` parametresinde belirtilen `D` class'ından sonrasını (`C -> object`) miras alır. `print_msg` methodu `C -> object` sırasına göre ilk `C` class'ında bulunduğu için `super(D, D()).print_msg` kodu, `C` class'ının `print_msg` methodunun proxy objesini üretir ve `super(D, D()).print_msg()` kodu ile bu proxy objesi çağırılır (call).

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
        A.print_msg(self)
        B.print_msg(self)
        C.print_msg(self)
        D.print_msg(self)


var = E()
print(E.__mro__) # Output: (<class '__main__.E'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)
print(D.__mro__) # Output: (<class '__main__.D'>, <class '__main__.C'>, <class 'object'>)
var.print_msg()
```
**Not:** `D` subclass'ında `C.print_msg(self)` yerine `super(D, self).print_msg()` kullanırsanız, `super(D, self).print_msg()` kodundan dolayı Python `TypeError: super(type, obj): obj must be an instance or subtype of type` hatası yükseltir.








# MRO (Method Resolution Order)
Method resolution order (kısaca MRO), 'method çözümleme sırası' anlamına gelmektedir. MRO, **[directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)**'dan (kısaca DAG) türetilen, **[C3 linearization algorithm](https://en.wikipedia.org/wiki/C3_linearization)** tarafından oluşturulan **[total order](https://en.wikipedia.org/wiki/Total_order)**'dır.

Bir class'ın inheritance hierarchy'sini temsil eden, 'yönlendirilmiş döngüsel olmayan grafik' anlamına gelen bir graph'a **Directed Acyclic Graph (DAG)** denir. Kısacası class'ların inheritance konusunda birbirleriyle olan bağlantılarının gösterildiği grafiktir. Örnek:
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

Bu graph bize sadece hangi class'ın hangi class'dan miras aldığını söyler, MRO hakkında bir bilgi vermez.

Multiple inheritance söz konusu olduğunda,

**!Burada Kaldın!** soru sordun ve aldığın cevaba göre super'i baştan inşa edebilir ya da yeni bilfiler MRO ile ilgili olduğu için basitçe bu başlıkta açıklayabilirsin.

https://gist.github.com/e-k-eyupoglu/bf5f05487e0b8d820031ab5c71ef194e

multi inheritance'i MRO'nun üstüne yaz.





Tablonuz, "A"nın kalıtım hiyerarşisini temsil eden bir "yönlendirilmiş döngüsel olmayan grafiktir" (DAG). Bir DAG olarak, ilgili sınıfların kısmi bir sırasını ifade eder. Örneğin, "A", hem "B" hem de "C"den önce gelir, ancak grafik "B"nin "C"den veya "C"nin "B"den önce gelip gelmediği hakkında hiçbir şey söylemez. Aslında ikisi de doğru değil.

Bir sınıfın MRO'su, "C3 doğrusallaştırma algoritması" tarafından oluşturulan DAG'dan türetilen "toplam bir düzendir". Herhangi iki sınıf verildiğinde, iki basit kurala göre birinin diğerinden önce geldiğini söyleyebiliriz:
- Bir sınıf her zaman üst sınıflarından herhangi birinin önüne geçer
- Temel sınıfın sırasına saygı duyulur. (Örneğin, "A", "B" ve "C"den bu sırayla miras alır, bu nedenle "B", "C"den önce gelir.)

Bu nispeten basit örnekte, "toplam düzen" grafiğin yalnızca en-birinci çapraz geçişi gibi görünmektedir, ancak bu genel olarak doğru değildir. Grafiğin kendisi "D", "E" ve "F" için özel bir "yatay" sıralama dayatmaz; sadece MRO'ya karşılık gelecek şekilde çizilmiştir.

super fonksiyonunun 2. parametresi mro ile ilgilidir. multi inhert'den örnek ver, simple örnek ver.

bir multi inherit iinde birden fazla super kullanabiliyoruz okey de bunu sadece subclass'ın miras aldığı class'lar üzerinde mi yapabiliyoruz araştır.







**!Burada Kaldın!** **(En son)**
- MRO'u bir başlıkta açıklayacaksın. Burada MRO'yu, `super()`'i ve inheritance'nin nasıl çalıştığını açıklayacaksın.
- Kare küp dikdörtgen örneğini MRO başlığı altında açıklayabilirsin.
- En baştan okuyup Aşağıdakileri bir yere sıkıştır gerekliyse.

**Not:** `super()` fonksiyonunu kullanırken `RuntimeError: super(): no arguments` hatası alıyorsanız, büyük ihtimal ya bir instance veya class method'a `self` veya `cls` parametresi eklemeyi unuttunuz ya da `super()` fonksiyonunun parametrelerine yanlış argümanlar girdiniz.

**Not:** `<subclass object>` parametresinin ne olduğunu ve nasıl kullanıldığını anlamadıysanız, OOP konusunun en başında `self` ve `cls`'nin ne olduğunu anlattığım kısımları okuyup sonra bu kısmı tekrardan okuyunuz.