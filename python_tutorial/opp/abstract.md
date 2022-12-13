# İçindekiler

- [Abstract Class](#1)
    - [Abstract Class Özellikleri](#1.1)
    - [Abstraction](#1.2)

<h1 id="1">Abstract Class</h1>

Abstract Class'lar, aynı özellikleri taşıyan objeleri aynı çatı altında toplayıp, bu objelere bir şablon (template) görevi gören class'lardır.

<h2 id="1.1">Abstract Class Özellikleri</h2>

- Python, abstract class'ları doğrudan desteklemez. Bu yüzden `from abc import ABC, abstractmethod` şeklinde `ABC` (Abstract Base Class) ve `abstractmethod` decorator'ını programınıza import ederek başlamalısınız.

- `ABC`'den miras almış class'lardan instance türetemezsiniz. Aksi halde `TypeError: Can't instantiate abstract class abstract_class_exp with abstract method process` örneğindeki gibi bir hatası alırsınız. Örnek:
    ```py
    from abc import ABC, abstractmethod

    class A(ABC):
        @abstractmethod
        def func(self): pass

    var = A() # TypeError: Can't instantiate abstract class abstract_class_exp with abstract method process
    ```
    `ABC`'dan (Abstract Base Class'dan) instance türetince aynı şey yaşanmaz çünkü `ABC` ve `ABCMeta` class'larının methodları abstract method değildir.

- Abstract class'lar en az bir tane `@abstractmethod` decoratoru ile decore edilerek abstract method'a dönüştürülmüş method'a sahip olmalıdır. Aksi halde abstract class olarak kabul edilmezler.

- Bir abstract class'ı (`ABC` class'ını miras almış class'lar abstract class oluyor) miras alan subclass'lara, miras aldığı abstract class'da bildirilmiş (declaration) ya da tanımlanmış (definition) abstract methodları tanımlamak (definition) zorundasınız. Aksi halde `TypeError: Can't instantiate abstract class abstract_subclass_exp with abstract method process` örneğindeki gibi bir hatası alırsınız. Örnek:
    ```py
    from abc import ABC, abstractmethod

    class A(ABC):
        def __init__(self):
            print("Çalıştı...")

        @abstractmethod
        def func(self):
            pass

    class B(A):
        pass

    class C(A):
        def func(self):
            pass

    var1 = B() # TypeError: Can't instantiate abstract class B with abstract method func
    var2 = C() # Output: Çalıştı...
    ```

<h2 id="1.2">Abstraction</h2>

Abstraction (soyutlama) işlemine örnek:
```py
from abc import ABC, abstractmethod

class A(ABC): # A artık bir abstract class.

    @abstractmethod
    def func1(self):
        print("func1 A Class'ında çalıştı.", end=" ")

class B(A):
    def func1(self):
        print("func1 B Class'ında çalıştı.")

class C(A):
    def func1(self):
        super().func1()
        print("func1 C Class'ında çalıştı.")

class D:
    def func2(self):
        print("func2 D Class'ında çalıştı.")

class E(A):
    def func2(self):
        print("func2 E Class'ında çalıştı.")

var1 = A() # TypeError: Can't instantiate abstract class A with abstract method func1
var2 = B()
var3 = C()
var4 = D()
var5 = E() # TypeError: Can't instantiate abstract class E with abstract method func1

var2.func1() # Output: func1 B Class'ında çalıştı.
var3.func1() # Output: func1 A Class'ında çalıştı. func1 C Class'ında çalıştı.
var4.func1() # AttributeError: 'D' object has no attribute 'func1'
var4.func2() # Output: func2 D Class'ında çalıştı.
```
Bu örneği parça parça açıklayalım:
- `A` class'ı `ABC` abstract base class'dan miras alarak bir abstract class'a olmuştur. Bu yüzden `A` class'ından instance türetemezsiniz. Türetmeye çalışırsanız yukarıdaki gibi `TypeError: Can't instantiate abstract class A with abstract method func1` hatası yükseltilir.
- `A` abstract class'ındaki `func1` methodu `@abstractmethod` decorator'ı ile decore edildiği için bu method artık bir abstract method olur. Bu yüzden `A` abstract class'ından miras alan class'larda (`B`, `C` ve `E` class'ları) `func1` abstract methodunu tanımlamak zorundasınız. Aksi halde `var5 = E()` kodundaki gibi `TypeError: Can't instantiate abstract class BlackBoard with abstract method func1` hatası yükseltilir (çünkü `E` class'ından `func1` abstract methodu tanımlı değil).

**Not:** Yukarıdaki örnekte `B` ve `C` class'larında gördüğünüz gibi, bu class'ların `func1` methodunun içeriğini, bu class'ların miras aldığı `A` abstract class'ındaki `func1` abstract methodunun içeriğinin aynısı olacak şekilde tanımlamak zorunda değilsiniz. `B` ve `C` class'larında `func1` identifier'ına sahip bir fonksiyonun tanımlı olması yeterlidir. İçeriğini istediğiniz gibi değiştirebilirsiniz.

**Not:** Normal bir class'ın instance-class-static methodları ve property objeleri olduğu gibi, abstract class'ların da bunlar gibi objeleri vardır:
```py
import abc

print(dir(abc))
```
**Output:**
```py
['ABC', 'ABCMeta', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_abc_init', '_abc_instancecheck', '_abc_register', '_abc_subclasscheck', '_get_dump', '_reset_caches', '_reset_registry', 'abstractclassmethod', 'abstractmethod', 'abstractproperty', 'abstractstaticmethod', 'get_cache_token']
```
**Karşılıkları:**
```
ABCMeta              : ABC tanımlamak için kullanılan meta class
ABC                  : Abstract class oluşturmak için miras alınan class
abstractmethod       : Instance methodun abstract olanı
abstractclassmethod  : Class methodun abstract olanı
abstractstaticmethod : Static methodun abstract olanı
abstractproperty     : Property'nin abstract olanı
```
Bunları kullanacaksanız, Python ile baya kapsamlı bir proje geliştiriyorsunuz demektir. Böyle bir proje geliştirebilen birisi ingilizce de biliyordur. Bu yüzden ingilizce kaynaklardan kendiniz araştırabilirsiniz.

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/abc.html?highlight=abstract "https://docs.python.org/3/library/abc.html?highlight=abstract")