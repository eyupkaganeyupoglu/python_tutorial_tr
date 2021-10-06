# İçindekiler

- [Class Members](#1)
    - [Public Members (Aleni Üyeler)](#1.1)
    - [Private Members (Gizli Üyeler)](#1.2)
    - [Semi-private Members (Yarı-gizli Üyeler)](#1.3)

<h1 id="1">Class Members</h1>

Bir class'ın içindeki attribute'lar, variable'lar, method'lar vb. diğer öğelerin her biri bir class member'dır (sınıf üyesidir). Class member'lar üçe ayrılır:
- Aleni Üyeler (Public Members)
- Gizli Üyeler (Private Members)
- Yarı-Gizli Üyeler (Semi-Private Members)

<h2 id="1.1">Public Members (Aleni Üyeler)</h2>

Bir class member'a class dışından normal yöntemlerle erişilebiliyorsa, bu class member'a **public member** denir. Örnek:
```py
class A():
    c_attri = 'Class Attribute'

    def __init__(self),:
        self.i_attri = 'Instance Attribute'

    def instance_method(self):
        print(f"instance_method() Çalıştı! | {self.i_attri}")

    @classmethod
    def class_method(cls):
        print(f"class_method() Çalıştı! | {cls.c_attri}")

    @staticmethod
    def static_method():
        s_attri = 'Static Attribute'
        print(f"static_method() Çalıştı! | {s_attri}")

var = A()
print(dir(var)) # Output: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'c_attri', 'class_method', 'i_attri', 'instance_method', 'static_method']

# Normal yöntemlerden kasıt:
print(A.c_attri) # Output: Class Attribute
var.instance_method() # Output: instance_method() Çalıştı! | Instance Attribute
var.class_method() # Output: class_method() Çalıştı! | Class Attribute
var.static_method() # Output: static_method() Çalıştı! | Static Attribute
```
`dir(A)` fonksiyonu bize `A` class'ı içindeki bütün class member'ları verir. Bu class member'lara yukarıdaki gibi **normal yöntemlerle doğrudan** erişebildiği için bu öğeler public member'dır. Gördüğünüz gibi buradaki `c_attri`, `i_attri`, `instance_method`, `class_method`, `static_method` ve diğer method ve attribute'lar public member'dır.

**Not:** Private member olarak tanımlanmamış bütün class member'lar (semi-private ve public member'lardan bahsediyorum), Python tarafından otomatik olarak public member olarak kabul edilir.

<h2 id="1.2">Private Members (Gizli Üyeler)</h2>

Class'ın iç işlerini ilgilendirdiği için dışarıdan erişimine gerek olmayan ya da dışarıdan erişilirse programda sorunlara neden olabilecek (dışarıdan erişilmesi istenmeyen) class member'ların isimlerinin önüne (yani en soluna) **en az 2** tane, sonuna (yani en sağına) **en fazla 1** tane alt çizgi (`_` underscore) koyarak bu class member'ları **private member**'lar haline getirebilirsiniz. Private member'lara normal yöntemlerle doğrudan erişilemez. Örnekler:
```py
class A():
#      Attribute        Attribute           Class Member  
#        Name             Value                 Type      
    gizli            = "gizli"            # Public Member
    _gizli           = "_gizli"           # Public Member
    _gizli_          = "_gizli_"          # Public Member
    _gizli__         = "_gizli__"         # Public Member
    _gizli___        = "_gizli___"        # Public Member
    __gizli          = "__gizli"          # Private Member
    __gizli_         = "__gizli_"         # Private Member
    __gizli__        = "__gizli__"        # Public Member
    __gizli___       = "__gizli___"       # Public Member
    __gizli_gizli    = "__gizli_gizli"    # Private Member
    __gizli_gizli_   = "__gizli_gizli_"   # Private Member
    __gizli_gizli__  = "__gizli_gizli__"  # Public Member
    __gizli_gizli___ = "__gizli_gizli___" # Public Member
    ___gizli         = "___gizli"         # Private Member
    ___gizli_        = "___gizli_"        # Private Member
    ___gizli__       = "___gizli__"       # Public Member
    ___gizli___      = "___gizli___"      # Public Member

print(A().gizli) # Output: gizli
print(A().__gizli) # AttributeError: 'A' object has no attribute '__gizli'
```
Gördüğünüz gibi private member oluşturma kuralına uyan isimleri (identifier) Python private member olarak kabul ederken, bu kurala uymayanları public member olarak kabul ediyor.

Herhangi bir class objesi (method, attribute, property vs.) private member olarak tanımlanabilir. Örnekler:
```py
class A():
    __c_attri = 'Class Attribute'

    def __init__(self):
        self.__i_attri = 'Instance Attribute'

    def __instance_method(self):
        print(f"instance_method() Çalıştı! | {self.__i_attri}")

    @classmethod
    def __class_method(cls):
        print(f"class_method() Çalıştı! | {cls.__c_attri}")

    @staticmethod
    def __static_method():
        s_attri = 'Static Attribute'
        print(f"static_method() Çalıştı! | {s_attri}")

    __property_exp = property()

var = A()
for i in dir(var):
    if "_A" in i:
        print(i)
```
**Output:**
```
_A__c_attri
_A__class_method
_A__i_attri
_A__instance_method
_A__property_exp
_A__static_method
```

Private member'ları tanımlandıkları isimlerle (identifier) doğrudan çağıramazsınız çünkü bellekte tanımlandıkları isimlerle depolanmazlar. Yani private olarak tanımlanmış bir class member, class dışından tamamen erişilemez değildir. Bu durum Python'ın, private member'ları **Name Mangling** kullanarak farklı bir isimle (identifier) belleğe kaydetmesinden kaynaklanır. Python private member'ları `_{class_name}{private_class_member_name}` formatında oluşturulmuş isimlerle (identifier) belleğe kaydeder. Buna **Name Mangling (isim bulandırma)** denir. Örnekler:
```py
class A():
#      Attribute        Attribute            Class Member  |  Bellekteki
#        Name             Value                  Type      |     İsmi
    gizli            = "gizli"            # Public Member  | gizli
    _gizli           = "_gizli"           # Public Member  | _gizli
    _gizli_          = "_gizli_"          # Public Member  | _gizli_
    _gizli__         = "_gizli__"         # Public Member  | _gizli__
    _gizli___        = "_gizli___"        # Public Member  | _gizli___
    __gizli          = "__gizli"          # Private Member | _A__gizli
    __gizli_         = "__gizli_"         # Private Member | _A__gizli_
    __gizli__        = "__gizli__"        # Public Member  | __gizli__
    __gizli___       = "__gizli___"       # Public Member  | __gizli___
    __gizli_gizli    = "__gizli_gizli"    # Private Member | _A__gizli_gizli
    __gizli_gizli_   = "__gizli_gizli_"   # Private Member | _A__gizli_gizli_
    __gizli_gizli__  = "__gizli_gizli__"  # Public Member  | __gizli_gizli__
    __gizli_gizli___ = "__gizli_gizli___" # Public Member  | __gizli_gizli___
    ___gizli         = "___gizli"         # Private Member | _A___gizli
    ___gizli_        = "___gizli_"        # Private Member | _A___gizli_
    ___gizli__       = "___gizli__"       # Public Member  | ___gizli__
    ___gizli___      = "___gizli___"      # Public Member  | ___gizli___

print(A().gizli) # Output: gizli
print(A()._A__gizli) # Output: __gizli
print(A().__gizli) # AttributeError: 'A' object has no attribute '__gizli'
```
Gördüğünüz gibi private member'lara `A().__gizli` örneğindeki gibi erişemezsiniz çünkü bellekte bu isimde bir attribute yok.

**Not:** Private member'lara bu şekilde erişebilmemiz, private member'ları teknik olarak private yapmaz. Bu yüzden private member'ların doğru kullanımı name mangling ile bir nebze güvenceye alınmış ve kullanıcıların inisiyatifine bırakılmıştır.

Private member'lara class dışından normal yollarla doğrudan erişemesek bile, class'ın içinde kullanabiliriz. Örnek:
```py
class A():
    __gizli1 = "Private Member 1"
    __gizli2 = "Private Member 2"

    def yazdir1(self):
        print(self.__gizli1)
    
    def yazdir2(self):
        return self.__gizli2

A().yazdir1() # Output: Private Member 1
print(A().yazdir2()) # Output: Private Member 2
```
`A().yazdir1()` ve `print(A().yazdir2())` kodlarıyla bu private member'ların value'larına class dışından ulaşabilsek bile bu normal yollarla doğrudan bir erişim olmadığından, dolaylı yoldan (method aracılığıyla) bir erişim olduğundan bu class member'lar public member olarak kabul edilmez.

<h2 id="1.3">Semi-private Members (Yarı-gizli Üyeler)</h2>

Önüne (yani en soluna) bir tane alt çizgi (`_`) konularak oluşturulan isimlere (identifier) sahip class member'lara **Semi-Private Member**'lar denir.Ssemi-private member teknik olarak public member'dır. Yeni semi-private member'lar, Python kullanıcıların uydurduğu bir şeydir. Python kullanıcıları semi-private member'ları, bir class member'ın bellekteki ismini (identifier) değiştirmeden private member gibi kullanmak istediklerinde kullanmayı tercih eder.
```py
class A():
#      Attribute  Attribute     Class Member   |  Bellekteki
#        Name       Value           Type       |     İsmi
    gizli        = "gizli"   # Public Member   | gizli
    _gizli       = "_gizli"  # Public Member   | _gizli
    __gizli      = "__gizli" # Private Member  | _A__gizli

print(A().gizli) # Output: gizli
print(A()._gizli) # Output: _gizli
print(A()._A__gizli) # Output: __gizli
print(A().__gizli) # AttributeError: 'A' object has no attribute '__gizli'
```