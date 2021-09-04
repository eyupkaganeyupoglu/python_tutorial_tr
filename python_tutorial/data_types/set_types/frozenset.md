# İçindekiler

- [Dondurulmuş Kümeler (Frozenset)](#1)
	- [Frozenset'de İşlemler](#1.1)
	- [Frozenset Üreteçleri (Frozenset Comprehensions)](#1.2)
	- [Frozenset Methodları](#1.3)
        - [`copy()` Methodu](#1.3.1)
        - [`difference(*s)` Methodu](#1.3.2)
        - [`intersection(*s)` Methodu](#1.3.3)
        - [`union(*s)` Methodu](#1.3.4)
        - [`isdisjoint(s)` Methodu](#1.3.5)
        - [`issubset(s)` Methodu](#1.3.6)
        - [`issuperset(s)` Methodu](#1.3.7)
        - [`symmetric_difference(s)` Methodu](#1.3.8)

<h1 id="1">Dondurulmuş Kümeler (Frozenset)</h1>

`frozenset`, bildiğimiz matematikteki kümeler gibidir. Her öğeden bir tane bulundurur. Frozenset'ler sırasız (indexlenemezler) ve değiştirilemez (immutable) data type'lardır. `frozenset(iterable)` build'in fonksiyonu ile frozenset oluşturabilirsiniz veya uygun objeleri frozenset'e dönüştürebilirsiniz. Örnek:
```py
fs1 = frozenset()
fs2 = frozenset({"string",
	  1, 1.5, 15+5j,
	  ("tuple", "Tuple"),
	  range(10),
      frozenset({1,2,3,4}),
      True,
      bytes(3)})

print(fs1) # Output: frozenset()
print(fs2) # Output: frozenset({1, 1.5, range(0, 10), 'string', b'\x00\x00\x00', frozenset({1, 2, 3, 4}), ('tuple', 'Tuple'), (15+5j)})
```
`bool`, `int`, `float`, `complex`, `tuple`, `frozenset`, `bytes`, `str`, `range` değiştirilemez (immutable) type'lar oldukları için frozenset'e öğe olarak girilebilirler. `list`, `set`, `dict`, `bytearray` ve user-defined class'lar değiştirilebilir (mutable) data type'lar oldukları için frozenset'e öğe olarak girilemezler.

Frozenset data type'ı sırasız olduğu için örneğin `print()` fonksiyonu ile yazdırılmak istense, program her çalıştırıldığında öğeler farklı sırada yazdırılabilir. Bu durum öğelerin **hashlenmesi** ile ilgilidir. Hash dediğimiz şey, veriyi daha az kaynak kullanarak ifade etmek için ilgili hashing algoritmasının ürettiği değerdir. Örneğin 1024 bitlik bir mesajı bir hashing algoritması 128 bitlik yapıya indirgeyebilir. Python'da da böyledir. Bir Python programı çalıştırıldığında, o programdaki değerler bir hash'e sahip olur. Çok kaynak kullanılarak ifade edilebilen değerlerin hash'leri, program her çalıştırıldığında değişir. Ama az kaynak kullanılarak ifade edilebilen değerlerin hash'leri her zaman aynıdır. Örnek:
```py
# Programı İlk Çalıştırmamız
print(hash(tuple([1,2,3])))                # Output: 529344067295497451
print(hash(tuple(["1","2","3"])))          # Output: 7401844457185675310
print(hash(frozenset([1,2,3])))            # Output: -272375401224217160
print(hash(frozenset(["1","2","3"])))      # Output: -2204149807619723895
print(hash(bytes(12)))                     # Output: 6673985660609553768
print(hash("String"))                      # Output: 4966508039248316583

print(hash(bool(True)), hash(bool(False))) # Output: 1 0
print(hash(123))                           # Output: 123
print(hash(123.123))                       # Output: 283618690133295227
print(hash(123+123j))                      # Output: 123000492
print(hash(range(10)))                     # Output: -7546101314042312252
```
```py
# Programı İkinci Çalıştırmamız
print(hash(tuple([1,2,3])))                # Output: 529344067295497451
print(hash(tuple(["1","2","3"])))          # Output: -6370647310685844327
print(hash(frozenset([1,2,3])))            # Output: -272375401224217160
print(hash(frozenset(["1","2","3"])))      # Output: 7667363132115089216
print(hash(bytes(12)))                     # Output: 3239916383633325594 
print(hash("String"))                      # Output: -3850919489988372704

print(hash(bool(True)), hash(bool(False))) # Output: 1 0
print(hash(123))                           # Output: 123
print(hash(123.123))                       # Output: 283618690133295227
print(hash(123+123j))                      # Output: 123000492
print(hash(range(10)))                     # Output: -7546101314042312252
```
```py
# Programı Üçüncü Çalıştırmamız
print(hash(tuple([1,2,3])))                # Output: 529344067295497451
print(hash(tuple(["1","2","3"])))          # Output: 6340878864105529814
print(hash(frozenset([1,2,3])))            # Output: -272375401224217160
print(hash(frozenset(["1","2","3"])))      # Output: -5783254467061130136
print(hash(bytes(12)))                     # Output: -7182886563342320287
print(hash("String"))                      # Output: 8500247573865546266

print(hash(bool(True)), hash(bool(False))) # Output: 1 0
print(hash(123))                           # Output: 123
print(hash(123.123))                       # Output: 283618690133295227
print(hash(123+123j))                      # Output: 123000492
print(hash(range(10)))                     # Output: -7546101314042312252
```
`bool`, `int`, `float`, `complex` ve `range` type'ların hash'leri hiçbir zaman değişmez çünkü bu type'lar az kaynak harcarlar. Ama `bytes` ve `str` type'ların hash'leri, program her baştan çalıştırıldığında değişir çünkü bu type'lar çok kaynak harcarlar. `tuple` ve `frozenset` type'ları da içerdiği değerlere göre çok ya da az kaynak harcayabilir. Örneğin öğeleri çok kaynak harcayan string veya bytes type olan bir tuple veya frozenset objelerinin hash'i, program her çalıştırıldığında değişirken; öğeleri az kaynak harcayan type'lar olan tuple veya frozenset objelerinin hash'i hep aynıdır. Yukarıda örneği var.

**Not:** `list`, `set`, `dict`, `bytearray` gibi değiştirilebilir (mutable) type'lar hash'lenemez. Hash'lenmeye çalışılırsa `TypeError: unhashable type: 'list'`, `TypeError: unhashable type: 'set'`, `TypeError: unhashable type: 'dict'`, `TypeError: unhashable type: 'bytearray'` gibi hatalar yükseltilir. **Hash** hakkında daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#hash "https://docs.python.org/3/library/functions.html#hash"). **Hashable** hakkında daha fazla bilgi için [tıklayınız](https://docs.python.org/3/glossary.html#term-hashable "https://docs.python.org/3/glossary.html#term-hashable").

**Not:** `None` type da değiştirilemez (immutable) bir type'dır ve hash'i her zaman sabittir. Ama farklı makinelerde bu hash değeri değişebilir. Örneğin benim makinede (bilgisayarımda) `-9223363241081056563` hash'ine sahipken, bir arkadaşımın bilgisayarında `-9223363242374385203` hash'ine sahiptir.

**Not:** Frozenset, öğelerini hash'in sayısal büyüklüğüne göre mi sıralıyor diye bakmayın, ben baktım ve öyle bir şey yok sanırım. Örnek:
```py
frozenset_exp = {"1", "2", "3"}
for i in frozenset_exp:
    print(i, hash(i))
print(frozenset_exp)
```
**Output:**
```
2 -3778677644095488240
1 7888383718303043910
3 2738165215596315832
{'2', '1', '3'}
```
Burada `'2'` string'ini hash'inin sayısal değeri diğerlerinden küçük olmasına rağmen ilk sırada. Bu da hash'lerin sıralanışının sayısal büyüklükleriyle alakalı olmadığını kanıtlıyor. Bu kadar ayrıntı bilmenize gerek yok. Diğer kısımlara geçin.

<h2 id="1.1">Frozenset'de İşlemler</h2>

Iterable bütün type'ları set'e dönüştürebilirsin. Örnek:
```py
print("frozenset:", frozenset({"A", "B", "C"}))            # Output: set: frozenset({'B', 'A', 'C'})
print("set:", frozenset({"A", "B", "C"}))                  # Output: frozenset: frozenset({'B', 'A', 'C'})
print("list:", frozenset(["A", "B", "C"]))                 # Output: list: frozenset({'B', 'A', 'C'})
print("tuple:", frozenset(("A", "B", "C")))                # Output: tuple: frozenset({'B', 'A', 'C'})
print("str:", frozenset("ABC"))                            # Output: str: frozenset({'B', 'A', 'C'})
print("dict:", frozenset({"A": "a", "B": "b", "C": "c"}))  # Output: dict: frozenset({'B', 'A', 'C'})
print("bytearray:", frozenset(bytearray('ABC', 'utf-8')))  # Output: bytearray: frozenset({65, 66, 67})
print("range:", frozenset(range(3)))                       # Output: range: frozenset({0, 1, 2})
```

**Not:** `__iter__()` methoduna sahip bütün class'lardan türetilen objeler (instance) iterable'dır. Bazı iterable obje örnekleri: `frozenset`, `set`, `list`, `tuple`, `str`, `dict`, `bytearray`, `range`, `memoryview`, `enumerate`, `filter`, `map`, `reversed`, `zip`

Frozenset'lerin öğe sayısına `len()` fonksiyonuyla ulaşılabilir. Örnek:
```py
fs1 = frozenset({1,2,3,4,5})
print(len(fs1)) # Output: 5
```

Frozenset type, aritmetik (sayısal) işlemleri desteklemez. Örnek:
```py
print(frozenset({1,2,3}) + frozenset({4,5,6})) # TypeError: unsupported operand type(s) for +: 'frozenset' and 'frozenset'
print(frozenset({1,2,3}) * 2) # TypeError: unsupported operand type(s) for *: 'frozenset' and 'int'
```

Frozenset objesini tamamen silmek:
```py
fs1 = frozenset({1,2,3,4,5})
del fs1
print(fs1) # NameError: name 'fs1' is not defined
```

Bir frozenset'i kopyalamak ve sonuçları:
```py
fs1 = frozenset({1,2,3,4})
fs2 = fs1
print(fs1) # Output: frozenset({1, 2, 3, 4})
print(fs2) # Output: frozenset({1, 2, 3, 4})
print(id(fs1) == id(fs2)) # Output: True
```

<h2 id="1.2">Frozenset Üreteçleri (Frozenset Comprehensions)</h2>

**Comprehension**, tek satırda oluşturduğumuz **Generator** (daha sonra anlatılacak) yapısına verilen isimdir. `(expression for item in iterable)` syntax'ına sahiptir (parantezler dahil). Bu generator yapısı (**Generator Comprehension**) bir generator objesi oluşturmakta kullanılır. Daha sonra bu generator objesini frozenset type'a dönüştürerek Frozenset Comprehension oluşturabiliriz. Örnek:
```py
frozenset_exp = frozenset({i for i in range(1,4)})
print(frozenset_exp, type(frozenset_exp)) # Output: frozenset({1, 2, 3}) <class 'frozenset'>
```
Bu konu daha sonra comprehension başlığı altında daha detaylı anlatılacak.

<h2 id="1.3">Frozenset Methodları</h2>

<h3 id="1.3.1"><code>copy()</code> Methodu</h3>

Uygulandığı frozenset'in bir kopyasını oluşturur (teoride böyle). `frozenset_exp1 = frozenset_exp2` gibi assignment operator kullanarak frozenset kopyalama yönteminden farkı, yeni frozenset ile eski frozenset'in birbirinden bağımsız, farklı (farklı ID'lere sahip) objeler olmasıdır. Örnek:
```py
frozenset_exp = frozenset({1,2,3,4,5})

frozenset_copy1 = frozenset_exp
print(id(frozenset_exp) == id(frozenset_copy1)) # Output: True

frozenset_copy2 = frozenset_exp.copy()
print(id(frozenset_exp) == id(frozenset_copy2)) # Output: True
```
`copy()` methodu, değiştirilemez (immutable) data type olan `frozenset`'de neden var anlamış değilim. Zaten bu method, `froozenset` type'da olmasına rağmen çalışmıyor gördüğünüz gibi. Değiştirilemez (immutable) data type'lar adı üstünde değiştirilemez olduğu için verimlilik açısından bütün kopyaları aynı bellek adresine atıfta bulunur. Bu yüzden aynı şeyin farklı kopyaları oluşturulmaz çünkü verimlilik açısından dezavantajlı ve gereksiz. 

<h3 id="1.3.2"><code>difference(*s)</code> Methodu</h3>

Uygulandığı frozenset ile `*s` parametresine girilen frozenset'lerin farkını alır ve sonucu döndürür. `A` ve `B` iki frozenset type obje olmak üzere, `A - B` işleminin şematik gösterimi:

![](https://i.ibb.co/1Rx3z20/a-fark-b.png)

Yukarıdaki şemaya göre `A - B` işlemi "`A`'da olup `B`'de olmayan" anlamına gelmektedir. Örnek:
```py
print(frozenset({1,2,3,4,5}).difference(frozenset({1,2,3}))) # Output: frozenset({4, 5})
print(frozenset({1,2,3,4,5}).difference(frozenset({1,}),frozenset({2,}),frozenset({3,}))) # Output: frozenset({4, 5})
print(frozenset({1,2,3,4,5}).difference(frozenset({1,2,3}),frozenset({1,4}))) # Output: frozenset({5})
```


<h3 id="1.3.3"><code>intersection(*s)</code> Methodu</h3>

Uygulandığı frozenset ile `*s` parametresine girilen frozenset'lerin kesişimini alır ve sonucu döndürür. İki frozenset'i kesişimini almak için `&` operator'ı da kullanılabilir. `A` ve `B` iki frozenset type obje olmak üzere, `A & B` işleminin şematik gösterimi:

![](https://i.ibb.co/LdKstBY/a-kesi-im-b.png)

Yukarıdaki şemaya göre `A & B` işlemi "`A` ve `B`'de bulunan" anlamına gelmektedir. Örnekler:

![](https://i.ibb.co/NTTF2th/12345-kesi-im-1236.png)

Yukarıdaki şemanın ifade ettiği kod:
```py
A = frozenset({1,2,3,4,5})
B = frozenset({1,2,3,6})
print(A.intersection(B)) # Output: frozenset({1, 2, 3})
print(A & B) # Output: frozenset({1, 2, 3})
```

<hr>

![](https://i.ibb.co/jvVsmY1/12345-1-2.png)

Yukarıdaki şemanın ifade ettiği kod:
```py
A = frozenset({1,2,3,4,5})
B = frozenset({1,})
C = frozenset({2,})
print(A.intersection(B,C)) # Output: frozenset() (boş frozenset)
print(A & B & C) # Output: frozenset() (boş frozenset)
```

<hr>

![](https://i.ibb.co/K6hSgCj/12345-123-14.png)

Yukarıdaki şemanın ifade ettiği kod:
```py
A = frozenset({1,2,3,4,5})
B = frozenset({1,2,3})
C = frozenset({1,4})
print(A.intersection(B,C)) # Output: frozenset({1})
print(A & B & C) # Output: frozenset({1})
```

<h3 id="1.3.4"><code>union(*s)</code> Methodu</h3>

Uygulandığı frozenset ile `*s` parametresine girilen frozenset'lerin birleşimini alır ve sonucu döndürür. İki frozenset'i birleşimini almak için `|` operator'ı da kullanılabilir. `A` ve `B` iki frozenset type obje olmak üzere, `A | B` işleminin şematik gösterimi:

![](https://i.ibb.co/CvjTRYs/a-birle-im-b.png)

Yukarıdaki şemaya göre `A | B` işlemi "`A` veya `B`'de bulunan" anlamına gelmektedir. Örnekler:

![](https://i.ibb.co/kQByHRV/12345-kesi-im-1236.png)

Yukarıdaki şemanın ifade ettiği kod:
```py
A = frozenset({1,2,3,4,5})
B = frozenset({1,2,3,6})
print(A.union(B)) # Output: frozenset({1, 2, 3, 4, 5, 6})
print(A | B) # Output: frozenset({1, 2, 3, 4, 5, 6})
```

<hr>

![](https://i.ibb.co/xFN9bnz/12345-1-2.png)

Yukarıdaki şemanın ifade ettiği kod:
```py
A = frozenset({1,2,3,4,5})
B = frozenset({1,})
C = frozenset({2,})
print(A.union(B,C)) # Output: frozenset({1, 2, 3, 4, 5})
print(A | B | C) # Output: frozenset({1, 2, 3, 4, 5})
```

<hr>

![](https://i.ibb.co/PCjfjNY/12345-123-14.png)

Yukarıdaki şemanın ifade ettiği kod:
```py
A = frozenset({1,2,3,4,5})
B = frozenset({1,2,3})
C = frozenset({1,4})
print(A.union(B,C)) # Output: frozenset({1, 2, 3, 4, 5})
print(A | B | C) # Output: frozenset({1, 2, 3, 4, 5})
```

<h3 id="1.3.5"><code>isdisjoint(s)</code> Methodu</h3>

Uygulandığı frozenset objesi ile `s` parametresine argüman olarak girilen frozenset objesinin kesişiminin boş olup olmadığını sordular. Boşsa `True`, diğer durumlarda `False` döndürür. Örnek:
```py
A = frozenset({1,2,3,4,5})
B = frozenset({1,2,3})
C = frozenset({6,7})
print(A.isdisjoint(B)) # Output: False (Boş değil)
print(A.isdisjoint(C)) # Output: True (Boş)
```

<h3 id="1.3.6"><code>issubset(s)</code> Methodu</h3>

Uygulandığı frozenset objesinin, `s` parametresine argüman olarak girilen frozenset objesinin alt kümesi olup olmadığını sorgular. Alt kümesi ise `True`, diğer durumlarda `False` döndürür.

**Alt Küme:** `A` ve `B` iki küme olmak üzere, `B` kümesinin bütün elemanları `A` kümesinde de varsa (başka bir deyişle, `B` kümesinin bütün elemanları `A` kümesine ait ise), `B` kümesi `A` kümesinin alt kümesidir.

Örnek:
```py
A = frozenset({1,2,3,4,5})
B = frozenset({1,2,3,4})
C = frozenset({1,2,3})
D = frozenset({1,2})
E = frozenset({1})
F = frozenset()
print(A.issubset(A)) # Output: True (Her küme kendisinin alt kümesidir)
print(B.issubset(A)) # Output: True
print(C.issubset(A)) # Output: True
print(D.issubset(A)) # Output: True
print(E.issubset(A)) # Output: True
print(F.issubset(A)) # Output: True (Boş küme, bütün kümelerin alt kümesidir)
```
`A` kümesi diğer kümeleri kapsadığı için diğer kümeler `A` kümesinin alt kümesidir. Aykırı bir örnek:
```py
A = frozenset({1,2,3,4,5})
B = frozenset({1,2,3,4,5,6})
print(B.issubset(A)) # Output: False (A kümesi B kümesini kapsamaz)
```

<h3 id="1.3.7"><code>issuperset(s)</code> Methodu</h3>

Uygulandığı frozenset objesinin, `s` parametresine argüman olarak girilen frozenset objesinin üst kümesi olup olmadığını sorgular. Başka bir deyişle, Uygulandığı frozenset objesinin, `s` parametresine argüman olarak girilen frozenset objesini kapsayıp kapsamadığını sorgular Üst kümesi ise (kapsıyorsa) `True`, diğer durumlarda `False` döndürür. Örnek:
```py
A = frozenset({1,2,3,4,5})
B = frozenset({1,2,3,4})
C = frozenset({1,2,3})
D = frozenset({1,2})
E = frozenset({1})
F = frozenset()
print(A.issuperset(A)) # Output: True (Her küme kendisinin üst kümesidir)
print(A.issuperset(B)) # Output: True
print(A.issuperset(C)) # Output: True
print(A.issuperset(D)) # Output: True
print(A.issuperset(E)) # Output: True
print(A.issuperset(F)) # Output: True (Bütün kümeler, boş kümenin üst kümesidir)
```
Aykırı bir örnek:
```py
A = frozenset({1,2,3,4,5})
B = frozenset({1,2,3,4,5,6})
print(A.issuperset(B)) # Output: False (B kümesi A kümesini kapsamaz)
```

<h3 id="1.3.8"><code>symmetric_difference(s)</code> Methodu</h3>

`A` ve `B` iki frozenset objesi olmak üzere, `A.difference(B) | B.difference(A)` (yani `(A - B) | (B - A)`) işleminin sonucunu döndürür. Bu işlemin şematik gösterimi:

![](https://i.ibb.co/3y5bxKY/symmetric-difference.png)

Örnek:

![](https://i.ibb.co/f8mtZhV/12345-12678.png)

Yukarıdaki şemanın ifade ettiği kod:
```py
A = frozenset({1,2,3,4,5})
B = frozenset({1,2,6,7,8})
print(A.symmetric_difference(B)) # Output: frozenset({3, 4, 5, 6, 7, 8})
```