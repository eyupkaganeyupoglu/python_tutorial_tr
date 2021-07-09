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

# Property
Property kelimesi de attribute kelimesi gibi nitelik/özellik anlamına gelmektedir. Class içinde salt verileri tutan variable'lara attribute, belirli işlevleri yerine getiren fonksiyonlara method adı verildiğini biliyoruz. Property'lerin en temel işlevi, main class'da tanımlı bir methodu, bir instance içinde attribute gibi kullanabilmemizi sağlamasıdır. Property objesi oluşturmak için `@property` decorator'ını ya da `property()` fonksiyonunu kullanabilirsiniz.

## `@property` Decorator
Bir class'daki instance methodların üzerinde `@property` decorator'ı kullanılarak **property** objeleri oluşturulabilir. Örnek:
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
Bu koddaki `func1` methodu bellekte `<function Class.func1 at 0x00000160370A2790>` objesi olarak saklanırken, `func2` methodu bellekte `func2` adındaki `<property object at 0x00000160370ADC20>` property objesinin içinde bulunan `fget` ismindeki methodda `<function Class.func2 at 0x00000160370A2790>` olarak saklanır. Kanıt:

<img src="https://i.ibb.co/ydDXLKk/image.png" alt="image" border="0">

Bu görseldeki `fget`, `fset` ve `fdel` methodlarının tam olarak ne olduğu daha sonra property methodları başlığında anlatılacak. Yukarıdaki görselde dikkat edilmesi gereken şey; `func2` fonksiyon objesi, `func1` fonksiyon objesi gibi main class objesinin `function variables` kısmında bulunmuyor, `fget` kısmında bulunuyor. Bunun sebebi; `func2` fonksiyon objesi artık `func2` property'sinin `getter` işleminde kullanılacak olmasıdır.

Property'lerin en temel işlevi, main class'da tanımlı bir methodu, bir instance içinde attribute gibi kullanabilmemizi sağlamasıdır demiştik. Buradan yola çıkarak; property'ler main class'da obje olarak bulunurken, instance'larda sadece attribute olarak bulunur diyebiliriz. Örnek:
```py
class Class():
    def __init__(self):
        pass

    def func1(self):
        pass

    @property
    def func2(self):
        pass

var = Class()
```
Yukarıdaki kodda, main class'da property objesi olarak bulunan `func2`, `var` instance'ında attribute olarak bulunmaktadır. Kanıtı:

<img src="https://i.ibb.co/7XqSJvB/image.png" alt="image" border="0">

`func2` fonksiyon objesini `Class.func2()` ya da `var.func2()` şeklinde çağıramazsınız (call) çünkü `func2` fonksiyon objesi `func2` property'sinin bir parçası olduğu için artık main class'da bir method olarak bulunmamaktadır. Main class'da bir method olarak bulunmayan `func2` fonksiyon objesi, dolayısıyla main class'dan türetilen `var` instance'ında da bir method olarak bulunmaz.
- `Class.func2()` kodunu çalıştırırsanız sırasıyla aşağıdaki olaylar gerçekleşir:
    - Python, `Class.func2()` kodunun önce `Class.func2` kısmını okur ve `Class` class'ının `func2` adında bir methodu varmı diye bakar ve `func2` adında bir (`<property object at 0x000001A6D72DBD60>`) property objesi bulur. Bu `<property object at 0x000001A6D72DBD60>` property objesine kısaca "`func2`" diyelim.
    - Property objeleri çağırılabilir (callable) değildir. Bu yüzden `Class` class'ının `func2` methodunda bulunan property objesini `Class.func2()` şeklinde çağırmaya (call) çalışırsak `TypeError: 'property' object is not callable` hatası yükseltilir.

- `var.func2()` kodunu çalıştırırsanız sırasıyla aşağıdaki olaylar gerçekleşir:
    - Python, `var.func2()` kodunun önce `var.func2` kısmını okur ve `var` instance'ının `func2` adında bir methodu varmı diye bakar ve `func2` adında bir attribute bulur.
    - Python, `func2` attribute'u `'None'` value'sunu içerdiği için (neden `'None'` olduğunu `getter` methodu başlığında anlatılacak) `var.func2` kodu `'None'` çıktısını verir. Bu yüzden `var.func2()` kodu, Python'un gözünde `None()` koduna dönüşür.
    - `None` value'su `NoneType` bir objedir. `NoneType` objeler çağırılabilir (callable) olmadığı için `TypeError: 'NoneType' object is not callable` hatası yükseltilir.

Şimdiye kadar anlattıklarımızla ilgili bir örnek:
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
print(var1.func1) # Output: <bound method Class1.func1 of <__main__.Class1 object at 0x00000298C68A3FD0>>
print(var2.func2()) # TypeError: 'str' object is not callable
print(var2.func2) # Output: Class2 A
```
Yukarıdaki kodda, `print()` fonksiyonlarının outputlarının nedenlerini teker teker açıklamak gerekirse:
- `print(var1.func1())`
    - `Class1` class'ında tanımlı `func1` adındaki instance method, `@property` decorator'ı ile işaretlenmediği için fonksiyon özelliğini korur ve `Class1().func1()` kodundaki gibi `func1()` şeklinde çağırılabilir (call) çünkü fonksiyonlar çağırılabilir (callable) objelerdir. `print(Class1().func1())` kodundaki `Class1().func1()` kodu ile `func1` methodu çağırarak (call), döndürdüğü değer `print()` fonksiyonu ile yazdırılır.

- `print(var1.func1)`
    - `Class1` class'ında tanımlı `func1` adındaki instance method, `@property` decorator'ı ile işaretlenmediği için fonksiyon özelliğini korur. `var1.func1` kodu, "`0x00000298C68A3FD0` adresindeki `__main__.Class1` objesine ait `<function Class1.func1 at 0x00000160370A2790>` fonksiyonuna bağlı bir method (bound method) olan `func1` adındaki instance method'u" anlamına gelen `<bound method Class1.func1 of <__main__.Class1 object at 0x00000298C68A3FD0>>` objesini verir. Bu yüzden `print(var1.func1)` kodunun output'u bu `<bound method Class1.func1 of <__main__.Class1 object at 0x00000298C68A3FD0>>` objesini yazdırır.

- `print(var2.func2())`
    - `Class2` class'ında tanımlı `func2` adındaki instance method, `@property` decorator'ı ile işaretlendiği için fonksiyon özelliğini koruyamaz ve `func2` adındaki property'nin (`fget` methodunda depolanmış) bir parçası olur. Bu property `var2` instance'ında `func2` attribute'u olarak bulunur ve `Class2 A` stringini içerir (nasıl olduğu daha önce anlatıldı). Python, `var2.func2()` kodunun önce `var2.func2` kısmını okur. `var2.func2` kısmı `Class2 A` string değerini verdiği için `var2.func2()` kodu Python gözünde `'Class2 A'()` koduna dönüşür. String bir obje çağırılabilir (callable) olmadığı için `var2.func2()` kodu "string objeler çağırılabilir (callable) değildir." anlamına gelen `TypeError: 'str' object is not callable` hatasını yükseltir. Daha önce de `Class` class'ındaki `func2` property'sini `Class.func2()` şeklinde çağırmaya (call) çalışınca `TypeError: 'property' object is not callable` hatası yükseltilmişti. Bu hatayla `var2.func2()` kodunun yükselttiği hata benzerdir çünkü ikisinde de çağırılabilir (callable) olmayan objeleri çağırmaya çalışıyoruz.

- `print(var2.func2)`
    - `Class2` class'ında tanımlı `func2` adındaki instance method, `@property` decorator'ı ile işaretlendiği için fonksiyon özelliğini koruyamaz ve `func2` adındaki property'nin (`fget` methodunda depolanmış) bir parçası olur. `func2` property'si, `Class2` class'ından türetilen `var2` instance'ında `func2` attribute'u olarak bulunur ve `Class2 A` string type value'sunu içerir (nasıl olduğu daha önce anlatıldı). `print(var2.func2)` kodu, `var2` instance'ında bulunan `func2` attribute'unun içerdiği `Class2 A` stringini yazdırır.

**Not:** Property kavramını anlamak için [**descriptor**](https://docs.python.org/3/howto/descriptor.html) kavramını araştırmalısınız. Bu konu, Python dışındaki programlama dillerini de ilgilendiren bir mesele olduğu için anlatması çok uzun sürer. Bu yüzden merak eden kendisi araştırı öğrenebilir.

## Property Methodları
Property'lerin üç önemli build-in methodu vardır:
- Değer döndürmek için kullanılan `getter`
- Değer atamak için kullanılan `setter`
- Değer silmek için kullanılan `deleter`

Bu build-in methodların etki ettiği üç tane attribute vardır.
- `getter` build-in methodu ile işaretlenmiş fonksiyonunun atandığı attribute olan `fget`
- `setter` build-in methodu ile işaretlenmiş fonksiyonunun atandığı attribute olan `fset`
- `deleter` build-in methodu ile işaretlenmiş fonksiyonunun atandığı attribute olan `fdel`

**!Burada Kaldın!** En son getter, setter, deleter methodları başlıklarını yazacaktın ama yeni property oluşturma saçmalığını bu 3 başlığı yazdıktan sonra açıklayacağın için bütün örneklerdeki method isimlerini aynı yap.