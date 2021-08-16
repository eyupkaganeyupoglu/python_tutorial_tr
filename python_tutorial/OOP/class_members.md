# Class Members
Bir class'ın içindeki attribute'lar, variable'lar, method'lar vb. diğer öğelerin her biri bir class member'dır (sınıf üyesidir). Class member'lar üçe ayrılır:
- Aleni üyeler (public members)
- Gizli üyeler (private members)
- Yarı-gizli üyeler (semi-private members)

## Public Members (Aleni Üyeler)
Bir class member'a class dışından normal yöntemlerle erişilebiliyorsa, bu class member'a **public member** denir. `dir(Class)` fonksiyonu bize `Class` class'ı içindeki bütün class member'ları verir. Bu class member'lara aşağıda bulunan koddaki gibi **normal yöntemlerle doğrudan** erişilebiliyorsa, bu öğeler public member'dır. Örnek:
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
Gördüğünüz gibi buradaki c_attri, i_attri, instance_method, class_method, static_method ve diğer method ve attribute'lar public member'dır.

**Not:** Private member olarak tanımlanmamış bütün class member'lar, Python tarafından otomatik olarak public member olarak kabul edilir.

## Private Members (Gizli Üyeler)
Class'ın iç işlerini ilgilendirdiği için dışarıdan erişimine gerek olmayan ya da dışarıdan erişilirse programda sorunlara neden olabilecek class member'ların dışarıya açık (yani public member) olması istenmez. Bu class member'ların isimlerinin önüne (yani en soluna) **en az 2** tane, sonuna (yani en sağına) **en fazla 1** tane alt çizgi (`_`) koyarak bu class member'ları **private member**'lar haline getirebilirsiniz. Private member'lara **normal yöntemlerle doğrudan** erişilemez. Örnekler:
```py
class A():
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

print(A().gizli) # Output: gizli
print(A().__gizli) # AttributeError: 'A' object has no attribute '__gizli'
```
Gördüğünüz gibi private member oluşturma kuralına uyan isimleri (identifier) Python private member olarak kabul ederken, bu kurala uymayanları public member olarak kabul ediyor.

Herhangi bir method veya attribute private member olarak tanımlanabilir. Örnekler:
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

var = A()
for i in dir(var): # Output: _A__c_attri, _A__class_method, _A__i_attri, _A__instance_method, _A__static_method, 
    if "_A" in i:
        print(i, end=", ")
```

Private member'ları tanımlandıkları isimlerle (identifier) doğrudan çağıramazsınız çünkü bellekte tanımlandıkları isimlerle depolanmazlar (daha sonra anlatılacak). Yani private olarak tanımlanmış bir class member, class dışından tamamen erişilemez değildir. Bu durum, Python'ın private member'ları **Name Mangling** kullanarak farklı bir isimle (identifier) belleğe kaydetmesinden kaynaklanır. Python private member'ları `_{class_name}{private_class_member_name}` formatında oluşturulmuş isimlerle (identifier) belleğe kaydeder. Buna **Name Mangling (isim bulandırma)** denir. Örnekler:
```py
class A():
#      Attribute        Attribute           Class Member  |  Bellekteki
#        Name             Value                 Type      |     İsmi
    gizli            = "gizli"            # Public Class  | gizli
    _gizli           = "_gizli"           # Public Class  | _gizli
    _gizli_          = "_gizli_"          # Public Class  | _gizli_
    _gizli__         = "_gizli__"         # Public Class  | _gizli__
    _gizli___        = "_gizli___"        # Public Class  | _gizli___
    __gizli          = "__gizli"          # Private Class | _A__gizli
    __gizli_         = "__gizli_"         # Private Class | _A__gizli_
    __gizli__        = "__gizli__"        # Public Class  | __gizli__
    __gizli___       = "__gizli___"       # Public Class  | __gizli___
    __gizli_gizli    = "__gizli_gizli"    # Private Class | _A__gizli_gizli
    __gizli_gizli_   = "__gizli_gizli_"   # Private Class | _A__gizli_gizli_
    __gizli_gizli__  = "__gizli_gizli__"  # Public Class  | __gizli_gizli__
    __gizli_gizli___ = "__gizli_gizli___" # Public Class  | __gizli_gizli___
    ___gizli         = "___gizli"         # Private Class | _A___gizli
    ___gizli_        = "___gizli_"        # Private Class | _A___gizli_
    ___gizli__       = "___gizli__"       # Public Class  | ___gizli__
    ___gizli___      = "___gizli___"      # Public Class  | ___gizli___

print(A().gizli) # Output: gizli
print(A()._A__gizli) # Output: __gizli
print(A().__gizli) # AttributeError: 'A' object has no attribute '__gizli'
```
Bu yüzden bir private member'a, `A().__gizli` örneğindeki gibi erişemezsiniz çünkü bellekte bu isimde bir attribute yok.

**Not:** Private member'lara bu şekilde erişebilmemiz, private member'ları teknik olarak private yapmaz. Bu yüzden private member'ların doğru kullanımı name mangling ile bir nebze güvenceye alınmış ve kullanıcıların inisiyatifine bırakılmıştır.

Private member'lara class dışından normal yollarla doğrudan erişemesek bile, class'ın içinde kullanabiliriz. Örnek:
```py
class A():
    __gizli1 = "Private Class Member 1"
    __gizli2 = "Private Class Member 2"

    def yazdir1(self):
        print(self.__gizli1)
    
    def yazdir2(self):
        return self.__gizli2

A().yazdir1() # Output: Private Class Member 1
print(A().yazdir2()) # Output: Private Class Member 2
```
`A().yazdir1()` ve `print(A().yazdir2())` kodlarıyla bu private member'ların value'larına class dışından ulaşabilsek bile bu **normal yollarla doğrudan** bir erişim olmadığından, dolaylı yoldan (method aracılığıyla) bir erişim olduğundan bu class member'lar public member olarak kabul edilmez.

## Semi-private Members (Yarı-gizli Üyeler)
Önüne (yani en soluna) bir tane alt çizgi (`_`) konularak oluşturulan isimlere (identifier) sahip class member'lara **Semi-private member**'lar denir. semi-private member teknik olarak public member'dır. Yeni semi-private member'lar, Python kullanıcıların uydurduğu bir şeydir. Python kullanıcıları semi-private member'ları, bir class member'ın bellekteki ismini (identifier) değiştirmeden private member gibi kullanmak istediklerinde semi-private member'ları kullanmayı tercih eder.
```py
class A():
#      Attribute  Attribute    Class Member   |  Bellekteki
#        Name       Value          Type       |     İsmi
    gizli        = "gizli"   # Public Class   | gizli
    _gizli       = "_gizli"  # Public Class   | _gizli
    __gizli      = "__gizli" # Private Class  | A

print(A().gizli) # Output: gizli
print(A()._gizli) # Output: _gizli
print(A()._A__gizli) # Output: __gizli
print(A().__gizli) # AttributeError: 'A' object has no attribute '__gizli'
```