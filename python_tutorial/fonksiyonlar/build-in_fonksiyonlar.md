## Ön Bilgi
Python ve Python'daki build-in fonksiyonlar **C** diliyle yazılmıştır. Gömülü fonksiyon olarak da bilinen build-in fonksiyonlar, Python diline gömülmüş fonksiyonlardır. Python modülleri Python diliyle yazılmıştır ama build-in fonksiyonlar **C** diliyle yazılmıştır. Aşağıda, tutorialin başka bir konusunda değinilmemiş ya da yeterince değinilmemiş build-in fonksiyonların kullanım alanlarından bahsedilmiştir.

# `all(iterable)`

**Ön bilgi:** *Iterate* ile *Iterate over* kelimelerinin farkı şudur:
- **Iterate**, bir şeyi bir kere tekrarlamak anlamında kullanılan bir fiildir (repeat).
- **Iterate over**, bir şeyi sürekli tekrarlamak anlamında kullanılır (repeatedly).

**Iterator** ile **Iterable** İki farklı kavramdır. Defalarca tekrarlanabilir (can iterate over) herhangi bir şey, **Iterable** (tekrarlanabilir) bir objedir. `str`, `list`, `tuple`, `set`, `frozenset`, `dict` gibi data type'lar **Iterable**'dir. Collection type'lar (arrays) genellikle **iterable**'dir.
- **List**, indexlenebilir (yani sıralı) ve değiştirilebilir (mutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin verir.

- **Tuple**, indexlenebilir (yani sıralı) ve değiştirilemez (immutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin verir.

- **Set**, indexlenemez (yani sırasız) ve değiştirilebilir (mutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin vermez.

- **Dictionary**, indexlenebilir (yani sıralı) ve değiştirilebilir (mutable) bir collection'dır. Python 3.6'dan önce indexlenemezken (yani sırasız),  Python 3.7'den itibaren indexlenebilir (yani sıralı) olmuştur. Duplicate members'a (Bir öğeden birden fazla olması) izin vermez.

[`iter()`](https://docs.python.org/3/library/functions.html#iter) fonksiyonu kullanarak, **Iterable** (tekrarlanabilir) bir objeden, **Iterator** objesi oluşturulabilir. Bunu mümkün kılmak için **Iterable** (tekrarlanabilir) bir objenin class'ının, **Iterator** döndüren bir `__iter__` ya da `0` ile başlayan sıralı (sequential) index'lere sahip `__getitem__` methoduna ihtiyacı vardır. `iter()` fonksiyonuna **Iterable** (tekrarlanabilir) olmayan bir obje verilirse, `TypeError` hatası yükseltilir. **Iterator**'ler, objenin bir sonraki item'ına geçmeye yarayan `__next__()` methoduna sahiptir. **Iterator**'ler, `__next__()` methodu kullanarak, **Iterable** bir obje üzerinde iterate (yenileme) yapmak için kullanılan objelerdir.
```py
liste = ["l", "i", "s", "t", "e"]
liste_iter1 = iter(liste)
liste_iter2 = iter(liste)
  
print(next(liste_iter1)) # Output: l
print(next(liste_iter1)) # Output: i
print(next(liste_iter1)) # Output: s
print(next(liste_iter1)) # Output: t
print(next(liste_iter1)) # Output: e
  
print(liste_iter2.__next__()) # Output: l
print(liste_iter2.__next__()) # Output: i
print(liste_iter2.__next__()) # Output: s
print(liste_iter2.__next__()) # Output: t
print(liste_iter2.__next__()) # Output: e
```
Bir **Iterator**'ün barındırdığı öğe sayısından fazla `next` methodu ya da fonksiyonu kullanılırsa, başka kullanılabilir öğe bulamadığı için `StopIteration` hatası yükseltilir.

**Not:** Bütün **Iterator**'ler **Iterable**'dir ama her **Iterable** obje, **Iterator** değildir. Örneğin bir `list` **Iterable** bir objedir ama **Iterator** değildir.

`all(iterable)` fonksiyonu aşağıdaki syntax'a sahiptir:
```py
def all(iterable):
    for element in iterable: # iterable boş olursa for çalışmaz.
        if not element: # element False ise `not False == True` olacağı için çalışır.
            return False
    return True # For çalışmazsa direkt bu satır çalışır.
```
`all(iterable)` fonksiyonu, `iterable` parametresine girilen argümanlara göre aşağıdaki gibi davranır:
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
Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#all).

# `any(iterable)`
**Ön bilgi:** *Iterate* ile *Iterate over* kelimelerinin farkı şudur:
- **Iterate**, bir şeyi bir kere tekrarlamak anlamında kullanılan bir fiildir (repeat).
-  **Iterate over**, bir şeyi sürekli tekrarlamak anlamında kullanılır (repeatedly).

**Iterator** ile **Iterable** İki farklı kavramdır. Defalarca tekrarlanabilir (can iterate over) herhangi bir şey, **Iterable** (tekrarlanabilir) bir objedir. `str`, `list`, `tuple`, `set`, `frozenset`, `dict` gibi data type'lar **Iterable**'dir. Collection type'lar (arrays) genellikle **iterable**'dir.
- **List**, indexlenebilir (yani sıralı) ve değiştirilebilir (mutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin verir.

- **Tuple**, indexlenebilir (yani sıralı) ve değiştirilemez (immutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin verir.

- **Set**, indexlenemez (yani sırasız) ve değiştirilebilir (mutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin vermez.

- **Dictionary**, indexlenebilir (yani sıralı) ve değiştirilebilir (mutable) bir collection'dır. Python 3.6'dan önce indexlenemezken (yani sırasız),  Python 3.7'den itibaren indexlenebilir (yani sıralı) olmuştur. Duplicate members'a (Bir öğeden birden fazla olması) izin vermez.

[`iter()`](https://docs.python.org/3/library/functions.html#iter) fonksiyonu kullanarak, **Iterable** (tekrarlanabilir) bir objeden, **Iterator** objesi oluşturulabilir. Bunu mümkün kılmak için **Iterable** (tekrarlanabilir) bir objenin class'ının, **Iterator** döndüren bir `__iter__` ya da `0` ile başlayan sıralı (sequential) index'lere sahip `__getitem__` methoduna ihtiyacı vardır. `iter()` fonksiyonuna **Iterable** (tekrarlanabilir) olmayan bir obje verilirse, `TypeError` hatası yükseltilir. **Iterator**'ler, objenin bir sonraki item'ına geçmeye yarayan `__next__()` methoduna sahiptir. **Iterator**'ler, `__next__()` methodu kullanarak, **Iterable** bir obje üzerinde iterate (yenileme) yapmak için kullanılan objelerdir.
```py
liste = ["l", "i", "s", "t", "e"]
liste_iter1 = iter(liste)
liste_iter2 = iter(liste)
  
print(next(liste_iter1)) # Output: l
print(next(liste_iter1)) # Output: i
print(next(liste_iter1)) # Output: s
print(next(liste_iter1)) # Output: t
print(next(liste_iter1)) # Output: e
  
print(liste_iter2.__next__()) # Output: l
print(liste_iter2.__next__()) # Output: i
print(liste_iter2.__next__()) # Output: s
print(liste_iter2.__next__()) # Output: t
print(liste_iter2.__next__()) # Output: e
```
Bir **Iterator**'ün barındırdığı öğe sayısından fazla `next` methodu ya da fonksiyonu kullanılırsa, başka kullanılabilir öğe bulamadığı için `StopIteration` hatası yükseltilir.

**Not:** Bütün **Iterator**'ler **Iterable**'dir ama her **Iterable** obje, **Iterator** değildir. Örneğin bir `list` **Iterable** bir objedir ama **Iterator** değildir.

`any(iterable)` fonksiyonu aşağıdaki syntax'a sahiptir:
```py
def any(iterable):
    for element in iterable: # iterable boş olursa for çalışmaz.
        if element: # element False ise `True == True` olacağı için çalışır.
            return True
    return False # For çalışmazsa direkt bu satır çalışır.
```

`any(iterable)` fonksiyonu, `iterable` parametresine girilen argümanlara göre aşağıdaki gibi davranır:
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
Yani `any()` fonksiyonunun `True` sonucunu vermesi için boolean değeri `True` olan 1 tane element ile karşılaşması yeterlidir.
Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#any).


# `breakpoint(*args, **kws)`
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#breakpoint).

# `callable(object)`
Bir nesnenin ‘çağrılabilir’ olup olmadığını denetler. fonksiyonlar çağrılabilir nesnelerdir. Değişkenler ise çağrılabilir nesneler değildir.
```py
import sys
print(callable(open)) # Output: True
print(callable(sys.version)) # Output: False
```
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#callable).

# `compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)`
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#compile).

# `dir(object)`
Parametresiz olarak kullanırsak, mevcut scope'deki öğeleri liste olarak verir. `globals()` ve `locals()`'den farkı, çıktıyı dict olarak değil, liste olarak vermesidir. Nesnelerin method ve property'lerini yazdırır. Örnek:
```py
print(dir(list()))
```
**Output:**
```
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#dir).

# `eval(expression, globals=None, locals=None)`

## Expression (İfadeler)

İngilizcede **expression** denen **ifadeler**, bir değer üretmek için kullanılan kod parçalarıdır. Karakter dizileri, sayılar, operatörler, öteki veri tipleri, liste üreteçleri, sözlük üreteçleri, küme üreteçleri, `fonksiyon()` şeklinde çağırdığırılan fonksiyonlar hep birer **expression**'dır Örneğin:
```py
5
23 + 4
[i for i in range(10)]
len([1,2,3])
```

## Statement (Deyimler)

İngilizcede **statement** olarak adlandırılan **deyimler** ise ifadeleri de kapsayan daha geniş bir kavramdır. Buna göre bütün expression'lar aynı zamanda birer statement'dir. Daha doğrusu, expression'ların bir araya gelmesi ile statement'lar oluşturulabilir. Python'da her line bir statement'dir. **C** programlama dilinde ise ';' işareti **statement terminator** olarak adlandırılır. Örneğin:
```py
a = 5 (Python’da bütün değer atama işlemleri birer deyimdir.)

if a:
    print(a)

for i in range(10):
    print(i)

while True:
    print(1)
    break
```
Bu iki şeyi ayırt etmek için `eval()` kullanılabilir. Çünkü `eval()` parametre olarak sadece expression'ları kabul eder. `eval()` fonksiyonu kendisine verilen stringi yorumlar ve çalıştırır. Yani `eval("print('selam')")` şeklinde bir komut tanımlarsanız, `eval()` bunu önce yorumlar, sonra yorumundan çıkardığı `print('selam')` anlamsal kodu çalıştırır. `eval()`'in bu özelliğini kullanırken dikkat edilmelidir çünkü bu fonksiyon kötü amaçlarla da kullanılabilir. Örneğin sistem dosyalarını silecek bir kodu `eval()` fonksiyonuna yazabilirsiniz. Bunu önlemek için birçok kontrol mekanizması eklenmelidir. `eval()` fonksiyonu, herhangi bir değişken tanımlama işlemi, yani `eval("a=5")` tarzı işlemleri yapamaz. `eval()` fonksiyonu yavaş çalışan bir fonksiyondur. Bu yüzden en son tercih edilir. Örnek:
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
bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#eval).

# `exec(expression, globals=None, locals=None)`
## Expression (İfadeler)

İngilizcede **expression** denen **ifadeler**, bir değer üretmek için kullanılan kod parçalarıdır. Karakter dizileri, sayılar, operatörler, öteki veri tipleri, liste üreteçleri, sözlük üreteçleri, küme üreteçleri, `fonksiyon()` şeklinde çağırdığırılan fonksiyonlar hep birer **expression**'dır Örneğin:
```py
5
23 + 4
[i for i in range(10)]
len([1,2,3])
```

## Statement (Deyimler)

İngilizcede **statement** olarak adlandırılan **deyimler** ise ifadeleri de kapsayan daha geniş bir kavramdır. Buna göre bütün expression'lar aynı zamanda birer statement'dir. Daha doğrusu, expression'ların bir araya gelmesi ile statement'lar oluşturulabilir. Python'da her line bir statement'dir. **C** programlama dilinde ise ';' işareti **statement terminator** olarak adlandırılır. Örneğin:
```py
a = 5 (Python’da bütün değer atama işlemleri birer deyimdir.)

if a:
    print(a)

for i in range(10):
    print(i)

while True:
    print(1)
    break
```
`exec()` fonksiyonu, `eval()`'den farklı olarak sadece expression'ları değil, statement'leri de çalıştırabilir. `exec()` içinde bir variable tanımladığınızda, `exec()`, çalıştığı scope'da bu variable'yi tanımlar.
```py
def fuck():
    pass
if True:
    exec('a=5')
print(a) # Output: 5
```
`eval()` fonksiyonunun özellikleri ve riskleri `exec()` için de geçerlidir. `eval()`'den tek farkı, daha gelişmiş komutları da çalıştırabiliyor. Örneğin `eval("a=5")` gibi bir şey yapamazken, `exec("a=5")` yapabiliyoruz.

bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#exec).

# `filter(function, iterable)`
`function`, ölçütü belirleyen fonksiyon; `iterable`, bu ölçütün uygulanacağı öğedir. İşlemleri `True` ya da `False` olarak değerlendirir. Bu yüzden `function`'in return değeri boolean olmak zorunda. `function`'e girilen fonksiyon, `fonk()` şeklinde değil `fonk` şeklinde olmalıdır.
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

def süz(n):
    return n >= 70

print(*filter(süz, notlar.values())) # Output: 87 99 98 100 80
```
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#filter).

# `format(value, format_spec)`
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#breakpoint).

# `globals()`
Python'da scope'lar dictionary type bir data'dır. Örneğin **global scope** basit bir dictionary'ten ibarettir. Bu yüzden dictionary methodlarını kullanabiliyorsunuz. Ama bundan kaçınmalısınız çünkü işin sonunda nereden geldiği belli olmayan değerlerle **global scope**'u kirletmiş olursunuz.**Global scope**'u gösteren dictionary'de bulunan anahtar ve değerleri görmek için `print(globals())` kullanılır. `globals` adlı bu dictionary'nin içeriği, o anda **global scope**'da bulunan nesnelere göre farklılık gösterecektir. Örneğin **global scope**'a `x = 10` tarzı bir şey eklediğinizde,`globals()`'in outputunda `{'a': 'yeni değer'}` eklenmiş olur.
```py
a = "yeni değer"
print(globals())
```
**Output:**
```
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001B106D01F70>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:\\build_in_fonksiyonlar.py', '__cached__': None, 'a': 'yeni değer'}
```
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#globals).

# `hash(object)`
Verilen obje ve değerine göre rastgele bir karma (rastgele) tamsayı üretir.

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#hash).

# `help(object)`
Python'un ingilizce dökümanlarına ulaşırsınız. **interactive help** ile özellikle aradığınız şeyler ulaşabilirsiniz. direkt `help()` olarak kullanılırsa genel bir yardım arayüzü açılır ve `help>` ifadesinden sonra herhangi bir şeyi aratabilirsiniz. Hiçbir şey yazmadan direkt enter tuşuna basarsanız çıkış yapar. Herhangi bir şey hakkında direkt bilgi almak için `help(bilgi almak istediğiniz şey)` şeklinde kullanabilirsiniz.

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#help).

# `id(object)`
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#id).

# `isinstance(object, classinfo)`
Veri tipi kontrolü için kullanılır.
```py
print(isinstance('ornek', str)) # Output: True
```
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#isinstance).

# `issubclass(class, classinfo)`
`class` parametresine tanımlanan class, `classinfo` parametresine tanımlanan class'ın subclass'ı mı diye kontrol eder. Örnek:
```py
class base_class():
    pass

class sub_class(base_class):
    pass

instance = sub_class

print(issubclass(sub_class, base_class)) # Output: True
print(issubclass(instance, sub_class)) # Output: True
print(issubclass(instance, base_class)) # Output: True
```
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#issubclass).

# `iter(object, sentinel)`
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#iter).

# `len(s)`
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#len).

# `locals()`
Python'da scope'lar dictionary type bir data'dır. Örneğin **local scope** basit bir dictionary'ten ibarettir. Bu yüzden dictionary methodlarını kullanabiliyorsunuz. Ama bundan kaçınmalısınız çünkü işin sonunda nereden geldiği belli olmayan değerlerle **local scope**'u kirletmiş olursunuz.**Local scope**'u gösteren dictionary'de bulunan anahtar ve değerleri görmek için `print(locals())` kullanılır. `locals` adlı bu dictionary'nin içeriği, o anda **local scope**'da bulunan nesnelere göre farklılık gösterecektir. Örneğin **local scope**'a `x = 10` tarzı bir şey eklediğinizde,`locals()`'in outputunda `{'a': 'yeni değer'}` eklenmiş olur.
```py
def local_scope():
    a = "yeni değer"
    print(locals())
local_scope()
```
**Output:**
```
{'a': 'yeni değer'}
```
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#locals).

# `map(function, iterable, ...)`
`filter()`, `iterable`'deki elemanı/elemanları `function`'deki boolean işleme göre ayırır ve sadece `True` sonuç verenleri output olarak verir ama `map()` `iterable`'deki elemana/elemanlara `function`'de belirtilen işlemi uygular. Yani `iterable`'deki elemanların hepsi `function`'deki işleme sokulur ve işleme sokulan `iterable` elemanı/elemanları output olarak verilir. `function`'e girilen fonksiyon, `fonk()` şeklinde değil `fonk` şeklinde olmalıdır.
```py
l = [1,2,3,4,5]
def karesini_al(i):
    return i**2
print(map(karesini_al, l)) # Output: <map object at 0x000001DA2EF2EFA0>
print(list(map(karesini_al, l))) # Output: [1, 4, 9, 16, 25]
```
**Not:** `map()` fonksiyonuna birden fazla iterable obje tanımlanabilir. `iterable, ...` buradaki üç nokta bu anlama gelmektedir.

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#map).

# `next(iterator, default)`
**Ön bilgi:** *Iterate* ile *Iterate over* kelimelerinin farkı şudur:
- **Iterate**, bir şeyi bir kere tekrarlamak anlamında kullanılan bir fiildir (repeat).
-  **Iterate over**, bir şeyi sürekli tekrarlamak anlamında kullanılır (repeatedly).

**Iterator** ile **Iterable** İki farklı kavramdır. Defalarca tekrarlanabilir (can iterate over) herhangi bir şey, **Iterable** (tekrarlanabilir) bir objedir. `str`, `list`, `tuple`, `set`, `frozenset`, `dict` gibi data type'lar **Iterable**'dir. Collection type'lar (arrays) genellikle **iterable**'dir.
- **List**, indexlenebilir (yani sıralı) ve değiştirilebilir (mutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin verir.

- **Tuple**, indexlenebilir (yani sıralı) ve değiştirilemez (immutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin verir.

- **Set**, indexlenemez (yani sırasız) ve değiştirilebilir (mutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin vermez.

- **Dictionary**, indexlenebilir (yani sıralı) ve değiştirilebilir (mutable) bir collection'dır. Python 3.6'dan önce indexlenemezken (yani sırasız),  Python 3.7'den itibaren indexlenebilir (yani sıralı) olmuştur. Duplicate members'a (Bir öğeden birden fazla olması) izin vermez.
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#next).

`next()` fonksiyonu, bir `generator` nesnesinden bir sonraki öğeyi alır.

# `slice(start, stop, step)`
```py
l = ['ahmet', 'mehmet', 'ayşe', 'senem', 'salih']
dl = slice(0,3)
print(l[dl]) # Output: ['ahmet', 'mehmet', 'ayşe']
```
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#slice).

# `type(object)`
Bir objenin type'ını verir.
```py
print(type(list())) # Output: <class 'list'>
```
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#type).

# `vars(object)`
Bulunduğunuz scope içindeki method, fonksiyon, attribute ve listeleri gösterir. parametresiz kullanılırsa `locals()` ile aynı çıktıyı verir. parametre olarak bir değer verilirse örneğin `vars(str)`, o nesnenin method ve attribute'larını öğrenmek için kullanabilirsiniz.

Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#vars).

# `zip(*iterables)`
```py
a1 = ['a', 'b', 'c']
a2 = ['d', 'e', 'f']
print(zip(a1, a2)) # Output: <zip object at 0x00000246D74226C0>
print(list(zip(a1, a2))) # Output: [('a', 'd'), ('b', 'e'), ('c', 'f')]
```
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#zip).

# `site` Modülü Tarafından Eklenen Constant'lar
`site` modülü, ([`-S`](https://docs.python.org/3/using/cmdline.html#id3) command-line option'ı belirtilmedikçe, startup (başlatma) sırasında otomatik olarak import edilir), build-in namespace'e birkaç constant ekler. Interactive interpreter shell için kullanışlıdırlar ama programın içinde kullanılmamalıdırlar.

## `quit(code=None)`
O anda çalışan programdan çıkmanızı sağlar. Interactive shell'de kullanılırsa o anda açık olan oturum kapanır.

Bilgi için [tıklayınız](https://docs.python.org/3/library/constants.html#quit).

## `exit(code=None)`
O anda çalışan programdan çıkmanızı sağlar. Interactive shell'de kullanılırsa o anda açık olan oturum kapanır.

Bilgi için [tıklayınız](https://docs.python.org/3/library/constants.html#exit).

## `copyright()`
Python’ın telif haklarına ilişkin bilgilere erişebilirsiniz.
```py
copyright()
```
Bilgi için [tıklayınız](https://docs.python.org/3/library/constants.html#copyright).

## `credits()`
Python programlama diline katkıda bulunanlara teşekkür içeren küçük bir metni çıktı olarak verir.
```py
credits()
```
Bilgi için [tıklayınız](https://docs.python.org/3/library/constants.html#credits).

## `license()`
Python’ın lisansına ilişkin epey ayrıntılı metinlere ulaşabilirsiniz.
```py
license()
```
Bilgi için [tıklayınız](https://docs.python.org/3/library/constants.html#license).