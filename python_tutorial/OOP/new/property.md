# Property
Property kelimesi de attribute kelimesi gibi nitelik/özellik anlamına gelmektedir. Property'lerin en temel işlevi, main class'da tanımlı bir methodu, main class'dan türetilmiş bir instance içinde attribute gibi kullanabilmemizi sağlamasıdır. Property objesi oluşturmak için `@property` decorator'ını ya da `property()` fonksiyonunu kullanabilirsiniz.

## `@property` Decorator
`@property` decorator'ı, kendisinden sonraki fonksiyonla aynı isimde bir `propery` objesi yaratır. Örnek:
```py
class A():
    def func1(self):
        pass

    @property
    def func2(self):
        pass

var = A()
```
`func1` methodu (`<function A.func1 at 0x00000160370A2790>`) `A` class'ında normal bir şekilde function variables kısmında bulunurken `func2` methodu bulunmuyor. Çünkü `func2` methodu bellekte `func2` adındaki property objesinin (`<property object at 0x00000160370ADC20>`) içinde bulunan `fget` methoduna atanmış `<function A.func2 at 0x00000160370A2790>` objesi olarak bellekte depolanır. Kanıt:

<img src="https://i.ibb.co/YWSNxgf/image.png" alt="image" border="0">

Bunun sebebi `func2` fonksiyonunun artık `func2` property'sinin read işleminde (daha sonra anlayılacak) kullanılacak olmasıdır. Property'ler main class'da property objesi olarak bulunurken, main class'dan türetilen instance'larda attribute olarak bulunur. Kanıt:

<img src="https://i.ibb.co/tXKdkTs/image.png" alt="image" border="0">

**Not:** Bu instance'daki `func2` attribute'u, main class'daki `func2` property objesindeki `fget` methoduna atanmış fonksiyon herhangi bir değer döndürmediği için `None` value'suna sahiptir.

**Not:** Bir property, main class'da property objesi olarak bulunurken, main class'dan türetilen instance'da attribute olarak bulunur ama bu attribute, bu instance'ın `__dict__` methodunda bulunmaz. Buradan, main class'daki bu property objesi üzerinde yapılacak herhangi bir değişikliğin, main class'dan türetilen instance'daki attribute'u da etkileyeceği sonucunu çıkarabiliriz. Yani bu attribute, instance'a özel değildir.

`func2` fonksiyonu `func2` property'sinin bir parçası olduğu için bu fonksiyonu `A.func2(var)` şeklinde çağıramazsınız. Çağırmaya çalışırsanız `TypeError: 'property' object is not callable` hataları yükseltilir çünkü `func2` artık bir property objesinin ismidir ve property objeleri çağırılabilir (callable) değildir. Benzeri `var.func2()` şeklindeki çağırmada da yaşanır çünkü `var` instance'ındaki `func2` attribute'u `None` value'sunu içerdiği için `TypeError: 'NoneType' object is not callable` hatası yükseltilir. `A` class'ını tanımlarken `func2` instance methoduna `return "Falan filan"` statement ekleseydik, `var` instance'ındaki `func2` attribute'u `"Falan filan"` value'suna sahip olacaktı ve `var.func2()` kodu bu sefer `TypeError: 'str' object is not callable` hatası verecekti.

## Property Methodları
Property'lerin üç önemli build-in methodu vardır:
- Değer döndürmek için kullanılan, read yetkisini temsil eden `getter`
- Değer atamak için kullanılan, write yetkisini temsil eden `setter`
- Değer silmek için kullanılan, delete yetkisini temsil eden`deleter`

Bu build-in methodların etki ettiği üç tane method vardır.
- `getter` build-in methodu ile decore edilmiş fonksiyonunun atandığı `fget` methodu
- `setter` build-in methodu ile decore edilmiş fonksiyonunun atandığı `fset` methodu
- `deleter` build-in methodu ile decore edilmiş fonksiyonunun atandığı `fdel` methodu

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

**Not:** Daha önce de anlattığım gibi, `fget`, `fset` ve `fdel` methodlarına atanan methodlar main class'ın `function attributes` kısmında bulunmazlar. Dolayısıyla main class'dan türetilen instance'ların `function attributes` kısmında da bulunmazlar.

### `getter` Methodu:
`getter` build-in methodu kendisinden sonra gelen fonksiyonu, ilgili property'nin **read** (değer döndürme) işleminden sorumlu fonksiyonun atandığı `fget` methoduna atar. Örnek:
```py
class A():
    def __init__(self):
        self.__sayı = 0

    @property
    def sayı(self):
        pass

    @sayı.getter
    def sayı(self):
        return self.__sayı
var = A()
print(var.sayı) # Output: 0
print(var._A__sayı) # Output: 0
```
`getter` build-in methodu, `@{Property_object_name}.getter` formatında tanımlanır ve decore ettiği fonksiyonu `{Property_object_name}` kısmında belirtilen property objesinin `fget` methoduna atar. Read işleminden sorumlu fonksiyon düzgün çalışabilmesi için yukarıdaki `return self.__sayı` gibi ilgili attribute'un value'sunu döndürdüğü bir statement içermelidir. Bu sayede yukarıdaki örnekteki gibi, `var` instance'ındaki `sayı` attribute'u, read işleminden sorumlu fonksiyonun döndürdüğü değere sahip olur. Eğer read işleminden sorumlu fonksiyonda `return` statement olmasaydı, `sayı` attribute'unun value'su `None` olacaktı.

**Not:** Sadece read işlemi yapılabilen (yani sadece `fget` methoduna ilgili fonksiyon atanmış olan, `fset` ve `fdel` methodları `None` olan) attribute'lara **Read Only Attribute** (Salt Okunur Attribute) denir.

**Not:** `@property` decorator'ı ile decore edilmiş bir fonksiyon, otomatik olarak o property objesinin `fget` methoduna atanır. Yani `getter` build-in methodunu kullanmak zorunda değilsiniz.

### `setter` Methodu:
`setter` build-in methodu kendisinden sonra gelen fonksiyonu, ilgili property'nin **write** (değer atama) işleminden sorumlu fonksiyonun atandığı `fset` methoduna atar. Örnek:
```py
class A():
    def __init__(self):
        self.__sayı = 0

    @property
    def sayı(self):
        return self.__sayı

    @sayı.setter
    def sayı(self, yeni_değer):
        print("Write işleminden sorumlu fonksiyon çalıştı...")
        self.__sayı = yeni_değer

var = A()
print(var.sayı) # Output: 0
print(var._A__sayı) # Output: 0
var.sayı = 1 # Output: Write işleminden sorumlu fonksiyon çalıştı...
print(var.sayı) # Output: 1
print(var._A__sayı) # Output: 1
```
`setter` build-in methodu, `@{Property_object_name}.setter` formatında tanımlanır ve decore ettiği fonksiyonu `{Property_object_name}` kısmında belirtilen property objesinin `fset` methoduna atar. Write işleminden sorumlu fonksiyon düzgün çalışabilmesi için yukarıdaki `yeni_değer` gibi ekstra bir parametre ve `self.__sayı = yeni_değer` gibi ilgili attribute'un value'sunu değiştirdiğimiz bir statement içermelidir.

**Not:** `setter` build-in methodu ile decore edilmiş fonksiyon, değerini değiştirdiği attribute'u döndürmek zorunda değildir. Örnek:
```py
class A():
    def __init__(self):
        self.__sayı = 0

    @property
    def sayı(self):
        return self.__sayı

    @sayı.setter
    def sayı(self, yeni_değer):
        print("Write işleminden sorumlu fonksiyon çalıştı...")
        self.__sayı = yeni_değer
        return self.__sayı
```
Buradaki `return self.__sayı` statement'ın `setter` build-in methodunun işleviyle bir alakası yok. Bu yüzden varlığı bir anlam ifade etmiyor.

Write işlemini kullanarak programımızda **backwards compatibility** (geriye dönük uyumluluk) konusunda avantaj sağlayabiliriz. Örnek:
```py
class A():
    def __init__(self):
        self.veri = 0

    @property
    def data(self):
        return self.veri

    @data.setter
    def data(self, yeni_değer):
        self.veri = yeni_değer
var = A()
print(var.data) # Output: 0
var.data = 1
print(var.data) # Output: 1
```
Programınızda tanımladığınız bir class içindeki bir attribute'un isimini sonradan değiştirseniz, programınızın eski versiyonunu kullanan kişiler için sıkıntı yaratmış olursunuz. Örneğin `self.veri` attribute'u programınızın eski versiyonunda `self.data` isminde tanımlıysa, `self.data` attribute'unun ismini `self.veri` olarak değiştirdiğiniz zaman programınızın eski versiyonunu kullanan kullanıcılar, `self.veri` attribute'unu `self.data` isminde tanımlı zannettikleri için kendi programlarını yanlış yazıp hata alabilirler. Bu sorunun önüne geçmek için yukarıdaki kodda olduğu gibi, `self.veri` attribute'u üzerinde read ve write işlemleri yapabilen `data` isminde bir property tanımlayabilirsiniz. Bu sayede programınızı kullanan kullanıcıların `self.veri` attribute'unu `self.data` şeklinde kullanmalarında bir sıkıntı kalmayacağı için programınızda **backwards compatibility** (geriye dönük uyumluluk) sağlamış olursunuz.

`setter` methodu değer doğrulama gibi işlemlerde de kullanışlıdır. Örnek:
```py
class A():
    def __init__(self):
        self.__sayı = 0

    @property
    def sayı(self):
        return self.__sayı

    @sayı.setter
    def sayı(self, yeni_değer):
        if yeni_değer % 2 == 0:
            self.__sayı = yeni_değer
        else:
            print('Çift değil!')

var = A()
print(var.sayı) # Output: 0
print(var._A__sayı) # Output: 0

var.sayı = 1 # Output: Çift değil!
print(var.sayı) # Output: 0
print(var._A__sayı) # Output: 0

var.sayı = 2
print(var.sayı) # Output: 2
print(var._A__sayı) # Output: 2
```

`setter` methodunun birçok alanda hayat kurtarabilir. Bir tane örnek verelim:
```py
class A():
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

var1 = A("AAA") # Output: 'AAA' adlı instnace eklendi.
var2 = A("BBB") # Output: 'BBB' adlı instnace eklendi.
A.show_all_instance() # Output: All Instances: AAA, BBB

var1.instace_name = "CCC"
print(var1.instace_name) # Output: CCC
A.show_all_instance() # Output: All Instances: AAA, BBB
var1.show_all_instance() # Output: All Instances: AAA, BBB
var2.show_all_instance() # Output: All Instances: AAA, BBB
```
Gördüğünüz gibi `var1` instance'ının `instace_name` instance attribute'unun value'sunu değiştirsek bile bu değişiklik `all_instances` class attribute'una yansımadı. Bu sorunu çözmek için ekstra bir method tanımlayabilir ya da property kullanabiliriz. ekstra method tanımlama çözümü:
```py
class A():
    all_instances = []
    def __init__(self, name):
        self.__instace_name = name
        self.add_instance()

    def add_instance(self):
        print(f"'{self.__instace_name}' adlı instnace eklendi.")
        self.all_instances.append(self.__instace_name)

    @classmethod
    def show_all_instance(cls):
        print("All Instances:", end=" ")
        for member in cls.all_instances:
            if member == cls.all_instances[-1]:
                print(member)
            else:
                print(member, end=", ")

    def change_instance_name(self, new_name):
        print(f"{self.__instace_name} -> {new_name}")
        self.all_instances[self.all_instances.index(self.__instace_name)] = new_name
        self.__instace_name = new_name

var1 = A("AAA") # Output: 'AAA' adlı instnace eklendi.
var2 = A("BBB") # Output: 'BBB' adlı instnace eklendi.
A.show_all_instance() # Output: All Instances: AAA, BBB

var1.change_instance_name("CCC") # Output: AAA -> CCC
print(var1._A__instace_name) # Output: CCC
A.show_all_instance() # Output: All Instances: CCC, BBB
var1.show_all_instance() # Output: All Instances: CCC, BBB
var2.show_all_instance() # Output: All Instances: CCC, BBB
```
Yukarıdaki kodda, üzerinden çağırıldığı instance'ın `__instace_name` private instance attribute'unun value'sunu değiştiren ve bu değişikliği `all_instances` class attibute'a da yansıtan `change_instance_name` isimli bir instance method tanımlandı. Property çözümü:
```py
class A():
    all_instances = []
    def __init__(self, name):
        self.__instace_name = name
        self.add_instance()

    def add_instance(self):
        print(f"'{self.__instace_name}' adlı instnace eklendi.")
        self.all_instances.append(self.__instace_name)

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
        return self.__instace_name

    @instace_name.setter
    def instace_name(self, new_name):
        print(f"{self.__instace_name} -> {new_name}")
        self.all_instances[self.all_instances.index(self.__instace_name)] = new_name
        self.__instace_name = new_name

var1 = A("AAA") # Output: 'AAA' adlı instnace eklendi.
var2 = A("BBB") # Output: 'BBB' adlı instnace eklendi.
A.show_all_instance() # Output: All Instances: AAA, BBB

var1.instace_name = "CCC" # Output. AAA -> CCC
print(var1.instace_name) # Output: CCC
A.show_all_instance() # Output: All Instances: CCC, BBB
var1.show_all_instance() # Output: All Instances: CCC, BBB
var2.show_all_instance() # Output: All Instances: CCC, BBB
```
Bir önceki kodda `change_instance_name` isimli instance methodda tanımlanan işlemlerin aynısı `setter` build-in methodu ile decore edilmiş `instace_name` instance methoduna tanımlanmıştır. Böylece bir önceki koddaki `var1.change_instance_name("CCC")` gibi ekstra methodlarla uğraşmadan `var1.instace_name = "CCC"` işlemiyle `var1.change_instance_name("CCC")` işlemindeki sonucu elde etmiş olduk.

### `deleter` Methodu:
`deleter` build-in methodu kendisinden sonra gelen fonksiyonu, ilgili property'nin **delete** (değer silme) işleminden sorumlu fonksiyonun atandığı `fdel` methoduna atar. Örnek:
```py
class A():
    def __init__(self):
        self.__sayı = 0

    @property
    def sayı(self):
        return self.__sayı

    @sayı.deleter
    def sayı(self):
        print("Delete işleminden sorumlu fonksiyon çalıştı...")
        del self.__sayı

var = A()
print(var.sayı) # Output: 0
print(var._A__sayı) # Output: 0
del var.sayı # Output: Delete işleminden sorumlu fonksiyon çalıştı...
print(var.sayı) # AttributeError: 'A' object has no attribute '_A__sayı'
```
`deleter` build-in methodu, `@{Property_object_name}.deleter` formatında tanımlanır ve decore ettiği fonksiyonu `{Property_object_name}` kısmında belirtilen property objesinin `fdel` methoduna atar. Delete işleminden sorumlu fonksiyon düzgün çalışabilmesi için yukarıdaki `del self.__sayı` gibi ilgili attribute'u bellekten sildiğimiz bir statement içermelidir.

**Not:** `var` instance'ındaki `self__sayı` private instance attribute'u bellekten silindiği için `sayı` property'sinin fget methoduna tanımlı fonksiyonun `return self.__sayı` statement'i hata mesajı döndürür (yükseltir değil, döndürür). Bu yüzden `var` instance'ındaki `sayı` attribute'unun value'su bu hata mesajı olur. Kanıt:

<img src="https://i.ibb.co/swJ4ZjR/image.png" alt="image" border="0">

```
sayı: 'Traceback (most recent call last):\n  File "c:\\Users\\HP\\.vscode\\extensions\\ms-python.python-2021.8.1105858891\\pythonFiles\\lib\\python\\debugpy\\_vendored\\pydevd\\_pydevd_bundle\\pydevd_resolver.py", line 193, in _get_py_dictionary\n    attr = getattr(var, name)\n  File "d:\\my_folder\\education\\software\\software_lessons\\python\\python_tutorial\\main\\.md\\TP1.py", line 7, in sayı\n    return self.__sayı\nAttributeError: \'A\' object has no attribute \'_A__sayı\'\n'
```
```
Traceback (most recent call last):
  File "c:\Users\HP\.vscode\extensions\ms-python.python-2021.8.1105858891\pythonFiles\lib\python\debugpy\_vendored\pydevd\_pydevd_bundle\pydevd_resolver.py", line 193, in _get_py_dictionary
    attr = getattr(var, name)
  File "d:\my_folder\education\software\software_lessons\python\python_tutorial\main\.md\TP1.py", line 7, in sayı
    return self.__sayı
AttributeError: 'A' object has no attribute '_A__sayı'
```

## Decorator'ların Saçmalığı
Şimdiye kadar read, write ve delete işlemlerini gerçekleştirmesi için `fget`, `fset` ve `fdel` methodlarına atadığımız fonksiyonların aynı isme (identifier) sahip olduğunu farketmişsinizdir. Örnek:
```py
class A():
    def __init__(self):
        self.__sayı = 0
    
    @property
    def sayı(self):
        pass

    @sayı.getter
    def sayı(self):
        return f"getter çalıştı. {self.__sayı}"

    @sayı.setter
    def sayı(self, yeni_değer):
        print("setter çalıştı.")
        self.__sayı = yeni_değer

    @sayı.deleter
    def sayı(self):
        print("deleter çalıştı.")
        del self.__sayı

var = A()
print(var._A__sayı) # Output: 0
print(var.sayı) # Output: getter çalıştı. 0

var.sayı = 1 # Output: setter çalıştı.
print(var._A__sayı) # Output: 1
print(var.sayı) # Output: getter çalıştı. 1

del var.sayı # Output: deleter çalıştı.
print(var._A__sayı) # Output: AttributeError: 'A' object has no attribute '_A__sayı'
print(var.sayı) # Output: AttributeError: 'A' object has no attribute '_A__sayı'
```
`sayı` property'sinin `fget`, `fset` ve `fdel` methodlarının hepsi tanımlıdır çünkü bu methodlara atanan fonksiyonlar aynı isimdedir (identifier). Kanıtı:

<img src="https://i.ibb.co/7kmgRmQ/image.png" alt="image" border="0">

Peki `fget`, `fset` ve `fdel` methodlarına atanan fonksiyonların isimleri farklı olsaydı? Örnek:
```py
class A():
    def __init__(self):
        self.__sayı = 0
    
    @property
    def sayı1(self):
        pass

    @sayı1.getter
    def sayı2(self):
        return f"getter çalıştı. {self.__sayı}"

    @sayı1.setter
    def sayı3(self, yeni_değer):
        print("setter çalıştı.")
        self.__sayı = yeni_değer

    @sayı1.deleter
    def sayı4(self):
        print("deleter çalıştı.")
        del self.__sayı

var = A()
```
`A` class'ında 4 farklı property objesi, `var` instance'ında 4 farklı attribute yaratıldı. Kanıtı:

<img src="https://i.ibb.co/0D8CDbd/image.png" alt="image" border="0">

<img src="https://i.ibb.co/4FSrsGm/image.png" alt="image" border="0">

Gördüğünüz gibi tam bir karmaşa oldu.
- `A` class'ındaki `sayı1` property'sinin `fget` methodunda `sayı1` fonksiyonu tanımlıdır, `fset` ve `fdel` methodları tanımlı değildir. `sayı1` fonksiyonu herhangi bir `return` statement'e sahip olmadığı `var` instance'ındaki `sayı1` attribute'u `None` value'suna sahiptir.

- `A` class'ındaki `sayı2` property'sinin `fget` methodunda `sayı2` fonksiyonu tanımlıdır, `fset` ve `fdel` methodları tanımlı değildir. `sayı2` fonksiyonu `return f"getter çalıştı. {self.__sayı}"` statement'e sahip olduğu için `var` instance'ındaki `sayı2` attribute'u `getter çalıştı. 0` value'suna sahiptir. Yani `sayı2` property'sinin `fget` methoduna tanımlı fonksiyon, read görevini yapabiliyor. Örnek:
    ```py
    # . . .
    print(var.sayı1) # Output: None
    print(var.sayı2) # Output: getter çalıştı. 0
    ```

- `A` class'ındaki `sayı3` property'sinin `fget` methodunda `sayı1` ve `fset` methodunda `sayı3` fonksiyonu tanımlıdır, `fdel` methodu tanımlı değildir. `sayı1` fonksiyonu herhangi bir `return` statement'e sahip olmadığı `var` instance'ındaki `sayı3` attribute'u `None` value'suna sahiptir. `sayı3` property'sinin `fget` methoduna tanımlı fonksiyon, read görevini yapamasa bile `fset` methoduna tanımlı fonksiyon, write görevini yapabilir. Örnek:
    ```py
    # . . .
    print(var.sayı1) # Output: None
    print(var.sayı2) # Output: getter çalıştı. 0
    var.sayı3 = 1 # Output: setter çalıştı.
    print(var.sayı2) # Output: getter çalıştı. 1
    ```

- `A` class'ındaki `sayı4` property'sinin `fget` methodunda `sayı1` ve `fdel` methodunda `sayı4` fonksiyonu tanımlıdır, `fset` methodu tanımlı değildir. `sayı1` fonksiyonu herhangi bir `return` statement'e sahip olmadığı `var` instance'ındaki `sayı4` attribute'u `None` value'suna sahiptir. `sayı4` property'sinin `fget` methoduna tanımlı fonksiyon, read görevini yapamasa bile `fdel` methoduna tanımlı fonksiyon, delete görevini yapabilir. Örnek:
    ```py
    # . . .
    print(var.sayı1) # Output: None
    print(var.sayı2) # Output: getter çalıştı. 0
    del var.sayı3 # Output: deleter çalıştı.
    print(var.sayı2) # Output: AttributeError: 'A' object has no attribute '_A__sayı'
    ```

Burada sorulması gereken soru; "Madem `getter`, `setter` ve `deleter` build-in methodları decore ettikleri fonksiyonların isimlerine (identifier) sahip yeni property objeleri oluşmasına neden olacaktı, neden `@sayı1.getter`, `@sayı1.setter` ve `@sayı1.deleter` build-in methodlarında `sayı1` kelimesi ne işe yarıyor? Buradaki `sayı1` kelimesi, `getter`, `setter` ve `deleter` build-in methodlarının decore ettiği fonksiyonların `sayı1` property'sinin `fget`, `fset` ve `fdel` methodlarına atanmasına vesile olmuyor da neden yeni property objeleri oluşmasına vesile oluyor?" Buna bir cevap henüz bulamadım. Tek anladığım şey, `sayı1` kelimesi yüzünden `sayı1` fonksiyonu `@sayı1.getter`, `@sayı1.setter` ve `@sayı1.deleter` build-in methodlarının oluşturduğu yeni property objelerinin `fget` methodlarına atandığı (`sayı2` property objesinin `fget` methoduna ilk başta `sayı1` fonksiyonu atanmasına rağmen `getter` build-in methodu yüzünden `sayı2` fonksiyonu olarak yeniden tanımlanmıştır (redefinition)).

Gördüğünüz gibi `@property` decorator'unun ve bu decorator'un `getter`, `setter`, `deleter` build-in methodlarının böyle saçma davranışları olduğu için bu decorator'lar, bir property objesi yaratmanın en iyi yöntemi değildir. Bu yüzden bir property objesi yaratmak istediğinizde bu decorator'ları kullanmak terine `property()` fonksiyonunu tercih etmelisiniz.

## `property(fget=None, fset=None, fdel=None, doc=None)` Fonksiyonu
`property()` fonksiyonu, `fget`, `fset` ve `fdel` parametrelerine sırasıyla read, write ve delete işlemlerini gerçekleştirecek fonksiyon objelerini argüman olarak verip bir property oluşturabilmenizi sağlar. Örnek:
```py
class A():
    def __init__(self):
        self.__sayı = 0

    def sayı_get(self):
        return self.__sayı

    def sayı_set(self, yeni_değer):
        print("sayı_set çalıştı...")
        self.__sayı = yeni_değer

    def sayı_del(self):
        print("sayı_del çalıştı...")
        del self.__sayı

    sayı = property(fget = sayı_get, fset = sayı_set, fdel = sayı_del, doc="Sayı Property'si")

var = A()
print(A.sayı.__doc__) # Output: Sayı Property'si
print(var.sayı) # Output: 0
var.sayı = 1 # Output: sayı_set çalıştı...
print(var.sayı) # Output: 1
del var.sayı # Output: sayı_del çalıştı...
print(var.sayı) # AttributeError: 'A' object has no attribute '_A__sayı'
```
Gördüğünüz gibi `property()` fonksiyonu sayesinde `sayı` adında bir property objesi yaratıldı ve read, write, delete işlemleri için kullanılacak fonksiyonların isimleri farklı olsa bile, tek bir property objesinin ilgili methodlarına atandı.

`__doc__` methodu genelde ilgili obje hakkında bilgi vermek için kullanılan bir şeydir. Örneğin integer type objelerin `__doc__` attribute'una bakalım:
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
Bir property objesinin `__doc__` methoduna, bu property objesinin ne amaçla kullanıldığını yazabilirsiniz.

**Not:** `property()` fonksiyonunu global namespace'de de kullanabilirsiniz. Bu sayede global namespace'de de property objeleri yaratabilirsiniz. Ama bu bir işinize yarar mı bilmiyorum.

Decoretor'ları kullanarak oluşturduğumuz property objelerinin `fget`, `fset` ve `fdel` methodlarına atanan fonksiyonların direkt kendisine ulaşamadığımızı söylemiştik. Örnek:
```py
class A:
    def __init__(self):
        self.__sayı = 0

    @property
    def sayı_change(self):
        return self.__sayı

var = A()

print(var.sayı_change) # Output: 0
print(var.sayı_change()) # TypeError: 'int' object is not callable
print(A.sayı_change()) # TypeError: 'property' object is not callable
```
Bu durum `property()` fonksiyonu ile oluşturulmuş property objeleri için geçerli değildir. Örnek:
```py
class A:
    def __init__(self):
        self.__sayı = 0

    def sayı_get(self):
        return self.__sayı

    def sayı_set(self, yeni_değer):
        print("sayı_set çalıştı...")
        self.__sayı = yeni_değer

    def sayı_del(self):
        print("sayı_del çalıştı...")
        del self.__sayı

    sayı = property(fget = sayı_get, fset = sayı_set, fdel = sayı_del, doc="Sayı Property'si")

var = A()

print(var.sayı) # Output: 0
print(var.sayı_get()) # Output: 0
print(A.sayı_get(var)) # Output: 0

var.sayı = 1 # Output: sayı_set çalıştı...
print(var.sayı) # Output: 1

var.sayı_set(2) # Output: sayı_set çalıştı...
print(var.sayı_get()) # Output: 2

A.sayı_set(var, 3) # Output: sayı_set çalıştı...
print(A.sayı_get(var)) # Output: 3

del var.sayı # Output: sayı_del çalıştı...
print(var.sayı) # AttributeError: 'A' object has no attribute '_A__sayı'

# del var.sayı_del() # Output: sayı_del çalıştı...
# print(var.sayı_get()) # AttributeError: 'A' object has no attribute '_A__sayı'

# del A.sayı_del(var) # Output: sayı_del çalıştı...
# print(A.sayı_get(var)) # AttributeError: 'A' object has no attribute '_A__sayı'
```
`sayı` property'sinin `fget`, `fset` ve `fdel` methodlarına tanımlanan, sırasıyla `sayı_get`, `sayı_set` ve `sayı_del` fonksiyonları ile `A` class'ının *function variables* kısmındaki `sayı_get`, `sayı_set` ve `sayı_del` fonksiyonları, aynı objeleridir. Bu fonksiyonlara erişilmesini istemiyorsanız, `__sayı_get`, `__sayı_set` ve `__sayı_del` şeklinde tanımlayarak private hale getirebilirsiniz.

Property objelerinin `fget`, `fset` ve `fdel` methodlarına şimdiye kadar sadece instance method atadık ama istersek class veya static method'da atayabiliriz. Örnek:
```py
class A:
    def __init__(self):
        self.__sayı = 0

    def sayı_get(self):
        return self.__sayı

    @classmethod
    def sayı_set(cls, yeni_değer):
        print("sayı_set çalıştı...")
        cls.__sayı = yeni_değer

    @staticmethod
    def sayı_del(self = A()):
        print("sayı_del çalıştı...")
        del self.__sayı

    sayı = property(fget = sayı_get, fset = sayı_set, fdel = sayı_del, doc="Sayı Property'si")

print(A.sayı.fget) #Output: <function A.sayı_get at 0x000001F92CD641F0>
print(A.sayı.fget) #Output: <classmethod object at 0x000001F92CD68FD0> 
print(A.sayı.fdel) #Output: <staticmethod object at 0x000001F92CD68FA0>

var = A()
print(var.sayı) # Output: 0
var.sayı = 1 # TypeError: 'classmethod' object is not callable
del var.sayı # TypeError: 'staticmethod' object is not callable
```
`classmethod` ve `staticmethod` objeleri çağırılabilir (callable) olmadıkları için `sayı` property'si düzgün çalışmaz.

**Not:** Property objelerinin `fget`, `fset` ve `fdel` methodlarına şimdiye kadar sadece instance method atadığımız için bahsetmemiştim ama son olarak şundan bahsedeyim: Bir property objesi, `fget`, `fset` ve `fdel` methodlarına atanan fonksiyonların ilk parametresine ilgili instance'ı argüman olarak verir. Örnek:
```py
class A:
    def func(self):
        pass

    pro_exp = property(fget=lambda p1, p2 = "Objesi": f"{p1} {p2}")

var = A()
print(var.func) # Output: <bound method A.func of <__main__.A object at 0x000001EF49763FD0>>
print(var.pro_exp) # Output: <__main__.A object at 0x000001EF49763FD0> Objesi

# func    : 0x000001EF49763FD0
# pro_exp : 0x000001EF49763FD0
```
`func` instance fonksiyonunun `<bound method A.func of <__main__.A object at 0x000001EF49763FD0>>` objesinin `<__main__.A object at 0x000001EF49763FD0>` kısmı "`0x000001EF49763FD0` konumundaki `A` class'ının nesnesi (yani A class'ından türetilmiş instance)" anlamına gelmektedir. `pro_exp` property objesi, `fget` methoduna atanan lambda fonksiyonunun ilk parametresine `<__main__.A object at 0x000001EF49763FD0>` instance'ını (`func`'da bahsettiğimiz instance) argüman olarak vermiş, sadece ilk parametresine verdiği için `p2` parametresinin default value'su değişmemiş ve bu sayede `print(var.pro_exp)` fonksiyonu `<__main__.A object at 0x000001EF49763FD0> Objesi` output'unu vermiştir.

**Not:** Property kavramını anlamak için **descriptor** kavramını araştırmalısınız. Gerekli siteler sırasıyla:
- [Tıklayınız](https://docs.python.org/3.7/howto/descriptor.html).
- [Tıklayınız](https://docs.python.org/3/howto/descriptor.html).