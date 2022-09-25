# İçindekiler

- [Kümeler (Sets)](#1)
	- [Set'de İşlemler](#1.1)
	- [Set Üreteçleri (Set Comprehensions)](#1.2)
	- [Set Methodları](#1.3)
		- [`clear()` Methodu](#1.3.1)
		- [`copy()` Methodu](#1.3.2)
		- [`add(element)` Methodu](#1.3.3)
		- [`difference(*s)` Methodu](#1.3.4)
		- [`difference_update(*s)` Methodu](#1.3.5)
		- [`discard(element)` Methodu](#1.3.6)
		- [`remove(element)` Methodu](#1.3.7)
		- [`intersection(*s)` Methodu](#1.3.8)
		- [`intersection_update(*s)` Methodu](#1.3.9)
		- [`isdisjoint(s)` Methodu](#1.3.10)
		- [`issubset(s)` Methodu](#1.3.11)
		- [`issuperset(s)` Methodu](#1.3.12)
		- [`union(*s)` Methodu](#1.3.13)
		- [`update(*s)` Methodu](#1.3.14)
		- [`symmetric_difference(s)` Methodu](#1.3.15)
		- [`symmetric_difference_update(s)` Methodu](#1.3.16)
		- [`pop()` Methodu](#1.3.17)

<h1 id="1">Kümeler (Sets)</h1>

`set`, bildiğimiz matematikteki kümeler gibidir. Her öğeden bir tane bulundurur. Set'ler sırasız (indexlenemezler) ve değiştirilebilir (mutable) data type'lardır. `set(iterable)` build'in fonksiyonu ile set oluşturabilirsiniz veya uygun objeleri set'e dönüştürebilirsiniz. Set'ler süslü parantez (`{}`) ile ifade edilir. Süslü parantezleri (`{}`) sade bir şekilde kullanırsak bir dictionary objesi elde etmiş oluruz. Çünkü `set` type'ın `list`, `tuple` ve `dict` gibi spesifik bir işareti yoktur. Bu yüzden boş `set` objesi elde etmek istiyorsanız `set()` build-in fonksiyonunu kullanmalısınız. Örnek:
```py
s1 = set()
s2 = {"string",
	  1, 1.5, 15+5j,
	  ("tuple", "Tuple"),
	  range(10),
      frozenset({1,2,3,4}),
      True,
      bytes(3)}

print(s1) # Output: set()
print(s2) # Output: {'string', 1, 1.5, range(0, 10), b'\x00\x00\x00', frozenset({1, 2, 3, 4}), ('tuple', 'Tuple'), (15+5j)}
```
`bool`, `int`, `float`, `complex`, `tuple`, `frozenset`, `bytes`, `str`, `range` değiştirilemez (immutable) type'lar oldukları için set'e öğe olarak girilebilirler. `list`, `set`, `dict`, `bytearray` ve user-defined class'lar değiştirilebilir (mutable) data type'lar oldukları için set'e öğe olarak girilemezler.

**Not:** Set data type'ı sırasız olduğu için örneğin `print()` fonksiyonu ile yazdırılmak istense, program her çalıştırıldığında öğeler farklı sırada yazdırılabilir. Bu durum öğelerin **hashlenmesi** ile ilgilidir. Hash dediğimiz şey, veriyi daha az kaynak kullanarak ifade etmek için ilgili hashing algoritmasının ürettiği değerdir. Örneğin 1024 bitlik bir mesajı bir hashing algoritması 128 bitlik yapıya indirgeyebilir. Python'da da böyledir. Bir Python programı çalıştırıldığında, o programdaki değerler bir hash'e sahip olur. Çoğu immutable built-in object hashable'dir. `list`, `set`, `dict`, `bytearray` gibi mutable container'lar hashable değildir. `tuple` ve `frozenset` gibi mutable container'lar hashable içeriğe sahipse hashable'dir. Çok kaynak kullanılarak ifade edilebilen değerlerin hash'leri program her çalıştırıldığında değişir ama az kaynak kullanılarak ifade edilebilen değerlerin hash'leri her zaman aynıdır. `bool`, `int`, `float`, `complex` ve `range` type'ların hash'leri hiçbir zaman değişmez çünkü bu type'lar az kaynak harcarlar ama `bytes` ve `str` type'ların hash'leri program her baştan çalıştırıldığında değişir çünkü bu type'lar çok kaynak harcarlar. `tuple` ve `frozenset` type'ları da içerdiği değerlere göre çok ya da az kaynak harcayabilir. **Hash** hakkında daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#hash "https://docs.python.org/3/library/functions.html#hash"). **Hashable** hakkında daha fazla bilgi için [tıklayınız](https://docs.python.org/3/glossary.html#term-hashable "https://docs.python.org/3/glossary.html#term-hashable").

**Not:** `None` type da değiştirilemez (immutable) bir type'dır ve hash'i her zaman sabittir. Ama farklı makinelerde bu hash değeri değişebilir. Örneğin bir makinede `-9223363241081056563` hash'ine sahipkenbaşka bir makinede `-9223363242374385203` hash'ine sahip olmuştur.

**Not:** `set` type bir objenin öğeleri, öğelerin hash'lerinin sayısal büyüklüğüne göre mi sıralanıyor sorusunun cevabı "Hayır".

<h2 id="1.1">Set'de İşlemler</h2>

Iterable bütün type'ları set'e dönüştürebilirsin. Örnek:
```py
print("set:", {"A", "B", "C"})                       # Output: set: {'A', 'C', 'B'}
print("frozenset:", set(frozenset({"A", "B", "C"}))) # Output: frozenset: {'A', 'C', 'B'}
print("list:", set(["A", "B", "C"]))                 # Output: list: {'A', 'C', 'B'}
print("tuple:", set(("A", "B", "C")))                # Output: tuple: {'A', 'C', 'B'}
print("str:", set("ABC"))                            # Output: str: {'A', 'C', 'B'}
print("dict:", set({"A": "a", "B": "b", "C": "c"}))  # Output: dict: {'A', 'C', 'B'}
print("bytearray:", set(bytearray('ABC', 'utf-8')))  # Output: bytearray: {65, 66, 67}
print("range:", set(range(3)))                       # Output: range: {0, 1, 2}
```

**Not:** `__iter__()` methoduna sahip bütün class'lardan türetilen objeler (instance) iterable'dır. Bazı iterable obje örnekleri: `frozenset`, `set`, `list`, `tuple`, `str`, `dict`, `bytearray`, `range`, `memoryview`, `enumerate`, `filter`, `map`, `reversed`, `zip`

Set'lerin öğe sayısına `len()` fonksiyonuyla ulaşılabilir. Örnek:
```py
s1 = {1,2,3,4,5}
print(len(s1)) # Output: 5
```

Set type, aritmetik (sayısal) işlemleri desteklemez. Örnek:
```py
print({1,2,3} + {4,5,6}) # TypeError: unsupported operand type(s) for +: 'set' and 'set'
print({1,2,3} * 2) # TypeError: unsupported operand type(s) for *: 'set' and 'int'
```

Set objesini tamamen silmek:
```py
s1 = {1,2,3,4}
del s1
print(s1) # NameError: name 's1' is not defined
```

Bir set'i kopyalamak ve sonuçları:
```py
s1 = {1,2,3,4}
s2 = s1
print(s1) # Output: {1, 2, 3, 4}
print(s2) # Output: {1, 2, 3, 4}
print(id(s1) == id(s2)) # Output: True

s1.add(5)
print(s1) # Output: {1, 2, 3, 4, 5}
print(s2) # Output: {1, 2, 3, 4, 5}
```
Set, değiştirilebilir (mutable) bir data type olduğu için assignment operator (`=`) kullanılarak bir set objesini yukarıdaki gibi farklı bir variable'a atarsanız, son durumda oluşan objeler aynı set objesine atıfta bulunacağı (refers to) için birinde yapılan değişiklikler diğerini de etkiler. Bu durum değiştirilemez (immutable) data type'lar için geçerli değildir çünkü değiştirilemez (immutable) data type'ları değiştirmek için yeniden tanımlama (redefinition) işlemi yapmak zorundayız. Yeniden tanımlama (redefinition) işlemi sonucunda da mevcut obje farklı bir objeye dönüştüğü için birbirinden bağımsız olacak.

<h2 id="1.2">Set Üreteçleri (Set Comprehensions)</h2>

**Comprehension**, tek satırda oluşturduğumuz **Generator** (daha sonra anlatılacak) yapısına verilen isimdir. `(expression for item in iterable)` syntax'ına sahiptir (parantezler dahil). Bu generator yapısı (**Generator Comprehension**) bir generator objesi oluşturmakta kullanılır. Daha sonra bu generator objesini set type'a dönüştürerek Set Comprehension oluşturabiliriz. Örnek:
```py
set_exp = {i for i in range(1,4)}
print(set_exp, type(set_exp)) # Output: {1, 2, 3} <class 'set'>
```
Bu konu daha sonra comprehension başlığı altında daha detaylı anlatılacak.

<h2 id="1.3">Set Methodları</h2>

<h3 id="1.3.1"><code>clear()</code> Methodu</h3>

Uygulandığı set'in içeriğini siler. `del` statement ile set objesini tamamen silmeden sadece set'in içini boşaltmak isteyenler için uygun bir tercihtir. Örnek:
```py
set_exp = {'Ahmet', 'Mehmet', 'Ceylan'}
set_exp.clear()
print(set_exp) # Output: set()
```

<h3 id="1.3.2"><code>copy()</code> Methodu</h3>

Uygulandığı set'in bir kopyasını oluşturur. `set_exp1 = set_exp2` gibi assignment operator kullanarak set kopyalama yönteminden farkı, yeni set ile eski set'in birbirinden bağımsız, farklı (farklı ID'lere sahip) objeler olmasıdır. Böylece birinde yapılan değişikli diğerini etkilemez. Örnek:
```py
set_exp = {1,2,3,4,5}
set_copy1 = set_exp
print(id(set_exp) == id(set_copy1)) # Output: True
print(set_exp) # Output: {1, 2, 3, 4, 5}
print(set_copy1) # Output: {1, 2, 3, 4, 5}

set_copy1.add("Bir")
print(set_exp) # Output: {'Bir', 1, 2, 3, 4, 5}
print(set_copy1) # Output: {'Bir', 1, 2, 3, 4, 5}

set_copy2 = set_exp.copy()
print(id(set_exp) == id(set_copy2)) # Output: False
print(set_exp) # Output: {'Bir', 1, 2, 3, 4, 5}
print(set_copy2) # Output: {'Bir', 1, 2, 3, 4, 5}

set_copy2.add("İki")
print(set_exp) # Output: {'Bir', 1, 2, 3, 4, 5}
print(set_copy2) # Output:{'Bir', 1, 2, 3, 4, 5, 'İki'}
```

<h3 id="1.3.3"><code>add(element)</code> Methodu</h3>

`element` parametresine argüman olarak girilen değeri set'e öğe ekmeleye yarar. Eklenecek öğrenin değiştirilemez (immutable) olması gerekir. Aksi halde `TypeError` hatası yükseltilir. Set'de zaten bulunan bir öğe eklenmeye çalışırlırsa set'de bir değişiklik olmaz çünkü set'lerde her öğeden bir tane bulunabilir. Örnek:
```py
set_exp = {"bir", "iki", "üç"}
set_exp.add("dört")
print(set_exp) # Output: {"bir", "iki", "üç", "dört"}
set_exp.add("bir")
print(set_exp) # Output: {"bir", "iki", "üç", "dört"}
```

<h3 id="1.3.4"><code>difference(*s)</code> Methodu</h3>

Uygulandığı set ile `*s` parametresine girilen set'lerin farkını alır ve sonucu döndürür. `A` ve `B` iki set type obje olmak üzere, `A - B` işleminin şematik gösterimi:

![](https://i.ibb.co/P4rYJcy/a-fark-b.png)

Yukarıdaki şemaya göre `A - B` işlemi "`A`'da olup `B`'de olmayan" anlamına gelmektedir. Örnek:
```py
print({1,2,3,4,5}.difference({1,2,3})) # Output: {4, 5}
print({1,2,3,4,5}.difference({1,},{2,},{3,})) # Output: {4, 5}
print({1,2,3,4,5}.difference({1,2,3},{1,4})) # Output: {5}
```

**Not:** `difference` methodu, uygulandığı set'i değiştirmez. Ama bir başka method olan `difference_update` değiştirir.


<h3 id="1.3.5"><code>difference_update(*s)</code> Methodu</h3>

Uygulandığı set ile `*s` parametresine girilen set'lerin farkını alır ama `difference` methodundaki gibi sonucu döndürmez, bunun yerine uygulandığı set'i değiştirir. `A` ve `B` iki set type obje olmak üzere, `A - B` işleminin şematik gösterimi:

![](https://i.ibb.co/P4rYJcy/a-fark-b.png)

Yukarıdaki şemaya göre `A - B` işlemi "`A`'da olup `B`'de olmayan" anlamına gelmektedir. Örnek:
```py
A = {1,2,3,4,5}
A.difference_update({1,2,3})
print(A) # Output: {4, 5}

A = {1,2,3,4,5}
A.difference_update({1,},{2,},{3,})
print(A) # Output: {4, 5}

A = {1,2,3,4,5}
A.difference_update({1,2,3},{1,4})
print(A) # Output: {5}
```

**Not:** `difference_update` methodu, uygulandığı set'i değiştirir. Ama bir başka method olan `difference` değiştirmez.

<h3 id="1.3.6"><code>discard(element)</code> Methodu</h3>

`element` parametresine argüman olarak girilen değeri set'den silmeye yarar. İşlev bakımından `add` methodunun zıttıdır. `element` parametresinde belirtilen değer set'de yoksa hiçbir şey yapmaz. Örnek:
```py
A = {1,2,3,4,5}
A.discard(1)
print(A) # Output: {2, 3, 4, 5}
A.discard(6)
print(A) # Output: {2, 3, 4, 5}
```

<h3 id="1.3.7"><code>remove(element)</code> Methodu</h3>

`element` parametresine argüman olarak girilen değeri set'den silmeye yarar. İşlev bakımından `add` methodunun zıttını, `discard` methodunun benzerini yapar ama `element` parametresinde belirtilen değer set'de yoksa `KeyError` hatası yükseltir. Örnek:
```py
A = {1,2,3,4,5}
A.remove(1)
print(A) # Output: {2, 3, 4, 5}
A.remove(6) # KeyError: 6
```

<h3 id="1.3.8"><code>intersection(*s)</code> Methodu</h3>

Uygulandığı set ile `*s` parametresine girilen set'lerin kesişimini alır ve sonucu döndürür. İki set'i kesişimini almak için `&` operator'ı da kullanılabilir. `A` ve `B` iki set type obje olmak üzere, `A & B` işleminin şematik gösterimi:

![](https://i.ibb.co/LdKstBY/a-kesi-im-b.png)

Yukarıdaki şemaya göre `A & B` işlemi "`A` ve `B`'de bulunan" anlamına gelmektedir. Örnekler:

![](https://i.ibb.co/NTTF2th/12345-kesi-im-1236.png)

Yukarıdaki şemanın ifade ettiği kod:
```py
A = {1,2,3,4,5}
B = {1,2,3,6}
print(A.intersection(B)) # Output: {1, 2, 3}
print(A & B) # Output: {1, 2, 3}
```

<hr>

![](https://i.ibb.co/jvVsmY1/12345-1-2.png)

Yukarıdaki şemanın ifade ettiği kod:
```py
A = {1,2,3,4,5}
B = {1,}
C = {2,}
print(A.intersection(B,C)) # Output: set() (boş küme)
print(A & B & C) # Output: set() (boş küme)
```

<hr>

![](https://i.ibb.co/K6hSgCj/12345-123-14.png)

Yukarıdaki şemanın ifade ettiği kod:
```py
A = {1,2,3,4,5}
B = {1,2,3}
C = {1,4}
print(A.intersection(B,C)) # Output: {1}
print(A & B & C) # Output: {1}
```

<h3 id="1.3.9"><code>intersection_update(*s)</code> Methodu</h3>

Uygulandığı set ile `*s` parametresine girilen set'lerin farkını alır ama `intersection` methodundaki gibi sonucu döndürmez, bunun yerine uygulandığı set'i değiştirir. İki set'i kesişimini almak için `&` operator'ı da kullanılabilir. `A` ve `B` iki set type obje olmak üzere, `A & B` işleminin şematik gösterimi:

![](https://i.ibb.co/LdKstBY/a-kesi-im-b.png)

Yukarıdaki şemaya göre `A & B` işlemi "`A` ve `B`'de bulunan" anlamına gelmektedir. Örnekler:

![](https://i.ibb.co/NTTF2th/12345-kesi-im-1236.png)

Yukarıdaki şemanın ifade ettiği kod:
```py
A = {1,2,3,4,5}
B = {1,2,3,6}
A.intersection_update(B)
print(A) # Output: {1, 2, 3}
print(A & B) # Output: {1, 2, 3}
```

<hr>

![](https://i.ibb.co/jvVsmY1/12345-1-2.png)

Yukarıdaki şemanın ifade ettiği kod:
```py
A = {1,2,3,4,5}
B = {1,}
C = {2,}
A.intersection_update(B,C)
print(A) # Output: set() (boş küme)
print(A & B & C) # Output: set() (boş küme)
```

<hr>

![](https://i.ibb.co/K6hSgCj/12345-123-14.png)

Yukarıdaki şemanın ifade ettiği kod:
```py
A = {1,2,3,4,5}
B = {1,2,3}
C = {1,4}
A.intersection_update(B,C)
print(A) # Output: {1}
print(A & B & C) # Output: {1}
```

<h3 id="1.3.10"><code>isdisjoint(s)</code> Methodu</h3>

Uygulandığı set objesi ile `s` parametresine argüman olarak girilen set objesinin kesişiminin boş olup olmadığını sorgular. Boşsa `True`, diğer durumlarda `False` döndürür. Örnek:
```py
A = {1,2,3,4,5}
B = {1,2,3}
C = {6,7}
print(A.isdisjoint(B)) # Output: False (Boş değil çünkü kesişimi {1,2,3})
print(A.isdisjoint(C)) # Output: True (Boş)
```

<h3 id="1.3.11"><code>issubset(s)</code> Methodu</h3>

Uygulandığı set objesinin, `s` parametresine argüman olarak girilen set objesinin alt kümesi olup olmadığını sorgular. Alt kümesi ise `True`, diğer durumlarda `False` döndürür.

**Alt Küme:** `A` ve `B` iki küme olmak üzere, `A` kümesi `B` kümesini kapsıyorsa (başka bir deyişle `B` kümesinin bütün elemanları `A` kümesinde de varsa), `B` kümesi `A` kümesinin alt kümesidir.

Örnek:
```py
A = {1,2,3,4,5}
B = {1,2,3,4}
C = {1,2,3}
D = {1,2}
E = {1}
F = set()
print(A.issubset(A)) # Output: True (Her küme kendisinin alt kümesidir)
print(B.issubset(A)) # Output: True
print(C.issubset(A)) # Output: True
print(D.issubset(A)) # Output: True
print(E.issubset(A)) # Output: True
print(F.issubset(A)) # Output: True (Boş küme, bütün kümelerin alt kümesidir)
```
`A` kümesi diğer kümeleri kapsadığı için diğer kümeler `A` kümesinin alt kümesidir. Aykırı bir örnek:
```py
A = {1,2,3,4,5}
B = {1,2,3,4,5,6}
print(B.issubset(A)) # Output: False (A kümesi B kümesini kapsamaz)
```

<h3 id="1.3.12"><code>issuperset(s)</code> Methodu</h3>

Uygulandığı set objesinin, `s` parametresine argüman olarak girilen set objesinin üst kümesi olup olmadığını sorgular. Üst kümesi ise `True`, diğer durumlarda `False` döndürür.

**Üst Küme:** `A` ve `B` iki küme olmak üzere, `A` kümesi `B` kümesini kapsıyorsa (başka bir deyişle `B` kümesinin bütün elemanları `A` kümesinde de varsa), `A` kümesi `B` kümesinin üst kümesidir.

Örnek:
```py
A = {1,2,3,4,5}
B = {1,2,3,4}
C = {1,2,3}
D = {1,2}
E = {1}
F = set()
print(A.issuperset(A)) # Output: True (Her küme kendisinin üst kümesidir)
print(A.issuperset(B)) # Output: True
print(A.issuperset(C)) # Output: True
print(A.issuperset(D)) # Output: True
print(A.issuperset(E)) # Output: True
print(A.issuperset(F)) # Output: True (Bütün kümeler, boş kümenin üst kümesidir)
```
Aykırı bir örnek:
```py
A = {1,2,3,4,5}
B = {1,2,3,4,5,6}
print(A.issuperset(B)) # Output: False (B kümesi A kümesini kapsamaz)
```

<h3 id="1.3.13"><code>union(*s)</code> Methodu</h3>

Uygulandığı set ile `*s` parametresine girilen set'lerin birleşimini alır ve sonucu döndürür. İki set'i birleşimini almak için `|` operator'ı da kullanılabilir. `A` ve `B` iki set type obje olmak üzere, `A | B` işleminin şematik gösterimi:

![](https://i.ibb.co/CvjTRYs/a-birle-im-b.png)

Yukarıdaki şemaya göre `A | B` işlemi "`A` veya `B`'de bulunan" anlamına gelmektedir. Örnekler:

![](https://i.ibb.co/kQByHRV/12345-kesi-im-1236.png)

Yukarıdaki şemanın ifade ettiği kod:
```py
A = {1,2,3,4,5}
B = {1,2,3,6}
print(A.union(B)) # Output: {1, 2, 3, 4, 5, 6}
print(A | B) # Output: {1, 2, 3, 4, 5, 6}
```

<hr>

![](https://i.ibb.co/xFN9bnz/12345-1-2.png)

Yukarıdaki şemanın ifade ettiği kod:
```py
A = {1,2,3,4,5}
B = {1,}
C = {2,}
print(A.union(B,C)) # Output: {1, 2, 3, 4, 5}
print(A | B | C) # Output: {1, 2, 3, 4, 5}
```

<hr>

![](https://i.ibb.co/PCjfjNY/12345-123-14.png)

Yukarıdaki şemanın ifade ettiği kod:
```py
A = {1,2,3,4,5}
B = {1,2,3}
C = {1,4}
print(A.union(B,C)) # Output: {1, 2, 3, 4, 5}
print(A | B | C) # Output: {1, 2, 3, 4, 5}
```

<h3 id="1.3.14"><code>update(*s)</code> Methodu</h3>

`*s` parametresine argüman olarak girilen iterable objelerin elemanlarını, `update` methodunun uygulandığı set'e ekleyerek set'i günceller. Örnek:
```py
A = (1,2)
B = [3,4]
C = {5:"beş", 6:"altı"}
D = {7,8}
E = "90"
F = set()
G = set()

F.update(A)
print(F) # Output: {1, 2}

F.update(B)
print(F) # Output: {1, 2, 3, 4}

F.update(C)
print(F) # Output: {1, 2, 3, 4, 5, 6}

F.update(D)
print(F)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

F.update(E)
print(F)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, '9', '0'}

G.update(A,B,C,D,E)
print(G)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, '9', '0'}
```
`update` methodunun eşdeğeri:
```py
A = (1,2)
B = [3,4]
C = {5:"beş", 6:"altı"}
D = {7,8}
E = "90"
F = set()

for i in A,B,C,D,E:
    for j in i:
        F.add(j)

print(F) # Output: {1, 2, 3, 4, 5, 6, 7, 8, '0', '9'}
```

<h3 id="1.3.15"><code>symmetric_difference(s)</code> Methodu</h3>

`A` ve `B` iki set objesi olmak üzere, `A.difference(B) | B.difference(A)` (yani `(A - B) | (B - A)`) işleminin sonucunu döndürür. Bu işlemin şematik gösterimi:

![](https://i.ibb.co/3y5bxKY/symmetric-difference.png)

Örnek:

![](https://i.ibb.co/f8mtZhV/12345-12678.png)

Yukarıdaki şemanın ifade ettiği kod:
```py
A = {1,2,3,4,5}
B = {1,2,6,7,8}
print(A.symmetric_difference(B)) # Output: {3, 4, 5, 6, 7, 8}
```

<h3 id="1.3.16"><code>symmetric_difference_update(s)</code> Methodu</h3>

`A` ve `B` iki set objesi olmak üzere, `A.difference(B) | B.difference(A)` (yani `(A - B) | (B - A)`) işleminin sonucu döndürmez, bunun yerine uygulandığı set'i değiştirir. Bu işlemin şematik gösterimi:

![](https://i.ibb.co/3y5bxKY/symmetric-difference.png)

Örnek:

![](https://i.ibb.co/f8mtZhV/12345-12678.png)

Yukarıdaki şemanın ifade ettiği kod:
```py
A = {1,2,3,4,5}
B = {1,2,6,7,8}
A.symmetric_difference_update(B)
print(A) # Output: {3, 4, 5, 6, 7, 8}
```

<h3 id="1.3.17"><code>pop()</code> Methodu</h3>

Uygulandığı set'in rastgele bir öğesini önce döndürür sonra siler. Örnek:
```py
A = {1,2,3,4,5}
print(A.pop()) # Output: 1
print(A) # Output: {2, 3, 4, 5}
```
```py
A = {1,2,3,4,5}
print(A.pop()) # Output: 1
print(A) # Output: {2, 3, 4, 5}
```
```py
A = {1,2,3,4,5}
print(A.pop()) # Output: 1
print(A) # Output: {2, 3, 4, 5}
```
`pop` merhodu, (yukarıdaki örnekte integer gibi) hash'leri her zaman aynı olan data type'larda her zaman aynı öğeyi silerken, (aşağıdaki örnekte string gibi) hash'leri her seferinde değişen data type'larda her zaman aynı öğeyi silmeyebilir.
```py
B = {"1","2","3","4","5"}
print(B.pop()) # Output: 3
print(B) # Output: {'2', '1', '4', '5'}
```
```py
B = {"1","2","3","4","5"}
print(B.pop()) # Output: 1
print(B) # Output: {'3', '5', '2', '4'}
```
```py
B = {"1","2","3","4","5"}
print(B.pop()) # Output: 4
print(B) # Output: {'5', '3', '1', '2'}
```