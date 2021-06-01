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
`func1` ile `func2` aynı işleve sahiptir. `lambda` fonksiyonuna tanımlanan `arguments`, `def` ile tanımlanan fonksiyonlardaki parametre kısmına denk gelmektedir. `:`'dan sonraki kısım da `def` ile tanımlanan fonksiyonlardaki `return` keyword'ünü temsil eder. Örnek:
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

# Nasted (İç İçe) Fonksiyonlar
İç içe fonksiyonlarda, en dıştaki (yani global scope'da tanımlanan) fonksiyon **enclosing**, enclosing'in scope'una tanımlanan bütün fonksiyonlar da **nasted** olarak isimlenirilir.
```py
def yazıcı():
    print("Yazıcı Çalıştı.")
    def yaz(mesaj):
        print(mesaj)
    return yaz
```
Yukarıdaki fonksiyonda, `yazıcı()` fonksiyonunu çağırmadan `yaz()` fonksiyonunu çağıramayız. Bu her yerde böyledir. Çünkü `yazıcı()` fonksiyonunu çağırdığımızda onu tanımlamış oluyoruz ve `yazıcı()` fonksiyonunu tanımlamadan `yaz()` fonksiyonunu direkt çağıramayız. `yazıcı()` fonksiyonu her çağırıldığında `yaz()` fonksiyonu baştan tanımlanır. Yani `yazıcı()` fonksiyonunu ilk çağırışınızdaki `yaz()` fonksiyonu ile  `yazıcı()` fonksiyonunu ikinci çağırışınızdaki `yaz()` fonksiyonu birbirinden farklı objelerdir. Bu objeler `<function yazıcı.<locals>.yaz at 0x00000210D9235558>` şeklindedir.

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

[`iter()`](asd) fonksiyonu ile, **Iterable** (tekrarlanabilir) bir objenin template'i kullanılara bir **Iterator** objesi oluşturulabilir. Bunu mümkün kılmak için **Iterable** (tekrarlanabilir) bir objenin class'ının, **Iterator** döndüren bir `__iter__` ya da `0` ile başlayan sıralı (sequential) index'lere sahip `__getitem__` methoduna ihtiyacı vardır. `iter()` fonksiyonuna **Iterable** (tekrarlanabilir) olmayan bir obje verilirse, `TypeError` hatası döndürülür. **Iterator**'ler, objenin bir sonraki item'ına geçmeye yarayan `__next__()` methoduna sahiptir. **Iterator**'ler, `__next__()` methodu kullanarak, **Iterable** bir objeden kopyaladıkları template üzerinde iterate (yenileme) yapmak için kullanılan objelerdir.
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

**Not:** Bir **Iterator**, barındırdığı öğe sayısından fazla `next` methodu ya da fonksiyonu kullanılırsa, başka kullanılabilir öğe bulamadığı için `StopIteration` hatası döndürülür. Örnek:
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
    - **Not:** Burada da ilk koddaki gibi `for i in generator():` kullanmak yerine önce `gen = generator()` kodu ile, oluşturulan **Generator** objesini `gen` variable'sine atayıp `gen` variable'sinì kullanmamızın nedeni: `for i in generator():` kodunda oluşan **Generator** objesi ile `f_locals_repo.update(generator().gi_frame.f_locals)` kodunda oluşan **Generator** objesi birbirinden farklı olacağı için `f_locals_repo` data'sını elde edemezdik. Bu yüzden `gen = generator()` kodu çağırılan **Generator** objesi `gen` variable'ına atandı ve bu variable kullanıldı.

**Iterator** ile **Generator**'ün farkları şunlardır:
- **Generator** oluşturmak için fonksiyon kullanılır. **Iterator** oluşturmak için `iter()` ve `next()` fonksiyonları kullanılır.
- **Generator** `yield` keyword'ünü kullanır ama **Iterator** kullanmaz.
- **Generator**'daki `yield`, python'daki loop her duraklatıldığında local variable'ların durumlarını kaydeder. **Iterator** local variable'ları kullanmaz. **Iterator**'e, *iterate* edilebilecek *iterable* bir obje vermeniz yeterlidir. **Generator** ve **Iterator**'ın birbirinden en büyük farkı budur.
- Bir **Generator**'a, herhangi bir sayıda `yield` statement tanımlanabilir.
- Bir class'a **Iterator** implement ederek, **Iterator** ile kullanım desteği kazandırılabilir. **Generator**, python'da bir class'a ihtiyaç duymaz.
- **Generator** yazmak için bir python fonksiyonu ya da **Comprehension** kullanabilirsiniz. **Iterator** yazmak için `iter()` ve `next()` fonksiyonlarını kullanmak zorundasınız.
- Bir **Generator**, **Generator** objesi döndürür (`<generator object generator_exp at 0x0000023D508D6D60>`, `<class ‘generator’>`); bir **Iterator**, kullanılan **Iterable** class'a özel **Iterator** objesi döndürür (Örneğin bir list'i **Iterator**'e dönüştürürseniz, o **Iterator** objesi, oluşturulduğu **Iterable** class'a göre özelleşir: `<list_iterator object at 0x0000023D508EDFD0>`, `<class ‘list_iterator’>`).
- **Iterator**, bellek açısından daha verimlidir (more memory-efficient). Bir **Generator**, `__sizeof__()` methoduyla kullanılırsa 32; bir **Iterator**, `__sizeof__()` methoduyla kullanılırsa 16 outputunu verir.
- **Generator**, co-routines'de (ortak rutinler) daha fazla functionality sağlar.
- **Generator**'ler ve **Iterator**'ler, **iterable object**'e (Yenilenebilir sınıflara) örnektir.

**Not:** Bir **Generator** ya da **Iterator**, barındırdığı öğe sayısından fazla `next` methodu ya da fonksiyonu kullanılırsa, başka kullanılabilir öğe bulamadığı için `StopIteration` hatası döndürülür. Örnek:
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
`yield` keyword'ü, tek başınayken keyword, bir değer döndürürken (örneğin `yield local_vrb`) statement olarak isimlendirilir. Ne işe yaradığı yukarıda bahsedildi. Spesifik olarak aşağıdaki mekaniklere sahiptir:

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