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

Bu görseldeki `fget`, `fset` ve `fdel` methodlarının tam olarak ne olduğu daha sonra property methodları başlığında anlatılacak. Yukarıdaki görselde dikkat edilmesi gereken şey; `func2` fonksiyon objesi, `func1` fonksiyon objesi gibi main class objesinin `function variables` kısmında bulunmuyor, `fget` kısmında bulunuyor. Bunun sebebi; `func2` fonksiyon objesi artık `func2` property'sinin read işleminde (daha sonra anlayılacak) kullanılacak olmasıdır. 

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
    - `Class1` class'ında tanımlı `func1` adındaki instance method, `@property` decorator'ı ile decore edilmediği için fonksiyon özelliğini korur ve `Class1().func1()` kodundaki gibi `func1()` şeklinde çağırılabilir (call) çünkü fonksiyonlar çağırılabilir (callable) objelerdir. `print(Class1().func1())` kodundaki `Class1().func1()` kodu ile `func1` methodu çağırarak (call), döndürdüğü değer `print()` fonksiyonu ile yazdırılır.

- `print(var1.func1)`
    - `Class1` class'ında tanımlı `func1` adındaki instance method, `@property` decorator'ı ile decore edilmediği için fonksiyon özelliğini korur. `var1.func1` kodu, "`0x00000298C68A3FD0` adresindeki `__main__.Class1` objesine ait `<function Class1.func1 at 0x00000160370A2790>` fonksiyonuna bağlı bir method (bound method) olan `func1` adındaki instance method'u" anlamına gelen `<bound method Class1.func1 of <__main__.Class1 object at 0x00000298C68A3FD0>>` objesini verir. Bu yüzden `print(var1.func1)` kodunun output'u bu `<bound method Class1.func1 of <__main__.Class1 object at 0x00000298C68A3FD0>>` objesini yazdırır.

- `print(var2.func2())`
    - `Class2` class'ında tanımlı `func2` adındaki instance method, `@property` decorator'ı ile decore edildiği için fonksiyon özelliğini koruyamaz ve `func2` adındaki property'nin (`fget` methodunda depolanmış) bir parçası olur. Bu property `var2` instance'ında `func2` attribute'u olarak bulunur ve `Class2 A` stringini içerir (nasıl olduğu daha önce anlatıldı). Python, `var2.func2()` kodunun önce `var2.func2` kısmını okur. `var2.func2` kısmı `Class2 A` string değerini verdiği için `var2.func2()` kodu Python gözünde `'Class2 A'()` koduna dönüşür. String bir obje çağırılabilir (callable) olmadığı için `var2.func2()` kodu "string objeler çağırılabilir (callable) değildir." anlamına gelen `TypeError: 'str' object is not callable` hatasını yükseltir. Daha önce de `Class` class'ındaki `func2` property'sini `Class.func2()` şeklinde çağırmaya (call) çalışınca `TypeError: 'property' object is not callable` hatası yükseltilmişti. Bu hatayla `var2.func2()` kodunun yükselttiği hata benzerdir çünkü ikisinde de çağırılabilir (callable) olmayan objeleri çağırmaya çalışıyoruz.

- `print(var2.func2)`
    - `Class2` class'ında tanımlı `func2` adındaki instance method, `@property` decorator'ı ile decore edildiği için fonksiyon özelliğini koruyamaz ve `func2` adındaki property'nin (`fget` methodunda depolanmış) bir parçası olur. `func2` property'si, `Class2` class'ından türetilen `var2` instance'ında `func2` attribute'u olarak bulunur ve `Class2 A` string type value'sunu içerir (nasıl olduğu daha önce anlatıldı). `print(var2.func2)` kodu, `var2` instance'ında bulunan `func2` attribute'unun içerdiği `Class2 A` stringini yazdırır.

**Not:** Property kavramını anlamak için **descriptor** kavramını araştırmalısınız. Gerekli siteler sırasıyla:
- [Tıklayınız](https://docs.python.org/3.7/howto/descriptor.html).
- [Tıklayınız](https://docs.python.org/3/howto/descriptor.html).

## Property Methodları
Property'lerin üç önemli build-in methodu vardır:
- Değer döndürmek için kullanılan, read yetkisini temsil eden `getter`
- Değer atamak için kullanılan, write yetkisini temsil eden `setter`
- Değer silmek için kullanılan, delete yetkisini temsil eden`deleter`

Bu build-in methodların etki ettiği üç tane attribute vardır.
- `getter` build-in methodu ile decore edilmiş fonksiyonunun atandığı attribute olan `fget`
- `setter` build-in methodu ile decore edilmiş fonksiyonunun atandığı attribute olan `fset`
- `deleter` build-in methodu ile decore edilmiş fonksiyonunun atandığı attribute olan `fdel`

Bu methodlara aşağıdaki gibi görüntüleyebilirsiniz:
```py
print(dir(property), end=f"\n" + "-"*70 + "\n")

for i in dir(property):
    if not ("_" in i):
        print(i, end=", ")
```
**Output:**
```
['__class__', '__delattr__', '__delete__', '__dir__', '__doc__',
'__eq__', '__format__', '__ge__', '__get__', '__getattribute__',
'__gt__', '__hash__', '__init__', '__init_subclass__',
'__isabstractmethod__', '__le__', '__lt__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__set__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', 'deleter', 'fdel',
'fget', 'fset', 'getter', 'setter']
----------------------------------------------------------------------
deleter, fdel, fget, fset, getter, setter,
```
**Not:** Bir property'nin `getter`, `setter` ve `deleter` build-in methodları ile  `fget`, `fset` ve `fdel` methodlarına atanan instance methodlar (`@property` decorator'ında olduğu gibi) main class'ın `function attributes` kısmında bulunmazlar. Örnek:
```py
class Class():
    def __init__(self):
        self._sayı = 0

    def sayı1(self):
        pass

    def sayı2(self):
        return self._sayı

    def sayı3(self, yeni):
        self._sayı = yeni
        return self._sayı

    def sayı4(self):
        del self._sayı

var = Class()
```

<img src="https://i.ibb.co/1sVKrFh/image.png" alt="image" border="0">

Gördüğünüz gibi `getter`, `setter`, `deleter` property methodları ve `@property` decorator'u ile decore edilmeyen instance methodlar, `var` instance'ında ve main class'da `function attributes` kısmında bulunmaktalar.
```py
class Class():
    def __init__(self):
        self._sayı = 0

    @property
    def sayı(self):
        pass

    @sayı.getter
    def sayı(self):
        return self._sayı

    @sayı.setter
    def sayı(self, yeni):
        self._sayı = yeni
        return self._sayı

    @sayı.deleter
    def sayı(self):
        del self._sayı
```

<img src="https://i.ibb.co/h90n9fM/image.png" alt="image" border="0">

Gördüğünüz gibi `getter`, `setter`, `deleter` property methodları ve `@property` decorator'u ile decore edilen instance methodlar, `fget`, `fset` ve `fdel` methodlarına atandığı için main class'da `function attributes` kısmında bulunmamaktadırlar. Dolayısıyla bu instance methodlar, main class'dan türetilen instance'larda da bulunmazlar.

### `getter` Methodu:
Bir class'ın içinde tanımlı olan instance method üzerinde `getter` property methodunu kullanırsanız, bu instance method, ilgili property objesinin `fget` methodunda tanımlı, **read** olarak isimlendirilmiş **değer döndürme** işlemini gerçekleştiren fonksiyon olarak varlığını sürdürür (bundan sonra 'değer döndürme işleminden'den 'read işlemi' olarak bahsedilecek). Örnek:
```py
class Class():
    def __init__(self):
        self._sayı = 0

    @property
    def sayı(self):
        pass

    @sayı.getter
    def sayı(self): # Buna "2. sayı fonksiyonu" diyelim
        return self._sayı
var = Class()
print(var.sayı) # Output: 0
print(var._sayı) # Output: 0
```
Gördüğünüz gibi `@property` decorator'u ile oluşturduğumuz `sayı` adındaki property objesi tanımladık. Daha sonra `getter` property methodunu kullanarak `return self._sayı` kodu ile `_sayı` attribute'unun değerini döndüren 2. `sayı` fonksiyonunu, `sayı` property'sinin `fget` methoduna atadık. Kanıtı:

<img src="https://i.ibb.co/Jt7wmqZ/image.png" alt="image" border="0">

Böylece; `@{Property_object_name}.getter` formatındaki decorator'u kullanarak, `{Property_object_name}` kısmında belirttiğimiz property objesinin read işleminden sorumlu olmasını istediğimiz instance methodu, `{Property_object_name}` kısmında belirttiğimiz property objesinin `fget` methoduna atabildiğiniz öğrendik.

`Class` class'ından `sayı` property'si, `var` instance'ında `sayı` adında bir attribute olarak bulunuyor (nedenini daha önce anlattım). Kanıtı:

<img src="https://i.ibb.co/zmmFmTQ/image.png" alt="image" border="0">

Gördüğünüz gibi `var` instance'ında bulunan `sayı` attribute'unun değeri, `_sayı` attribute'undaki gibi `0`'dır. Bunun böyle olması, `fget` methodunda tanımlı, read işleminden sorumlu fonksiyon olan 2. `sayı` fonksiyonundaki `return self._sayı` kodu sayesindedir. 2. `sayı` fonksiyonunda `return self._sayı` kodu olmasaydı, 2. `sayı` fonksiyonu hiçbir değer döndürmeyeceği için `var` instance'ındaki `sayı` attribute'unun değeri `'None'` olacaktı. Kanıtı:

<img src="https://i.ibb.co/5TdfjzZ/image.png" alt="image" border="0">

Böylece `var` instance'ında bulunan `sayı` attribute'unun value'sunun, `Class` class'ındaki `sayı` property'sinin `fget` methodunda tanımlı, read işleminden sorumlu fonksiyon olan 2. `sayı` fonksiyonundaki `return self._sayı` kodu ile ilişkili olduğunu öğrendik.

`sayı` property'sinde `fset` methodunda write işlemi ile ilgili fonksiyon ve `fdel` methodunda delete işlemi ile ilgili fonksiyon tanımlı olmadığı için `var.sayı = 1` gibi write (değer atama) ya da `del var.sayı` gibi delete (değer silme) işlemleri yapamazken, `fget` methodunda read işlemi ile ilgili fonksiyon tanımlı olduğu için read işlemi yapılabiliyor. Bunun gibi sadece read işlemi yapılabilen attribute'lara **Read Only Attribute** (Salt Okunur Attribute) denir.

**Not:** `@{Property_object_name}.getter` formatındaki decorator'ı kullanarak bir property'nin' `fget` methoduna read işlemi ile ilgili fonksiyonu tanımlamasanız bile, sadece `@property` decorator'u kullanılarak oluşturulan property'lerde `fget` methodunda read işlemi ile ilgili fonksiyonun tanımlı olduğunu farketmişsinizdir. Örnek:
```py
class Class():
    def __init__(self):
        self._sayı = 0

    @property
    def sayı(self):
        pass

var = Class()
print(var.sayı) # Output: None
print(var._sayı) # Output: 0
```
Gördüğünüz gibi `sayı` property'si için `getter` tanımlamasak bile `print(var.sayı)` kodu hata vermiyor, `var` instance'ında tanımlı `sayı` attribute'unun değerini döndürüyor. Bunun sebebi, `getter` methodu kullanılmadan sadece `@property` decorator'u kullanılarak oluşturulan property'lerde `fget` methoduna tanımlanacak fonksiyon otomatik olarak  `@property` decorator'unun hemen altındaki instance method oluyor. `var.sayı` kodunun `'None'` değerini döndürmesi bunu kanıtlıyor çünkü `fget` methoduna tanımlanan `sayı` fonksiyonunda `return self._sayı` kodu yok. `getter` property methodu ile uğraşmadan sadece `@property` decorator'u kullanarak `fget` methoduna tanımlanacak fonksiyonun Python tarafından otomatik halledilmesini istiyorsanız, yukarıdaki kodu aşağıdaki gibi yazabilirsiniz:   
```py
class Class():
    def __init__(self):
        self._sayı = 0

    @property
    def sayı(self):
        return self._sayı

var = Class()
print(var.sayı) # Output: 0
print(var._sayı) # Output: 0
```

### `setter` Methodu:
Bir class'ın içinde tanımlı olan instance method üzerinde `setter` property methodunu kullanırsanız, bu instance method, ilgili property objesinin `fset` methodunda tanımlı, **write** olarak isimlendirilmiş **değer atama** işlemini gerçekleştiren fonksiyon olarak varlığını sürdürür (bundan sonra 'değer atama' işleminden'den 'write işlemi' olarak bahsedilecek). Örnek:
```py
class Class():
    def __init__(self):
        self._sayı = 0

    @property
    def sayı(self): # Buna "1. sayı fonksiyonu" diyelim
        return self._sayı

    @sayı.setter
    def sayı(self, yeni_değer): # Buna "2. sayı fonksiyonu" diyelim
        print("Write işleminden sorumlu fonksiyon çalıştı...")
        self._sayı = yeni_değer
        return self._sayı

var = Class()
print(var.sayı) # Output: 0
print(var._sayı) # Output: 0
var.sayı = 1 # Output: Write işleminden sorumlu fonksiyon çalıştı...
print(var.sayı) # Output: 1
print(var._sayı) # Output: 1
```
Gördüğünüz gibi `@property` decorator'u ile oluşturduğumuz `sayı` adındaki property objesi tanımladık. `sayı` property objesinin read işleminden sorumlu fonksiyonu, `@property` decorator'unun hemen altındaki 1. `sayı` fonksiyonu olarak belirlenmiş ve `fget` methoduna tanımlanmıştır. `sayı` property objesinin write işleminden sorumlu fonksiyonu da `@sayı.setter` decorator'ının hemen altındaki 2. `sayı` fonksiyonu olarak belirlenmiş ve `fset` methoduna tanımlanmıştır. Kanıtı:

<img src="https://i.ibb.co/k6RTYSB/image.png" alt="image" border="0">

Böylece; `@{Property_object_name}.setter` formatındaki decorator'u kullanarak, `{Property_object_name}` kısmında belirttiğimiz property objesinin write işleminden sorumlu olmasını istediğimiz instance methodu, `{Property_object_name}` kısmında belirttiğimiz property objesinin `fset` methoduna atabildiğiniz öğrendik.

`Class` class'ından `sayı` property'si, `var` instance'ında `sayı` adında bir attribute olarak bulunuyor (nedenini daha önce anlattım). Kanıtı:

<img src="https://i.ibb.co/WFzdc0V/image.png" alt="image" border="0">

Gördüğünüz gibi `var` instance'ında bulunan `sayı` attribute'unun değeri, `_sayı` attribute'undaki gibi `0`'dır. Bunun böyle olmasının nedenini `getter` methodunda anlattık. `var` instance'ında bulunan `sayı` attribute'unun değerini değiştirmek için `var.sayı = 1` kodunu çalıştırırsak, `fset` methoduna tanımlı, write işleminden sorumlu fonksiyon çalışır (çalıştığını "Write işleminden sorumlu fonksiyon çalıştı..." stringinin yazdırılmasından anlayabilirsiniz) ve hem `sayı` attribute'unun değerini hem de bu fonksiyonun içerdiği kodlar ile `_sayı` attribute'unun değerini `1` olarak değiştirir. Kanıtı:

<img src="https://i.ibb.co/JzGsdmw/image.png" alt="image" border="0">

Buradan, write işleminden sorumlu `def sayı(self, yeni_değer)` fonksiyonunda bulunan `yeni_değer` parametresinin write işlemi için önemli olduğunu çünkü `var.sayı = 1` kodundaki `1` value'sunun `yeni_değer` parametresine argüman olarak verildiğini çıkarabiliriz. Bu örnek koddan, write işleminden sorumlu fonksiyonu `def {Property_object_name}(self, new_value):` formatında tanımlayacağımızı ve `new_value` parametresinin ne işe yaradığını öğrenmiş olduk.

Property'lerde write işlemi **backwards compatibility** (geriye dönük uyumluluk) konusunda avantaj sağlar. Örnek:
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
Programınızda tanımladığınız bir class içindeki bir attribute'un isimlerini sonradan değiştirseniz, programınızın eski versiyonunu kullanan kişiler için sıkıntı yaratmış olursunuz. Örneğin `self.veri` attribute'u programınızın eski versiyonunda `self.data` isminde tanımlıysa, `self.data` attribute'unun ismini `self.veri` olarak değiştirdiğiniz zaman, programınızın eski versiyonunu kullanan kullanıcılar `self.veri` attribute'unu `self.data` zannettikleri için programlarını yanlış yazıp hata alabilirler. Bu sorunun önüne geçmek için yukarıdaki kodda olduğu gibi, `self.veri` attribute'u üzerinde read ve write işlemleri yapabilen `data` isminde bir property tanımlayabilirsiniz. Bu sayede programınızda **backwards compatibility** (geriye dönük uyumluluk) sağlamış olursunuz.

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
Gördüğünüz gibi `sayı` attribute'una çift sayı değeri atamaya çalışınca, değer atama işlemi gerçekleşmiyor ve `sayı` attribute'unun değeri değişmiyor çünkü `else` bloğunda `return self.sayı` kodu yok.

`setter` methodunun birçok alanda hayat kurtarabilir. Bir tane örnek verelim:
```py
class Class():
    all_instances = []
    def __init__(self, name):
        self.instace_name = name
        self.add_instance()

    def add_instance(self):
        print(f"'{self.instace_name}' adlı instnace eklendi.")
        self.all_instances.append(self.instace_name)

    @classmethod
    def show_all_instance(cls):
        print("All Instances:", end=" ")
        for member in cls.all_instances:
            if member == cls.all_instances[-1]:
                print(member)
            else:
                print(member, end=", ")

var1 = Class("AAA") # Output: 'AAA' adlı instnace eklendi.
var2 = Class("BBB") # Output: 'BBB' adlı instnace eklendi.
Class.show_all_instance() # Output: All Instances: AAA, BBB

var1.instace_name = "CCC"
Class.show_all_instance() # Output: All Instances: AAA, BBB
print(var1.instace_name) # Output: CCC
```
Gördüğünüz gibi main class'dan türetilen instance'ların isimlerini bir class attribute'da depolayan ve `show_all_instance()` class methodu ile bu isimleri listeleyen bir program yazdık. Ama bir sorun var. Yukarıda da gördüğünüz gibi `var1` instance'ının ismini değiştirirseniz, bu değişiklik sadece `var1` instance'ında geçerli olacağı için main class bu değişiklikten etkilenmez ve dolayısı ile `all_instances` listesinin içeriği aynı kalır. Bu sorunun önüne geçebilmek için isim değiştirme işlemini yapan bir fonksiyon tanımlayabilir ya da property'lerden yararlanabilirsiniz. Önce isim değiştirme işlemini yapan bir fonksiyon tanımlayalım:
```py
class Class():
    all_instances = []
    def __init__(self, name):
        self._instace_name = name
        self.add_instance()

    def add_instance(self):
        print(f"'{self._instace_name}' adlı instnace eklendi.")
        self.all_instances.append(self._instace_name)

    @classmethod
    def show_all_instance(cls):
        print("All Instances:", end=" ")
        for member in cls.all_instances:
            if member == cls.all_instances[-1]:
                print(member)
            else:
                print(member, end=", ")

    def change_instance_name(self, new_name):
        old_name = self._instace_name
        self.all_instances[self.all_instances.index(self._instace_name)] = new_name
        print(f"{old_name} -> {new_name}")

var1 = Class("AAA") # Output: 'AAA' adlı instnace eklendi.
var2 = Class("BBB") # Output: 'BBB' adlı instnace eklendi.
Class.show_all_instance() # Output: All Instances: AAA, BBB
var1.change_instance_name("CCC") # Output: AAA -> CCC
Class.show_all_instance() # Output: All Instances: CCC, BBB
```
Artık bir instance'ın ismini değiştirmek için `change_instance_name` instance methodunu kullanabilirsiniz. Bu sayede `instace_name` instance attribute'u ile işimiz kalmadığı için bunu semi_private member haline getirdik. İlla `var1` instance'ının ismini `var1.instace_name = "CCC"` koduyla değiştirmek istiyorum diyorsanız, property'lerden yararlanabilirsiniz. Örnek:
```py
class Class():
    all_instances = []
    def __init__(self, name):
        self._instace_name = name
        self.add_instance()

    def add_instance(self):
        print(f"'{self._instace_name}' adlı instnace eklendi.")
        self.all_instances.append(self._instace_name)

    @classmethod
    def show_all_instance(cls):
        print("All Instances:", end=" ")
        for member in cls.all_instances:
            if member == cls.all_instances[-1]:
                print(member)
            else:
                print(member, end=", ")

    @property
    def instace_name(self):
        return self._instace_name

    @instace_name.setter
    def instace_name(self, new_name):
        old_name = self._instace_name
        self._instace_name = new_name
        self.all_instances[self.all_instances.index(old_name)] = new_name
        print(f"{old_name} -> {new_name}")
        return self._instace_name

var1 = Class("AAA")
var2 = Class("BBB")
Class.show_all_instance() # Output: All Instances: AAA, BBB

var1.instace_name = "CCC" # Output. AAA -> CCC
Class.show_all_instance() # Output: All Instances: CCC, BBB
var1.show_all_instance() # Output: All Instances: CCC, BBB
var2.show_all_instance() # Output: All Instances: CCC, BBB
print(var1.instace_name) # Output: CCC
```
Gördüğünüz gibi `var1.instace_name = "CCC"` kodunu kullanarak hem `var1` instance'ının ismini değiştirebildik hem de `all_instances` içeriğini her yerde güncelleyebildik.

### `deleter` Methodu:
Bir class'ın içinde tanımlı olan instance method üzerinde `deleter` property methodunu kullanırsanız, bu instance method, ilgili property objesinin `fdel` methodunda tanımlı, **delete** olarak isimlendirilmiş **değer silme** işlemini gerçekleştiren fonksiyon olarak varlığını sürdürür (bundan sonra 'değer silme' işleminden'den 'delete işlemi' olarak bahsedilecek). Örnek:
```py
class Class():
    def __init__(self):
        self._sayı = 0

    @property
    def sayı(self): # Buna "1. sayı fonksiyonu" diyelim
        return self._sayı

    @sayı.deleter
    def sayı(self): # Buna "2. sayı fonksiyonu" diyelim
        print("Delete işleminden sorumlu fonksiyon çalıştı...")
        del self._sayı

var = Class()
print(var.sayı) # Output: 0
print(var._sayı) # Output: 0
del var.sayı # Output: Delete işleminden sorumlu fonksiyon çalıştı...
print(var.sayı) # AttributeError: 'Class' object has no attribute '_sayı'
```
Gördüğünüz gibi `@property` decorator'u ile oluşturduğumuz `sayı` adındaki property objesi tanımladık. `sayı` property objesinin read işleminden sorumlu fonksiyonu, `@property` decorator'unun hemen altındaki 1. `sayı` fonksiyonu olarak belirlenmiş ve `fget` methoduna tanımlanmıştır. `sayı` property objesinin delete işleminden sorumlu fonksiyonu da `@sayı.deleter` decorator'ının hemen altındaki 2. `sayı` fonksiyonu olarak belirlenmiş ve `fdel` methoduna tanımlanmıştır. Kanıtı:

<img src="https://i.ibb.co/8X638hH/image.png" alt="image" border="0">

Böylece; `@{Property_object_name}.deleter` formatındaki decorator'u kullanarak, `{Property_object_name}` kısmında belirttiğimiz property objesinin delete işleminden sorumlu olmasını istediğimiz instance methodu, `{Property_object_name}` kısmında belirttiğimiz property objesinin `fdel` methoduna atabildiğiniz öğrendik.

`Class` class'ından `sayı` property'si, `var` instance'ında `sayı` adında bir attribute olarak bulunuyor (nedenini daha önce anlattım). Kanıtı:

<img src="https://i.ibb.co/WFzdc0V/image.png" alt="image" border="0">

Gördüğünüz gibi `var` instance'ında bulunan `sayı` attribute'unun değeri, `_sayı` attribute'undaki gibi `0`'dır. Bunun böyle olmasının nedenini `getter` methodunda anlattık. `var` instance'ında bulunan `sayı` attribute'unun değerini silmek için `del var.sayı` kodunu çalıştırırsak, `fdel` methoduna tanımlı, delete işleminden sorumlu fonksiyon çalışır (çalıştığını "Delete işleminden sorumlu fonksiyon çalıştı..." stringinin yazdırılmasından anlayabilirsiniz) ve `_sayı` attribute'unu bellekten siler. Kanıtı:

<img src="https://i.ibb.co/Lgz2kTk/image.png" alt="image" border="0">

Gördüğünüz gibi `_sayı` variable'ı bellekten silindi. `_sayı` variable'ı bellekten silindiği için `fget` methodunda tanımlı, read işleminden sorumlu fonksiyonun içerdiği `return self._sayı` kodundaki `self._sayı` kodu, `_self` attribute'u bellekten silindiği için aşağıdaki hatayı yükseltir:
```
Traceback (most recent call last):
  File "c:\Users\HP\.vscode\extensions\ms-python.python-2021.6.944021595\pythonFiles\lib\python\debugpy\_vendored\pydevd\_pydevd_bundle\pydevd_resolver.py", line 193, in _get_py_dictionary
    attr = getattr(var, name)
  File "d:\my_folder\education\software\software_lessons\python\python_tutorial\main\.md\tempCodeRunnerFile.py", line 7, in sayı
    return self._sayı
AttributeError: 'Class' object has no attribute '_sayı'
```
`return` statement bu hata mesajını döndürdüğü için bu hata mesajı `sayı` attribute'unun string type value'su olur:
```
sayı: 'Traceback (most recent call last):\n  File "c:\\Users\\HP\\.vscode\\extensions\\ms-python.python-2021.6.944021595\\pythonFiles\\lib\\python\\debugpy\\_vendored\\pydevd\\_pydevd_bundle\\pydevd_resolver.py", line 193, in _get_py_dictionary\n    attr = getattr(var, name)\n  File "d:\\my_folder\\education\\software\\software_lessons\\python\\python_tutorial\\main\\.md\\tempCodeRunnerFile.py", line 7, in sayı\n    return self._sayı\nAttributeError: \'Class\' object has no attribute \'_sayı\'\n'
```
`print(var.sayı)` kodu ile `sayı` propery'sinin `fget` methodunda tanımlı, read işleminden sorumlu fonksiyonu çalıştırdığımız için yine `return self._sayı` kodu yüzünden `AttributeError: 'Class' object has no attribute '_sayı'` hatası yükseltilir.

### Decorator'ların Saçmalığı
Şimdiye kadar read, write ve delete işlemlerini gerçekleştirmesi için `fget`, `fset` ve `fdel` methodlarına atadığımız fonksiyonların aynı isme (identifier) sahip olduğunu farketmişsinizdir. Örnek:
```py
class Class():
    def __init__(self):
        self._sayı = 0
    
    @property
    def sayı(self):
        pass

    @sayı.getter
    def sayı(self):
        return self._sayı

    @sayı.setter
    def sayı(self, yeni_değer):
        self._sayı = yeni_değer
        return self._sayı

    @sayı.deleter
    def sayı(self):
        del self._sayı

var = Class()
```

<img src="https://i.ibb.co/b7GT6L5/image.png" alt="image" border="0">

Gördüğünüz gibi `sayı` ismindeki property'nin `fget`, `fset` ve `fdel` methodlarına ilgili `sayı` ismindeki fonksiyonlar atandı. Peki bu fonksiyonları isimleri `sayı` yerine farklı farklı şeyler olsaydı? Örnek:
```py
class Class():
    def __init__(self):
        self._sayı = 0
    
    @property
    def sayı(self):
        pass

    @sayı.getter
    def sayı_get(self):
        return self._sayı

    @sayı.setter
    def sayı_set(self, yeni_değer):
        self._sayı = yeni_değer
        return self._sayı

    @sayı.deleter
    def sayı_del(self):
        del self._sayı

var = Class()
```

<img src="https://i.ibb.co/BtqsGTs/image.png" alt="image" border="0">

Gördüğünüz gibi tam bir karmaşa oldu. Burada sorulması gereken soru; "Madem `getter`, `setter` ve `deleter` methodları etkilediği fonksiyonların isimlerine sahip yeni property objeleri oluşmasına neden olacaktı, neden `@sayı.getter`, `@sayı.setter` ve `@sayı.deleter` decorator'larında `sayı` kelimesi var? Buradaki `sayı` kelimesi, `getter`, `setter` ve `deleter` methodlarının etkilediği fonksiyonların `sayı` property'sinin `fget`, `fset` ve `fdel` methodlarına atanmasına vesile olmuyor da neden yeni property objeleri oluşmasına vesile oluyor?" Buna bir cevap henüz bulamadım. Bu property objelerini daha iyi anlamak için read, write ve delete yetkilerinden hangilerine sahip olduklarına bakmakta fayda var:

- `@property` decorator'ı ile oluşturulan property objesinde sadece `fget` methodu tanımlıdır. Kanıtı:

    <img src="https://i.ibb.co/qdH8YsP/image.png" alt="image" border="0">

    Böyle olmasının sebebi, daha önce de anlattığım `@property` decorator'ı ile decore edilen fonksiyonun otomatik olarak `fget` methoduna atanmasıdır. `fget` methoduna atanmış, read işleminden sorumlu fonksiyonda `return self._sayı` kodu olmadığı için (daha önce de anlattığım gibi) `var` instance'ındaki `sayı` attribute'unun value'su `'None'` olur.

    <img src="https://i.ibb.co/dQDzsGq/image.png" alt="image" border="0">

- `@sayı.getter` decorator'ı ile oluşturulan property objesinde sadece `fget` methodu tanımlıdır. Kanıtı:

    <img src="https://i.ibb.co/7Q86NwN/image.png" alt="image" border="0">

    Main class'daki her property objesinin, bu main class'dan türetilen instance'da kendi adında bir attribute oluşturduğunu biliyoruz. Kanıtı:
    
    <img src="https://i.ibb.co/BtqsGTs/image.png" alt="image" border="0">
    
    Burada dikkat edilmesi gereken şey; `sayı_get` property'sinin `fget` methoduna atanmış, read işleminden sorumlu fonksiyon, `sayı`, `sayı_set` ve `sayı_del` property'lerinin `fget` methoduna atanmış, read işleminden sorumlu fonksiyondan farklı bir fonksiyon objesidir (deneyip görebilirsiniz). Bu yüzden `var` instance'ındaki `sayı`, `sayı_set` ve `sayı_del` attribute'larının value'su `'None'` iken `sayı_get` attribute'unun value'su `_sayı` attribute'unun value'su ile aynı ve bağlantılıdır. Çünkü `sayı`, `sayı_set` ve `sayı_del` property'lerinin `fget` methoduna atanmış read işleminden sorumlu fonksiyonda `return self._sayı` kodu olmadığından bu property'ler read işlemini gerçekleştirip `_sayı` attribute'unun value'suna erişemez ama `sayı_get` property'sinin `fget` methoduna atanmış read işleminden sorumlu fonksiyonda `return self._sayı` kodu olduğundan `sayı_get` property'si, read işlemini gerçekleştirip `_sayı` attribute'unun value'suna erişebilir. Kanıtı:

    <img src="https://i.ibb.co/gTV2fFh/image.png" alt="image" border="0">

- `@sayı.setter` decorator'ı ile oluşturulan property objesinde hem `fset` hem de `fget` methodları tanımlıdır. Kanıtı:

    <img src="https://i.ibb.co/TPstsLF/image.png" alt="image" border="0">

    Burada dikkat çeken şey, `sayı_set` property'sinin `fget` methodunda tanımlı read işleminden sorumlu fonksiyon objesi ile `sayı` property'sinin `fget` methodunda tanımlı read işleminden sorumlu fonksiyon objesinin aynı olmasıdır. Nedenini bilmesem de buradan, `sayı_set` property'sinin `sayı` property'sinden bir şekilde etkilendiği sonucu çıkarılabilir.
    
    `sayı_set` ve `sayı` iki farklı property objesi olduğu için `var` instance'ında `sayı_set` ve `sayı` adında iki farklı attribute oluşmasına neden oluyorlar. Kanıtı:

    <img src="https://i.ibb.co/7RYjdwF/image.png" alt="image" border="0">

    `sayı_set` property'sinin `fget` methoduna atanmış, read işleminden sorumlu fonksiyonda `return self._sayı` kodu olmadığı için (daha önce de anlattığım gibi) `var` instance'ındaki `sayı_set` attribute'unun value'su `'None'` olur. `var.sayı_set = 1` koduyla `sayı_set` property'sinin `fset` methoduna atanmış, write işleminden sorumlu fonksiyonunu çalıştırınca `_sayı` ve dolayısıyla `sayı_get` value'ları `1` olarak güncellense bile `sayı_set` property'sinin `fget` methoduna atanmış, read işleminden sorumlu fonksiyon işlevini yerine getiremediği için `var` instance'ındaki `sayı_set` attribute'unun value'su `'None'` olarak kalıyor. Kanıtı:

    <img src="https://i.ibb.co/cvSLxhv/image.png" alt="image" border="0">

- `@sayı.deleter` decorator'ı ile oluşturulan property objesinde hem `fdel` hem de `fget` methodları tanımlıdır. Kanıtı:

    <img src="https://i.ibb.co/vBfR5cq/image.png" alt="image" border="0">

    Burada dikkat çeken şey, `sayı_del` property'sinin `fget` methodunda tanımlı read işleminden sorumlu fonksiyon objesi ile `sayı` property'sinin `fget` methodunda tanımlı read işleminden sorumlu fonksiyon objesinin aynı olmasıdır. Nedenini bilmesem de buradan, `sayı_del` property'sinin `sayı` property'sinden bir şekilde etkilendiği sonucu çıkarılabilir.
    
    `sayı_del` ve `sayı` iki farklı property objesi olduğu için `var` instance'ında `sayı_del` ve `sayı` adında iki farklı attribute oluşmasına neden oluyorlar. Kanıtı:

    <img src="https://i.ibb.co/5vFSMJw/image.png" alt="image" border="0">

    `sayı_del` property'sinin `fget` methoduna atanmış, read işleminden sorumlu fonksiyonda `return self._sayı` kodu olmadığı için (daha önce de anlattığım gibi) `var` instance'ındaki `sayı_del` attribute'unun value'su `'None'` olur. `del var.sayı_del` koduyla `sayı_del` property'sinin `fdel` methoduna atanmış, delete işleminden sorumlu fonksiyonunu çalıştırınca `_sayı` attribute'u bellekten siliniz. `_sayı` attribute'u bellekten silindiği için (daha önce de anlattığım gibi) `sayı_get` property'sinin `fget` methoduna atanmış, read işleminden sorumlu fonksiyondaki `return self._sayı` kodunun `self._sayı` kısmı aşağıdaki hatayı yükseltir.
    ```
        Traceback (most recent call last):
    File "c:\Users\HP\.vscode\extensions\ms-python.python-2021.6.944021595\pythonFiles\lib\python\debugpy\_vendored\pydevd\_pydevd_bundle\pydevd_resolver.py", line 193, in _get_py_dictionary
        attr = getattr(var, name)
    File "d:\my_folder\education\software\software_lessons\python\python_tutorial\main\.md\tempCodeRunnerFile.py", line 11, in sayı_get
        return self._sayı
    AttributeError: 'Class' object has no attribute '_sayı'
    ```
    `return` statement bu hata mesajını döndürdüğü için bu hata mesajı `sayı_get` attribute'unun string type value'su olur:

    <img src="https://i.ibb.co/thLB7CY/image.png" alt="image" border="0">

    ```
    sayı_get: 'Traceback (most recent call last):\n  File "c:\\Users\\HP\\.vscode\\extensions\\ms-python.python-2021.6.944021595\\pythonFiles\\lib\\python\\debugpy\\_vendored\\pydevd\\_pydevd_bundle\\pydevd_resolver.py", line 193, in _get_py_dictionary\n    attr = getattr(var, name)\n  File "d:\\my_folder\\education\\software\\software_lessons\\python\\python_tutorial\\main\\.md\\tempCodeRunnerFile.py", line 11, in sayı_get\n    return self._sayı\nAttributeError: \'Class\' object has no attribute \'_sayı\'\n'
    ```

Gördüğünüz gibi `@property` decorator'unun ve bu decorator'un `getter`, `setter`, `deleter` methodlarının böyle saçma davranışları olduğu için bu decorator'lar, bir property objesi yaratmanın en iyi yöntemi değildir. Bu yüzden bir property objesi yaratmak istediğinizde bu decorator'ları kullanmak terine `property()` fonksiyonunu tercih etmelisiniz.

## `property(fget=None, fset=None, fdel=None, doc=None)` Fonksiyonu
`property()` fonksiyonu, `fget`, `fset` ve `fdel` parametrelerine read, write ve delete işlemlerini gerçekleştirecek fonksiyon objelerini argüman olarak verip bir property oluşturabilmenizi sağlar. Örnek:
```py
class Class():
    def __init__(self):
        self._sayı = 0

    def sayı_get(self):
        return self._sayı

    def sayı_set(self, yeni):
        print("sayı_set çalıştı...")
        self._sayı = yeni
        return self._sayı

    def sayı_del(self):
        print("sayı_del çalıştı...")
        del self._sayı

    sayı = property(fget = sayı_get, fset = sayı_set, fdel = sayı_del, doc="Sayı Property'si")

var = Class()
print(Class.sayı.__doc__) # Output: Sayı Property'si
print(var.sayı) # Output: 0
var.sayı = 1 # Output: sayı_set çalıştı...
print(var.sayı) # Output: 1
del var.sayı # Output: sayı_del çalıştı...
print(var.sayı) # AttributeError: 'Class' object has no attribute '_sayı'
```
Gördüğünüz gibi read, write ve delete işlemleri için kullanılan fonksiyonların isimleri farklı olsa da hepsine `sayı` property objesi üzerinden erişip kullanabiliyoruz ve decorator'lardaki gibi saçma davranışlarla karşılaşmıyoruz.

**Not:** Global scope'da da property objesi yaratabiliriz. Örnek:
```py
sayı = property(doc="Sayı Property'si")
print(type(sayı)) # Output: <class 'property'>
print(sayı.__doc__) # Output: Sayı Property'si
```
Yukarıdaki kodda gördüğünüz gibi, `property()` fonksiyonundaki `doc` parametresine verilen argüman, bu fonksiyon ile oluşturulan property'nin `__doc__` attribute'una atanır. Kanıtı:

<img src="https://i.ibb.co/6Y9kFQw/image.png" alt="image" border="0">

`__doc__` attribute'u genelde ilgili obje hakkında bilgi vermek için kullanılan bir şeydir. Örneğin integer type objelerin `__doc__` attribute'una bakalım:
```py
print(int.__doc__) # ya da `print((1).__doc__)`
```
**Output:**
```
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4
```

**Not:** Decorator'ları anlatırken, decorator ile decore edilen fonksiyonlar, property objesinin `fget`, `fset` ve `fdel` methodlarına atanıp main class'ın `function variables` kısmından silindiği için `Class.sayı_get()` şeklinde kullanamadığımızı biliyoruz. Ama `property()` fonksiyonu ile oluşturulan property'ler için bu geçerli değildir. Örnek:
```py
class Class():
    def __init__(self):
        self._sayı = 0

    def sayı_get(self):
        return self._sayı

    def sayı_set(self, yeni):
        print("sayı_set çalıştı...")
        self._sayı = yeni
        return self._sayı

    def sayı_del(self):
        print("sayı_del çalıştı...")
        del self._sayı

    sayı = property(fget = sayı_get, fset = sayı_set, fdel = sayı_del, doc="Sayı Property'si")

var = Class()
print(var.sayı_get()) # Output: 0
var.sayı_set(1) # Output: sayı_set çalıştı...
print(var.sayı_get()) # Output: 1
var.sayı_del() # Output: sayı_del çalıştı...
print(var.sayı_get()) # AttributeError: 'Class' object has no attribute '_sayı'
```
Gördüğünüz gibi `sayı` property objesinin `fget`, `fset` ve `fdel` methodlarına atanan fonksiyonlar main class'ın `function variables` kısmından silinmediği için bu main class'dan oluşturulan `var` instance'da bu fonksiyonlara sahip oluyor. Kanıtı:

<img src="https://i.ibb.co/N7sKkk9/image.png" alt="image" border="0">

<img src="https://i.ibb.co/VVBcH9Y/image.png" alt="image" border="0">

Bu sayede `var` instance'ında isterseniz property'i isterseniz bu instance methodları kullanın. Bu instance methodların böyle kullanılmasını istemiyorsanız, kullanıcının sadece property objesini kullanmasını istiyorsanız, bu instance methodları private hale getirebilirsiniz. Örnek:
```py
class Class():
    def __init__(self):
        self._sayı = 0

    def __sayı_get(self):
        return self._sayı

    def __sayı_set(self, yeni):
        print("sayı_set çalıştı...")
        self._sayı = yeni
        return self._sayı

    def __sayı_del(self):
        print("sayı_del çalıştı...")
        del self._sayı

    sayı = property(fget = __sayı_get, fset = __sayı_set, fdel = __sayı_del, doc="Sayı Property'si")

var = Class()
```
Bu private instanca methodların `Class` class'ında ve `var` instance'ında nasıl bulunduğuna bakalım:

<img src="https://i.ibb.co/gZhjpKG/image.png" alt="image" border="0">

<img src="https://i.ibb.co/0s8gjh8/image.png" alt="image" border="0">

Bu görüntü size karmaşık gelmiş olabilir ama sonuç olarak bu instance methodları private hale getirdiğimiz için ilk yazdığımız koddaki gibi bu instance methodları `var.sayı_get()`, `var.sayı_set(1)` ya da `var.sayı_del()` gibi kullanamayız. Örnek:
```py
class Class():
    def __init__(self):
        self._sayı = 0

    def __sayı_get(self):
        return self._sayı

    def __sayı_set(self, yeni):
        print("sayı_set çalıştı...")
        self._sayı = yeni
        return self._sayı

    def __sayı_del(self):
        print("sayı_del çalıştı...")
        del self._sayı

    sayı = property(fget = __sayı_get, fset = __sayı_set, fdel = __sayı_del, doc="Sayı Property'si")

var = Class()

print(var.sayı_get()) # AttributeError: 'Class' object has no attribute 'sayı_get'
var.sayı_set(1) # AttributeError: 'Class' object has no attribute 'sayı_set'
print(var.sayı_get()) # AttributeError: 'Class' object has no attribute 'sayı_get'
var.sayı_del() # AttributeError: 'Class' object has no attribute 'sayı_del'
print(var.sayı_get()) # AttributeError: 'Class' object has no attribute 'sayı_get'
```

**Not:** `property()` fonksiyonunun `fget`, `fset` ve `fdel` parametrelerine girilen read, write ve delete işlemlerini gerçekleştirecek fonksiyonlar instance method değil, class method ise, oluşturulan property'yi kullanamazsınız. Örnek:
```py
class Class():
    _sayı = 0
    def __init__(self):
        self._sayı

    @classmethod
    def sayı_get(cls):
        return cls._sayı

    @classmethod
    def sayı_set(cls, yeni):
        print("sayı_set çalıştı...")
        cls._sayı = yeni
        return cls._sayı

    @classmethod
    def sayı_del(cls):
        print("sayı_del çalıştı...")
        del cls._sayı

    sayı = property(fget = sayı_get, fset = sayı_set, fdel = sayı_del, doc="Sayı Property'si")

var = Class()
print(var.sayı) # Output: TypeError: 'classmethod' object is not callable
var.sayı = 1 # Output: TypeError: 'classmethod' object is not callable
del var.sayı # Output: TypeError: 'classmethod' object is not callable
```
Bu durumun sebebi bir instance üzerinde bu işlemleri yapmaya çalışmak değildir. Aynı işlemleri doğrudan `Class` class'ının üzerinde de yapamazsınız.
```py
class Class():
    _sayı = 0
    def __init__(self):
        self._sayı

    @classmethod
    def sayı_get(cls):
        return cls._sayı

    @classmethod
    def sayı_set(cls, yeni):
        print("sayı_set çalıştı...")
        cls._sayı = yeni
        return cls._sayı

    @classmethod
    def sayı_del(cls):
        print("sayı_del çalıştı...")
        del cls._sayı

    sayı = property(fget = sayı_get, fset = sayı_set, fdel = sayı_del, doc="Sayı Property'si")

print(Class.sayı.fget()) # Output: TypeError: 'classmethod' object is not callable
print(Class.sayı.fset()) # Output: TypeError: 'classmethod' object is not callable
print(Class.sayı.fdel()) # Output: TypeError: 'classmethod' object is not callable
```
**!Bu Hatanın Sebebi Öğrenince Buraya Yaz!**

Bu class method'lara property üzerinden erişemesek bile main class ya da main class'dan türetilmiş bir instance üzerinden doğrudan erişebiliriz. Örnek:
```py
class Class():
    _sayı = 0
    def __init__(self):
        self._sayı

    @classmethod
    def sayı_get(self):
        return self._sayı

    @classmethod
    def sayı_set(self, yeni):
        print("sayı_set çalıştı...")
        self._sayı = yeni
        return self._sayı

    @classmethod
    def sayı_del(self):
        print("sayı_del çalıştı...")
        del self._sayı

    sayı = property(fget = sayı_get, fset = sayı_set, fdel = sayı_del, doc="Sayı Property'si")

var = Class()
print(Class.sayı_get()) # Output: 0
print(var.sayı_get()) # Output: 0

Class.sayı_set(1) # Output: sayı_set çalıştı...
print(Class.sayı_get()) # Output: 1

var.sayı_set(2) # Output: sayı_set çalıştı...
print(var.sayı_get()) # Output: 2

Class.sayı_del() # Output: sayı_del çalıştı...
print(Class.sayı_get()) # AttributeError: type object 'Class' has no attribute '_sayı'

var.sayı_del() # Output: sayı_del çalıştı...
print(var.sayı_get()) # AttributeError: type object 'Class' has no attribute '_sayı'
```