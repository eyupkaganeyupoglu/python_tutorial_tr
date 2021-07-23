# Abstract Class
Abstract Class'lar, aynı özellikleri taşıyan objelerin aynı çatı altında toplanıp, bu objelere bir şablon (template) görevi gören class'lardır.

## Abstract Class Özellikleri
- Python, abstract class'ları doğrudan desteklemez. Bu yüzden `from abc import ABC, abstractmethod` şeklinde `ABC` (Abstract Base Class) ve `abstractmethod` decorator'ını programınıza import ederek başlamalısınız.

- `ABC` (Abstract Base Class'dan) ve `ABC`'den miras almış class'lardan instance türetemezsiniz. Aksi halde `TypeError: Can't instantiate abstract class abstract_class_exp with abstract method process` örneğindeki gibi bir hatası alırsınız.

- Abstract class'lar en az bir tane `@abstractmethod` decoratoru ile decore edilerek abstract method'a dönüştürülmüş method'a sahip olmalıdır.

- Abstract class'dan miras alan subclass'lara, abstract class'da bildirilmiş (declaration) ya da tanımlanmış (definition) abstract methodları tanımlamak (definition) zorundasınız. Aksi halde `TypeError: Can't instantiate abstract class abstract_subclass_exp with abstract method process` örneğindeki gibi bir hatası alırsınız.

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
- `Computer` class'ı `ABC` abstract base class'dan miras alarak bir abstract class'a dönüşmüştür. Bu yüzden yukarıdaki gibi `var1 = Computer()` şeklinde instance türetmeye çalışırsanız `TypeError: Can't instantiate abstract class Computer with abstract method process` hatası alırsınız.
- `Computer` abstract class'ındaki `process` instance methodu, `@abstractmethod` decorator'u ile bir abstract methoda decore edilmiştir. Bu yüzden `Computer` abstract class'ından miras alan bütün subclass'larda bu `process` abstract methodu yukarıdaki gibi tanımlanmak zorundadır. Eğer tanımlanmazsa, `BlackBoard` subclass'ından instance türetmeye çalışırkenki gibi `TypeError: Can't instantiate abstract class BlackBoard with abstract method process` hatası ile karşılaşırsınız.
- `Computer` abstract class'ındaki `process` instance methodunu illa `def process(self): pass` şeklinde declare edip bırakmak zorunda değilsiniz. İçine çeşitli şeyler tanımlayıp, bunları `Computer` abstract class'ından miras alan subclass'larda da `super().process()` şeklinde miras vererek kullanabilirsiniz.

Daha fazla bilgi için [tıklayınız](https://www.geeksforgeeks.org/abstract-classes-in-python/).