# Abstract Class
Abstract Class'lar, aynı özellikleri taşıyan objelerin aynı çatı altında toplayıp, bu objelere bir şablon (template) görevi gören class'lardır.

## Abstract Class Özellikleri
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

- Abstract class'dan miras alan subclass'lara, abstract class'da bildirilmiş (declaration) ya da tanımlanmış (definition) abstract methodları tanımlamak (definition) zorundasınız. Aksi halde `TypeError: Can't instantiate abstract class abstract_subclass_exp with abstract method process` örneğindeki gibi bir hatası alırsınız. Örnek:
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

## Abstraction
Abstraction (soyutlama) işlemine örnek:
```py
from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        print("Çalışıyor...", end=" ")

class Laptop(Computer):
    def process(self):
        print("Problem çözüldü.")

class Notebook(Computer):
    def process(self):
        super().process()
        print("Bug çözüldü.")

class WhiteBoard:
    def write(self):
        print("Yazı yazıldı.")

class BlackBoard(Computer):
    def write(self):
        print("Yazı yazıldı.")

var1 = Computer() # TypeError: Can't instantiate abstract class Computer with abstract method process
var2 = Laptop()
var3 = Notebook()
var4 = WhiteBoard()
var5 = BlackBoard() # TypeError: Can't instantiate abstract class BlackBoard with abstract method process

var2.process() # Output:Problem çözüldü.
var3.process() # Output: Çalışıyor... Bug çözüldü.
var4.process() # AttributeError: 'WhiteBoard' object has no attribute 'process'
```
Bu örneği parça parça açıklayalım:
- `Computer` class'ı `ABC` abstract base class'dan miras alarak bir abstract class'a olmuştur. Bu yüzden `Computer` class'ından instance türetemezsiniz.
- `Computer` abstract class'ındaki `process` methodu `@abstractmethod` decorator'ı ile decore edildiği için bu method artık bir abstract method olur. Bu yüzden `Computer` abstract class'ından miras alan class'larda `process` abstract methodunu tanımlamak zorundasınız. Aksi halde `TypeError: Can't instantiate abstract class BlackBoard with abstract method process` hatası yükseltilir. Bu methodun içeriğini aynı şekilde tanımlamak zorunda değilsiniz.

**Not:** Class'ın instance, class, static methodlar ve property objeleri olduğu gibi, Abstract class'ların da bunlar gibi objeleri vardır:
```py
import abc
for i in dir(abc):
    if not "_" in i[0]:
        if i == dir(abc)[-1]:
            print(i)
        else:
            print(i, end=", ")
```
**Output:**
```py
ABC, ABCMeta, abstractclassmethod, abstractmethod, abstractproperty, abstractstaticmethod, get_cache_token
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
Bunları kullanacaksanız, Python'da baya ilerilerde bir proje geliştiriyorsunuz demektir. Böyle bir proje geliştiren birisi ingilizce biliyordur. Bu yüzden ingilizce kaynaklardan kendiniz araştırabilirsiniz.

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/abc.html?highlight=abstract)