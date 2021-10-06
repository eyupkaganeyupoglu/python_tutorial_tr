# İçindekiler

- [Iterators (Yenileyiciler)](#1)

<h1 id="1">Iterators (Yenileyiciler)</h1>

**Ön bilgi:** 'Iterate' ile 'Iterate over' kelimelerinin farkı şudur:
- **Iterate:** Bir şeyi bir kere tekrarlamak anlamında kullanılan bir fiildir (repeat).
-  **Iterate over:** Bir şeyi sürekli tekrarlamak anlamında kullanılır (repeatedly).

**Iterator** ile **Iterable** iki farklı kavramdır. Defalarca tekrarlanabilir (can iterate over) herhangi bir obje, iterable (tekrarlanabilir) bir objedir. `str`, `list`, `tuple`, `set`, `frozenset`, `dict`... gibi `__iter__` veya `__getitem__` methodlarına sahip type'lar (class'lar) iterable'dır. Collection type'lar (arrays) genellikle iterable'dir. Bazı collection örnekleri:

- **List**, indexlenebilir (yani sıralı) ve değiştirilebilir (mutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin verir.

- **Tuple**, indexlenebilir (yani sıralı) ve değiştirilemez (immutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin verir.

- **Set**, indexlenemez (yani sırasız) ve değiştirilebilir (mutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin vermez.

- **Dictionary**, indexlenebilir (yani sıralı) ve değiştirilebilir (mutable) bir collection'dır. Python 3.6'dan önce indexlenemezken (yani sırasız),  Python 3.7'den itibaren indexlenebilir (yani sıralı) olmuştur. Duplicate members'a (Bir öğeden birden fazla olması) izin vermez.

[**`iter()`**](https://docs.python.org/3/library/functions.html#iter "https://docs.python.org/3/library/functions.html#iter") fonksiyonu ile, iterable (tekrarlanabilir) bir objenin template'i (şablonu) kullanılarak bir iterator objesi oluşturulabilir. Bunu mümkün kılmak için iterable (tekrarlanabilir) bir objenin class'ının, iterator döndüren bir `__iter__` ya da `0` ile başlayan sıralı (sequential) index'lere sahip `__getitem__` methoduna ihtiyacı vardır.

**Not:** Oluşturulan bu iterator objesi ile iterable obje arasında birbirlerini etkileyecek bir ilişki yoktur, birbirlerinden bağımsız/farklı objelerdir. Örnek:
```py
liste1 = [1,2,3]
liste2 = iter(liste1)

print((type(liste1))) # Output: <class 'list'>
print((type(liste2))) # Output: <class 'list_iterator'>
print(liste1) # Output: [1, 2, 3]
print(liste2) # Output: <list_iterator object at 0x000002F1BC3CDFD0>
print(liste1 == liste2) # Output: False
print(liste1 is liste2) # Output: False
```

**Not:** Bütün iterator'ler iterable'dir ama her iterable obje, iterator değildir. Örneğin `list` type bir obje iterable'dır ama iterator değildir.

**Not:** `iter()` fonksiyonuna iterable (tekrarlanabilir) olmayan bir obje verilirse, `TypeError` hatası yükseltilir. Örnek:
```py
temp = 123
a = iter(temp) # TypeError: 'int' object is not iterable
```

Iterable bir obje tekrarlanamaz, yani içinde gezinemezsiniz. Iterator bir obje tekrarlanabilir, yani içinde gezinilebilir. Iterator'ler bunu mümkün kılan `__next__()` methoduna sahiptir. `__next__()` methodu kullanılarak bir iterator üzerinde iterate (yenileme, yani içinde gezinme) işlemi yapılabilir. Örnek:
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

Bir iterator, içerdiği item sayısından fazla yenilenirse, başka kullanılabilir item bulamadığı için `StopIteration` hatası yükseltilir. Örnek:
```py
liste = [1,2,3]
iterator_exp1 = iter(liste)
iterator_exp2 = iter(liste)

print(iterator_exp2.__next__()) # Output: 1
print(iterator_exp2.__next__()) # Output: 2
print(iterator_exp2.__next__()) # Output: 3
print(iterator_exp2.__next__()) # Output: StopIteration

print(next(iterator_exp1)) # Output: 1
print(next(iterator_exp1)) # Output: 2
print(next(iterator_exp1)) # Output: 3
print(next(iterator_exp1)) # Output: StopIteration
```