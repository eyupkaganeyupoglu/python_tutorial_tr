## Ön Bilgi
Python ve python'daki build-in fonksiyonlar **C** diliyle yazılmıştır. Gömülü fonksiyon olarak da bilinen build-in fonksiyonlar, python diline gömülmüş fonksiyonlardır. Python modülleri python diliyle yazılmıştır ama build-in fonksiyonlar **C** diliyle yazılmıştır.

# `all(iterable)`
**Ön bilgi:** *Iterate* ile *Iterate over* kelimelerinin farkı şudur:
- **Iterate**, bir şeyi bir kere tekrarlamak anlamında kullanılır (repeat).
- **Iterate over**, bir şeyi sürekli tekrarlamak anlamında kullanılır (repeatedly).

**Iterator** ile **Iterable** İki farklı kavramdır. Defelarca tekrarlanabilir (can iterate over) herhangi bir şey, **Iterable** (tekrarlanabilir) bir objedir. `str`, `list`, `tuple`, `set`, `frozenset`, `dict` gibi data type'lar **Iterable**'dir. Collection type'lar (arrays) genellikle **iterable**'dir.
- **List**, indexlenebilir (yani sıralı) ve değiştirilebilir (mutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin verir.

- **Tuple**, indexlenebilir (yani sıralı) ve değiştirilemez (immutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin verir.

- **Set**, indexlenemez (yani sırasız) ve değiştirilebilir (mutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin vermez.

- **Dictionary**, indexlenebilir (yani sıralı) ve değiştirilebilir (mutable) bir collection'dır. Python 3.6'dan önce indexlenemezken (yani sırasız),  Python 3.7'den itibaren indexlenebilir (yani sıralı) olmuştur. Duplicate members'a (Bir öğeden birden fazla olması) izin vermez.

[`iter()`](asd) fonksiyonu kullanarak, **Iterable** (tekrarlanabilir) bir objeden, **Iterator** objesi oluşturulabilir. Bunu mümkün kılmak için **Iterable** (tekrarlanabilir) bir objenin class'ının, **Iterator** döndüren bir `__iter__` ya da `0` ile başlayan sıralı (sequential) index'lere sahip `__getitem__` methoduna ihtiyacı vardır. `iter()` fonksiyonuna **Iterable** (tekrarlanabilir) olmayan bir obje verilirse, `TypeError` hatası döndürülür. **Iterator**'ler, objenin bir sonraki item'ına geçmeye yarayan `__next__()` methoduna sahiptir. **Iterator**'ler, `__next__()` methodu kullanarak, **Iterable** bir obje üzerinde iterate (yenileme) yapmak için kullanılan objelerdir.
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
Bir **Iterator**'ün barındırdığı öğe sayısından fazla `next` methodu ya da fonksiyonu kullanılırsa, başka kullanılabilir öğe bulamadığı için `StopIteration` hatası döndürülür.

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
- **Iterate**, bir şeyi bir kere tekrarlamak anlamında kullanılır (repeat).
-  **Iterate over**, bir şeyi sürekli tekrarlamak anlamında kullanılır (repeatedly).

**Iterator** ile **Iterable** İki farklı kavramdır. Defelarca tekrarlanabilir (can iterate over) herhangi bir şey, **Iterable** (tekrarlanabilir) bir objedir. `str`, `list`, `tuple`, `set`, `frozenset`, `dict` gibi data type'lar **Iterable**'dir. Collection type'lar (arrays) genellikle **iterable**'dir.
- **List**, indexlenebilir (yani sıralı) ve değiştirilebilir (mutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin verir.

- **Tuple**, indexlenebilir (yani sıralı) ve değiştirilemez (immutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin verir.

- **Set**, indexlenemez (yani sırasız) ve değiştirilebilir (mutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin vermez.

- **Dictionary**, indexlenebilir (yani sıralı) ve değiştirilebilir (mutable) bir collection'dır. Python 3.6'dan önce indexlenemezken (yani sırasız),  Python 3.7'den itibaren indexlenebilir (yani sıralı) olmuştur. Duplicate members'a (Bir öğeden birden fazla olması) izin vermez.

[`iter()`](asd) fonksiyonu kullanarak, **Iterable** (tekrarlanabilir) bir objeden, **Iterator** objesi oluşturulabilir. Bunu mümkün kılmak için **Iterable** (tekrarlanabilir) bir objenin class'ının, **Iterator** döndüren bir `__iter__` ya da `0` ile başlayan sıralı (sequential) index'lere sahip `__getitem__` methoduna ihtiyacı vardır. `iter()` fonksiyonuna **Iterable** (tekrarlanabilir) olmayan bir obje verilirse, `TypeError` hatası döndürülür. **Iterator**'ler, objenin bir sonraki item'ına geçmeye yarayan `__next__()` methoduna sahiptir. **Iterator**'ler, `__next__()` methodu kullanarak, **Iterable** bir obje üzerinde iterate (yenileme) yapmak için kullanılan objelerdir.
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
Bir **Iterator**'ün barındırdığı öğe sayısından fazla `next` methodu ya da fonksiyonu kullanılırsa, başka kullanılabilir öğe bulamadığı için `StopIteration` hatası döndürülür.

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
Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#any).

# `ascii(object)`
`object` parametresinde firilen objenin yazdırılabilir karşılığını döndürür. ASCII karakterlerin direkt kendisini döndürürken, ASCII olmayan karakterlerin `\x`, `\u` ya da `\U` karşılıklarını döndürür. Ürettiği değer `repr()` fonksiyonuna benzerdir. Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#ascii).
```py
print(ascii('şeker')) # Output: '\\u015feker'
print(repr('şeker')) # Output: 'şeker'
``` 


# *class* `bool([x])`
`x` parametresine girilen argümanın boolean karşılığınız verir. Bu argüman [truth testing procedure](https://docs.python.org/3/library/stdtypes.html#truth)'e göre dönüştürülür. Eğer `x` parametresine `False` yada `False` değerine karşılık gelen bir ifade girilmişse ya da bir değer girilmemişse (**omitted**, yani ihmal etmek) `False`; aksi taktirde `True` döndürür. `bool` class, `int`'in subclass'ıdır. Bu yüzden daha fazla subclass'landırılamaz. Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#bool).

# `breakpoint(*args, **kws)`
Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#breakpoint).

# *class* `bytearray(source, encoding, errors)`
Yeni bir byte array döndürür. `bytearray` class, `0 <= x < 256` arasında mutable (değiştirilebilir) bir integer dizisidir (sequence). [Mutable Sequence Types](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)'da açıklanan mutable (değişirilebilir) dizi (sequence) methodlarının çoğuna ve `byte` type'ın sahip olduğu methodlara sahiptir. Bu methodlara [Bytes and Bytearray Operations](https://docs.python.org/3/library/stdtypes.html#bytes-methods)'dan ulaşabilirsiniz.

https://www.programiz.com/python-programming/methods/built-in/bytearray
https://docs.python.org/3/library/functions.html#func-bytes
https://docs.python.org/3/library/stdtypes.html#bytearray

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#func-bytearray).

# *class* `bytes(source, encoding, errors)`
https://docs.python.org/3/library/functions.html#func-bytes

# `callable(object)`
https://docs.python.org/3/library/functions.html#callable

# `chr(i)`
`i` parametresine girilen integer değerin UNICODE karşılığını döndürür. `ord()` fonksiyonunun tam tersi işleve sahiptir. `i` parametresine girilen argüman 0 ile 1,114,111 arasındaysa bu fonksiyon çalışır. `i` parametresine girilen argüman bu değerleri geçerse `ValueError` verir.

# `@ classmethod`
https://docs.python.org/3/library/functions.html#classmethod

# `compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)`
https://docs.python.org/3/library/functions.html#compile

# *class* `complex(real, imag)`
https://docs.python.org/3/library/functions.html#complex

# `delattr(object, name)`
https://docs.python.org/3/library/functions.html#delattr

# *class* `dict()`
https://docs.python.org/3/library/functions.html#func-dict

# `dir(object)`
https://docs.python.org/3/library/functions.html#dir

