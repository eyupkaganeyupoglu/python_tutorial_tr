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

`set`, bildiğimiz matematikteki kümeler gibidir. Her öğeden bir tane bulundurur. Set'ler sırasız (indexlenemezler) ve değiştirilebilir (mutable) data type'lardır. `set(iterable)` build'in fonksiyonu ile set oluşturabilirsiniz veya uygun objeleri set'e dönüştürebilirsiniz. Set'ler süslü parantez (`{}`) ile ifade edilir. Örnek:
```py
s1 = set()
s2 = {"string",
	  1, 1.5, 15+5j,
	  ("tuple", "Tuple"),
	  range(10)}

print(s1) # Output: set()
print(s2) # Output: {'string', 1, 1.5, ('tuple', 'Tuple'), (15+5j), range(0, 10)}
```
`bool`, `int`, `float`, `complex`, `tuple`, `frozenset`, `bytes` ve `range` değiştirilemez (immutable) type'lar oldukları için set'e öğe olarak girilebilirler. `list`, `set`, `dict`, `bytearray` ve user-defined class'lar değiştirilebilir (mutable) data type'lar oldukları için set'e öğe olarak girilemezler.

Set data type'ı sırasız olduğu için örneğin `print()` fonksiyonu ile yazdırılmak istense, program her çalıştırıldığında öğeler farklı sırada yazdırılabilir. Bu durum öğelerin **hashlenmesi** ile ilgilidir. Hash dediğimiz şey, veriyi daha az kaynak kullanarak ifade etmek için ilgili hashing algoritmasının ürettiği değerdir. Örneğin 1024 bitlik bir mesajı bir hashing algoritması 128 bitlik yapıya indirgeyebilir. Python'da da böyledir. Bir Python programı çalıştırıldığında, o programdaki değerler bir hash'e sahip olur. Çok kaynak kullanılarak ifade edilebilen değerlerin hash'leri, program her çalıştırıldığında değişir. Ama az kaynak kullanılarak ifade edilebilen değerlerin hash'leri her zaman aynıdır. Örnek:
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
boolean, integer, float, complex ve range type'ların hash'leri hiçbir zaman değişmez çünkü bu type'lar az kaynak harcarlar. Ama bytes ve string type'ların hash'leri, program her baştan çalıştırıldığında değişir çünkü bu type'lar çok kaynak harcarlar. Tuple ve Frozenset type'ları da içerdiği değerlere göre çok ya da az kaynak harcayabilir. Örneğin öğeleri çok kaynak harcayan string veya bytes type olan bir tuple veya frozenset objelerinin hash'i, program her çalıştırıldığında değişirken; öğeleri az kaynak harcayan type'lar olan tuple veya frozenset objelerinin hash'i hep aynıdır. Yukarıda örneği var.

**Not:** `list`, `set`, `dict`, `bytearray` gibi değiştirilebilir (mutable) type'lar hash'lenemez. Hash'lenmeye çalışılırsa `TypeError: unhashable type: 'list'`, `TypeError: unhashable type: 'set'`, `TypeError: unhashable type: 'dict'`, `TypeError: unhashable type: 'bytearray'` gibi hatalar yükseltilir. **Hash** hakkında daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#hash "https://docs.python.org/3/library/functions.html#hash"). **Hashable** hakkında daha fazla bilgi için [tıklayınız](https://docs.python.org/3/glossary.html#term-hashable "https://docs.python.org/3/glossary.html#term-hashable").

**Not:** `None` type da değiştirilemez (immutable) bir type'dır ve hash'i her zaman sabittir. Ama farklı makinelerde bu hash değeri değişebilir. Örneğin benim makinede (bilgisayarımda) `-9223363241081056563` hash'ine sahipken, bir arkadaşımın bilgisayarında `-9223363242374385203` hash'ine sahiptir.

**Not:** Set, öğelerini hash'in sayısal büyüklüğüne göre mi sıralıyor diye bakmayın, ben baktım ve öyle bir şey yok sanırım. Örnek:
```py
set_exp = {"1", "2", "3"}
for i in set_exp:
    print(i, hash(i))
print(set_exp)
```
**Output:**
```
2 -3778677644095488240
1 7888383718303043910
3 2738165215596315832
{'2', '1', '3'}
```
Burada `'2'` string'ini hash'inin sayısal değeri diğerlerinden küçük olmasına rağmen ilk sırada. Bu da hash'lerin sıralanışının sayısal büyüklükleriyle alakalı olmadığını kanıtlıyor. Bu kadar ayrıntı bilmenize gerek yok. Diğer kısımlara geçin.

**Not:** Süslü parantezleri (`{}`) sade bir şekilde kullanırsak bir dictionary objesi elde etmiş oluruz. Çünkü `set` type'ın `list`, `tuple` ve `dict` gibi spesifik bir işareti yoktur. Bu yüzden boş `set` objesi elde etmek istiyorsanız `set()` build-in fonksiyonunu kullanmalısınız. Örnek:
```py
var1 = {}
var2 = set()
print(type(var1)) # Output: <class 'dict'>
print(type(var2)) # Output: <class 'set'>
```

<h2 id="1.1">Set'de İşlemler</h2>

Iterable bütün type'ları set'e dönüştürebilirsin. Örnek:
```py
print("set  ", {"A", "B", "C"})                     # Output: set   {'C', 'B', 'A'}
print("list ", set(["A", "B", "C"]))                # Output: list  {'C', 'B', 'A'}
print("tuple", set(("A", "B", "C")))                # Output: tuple {'C', 'B', 'A'}
print("str  ", set("ABC"))                          # Output: str   {'C', 'B', 'A'}
print("dict ", set({"A": "a", "B": "b", "C": "c"})) # Output: dict  {'C', 'B', 'A'}
```

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
Set, değiştirilebilir (mutable) bir data type olduğu için assignment operator (`=`) kullanılarak bir set objesini yukarıdaki gibi farklı bir variable'a atarsanız, son durumda oluşan objeler aynı set objesine atıfta bulunacağı (refers to) için birinde yapılan değişiklikler diğerini de etkiler. Bu durum değiştirilemez (immutable) data type'lar için geçerli değildir çünkü değiştirilemez (immutable) data type'ları değiştirmek için yeniden tanımlama (redefinition) işlemi yapmak zorundayız. Yeniden tanımlama (redefinition) işlemi sonucunda da mevcut obje farklı bir objeye dönüştüğü için birbirine atıfta bulunma durumu ortadan kalkacak ve bu objeler birbirini etkilemeyecek.

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
set = {1,2,3,4,5}
set_copy1 = set
print(set) # Output: {1, 2, 3, 4, 5}
print(set_copy1) # Output: {1, 2, 3, 4, 5}

set_copy1.add("Bir")
print(set) # Output: {'Bir', 1, 2, 3, 4, 5}
print(set_copy1) # Output: {'Bir', 1, 2, 3, 4, 5}

set_copy2 = set.copy()
print(id(set) == id(set_copy2)) # Output: False
print(set) # Output: {'Bir', 1, 2, 3, 4, 5}
print(set_copy2) # Output: {'Bir', 1, 2, 3, 4, 5}

set_copy2.add("İki")
print(set) # Output: {'Bir', 1, 2, 3, 4, 5}
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

Uygulandığı küme ile `*s` parametresine girilen kümelerin farkını alır ve sonucu döndürür. `A` ve `B` iki set type obje olmak üzere, `A - B` işleminin şematik gösterimi:

![](https://i.ibb.co/1Rx3z20/a-fark-b.png)

Yukarıdaki şemaya göre `A - B` işlemi "`A`'da olup `B`'de olmayan" anlamına gelmektedir. Örnek:
```py
print({1,2,3,4,5}.difference({1,2,3})) # Output: {4, 5}
print({1,2,3,4,5}.difference({1,},{2,},{3,})) # Output: {4, 5}
print({1,2,3,4,5}.difference({1,2,3},{1,4})) # Output: {5}
```

**Not:** `difference` methodu, uygulandığı set'i değiştirmez. Ama bir başka method olan `difference_update` değiştirir.


<h3 id="1.3.5"><code>difference_update(*s)</code> Methodu</h3>

Uygulandığı küme ile `*s` parametresine girilen kümelerin farkını alır ama `difference` methodundaki gibi sonucu döndürmez, bunun yerine uygulandığı set'i değiştirir. `A` ve `B` iki set type obje olmak üzere, `A - B` işleminin şematik gösterimi:

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

`element` parametresine argüman olarak girilen değeri set'den silmeye yarar. İşlev bakımından`add` methodunun zıttını yapar. `element` parametresinde belirtilen değer set'de yoksa hiçbir şey yapmaz. Örnek:
```py
A = {1,2,3,4,5}
A.discard(1)
print(A) # Output: {2, 3, 4, 5}
A.discard(6)
print(A) # Output: {2, 3, 4, 5}
```

<h3 id="1.3.7"><code>remove(element)</code> Methodu</h3>

`element` parametresine argüman olarak girilen değeri set'den silmeye yarar. İşlev bakımından`add` methodunun zıttını, `discard` methodunun aynısını yapar. `element` parametresinde belirtilen değer set'de yoksa `KeyError` hatası yükseltir. Örnek:
```py
A = {1,2,3,4,5}
A.remove(1)
print(A) # Output: {2, 3, 4, 5}
A.remove(6) # KeyError: 6
```

<h3 id="1.3.8"><code>intersection(*s)</code> Methodu</h3>

Uygulandığı küme ile `*s` parametresine girilen kümelerin kesişimini alır ve sonucu döndürür. İki set'i kesişimini almak için `&` operator'ı da kullanılabilir. `A` ve `B` iki set type obje olmak üzere, `A & B` işleminin şematik gösterimi:

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

Uygulandığı küme ile `*s` parametresine girilen kümelerin farkını alır ama `intersection` methodundaki gibi sonucu döndürmez, bunun yerine uygulandığı set'i değiştirir. İki set'i kesişimini almak için `&` operator'ı da kullanılabilir. `A` ve `B` iki set type obje olmak üzere, `A & B` işleminin şematik gösterimi:

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

Uygulandığı set objesi ile `s` parametresine argüman olarak girilen set objesinin kesişiminin boş olup olmadığını sordular. Boşsa `True`, diğer durumlarda `False` döndürür. Örnek:
```py
A = {1,2,3,4,5}
B = {1,2,3}
C = {6,7}
print(A.isdisjoint(B)) # Output: False (Boş değil)
print(A.isdisjoint(C)) # Output: True (Boş)
```

<h3 id="1.3.11"><code>issubset(s)</code> Methodu</h3>

Uygulandığı set objesinin, `s` parametresine argüman olarak girilen set objesinin alt kümesi olup olmadığını sorgular. Alt kümesi ise `True`, diğer durumlarda `False` döndürür.

**Alt Küme:** `A` ve `B` iki küme olmak üzere, `B` kümesinin bütün elemanları `A` kümesinde de varsa (başka bir deyişle, `B` kümesinin bütün elemanları `A` kümesine ait ise), `B` kümesi `A` kümesinin alt kümesidir.

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

Uygulandığı set objesinin, `s` parametresine argüman olarak girilen set objesinin üst kümesi olup olmadığını sorgular. Başka bir deyişle, Uygulandığı set objesinin, `s` parametresine argüman olarak girilen set objesini kapsayıp kapsamadığını sorgular Üst kümesi ise (kapsıyorsa) `True`, diğer durumlarda `False` döndürür. Örnek:
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

Uygulandığı küme ile `*s` parametresine girilen kümelerin birleşimini alır ve sonucu döndürür. İki set'i birleşimini almak için `|` operator'ı da kullanılabilir. `A` ve `B` iki set type obje olmak üzere, `A | B` işleminin şematik gösterimi:

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

`A` ve `B` iki set objesi olmak üzere, `A.difference(k2) | B.difference(k1)` (yani `(A - B) | (B - A)`) işleminin sonucunu döndürür. Bu işlemin şematik gösterimi:

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

`A` ve `B` iki set objesi olmak üzere, `A.difference(k2) | B.difference(k1)` (yani `(A - B) | (B - A)`) işleminin sonucu döndürmez, bunun yerine uygulandığı set'i değiştirir. Bu işlemin şematik gösterimi:

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
`pop` merhodu, (yukarıdaki örnekte integer gibi) hash'leri her zaman aynı olan data type'larda her zaman aynı öğeyi silerken,  (yukarıdaki örnekte string gibi) hash'leri her seferinde değişen data type'larda her zaman aynı öğeyi silmeyebilir.
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