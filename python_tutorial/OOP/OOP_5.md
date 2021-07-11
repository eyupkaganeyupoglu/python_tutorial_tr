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

Inheritance (Miras Alma) işleminde subclass, base class'ın method ve class attribute'larının kopyasını kendi class objesinde oluşturmaz, base class'daki method ve class attribute'lara referans verir. Örnek:
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

Gördüğünüz gibi `Class2` subclass'ındaki instance method objesinde `function Class1.func1` yazmaktadır. Buradaki `Class1.func1` ifadesi, `func1` fonksiyonunun `Class1`'in instance method objesi olduğunu söylemektedir. Yani `Class2` subclass'ındaki `func1` objesi, `Class1` base class'ındaki `func1` objesine referanstır. Referans durumu söz konusu olduğu için base class'da bir değişiklik yapıldığında bundan subclass'da etkilenir. Örneğin Yukarıdaki koda `Class1.cs1 = "Yeni Class Attribute 1"` kodunu ekleyip çalıştırırsak, hem `Class1` base class'ının hem de `Class2` subclass'ının `cs1` class attribute'unun değeri değişir. Kanıtı:

<img src="https://i.ibb.co/CwZGwxM/image.png" alt="image" border="0">

**Not:** En başta `Class1` ve `Class2` birbirinden üstün olmamasına rağmen, inheritance (miras alma) işleminden sonra `Class2` class'ının subclass rütbesine düştüğünü, `Class1` class'ının da base class rütbesine yükseldiğini söyleyebiliriz. Tabi bu, lafta böyle. Python bunları base class ya da subclass olarak değerlendirmez. `Class2` class'ı, `Class1` class'ından miras almış subclass olarak değerlendirir.

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

#### `super()` Fonksiyonu
`super()` build-in fonksiyonu, base class'ın methodlarına erişmemizi sağlayan bir proxy objesi (base class'ın geçici (temporary) objesi) döndürür. Bu sayede subclass methodlarının içeriğini değiştirirken, override sorununun yolumuza çıkmasını engellemiş oluyoruz. Örnek:
```py
class Class1():
    def __init__(self, p1, p2, p3):
        print("init çalıştı...")
        self.a = p1
        self.b = p2
        self.c = p3

class Class2(Class1):
    def __init__(self, p4):
        super().__init__(p4, p4, p4)
        self.d = p4

var1 = Class1(1,2) # Output: init çalıştı...
var2 = Class2(1,2) # Output: init çalıştı...
print(var1.a) # Output: 1
print(var1.b) # Output: 2
print(var1.c) # Output: 3
print(var2.a) # Output: 4
print(var2.b) # Output: 4
print(var2.c) # Output: 4
```
Gördüğünüz gibi  `Class2` subclass'ından türetilmiş `var2` instance'sini kullanarak, `Class2` subclass'ının `__init__` methoduna elle tanımlamadığımız instance attribute'lara bile erişebiliyoruz. Bunu, `super()` build-in fonksiyonunun döndürdüğü proxy objesine borçluyuz. `super()` build-in fonksiyonu tanımlarken, `super().__init__(p4, p4, p4)` örneğindeki gibi erişmek istediğimiz methodun parametre sayısı (`self` ve `cls` parametreleri hariç), base class'daki halinin parametre sayısı ile uyuşmalıdır (içerik `p4, p4, p4`'de olduğu gibi, kodunuza göre değişkenlik gösterir).

`super()` build-in fonksiyonu instance ve class methodlarda da kullanabiliriz. Örnek:
```py
class Class1():
    class_attribute = "Class1'in Class Attribute'u"

    def instance_method(self):
        self.instance_attribute = "Class1'in Instance Attribute'u"
        print("Class1'in instance_method'u çalıştı:", end=" ")

    @classmethod
    def class_method(cls):
        cls.class_attribute
        print("Class1'in static_method'u çalıştı:", end=" ")

class Class2(Class1):

    def instance_method(self):
        super().instance_method()
        print(self.instance_attribute)

    @classmethod
    def class_method(cls):
        super().class_method()
        print(cls.class_attribute)
        
var1 = Class1() # Output: init çalıştı...
var2 = Class2() # Output: init çalıştı...
var2.class_method() # Output: Class1'in static_method'u çalıştı: Class1'in Class Attribute'u
var2.instance_method() # Output: Class1'in instance_method'u çalıştı: Class1'in Instance Attribute'u
```
**Not:** **!Burada Kaldın!** staticmethod'larda neden super() kullanamadığını araştırıyordun. Python türkiyeye soru sordun.
https://stackoverflow.com/questions/53508770/python-3-error-runtimeerror-super-no-arguments/53509145
https://docs.quantifiedcode.com/python-anti-patterns/correctness/missing_argument_to_super.html
https://www.programiz.com/python-programming/inheritance
https://docs.python.org/3/library/functions.html (Bu issubclass ve isinstance build-in için)
