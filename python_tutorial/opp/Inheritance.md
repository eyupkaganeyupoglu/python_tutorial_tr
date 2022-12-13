# İçindekiler

- [Inheritance (Miras Alma)](#1)
    - [Object Class](#1.1)
    - [Types of Inheritance (Miras Alma Türleri)](#1.2)
        - [Her şeyi miras almak](#1.2.1)
        - [Miras alınan objeyi geçersiz kılmak (override)](#1.2.2) 
        - [Objeyi geçersiz kılmadan (override) miras almak](#1.2.3)
- [Multiple Inheritance (Çoklu Miras Alma)](#2)
- [`super(subclass, subclass_object)` Fonksiyonu](#3)

<h1 id="1">Inheritance (Miras Alma)</h1>

Bir class'ın, başka bir class'ın bütün objelerine (method, class attribute, property vs.) sahip olması için yapılan işleme **Inheritance** (Miras Alma) denir. Inheritance (Miras Alma), aynı kodları her class'a tekrar tekrar yazma zahmetinden bizi kurtarır. Miras veren class parent class, super class, base class olarak isimlendirilir. Miras alan class child class, derived class, subclass olarak isimlendirilir. Ben tutorial boyunca **base class** ve **subclass** isimlendirmelerini kullanacağım. Örnek:
```py
class A:
    pass

class B(A):
    pass
```
Burada `B` class'ı, `A` class'ından miras almıştır. Yani class'ların yanındaki parantezler inheritance işleminde anlam kazanıyor. Bu parantezin içine yazdığınız class base class'dır

Inheritance işleminde subclass base class'daki objeleri miras alması demek, base class'daki objeleri kopyalaması demek değildir. Subclass, base class'dan miras aldığı objelere atıfta bulunur (yani aynı objelerdir). Bu yüzden base class'da yapılan değişiklikler subclass'ı da etkiler. Örnek:
```py
class A:
    class_exp1 = []
    class_exp2 = "1. object"

    def func():
        pass

class B(A):
    pass

print(B.func) # Output: <function A.func at 0x000001B3CEAE5040>
print(A.func) # Output: <function A.func at 0x000001B3CEAE5040>

print(A.class_exp1) # Output: []
print(B.class_exp1) # Output: []
A.class_exp1.append("Item 1")
print(A.class_exp1) # Output: ['Item 1']
print(B.class_exp1) # Output: ['Item 1']
B.class_exp1.append("Item 2")
print(A.class_exp1) # Output: ['Item 1', 'Item 2']
print(B.class_exp1) # Output: ['Item 1', 'Item 2']

print(A.class_exp2) # Output: 1. object
print(B.class_exp2) # Output: 1. object
A.class_exp2 = "2. object"
print(A.class_exp2) # Output: 2. object
print(B.class_exp2) # Output: 2. object
B.class_exp2 = "3. object"
print(A.class_exp2) # Output: 2. object
print(B.class_exp2) # Output: 3. object
```
`B` class'ındaki objelerin `A` class'ındaki objelere atıfta bulunmasının (refers to) kanıtı:
```py
class A:
    class_exp1 = []
    class_exp2 = "First object"

    def func1(self):
        pass

    @classmethod
    def func2(cls):
        pass

    @staticmethod
    def func3():
        pass

    property_exp = property()

class B(A):
    pass

print(A.class_exp1==B.class_exp1) # Output: True
print(A.class_exp2==B.class_exp2) # Output: True
print(A.func1==B.func1) # Output: True
print(A.func2==B.func2) # Output: False
print(A.func3==B.func3) # Output: True
print(A.property_exp==B.property_exp) # Output: True
```
`A.func2==B.func2` `False` olmasına aldanmayın, ikisi de `A.func2` objesi. Sadece `<class '__main__.B'>` kısmı farklı diye `False` sonucunu döndürüyor. Kanıtı:

![](./pics/5.png)

`__dict__` methodu, bulunduğu objenin içerdiği kendisine ait objelerin bulunduğu bir dictionary objesidir demiştik. Yukarıdaki durumu daha iyi anlamak için `B` class'ının `__dict__` methoduna bakmanız yeterli:
```py
print({(i):(A.__dict__[i]) for i in A.__dict__ if not "__" in i}) # Output: {'class_exp1': [], 'class_exp2': 'First object', 'func1': <function A.func1 at 0x00000203562060D0>, 'func2': <classmethod object at 0x0000020356204FD0>, 'func3': <staticmethod object at 0x0000020356204FA0>, 'property_exp': <property object at 0x00000203561F5E50>}
print({(i):(B.__dict__[i]) for i in B.__dict__ if not "__" in i}) # Output: {}
```
Gördüğünüz gibi `B` class'ının `A` class'ından miras aldığı objeler `B` class'ını `__dict__` methodunda bulunmuyor. Bu durum, `A` class'ındaki objelerin `B` class'ına kopyalanmadığını, `B` class'ındaki objelerin `A` class'ındaki objelere atıfta bulunduğunu (refers to) kanıtlar.

**Not:** Bir class'ın base class ya da subclass olarak isimlendirilmesi programcıların kendi arasında iletişim kurabilmesi için uydurulmuş sembolik bir şeydir. Python için bu durum "`A` base class, `B` subclass." olarak değil "`B` class'ı `A` class'ından miras almış." şeklinde yorumlanır.

<h2 id="1.1">Object Class</h2>

Class'lar, Python'ın 3.x öncesi sürümlerinde **yeni tip class'lar** ve **eski tip class'lar** olmak üzere ikiye ayrılıyordu. Eski tip class'lara örnek:
```py
class A():
    pass

class B(A):
    pass
```
Yeni tip class'lara örnek:
```py
class A(object):
    pass

class B(A):
    pass
```
Python'ın 3.x öncesi sürümlerinde, yeni tip class'larla birlikte gelen bazı özellikler vardı (Örneğin `@property` decorator'u). Python'ın 3.x öncesi sürümlerinde bir class'ın yeni tip özellikleri kullanabilmesi için `object` adındaki class'ından miras alması gerekiyordu. Bu yüzden `object` adındaki class'ından miras alan class'lara **yeni tip**, almayan class'lara da **eski tip** class dendi. Python 3'den sonra Python kaynak dosyalarındaki bütün class'lar yeni tip class olarak güncellenmiştir. Bu sayede herhangi bir class'da yeni özellikleri kullanabilmek için elle `object` base class'ını miras almasını sağlamamız gerekmiyor. Yani Python 3'den sonra aşağıdaki class tanımlamaları arasında hiçbir fark yoktur:
```py
class A:
    pass

class A():
    pass

class A(object):
    pass
```

<h2 id="1.2">Types of Inheritance (Miras Alma Türleri)</h2>

Inheritance (Miras Alma)'nın çeşitleri vardır:
- Her şeyi miras almak
- Miras alınan objeyi geçersiz kılmak (override)
- Objeyi geçersiz kılmadan (override) miras almak

<h3 id="1.2.1">Her şeyi miras almak</h3>

Bir class'ın, başka bir class'ın bütün objelerini olduğu gibi miras almasına denir. Örnek:
```py
class A():
    class_attri = "Class Attribute"

    def __init__(self):
        print("init çalıştı...")
        self.instance_attri = "Instance Attribute"

    def func1(self):
        print("func1 Çalıştı...")
        

    @classmethod
    def func2(cls):
        print("func2 Çalıştı...")

    @staticmethod
    def func3():
        print("func3 Çalıştı...")

    property_exp = property(fget=lambda temp="Property objesi çalıştı." : temp)

class B(A):
    pass

var = B() # Output: init çalıştı...
print(var.class_attri) # Output: Class Attribute
print(var.instance_attri) # Output: Instance Attribute
print(var.property_exp) # Output: Property objesi çalıştı.
var.func1() # Output: func1 Çalıştı...
var.func2() # Output: func2 Çalıştı...
var.func3() # Output: func3 Çalıştı...
```
Gördüğünüz gibi `B` class'ı `A` class'ının bütün objelerini olduğu gibi miras aldı.

**Not:** Bir subclass, bir base class'ın her şeyini miras alacaksa, `class` statement ile bir subclass tanımlamak yerine basitçe `subclass = base_class()` gibi bir instantiation işlemi ile de işinizi halledebilirsiniz (ben tercih etmiyorum). Örnek:
```py
class A:
    pass

B = A()
C = B() # TypeError: 'A' object is not callable
```
Bu durumda `B` class'ı bir instance olacağı için tekrardan instantiation işlemi yapamazsınız çünkü instance'lar, class'lar gibi çağırılabilir objeler değillerdir.

<h3 id="1.2.2">Miras alınan objeyi geçersiz kılmak (override)</h3>

Subclass ile base class'ın objeleri birbiri ile çakışıyorsa (yani iki class'da da aynı isimde (identifier) objeler varsa), subclass'da tanımlı obje, base class'dan miras alınan objeyi geçersiz kılar (override). Örnek:
```py
class A:
    def func(self):
        pass

class B(A):
    pass

class C(A):
    def func(self):
        pass

print(A.func==B.func) # Output: True
print(A.func==C.func) # Output: False
print(B.func==C.func) # Output: False
```

<h3 id="1.2.3">Objeyi geçersiz kılmadan (override) miras almak</h3>

Base class'dan miras alınan objeler geçersiz kılınmadan (override) içeriği değiştirilmek istenilirse `super()` build-in fonksiyonunu (daha sonra anlatılacak) veya eski inheritance yöntemini (daha sonra anlatılacak) kullanabilirsiniz.

<h1 id="2">Multiple Inheritance (Çoklu Miras Alma)</h1>

Bir class'ın, birden fazla class'dan miras almasına **Multiple Inheritance (Çoklu Miras Alma)** denir. Örnek:
```py
class A():
    def func1(self):
        print("func1 çalıştı...")

class B():
    def func2(self):
        print("func2 çalıştı...")

class C():
    def func3(self):
        print("func3 çalıştı...")

class D(A,B,C):
    pass

var = D()
var.func1() # Output: func1 çalıştı...
var.func2() # Output: func2 çalıştı...
var.func3() # Output: func3 çalıştı...
```
Buradaki `D` subclass'ı sırasıyla `C`, `B` ve `A` class'larından miras almıştır. Çoklu miras alma işlemi, ilgili class'ın MRO'suna göre yapılır. **Method resolution order** (kısaca **MRO**), "method çözümleme sırası" anlamına gelmektedir. MRO, [**directed acyclic graph**](https://en.wikipedia.org/wiki/Directed_acyclic_graph "https://en.wikipedia.org/wiki/Directed_acyclic_graph")'dan (kısaca DAG) türetilen, [**C3 linearization algorithm**](https://en.wikipedia.org/wiki/C3_linearization "https://en.wikipedia.org/wiki/C3_linearization") tarafından oluşturulan [**total order**](https://en.wikipedia.org/wiki/Total_order "https://en.wikipedia.org/wiki/Total_order")'dır.

Bir class'ın inheritance hierarchy'sini (miras almanın önem sırası) temsil eden, "yönlendirilmiş döngüsel olmayan grafik" anlamına gelen graph'a (graph'ın ne olduğunu bilmiyorsanız araştırın) **Directed Acyclic Graph (DAG)** denir. Kısacası class'ların inheritance konusunda birbirleriyle olan bağlantılarının gösterildiği grafiktir. Örnek:
```py
O = object
class F(O): pass
class E(O): pass
class D(O): pass
class C(D,F): pass
class B(E,D): pass
class A(B,C): pass
```

![](./pics/6.png)

Bu graph bize sadece hangi class'ın hangi class'dan miras aldığını söyler, single ya da multiple inheritance'ın MRO'su hakkında bir bilgi vermez.

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

**Not:** MRO sadece class'larda bulunan bir şey'dir. Instance'larda bulunmaz ama instance'ın `__class__` methodu üzerinden `var.__class__.__mro__` şeklinde, bu instance'ın türetildiği class'ın MRO'suna erişilebilir.

**Not:** MRO'yu anlamak için inheritance bilgisi, inheritance'ı anlamak için de MRO bilgisi gerekmektedir. MRO'yu hala anlamadıysanız, verdiğim linklerden de yararlanarak kendi başınıza MRO'nun ne olduğunu öğreniniz. MRO hakkında daha fazla bilgi için:
- [**Python history blogspot**](https://python-history.blogspot.com/2010/06/method-resolution-order.html "https://python-history.blogspot.com/2010/06/method-resolution-order.html")
- [**Stackoverflow**](https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance "https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance")

Multiple inheritance'ın MRO'su 2 kurala göre belirlenir:
1. Subclass her zaman ilk sıradadır.
2. Subclass'ın miras aldığı base class'ların subclass'a tanımlanma sırasına saygı gösterilir. (örneğin `class A(B, C)`'de `B`, `C`'den önce gelir.) Bu yüzden bir class'ın miras aldığı class'larda aynı isme (identifier) sahip objeler varsa, bu class kendi MRO'sundaki (kendisi hariç) soldan ilk sırada bulunan class'a öncelik verir. Örnek:
    ```py
    class A():
        def func(self):
            print("Class A")

    class B():
        def func(self):
            print("Class B")

    class C():
        def func(self):
            print("Class C")

    class D(A, B, C):
        pass

    var = D()
    print(D.__mro__) # Output: (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)
    var.func() # Output: Class A
    ```
    `D` class'ının MRO'su `D -> A -> B -> C -> object` şeklindedir. `D` class'ı `func()` methodunu, `D` class'ının MRO'suna göre öncelikli olan `D` class'ında arar ama bulamadığı için `A` class'ına bakar ve bulduğu için miras alıp diğer class'lardaki `func()` methodlarını görmezden gelir. Eğer `A` class'ında `func()` methodu olmasaydı, `D` class'ı bu methodu bulana kadar kendi MRO'sunda soldan sağa doğru bütün class'lara bakacaktı. Eğer `D` class'ının MRO'sunda belirtilen class'ların hiçbirinde `func()` methodu bulunamazsaydı, `AttributeError: 'D' object has no attribute 'func'` hatası yükseltilirdi.

**Not:** Multiple inheritance yaparken, miras alınan class'ları doğru sıra ile subclass'a girmek önemlidir. Örnek:
```py
O = object
class A(O): pass
class B(A): pass
class C(B,A): pass
class D(A,B): pass # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B
```
`B` class'ı `A`'dan miras aldığı için MRO sırasında `B` `A`'dan önce olmak zorundadır. `D` class'ının MRO'su bunu ihlal etmektedir. Olması gereken `D -> B -> A -> object` şeklindeyken, `D -> A -> B -> object` istendiği için hata yükseltilmiştir. Yani miras alınan class'ların MRO'suna saygı göstermek zorundasınız.

<h1 id="3"><code>super(subclass, subclass_object)</code> Fonksiyonu</h1>

`super()` fonksiyonunu anlayabilmeniz açısından bolca olası senaryo örneği vererek anlattım. Bu yüzden `super()` fonksiyonunu ilk seferde anlayamadıysanız, bu başlığı tekrar tarar okumanızı tavsiye ederim. Hala anlamadıysanız kendiniz farklı kaynaklardan araştırabilirsiniz.

`super()` build-in fonksiyonu, MRO'ya (Method Resolution Order) göre çalışan bir mekanizmaya dayanır. `super()` build-in fonksiyonu, istediğimiz class'ın proxy objesini (geçici (temporary) obje) oluşturmamızı ve bu proxy objeleri üzerinden base class'ın objelerine ulaşmamızı sağlar. Bu sayede base class'ın bütün objelerini miras almadan istediğimiz objeleri miras alabiliriz veya miras aldığımız objeyi geçersiz kılmadan (override) içeriği ile oynayarak ihtiyaca göre işlevselliğini değiştirebiliriz. Örnek:
```py
class A():
    def __init__(self):
        print("init çalıştı...")
        self.attri_1 = 0

    def func(self):
        pass

class B(A):
    def __init__(self):
        super().__init__()
        self.attri_2 = self.attri_1 + 1
        self.func()

    def func(self):
        self.proxy_exp = super(B, self)

var1 = A()
var2 = B()
print(var1.attri_1) # Output: 0
print(var2.attri_1) # Output: 0
print(var2.attri_2) # Output: 1
print(var2.proxy_exp) # Output: <super: <class 'B'>, <B object>>
```
Gördüğünüz gibi `super()` fonksiyonunun oluşturduğu `A` class'ının proxy objesi üzerinden `__init__` fonksiyonunu çağırarak `A` class'ının instance methodlarını elde etmiş olduk. Başka bir örnek:
```py
class A():
    def __init__(self, p1, p2, p3):
        self.attri_1 = p1 + p2 + p3

class B(A):
    def __init__(self, p4, p1, p2, p3):
        super().__init__(p1, p2, p3)
        self.attri_2 = self.attri_1 + p4 

class C(A):
    def __init__(self, p4, *args):
        super().__init__(*args)
        self.attri_2 = self.attri_1 + p4 

var1 = A(1,2,3)
var2 = B(4,1,2,3)
var3 = C(4,1,2,3)
print(var1.attri_1) # Output: 6
print(var2.attri_1) # Output: 6
print(var2.attri_2) # Output: 10
print(var3.attri_1) # Output: 6
print(var3.attri_2) # Output: 10
```
`super().__init__(p1, p2, p3)` kodundaki `__init__` methoduna girdiğiniz `p1`, `p2` ve `p3` değerleri parametre değil argümandır çünkü `super()` fonksiyonunun oluşturduğu proxy objesi üzerinden `__init__` methodunu çağırıyorsunuz. Bu argümanları `def __init__(self, p4, p1, p2, p3)` kısmından elde ediyoruz. Birden fazla parametre tanımlamanız gerektiği zaman yukarıdaki gibi `*args` (`p1 = "Falan Filan"` gibi default value'ya sahip parametreler varsa `*args` yerine `**kwargs`) yıldızlı parametresini kullanabilirsiniz.

`super()` fonksiyonu ile base class'ın bütün objelerini (method, attribute, property vs.) teker teker miras alabileceğimizi söylemiştim. Tek yapmanız gereken `super()` fonksiyonunun üzerinden ilgili objeyi, subclass içinde doğru scope'da çağırmak. Örnek:
```py
class A:
    class_attri = "Class Attribute"

    def __init__(self):
        self.instance_attri = "Instance Attribute"

    def func1(self):
        return "func1 instance method"

    @classmethod
    def func2(cls):
        return "func2 class method"

    @staticmethod
    def func3():
        return "func3 static method"

    property_exp = property(fget=lambda p1 : "property_exp objesi")

class B(A):

    def __init__(self):
        super().__init__()
        self.instance_attri_2 = self.instance_attri

    def func1(self):
        print(super().func1())

    @classmethod
    def func2(cls):
        print(super().func2())

    @staticmethod
    def func3():
        print(super(B,B()).func3())

var1 = A()
var2 = B()
var2.func1() # Output: func1 instance method
var2.func2() # Output: func2 class method
var2.func3() # Output: func3 static method
print({(i):(A.__dict__[i]) for i in A.__dict__ if not "__" in i}) # Output: {'class_attri': 'Class Attribute', 'func1': <function A.func1 at 0x0000018768EF8160>, 'func2': <classmethod object at 0x0000018768EF4FD0>, 'func3': <staticmethod object at 0x0000018768EF4FA0>, 'property_exp': <property object at 0x0000018768EE5AE0>}
print({(i):(B.__dict__[i]) for i in B.__dict__ if not "__" in i}) # Output: {'func1': <function B.func1 at 0x0000018768EF8430>, 'func2': <classmethod object at 0x0000018768EF4EE0>, 'func3': <staticmethod object at 0x0000018768EF47F0>}
```
Class'ların `__dict__` methodlarının listesi:
|  | func1 | func2 | func3 | class_attri | property_exp |
|-|-|-|-|-|-|
| Class A | <function A.func1 at 0x0000018768EF8160> | <classmethod object at 0x0000018768EF4FD0> | <staticmethod object at 0x0000018768EF4FA0> | 'Class Attribute' | <property object at 0x0000018768EE5AE0> |
| Class B | <function B.func1 at 0x0000018768EF8430> | <classmethod object at 0x0000018768EF4EE0> | <staticmethod object at 0x0000018768EF47F0> |  |  |

Gördüğünüz gibi `func1`, `func2` ve `func3` geçersiz kılındı (overrite) ama miras aldığı class'daki `func1`, `func2` ve `func3` methodlarının işlevlerine sahipler.

`super()` fonksiyonu Python'a sonradan eklenmiştir. `super()` fonksiyonu eklenmeden önce inheritance işlemi için doğrudan base class kullanılıyordu. Buna eski inheritance yöntemi denir. Örnek:
```py
class A:
    class_attri = "Class Attribute"

    def __init__(self):
        self.instance_attri = "Instance Attribute"

    def func1(self):
        return "func1 instance method"

    @classmethod
    def func2(cls):
        return "func2 class method"

    @staticmethod
    def func3():
        return "func3 static method"

    property_exp = property(fget=lambda p1 : "property_exp objesi")

class B(A):

    def __init__(self):
        super().__init__()
        self.instance_attri_2 = self.instance_attri

    def func1(self):
        print(super().func1())

    @classmethod
    def func2(cls):
        print(super().func2())

    @staticmethod
    def func3():
        print(super(B,B()).func3())

class C(A):

    def __init__(self):
        A.__init__(self)
        self.instance_attri_2 = self.instance_attri

    def func1(self):
        print(A.func1(self))

    @classmethod
    def func2(cls):
        print(A.func2())

    @staticmethod
    def func3():
        print(A.func3())

var1 = A()
var2 = B()
var3 = C()
var2.func1() # Output: func1 instance method
var2.func2() # Output: func2 class method
var2.func3() # Output: func3 static method
var3.func1() # Output: func1 instance method
var3.func2() # Output: func2 class method
var3.func3() # Output: func3 static method
```
Burada, `A` class'ı üzerinden instance method çağırıken `self` parametresini tanımlamayı unutmamaya dikkat etmelisiniz. Aynı `cls` için geçerli değildir çünkü zaten main class üzerinden class method çağırıyorsunuz. Python `cls`'ye gerekli argümanı kendisi otomatik tanımlıyor. Eski inheritance yöntemi ile `super()` fonksiyonunun farkı hakkında bilgi için [tıklayınız](https://stackoverflow.com/a/33469090/15170972 "https://stackoverflow.com/a/33469090/15170972").

**Not:** Instance ve class method'larda inheritance işlemi yaparken kullandığımız `super()` fonksiyonunun parametrelerine argüman tanımlamadan da kullanabilirsiniz. Bu durum Python'ın, instance ve class methodlarda kullanılan `super()` fonksiyonunun parametrelerine doğru argümanları otomatik olarak girmesinden kaynaklanır. Bu yüzden özel durumlar dışında `super()` fonksiyonunun parametresiz kullanılması tavsiye edilir. Eğer parametresiz kulanamıyorsanız, programınızda büyük tasarımsal hatalar var demektir.

`super()` fonksiyonunun `t` ve `obj` olmak üzere 2 parametresi vardır. Bu parametrelere daha kolay anlaşılsın diye `subclass` (`t`) ve `subclass_object` (`obj`) diyeceğim:

**Subclass**: `subclass` parametresine argüman olarak sadece class (`A`, `B`, ... vb.) verilebilir.

**Subclass Object**: `subclass_object` parametresine argüman olarak subclass ya da instance verilebilir.

Bu iki parametre birbiri ile ilişkili bazı kurallara sahiptir:

`subclass_object` parametresine argüman olarak instance ya da subclass girilebilir demiştim. `subclass_object` parametresine argüman olarak girilen instance'ın türetildiği subclass'ın ya da direkt subclass'ın MRO'su, `subclass` parametresinde belirtilen class'ı içermelidir. Örneğin `subclass_object` parametresine argüman olarak girilen `D` subclass'ının MRO'su `D -> C -> B -> A -> object` şeklindeyse, `subclass` parametresine argüman olarak girilen class bu class'lardan birisi olmak zorundadır. Aksi halde, `TypeError: super(type, obj): obj must be an instance or subtype of type` hatası yükseltilir. Bu hata, "`super(type, obj)`: `obj` parametresine girilen şey, `type` parametresine girilen şeyin instance'ı ya da subclass'ı olmalıdır." anlamına gelmektedir.

`subclass_object` parametresine argüman olarak instance girilirse, `super()` fonksiyonunun oluşturduğu proxy objesi üzerinden çağırılacak instance ve class methodların `self`/`cls` olan ilk parametresine argüman olarak `self`/`cls` kelimelerini (veya ilgili methodun kapsamında bu identifier'lar yerine ne kullandıysanız onu) ya da instnace/class objesi girmek zorunda değiliz. Ama `subclass_object` parametresine argüman olarak subclass girilirse, `super()` fonksiyonunun oluşturduğu proxy objesi üzerinden çağırılacak instance methodların `self` olan ilk parametresine argüman olarak `self` kelimesini (veya ilgili methodun kapsamında bu identifier yerine ne kullandıysanız onu) ya da instnace girmek zorundayken, class methodların `cls` olan ilk parametresine argüman olarak `cls` (veya ilgili methodun kapsamında bu identifier yerine ne kullandıysanız onu) ya da class objesi girmek zorunda değilsiniz. Static methodlarda ilk parametre özel olmadığı için az önce anlattıklarımızla uğraşmanız gerekmez. Ama static methoda parametre olarak özellikle `self` veya `cls` tanımladıysanız, `subclass_object` parametresine argüman olarak instance da girseniz subclass da girseniz, `self` veya `cls` parametrelerine argüman girmek zorundasınız.

`super()` fonksiyonu, `subclass_object` parametresine argüman olarak girilen instance'ın türetildiği subclass'ın ya da subclass'ın MRO'suna göre, `subclass` parametresine argüman olarak girilen class'dan bir sonraki class'ı miras alır. O class'da istenilen objeyi bulamazsa bir sonrakine geçer. Örnek:
```py
class A:
    def func(self):
        print("1")

class B:
    def func(self):
        print("2")

class C(B):
    pass

class D(C,A,B):
    def func(self):
        super(D,self).func()

var = D()
print(D.__mro__) # D -> C -> A -> B -> object
var.func() # Output: 1
```
Gördüğünüz gibi `D` class'ındaki `super()` fonksiyonu, `subclass_object` parametresinde belirtilen instance'ın türetildiği class olan `D` class'ının MRO'suna göre, `subclass` parametresinde belirtilen class'dan sonraki class olan `C` class'ına baktı ama orada `func` methodunu bulamadığı için bir sonraki class olan `A` class'ına baktı ve `func` methodunu bulduğu için miras aldı.

`subclass_object` parametresinde argüman olarak `self`/`cls` girmekle instnace/class objesi girmek arasında, programın işleyişine etki etme konusunda önemli farklar vardır. Örnek:
```py
class A():

    ################### 1 #####################

    class_attri = "Class Attribute"

    def __init__(self):
        self.instance_attri = "Instance Attribute"

    def func1(self):
        print("instance_attri:", end=" ")

    @classmethod
    def func2(cls):
        print("class_attri:", end=" ")

    ################### 2 #####################

    def func3(self):
        print("instance_attri:", end=" ")

    @classmethod
    def func4(cls):
        print("class_attri:", end=" ")

    ################### 3 #####################

    def func5(self):
        print("instance_attri:", end=" ")

    ################### 4 #####################

    def func6(self):
        print("instance_attri:", end=" ")

class B(A):

    ################### 1 #####################

    def func1(self):
        super(B, self).func1()
        print(self.instance_attri)

    @classmethod
    def func2(cls):
        super(B, cls).func2()
        print(cls.class_attri)

    ################### 2 #####################

    def func3(self):
        super(B, B()).func3()
        print(self.instance_attri)

    @classmethod
    def func4(cls):
        super(B, B()).func4()
        print(cls.class_attri)

    ################### 3 #####################

    def func5(self):
        super(B, B).func5(self)
        print(self.instance_attri)

    ################### 4 #####################

    def func6(self):
        super(B, B).func6(B())
        print(self.instance_attri)

var1 = B()
var1.func1() # Output: instance_attri: Instance Attribute
var1.func2() # Output: class_attri: Class Attribute
var1.func3() # Output: instance_attri: Instance Attribute
var1.func4() # Output: class_attri: Class Attribute
var1.func5() # Output: instance_attri: Instance Attribute
var1.func6() # Output: instance_attri: Instance Attribute
```
Gördüğünüz gibi bu kısımda `subclass_object` parametresinde argüman olarak `self`/`cls` ya da instnace/class objesi girmek arasında bir fark olmadı çünkü `instance_attri` ve `class_attri` attribute'ları `var1` instance'ı türetildiğinde zaten tanımlanmıştı. Bu yüzden `B` class'ındaki class ve instance methodlar, bu attribute'lara erişme konusunda sıkıntı yaşamadılar. Peki yaşasalardı? Örnek:
```py
class A():

    ################### 1 #####################

    class_attri = "Class Attribute"

    def __init__(self):
        pass

    def func1(self):
        self.instance_attri = "Instance Attribute"
        print("instance_attri:", end=" ")

    @classmethod
    def func2(cls):
        print("class_attri:", end=" ")

    ################### 2 #####################

    def func3(self):
        self.instance_attri = "Instance Attribute"
        print("instance_attri:", end=" ")

    @classmethod
    def func4(cls):
        print("class_attri:", end=" ")

    ################### 3 #####################

    def func5(self):
        self.instance_attri = "Instance Attribute"
        print("instance_attri:", end=" ")

    ################### 4 #####################

    def func6(self):
        self.instance_attri = "Instance Attribute"
        print("instance_attri:", end=" ")

class B(A):

    ################### 1 #####################

    def func1(self):
        super(B, self).func1()
        print(self.instance_attri)

    @classmethod
    def func2(cls):
        super(B, cls).func2()
        print(cls.class_attri)

    ################### 2 #####################

    def func3(self):
        super(B, B()).func3()
        print(self.instance_attri) # AttributeError: 'B' object has no attribute 'instance_attri'

    @classmethod
    def func4(cls):
        super(B, B()).func4()
        print(cls.class_attri)

    ################### 3 #####################

    def func5(self):
        super(B, B).func5(self)
        print(self.instance_attri)

    ################### 4 #####################

    def func6(self):
        super(B, B).func6(B())
        print(self.instance_attri) # AttributeError: 'B' object has no attribute 'instance_attri'

var1 = B()
var1.func1() # Output: instance_attri: Instance Attribute
var1.func2() # Output: class_attri: Class Attribute
var1.func3() # Error
var1.func4() # Output: class_attri: Class Attribute
var1.func5() # Output: instance_attri: Instance Attribute
var1.func6() # Error
```
Burada hata yükselten instance methodların `super()` fonksiyonuna argüman olarak `B()`, hata yükseltmeyen instance methodların `super()` fonksiyonuna argüman olarak `self` tanımlandığını görüyoruz. Bunun sebebi şudur:
- `super()` fonksiyonuna `B()` argümanını verirsek, `super(B, B())` fonksiyonu ürettiği proxy objesinin üzerinden çağırılan fonksiyonun etkileri `B()` koduyla türetilen instance'ı etkiler. `B()` koduyla türetilen instance `var1` instance'ından farklı bir obje olduğu için `var1` instance'ı, `super(B, B())` fonksiyonu ürettiği proxy objesi üzerinden çağırılan fonksiyonun etkilerinden etkilenmez. Bu yüzden `instance_attri` instance attribute'u `B()` instance'ında yaratılır (create) ama `var1` instance'ında yaratılmaz (create). `var1` instance'ında `instance_attri` instance attribute yaratılmadığı (create) için `print(self.instance_attri)` fonksiyonları yazdıracak bir `instance_attri` attribute bulamaz ve hata yükseltirler.
- `super()` fonksiyonuna `self` argümanını verirsek, `super(B, self)` fonksiyonu ürettiği proxy objesinin üzerinden çağırılan fonksiyonun etkileri `var1` instance'ını (yani doğru instance'ı) etkiler. Bu yüzden `print(self.instance_attri)` fonksiyonları yazdıracak bir `instance_attri` attribute'u bulabildikleri için hata yükseltmeden görevlerini yaparlar.

Böyle bir sorunla class methodlarda karşılaşmayız çünkü bir class'dan bir tane vardır, özeldir (special). Class'lar, instance'lar gibi sonsuz sayıda türetilemez. Bu yüzden ister class'ın ismini ister `cls` kullanın, ikisi de aynı class objesine atıfta bulunur (refers to).

**Not:** Yukarıda bahsettiğim sorunu basitçe `B()` yerine `self` kullanarak çözebilirsiniz. Instance attribute'u yarattırmak (create) için methoda `return` statement tanımlamak, methodu `__init__` methodunda çağırmak gibi çözüm arayışlarına girmeyin. Özellikle methodu `__init__` methodunda çağırmak gibi bir hata yaparsanız, terminaliniz yazılarla dolduktan sonra `RecursionError: maximum recursion depth exceeded while calling a Python object` hatası yükseltilir.

**Not:** Farketmediyseniz söyleyeyim. `super()` fonksiyonuna girdiğiniz `self`/`cls` argümanları, Python tarafından bu fonksiyonun tanımlı olduğu methodun parametresi olan `self`/`cls` parametrelerine otomatik olarak girilen argümandır. Yani bu parametrelerin isimlerini değiştirirseniz, `super()` fonksiyonundakileri de değiştirmeniz gerekmektedir.

Static method'larda olay bambaşkadır. Örnek:
```py
class A:
    @staticmethod
    def func():
        print("Static Method Çalıştı...")

class B(A):
    @staticmethod
    def func():
        super(B,B()).func()
        super(B,B).func()

var1 = B() # Output: Static Method Çalıştı...
var1.func() # Output: Static Method Çalıştı...
```
Static methodlara `self`/`cls` parametreleri tanımlamak zorunlu olmadığı için bu parametreleri tanımlamadığımızda, `subclass_object` parametresine argüman olarak `self` ya da `cls` giremeyiz ve mecburen instance ya da class objesi girmek zorunda kalırız. Peki bu parametreleri tanımlarsak? Örnek:
```py
class A:
    attri1 = "Class Attribute"
    def __init__(self):
        self.attri2 = "Instance Attribute"

    @staticmethod
    def foo(self, cls):
        self.attri2 = 2
        cls.attri1 = 1
        print(self.attri2, cls.attri1 sep=" | ")

class B(A):
    @staticmethod
    def func(self, cls):
        super(B,B()).foo(self, cls)

var = B()
print(var.attri2, var.attri1, sep=" | ") # Output: Instance Attribute | Class Attribute
var.foo(var,B) # Output: 2 | 1
print(var.attri2, var.attri1, sep=" | ") # Output: 2 | 1
```
Buradaki `super(B,B()).func(self, cls)` kodu ile aşağıdaki varyasyonları arasında hiçbir fark yoktur (`cls` ile `B` aynı şey olduğu için bu tarz varyasyonları boşuna yer kaplamasın diye dahil etmedim):
```py
super(B,B()).foo(self, cls)  # Output: 2 | 1 (attri1: 1, attri2: 2)
super(B,B()).foo(B(), cls)   # Output: 2 | 1 (attri1: 1, attri2: 2)
super(B,self).foo(self, cls) # Output: 2 | 1 (attri1: 1, attri2: 2)
super(B,self).foo(B(), cls)  # Output: 2 | 1 (attri1: 1, attri2: 2)
```
Ama `var.foo(var,B)` kodunu `var.foo(B(),B)` olarak değiştirirsek, bu varyasyonların davranışı değişir.
```py
super(B,B()).foo(self, cls)  # Output: 2 | 1 (attri1: 1, attri2: Instance Attribute)
super(B,B()).foo(B(), cls)   # Output: 2 | 1 (attri1: 1, attri2: Instance Attribute)
super(B,self).foo(self, cls) # Output: 2 | 1 (attri1: 1, attri2: Instance Attribute)
super(B,self).foo(B(), cls)  # Output: 2 | 1 (attri1: 1, attri2: Instance Attribute)
```
`B` class'ı her yerde `B` class'ı olduğu için hangi instance'da olduğu farketmeksizin `cls.attri1 = 1` statement bir kere okundu mu, `attri1` class attribute'unun value'su her yerde `1` olur. Ama daha önce de anlattığım gibi, her instance kendisine özel olduğu için `foo` static methodu, `var.foo(B(),B)` kodundaki `B()`'nin türettiği instance objesine etki ettiği için bu objedeki `attri2` instance methodunun value'su değişti ve `print()` fonksiyonu bu objedeki `attri2` instance methodunun value'sunun value'sunu yazdırdı. Bu yüzden `var` instance'ının `attri2` instance attribute'unun value'su değişmediği halde terminale `2 | 1` yazdırıldı.

**Not:** Static method'un kullanım amacı daha önce de anlattığım gibi "Bir methodun herhangi bir class veya instance attribute'a erişmesi gerekmiyorsa, bu method static method olarak tanımlanıp kullanılabilir." şeklindedir. Yukarıdaki bütün ayrıntıları, `super` fonksiyonunun mantığını anlamanız amacıyla anlattım. Siz bu kadar çok kurcalamayın, zaten ihtiyacınız da olmayacak.

**Not:** `B()` argümanı yeni bir instance türettiği için her seferinde `__init__` constructor'ını çalıştırır. Bu durum da istenmeyen sonuçlara neden olabilir. Örnek:
```py
class A:
    def __init__(self):
        print("init çalıştı...", end=" | ")

    def func1(self):
        print("func1 Çalıştı...")
    
    @classmethod
    def func2(cls):
        print("func2 Çalıştı...")

    @staticmethod
    def func3():
        print("func3 Çalıştı...")

class B(A):

    def func1(self):
        super(B,self).func1() # Output: func1 Çalıştı...
        super(B,B()).func1() # Output: init çalıştı... | func1 Çalıştı...

    @classmethod
    def func2(cls):
        super(B,B()).func2() # Output: init çalıştı... | func1 Çalıştı...

    @staticmethod
    def func3():
        super(B,B()).func3() # Output: init çalıştı... | func1 Çalıştı...

var = B() #Output: init çalıştı... | 
var.func1()
var.func2()
var.func3()
```
Bu sorunu çözmek için `super()` fonksiyonları yerine eski inheritance yöntemini kullanabilirsiniz. Örnek:
```py
class A:
    def __init__(self):
        print("init çalıştı...", end=" | ")

    def func1(self):
        print("func1 Çalıştı...")
    
    @classmethod
    def func2(cls):
        print("func2 Çalıştı...")

    @staticmethod
    def func3():
        print("func3 Çalıştı...")

class B(A):

    def func1(self):
        A.func1(self) # Output: func1 Çalıştı...
        A.func1(self) # Output: func1 Çalıştı...

    @classmethod
    def func2(cls):
        A.func2() # Output: func1 Çalıştı...

    @staticmethod
    def func3():
        A.func3() # Output: func1 Çalıştı...

var = B() #Output: init çalıştı... | 
var.func1()
var.func2()
var.func3()
```

Multiple inheritance'da MRO sırasından bağımsız olarak da miras alma işlemi yapabilirsiniz. Örnek:
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
        super(B, self).print_msg() # Output: Class C
        super(A, self).print_msg() # Output: Class B
        super(D, self).print_msg() # Output: Class A

var = D()
var.print_msg()
```
Gördüğünüz gibi `super()` fonksiyonunun parametreleri ile oynayarak MRO'ya uymak zorunda kalmadan istediğim gibi miras aldım. Hatta daha ileriye gidip bir subclass'ın miras almadığı (yani MRO'sunda bulunmayan) class'lardan bile miras alabilirim. Örnek:
```py
class A:
    def print_msg(self):
        print("Class A")

class B:
    def print_msg(self):
        print("Class B")

class C(B):
    def print_msg(self):
        super(C, self).print_msg() # Output: Class B

class E(A):
    def print_msg(self):
        super(C, C()).print_msg() # Output: Class B

var = E()
var.print_msg()
```
Gördüğünüz gibi `super()` class'ının parametrelerine doğru argümanları doğru şekilde girerseniz böyle şeyler yapabilirsiniz. Bunu eski inheritance yöntemi ile de yapabilirsiniz. Bunun için `super(C, C()).print_msg()` yerinde `B.print_msg(self)` yazmanız yeterli. Miras alınmayan class'dan miras almaya çalışmak fanteziye giriyor. Yukarıda basit bir `print()` fonksiyonu tanımlı olduğu için sıkıntı çıkmasa bile böyle şeyler yapmayın çünkü `super()` fonksiyonunu bu şekilde kullanarak attribute yaratmak (create) gibi işlemleri yapmakta sıkıntı yaşarsınız.

**Not:** Eski inheritance yönetimi yukarıdaki koda uygulayınca sorunsuz çalışsa bile, çalışmadığı zamanlar oluyor. Örnek:
```py
class A:
    def print_msg(self):
        print("Class A")

class B:
    def print_msg(self):
        print("Class B")

class C(B):
    def print_msg(self):
        super(C, self).print_msg() # TypeError: super(type, obj): obj must be an instance or subtype of type

class D(A):
    def print_msg(self):
        C.print_msg(self) # Error

var = D()
var.print_msg() # Error
```
Burada `C.print_msg(self)` kodundaki `self` parametresinin içerdiği instance, `D` class'ından türetilen instance olduğu için ve `D` class'ı ile `C` class'ının MRO düzeyinde bir alakaları olmadığı için `super(C, self).print_msg()` statement okunduktan sonra `TypeError: super(type, obj): obj must be an instance or subtype of type` hatası yükseltilir.

**Not:** `super()` fonksiyonunu kullanırken `RuntimeError: super(): no arguments` hatası alıyorsanız, büyük ihtimal ya bir instance veya class method'a `self` veya `cls` parametresi eklemeyi unuttunuz ya da `super()` fonksiyonunun parametrelerine yanlış argümanlar girdiniz.