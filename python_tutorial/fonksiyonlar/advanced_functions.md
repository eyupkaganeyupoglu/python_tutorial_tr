# `lambda` fonksiyonu
Bu fonksiyon, `lambda arguments : expression` syntax'ına sahiptir.
```py
def func1 (p1,p2):
    return (p1 + p2)
print(func1(2,3)) # Output: 5
print(func1) # Output: <function func1 at 0x000002243DB2BEE0>

func2 = lambda p1,p2: (p1 + p2)
print(func2(2,3)) # Output: 5
print(func2) # Output: <function <lambda> at 0x000002243DB2BF70>
```
`func1` ile `func2` aynı işleve sahiptir. `lambda` fonksiyonuna tanımlanan `arguments`, `def` ile tanımlanan fonksiyonlardaki parametre kısmına denk gelmektedir. `:`'dan sonraki kısım da `def` ile tanımlanan fonksiyonlardaki `return` statement'ını temsil eder. Örnek:
```py
func1 = lambda p1: ("Bu 2'dir.") if p1==2 else ("Bu 2 değildir.")
print(func1(1)) # Output: Bu 2 değildir.
print(func1(2)) # Output: Bu 2'dir.
```
Burada tek satırlık `if` - `else` yapısı kullanılarak `lambda` fonksiyonuna farklı `return` değerleri tanımlanabildi. Bu gibi kullanımlar, `sorted()` fonksiyonundaki `key` parametresi gibi yerlerde kullanılır. Örnek:
```py
elemanlar = [("bir", 1),
             ("dört", 4),
             ("üç", 3),
             ("iki", 2),
             ("beş", 5)]

def sırala(liste):
    return liste[1]
    
print(*sorted(elemanlar, key=sırala), sep='\n')
```
**Output:**
```
('bir', 1)
('iki', 2)
('üç', 3)
('dört', 4)
('beş', 5)
```
Yukarıdaki kodu `lambda` kullanarak şöyle yazarız:
```py
elemanlar = [("bir", 1),
             ("dört", 4),
             ("üç", 3),
             ("iki", 2),
             ("beş", 5)]
    
print(*sorted(elemanlar, key=lambda p1:(p1[1])), sep='\n')
```
**Output:**
```
('bir', 1)
('iki', 2)
('üç', 3)
('dört', 4)
('beş', 5)
```

# Recursive (Özyinelemeli) Fonksiyonlar
Bir fonksiyon çalıştığında, kendi scope'unda başka bir fonksiyonu çağırabilir. Örnek:
```py
def selamla():
    print("Selam")
selamla() # Output: Selam
```
Görüldüğü gibi `selamla()` fonksiyonu `print()` fonksiyonunu çağırabiliryor. Bu durum, bir fonksiyon kendi scope'unda kendisini çağırdığı durumlarda da geçerkidir. Örnek:
```py
def selamla():
    print("selam")
    selamla()
selamla()
```
Yukarıdaki fonksiyona **recursive (Özyinelemeli) fonksiyon** nedir. Yukarıdaki fonksiyon sürekli kendini yeniden çalıştırır. Bu fonsiyon, `RecursionError` hatası vermeden önce belli bir maksimum çalışma sayısına sahiptir. Bu sınırı aşağıdaki kodla öğrenebilirsiniz:
```py
import sys
print(sys.getrecursionlimit()) # Output: 1000
```
Recursive fonksiyon sonsuz döngüye girerse `RecursionError: maximum recursion depth exceeded while calling a Python object` hatası verir. Başka bir örnek:
```py
def azalt(s):
    if len(s) < 1:
        return s
    else:
        print(s)
        return azalt(s[:-1])
print(azalt("selam"))
```
**Output:**
```
selam
sela
sel
se
s
```
Örnek İç içe listeleri tek liste yapma fonksiyonu:
```py
def fixed(liste):
    if not isinstance(liste, list):
        return [liste]
    elif not liste:
        return []
    else:
        return fixed(liste[0]) + fixed(liste[1:])

l = [1, 2, 3, [4, 5, 6], [7, 8, 9, [10, 11], 12], 13, [14, 15]]

print(fixed(l)) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
```

# Nested (İç İçe) Fonksiyonlar
İç içe fonksiyonlarda, en dıştaki (yani global scope'da tanımlanan) fonksiyon **enclosing**, enclosing'in scope'una tanımlanan bütün fonksiyonlar da **nested** olarak isimlenirilir.
```py
def yazıcı():
    print("Yazıcı Çalıştı.")
    def yaz(mesaj):
        print(mesaj)
    return yaz
```
Yukarıdaki fonksiyonda, `yazıcı()` fonksiyonunu çağırmadan `yaz()` fonksiyonunu çağıramayız. Bu her yerde böyledir. Çünkü `yazıcı()` fonksiyonunu çağırdığımızda onu tanımlamış oluyoruz ve `yazıcı()` fonksiyonunu tanımlamadan `yaz()` fonksiyonunu direkt çağıramayız. `yazıcı()` fonksiyonu her çağırıldığında `yaz()` fonksiyonu baştan tanımlanır. Yani `yazıcı()` fonksiyonunu ilk çağırışınızdaki `yaz()` fonksiyonu ile  `yazıcı()` fonksiyonunu ikinci çağırışınızdaki `yaz()` fonksiyonu birbirinden farklı objelerdir. Bu objeler `<function yazıcı.<locals>.yaz at 0x00000210D9235558>` şeklindedir.

## Örnek Uygulama
```py
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def plus(y): return lambda x: x+y

print(four(plus(five()))) # Output: 9
```
Yukarıdaki `print(four(plus(five())))` şöyle çalışır:
- Python'un bir kodu nasıl okuyup çalıştırdığını **[temel_kavramlar.md](asd)**'de anlatıldı. İlk olarak en içteki `five()` çalışır ve parametre olarak bir şey girilmediği için `5` döndürür.
- Sonra `plus()` çalışır ve parametre olarak aldığı `5`'i kullanarak `lambda x : x+5` fonksiyonunu döndürür.
- Sonra `four()` çalışır ve parametre olarak lambda fonksiyonu objesi aldığı için `f` parametresi `None` değerini kaybeder. Bu yüzden `if` çalışmaz, `else` çalışır. `else`'e tanımlanmış `f(4)`, `(lambda x : x + 5)(4)` anlamına gelmektedir. Buradaki mantık `plus()()` mantığıyla aynıdır. `plus()()` şöyle okunur:
    - `plus(5)(4)`'da ilk önce soldaki kısım, yani `plus(5)` fonksiyonu (`<function plus at 0x00000179CF5ABEE0>`)çalışır. `plus(5)` fonksiyonu `lambda x: x+5` lambda fonksiyonu objesini `<function plus.<locals>.<lambda> at 0x00000179CF5ABF70>` döndürür.
    - Sonra, `plus(5)` fonksiyonunun döndürdüğü `lambda x: x+5` lambda fonksiyonu objesi, `plus(5)` fonksiyonunun yerine geçer ve `plus(5)(4)` yapısı, `(lambda x: x+5)(4)` yapısına dönüşür (asli `<function plus.<locals>.<lambda> at 0x00000179CF5ABF70>(4)`'dür).
    - Sonra, `(lambda x: x+5)(4)` yapısındaki `lambda x: x+5` lambda fonksiyonu, kendisine girilen `4`'ü işleme sokar ve `4+5`'den `9` sonucunu döndürür.

# Generators (Üreteçler)

**Ön bilgi:** *Iterate* ile *Iterate over* kelimelerinin farkı şudur:
- **Iterate**, bir şeyi bir kere tekrarlamak anlamında kullanılan bir fiildir (repeat).
-  **Iterate over**, bir şeyi sürekli tekrarlamak anlamında kullanılır (repeatedly).

**Iterator** ile **Iterable** İki farklı kavramdır. Defalarca tekrarlanabilir (can iterate over) herhangi bir şey, **Iterable** (tekrarlanabilir) bir objedir. `str`, `list`, `tuple`, `set`, `frozenset`, `dict` gibi data type'lar **Iterable**'dir. Collection type'lar (arrays) genellikle **iterable**'dir.
- **List**, indexlenebilir (yani sıralı) ve değiştirilebilir (mutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin verir.

- **Tuple**, indexlenebilir (yani sıralı) ve değiştirilemez (immutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin verir.

- **Set**, indexlenemez (yani sırasız) ve değiştirilebilir (mutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin vermez.

- **Dictionary**, indexlenebilir (yani sıralı) ve değiştirilebilir (mutable) bir collection'dır. Python 3.6'dan önce indexlenemezken (yani sırasız),  Python 3.7'den itibaren indexlenebilir (yani sıralı) olmuştur. Duplicate members'a (Bir öğeden birden fazla olması) izin vermez.
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#next).

[`iter()`](https://docs.python.org/3/library/functions.html#iter) fonksiyonu ile, **Iterable** (tekrarlanabilir) bir objenin template'i kullanılara bir **Iterator** objesi oluşturulabilir. Bunu mümkün kılmak için **Iterable** (tekrarlanabilir) bir objenin class'ının, **Iterator** döndüren bir `__iter__` ya da `0` ile başlayan sıralı (sequential) index'lere sahip `__getitem__` methoduna ihtiyacı vardır. `iter()` fonksiyonuna **Iterable** (tekrarlanabilir) olmayan bir obje verilirse, `TypeError` hatası yükseltilir. **Iterator**'ler, objenin bir sonraki item'ına geçmeye yarayan `__next__()` methoduna sahiptir. **Iterator**'ler, `__next__()` methodu kullanarak, **Iterable** bir objeden kopyaladıkları template üzerinde iterate (yenileme) yapmak için kullanılan objelerdir.
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
**Not:** Bir **Iterator**, **Iterable** bir objenin referansı değildir. Yani bu yineleme işlemini, oluşturulduğu **Iterable** bir objenin üzerinden yapmaz. **Iterator**, kendi başına ayrı bir objedir.
```py
liste = [1,2,3]
iter_obj = iter(liste)
print(iter_obj) # Output: <list_iterator object at 0x000002327E1BDFD0>
print(next(iter_obj)) # Output: 1
print(next(iter_obj)) # Output: 2
print(next(iter_obj)) # Output: 3
print(next(iter_obj)) # Output: StopIteration
```
```py
iter_obj = iter([1,2,3])
print(iter_obj) # Output: <list_iterator object at 0x000002327E1BDFD0>
print(next(iter_obj)) # Output: 1
print(next(iter_obj)) # Output: 2
print(next(iter_obj)) # Output: 3
print(next(iter_obj)) # Output: StopIteration
```
**Not:** Bütün **Iterator**'ler **Iterable**'dir ama her **Iterable** obje, **Iterator** değildir. Örneğin bir `list` **Iterable** bir objedir ama **Iterator** değildir.

**Not:** Bir **Iterator**, barındırdığı öğe sayısından fazla `next` methodu ya da fonksiyonu kullanılırsa, başka kullanılabilir öğe bulamadığı için `StopIteration` hatası yükseltilir. Örnek:
```py
iterable_item = ["selam", "merhaba"]
iterator = iter(iterable_item)

print(next(iterator)) # Output: selam
print(next(iterator)) # Output: merhaba
print(next(iterator)) # Output: StopIteration
```
**Dikkat:** **Generator**'ü anlatmaya başlamadan önce şunu kafanıza kazıyın, Her **Generator** bir **Iterator**'dür. Çünkü **Iterator** genel bir kavramdır. Yani **Generator**'lar, bir çeşit **Iterable** objedir.

**Generator**'lar, fonksiyonlara benzer tanımlanır. Farkı `return` değil, `yield` kullanılmasıdır. Örnek:
```py
def function():
    sayı = 0
    def say():
        nonlocal sayı
        sayı += 1
        return sayı
    return say

fonk = function()
print(type(fonk)) # Output: <class 'function'>
print(fonk()) # Output: 1
print(fonk()) # Output: 2
print(fonk()) # Output: 3
```
```py
def generator():
    sayı = 0
    while True:
        sayı += 1
        yield sayı

genr = generator()
print(type(genr)) # Output: <class 'generator'>
print(next(genr)) # Output: 1
print(next(genr)) # Output: 2
print(next(genr)) # Output: 3
```
`yield` keyword'ü `return`'e benzer. Farkı, `return` deyiminden sonra fonksiyondaki local variable'lar silinirken `yield` keyword'ünde local variable'ların tamamı saklanır. Bunun sağlamasını, Windows işletim sistemlerinde, görev yöneticisinin performans kısmındaki, RAM'inizin doluluğunu gösteren grafiğe bakarak yapabilirsiniz. `return` çalıştığında fonksiyon sonlanıp local variable'lar silindiği için RAM'inizin doluluğunu gösteren grafikte bir hareketlenme olmaz. `yield` çalıştığında fonksiyon sonlanmadığı için sürekli local variable'lar belleğe kaydedilir. Bu yüzden RAM'inizin doluluğunu gösteren grafik sürekli artış gösterir. `yield` keyword'ü sayesinde local variable'ler saklansa bile **Generator** objesi sonlandığında (yani `StopIteration` hatası oluşunca), bütün local variable'lar bellekten silinir. `yield` ile döndürülen local scope'daki value'lere global scope'da erişmek istiyorsanız, bunları direkt global scope'da depolayabilirsiniz. Örnek:
```py
def generator():
    for i in range(5):
        yield i

liste = []
for i in generator():
    liste.append(i)
print(liste) # Output: [0, 1, 2, 3, 4]
```
Yukarıdaki kodda, `generator()` çağırılır ve `for` her çalıştığında sırasıyla:
- Oluşan **Generator** objesinin içindeki, bir sonraki value'yi çekip `i`'ye atar.
- `generator()` ile yaratılan objeden çektiği ve `i`'ye atadığı value'yi `liste.append(i)` kodu ile `liste` listesine depolar.
- `generator()` ile yaratılan objeyi `next()`'ler.

**Generator** içinde `yield` ile döndürülmeyen local variable'lara ulaşmak istiyorsanız, **Generator** objesinin, `gi_frame` objesinde tanımlı `f_locals` dictionary'sine bakabilirsiniz çünkü bir **Generator** objesinin local variable'ları bu dictionary'de depolanıyor. Örnek:

<img src="https://i.ibb.co/NyCJvsX/image.png" alt="image" border="0">

```py
def generator():
    local_k = 0
    for i,j in [(1,2), (3,4), (5,6)]:
        local_k = i + j
        yield local_k

gen = generator()
global_k = int()
f_locals_repo = dict()

for i in gen:
    global_k = i
    f_locals_repo.update(gen.gi_frame.f_locals)

print(global_k) # Output: 11
print(f_locals_repo)  # Output: {'k': 11, 'i': 5, 'j': 6}
```
Yukarıdaki kodda, `gen = generator()` kodu ile `generator()` çağırılır ve **Generator** objesi `gen` variable'ına atanır. `for` her çalıştığında sırasıyla:
- `gen` variable'ına atanan **Generator** objesinin içindeki, bir sonraki value'yi çekip `i`'ye atar.
- `generator()` sadece `local_k` değerini `yield` ettiği için bu değerin güncel halini `global_k = i` kodu ile `global_k` variable'ına tutuyoruz.
- `f_locals_repo.update(gen.gi_frame.f_locals)` kodundaki `gen.gi_frame.f_locals` ile, `gen` variable'ına atanan **Generator** objesinin `gi_frame` objesinin içindeki `f_locals` dictionary'sinin içinde tutulan bütün local variable'ların (i, j, local_k) güncel hallerini çekip, `f_locals_repo.update(...)` ile globalde tanımladığımız `f_locals_repo` dictionary'sindeki değerleri güncelliyoruz.
    - **Not:** Burada da ilk koddaki gibi `for i in generator():` kullanmak yerine önce `gen = generator()` kodu ile, oluşturulan **Generator** objesini `gen` variable'sine atayıp `gen` variable'sini kullanmamızın nedeni: `for i in generator():` kodunda oluşan **Generator** objesi ile `f_locals_repo.update(generator().gi_frame.f_locals)` kodunda oluşan **Generator** objesi birbirinden farklı olacağı için `f_locals_repo` data'sını elde edemezdik. Bu yüzden `gen = generator()` kodu çağırılan **Generator** objesi `gen` variable'ına atandı ve bu variable kullanıldı.

**Iterator** ile **Generator**'ün farkları şunlardır:
- **Generator** oluşturmak için fonksiyon kullanılır. **Iterator** oluşturmak için `iter()` ve `next()` fonksiyonları kullanılır.
- **Generator** `yield` keyword'ünü kullanır ama **Iterator** kullanmaz.
- **Generator**'daki `yield`, Python'daki loop her duraklatıldığında local variable'ların durumlarını kaydeder. **Iterator** local variable'ları kullanmaz. **Iterator**'e, *iterate* edilebilecek *iterable* bir obje vermeniz yeterlidir. **Generator** ve **Iterator**'ın birbirinden en büyük farkı budur.
- Bir **Generator**'a, herhangi bir sayıda `yield` statement tanımlanabilir.
- Bir class'a **Iterator** implement ederek (uygulayarak), **Iterator** ile kullanım desteği kazandırılabilir. **Generator**, Python'da bir class'a ihtiyaç duymaz.
- **Generator** yazmak için bir Python fonksiyonu ya da **Comprehension** kullanabilirsiniz. **Iterator** yazmak için `iter()` ve `next()` fonksiyonlarını kullanmak zorundasınız.
- Bir **Generator**, **Generator** objesi döndürür (`<generator object generator_exp at 0x0000023D508D6D60>`, `<class ‘generator’>`); bir **Iterator**, kullanılan **Iterable** class'a özel **Iterator** objesi döndürür (Örneğin bir list'i **Iterator**'e dönüştürürseniz, o **Iterator** objesi, oluşturulduğu **Iterable** class'a göre özelleşir: `<list_iterator object at 0x0000023D508EDFD0>`, `<class ‘list_iterator’>`).
- **Iterator**, bellek açısından daha verimlidir (more memory-efficient). Bir **Generator**, `__sizeof__()` methoduyla kullanılırsa 32; bir **Iterator**, `__sizeof__()` methoduyla kullanılırsa 16 outputunu verir.
- **Generator**, co-routines'de (ortak rutinler) daha fazla functionality sağlar.
- **Generator**'ler ve **Iterator**'ler, **iterable object**'e (Yenilenebilir sınıflara) örnektir.

**Not:** Bir **Generator** ya da **Iterator**, barındırdığı öğe sayısından fazla `next` methodu ya da fonksiyonu kullanılırsa, başka kullanılabilir öğe bulamadığı için `StopIteration` hatası yükseltilir. Örnek:
```py
def Generator():
    yield "selam"
    yield "merhaba"
gen = Generator()
print(next(gen)) # Output: selam
print(next(gen)) # Output: merhaba
print(next(gen)) # Output: StopIteration
```
```py
iterable_item = ["selam", "merhaba"]
iterator = iter(iterable_item)

print(next(iterator)) # Output: selam
print(next(iterator)) # Output: merhaba
print(next(iterator)) # Output: StopIteration
```
## `yield` Keyword'ü
`yield` keyword'ünün ne işe yaradığı yukarıda bahsedildi. Spesifik olarak aşağıdaki mekaniklere sahiptir:

Bir **Generator**'ın içinde başka bir **Generator** `yield` etmek için kullanılabilir. Örnek:
```py
def generator1():
    yield "generator1 başladı" # 3.
    yield "generator1 bitti" # 4.

def generator2():
    yield "generator2 başladı" # 1.
    for i in generator1(): # 2.
        yield i
    yield "generator2 bitti" # 5.

for i in generator2():
    print(i)
```
**Output:**
```
generator2 başladı
generator1 başladı
generator1 bitti
generator2 bitti
```
Yukarıdaki kodda, kodların `yield` edilme sırası, `#` işaretinin önünde belirtilen numaralarla belirtilmiştir. Buradaki olayın aynısı `yield from` kullanılarak elde edilebilir. Örnek:
```py
def generator1():
    yield "generator1 başladı" # 3
    yield "generator1 bitti" # 4

def generator2():
    yield "generator2 başladı" # 1
    yield from generator1() # 2 (generator1 direkt bitene kadar çalışır.)
    yield "generator2 bitti" # 5

for i in generator2():
    print(i)
```
**Output:**
```
generator2 başladı
generator1 başladı
generator1 bitti
generator2 bitti
```
Yukarıdaki kodda görüldüğü gibi, `from` keyword'ü kullanılarak başka bir **Generator**'e referans vererek, o **Generator**'ın çalışıp sonra ana **Generator**'ın kaldığı yerde devam etmesi sağlanabilir. Buradan şu sonucu çıkarıyoruz:
```py
# 1. Yapı
yield from herhangi_bir_üreteç()

# 2. Yapı
for i in herhangi_bir_üreteç():
    yield i
```
`1. Yapı` ve `2. Yapı`'da belirliten kodlar aynı işleve sahiptir.

# Comprehension
**Comprehension**, tek satırda oluşturduğumuz **Generator** yapısına verilen isimdir. `(expression for item in iterable)` syntax'ına sahiptir (parantezler dahil). Örnek:
```py
generator_exp = ((i**2) for i in range(1,4))

print(generator_exp) # Output: <generator object <genexpr> at 0x0000016A87522120>

for i in generator_exp:
    print(i, end=" ") # Output: 1 4 9
```
Yukarıdaki `((i**2) for i in range(1,4))` kodu, aşağıdaki anlama gelmektedir:
```py
def generator():
    for i in range(10):
        yield i

generator_exp = generator()

print(generator_exp) # Output: <generator object <genexpr> at 0x0000016A87522120>

for i in generator_exp:
    print(i, end=" ") # Output: 1 4 9
```
**Generator Comprehension** yapısı (Örneğin `((i**2) for i in range(1,4))` kodu), sadece bir tane **Generator** objesi oluşturur. Bu yüzden sadece bir tur yenilenebilir. Tekrar kullanılmaya kalkarsanız `StopIteration` hatası alırsınız. Örnek:
```py
generator_exp = ((i**2) for i in range(1,4))

print(next(generator_exp)) # Output: 1
print(next(generator_exp)) # Output: 4
print(next(generator_exp)) # Output: 9
print(next(generator_exp)) # Output: StopIteration
```
Bu **Generator** objesini çeşitli data type'lara dönüştürerek kullanabilirsiniz.

## List Comprehension
Bir **Generator Comprehension**'ı, `list` data type'ında kullandığımız yapıdır. `[expression for item in iterable]` syntax'ına sahiptir. Örnek:
```py
list_exp = [(i**2) for i in range(1,4)]

print(list_exp) # Output: [1, 4, 9]

for i in list_exp:
    print(i, end=" ") # Output: 1 4 9
```
`[expression for item in list]` syntax'ını kullanmak zorunda değilsiniz. Bir **Generator** objesi oluşturup sonradan bu objeyi listeye de dönüştürebilirsiniz ama `[expression for item in list]` syntax'ını kullanmak daha uygundur.
```py
generator_exp = ((i**2) for i in range(1,4))
print(generator_exp) # Output: <generator object <genexpr> at 0x0000016A87522120>
list_exp = list(generator_exp)
print(type(list_exp)) # Output: <class 'list'>

print(list_exp) # Output: [1, 4, 9]

for i in list_exp:
    print(i, end=" ") # Output: 1 4 9
```
Aşağıda, 0'dan 60'a kadar (0 ve 60 dahil) olan sayıların 6'ya bölünebilenlerini liste halinde depolayan özel bir yapı vardır.
```py
liste = [i for i in range(60) if i % 6 == 0]
print(liste) # Output: [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
```
Bu koddaki `[i for i in range(60) if i % 6 == 0]` kodu aşağıdaki anlama gelmektedir:
```py
liste = []
for i in range(61):
    if i % 6 == 0:
        liste.append(i)
```

### Nested List Comprehension
`[[1,2], [3,4], [5,6]]` gibi nested listleri oluşturmak ya da böyle listeler üzerinde işlemler yapmak için kullanılan yapıya denir. Örnekler:

#### Örnek 1
**Nested** liste oluşturmak için aşağıdaki örneklere bakınız.

##### Örnek 1.1
```py
list1 = []
for i in range(3):
    list1.append([])
    for j in range(3):
        list1[i].append(j)
print(list1) # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

list2 = [[j for j in range(3)] for i in range(3)]
print(list2) # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
```
##### Örnek 1.2
```py
list1 = []
for i in range(3):
    list1.append([])
    for j in range(3):
        list1[i].append(i) # j yerine i yazıldı.
print(list1) # Output: [[0, 0, 0], [1, 1, 1], [2, 2, 2]]

list2 = [[i for j in range(3)] for i in range(3)]
print(list2) # Output: [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
```

#### Örnek 2
Mevcut **nested** listeyi ayrıştırma için aşağıdaki örneklere bakınız.

##### Örnek 2.1
```py
main_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

flatten_list1 = []
for sublist in main_list:
    for i in sublist:
        flatten_list1.append(i)
print(flatten_list1) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

flatten_list2 = [i for sublist in main_list for i in sublist]
print(flatten_list2) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
**Not:** `main_list` variable'ına `[0, [1, 2, 3], [4, 5], [6, 7, 8, 9]]` tarzı bir liste girilseydi `TypeError: 'int' object is not iterable` hatası ile karşılaşılırdı çünkü `0` itemi yüzünden `for i in sublist:` kodundaki `sublist`'e atanan değer `0` oluyor. `0` `iterable` bir obje değil, integer bir objedir. Bu yüzden `TypeError: 'int' object is not iterable` hatası ile karşılaşılıyor.

##### Örnek 2.2
```py
main_list = [[[1,2], [3,4,5], [6]], [[7,8,9,10], [11,12]], [[13,14,15], [16], [17,18],[19,20]]]

flatten_list1 = []
for i in main_list:
    for j in i:
        for k in j:
            flatten_list1.append(k)
print(flatten_list1) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

flatten_list2 = [k for i in main_list for j in i for k in j]
print(flatten_list2) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
```
Yukarıdaki `k for i in main_list for j in i for k in j` kodu şöyle çalışır:
- En baştaki `k`, en içteki nested `for` loop'un `item`'idir yani `flatten_list1.append(k)` kısmını temsil eder.
- `k for i in main_list for j in i for k in j` kodunu `(k) (for i in main_list) (for j in i) (for k in j)` şeklinde parçalarsak, `for i in main_list` **enclosing**, ondan sonrakiler soldan sağa doğru **nested** `for` loop oluyor. Yani soldan sağa doğru **nested**'lık artıyor. En sağdaki for loop'un item'ı da (örneğin yukarıdaki `for k in j`'ın `k` item'i), en baştaki expression'ı (örneğin yukarıdaki kodun en sağındaki `k`) temsil eder.

**Not:** Liste objelerinde **nested**'lik ile bu listeye erişen **Nested List Comprehension** objelerindeki `for` loop sayısı doğru orantılıdır. Yani bir liste objesi 2 katman (Oreneğin `[[1,2], [3,4]]`) **nested** ise, bu listeye erişen **Nested List Comprehension** objelerindeki `for` loop (Örneğin `j for i in liste for j in i`) sayısı da 2'dir.

#### Örnek 3
**Nested List Comprehension** objesi oluştururken belli bir koşul belirleyebilirsiniz. Mevcut **nested** listeyi koşula göre ayrıştırma için aşağıdaki örneklere bakınız. Örnek:

##### Örnek 3.1
```py
main_list = [[[1,2], [3,4,5], [6]], [[7,8,9,10], [11,12]], [[13,14,15], [16], [17,18],[19,20]]]

flatten_list1 = []
for i in main_list:
    for j in i:
        for k in j:
            if k % 2 == 0:
                flatten_list1.append(k)
print(flatten_list1) # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

flatten_list2 = [k for i in main_list for j in i for k in j if k % 2 == 0]
print(flatten_list2) # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

##### Örnek 3.1
```py
main_list = [[[1,2], [3,4,5], [6]], [[7,8,9,10], [11,12]], [[13,14,15], [16], [17,18],[19,20]]]

flatten_list1 = []
for i in main_list:
    for j in i:
        for k in j:
            if k % 2 == 0:
                flatten_list1.append(k)
            else:
                flatten_list1.append(k*0)
print(flatten_list1) # Output: [0, 2, 0, 4, 0, 6, 0, 8, 0, 10, 0, 12, 0, 14, 0, 16, 0, 18, 0, 20]

flatten_list2 = [(k if k % 2 == 0 else k*0) for i in main_list for j in i for k in j]
print(flatten_list2) # Output: [0, 2, 0, 4, 0, 6, 0, 8, 0, 10, 0, 12, 0, 14, 0, 16, 0, 18, 0, 20]
```

#### Örnek 4
Mevcut **nested** listeden başka bir **nested** liste üretmek için aşağıdaki örneklere bakınız.

##### Örnek 4.1
```py
main_list = [1,2,3]

liste1 = []
for i in range(2):
    temp_list = []
    for j in main_list:
        temp_list.append(j)
    liste1.append(temp_list)
print(liste1) # Output: [[1, 2, 3], [1, 2, 3]]

liste2 = [[j for j in main_list] for i in range(2)]
print(liste2) # Output: [[1, 2, 3], [1, 2, 3]]
```
Yukarıdaki `[j for j in main_list] for i in range(2)` yapısının, `j for i in main_list for j in i` yapısından farkı, `[j for j in main_list] for i in range(2)` yapısının `expression for item in list` syntax'ının mantığıyla çalışmasıdır çünkü `[j for j in main_list] for i in range(2)` yapı ile `expression for item in list` syntax'ı aynı şeydir. Yani `expression for item in list` syntax'ındaki `expression`, `[j for j in main_list] for i in range(2)` yapısındaki `[j for j in main_list]` kısmına karşılık gelmektedir.

##### Örnek 4.2
```py
main_list = [[1, 2, 3, 4], [5, 6, 7, 8]]

list1 = []
for i in range(0, len(main_list[0])):
    temp_list = []
    for j in main_list:
        temp_list.append(j[i])
    list1.append(temp_list)
    temp_list = []
print(list1) # Output: [[1, 5], [2, 6], [3, 7], [4, 8]]

list2 = [[j[i] for j in main_list] for i in range(len(main_list[0]))]
print(list2) # Output: [[1, 5], [2, 6], [3, 7], [4, 8]]
```

##### Örnek 4.3
```py
main_list = [[1, 2], [3, 4], [5, 6], [7, 8]]

list1 = []
for i in range(0, len(main_list[0])):
    temp_list = []
    for j in main_list:
        temp_list.append(j[i])
    list1.append(temp_list)
    temp_list = []
print(list1) # Output: [[1, 3, 5, 7], [2, 4, 6, 8]]

list2 = [[j[i] for j in main_list] for i in range(len(main_list[0]))]
print(list2) # Output: [[1, 3, 5, 7], [2, 4, 6, 8]]
```

## Dictionary Comprehension
Bir **Generator Comprehension**'ı, `dict` data type'ında kullandığımız yapıdır. `{item_1:item_1 for item_1 in iterable}` syntax'ına sahiptir. Örnek:
```py
dict_exp = {(i):(i**2) for i in range(1,4)}

print(dict_exp) # Output: {1: 1, 2: 4, 3: 9}

for i in dict_exp:
    print(i, end=" ") # Output: 1 2 3
```
`{item_1:item_1 for item_1 in iterable}` syntax'ını kullanmak zorunda değilsiniz. Bir **Generator** objesi oluşturup sonradan bu objeyi dictionary'e de dönüştürebilirsiniz ama `{item_1:item_1 for item_1 in iterable}` syntax'ını kullanmak daha uygundur.
```py
generator_exp = ((i,i**2) for i in range(5))
print(generator_exp) # Output: <generator object <genexpr> at 0x0000016A87522120>

dict_exp = list(generator_exp)
print(dict_exp) # Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

dict_exp = dict(generator_exp)
print(dict_exp) # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(type(dict_exp)) # Output: <class 'dict'>

for i in dict_exp:
    print(i, end=" ") # Output: 0 1 2 3 4
```
Aşağıda, 0'dan 10'a kadar (0 ve 10 dahil) olan sayıların çift olanlarının karalerini alan ve bunları dictionary halinde depolayan özel bir yapı vardır.
```py
dict_exp = {i:i**2 for i in range(11) if i % 2 == 0}
print(dict_exp) # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```
Bu koddaki `[i for i in range(60) if i % 6 == 0]` kodu aşağıdaki anlama gelmektedir:
```py
dict_exp = dict()
for i in range(11):
    if i % 2 == 0:
        dict_exp.update({i:i**2})
```

### Nested Dictionary Comprehension
`{1: {1: 1, 2: 4}, 2: {1: 1, 2: 4}}` gibi nested dictionary'leri oluşturmak ya da böyle dictionary'ler üzerinde işlemler yapmak için kullanılan yapıya denir. Örnekler:

#### Örnek 1
**Nested** dictionary oluşturmak için aşağıdaki örneklere bakınız.

##### Örnek 1.1
```py
dict1 = dict()
for i in range(1,3):
    temp_dict1 = {i:{}}
    print(type(temp_dict1))
    for j in range(1,3):
        temp_dict2 = {j:j**2}
        temp_dict1[i].update(temp_dict2)
    dict1.update(temp_dict1)
print(dict1) # Output: {1: {1: 1, 2: 4}, 2: {1: 1, 2: 4}}

dict2 = {i:{j:j**2 for j in range(1,3)} for i in range(1,3)}
print(dict2) # Output: {1: {1: 1, 2: 4}, 2: {1: 1, 2: 4}}
```
##### Örnek 1.2
```py
dict1 = dict()
for i in range(1,3):
    temp_dict1 = {i:{}}
    print(type(temp_dict1))
    for j in range(1,3):
        temp_dict2 = {i:j**2}
        temp_dict1[i].update(temp_dict2)
    dict1.update(temp_dict1)
print(dict1) # Output: {1: {1: 4}, 2: {2: 4}}

dict2 = {i:{i:j**2 for j in range(1,3)} for i in range(1,3)}
print(dict2) # Output: {1: {1: 4}, 2: {2: 4}}
```

#### Örnek 2
Mevcut **nested** dictionary'yi ayrıştırma için aşağıdaki örneklere bakınız.

##### Örnek 2.1
```py
main_dict = {"1 key":{"nested 1.1 key":"nested 1.1 value",
                      "nested 1.2 key":"nested 1.2 value",
                      "nested 1.3 key":"nested 1.3 value"},
             "2 key":{"nested 2.1 key":"nested 2.1 value"},
             "3 key":{"nested 3.1 key":"nested 3.1 value",
                      "nested 3.2 key":"nested 3.2 value"}}

dict1 = dict()
for i in main_dict:
    for j in main_dict[i]:
        dict1.update({j:main_dict[i][j]})
print(dict1) # Output: {'nested 1.1 key': 'nested 1.1 value', 'nested 1.2 key': 'nested 1.2 value', 'nested 1.3 key': 'nested 1.3 value', 'nested 2.1 key': 'nested 2.1 value', 'nested 3.1 key': 'nested 3.1 value', 'nested 3.2 key': 'nested 3.2 value'}

dict2 = {j:main_dict[i][j] for i in main_dict for j in main_dict[i]}
print(dict2) # Output: {'nested 1.1 key': 'nested 1.1 value', 'nested 1.2 key': 'nested 1.2 value', 'nested 1.3 key': 'nested 1.3 value', 'nested 2.1 key': 'nested 2.1 value', 'nested 3.1 key': 'nested 3.1 value', 'nested 3.2 key': 'nested 3.2 value'}

print(dict1 == dict2) # Output: True
```
**Not:** `main_dict` variable'ına
```py
main_dict = {"0 key":"0 value",
             "1 key":{"nested 1.1 key":"nested 1.1 value",
                      "nested 1.2 key":"nested 1.2 value",
                      "nested 1.3 key":"nested 1.3 value"},
             "2 key":{"nested 2.1 key":"nested 2.1 value"},
             "3 key":{"nested 3.1 key":"nested 3.1 value",
                      "nested 3.2 key":"nested 3.2 value"}}
```
tarzı bir dictionary girilseydi `TypeError: string indices must be integers` hatası ile karşılaşılırdı çünkü `"0 key":"0 value"` argümanı yüzünden `for j in main_dict[i]` kodundaki `main_dict[i]`'ye denk gelen değer `"0 value"` olduğu için``for j in main_dict[i]` kodu bu string'i parça parça alacaktır. Bu yüzden `dict1.update({j:main_dict[i][j]})` kodundaki `main_dict[i][j]` kısmındaki `main_dict[i]`'ye denk gelen değer ve `j` variable'ının içerdiği değer string olduğu için Python string bir değerin indexlerine string bir değerle ulaşamıyor (çünkü string bir data type'ın indexlerine `"0 value"[3]` gibi integer değerlerle ulaşırsın, `"0 value"['v']` gibi string bir değerle ulaşamazsın) ve `TypeError: string indices must be integers` hatası veriyor.

##### Örnek 2.2
```py
main_dict = {"1 key":{"nested 1.1 key":{"2x nested 1.1.1 key":"2x nested 1.1.1 value",
                                        "2x nested 1.1.2 key":"2x nested 1.1.2 value"},
                      "nested 1.2 key":{"2x nested 1.2.1 key":"2x nested 1.2.1 value"},
                      "nested 1.3 key":{"2x nested 1.3.1 key":"2x nested 1.3.1 value",
                                        "2x nested 1.3.2 key":"2x nested 1.3.2 value",
                                        "2x nested 1.3.3 key":"2x nested 1.3.3 value"}},
             "2 key":{"nested 2.1 key":{"2x nested 2.1.1 key":"2x nested 2.1.1 value",
                                        "2x nested 2.1.2 key":"2x nested 2.1.2 value",
                                        "2x nested 2.1.3 key":"2x nested 2.1.3 value"}},
             "3 key":{"nested 3.1 key":{"2x nested 3.1.1 key":"2x nested 3.1.1 value",
                                        "2x nested 3.1.2 key":"2x nested 3.1.2 value"},
                      "nested 3.2 key":{"2x nested 3.2.1 key":"2x nested 3.2.1 value"}}}

dict1 = dict()
for i in main_dict:
    for j in main_dict[i]:
        for k in main_dict[i][j]:
            dict1.update({k:main_dict[i][j][k]})
print(dict1) # Output: {'2x nested 1.1.1 key': '2x nested 1.1.1 value', '2x nested 1.1.2 key': '2x nested 1.1.2 value', '2x nested 1.2.1 key': '2x nested 1.2.1 value', '2x nested 1.3.1 key': '2x nested 1.3.1 value', '2x nested 1.3.2 key': '2x nested 1.3.2 value', '2x nested 1.3.3 key': '2x nested 1.3.3 value', '2x nested 2.1.1 key': '2x nested 2.1.1 value', '2x nested 2.1.2 key': '2x nested 2.1.2 value', '2x nested 2.1.3 key': '2x nested 2.1.3 value', '2x nested 3.1.1 key': '2x nested 3.1.1 value', '2x nested 3.1.2 key': '2x nested 3.1.2 value', '2x nested 3.2.1 key': '2x nested 3.2.1 value'}

dict2 = {k:main_dict[i][j][k] for i in main_dict for j in main_dict[i] for k in main_dict[i][j]}
print(dict2) # Output: {'2x nested 1.1.1 key': '2x nested 1.1.1 value', '2x nested 1.1.2 key': '2x nested 1.1.2 value', '2x nested 1.2.1 key': '2x nested 1.2.1 value', '2x nested 1.3.1 key': '2x nested 1.3.1 value', '2x nested 1.3.2 key': '2x nested 1.3.2 value', '2x nested 1.3.3 key': '2x nested 1.3.3 value', '2x nested 2.1.1 key': '2x nested 2.1.1 value', '2x nested 2.1.2 key': '2x nested 2.1.2 value', '2x nested 2.1.3 key': '2x nested 2.1.3 value', '2x nested 3.1.1 key': '2x nested 3.1.1 value', '2x nested 3.1.2 key': '2x nested 3.1.2 value', '2x nested 3.2.1 key': '2x nested 3.2.1 value'}

print(dict2 == dict1) # Output: True
```
Yukarıdaki `k:main_dict[i][j][k] for i in main_dict for j in main_dict[i] for k in main_dict[i][j]` kodu şöyle çalışır:
- En baştaki `k:main_dict[i][j][k]`, en içteki nested `for` loop'un `item`'idir yani `dict1.update({k:main_dict[i][j][k]})` kısmını temsil eder.
- `k:main_dict[i][j][k] for i in main_dict for j in main_dict[i] for k in main_dict[i][j]` kodunu `(k:main_dict[i][j][k]) (for i in main_dict) (for j in main_dict[i]) (for k in main_dict[i][j])` şeklinde parçalarsak, `for i in main_dict` **enclosing**, ondan sonrakiler soldan sağa doğru **nested** `for` loop oluyor. Yani soldan sağa doğru **nested**'lık artıyor. En sağdaki for loop'un item'ı da (örneğin yukarıdaki `for k in main_dict[i][j]`'ın `k` item'i), en baştaki expression'ı (örneğin yukarıdaki kodun en sağındaki `k:main_dict[i][j][k]`) temsil eder.

**Not:** Dictionary objelerinde **nested**'lik ile bu dictionary'ye erişen **Nested Dictionary Comprehension** objelerindeki `for` loop sayısı doğru orantılıdır. Yani bir dictionary objesi 2 katman (Öreneğin `{1:{1:1, 2:2}, 2:{1:1, 2:2}}`) **nested** ise, bu dictionary'ye erişen **Nested Dictionary Comprehension** objelerindeki `for` loop (Örneğin `j:main_dict[i][j] for i in main_dict for j in main_dict[i]`) sayısı da 2'dir.

#### Örnek 3
**Nested Dictionary Comprehension** objesi oluştururken belli bir koşul belirleyebilirsiniz. Mevcut **nested** dictionary'yi koşula göre ayrıştırma için aşağıdaki örneklere bakınız. Örnek:
```py
main_dict = {1:{0:0, 2:4, 4:16}, 2:{6:36, 8:64, 10:100}}

dict1 = dict()
for i in main_dict:
    for j in main_dict[i]:
        if main_dict[i][j] > 50:
            dict1.update({j:main_dict[i][j]})
print(dict1) # Output: {8: 64, 10: 100}

dict2 = {j:main_dict[i][j] for i in main_dict for j in main_dict[i] if main_dict[i][j] > 50}
print(dict2) # Output: {8: 64, 10: 100}

print(dict1 == dict2) # Output: True
```