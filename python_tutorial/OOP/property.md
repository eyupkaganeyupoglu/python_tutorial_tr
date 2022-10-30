# İçindekiler

- [Property](#1)
    - [`@property` Decorator](#1.1)
    - [Property Methodları](#1.2)
        - [`getter` Methodu](#1.2.1)
        - [`setter` Methodu](#1.2.2)
        - [`deleter` Methodu](#1.2.3)
    - [Decorator'ların Saçmalığı](#1.3)
    - [`property(fget=None, fset=None, fdel=None, doc=None)` Fonksiyonu](#1.4)

<h1 id="1">Property</h1>

Property kelimesi de attribute kelimesi gibi nitelik/özellik anlamına gelmektedir. Property'lerin en temel işlevi, main class'da tanımlı bir methodu, main class'dan türetilmiş bir instance üzerinden attribute gibi erişip kullanabilmemizi sağlamasıdır. Property objesi oluşturmak için `@property` decorator'ını ya da `property()` fonksiyonunu kullanabilirsiniz.

<h2 id="1.1"><code>@property</code> Decorator</h2>

`@property` decorator'ı, kendisinden hemen sonraki fonksiyonla aynı isimde bir `propery` objesi yaratır. Örnek:
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

![](./pics/7.png)

Bunun sebebi `func2` fonksiyonunun artık `func2` property'sinin read işleminde (daha sonra anlayılacak) kullanılacak olmasıdır. Property'ler main class'da property objesi olarak bulunurken, main class'dan türetilen instance'larda attribute olarak bulunur. Kanıt:

![](./pics/8.png)

`func2` fonksiyonu `func2` property'sinin bir parçası olduğu için bu fonksiyonu `A.func2(var)` şeklinde çağıramazsınız. Çağırmaya çalışırsanız `TypeError: 'property' object is not callable` hataları yükseltilir çünkü `func2` artık bir property objesinin identifier'ıdır ve property objeleri çağırılabilir (callable) bir obje değildir. Benzeri `var.func2()` şeklindeki çağırmada da yaşanır çünkü `var` instance'ındaki `func2` attribute'u `None` value'sunu içerdiği için `TypeError: 'NoneType' object is not callable` hatası yükseltilir.

**Not:** Bu instance'daki `func2` attribute'u, main class'daki `func2` property objesindeki `fget` methoduna atanmış fonksiyon herhangi bir değer döndürmediği için `None` value'suna sahiptir.

**Not:** Bir property, main class'da property objesi olarak bulunurken, main class'dan türetilen instance'da attribute olarak bulunur ama bu attribute, bu instance'ın `__dict__` methodunda bulunmaz. Yani instance'lardaki bu attribute'ların main class'daki property objelerine atıfta bulunduğunu (refers to) söyleyebiliriz.

<h2 id="1.2">Property Methodları</h2>

Property'lerin üç önemli build-in methodu vardır:
- Değer döndürmek için kullanılan, read yetkisini temsil eden `getter`
- Değer atamak için kullanılan, write yetkisini temsil eden `setter`
- Değer silmek için kullanılan, delete yetkisini temsil eden `deleter`

Bu build-in methodların etki ettiği üç tane method vardır:
- `getter` build-in methodu ile decore edilmiş fonksiyonunun atandığı `fget` methodu
- `setter` build-in methodu ile decore edilmiş fonksiyonunun atandığı `fset` methodu
- `deleter` build-in methodu ile decore edilmiş fonksiyonunun atandığı `fdel` methodu

Bu methodlara `dir` fonksiyonu ile ulaşabilirsiniz:
```py
print(dir(property), end=f"\n" + "-"*70 + "\n")

for i in dir(property):
    if not "_" in i:
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

<h3 id="1.2.1"><code>getter</code> Methodu</h3>

`getter` build-in methodu, kendisinden sonra gelen fonksiyonu, ilgili property'nin **read** (değer döndürme) işleminden sorumlu fonksiyonun atandığı `fget` methoduna atar. Örnek:
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
print(A.sayı.fget) # Output: <function A.sayı at 0x000001F0E8DD51F0>
print(var.sayı) # Output: 0
print(var._A__sayı) # Output: 0
```
`getter` build-in methodu, `@{Property_object_name}.getter` formatında tanımlanır ve decore ettiği fonksiyonu `{Property_object_name}` kısmında belirtilen identifier'a sahip property objesinin `fget` methoduna atar. `getter` methodunun çalışması için ilgili instance'da ilgili attribute (yani property) talep edilmeli (`var.sayı` gibi). Read işleminden sorumlu fonksiyon düzgün çalışabilmesi için yukarıdaki `return self.__sayı` gibi ilgili attribute'un value'sunu döndürdüğü bir `return` statement içermelidir. Bu sayede yukarıdaki örnekteki gibi `var` instance'ındaki `sayı` attribute'u, read işleminden sorumlu fonksiyonun döndürdüğü değere sahip olur. Eğer read işleminden sorumlu fonksiyonda `return` statement olmasaydı, `sayı` attribute'unun value'su `None` olacaktı.

**Not:** Sadece read işlemi yapılabilen (yani sadece `fget` methoduna ilgili fonksiyon atanmış olan, `fset` ve `fdel` methodları `None` olan) attribute'lara **Read Only Attribute** (Salt Okunur Attribute) denir.

**Not:** `@property` decorator'ı ile decore edilmiş bir fonksiyon, otomatik olarak o property objesinin `fget` methoduna atanır. Yani `getter` build-in methodunu kullanmak zorunda değilsiniz.

<h3 id="1.2.2"><code>setter</code> Methodu</h3>

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
print(A.sayı.fget) # Output: <function A.sayı at 0x0000023B09B35160>
print(A.sayı.fset) # Output: <function A.sayı at 0x0000023B09B351F0>
print(var.sayı) # Output: 0
print(var._A__sayı) # Output: 0
var.sayı = 1 # Output: Write işleminden sorumlu fonksiyon çalıştı...
print(var.sayı) # Output: 1
print(var._A__sayı) # Output: 1
```
`setter` build-in methodu, `@{Property_object_name}.setter` formatında tanımlanır ve decore ettiği fonksiyonu `{Property_object_name}` kısmında belirtilen identifier'a sahip property objesinin `fset` methoduna atar. `setter` methodunun çalışması için ilgili instance'da ilgili attribute'un (yani property'nin) yeniden tanımlanması (redefinition) gerekmektedir (`var.sayı` gibi). Write işleminden sorumlu fonksiyon düzgün çalışabilmesi için yukarıdaki `yeni_değer` gibi ekstra bir parametre ve `self.__sayı = yeni_değer` gibi ilgili attribute'un value'sunu değiştirdiğimiz bir statement içermelidir.

**Not:** `setter` methodunun çalışması için ilgili instance'da ilgili attribute'un (yani property'nin) yeniden tanımlanması (redefinition) gerektiği için ilgili fonksiyona `return` statement tanımlamanız hiçbir anlam ifade etmez.

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
Programınızda bir attribute'un isimini sonradan değiştirseniz, programınızın eski versiyonunu kullanan kişiler için sıkıntı yaratmış olursunuz. Örneğin `veri` attribute'u programınızın eski versiyonunda `data` isminde tanımlıysa, `data` attribute'unun ismini `veri` olarak değiştirdiğiniz zaman programınızın eski versiyonunu kullanan kullanıcılar `veri` attribute'unu `data` olarak tanımlı zannettikleri için kendi programlarını yanlış yazıp sorunlarla karşılaşabilirler. Bu sorunun önüne geçmek için yukarıdaki kodda olduğu gibi, `veri` attribute'u üzerinde read ve write işlemleri yapabilen `data` isminde bir property tanımlayabilirsiniz. Bu sayede programınızı kullanan kullanıcıların `veri` attribute'unu `data` şeklinde kullanmalarında bir sıkıntı kalmayacağı için programınızda **backwards compatibility** (geriye dönük uyumluluk) sağlamış olursunuz.

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

`setter` methodunun birçok alanda hayat kurtarabilir. Örnek:
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

<h3 id="1.2.3"><code>deleter</code> Methodu</h3>

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
print(A.sayı.fdel) # Output: <function A.sayı at 0x00000289FDFF51F0>
print(var.sayı) # Output: 0
print(var._A__sayı) # Output: 0
del var.sayı # Output: Delete işleminden sorumlu fonksiyon çalıştı...
print(var.sayı) # AttributeError: 'A' object has no attribute '_A__sayı'
```
`deleter` build-in methodu, `@{Property_object_name}.deleter` formatında tanımlanır ve decore ettiği fonksiyonu `{Property_object_name}` kısmında belirtilen identifier'a sahip property objesinin `fdel` methoduna atar. `deleter` methodunun çalışması için ilgili instance'da ilgili attribute'un (yani property'nin) silinmesi (`del var.sayı` gibi) gerek. Delete işleminden sorumlu fonksiyon düzgün çalışabilmesi için yukarıdaki `del self.__sayı` gibi ilgili attribute'u bellekten sildiğimiz bir statement içermelidir.

**Not:** `var` instance'ındaki `self__sayı` private instance attribute'u bellekten silindiği için `sayı` property'sinin `fget` methoduna tanımlı fonksiyonun `return self.__sayı` statement'i hata mesajı döndürür (yükseltir değil, döndürür). Bu yüzden `var` instance'ındaki `sayı` attribute'unun value'su bu hata mesajı olur. Kanıt:

![](./pics/9.png)

```
sayı: 'Traceback (most recent call last):\n  File "c:\\Users\\HP\\.vscode\\extensions\\ms-python.python-2021.8.1105858891\\pythonFiles\\lib\\python\\debugpy\\_vendored\\pydevd\\_pydevd_bundle\\pydevd_resolver.py", line 193, in _get_py_dictionary\n    attr = getattr(var, name)\n  File "d:\\my_folder\\education\\software\\software_lessons\\python\\python_tutorial\\main\\.md\\TP1.py", line 7, in sayı\n    return self.__sayı\nAttributeError: \'A\' object has no attribute \'_A__sayı\'\n'
```
**Düzenlenmiş hali:**
```
Traceback (most recent call last):
  File "c:\Users\HP\.vscode\extensions\ms-python.python-2021.8.1105858891\pythonFiles\lib\python\debugpy\_vendored\pydevd\_pydevd_bundle\pydevd_resolver.py", line 193, in _get_py_dictionary
    attr = getattr(var, name)
  File "d:\my_folder\education\software\software_lessons\python\python_tutorial\main\.md\TP1.py", line 7, in sayı
    return self.__sayı
AttributeError: 'A' object has no attribute '_A__sayı'
```

**Not:** Aklınıza şöyle bir soru gelmiş olabilir: "Aynı scope'da bulunan aynı identifier'a sahip objeler birbirini geçersiz kılmıyor (override) muydu? O zaman neden `getter`, `setter`, `deleter` methodları ile decore edilen fonksiyonlar aynı identifier'a sahip olmasına rağmen birbirini geçersiz kılmadı?". Bu sorunun cevabı şudur: "`getter`, `setter`, `deleter` methodları ile decore edilen fonksiyonların objeleri, ilgili property objesinin `fget`, `fset`, `fdel` methodlarına atandı. Bu atama sonucu, `fget`, `fset`, `fdel` methodları başka bir scope'da (veya namespace'e, anladınız siz) olduğu için bu fonksiyon objeleri de başka bir scope'da olmuş oluyor. Aynı scope'da aynı identifier'a sahip bir fonksiyon olmadığından, geçersiz kılma (override) da söz konusu olmuyor.

<h2 id="1.3">Decorator'ların Saçmalığı</h2>

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

![](./pics/10.png)

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
`A` class'ında 4 farklı property objesi, `var` instance'ında 4 farklı attribute var. Kanıtı:

![](./pics/11.png)

![](./pics/12.png)

Gördüğünüz gibi tam bir karmaşa oldu. Bu objeleri teker teker açıklayalım:
- `A` class'ındaki `sayı1` property'sinin `fget` methodunda `sayı1` fonksiyonu tanımlıdır, `fset` ve `fdel` methodları tanımlı değildir. `sayı1` fonksiyonu herhangi bir `return` statement'e sahip olmadığı için `var` instance'ındaki `sayı1` attribute'u `None` value'suna sahiptir.

- `A` class'ındaki `sayı2` property'sinin `fget` methodunda `sayı2` fonksiyonu tanımlıdır, `fset` ve `fdel` methodları tanımlı değildir. `sayı2` fonksiyonu `return f"getter çalıştı. {self.__sayı}"` statement'e sahip olduğu için `var` instance'ındaki `sayı2` attribute'u `getter çalıştı. 0` value'suna sahiptir. Örnek:
    ```py
    # . . .
    print(var.sayı1) # Output: None
    print(var.sayı2) # Output: getter çalıştı. 0
    ```

- `A` class'ındaki `sayı3` property'sinin `fget` methodunda `sayı1` ve `fset` methodunda `sayı3` fonksiyonu tanımlıdır, `fdel` methodu tanımlı değildir. `sayı1` fonksiyonu herhangi bir `return` statement'e sahip olmadığı için `var` instance'ındaki `sayı3` attribute'u `None` value'suna sahiptir. `sayı3` property'sinin `fget` methoduna tanımlı fonksiyon, read görevini yapamasa bile, `fset` methoduna tanımlı fonksiyon write görevini yapabilir. Örnek:
    ```py
    # . . .
    print(var.sayı1) # Output: None
    print(var.sayı2) # Output: getter çalıştı. 0
    var.sayı3 = 1 # Output: setter çalıştı.
    print(var.sayı2) # Output: getter çalıştı. 1
    ```

- `A` class'ındaki `sayı4` property'sinin `fget` methodunda `sayı1` ve `fdel` methodunda `sayı4` fonksiyonu tanımlıdır, `fset` methodu tanımlı değildir. `sayı1` fonksiyonu herhangi bir `return` statement'e sahip olmadığı için `var` instance'ındaki `sayı4` attribute'u `None` value'suna sahiptir. `sayı4` property'sinin `fget` methoduna tanımlı fonksiyon read görevini yapamasa bile, `fdel` methoduna tanımlı fonksiyon delete görevini yapabilir. Örnek:
    ```py
    # . . .
    print(var.sayı1) # Output: None
    print(var.sayı2) # Output: getter çalıştı. 0
    del var.sayı3 # Output: deleter çalıştı.
    print(var.sayı2) # Output: AttributeError: 'A' object has no attribute '_A__sayı'
    ```

Burada sorulması gereken soru; "Madem `getter`, `setter` ve `deleter` build-in methodları, decore ettikleri fonksiyonların isimlerine (identifier) sahip yeni property objeleri oluşmasına neden olacaktı, `@sayı1.getter`, `@sayı1.setter` ve `@sayı1.deleter` build-in methodlarındaki `sayı1` kelimesi ne işe yarıyor? Buradaki `sayı1` kelimesi, `getter`, `setter` ve `deleter` build-in methodlarının decore ettiği fonksiyonların `sayı1` property'sinin `fget`, `fset` ve `fdel` methodlarına atanmasına vesile olmuyor da neden yeni property objeleri oluşmasına vesile oluyor?" [Decorators](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/functions/decorators.md "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/functions/decorators.md") konusunu bilen birisi bunun nedenini zaten anlamıştır. Anlamayanlar için:
- Decorator'lar, kendisinden hemen sonraki koda işlevsellik (functionality) eklemek için kullanılır. Hatırlatma amacıyla örnek:
```py
def decorator_maker(p1):
    def inner():
        print("Artık bu bir", end=" ")
        p1()
    return inner

def decorator_exp1():
    print("DECORATOR")

@decorator_maker
def decorator_exp2():
    print("DECORATOR")

decorator_exp1 = decorator_maker(decorator_exp1)
decorator_exp1() # Output: Artık bu bir DECORATOR

decorator_exp2() # Output: Artık bu bir DECORATOR
```
Buradan yola cıkarak şunu söyleyebiliriz: Decorator'lar, kendisinden hemen sonraki fonksiyona işlevsellik (functionality) eklediği için property decorator'ları da uygulandığı fonksiyona işlevsellik ekler.
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
Bu koddaki (yukarıdaki kodun aynısı) `@property` decorator'ı, `sayı1` fonksiyonuna Python'ın build-in namespace'inde tanımlı `property` class'ının işlevselliğini (functionality) ekliyor. `@sayı1.getter`, `@sayı1.setter`, `@sayı1.deleter` decorator'ları da sırasıyla `sayı2`, `sayı3`, `sayı4` fonksiyonlarına, Python'ın build-in namespace'inde tanımlı `property` class'ının işlevselliği (functionality) eklenmiş `sayı1` fonksiyonunun işlevselliğini ekliyor. Yani burada `sayı2`, `sayı3`, `sayı4` fonksiyonlarının işlevselliklerinin (functionality) `sayı1` property objesine eklenmesi gibi bir durum söz konusu değil çünkü bu durum decoretor'ların çalışma şekline aykırı. `sayı1` property objesinin işlevselliğini (functionality) `sayı2`, `sayı3`, `sayı4` property'lerine ekleniyor. Bu yüzden decore edilen bütün fonksiyonların kendisine özel bir property objesi var.

Gördüğünüz gibi `@property` decorator'unun ve bu decorator'un `getter`, `setter`, `deleter` build-in methodlarının böyle saçma davranışları olduğu için bu decorator'lar, bir property objesi yaratmanın en iyi yöntemi değildir (bana göre). "Decore ettiğim fonksiyonlar bir `property` objesinin parçası olsun. Normal fonksiyon gibi teker teker çağırıp kullanamayayım." diyorsanız, `property` decorator'ını kullanabilirsiniz. "Decore ettiğim fonksiyonlar bir `property` objesinin parçası olsun ama aynı zamanda bu fonksiyonlar normal fonksiyon gibi teker teker çağırıp da kullanabileyim." diyorsanız, `property` class'ından bir property objesi türetebilirsiniz (daha sonra anlatılacak).

**Not:** `@classmethod` ve `@staticmethod` decorator'larını `@property` decorator'ı ile zincirleme (chaining) kullanmayın çünkü garip davranışlar sergiliyor. Sonuçları kendiniz deneyerek öğrenebilirsiniz.

<h2 id="1.4"><code>property(fget=None, fset=None, fdel=None, doc=None)</code> Fonksiyonu</h2>

**Not:** Daha önce de söylediğim gibi, "`property()` fonksiyonu" olarak bahsedeceğim şey de aslında `property` class'ını kullanarak yaptığımız bir instantiation işlemidir.

`property()` fonksiyonu bir property objesi döndürür. `fget`, `fset` ve `fdel` parametrelerine argüman olarak sırasıyla read, write ve delete işlemlerini gerçekleştirecek fonksiyon objelerini girebiliriz. Bu parametrelerin default değeri `None`'dur Örnek:
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

    sayı1 = property(fget = sayı_get, fset = sayı_set, fdel = sayı_del, doc="Sayı Property'si")
    sayı2 = property()

var = A()
print(A.sayı1.fget) # Output: <function A.sayı_get at 0x000001D437EF51F0>
print(A.sayı1.fset) # Output: <function A.sayı_set at 0x000001D437EF5280>
print(A.sayı1.fdel) # Output: <function A.sayı_del at 0x000001D437EF5310>
print(A.sayı1.__doc__) # Output: Sayı Property'si
print(A.sayı2.fget) # Output: None
print(A.sayı2.fset) # Output: None
print(A.sayı2.fdel, end="\n\n") # Output: None

print(var.sayı1) # Output: 0
var.sayı1 = 1 # Output: sayı_set çalıştı...
print(var.sayı1) # Output: 1
del var.sayı1 # Output: sayı_del çalıştı...
print(var.sayı1) # AttributeError: 'A' object has no attribute '_A__sayı'
```
Gördüğünüz gibi `property()` fonksiyonu sayesinde `sayı` adında bir property objesi yaratıldı ve read, write, delete işlemleri için kullanılacak fonksiyonların isimleri (identifier'ları) farklı olsa bile, tek bir property objesinin ilgili methodlarına atandı.

`__doc__` methodu genelde ilgili obje hakkında bilgi vermek için kullanılan bir methoddur. Örneğin integer type objelerin `__doc__` attribute'una bakalım:
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

Decoretor'ları kullanarak oluşturduğumuz property objelerinin `fget`, `fset` ve `fdel` methodlarına atanan fonksiyonların direkt kendisine ulaşamadığımızı söylemiştik çünkü bu objeler artık property objesinin bir parçası olmuştur. Örnek:
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
print(A.sayı_change.fget(var)) # Output: 0
```
`var` instance'ındaki `sayı_change` objesi, integer value içeren bir attribute olduğu için çağırılabilir (callable) değildir. Benzer şekilde `A` class'ındaki `sayı_change` objesi bir property olduğu için çağırılabilir (callable) değildir. Ama Python dinamik bir dil olduğu için nereye bakacağınızı bilirseniz (`A.sayı_change.fget(var)` gibi) istediğiniz şeye ulaşabilirsiniz (genellikle).

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
print(A.sayı.fget) # Output: <function A.sayı_get at 0x000001ED6AC351F0>
print(A.sayı.fset) # Output: <function A.sayı_set at 0x000001ED6AC35280>
print(A.sayı.fdel) # Output: <function A.sayı_del at 0x000001ED6AC35310>
print(A.sayı.__doc__, end="\n\n") # Output: Sayı Property'si

###########################################################################

print(var.sayı) # Output: 0

print(var.sayı_get()) # Output: 0

print(A.sayı_get(var), end="\n\n") # Output: 0

###########################################################################

var.sayı = 1 # Output: sayı_set çalıştı...
print(var.sayı) # Output: 1

var.sayı_set(2) # Output: sayı_set çalıştı...
print(var.sayı_get()) # Output: 2

A.sayı_set(var, 3) # Output: sayı_set çalıştı...
print(A.sayı_get(var), end="\n\n") # Output: 3

###########################################################################

del var.sayı # Output: sayı_del çalıştı...
print(var.sayı) # AttributeError: 'A' object has no attribute '_A__sayı'

var.sayı_del() # Output: sayı_del çalıştı...
print(var.sayı_get()) # AttributeError: 'A' object has no attribute '_A__sayı'

A.sayı_del(var) # Output: sayı_del çalıştı...
print(A.sayı_get(var)) # AttributeError: 'A' object has no attribute '_A__sayı'
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

    pro_exp1 = property(fget=lambda p1 : f"{p1} Objesi")
    pro_exp2 = property(fget=lambda p1, p2 = "Objesi": f"{p1} {p2}")

var = A()
print(var.func) # Output: <bound method A.func of <__main__.A object at 0x0000013D83294FD0>>
print(var.pro_exp1) # Output: <__main__.A object at 0x0000013D83294FD0> Objesi
print(var.pro_exp2) # Output: <__main__.A object at 0x0000013D83294FD0> Objesi

# func     : 0x0000013D83294FD0
# pro_exp1 : 0x0000013D83294FD0
# pro_exp2 : 0x0000013D83294FD0
```
`func` instance fonksiyonunun `<bound method A.func of <__main__.A object at 0x0000013D83294FD0>>` objesinin `<__main__.A object at 0x0000013D83294FD0>` kısmı "`0x0000013D83294FD0` konumundaki `A` class'ının nesnesi (yani A class'ından türetilmiş instance)" anlamına gelmektedir. `pro_exp1` ve `pro_exp2` property objeleri otomatik olarak, `fget` methodlarına atanan lambda fonksiyonunun ilk parametresine argüman olarak `<__main__.A object at 0x000001EF49763FD0>` instance'ını girmiştir. Sadece ilk parametresine girdiği için `p2` parametresinin default value'su değişmemiş ve bu sayede `print(var.pro_exp2)` fonksiyonu `<__main__.A object at 0x0000013D83294FD0> Objesi` output'unu vermiştir.

**Not:** Property kavramını anlamak için **descriptor** kavramını araştırmalısınız. Gerekli siteler sırasıyla:
- [Tıklayınız](https://docs.python.org/3.7/howto/descriptor.html).
- [Tıklayınız](https://docs.python.org/3/howto/descriptor.html).