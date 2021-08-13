# Inheritance (Miras Alma)
Bir class'ın, başka bir class'ın method, class attribute, property vs. bütün objelerine sahip olması için yapılan işleme **Inheritance** (Miras Alma) denir. Inheritance (Miras Alma), aynı kodları her class'a tekrar tekrar yazma zahmetinden bizi kurtarır. Miras veren class parent class, super class, base class olarak isimlendirilir. Miras alan class child class, derived class, subclass olarak isimlendirilir. Ben tutorial boyunca bunlardan **base class** ve **subclass** isimlendirmelerini kullanacağım. Örnek:
```py
class A:
    pass

class B(A):
    pass
```
Burada `B` class'ı, `A` class'ından miras almıştır. Yani inheritance işlemini, subclass'ın isminin hemen yanındaki parantezin içine base class'ın ismini yazarak yapıyoruz.

Inheritance işleminden sonra base class ile subclass'daki objeler aynı obje oldukları için bu class'ların herhangi birinde yapılan işlem diğer class'a da yansıyabilir. Örnek:
```py
class A:
    class_exp1 = []
    class_exp2 = "First object"

class B(A):
    pass

A.class_exp1.append("Item 1")
print(A.class_exp1) # Output: ['Item 1']
print(B.class_exp1) # Output: ['Item 1']

B.class_exp1.append("Item 2")
print(A.class_exp1) # Output: ['Item 1', 'Item 2']
print(B.class_exp1) # Output: ['Item 1', 'Item 2']

A.class_exp2 = "First object"
print(A.class_exp2) # Output: First object
print(B.class_exp2) # Output: First object

B.class_exp2 = "Second object"
print(A.class_exp2) # Output: First object
print(B.class_exp2) # Output: Second object
```
Gördüğünüz gibi yeniden tanımlama (redefinition) işleminde `B` class'ını `class_exp2` class attribute'u `A` class'ındaki `class_exp2` class attribute'undan farklı bir objeye dönüştüğü için farklı value'lara sahip olmuş olabilir ama `class_exp1` class attribute'una `append` methodu kullanıldığı için farklı bir objeye dönüşmüyor ve dolayısıyla `A` veya `B` class'ı üzerinden yapılan müdahelelere iki class'dan da ulaşılabiliyor.

**Not:** Yukarıdaki olayın sebebi, `B` class'ındaki miras alınan objelerin `B` class'ına ait olmaması. Yani `A` class'ındaki objeler `B` class'ına kopyalanmıyor, `B` class'ındaki objeler `A` class'ındaki objelere atıfta bulunuyor (refers). Kanıt:

<img src="https://i.ibb.co/WDYRsCH/image.png" alt="image" border="0">

`B` class'ının `__dict__` methoduna bakarsanız bu durumun ne anlama geldiğini daha iyi anlarsınız:
```py
print({(i):(A.__dict__[i]) for i in A.__dict__ if not "__" in i}) # Output: {'class_exp1': [], 'class_exp2': 'First object', 'func1': <function A.func1 at 0x00000203562060D0>, 'func2': <classmethod object at 0x0000020356204FD0>, 'func3': <staticmethod object at 0x0000020356204FA0>, 'property_exp': <property object at 0x00000203561F5E50>}
print({(i):(B.__dict__[i]) for i in B.__dict__ if not "__" in i}) # Output: {}
```
Gördüğünüz gibi `B` class'ının `A` class'ından miras aldığı objeler `B` class'ını `__dict__` methodunda bulunmuyor. Bu durum, `A` class'ındaki objelerin `B` class'ına kopyalanmadığını, `B` class'ındaki objelerin `A` class'ındaki objelere atıfta bulunduğunu (refers) kanıtlar.

**Not:** Bir class'ın base class ya da subclass olarak isimlendirilmesi sembolik bir şeydir. Python için bu durumu "`B` class'ı `A` class'ından miras almış." şeklinde yorumlar.

## Object Class
Class'lar, Python'ın' 3.x öncesi sürümlerinde **yeni tip class'lar** ve **eski tip class'lar** olmak üzere ikiye ayrılıyordu. Eski tip class'lara örnek:
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
Python'ın 3.x öncesi sürümlerinde, yeni tip class'larla birlikte gelen bazı özellikler vardı (Örneğin `@property` decorator'u). Python'ın 3.x öncesi sürümlerinde, bir class'ın yeni tip özellikleri kullanabilmesi için `object` adındaki class'ından miras alması gerekiyordu. Bu yüzden `object` adındaki class'ından miras alan class'lara **yeni tip**, almayan class'lara da **eski tip** class dendi. Python 3'den sonra bütün class'lar yeni tip class olarak güncellenmiştir. Bu yüzden Python 3'den sonra herhangi bir class'ın yeni tip class'larla birlikte gelen özellikleri kullanabilmesi için artık `object` adındaki class'ından miras alması gerekmiyor. Yani Python 3'den sonra aşağıdaki class tanımlamaları arasında hiçbir fark yoktur:
```py
class A:
    pass

class A():
    pass

class A(object):
    pass
```

## Types of Inheritance (Miras Alma Türleri)
Inheritance (Miras Alma)'nın çeşitleri vardır:
- Her şeyi miras almak
- Miras alınan objeyi geçersiz kılmak (override)
- Objeyi geçersiz kılmadan (override) miras almak

### Her şeyi miras almak
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
Gördüğünüz gibi `B` class'ı `A` class'ının bütün objelerini miras aldı.

**Not:** Bir subclass, bir base class'ın her şeyini miras alacaksa, `class` keyword ile bir subclass tanımlamak yerine basitçe `subclass = base_class()` gibi bir instantiation işlemi ile işinizi halledebilirsiniz. Örnek:
```py
class A:
    pass

B = A()
```

### Miras alınan objeyi geçersiz kılmak (override)
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

print(A.func) # Output: <function A.func at 0x00000294C0D96040>
print(B.func) # Output: <function A.func at 0x00000294C0D96040>
print(C.func) # Output: <function A.func at 0x00000294C0D960D0>>
```
Gördüğünüz gibi `B` class'ının `func` methodu `A` class'ının `func` methodu ile aynı objeyken, `C` class'ının `func` methodu `A` class'ının `func` methodundan farklı bir objedir. Bunun sebebi `C` class'ında tanımlanan `func` methodunun `A` class'ının `func` methodunu geçersiz kılmasıdır (override).

### Objeyi geçersiz kılmadan (override) miras almak
Base class'dan miras alınan objeler geçersiz kılınmadan (override) içeriği değiştirilmek istenilirse `super()` build-in fonksiyonunu veya eski inheritance yöntemini kullanabilirsiniz.

# Multiple Inheritance (Çoklu Miras Alma)
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
Buradaki `D` subclass'ı sırasıyla `C`, `B` ve `A` class'larından miras almıştır. Çoklu miras alma işlemi, ilgili class'ın MRO'suna göre yapılır. Method resolution order (kısaca MRO), "method çözümleme sırası" anlamına gelmektedir. MRO, **[directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)**'dan (kısaca DAG) türetilen, **[C3 linearization algorithm](https://en.wikipedia.org/wiki/C3_linearization)** tarafından oluşturulan **[total order](https://en.wikipedia.org/wiki/Total_order)**'dır.

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

<img src="https://i.ibb.co/X5XstLP/A.png" alt="A" border="0">

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

**Not:** MRO'yu anlamak için inheritance bilgisi, inheritance'ı anlamak için de MRO bilgisi gerekmektedir. Inheritance ve multiple inheritance konu başlıklarında bol bol MRO kavramıyla karşılaşacaksınız. MRO'yu hala anlamadıysanız, verdiğim linklerden de yararlanarak kendi başınıza MRO'nun ne olduğunu öğreniniz.

MRO hakkında daha fazla bilgi için:
- **[Python history blogspot](https://python-history.blogspot.com/2010/06/method-resolution-order.html)**
- **[Stackoverflow](https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance)**

Multiple inheritance'ın MRO'su 2 kurala göre belirlenir:
1. Subclass her zaman ilk sıradadır.
2. Subclass'ın miras aldığı base class'ların subclass'a tanımlanma sırasına saygı gösterilir. (örneğin `class A(B, C)` kodunda `B`, `C`'den önce gelir.) Bu yüzden bir class'ın miras aldığı class'larda aynı isme (identifier) sahip objeler varsa, bu class kendi MRO'sundaki (kendisi hariç) soldan ilk sırada bulunan class'a öncelik verir. Örnek:
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
    `D` class'ının MRO'su `D -> A -> B -> C -> object` şeklindedir. `D` class'ı `func()` methodunu, `D` class'ının MRO'suna göre öncelikli olan `A` class'ından miras alıp, diğer class'lardaki `func()` methodlarını görmezden gelir. Eğer `A` class'ında `func()` methodu olmasaydı, `D` class'ı bu methodu bulana kadar kendi MRO'sunda soldan sağa doğru bütün class'lara bakacaktı. Eğer `D` class'ının MRO'sunda belirtilen class'ların hiçbirinde `func()` methodu bulunamazsaydı, `AttributeError: 'D' object has no attribute 'func'` hatası yükseltilirdi.

**Not:** Multiple inheritance yaparken, miras alınan class'ları doğru sıra ile subclass'a girmek önemlidir. Örnek:
```py
O = object
class A(O): pass
class B(A): pass
class C(B,A): pass
class D(A,B): pass # Error
```
**Output:**
```
TypeError: Cannot create a consistent method resolution
order (MRO) for bases A, B
```
Gördüğünüz gibi `B` class'ı `A`'dan miras aldığı için `D` class'ına `A,B` sırasıyla yazamıyorsunuz. Diğer class'ların da miras alma sırasına (MRO'suna) saygı göstermek zorundasınız.

# `super(<subclass>, <subclass object>)` Fonksiyonu
**Başlamadan önce oku:** `super()` fonksiyonunu anlayabilmeniz açısından bolca olası senaryo örneği vererek anlattım. Bu yüzden `super()` fonksiyonunu ilk seferde anlayamadıysanız, bu başlığı tekrar tarar okumanızı tavsiye ederim. Hala anlamadıysanız kendiniz farklı kaynaklardan araştırabilirsiniz.

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
Gördüğünüz gibi `super()` fonksiyonunun oluşturduğu proxy objesinin üzerinden `A` class'ının `__init__` fonksiyonunu çağırarak `A` class'ının instance methodlarını elde etmiş olduk. Başka bir örnek:
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
`super().__init__(p1, p2, p3)` kodundaki `__init__` methoduna girdiğiniz `p1`, `p2` ve `p3` değerleri parametre değil argümandır. Çünkü `super()` fonksiyonunun oluşturduğu proxy objesi üzerinden `__init__` methodu çağırıyorsunuz. Bu yüzden erişebildikleri scope'lardan birinde tanımlanmaya ihtiyaç duyarlar. Bu tanımlama işini de `def __init__(self, p4, p1, p2, p3)` kısmında yapıyoruz. Birden fazla parametre tanımlamanız gerektiği zaman yukarıdaki gibi `*args` (`p1 = "Falan Filan"` gibi default value'ya sahip parametreler varsa `*args` yerine `**kwargs`) yıldızlı parametresini kullanabilirsiniz.

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
Burada, `A` class'ı üzerinden instance method çağırıken `self` parametresini tanımlamayı unutmamaya dikkat etmelisiniz. Eski inheritance yöntemi ile `super()` fonksiyonunun farkı hakkında bilgi için [tıklayınız](https://stackoverflow.com/a/33469090/15170972).

**Not:** Instance ve class method'larında inheritance işlemi yaparken kullandığımız `super()` fonksiyonunun parametrelerine argüman tanımlayarak kullanmakla argüman tanımlamadan kullanmak arasında hiçbir fark yoktur. Bu durum Python'ın, instance ve class methodlarda kullanılan `super()` fonksiyonunun parametrelerine doğru argümanları otomatik olarak girmesinden kaynaklanır. Bu yüzden özel durumlar dışında `super()` fonksiyonunun parametresiz kullanılması tavsiye edilir. Eğer parametresiz kulanamıyorsanız, programınızda büyük tasarım hatalar var demektir. ,

`super()` fonksiyonunun `<subclass>` (birinci parametre) ve `<subclass object>` (ikinci parametre) olmak üzere 2 parametresi vardır:

**Subclass**: `<subclass>` parametresine argüman olarak sadece class (`A`, `B`, ... vb.) verilebilir.

**Subclass Object**: `<subclass object>` parametresine verilen argüman subclass ya da instance olabilir.

Bu iki parametre birbiri ile ilişkili bazı kurallara sahiptir:

`<subclass object>` parametresine argüman olarak girilen subclass'ın ya da instance'ın türetildiği subclass'ın MRO'su, `<subclass>` parametresinde belirtilen class'ı içermelidir. Örneğin `<subclass object>` parametresine argüman olarak girilen `D` subclass'ının MRO'su `D -> C -> B -> A -> object` şeklindeyse, `<subclass>` parametresine argüman olarak girilen class bu class'lardan birisi olmak zorundadır. Aksi halde, `TypeError: super(type, obj): obj must be an instance or subtype of type` hatası yükseltilir. Bu hata, "`super(type, obj)`: `obj`, `type`'ın `instance`'ı ya da `subclass`'ı olmalıdır." anlamına gelmektedir.

`<subclass object>` parametresine argüman olarak instance verilirse, `super()` fonksiyonunun oluşturduğu proxy objesi üzerinden çağırılacak instance ve class methodların `self`/`cls` olan ilk parametresine argüman olarak `self`/`cls` ya da instnace/class girmek zorunda değiliz. Ama `<subclass object>` parametresine argüman olarak subclass verilirse, `super()` fonksiyonunun oluşturduğu proxy objesi üzerinden çağırılacak instance methodların `self` olan ilk parametresine argüman olarak `self` ya da instnace girmek zorundayken, class methodların `cls` olan ilk parametresine argüman olarak `cls` ya da class girmek zorunda değilsiniz. Static methodlarda ilk parametre özel olmadığı için az önce anlattıklarımızla uğraşmanız gerekmez (static methoda parametre olarak özellikle `self` ve `cls` tanımlamadıysanız tabiki)

`super()` fonksiyonu, `<subclass object>` parametresine argüman olarak verilen subclass'ın ya da instance'ın türetildiği subclass'ın MRO'suna göre, `<subclass>` parametresinde belirtilen class'dan bir sonraki class'dan miras alır. O class'da istenilen objeyi bulamazsa bir sonrakine geçer. Örnek:
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
Gördüğünüz gibi `D` class'ındaki `super()` fonksiyonu, `<subclass object>` parametresinde belirtilen instance'ın türetildiği class olan `D` class'ının MRO'suna göre `<subclass>` parametresinde belirtilen class'dan sonraki class olan `C` class'ına baktı ama orada `func` methodunu bulamadığı için bir sonraki class olan `A` class'ına baktı ve `func` methodunu bulduğu için miras aldı. Eğer `C` class'ına `pass` yerine `def func(self): super(D,self).func()` statement tanımlasaydık yine aynı sonucu alırdık ama `def func(self): super(D,D()).func()` statement tanımlasaydık `var.func()` methodu `2` sonucunu verecekti. Bunun nedenini aşağıda açıklıyorum.

`<subclass object>` parametresinde argüman olarak ya da `<subclass object>` parametresinde subclass girilip, döndürdüğü proxy objesi üzerinden çağırılacak methoda `self`/`cls` girmekle `A()` gibi instance girmek arasında, programın işleyişine etki etme konusunda önemli farklar vardır. Örnek:
```py
class A():
    class_attri = "Class Attribute"

    def __init__(self):
        self.instance_attri = "Instance Attribute"

    def func1(self):
        print("instance_attri:", end=" ")

    @classmethod
    def func2(cls):
        print("class_attri:", end=" ")

    ########################################

    def func3(self):
        print("instance_attri:", end=" ")

    @classmethod
    def func4(cls):
        print("class_attri:", end=" ")

    ########################################

    def func5(self):
        print("instance_attri:", end=" ")

    ########################################

    def func6(self):
        print("instance_attri:", end=" ")

class B(A):
    def func1(self):
        super(B, self).func1()
        print(self.instance_attri)

    @classmethod
    def func2(cls):
        super(B, cls).func2()
        print(cls.class_attri)

    ##############################

    def func3(self):
        super(B, B()).func3()
        print(self.instance_attri)

    @classmethod
    def func4(cls):
        super(B, B()).func4()
        print(cls.class_attri)

    ##############################

    def func5(self):
        super(B, B).func5(self)
        print(self.instance_attri)

    ##############################

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
Gördüğünüz gibi bu kısımda `<subclass object>` parametresinde argüman olarak `self`/`cls` ya da instnace/class girmek arasında bir fark olmadı çünkü `instance_attri` ve `class_attri` attribute'ları `var1` instance'ı türetildiğinde tanımlanmıştı. Bu yüzden `B` class'ındaki class ve instance methodlar, bu attribute'lara erişme konusunda sıkıntı yaşamadılar. Peki yaşasalardı? Örnek:
```py
class A():
    class_attri = "Class Attribute"

    def __init__(self):
        pass

    def func1(self):
        self.instance_attri = "Instance Attribute"
        print("instance_attri:", end=" ")

    @classmethod
    def func2(cls):
        print("class_attri:", end=" ")

    ########################################

    def func3(self):
        self.instance_attri = "Instance Attribute"
        print("instance_attri:", end=" ")

    @classmethod
    def func4(cls):
        print("class_attri:", end=" ")

    ########################################

    def func5(self):
        self.instance_attri = "Instance Attribute"
        print("instance_attri:", end=" ")

    ########################################

    def func6(self):
        self.instance_attri = "Instance Attribute"
        print("instance_attri:", end=" ")

class B(A):
    def func1(self):
        super(B, self).func1()
        print(self.instance_attri)

    @classmethod
    def func2(cls):
        super(B, cls).func2()
        print(cls.class_attri)

    ##############################

    def func3(self):
        super(B, B()).func3()
        print(self.instance_attri) # AttributeError: 'B' object has no attribute 'instance_attri'

    @classmethod
    def func4(cls):
        super(B, B()).func4()
        print(cls.class_attri)

    ##############################

    def func5(self):
        super(B, B).func5(self)
        print(self.instance_attri)

    ##############################

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
Burada hata veren instance methodların `super()` fonksiyonuna argüman olarak `B()`, hata vermeyen instance methodların `super()` fonksiyonuna argüman olarak `self` tanımlandığını görüyoruz. Bunun sebebi şudur:
- `super()` fonksiyonuna `B()` argümanını verirsek, `super()` fonksiyonu ürettiği proxy objesinin üzerinden çağırılan fonksiyonun etkileri, `B()` kodunun türettiği instance'ı etkiler. `B()` kodunun türettiği instance, `var1` instance'ından farklı bir obje olduğu için `var1` instance'ı, `super()` fonksiyonu ürettiği proxy objesinin üzerinden çağırılan fonksiyonun etkilerinden etkilenmez. Bu yüzden `print(self.instance_attri)` fonksiyonları yazdıracak bir `self.instance_attri` attribute'u bulamadıkları için hata yükseltirler.
- `super()` fonksiyonuna `self` argümanını verirsek, `super()` fonksiyonu ürettiği proxy objesinin üzerinden çağırılan fonksiyonun etkileri `var1` instance'ını (yani doğru instance'ı) etkiler. Bu yüzden `print(self.instance_attri)` fonksiyonları yazdıracak bir `self.instance_attri` attribute'u bulabildikleri için hata yükseltmeden görevlerini yaparlar.

Böyle bir sorunla class methodlarda karşılaşmayız çünkü o class'dan bir tane class vardır. İster `cls` istersen direkt class'ın ismini (identifier) kullan, o class'dan bir tane class olduğu için iki durumda da aynı class'a atıfta bulunulur. Instance'larda bunun olmamasının sebebi, her instance'ın birbirinden farklı bir obje olmasından kaynaklanıyor (nedenini anlattık zaten uzatmaya gerek yok). 

**Not:** Yukarıda bahsettiğim sorunu basitçe `B()` yerine `self` kullanarak çözebilirsiniz. Bunun yerine methoda `return` statement tanımlamak, methodu `__init__` methodunda çağırmak gibi çözüm arayışlarına girmeyin. Özellikle methodu `__init__` methodunda çağırmak gibi bir hata yaparsanız, terminaliniz yazılarla dolduktan sonra `RecursionError: maximum recursion depth exceeded while calling a Python object` hatası yükseltilir.

**Not:** `super()` fonksiyonuna girdiğiniz `self`/`cls` argümanları, bu fonksiyonun tanımlı olduğu methodun parametresine tanımlı olan `self`/`cls` parametreleridir. Yani bu parametrelerin isimlerini değiştirirseniz, `super()` fonksiyonuna gireceğiniz argümanların da isimlerini bu parametrelere göre düzenlemelisiniz.

Static method'larda olay bambaşkadır. Örnek:
```py
class A:
    @staticmethod
    def func():
        print("Static Method Çalıştı...")

class B(A):
    @staticmethod
    def func():
        super(B,B()).func() # Output: Static Method Çalıştı...
        super(B,B).func() # Output: Static Method Çalıştı...

var1 = B()
var1.func()
```
Static methodlara `self`/`cls` parametreleri tanımlamak zorunlu olmadığı için bu parametreleri tanımlamadığımızda, `<subclass object>` parametresine argüman olarak `self` ya da `cls` giremeyiz ve mecburen instance ya da class girmek zorunda kalırız. Peki bu parametreleri tanımlarsak? Örnek:
```py
class A:
    attri1 = "Class Attribute"
    def __init__(self):
        self.attri2 = "Instance Attribute"

    @staticmethod
    def foo(self, cls):
        self.attri2 = 2
        cls.attri1 = 1
        print(self.attri2, end=" | ")
        print(cls.attri1)

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
Gördüğünüz gibi `super()` class'ının parametrelerine doğru argümanları doğru şekilde girerseniz böyle şeyler yapabilirsiniz. Bunu eski inheritance yöntemi ile de yapabilirsiniz. Bunun için `super(C, C()).print_msg()` yerinde `B.print_msg(self)` yazmanız yeterli. Miras alınmayan class'dan miras almaya çalışmak fanteziye giriyor. Yukarıda basit bir `print()` fonksiyonu tanımlı olduğu için sıkıntı çıkmasa bile böyle şeyler yapmaktan çekinin çünkü `super()` fonksiyonunu bu şekilde kullanarak attribute tanımlamak gibi işlemleri yapmakta sıkıntı yaşarsınız.

**Not:** Eski inheritance yönetimi yukarıdaki koda uygulayınca sorunsuz çalışsada, çalışmadığı zamanlar oluyor. Örnek:
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
Burada `C.print_msg(self)` kodundaki `self` parametresinin içerdiği instance `D` class'ının instance'ı olduğu için ve `D` class'ı ile `C` class'ının MRO düzeyinde bir alakaları olmadığı için `super(C, self).print_msg()` statement okunduktan sonra `TypeError: super(type, obj): obj must be an instance or subtype of type` hatası yükseltilir.

**Not:** `super()` fonksiyonunu kullanırken `RuntimeError: super(): no arguments` hatası alıyorsanız, büyük ihtimal ya bir instance veya class method'a `self` veya `cls` parametresi eklemeyi unuttunuz ya da `super()` fonksiyonunun parametrelerine yanlış argümanlar girdiniz.