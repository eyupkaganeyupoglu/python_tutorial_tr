# İçindekiler

- [Range](#1)
    - [Range Methodları](#1.1)
        - [`index(value)` Methodu](#1.1.1)
        - [`count(value)` Methodu](#1.1.2)

<h1 id="1">Range</h1>

Range, belli bir sayısal aralığı temsil eden spesifik obje türüne verilen isimdir. `range()` build-in fonksiyonu ile range objeleri yaratabilirsiniz. `range(start=0, stop, step=1)` syntax'ına sahip bu fonksiyonuna girilen argümanlar integer type ya da `__index__` methodu uygulanmış (implement) bir obje olabilir.
- `start` parametresine girilen integer type argüman, başlangıç değerini ifade eder ve dahil edilir. Örneğin `print(tuple(range(2,5))) # Output: (2,3,4)` gördüğünüz gibi start parametresine girilen `2` dahil edilmiş. `start` parametresi girilmezse (omitted, ihmal etmek) bu parametre default değeri olan `0`'ı kullanır.
- `stop` parametresine girilen integer type argüman, bitiş değerini ifade eder ve dahil edilmez. Örneğin `print(tuple(range(2,5))) # Output: (2,3,4)` gördüğünüz gibi stop parametresine girilen `5` dahil edilmiş.
- `step` parametresine girilen integer type argüman, atlama değerini ifade eder. `step` parametresi girilmezse (omitted, ihmal etmek) bu parametre default değeri olan `1`'ı kullanır. Bu parametre `0` olarak girilirse `ValueError: range() arg 3 must not be zero` hatası yükseltilir çünkü matematiksel olarak bir sayıya `0` ekleyerek o sayıyı arttıramadığınız için `range()` fonksiyonunun amacına aykırı bir durum oluşuyor ve hata yükseltiliyor.
    - `step` pozitif bir değer olursa, bir `r` varaible'ına atanmış `range()` fonksiyonunun her bir öğesi `i >= 0` ve `r[i] < stop` olmak üzere, `r[i] = start + step*i` formülü ile hesaplanır. Örnek:
        ```
        `i >= 0` ve `r[i] < stop` olmak üzere, `r[i] = start + step*i`

        range(0,5,1) -> 0, 1, 2, 3, 4

        `0 >= 0` ve `r[0] < 5` -> 0 < 5 olmak üzere, `r[0] = 0 + 1*0` -> 0 = 0 + 1*0` √
        `1 >= 0` ve `r[1] < 5` -> 1 < 5 olmak üzere, `r[1] = 0 + 1*1` -> 1 = 0 + 1*1` √
        `2 >= 0` ve `r[2] < 5` -> 2 < 5 olmak üzere, `r[2] = 0 + 1*2` -> 2 = 0 + 1*2` √
        `3 >= 0` ve `r[3] < 5` -> 3 < 5 olmak üzere, `r[3] = 0 + 1*3` -> 3 = 0 + 1*3` √
        `4 >= 0` ve `r[4] < 5` -> 4 < 5 olmak üzere, `r[4] = 0 + 1*4` -> 4 = 0 + 1*4` √
        `5 >= 0` ve `r[5] < 0` -> 5 < 5 olmak üzere, `r[5] = 0 + 1*5` -> 5 = 0 + 1*5` X (5 < 5 sağlamadığı için r[5] dahil edilmez.)

        Not: 5 < 5 sağlamadığı için r[5] dahil edilmez.
        ```
    - `step` negatif bir değer olursa, bir `r` variable'ına atanmış `range()` fonksiyonunun her bir öğesi `i >= 0` ve `r[i] > stop` olmak üzere, `r[i] = start + step*i` formülü ile hesaplanır. Örnek:
        ```
        `i >= 0` ve `r[i] > stop` olmak üzere, `r[i] = start + step*i`

        range(5,0,-1) -> 5, 4, 3, 2, 1

        `0 >= 0` ve `r[0] > 0` -> 5 > 0 olmak üzere, `r[0] = 5 + -1*0` -> 5 = 5 + -1*0` √
        `1 >= 0` ve `r[1] > 0` -> 4 > 0 olmak üzere, `r[1] = 5 + -1*1` -> 4 = 5 + -1*1` √
        `2 >= 0` ve `r[2] > 0` -> 3 > 0 olmak üzere, `r[2] = 5 + -1*2` -> 3 = 5 + -1*2` √
        `3 >= 0` ve `r[3] > 0` -> 2 > 0 olmak üzere, `r[3] = 5 + -1*3` -> 2 = 5 + -1*3` √
        `4 >= 0` ve `r[4] > 0` -> 1 > 0 olmak üzere, `r[4] = 5 + -1*4` -> 1 = 5 + -1*4` √
        `5 >= 0` ve `r[5] > 0` -> 0 > 0 olmak üzere, `r[5] = 5 + -1*5` -> 1 = 5 + -1*5` X (0 > 0 sağlamadığı için r[5] dahil edilmez.)
        ```
    - `range(0,5,-1)` ve `range(5,0,1)` gibi tanımlanmış fonksiyonlar yukarıda bahsedilen formülleri sağlamadığı için boş kümedir, dolayısıyla bunları liste veya tuple'a dönüştürmek isterseniz elinize boş liste ve tuple geçer. Bu yüzden `start`, `stop` ve `step` parametrelerine argüman girerken bu förmüle uymasına dikkat edin.

`range()` fonksiyonu örnekleri:
```py
print(list(range(10))) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 11))) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(0, 30, 5))) # Output: [0, 5, 10, 15, 20, 25]
print(list(range(0, 10, 3))) # Output: [0, 3, 6, 9]
print(list(range(0, -10, -1))) # Output: [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

print(list(range(0))) # Output: []
print(list(range(0, 10, -1))) # Output: []
print(list(range(10, 0, 1))) # Output: []
```

**Not:** `sys.maxsize`, `Py_ssize_t` type bir variable'ın alabileceği max sayıdır. Yani işletim sisteminin bit'lerle ifade edebileceği max büyüklükteki sayıdır. 32 bir sistemlerde `2**31 - 1`, 64 bir sistemlerde `2**63 - 1` kadardır. `sys.maxsize` değerinden daha büyük büyük sayılara izin verilir ama `len()` gibi bazı özellikler (features) `OverflowError` hatasına neden olabilir. Örnek:
```py
print(range(2**63-1)) # Output: range(0, 9223372036854775807)
print(range(2**63)) # Output: range(0, 9223372036854775808)
print(range(2**64)) # Output: range(0, 18446744073709551616)
print(range(2**128)) # Output: range(0, 340282366920938463463374607431768211456)
print(len(range(2**63-1))) # Output: 9223372036854775807
print(len(range(2**63))) # OverflowError: Python int too large to convert to C ssize_t
```

**Not:** `range`'ler, concatenation ve repetition dışında tüm [common sequence operation'ları](https://docs.python.org/3/library/stdtypes.html?highlight=range#typesseq-common "https://docs.python.org/3/library/stdtypes.html?highlight=range#typesseq-common") uygular (implement). Çünkü range obje'leri yalnızca strict bir pattern'i takip eden sequence'ları takip edebilir. Concatenation ve repetition genellikle bu pattern'leri ihlal eder (violate). Burası baya ayrıntı. Merak ettiyseniz terimleri kendiniz araştırabilirsiniz.

**Not:** `range` type'ın `list` ya da `tuple` type'dan avantajlı olmasının sebebi, `range` type sadece `start`, `stop` ve `step` verilerini tuttuğu için `range(0,1,1)` objesi ile `range(0,255,1)` objesinin bellek boyutu aynıdır ama `list(range(0,1,1))` ile `list(range(0,255,1))`'in boyutu aynı değildir.
```py
print(list(range(0,1,1)).__sizeof__()) # Output: 48
print(list(range(0,9999,1)).__sizeof__()) # Output: 80048
print(range(0,1,1).__sizeof__()) # Output: 48
print(range(0,9999,1).__sizeof__()) # Output: 48

print(range(2**63-1)) # Output: range(0, 9223372036854775807)
print(list(range(2**63-1))) # MemoryError
```

**Not:** Range objeleri, diğer [Sequence Types](https://docs.python.org/3/library/stdtypes.html?highlight=range#typesseq) objelere dönüştürebilir, membership (`in`) operator'ı ile içeriğine erişebilir ve index'lenebilir (negatif index'lemeyi destekler). Daha fazla bilgi için [tıklayınız](https://newbedev.com/does-range-really-create-lists).
```py
print(range(-10, 10, 2)) # Output: range(-10, 10, 2)
print(*range(-10, 10, 2)) # Output: -10 -8 -6 -4 -2 0 2 4 6 8

print(-6 in range(-10, 10, 2)) # Output: True
print(-7 in range(-10, 10, 2)) # Output: False

print(range(-10, 10, 2)[5]) # Output: 0
print(range(-10, 10, 2)[:6]) # Output: range(-10, 2, 2)
print(range(-10, 10, 2)[-1]) # Output: 8

print(list(range(-10, 10, 2))) # Output: [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8]
print(tuple(range(-10, 10, 2))) # Output: (-10, -8, -6, -4, -2, 0, 2, 4, 6, 8)
```

**Not:** İki `range` objesinin üzerinde `==` ve `!=` işlemleri yapabiliriz. Bu işlemler, bu iki `range` objesinin içeriği aynı ya da farklı olmasına göre sonuçlar verir. Örnekler:
```py
print(range(0) == range(2,1,3) or range(0,3,2) == range(0,4,2)) # Output: True (Çünkü hepsi boş)

print(list(range(0,2,1))) # Output: [0, 1]
print(list(range(1,-1,-1))) # Output: [1, 0]
print(range(0,2,1) == range(1,-1,-1)) # Output: False

print(range(0,2,1) == range(0,2,1)) # Output: True
print(range(0,2,1) != range(0,2,1)) # Output: False

print(range(0,2,1) == range(2,4,1)) # Output: False
print(range(0,2,1) != range(2,4,1)) # Output: True
```

**Not:** [linspace recipe](https://code.activestate.com/recipes/579000/), floating point application'larda uygun lazy version bir range'in nasıl uygulanacağını (implement) gösterir.

<h2 id="1.1">Range Methodları</h2>

<h3 id="1.1.1"><code>index(value)</code> Methodu</h3>

`value` parametresine argüman olarak girdiğiniz value'nun, uygulandığı range içinde kaçıncı index'de bulunduğunu söyler. Örnek:
```py
print(list(range(0,11,2))) # Output: [0, 2, 4, 6, 8, 10]
print(range(0,11,2).index(4)) # Output: 2
```

<h3 id="1.1.2"><code>count(value)</code> Methodu</h3>

`value` parametresine argüman olarak girdiğiniz value'nun, uygulandığı range içinde kaç kere geçtiğini söyler. Range objesinde girilen aralıktaki her sayı 1 kere bulunduğu için bu methodun sonucu her zaman `1` çıkar. Örnek:
```py
print(list(range(0,11,2))) # Output: [0, 2, 4, 6, 8, 10]
print(range(0,11,2).count(4)) # Output: 1
```