# İçindekiler

- [`all(iterable)` Fonksiyonu](#1)
- [`any(iterable)` Fonksiyonu](#2)
- [`breakpoint(*args, **kws)` Fonksiyonu](#3)
- [`callable(object)` Fonksiyonu](#4)
- [`compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)` Fonksiyonu](#5)
- [`dir(object)` Fonksiyonu](#6)
- [`eval(expression, globals=None, locals=None)` Fonksiyonu](#7)
- [`exec(expression, globals=None, locals=None)` Fonksiyonu](#8)
- [`filter(function, iterable)` Fonksiyonu](#9)
- [`format(value, format_spec)` Fonksiyonu](#10)
- [`globals()` Fonksiyonu](#11)
- [`hash(object)` Fonksiyonu](#12)
- [`help(object)` Fonksiyonu](#13)
- [`id(object)` Fonksiyonu](#14)
- [`isinstance(object, classinfo)` Fonksiyonu](#15)
- [`issubclass(class, classinfo)` Fonksiyonu](#16)
- [`len(s)` Fonksiyonu](#17)
- [`locals()` Fonksiyonu](#18)
- [`map(function, iterable, ...)` Fonksiyonu](#18)
- [`slice(start, stop, step)` Fonksiyonu](#20)
- [`type(object)` Fonksiyonu](#21)
- [`vars(object)` Fonksiyonu](#22)
- [`zip(*iterables)` Fonksiyonu](#23)
- [`site` Modülü Tarafından Eklenen Constant'lar](#24)
    - [`quit(code=None)` Constant](#24.1)
    - [`exit(code=None)` Constant](#24.2)
    - [`copyright()` Constant](#24.3)
    - [`credits()` Constant](#24.4)
    - [`license()` Constant](#24.5)

**Ön Bilgi:** Python ve Python'daki build-in fonksiyonlar **C** diliyle yazılmıştır. Gömülü fonksiyon olarak da bilinen build-in fonksiyonlar, Python diline gömülmüş fonksiyonlardır. Çoğu Python modülü Python diliyle yazılmıştır ama build-in fonksiyonlar **C** diliyle yazılmıştır. Aşağıda, bu tutorialin başka bir yerinde değinilmemiş ya da yeterince değinilmemiş build-in fonksiyonlar anlatılmıştır. Yani dökümanı 50k satır yapmamak için diğer dökümanlarda anlattığım build-in fonksiyonları buraya eklemedim.

<h1 id="1"><code>all(iterable)</code> Fonksiyonu</h1>

**Ön bilgi:** Bu bölümü anlayabilmek için iterator ve iterable kavramlarını bilmeniz gerekmektedir. Gerekli bilgiler için [tıklayınız](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/functions/iterators.md "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/functions/iterators.md").

`all(iterable)` fonksiyonu aşağıdaki syntax'a sahiptir:
```py
def all(iterable):
    for element in iterable: # iterable boş olursa for çalışmaz.
        if not element: # element False ise `not False == True` olacağı için çalışır.
            return False
    return True # For çalışmazsa direkt bu satır çalışır.
```
Yani `all()` fonksiyonunun `True` sonucunu vermesi için `iterable` parametresine argüman olarak girilen iterable objenin bütün öğelerin boolean değeri `True` olmalı veya bu iterable obje boş olmalıdır. Örnek:
```py
l1 = [1, 2.6, 13+2j,"boş değil"]    # All True
l2 = [0, 0.0, 0+0j, ""]             # All False
l3 = [0, 1, 2.6, 13+2j,"boş değil"] # One False
l4 = []                             # Empty

print("all(), All True:", all(l1))  # True
print("all(), All False:", all(l2)) # False
print("all(), One False:", all(l3)) # False
print("all(), Empty:", all(l4))     # True
```
**Output:**
```
all(), All True: True
all(), All False: False
all(), One False: False
all(), Empty: True
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#all "https://docs.python.org/3/library/functions.html#all").

<h1 id="2"><code>any(iterable)</code> Fonksiyonu</h1>

**Ön bilgi:** Bu bölümü anlayabilmek için iterator ve iterable kavramlarını bilmeniz gerekmektedir. Gerekli bilgiler için [tıklayınız](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/functions/iterators.md "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/functions/iterators.md").

`any(iterable)` fonksiyonu aşağıdaki syntax'a sahiptir:
```py
def any(iterable):
    for element in iterable: # iterable boş olursa for çalışmaz.
        if element: # element False ise `True == True` olacağı için çalışır.
            return True
    return False # For çalışmazsa direkt bu satır çalışır.
```

Yani `any()` fonksiyonunun `True` sonucunu vermesi için `iterable` parametresine argüman olarak girilen iterable objenin en az bir tane öğesinin boolean değeri `True` olması yeterlidir. Örnek:
```py
l1 = [1, 2.6, 13+2j,"boş değil"]    # All True
l2 = [0, 0.0, 0+0j, ""]             # All False
l3 = [0, 1, 2.6, 13+2j,"boş değil"] # One False
l4 = []                             # Empty

print("any(), All True:", all(l1))  # True
print("any(), All False:", all(l2)) # False
print("any(), One False:", all(l3)) # True
print("any(), Empty:", all(l4))     # False
```
**Output:**
```
any(), All True: True
any(), All False: False
any(), One False: True
any(), Empty: False
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#any "https://docs.python.org/3/library/functions.html#any").

<h1 id="3"><code>breakpoint(*args, **kws)</code> Fonksiyonu</h1>

Debugging işleminde kullanılan bir fonksiyondur. Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#breakpoint "https://docs.python.org/3/library/functions.html#breakpoint").

<h1 id="4"><code>callable(object)</code> Fonksiyonu</h1>

`object` parametresine argüman olarak girilen objenin çağrılabilir (callable) olup olmadığını denetler. Çağırılabilirse `True`, değilse `False` döndürür.
```py
def func(): pass
var = 1
print(callable(func)) # Output: True
print(callable(var)) # Output: False
```

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#callable "https://docs.python.org/3/library/functions.html#callable").

<h1 id="5"><code>compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)</code> Fonksiyonu</h1>

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#compile "https://docs.python.org/3/library/functions.html#compile").

<h1 id="6"><code>dir(object)</code> Fonksiyonu</h1>

Parametresiz olarak kullanırsak, bulunduğu scope'deki öğeleri listeler. `globals()` ve `locals()`'den farkı, output'u dict type olarak değil, list type olarak vermesidir. Örnek:
```py
def func(): print(dir())
func() # Output: []

print(dir(list)) # Output: ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#dir "https://docs.python.org/3/library/functions.html#dir").

<h1 id="7"><code>eval(expression, globals=None, locals=None)</code> Fonksiyonu</h1>

**Ön bilgi:** Bu bölümü anlayabilmek için [expression](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/statements_expressions_keywords.md#2 "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/statements_expressions_keywords.md#2") ve [statement](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/statements_expressions_keywords.md#3 "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/statements_expressions_keywords.md#3") kavramlarını bilmeniz gerekmektedir. Gerekli bilgiler için [tıklayınız](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/statements_expressions_keywords.md "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/statements_expressions_keywords.md").

Expression ve statement'i ayırt edebilmek için `eval()` kullanılabilir çünkü `eval()`, parametre olarak sadece expression'ları kabul eder. `eval()` fonksiyonu `expression` parametresine argüman olarak girilen string'i yorumlar ve çalıştırır. Yani `eval("print('selam')")` şeklinde bir komut tanımlarsanız, `eval()` bunu önce yorumlar, sonra yorumundan çıkardığı anlamsal kodu (yani `print('selam')` kodunu) çalıştırır. `eval()`'in bu özelliğini kullanırken dikkat edilmelidir çünkü bu fonksiyon kötü amaçlarla da kullanılabilir. Örneğin sistem dosyalarını silecek bir kodu `eval()` fonksiyonuna yazabilirsiniz. Bunu önlemek için kodunuza kontrol mekanizması eklenmelidir. `eval()` fonksiyonunun `expression` parametresine argüman olarak statement (örneğin `eval("a=5")` gibi bir assignment statement) işlemini içeren bir string giremezsiniz. `eval()` fonksiyonu yavaş çalışan bir fonksiyondur. Bu yüzden en son tercihiniz olmalıdır. Örnek:
```py
eval("print('selam')")
print("""
İşlemler:
+ toplama
- çıkarma
* çarpma
/ bölme
  
Yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın. (Örneğin 23 ve 46 sayılarını
çarpmak için 23*46 yazdıktan sonra
ENTER tuşuna basın.)
""")
hesap = eval(input("İşleminiz: "))
print(hesap)
```
bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#eval "https://docs.python.org/3/library/functions.html#eval").

<h1 id="8"><code>exec(expression, globals=None, locals=None)</code> Fonksiyonu</h1>

**Ön bilgi:** Bu bölümü anlayabilmek için [expression](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/statements_expressions_keywords.md#2 "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/statements_expressions_keywords.md#2") ve [statement](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/statements_expressions_keywords.md#3 "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/statements_expressions_keywords.md#3") kavramlarını bilmeniz gerekmektedir. Gerekli bilgiler için [tıklayınız](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/statements_expressions_keywords.md "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/statements_expressions_keywords.md").

`exec()` fonksiyonu, `eval()`'den farklı olarak statement'ları yorumlayıp çalıştırabilir. Örneğin `exec()` fonksiyonu ile assignment statement tanımlayabilirsiniz.
```py
def fuck():
    pass
if True:
    exec('a=5')
print(a) # Output: 5
```
`eval()` fonksiyonunun özellikleri ve riskleri `exec()` için de geçerlidir.

bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#exec "https://docs.python.org/3/library/functions.html#exec").

<h1 id="9"><code>filter(function, iterable)</code> Fonksiyonu</h1>

`filter` fonksiyonu, `function` parametresine argüman olarak girilen fonksiyon objesini kullanarak `iterable` parametresine argüman olarak girilen iterable objenin öğelerini filtreler. `filter` fonksiyonu, `function` parametresine argüman olarak girilen fonksiyon objesinin kapsamında tanımlanan kurala uygun iterable objenin öğelerini içeren bir `filter` objesi döndürür. `function` parametresine argüman olarak girilen fonksiyon boolean bir değer döndürmelidir. Bu fonksiyon `True` döndürürse iterable objenin o öğesi filter nesnesine eklenir, `False` döndürürse eklenmez. Filtreleme işlemi bu şekilde gerçekleşir. Örnek:
```py
def tek(sayı):
    return sayı % 2 == 1
l = [400, 176, 64, 175, 355, 13, 207, 298, 397, 386, 31, 120, 120, 236, 241, 123, 249, 364, 292, 153]
print(filter(tek, l))       # Output: <filter object at 0x0000016DF4812FA0>
print(list(filter(tek, l))) # Output: [175, 355, 13, 207, 397, 31, 241, 123, 249, 153]
print(*filter(tek, l))      # Output: 175 355 13 207 397 31 241 123 249 153

notlar = {'Ahmet'   : 60,
          'Sinan'   : 50,
          'Mehmet'  : 45,
          'Ceren'   : 87,
          'Selen'   : 99,
          'Cem'     : 98,
          'Can'     : 51,
          'Kezban'  : 100,
          'Hakan'   : 66,
          'Mahmut'  : 80}

def func(n):
    return n >= 70

print(*filter(func, notlar.values())) # Output: 87 99 98 100 80
```
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#filter "https://docs.python.org/3/library/functions.html#filter").

<h1 id="10"><code>format(value, format_spec)</code> Fonksiyonu</h1>

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#format "https://docs.python.org/3/library/functions.html#format").

<h1 id="11"><code>globals()</code> Fonksiyonu</h1>

Python'da scope'lardaki bilgiler her scope'a özel bir dictionary'de depolanır. Örneğin global scope basit bir dictionary'ten ibarettir. Bu yüzden dictionary methodlarını kullanabiliyorsunuz. Ama bundan kaçınmalısınız çünkü işin sonunda nereden geldiği belli olmayan değerlerle global scope'u kirletmiş olursunuz. Global scope'u gösteren dictionary'de bulunan anahtar ve değerleri görmek için `print(globals())` kullanılır. `globals` adlı bu dictionary'nin içeriği, o anda global scope'da bulunan nesnelere göre farklılık gösterecektir. Örneğin global scope'a `x = 10` assignment statement'ını eklediğinizde, `globals()` dictionary'sine `{'a': 'yeni değer'}` item'ı eklenmiş olur. Örnek:
```py
print(globals(), end="\n\n")
a = "yeni değer"
print(globals())
```
**Output:**
```
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000175D54B1F70>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:\\my_folder\\education\\software\\software_lessons\\python\\python_tutorial\\main\\.md\\TP1.py', '__cached__': None}

{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000175D54B1F70>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:\\my_folder\\education\\software\\software_lessons\\python\\python_tutorial\\main\\.md\\TP1.py', '__cached__': None, 'a': 'yeni değer'}
```

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#globals "https://docs.python.org/3/library/functions.html#globals").

<h1 id="12"><code>hash(object)</code> Fonksiyonu</h1>

`object` parametresine girilen şeyin hash'ini döndürür.

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#hash "https://docs.python.org/3/library/functions.html#hash").

<h1 id="13"><code>help(object)</code> Fonksiyonu</h1>

Python'un ingilizce dökümanlarına ulaşırsınız. **Interactive help** ile özellikle aradığınız bir şeye ulaşabilirsiniz. Bunun için `object` parametresine argüman olarak aratmak istediğiniz şeyi yazmalısınız. Direkt `help()` olarak kullanılırsa genel bir yardım arayüzü açılır ve `help>` ifadesinden sonra herhangi bir şeyi aratabilirsiniz. Hiçbir şey yazmadan direkt enter tuşuna basarsanız çıkış yapar. Herhangi bir şey hakkında direkt bilgi almak için `help(bilgi almak istediğiniz şey)` şeklinde kullanabilirsiniz.

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#help "https://docs.python.org/3/library/functions.html#help").

<h1 id="14"><code>id(object)</code> Fonksiyonu</h1>

`object` parametresine argüman olarak girdiğiniz obje'nin ID'sini döndürür.

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#id "https://docs.python.org/3/library/functions.html#id").

<h1 id="15"><code>isinstance(object, classinfo)</code> Fonksiyonu</h1>

Veri tipi kontrolü için kullanılır.
```py
print(isinstance('ornek', str)) # Output: True
```
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#isinstance "https://docs.python.org/3/library/functions.html#isinstance").

<h1 id="16"><code>issubclass(class, classinfo)</code> Fonksiyonu</h1>

`class` parametresine tanımlanan class, `classinfo` parametresine tanımlanan class'ın subclass'ı mı diye kontrol eder. Örnek:
```py
class base_class():
    pass

class subclass(base_class):
    pass

instance = subclass

print(issubclass(subclass, base_class)) # Output: True
print(issubclass(instance, subclass)) # Output: True
print(issubclass(instance, baseclass)) # Output: True
```
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#issubclass "https://docs.python.org/3/library/functions.html#issubclass").

<h1 id="17"><code>len(s)</code> Fonksiyonu</h1>

`s` parametresine girilen objenin uzunluğunu döndürür. `list` gibi iterable objelerin öğe sayısını bulmak için kullanılabilir.

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#len "https://docs.python.org/3/library/functions.html#len").

<h1 id="18"><code>locals()</code> Fonksiyonu</h1>

Python'da scope'lar dictionary type bir data'dır. Örneğin local scope basit bir dictionary'ten ibarettir. Bu yüzden dictionary methodlarını kullanabiliyorsunuz. Ama bundan kaçınmalısınız çünkü işin sonunda nereden geldiği belli olmayan değerlerle local scope'u kirletmiş olursunuz. Local scope'u gösteren dictionary'de bulunan anahtar ve değerleri görmek için `print(locals())` kullanılır. `locals` adlı bu dictionary'nin içeriği, o anda local scope'da bulunan nesnelere göre farklılık gösterecektir. Örneğin local scope'a `x = 10` assignment statement'ını eklediğinizde, `locals()` dictionary'sine `{'a': 'yeni değer'}` item'ı eklenmiş olur. Örnek:
```py
def local_scope():
    print(locals(), end="\n\n")
    a = "yeni değer"
    print(locals())
local_scope()
```
**Output:**
```
{}

{'a': 'yeni değer'}
```

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#locals "https://docs.python.org/3/library/functions.html#locals").

<h1 id="18"><code>map(function, iterable, ...)</code> Fonksiyonu</h1>

`filter()` fonksiyonu, `iterable` parametresine argüman olarak girilen iterable objenin öğelerini, `function` parametresine argüman olarak girilen fonksiyon objenin `true` döndürmesine göre ayırıyordu/filtreliyordu. `map()` fonksiyonu, `iterable` parametresine argüman olarak girilen iterable objenin öğelerine `function` parametresine argüman olarak girilen fonksiyon objende tanımlı işlemi uygular ve yeni öğeleri içeren bir `map` objesi döndürülür. Örnek:
```py
l = [1,2,3,4,5]
def karesini_al(i):
    return i**2
print(map(karesini_al, l)) # Output: <map object at 0x000001DA2EF2EFA0>
print(list(map(karesini_al, l))) # Output: [1, 4, 9, 16, 25]
```

**Not:** `map` bir class'dır. "`map()` fonksiyonu" olarak bahsedeceğim şey de aslında `map` class'ını kullanarak yaptığımız bir instantiation işlemidir.

**Not:** `map()` fonksiyonuna birden fazla iterable obje tanımlanabilir. `iterable, ...` buradaki üç nokta bu anlama gelmektedir.

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#map "https://docs.python.org/3/library/functions.html#map").

<h1 id="20"><code>slice(start, stop, step)</code> Fonksiyonu</h1>

```py
l = ['ahmet', 'mehmet', 'ayşe', 'senem', 'salih']
dl = slice(0,3)
print(l[dl]) # Output: ['ahmet', 'mehmet', 'ayşe']
```

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#slice "https://docs.python.org/3/library/functions.html#slice").

<h1 id="21"><code>type(object)</code> Fonksiyonu</h1>

Bir objenin type'ını döndürür.
```py
print(type(list())) # Output: <class 'list'>
```

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#type "https://docs.python.org/3/library/functions.html#type").

<h1 id="22"><code>vars(object)</code> Fonksiyonu</h1>

Parametresiz kullanılırsa `locals()` ile aynı çıktıyı verir. Argüman olarak girilen nesnenin örneğin (`vars(str)`) method ve attribute'larını öğrenmek için kullanabilirsiniz. 

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#vars "https://docs.python.org/3/library/functions.html#vars").

<h1 id="23"><code>zip(*iterables)</code> Fonksiyonu</h1>

```py
a1 = ['a', 'b', 'c']
a2 = ['d', 'e', 'f']
a3 = ['h', "i", "j"]

print(zip(a1)) # Output: <zip object at 0x000001AFFB063340>
print(list(zip(a1))) # Output: [('a',), ('b',), ('c',)]

print(zip(a1, a2)) # Output: <zip object at 0x00000246D74226C0>
print(list(zip(a1, a2))) # Output: [('a', 'd'), ('b', 'e'), ('c', 'f')]

print(zip(a1, a2, a3)) # Output: <zip object at 0x00000290FF0D6280>
print(list(zip(a1, a2, a3))) # Output: [('a', 'd', 'h'), ('b', 'e', 'i'), ('c', 'f', 'j')]
```

**Not:** `zip` bir class'dır. "`zip()` fonksiyonu" olarak bahsedeceğim şey de aslında `zip` class'ını kullanarak yaptığımız bir instantiation işlemidir.

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#zip "https://docs.python.org/3/library/functions.html#zip").

<h1 id="24"><code>site</code> Modülü Tarafından Eklenen Constant'lar</h1>

`site` modülü, ([`-S`](https://docs.python.org/3/using/cmdline.html#id3 "https://docs.python.org/3/using/cmdline.html#id3") command-line option'ı belirtilmedikçe, startup (başlatma) sırasında otomatik olarak import edilir) build-in namespace'e birkaç constant ekler. Interactive interpreter shell için kullanışlıdırlar ama programın içinde kullanılmamalıdırlar.

<h2 id="24.1"><code>quit(code=None)</code> Constant</h2>

O anda çalışan programdan çıkmanızı sağlar. Interactive shell'de kullanılırsa o anda açık olan oturum kapanır.

Bilgi için [tıklayınız](https://docs.python.org/3/library/constants.html#quit "https://docs.python.org/3/library/constants.html#quit").

<h2 id="24.2"><code>exit(code=None)</code> Constant</h2>

O anda çalışan programdan çıkmanızı sağlar. Interactive shell'de kullanılırsa o anda açık olan oturum kapanır.

Bilgi için [tıklayınız](https://docs.python.org/3/library/constants.html#exit "https://docs.python.org/3/library/constants.html#exit").

<h2 id="24.3"><code>copyright()</code> Constant</h2>

Python’ın telif haklarına ilişkin bilgilere erişebilirsiniz.
```py
copyright()
```
Bilgi için [tıklayınız](https://docs.python.org/3/library/constants.html#copyright "https://docs.python.org/3/library/constants.html#copyright").

<h2 id="24.4"><code>credits()</code> Constant</h2>

Python programlama diline katkıda bulunanlara teşekkür içeren küçük bir metni çıktı olarak verir.
```py
credits()
```
Bilgi için [tıklayınız](https://docs.python.org/3/library/constants.html#credits "https://docs.python.org/3/library/constants.html#credits").

<h2 id="24.5"><code>license()</code> Constant</h2>

Python’ın lisansına ilişkin epey ayrıntılı metinlere ulaşabilirsiniz.
```py
license()
```
Bilgi için [tıklayınız](https://docs.python.org/3/library/constants.html#license "https://docs.python.org/3/library/constants.html#license").