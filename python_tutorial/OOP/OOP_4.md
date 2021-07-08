# Class Members
Bir class'ın içindeki attribute'lar, variable'lar, method'lar vb. diğer öğelerin her biri bir class member'dır (sınıf üyesidir). Class member'lar üçe ayrılır:
- Aleni üyeler (public members)
- Gizli üyeler (private members)
- Yarı-gizli üyeler (semi-private members)

## Public Members (Aleni Üyeler)
Bir class member'a class dışından normal yöntemlerle erişilebiliyorsa, bu class member'a **public member** denir. `dir(Class)` fonksiyonu bize `Class` class'ı içindeki bütün class member'ları verir. Bu class member'lara aşağıda bulunan koddaki gibi **normal yöntemlerle doğrudan** erişilebiliyorsa, bu öğeler public member'dır. Örnek:
```py
class Class():
    class_attribute = 'Class Attribute'

    def instance_method(self):
        self.instance_attribute = 'Instance Attribute'
        print(f"instance_method() Çalıştı! | {self.instance_attribute}")

    @classmethod
    def class_method(cls):
        print(f"class_method() Çalıştı! | {cls.class_attribute}")

    @staticmethod
    def static_method():
        static_attribute = 'Static Attribute'
        print(f"static_method() Çalıştı! | {static_attribute}")

print(dir(Class())) # Output: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'class_attribute', 'class_method', 'instance_method', 'static_method']

# Normal yöntemlerden kasıt:
print(Class.class_attribute) # Output: Class Attribute
Class().instance_method() # Output: instance_method() Çalıştı! | Instance Attribute
Class().class_method() # Output: class_method() Çalıştı! | Class Attribute
Class().static_method() # Output: static_method() Çalıştı! | Static Attribute
```
**Not:** Private member olarak tanımlanmamış bütün class member'lar, Python tarafından public member olarak kabul edilir.

## Private Members (Gizli Üyeler)
Class'ın iç işlerini ilgilendirdiği için dışarıdan erişimine gerek olmayan ya da dışarıdan erişilirse programda sorunlara neden olabilecek class member'ların dışarıya açık (yani public member) olması istenmez. Bu class member'ların isimlerinin önüne (yani en soluna) **en az 2** tane, sonuna (yani en sağına) **en fazla 1** tane alt çizgi (`_`) koyarak bu class member'ları **private member**'lar haline getirebilirsiniz. Private member'lara **normal yöntemlerle doğrudan** erişilemez. Örnek:
```py
class Class():
#      Attribute        Attribute           class member  
#        name             value                 type      
    gizli            = "gizli"            # Public Class
    _gizli           = "_gizli"           # Public Class
    _gizli_          = "_gizli_"          # Public Class
    _gizli__         = "_gizli__"         # Public Class
    _gizli___        = "_gizli___"        # Public Class
    __gizli          = "__gizli"          # Private Class
    __gizli_         = "__gizli_"         # Private Class
    __gizli__        = "__gizli__"        # Public Class
    __gizli___       = "__gizli___"       # Public Class
    __gizli_gizli    = "__gizli_gizli"    # Private Class
    __gizli_gizli_   = "__gizli_gizli_"   # Private Class
    __gizli_gizli__  = "__gizli_gizli__"  # Public Class
    __gizli_gizli___ = "__gizli_gizli___" # Public Class
    ___gizli         = "___gizli"         # Private Class
    ___gizli_        = "___gizli_"        # Private Class
    ___gizli__       = "___gizli__"       # Public Class
    ___gizli___      = "___gizli___"      # Public Class

print(Class().gizli) # Output: gizli
print(Class().__gizli) # AttributeError: 'Class' object has no attribute '__gizli'
```
Gördüğünüz gibi private member oluşturma kuralına uyan isimleri Python private member olarak kabul ederken, bu kurala uymayanları public member olarak kabul ediyor.

**Not:** Private member'lara class dışından normal yollarla doğrudan erişemesek bile, class'içinden kullanabiliriz. Örnek:
```py
class Class():
    __gizli1 = "Private Class Member 1"
    __gizli2 = "Private Class Member 2"

    def yazdir1(self):
        print(self.__gizli1)
    
    def yazdir2(self):
        return self.__gizli2

Class().yazdir1() # Output: Private Class Member 1
print(Class().yazdir2()) # Output: Private Class Member 2
```
Gördüğünüz gibi `__gizli1` ve `__gizli2` private member'ları class içinde kullandık. `Class().yazdir1()` ve `print(Class().yazdir2())` kodlarıyla bu private member'ların value'larına class dışından ulaşabilsek bile bu **normal yollarla doğrudan** bir erişim olmadığından, dolaylı yoldan bir erişim olduğundan bu class member'lar public member olarak kabul edilmez.

### Name Mangling (İsim Bulandırma)
Private olarak tanımlanmış bir class member, class dışından tamamen erişilemez değildir. Bu durum Python'ın private member'ları **Name Mangling** kullanarak farklı bir isimle (identifier) belleğe kaydetmesinden kaynaklanır.
```py
class Class():
#      Attribute        Attribute           Class Member  |  Bellekteki
#        Name             Value                 Type      |     İsmi
    gizli            = "gizli"            # Public Class  | gizli
    _gizli           = "_gizli"           # Public Class  | _gizli
    _gizli_          = "_gizli_"          # Public Class  | _gizli_
    _gizli__         = "_gizli__"         # Public Class  | _gizli__
    _gizli___        = "_gizli___"        # Public Class  | _gizli___
    __gizli          = "__gizli"          # Private Class | _Class__gizli
    __gizli_         = "__gizli_"         # Private Class | _Class__gizli_
    __gizli__        = "__gizli__"        # Public Class  | __gizli__
    __gizli___       = "__gizli___"       # Public Class  | __gizli___
    __gizli_gizli    = "__gizli_gizli"    # Private Class | _Class__gizli_gizli
    __gizli_gizli_   = "__gizli_gizli_"   # Private Class | _Class__gizli_gizli_
    __gizli_gizli__  = "__gizli_gizli__"  # Public Class  | __gizli_gizli__
    __gizli_gizli___ = "__gizli_gizli___" # Public Class  | __gizli_gizli___
    ___gizli         = "___gizli"         # Private Class | _Class___gizli
    ___gizli_        = "___gizli_"        # Private Class | _Class___gizli_
    ___gizli__       = "___gizli__"       # Public Class  | ___gizli__
    ___gizli___      = "___gizli___"      # Public Class  | ___gizli___

print(Class().__gizli) # AttributeError: 'Class' object has no attribute '__gizli'
print(Class()._Class__gizli) # Output: __gizli
```
Python private member'ları `_{class_name}{private_class_member_name}` formatında oluşturulmuş isimlerle (identifier) belleğe kaydeder. Buna **Name Mangling (isim bulandırma)** denir. Bu yüzden bir private member'a, `Class().__gizli` örneğindeki gibi class'da tanımlı ismini kullanarak erişemezsiniz çünkü bellekte bu isimde bir attribute yok. Kanıtı:
```py
class Class():
#      Attribute  Attribute    Class Member   |  Bellekteki
#        Name       Value          Type       |     İsmi
    gizli        = "gizli"   # Public Class   | gizli
    __gizli      = "__gizli" # Private Class  | _Class__gizli

print(Class().gizli) # Output: gizli
print(Class()._Class__gizli) # Output: __gizli
print(Class().__gizli) # AttributeError: 'Class' object has no attribute '__gizli'
```
<img src="https://i.ibb.co/02QnGKb/image.png" alt="image" border="0">

**Not:** Private member'lara bu şekilde erişebilmemiz, private member'ları teknik olarak private yapmaz. Bu yüzden private member'ların doğru kullanımı name mangling ile bir nebze güvenceye alınmış ve kullanıcıların inisiyatifine bırakılmıştır.

## Semi-private Members (Yarı-gizli Üyeler)
Önüne (Yani en soluna) bir tane alt çizgi (`_`) konularak oluşturulan isimlere sahip class member'lara **Semi-private member**'lar denir. Semi-private member'lar teknik olarak public member'lardır. Yeni Semi-private member'lar, Python kullanıcıların uydurduğu bir şeydir. Python kullanıcıları Semi-private member'ları, bir class member'ın bellekteki ismini (identifier) değiştirmeden private member gibi kullanmak istediklerinde Semi-private member'ları kullanmayı tercih eder.
```py
class Class():
#      Attribute  Attribute    Class Member   |  Bellekteki
#        Name       Value          Type       |     İsmi
    gizli        = "gizli"   # Public Class   | gizli
    _gizli       = "_gizli"  # Public Class   | _gizli
    __gizli      = "__gizli" # Private Class  | _Class__gizli

print(Class().gizli) # Output: gizli
print(Class()._gizli) # Output: _gizli
print(Class()._Class__gizli) # Output: __gizli
print(Class().__gizli) # AttributeError: 'Class' object has no attribute '__gizli'
```
<img src="https://i.ibb.co/YNxwwy6/image.png" alt="image" border="0">

# `@property` Decorator
Class içinde salt verileri tutan variable'lara attribute, belirli işlevleri yerine getiren fonksiyonlara method adı verildiğini biliyoruz. Property kelimesi de attribute kelimesi gibi nitelik/özellik anlamına gelmektedir. `@property` decorator kullanılarak oluşturulan objelere **property** denir. Örnek:
```py
class Class():
    def __init__(self):
        pass

    def func1(self):
        pass

    @property
    def func2(self):
        pass
```
Bu koddaki `func1` fonksiyonu bellekte `<function Class.func1 at 0x00000160370A2790>` objesi olarak saklanırken, `func2` fonksiyonu bellekte `func2` adındaki `<property object at 0x00000160370ADC20>` property objesinin içinde `fget` methodunda `<function Class.func2 at 0x00000160370A2790>` olarak saklanır. Kanıt:

<img src="https://i.ibb.co/ydDXLKk/image.png" alt="image" border="0">

Yukarıdaki görselde dikkat edilmesi gereken şey, `func2` fonksiyon objesi `func1` fonksiyon objesi gibi main class objesinin function variables kısmında bulunmuyor, `fget` kısmında bulunuyor çünkü `func2` fonksiyon objesi artık `func2` property'sinin bir parçası haline gelmiştir. Bu property'ler main class'da obje olarak bulunurken, instance'larda sadece attribute olarak bulunur. Örnek:
```py
class Class():
    def __init__(self):
        pass

    def func1(self):
        pass

    @property
    def func2(self):
        pass
```
<img src="https://i.ibb.co/RH6CtHm/image.png" alt="image" border="0">

`@property` decorator'ının en temel işlevi, bir methodu bir attribute gibi kullanılabilecek hale getirmektir. Bu yüzden `func2` fonksiyon objesini `var.func2()` kodundaki gibi çağıramazsınız çünkü `@property` decorator'ı, `func2` fonksiyonunu bir attribute haline getirmiştir ve attribute'lar fonksiyon'lar gibi çağırılabilir (callable) değildir. Çağırmaya çalışırsanız, `var.func2()` kodundaki `var.func2` kısmının döndürdüğü çağırılabilir olmayan `NoneType`'ı, `NoneType()` şeklinde çağırmaya çalıştığınız için `TypeError: 'NoneType' object is not callable` hatası alırsınız. Bu görseldeki `fget`, `fset` ve `fdel` methodlarının ne olduğu daha sonra değer döndürme, değer atama ve değer silme başlıklarında anlatılacak. 

`@property` decorator'ının en temel işlevi, bir methodu bir attribute gibi kullanılabilecek hale getirmektir demiştik. Bunu daha ayrıntılı açıklamak gerekirse; `@property` decorator'ının en temel işlevi, etkilediği methodları kullanan bir property objesi oluşturmaktır.

**!Burada Kaldın!** en son buraya property'lerin main class'da farklı instace'larda farklı olduğunu, instance'larda property'lerin bulunmadığını, sadece property'lerin attribute şeklindeki hallerinin bulunduğunun kanıtını gösterecektin. Buna ek olarak yukarıdaki uzun yazıda "`@property` decorator'ının en temel işlevi, bir methodu bir attribute gibi kullanılabilecek hale getirmektir." kısmını da instance ve main class'da farklı ilediğini (nedenini ilk cümlede anlattım) orada ya aktarıp cümleyi güncelleyecektin.

Örnek:
```py
class Class1():
    def __init__(self):
        pass

    def func1(self):
        return "Class1 A"

class Class2():
    def __init__(self):
        pass

    @property
    def func2(self):
        return "Class2 A"
var1 = Class1()
var2 = Class2()
print(var1.func1()) # Output: Class1 A
print(Class1().func1) # Output: <bound method Class1.func1 of <__main__.Class1 object at 0x000001BBC14E2280>>
print(Class2().func2()) # TypeError: 'str' object is not callable
print(Class2().func2) # Output: Class2 A
```
Yukarıdaki kodda, `print()` fonksiyonlarının outputlarının nedenlerini teker teker açıklamak gerekirse:
- `print(Class1().func1())`
    - `Class1` class'ındaki `func1` adındaki instance method, `@property` decorator'ı ile işaretlenmediği için fonksiyon özelliğini korur ve `Class1().func1()` kodundaki gibi `func1()` şeklinde çağırılabilir (call: çağırmak, callable: çağırılabilirlik). `print(Class1().func1())` kodu ile bu methodu çağırarak, döndürdüğü değeri `print()` fonksiyonu ile ekrana yazdırıyoruz.

- `print(Class1().func1)`
    - `Class1` class'ındaki `func1` adındaki instance method, `@property` decorator'ı ile işaretlenmediği için fonksiyon özelliğini korur. `Class1().func1` kodundaki `func1`, `<function Class1.func1 at 0x00000160370A2790>` objesini temsil eden bir isimdir (identifier). Bu objeyi `func1()` şeklinde çalıştırmadığımız için `print(Class1().func1)` kodu direkt `<function Class1.func1 at 0x00000160370A2790>` objesini işaret eden `<bound method Class1.func1 of <__main__.Class1 object at 0x00000298C68A3FD0>>` output'unu döndürüyor. Bu output, "`func1` metodu `Class1` sınıfına ait bir metot ve `0x00000298C68A3FD0` adresinde olan `__main__.Class1` objesine ait" anlamına gelmektedir.   

- `print(Class2().func2())`
    - `Class2` class'ındaki `func2` adındaki instance method, `@property` decorator'ı ile işaretlendiği için fonksiyon özelliğini koruyamaz ve bir property olur. `func2` property'si, daha sonra anlatılacak **değer döndürme** işlevini gerçekleştirir. `func1` methodu çağırılabilir (callable) bir objedir ama `func2`, string type bir property olduğu için ve string'ler çağırılabilir (callable) bir obje olmadığı için `Class2().func2()` kodu, "string objeler çağırılabilir (callable) değildir." anlamına gelen `TypeError: 'str' object is not callable` hatasını yükseltir.

- `print(Class2().func2)`
    - `Class2` class'ındaki `func2` adındaki instance method, `@property` decorator'ı ile işaretlendiği için fonksiyon özelliğini koruyamaz ve bir property olur. `func2` property'si, daha sonra anlatılacak **değer döndürme** işlevini gerçekleştirir. `func2` property'si string bir değer olan `Class2 A`'ya eşit olduğu için `print(Class2().func2)` kodu `Class2 A` değerini yazdırır.

**Not:** `func1`  ve `func2`'nin ikisi de bir method olmasına rağmen `func2` `@property` decorator'ı ile işaretlendiğinde nasıl oluyor da bir property'ye dönüşüp `Class2().func2` şeklinde kullanıldığında `func2` methodunun döndürdüğü değere eşit oluyor gibi sorularınızı cevaplayabilmeniz için [**descriptor**](https://docs.python.org/3/howto/descriptor.html) kavramını araştırmalısınız. Bu konu, Python dışındaki programlama dillerini de ilgilendiren bir mesele olduğu için anlatması çok uzun sürer. Bu yüzden merak eden kendisi araştırı öğrenebilir.

Bunun dışında `@property` decorator'ın üç önemli işlevi bulunur:
- Değer döndürmek
- Değer atamak
- Değer silmek

## Değer Döndürme
`@property` decorator'ı ile işaretlen bir method, aksi belirtilmediği sürece sadece `değer döndürme` işlevini gerçekleştirir. Örnek:
```py
class Class():
    def __init__(self):
        self.before = 0

    @property
    def after(self):
        return self.before
var = Class()
print(var.after) # Output: 0
print(var.before) # Output: 0
```
Gördüğünüz gibi `before` attribute'unu döndüren `after` methodunu `@property` decorator'ı ile işaretleyerek, `before` attribute'u gibi kullanabildiğimiz bir property elde etmiş olduk. Bu property'e `var.before = 1` kodundaki gibi `var.after = 1` şeklinde değer atayama çalışırsak `AttributeError: can't set attribute` hatası verir çünkü bu property için (daha sonra öğreneceğimiz) herhangi bir `setter` mekanizması tanımlamadığı için bu property **Read Only**'dir (salt okunur).

**Not:** Property'lerin değer döndürme özelliğinden yararlanarak, bilinçli olarak **Read Only Attribute**'lar (Salt Okunur Attribute'lar) oluşturabilirsiniz. Örnek:
```py
class Class():
    def __init__(self):
        self._before = 0

    @property
    def after(self):
        return self._before
var = Program()
print(var.after) # Output: 0
var._before = 1
print(var.after) # Output: 1
var.after = 1 # AttributeError: can't set attribute
```
Gördüğünüz gibi `after` property'si için herhangi bir `setter` mekanizması tanımlanmadığı için `var.after = 1` kodu ile `_before` attribute'unun değerini değiştiremeyiz. Değiştirmek istersek `var._before = 1` şeklinde değiştirmek zorundayız ama kodu yazan kullanıcı `_vari` attribute'unu semi-private member olarak tanımladığı için bu hareket etik olmaz. Bu sayede `_before` attribute'unu `after` property'si sayesinde read only attribute olarak kullanabiliyoruz.

## Değer Atama
**Ön Bilgi:** `setter`, `@property` decorator'unun bir methodudur.

Read only property'lerin değerlerini doğrudan değiştiremeyeceğimizi öğrenmiştik. Eğer amacınız bir attribute'u read only hale getirmek değilse, bir property üzerinde hem read hem de write (property'nin değerini değiştirmek gibi) işlemleri yapmak istiyorsanız, o property için bir `setter` method'u tanımlayabilirsiniz. Örnek:
```py
class Class():
    def __init__(self):
        self._before = 0

    @property
    def after(self):
        return self._before

    @after.setter
    def after_set(self, yeni_değer):
        self._before = yeni_değer
        return self._before

var = Class()
print(var._before) # Output: 0
print(var.after) # Output: 0

var.after_set = 1
print(var.after) # Output: 1
print(var.after_set) # Output: 1
var.after = 2 # AttributeError: can't set attribute
```
Buradaki durumları madde madde açıklamak gerekirse:
- `@after.setter` tanımlanmasaydı `after` property'si read only olarak kalacaktı.
- `setter` methodu, `@{property_name}.setter` formatında kullanılır. `after_set` methodunu `@after.setter` decorator'ı ile işaretleyerek, `after_set` methodunu bir property'e dönüştürmüş oluyoruz (`<property object at 0x000002315179BC70>`).
- Bir methodu attribute gibi kullanabilmemizi `@property` decorator'ının sağladığını öğrenmiştik. `_before` attribute'unun değerini `after` property'si ile okuyabildiğimiz gibi `after_set` property'si ile yazabiliriz. Burada dikkat çekmek istediğim şey `var.after = 2` kodunun `AttributeError: can't set attribute` hatası vermesi. Bunun sebebi, `after` property'sine sadece read yetkisi vermemizden kaynaklanıyor. `after_set` property'sinin hem değer döndürme hem de değer atama işlemlerini gerçekleştirebilmesinin nedeni, bu property'e hem read hem de write yetkisi verilmesidir. Kanıtı:

<img src="https://i.ibb.co/ykkNXBH/image.png" alt="image" border="0">

<img src="https://i.ibb.co/3f9SJfw/image.png" alt="image" border="0">

Gördüğünüz gibi `after` property'sinin içinde `after()` methodunun objesini içeren `fget` adında bir obje varken, `fset` ve `fdel` objeleri boş. Bu durum `after` property'sinin sadece read yetkisine sahip olmasının kanıtı çünkü `after` property'si read işlemi için `fget` objesindeki `after()` methodunu kullanabilecekken, `fset` ve `fdel` objeleri boş oldundan write ve delete işlemleri için kullanabilecekleri bir method yoktur. Diğer taraftan, `after_Set` property'sinin içinde `after()` methodunun objesini içeren `fget` ve `after_set()` methodunun objesini içeren `fset` objeleri varken, `fdel` objesi boş. Bu durum da `after_set` property'si sadece read ve write yetkisine sahip olması olmasının kanıtı çünkü `after_set` property'si read işlemi için `fget` objesindeki `after()` methodunu ve write işlemi için `fset` objesindeki `after_set()` methodunu kullanabilecekken, `fdel` objesi boş oldundan delete işlemi için kullanabileceği bir method yoktur.

**Not:** Yukarıda read işlemi için `after`, write işlemi için `after_set` property'si tanımlamış olsak bile, bu property'ler için böyle bir isimlendirme (identifier) Python camiasında kabul görmez çünkü bir programın işleyişinde property'nin kolaylık sağladığı en önemli mevzulardan birisi **backwards compatibility** (geriye dönük uyumluluk) sağlamasıdır. Örnek:
```py
class Class():
    def __init__(self):
        self.veri = 0

    @property
    def data(self):
        return self.veri

    @data.setter
    def data(self, yeni_değer):
        self.veri = yeni_değer
        return self.veri
var = Class()
print(var.data) # Output: 0
var.data = 1
print(var.data) # Output: 1
```
Programınızda tanımladığınız bir class içindeki bir attribute'un ismini sonradan değiştirseniz, programınızın eski versiyonunu kullanan kişiler için sıkıntı yaratmış olursunuz. Örneğin `self.veri` attribute'u programınızın eski versiyonunda `self.data` olarak tanımlıysa, `self.data`'yı `self.veri` olarak değiştirdiğiniz zaman programınızın eski versiyonunu kullanan kullanıcılar `self.veri`'yi `self.data` zannettikleri için programlarını yanlış yazıp hata alabilirler. `self.veri` attribute'u üzerinde yapılabilecek read ve write işlemlerini, yukarıdaki kodda olduğu gibi `data` ismindeki property üzerinde de yapılabilecek şekilde ayarlarsanız, bu sorunun önüne geçmiş olursunuz.

`setter` methodu değer doğrulama gibi işlemlerde de kullanışlıdır. Örnek:
```py
class Class():
    def __init__(self):
        self._sayı = 0

    @property
    def sayı(self):
        return self._sayı

    @sayı.setter
    def sayı(self, yeni_değer):
        if yeni_değer % 2 == 0:
            self._sayı = yeni_değer
        else:
            print('Çift değil!')

        return self.sayı

var = Class()
print(var.sayı) # Output: 0

var.sayı = 1 # Output: Çift değil!
print(var.sayı) # Output: 0

var.sayı = 2
print(var.sayı) # Output: 2
```

## Değer Silmek
`@property` decorator'ının `deleter` methodunu kullanarak bir attribute'u sildiğinizde python'un nasıl davranmasını gerektiğini belirleyebiliyorsunuz. Bunun için `setter` methoduna benzeyen `@{property_name}.deleter` formatını kullanıyoruz. Örnek:
```py
class Class():
    def __init__(self):
        self._sayı = 0

    @property
    def sayı(self):
        return self._sayı

    @sayı.deleter
    def sayı_del(self):
        print("sayı Siliniyor...")
        del self._sayı

var = Class()
print(var.sayı) # Output: 0
del var.sayı_del # Output: sayı Siliniyor...
print(var.sayı) # AttributeError: 'Class' object has no attribute '_sayı'
```
Gördüğünüz gibi `del var.sayı_del` kodu çalıştırıldığında Python, `__main__.Class` objesindeki `sayı_del` property'sinin `fdel` objesinde tanımlı olan `<function Class.sayı_del at 0x000001DD6C8C18B0>` objesinde belirtildiği gibi `sayı_del()` fonksiyonunu çalıştırıyor ve bu fonksiyondaki `del self._sayı` kodu sayesinden `self._sayı` attribute'u bellekten siliniyor. Bu işlem sonrasında artık `self._sayı` attribute'u bellekte bulunmadığından `var.sayı` koduyla sayı property'sini Python'dan talep ettiğimizde Python, böyle bir attribute'un olmadığını söyleyen `AttributeError: 'Class' object has no attribute '_sayı'` hatasını yükseltiyor.

## `property(fget=None, fset=None, fdel=None, doc=None)` Fonksiyonu
`property()` fonksiyonu, daha önce ne olduğunu anlattığımız `fget`, `fset` ve `fdel` methodlarını tanımlayarak bir property oluşturabilmenizi sağlar. Örnek:
```py
class Class():
    def __init__(self):
        self._sayı = 0

    def sayı(self):
        return self._sayı

    def sayı_set(self, yeni):
        self._sayı = yeni
        return self._sayı

    def sayı_del(self):
        print("sayı siliniyor...")
        del self._sayı

    sayı = property(fget = sayı, fset = sayı_set, fdel = sayı_del)

var = Class()
print(var.sayı) # Output: 0
var.sayı = 1
print(var.sayı) # Output: 1
del var.sayı # Output: sayı siliniyor...
print(var.sayı) # AttributeError: 'Class' object has no attribute '_sayı'
```
gördüğünüz gibi `@property`, `setter` ya da `deleter` decorator kullanmadan bir property oluşturup kullanabildik.

Bir proparty'nin `fget`, `fset` ve `fdel` methodlarına tanımlanan methodlar bir class method ise, bu property'i kullanarak işlemler yapamazsınız. Örnek:
```py
class Class():
    _sayı = 0
    def __init__(self):
        pass

    @classmethod
    def sayı(cls):
        return cls._sayı

    @classmethod
    def sayı_set(cls, yeni):
        cls._sayı = yeni
        return cls._sayı

    @classmethod
    def sayı_del(cls):
        print("sayı siliniyor...")
        del cls._sayı

    sayı = property(fget = sayı, fset = sayı_set, fdel = sayı_del)

var = Class()
print(var.sayı) # TypeError: 'classmethod' object is not callable
var.sayı = 1 # TypeError: 'classmethod' object is not callable
del var.sayı # TypeError: 'classmethod' object is not callable
```
Bu durumun sebebi bir instance üzerinde bu işlemleri yapmaya çalışmak değildir. Aynı işlemleri doğrudan `Class` class'ının üzerinde de yapamazsınız.
```py
class Class():
    _sayı = 0
    def __init__(self):
        pass

    @classmethod
    def sayı(cls):
        return cls._sayı

    @classmethod
    def sayı_set(cls, yeni):
        cls._sayı = yeni
        return cls._sayı

    @classmethod
    def sayı_del(cls):
        print("sayı siliniyor...")
        del cls._sayı

    sayı = property(fget = sayı, fset = sayı_set, fdel = sayı_del)

print(Class.sayı) # Output: <property object at 0x000002A41CC25EA0>
Class.sayı = 1
print(Class.sayı) # Output: 1
del Class.sayı
print(Class.sayı) # Output: AttributeError: type object 'Class' has no attribute 'sayı'
```
Gördüğünüz gibi istediğimiz sonuçları alamadık. `Class` class'ının üzerinden bu işlemleri yapmak için property kullanmaktan vazgeçip, doğrudan class methodları ve class attribute'ları kullanmalısınız. Örnek:
```py
class Class():
    _sayı = 0
    def __init__(self):
        pass

    @classmethod
    def sayı(cls):
        return cls._sayı

    @classmethod
    def sayı_set(cls, yeni):
        cls._sayı = yeni
        return cls._sayı

    @classmethod
    def sayı_del(cls):
        print("sayı siliniyor...")
        del cls._sayı

print(Class._sayı) # Output: 0
print(Class.sayı()) # Output: 0
print(Class.sayı_set(1)) # Output: 1
Class.sayı_del() # Output: sayı siliniyor...
print(Class._sayı) # AttributeError: type object 'Class' has no attribute '_sayı'
print(Class.sayı()) # AttributeError: type object 'Class' has no attribute '_sayı'
```
