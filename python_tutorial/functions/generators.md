# İçindekiler

- [Generators (Üreteçler)](#1)
    - [`yield` Statement](#1.1)

<h1 id="1">Generators (Üreteçler)</h1>

**Dikkat:** Generator'ü anlatmaya başlamadan önce şunu kafanıza kazıyın! Her generator bir iterator'dır. Çünkü iterator, generator'ı da kapsayan genel bir kavramdır. Yani Generator'lar bir çeşit iterable objedir.

`def` statement ile tanımladığımız bir fonksiyonun kod block'unun herhangi bir yerinde `yield` statement varsa, bu fonksiyon çağırıldığında bir generator objesi yaratılır (create). Örnek:
```py
def func(p1):
    if p1 == 1:
        return 1
    else:
        yield 2

exp1 = func(1)
exp2 = func(2)
print(func) # Output: <function func at 0x0000015B600DCE50>
print(exp1) # Output: <generator object func at 0x0000024823442120>
print(exp2) # Output: <generator object func at 0x0000024823466D60>
```
Gördüğünüz gibi `else` bloğu çalışsa da çalışmasa da `func` fonksiyonundan bir generator objesi yaratıldı (create).

Bir fonksiyon `return` statement ile karşılaşınca sonlanır ve sonlandığı için kapsamındaki objeler ve değerler bellekten silinir ama bir generetor `yield` statement ile karşılaşınca sonlanmaz ve sonlanmadığı için local objeler ve değerler bellekten silinmez. Bu yüzden RAM'in dolmasına sebep olabilir. Bunu RAM'inizin doluluğunu gösteren bir uygulama (windows için görev yöneticisi) ile gözlemleyebilirsiniz. Aşağıda aunı işleve sahip bir fonksiyon ve bir generator örneği verilmiştir:
```py
def function():
    sayı = 0
    def say():
        nonlocal sayı
        sayı += 1
        return sayı
    return say

say = function()
print(say) # Output: <function function.<locals>.say at 0x000001862C744040>
print(say()) # Output: 1
print(say()) # Output: 2
print(say()) # Output: 3

def generator():
    sayı = 0
    while True:
        sayı += 1
        yield sayı

genr = generator()
print(genr) # Output: <generator object generator at 0x000001A1EAA12120>
print(next(genr)) # Output: 1
print(next(genr)) # Output: 2
print(next(genr)) # Output: 3
```

Bir generator'a barındırdığı item sayısından fazla `next` methodu ya da fonksiyonu uygulanırsa, item bulunamadığı için generator yinelenemez ve `StopIteration` hatası yükseltilir. Generator objesi sonlandığında (yani `StopIteration` hatası oluştuğunda), local objeler ve değerler bellekten silinir. Örnek:
```py
def generator():
    i = 1
    yield

genr = generator()
genr.__next__()
print(genr.gi_frame.f_locals) # Output: {'i': 1}
try:
    print(next(genr)) # StopIteration
except:
    pass
print(genr.gi_frame) # Output: None
```

`next` fonksiyonu ve `__next__()` methodu, uygulandıkları generator objesinin `yield` statement'ları ile ilişkilidir. Yani her next işlemi bir `yield` statement tüketir. Örnek:
```py
def generator_exp1():
    yield

gen1 = generator_exp1()
loop_cnt = 0

try:
    for y in range(100):
        gen1.__next__()
        loop_cnt += 1
        
except StopIteration:
    print(loop_cnt)
    print("StopIteration hatası yükseltildi")
```
```
1
StopIteration hatası yükseltildi
```
`generator_exp1` bir tane `yield` statement'a sahip olduğu için bu fonksiyondan türetilen generator objesi üzerinde `StopIteration` hatası yükseltilene kadar bir kere yield işlemi yapılabiliyor. Bu yüzden for loop bir kere yineleniyor (`loop_cnt` variable'ının `1` değerine sahip olması bunu kanıtlıyor).
```py
def generator_exp2():
    yield
    yield

gen2 = generator_exp2()
loop_cnt = 0

try:
    for y in range(100):
        gen2.__next__()
        loop_cnt += 1

except StopIteration:
    print(loop_cnt)
    print("StopIteration hatası yükseltildi")
```
```
2
StopIteration hatası yükseltildi
```
`generator_exp2` iki tane `yield` statement'a sahip olduğu için bu fonksiyondan türetilen generator objesi üzerinde `StopIteration` hatası yükseltilene kadar iki kere yield işlemi yapılabiliyor. Bu yüzden for loop iki kere yineleniyor (`loop_cnt` variable'ının `2` değerine sahip olması bunu kanıtlıyor). bu iki örnekle "Her next işlemi bir `yield` statement tüketir" iddasını kanıtlamış olduk. Bundan sonra "Generator objesi her next'lendiğinde" dediğimde "Generator objesi her `yield` statement ile karşılaştığında" olarak anlayın.

**Not:** Generator objeleri fonksiyonlar gibi çağırılabilir (callable) değildir. Çağırmaya çağışırsanız `TypeError: 'generator' object is not callable` hatası yükseltilir. Örnek:
```py
def generator_exp():
    i = 1
    j = 2
    k = 3
    yield

gen = generator_exp()
print(callable(generator_exp),callable(gen)) # Output: True False
gen() # TypeError: 'generator' object is not callable
```

**Not:** `return` statement'ın Türkçe karşılığı "döndürmek", `yield` statement'ın Türkçe karşılığı "vermek"dir. Bundan sonra `yield` statement'dan "... değerini yield eder." şeklinde değil "... değerini verir." şeklinde bahsedeceğim.

**Not:** Bir generator objesinin içerdiği bütün local objeler, bu generator objesinin `gi_frame` (frame objesi) adındaki propery methodunda bulunan `f_locals` dictionary'sinde bulunur. Örnek:
```py
def generator_exp():
    i = 1
    j = 2
    k = 3
    yield

gen = generator_exp()
gen.__next__()
print(type(gen.gi_frame)) # Output: <class 'frame'>
print(type(gen.gi_frame.f_locals)) # Output: <class 'dict'>
print(gen.gi_frame.f_locals) # Output: {'i': 1, 'j': 2, 'k': 3}
```

![](./pics/1.png)

**Not:** `f_locals` dictionary'sindeki veriler, generator objesi her next'lendiğinde güncellenir. Yani generator next'lendiğinde, local variable'ların durumları kaydedilir.  Örnek:
```py
def generator_exp():
    for i in ["a1", "a2"]:
        for j in ["b1", "b2"]:
            for k in ["c1", "c2"]:
                yield

gen = generator_exp()

for y in range(100):
    gen.__next__()
    print(gen.gi_frame.f_locals)
```
**Output:**
```
{'i': 'a1', 'j': 'b1', 'k': 'c1'}
{'i': 'a1', 'j': 'b1', 'k': 'c2'}
{'i': 'a1', 'j': 'b2', 'k': 'c1'}
{'i': 'a1', 'j': 'b2', 'k': 'c2'}
{'i': 'a2', 'j': 'b1', 'k': 'c1'}
{'i': 'a2', 'j': 'b1', 'k': 'c2'}
{'i': 'a2', 'j': 'b2', 'k': 'c1'}
{'i': 'a2', 'j': 'b2', 'k': 'c2'}
Traceback (most recent call last):
  File "d:\TP1.py", line 9, in <module>
    gen.__next__()
StopIteration
```

Iterator ile generator'ın farkları şunlardır:
- Generator'lar fonksiyonlar gibi `def` statement ile tanımlanır. Iterator oluşturmak için `iter()` ve `next()` fonksiyonları kullanılır.

- Generator `yield` statement'ını kullanır ama iterator kullanmaz.

- Generator `yield` statement ile karşılaşınca local variable'ların durumları kaydedilir. Iterator, local variable'ları kullanmaz. Iterator'a yineleyebileceği (iterate) iterable bir obje vermeniz yeterlidir. Generator ve iterator'ın en büyük farkı budur.

- Bir generator'a herhangi bir sayıda `yield` statement tanımlanabilir.

- Bir class'a iterator uygulayarak (implement), iterator ile kullanım desteği kazandırılabilir. Örneğin `list` class'ına `__iter__` methodu uygulandığı (implement) için `list` class'ından türetilen objelerinden yararlanarak `iter()` fonksiyonu ile iterator objesi oluşturabiliyoruz. Generator objesi oluşturmak için bir class'a ihtiyaç yoktur. `yield` statement kullanmanız yeterlidir. Python onu generator objesine dönüştürecektir.

- Generator oluşturmak için bir Python fonksiyonu (`def` statement ile tanımlanandan bahsediyorum) ya da **Comprehension** kullanabilirsiniz. Iterator oluşturmak için `iter()` fonksiyonlarını kullanmak zorundasınız.

- Generator objesi `<generator object generator_exp at 0x0000023D508D6D60>`, `<class 'generator'>` şeklindedir. Bir iterator, kullanılan iterable type'a (class'a) özel farklı formlar kazanır. Örneğin `list` type bir objeyi kullanarak oluşturulan iterator objesi `<list_iterator object at 0x0000023D508EDFD0>`, `<class 'list_iterator'>` şeklinde; `tuple` type bir objeyi kullanarak oluşturulan iterator objesi `<tuple_iterator object at 0x000001B30B15DFD0>, <class 'tuple_iterator'>` şeklinde olacaktır. Diğer type'ları kendiniz deneyerek keşfedebilirsiniz.

- iterator'lar generator'lara göre bellek açısından daha verimlidir (memory-efficient). `__sizeof__()` methodunu kullanarak generator'ın bellekte 96, iterator'ın 32 byte yer kapladığını görebilirsiniz. Örnek:
    ```py
    # For windows 10 pro
    iterator_exp = iter(tuple())

    def generator_exp():
        yield

    print(iterator_exp.__sizeof__()) # Output: 32
    print(generator_exp.__sizeof__()) # Output: 96
    ```

- Generator, ortak rutinlerde (co-routines) daha fazla işlevsellik (functionality) sağlar.

- Generator'ler ve iterator'ler, **iterable object**'e (yinelenebilir sınıflar) örnektir.

<h2 id="1.1"><code>yield</code> Statement</h2>

`yield` statement'in temel işlevi yukarıdaki kısımlarda anlatıldı. Bunlara ek olarak `yield` statement aşağıda anlatılan mekaniklere sahiptir.

Bir generator'ın içinde başka bir generator yinelenebilir. Örnek:
```py
def generator1():
    yield "generator1 başladı"
    yield "generator1 bitti"

def generator2():
    yield "generator2 başladı"
    for i in generator1(): yield i
    yield "generator2 bitti"

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
Buradaki olayın aynısı `yield from` kullanılarak elde edilebilir. Örnek:
```py
def generator1():
    yield "generator1 başladı"
    yield "generator1 bitti"

def generator2():
    yield "generator2 başladı"
    yield from generator1() # (generator1 direkt bitene kadar çalışır)
    yield "generator2 bitti"

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
Yani `yield from generator1()` ile `for i in generator1(): yield i` aynı işleve sahiptirler.