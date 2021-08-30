# İçindekiler

- [Range](#1)
    - [Range Methodları](#1.1)
        - [`index(value)` Methodu](#1.1.1)
        - [`count(value)` Methodu](#1.1.2)

<h1 id="1">Range</h1>

Range, belli bir sayısal aralığı temsil eden spesifik obje türüne (type) verilen isimdir. `range()` build-in fonksiyonu ile range objeleri yaratabilirsiniz. `range(start=0, stop, step=1)` fonksiyonuna girilen argümanlar direkt integer type ya da `__index__` methodu uygulanmış (implement) bir obje olabilir.
- `start` parametresine girilen integer type argüman, başlangıç değerini ifade eder. Oluşturuşturulan sayı topluluğuna bu integer değer dahil edilir. Örnek `list(range(2,5)) == [2,3,4]`. `start` parametresi girilmezse (omitted, ihmal etmek) default olarak `0` kabul edilir.
- `stop` parametresine girilen integer type argüman, bitiş değerini ifade eder. Oluşturuşturulan sayı topluluğuna bu integer değer dahil edilmez. Örnek `list(range(2,5)) == [2,3,4]`. `range()` fonksiyonunu kullanabilmek için `stop` parametresine argüman girilmelidir.
- `step` parametresine girilen integer type argüman, atlama değerini ifade eder. `step` parametresi girilmezse (omitted, ihmal etmek) default olarak `1` kabul edilir. Bu parametre `0` olarak girilirse `ValueError: range() arg 3 must not be zero` hatası yükseltilir çünkü matematiksel olarak bir sayıya `0` ekleyerek o sayıyı arttıramazsınız. Bu da `range()` fonksiyonunun işlevine aykırıdır.
    - `step` pozitif bir değer olursa, bir `r` varaible'ına atanmış `range()` fonksiyonunun içeriği `i >= 0` ve `r[i] < stop` olmak üzere, `r[i] = start + step*i` formülü ile hesaplanır. Örnek:
        ```
        `i >= 0` ve `r[i] < stop` olmak üzere, `r[i] = start + step*i`

        range(0,5,1) -> 0, 1, 2, 3, 4

        `0 >= 0` ve `r[0] < 5` -> 0 > 5 olmak üzere, `r[0] = 0 + 1*0` -> 0 = 0 + 1*0` √
        `1 >= 0` ve `r[1] < 5` -> 1 > 5 olmak üzere, `r[1] = 0 + 1*1` -> 1 = 0 + 1*1` √
        `2 >= 0` ve `r[2] < 5` -> 2 > 5 olmak üzere, `r[2] = 0 + 1*2` -> 2 = 0 + 1*2` √
        `3 >= 0` ve `r[3] < 5` -> 3 > 5 olmak üzere, `r[3] = 0 + 1*3` -> 3 = 0 + 1*3` √
        `4 >= 0` ve `r[4] < 5` -> 4 > 5 olmak üzere, `r[4] = 0 + 1*4` -> 4 = 0 + 1*4` √
        ```
    - `step` negatif bir değer olursa, bir `r` variable'ına atanmış `range()` fonksiyonunun içeriği `i >= 0` ve `r[i] > stop` olmak üzere, `r[i] = start + step*i` formülü ile hesaplanır. Örnek:
        ```
        `i >= 0` ve `r[i] > stop` olmak üzere, `r[i] = start + step*i`

        range(5,0,-1) -> 5, 4, 3, 2, 1

        `0 >= 0` ve `r[0] > 0` -> 5 > 0 olmak üzere, `r[0] = 5 + -1*0` -> 5 = 5 + -1*0` √
        `1 >= 0` ve `r[1] > 0` -> 4 > 0 olmak üzere, `r[1] = 5 + -1*1` -> 4 = 5 + -1*1` √
        `2 >= 0` ve `r[2] > 0` -> 3 > 0 olmak üzere, `r[2] = 5 + -1*2` -> 3 = 5 + -1*2` √
        `3 >= 0` ve `r[3] > 0` -> 2 > 0 olmak üzere, `r[3] = 5 + -1*3` -> 2 = 5 + -1*3` √
        `4 >= 0` ve `r[4] > 0` -> 1 > 0 olmak üzere, `r[4] = 5 + -1*4` -> 1 = 5 + -1*4` √
        `5 >= 0` ve `r[5] > 0` -> 1 > 0 olmak üzere, `r[5] = 5 + -1*5` -> 1 = 5 + -1*5` X (`r[5]` out of range)
        ```
    - `range(0,5,-1)` ve `range(5,0,1)` gibi `range` fonksiyonları yukarıda bahsedilen formülleri sağlamadığı için hiçbir değer döndürmez ve bu yüzden `list(range(0,5,-1))` ve `list(range(5,0,1))` kodları boş liste objeleri döndürür.

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

**Not:** `sys.maxsize` (`Py_ssize_t` type bir variable'ın alabileceği max sayı. Yani işletim sisteminin bit'lerle ifade edebileceği max büyüklükteki sayı. 32 bir sistemlerde `2**31 - 1`, 64 bir sistemlerde `2**63 - 1` kadardır) değerinden daha büyük büyük sayılara izin verilir ama `len()` gibi bazı özellikler (features) `OverflowError` hatasına neden olabilir. Örnek:
```py
print(range(2**63-1)) # Output: range(0, 9223372036854775807)
print(range(2**63)) # Output: range(0, 9223372036854775808)
print(range(2**64)) # Output: range(0, 18446744073709551616)
print(range(2**128)) # Output: range(0, 340282366920938463463374607431768211456)
print(len(range(2**63-1))) # Output: 9223372036854775807
print(len(range(2**63))) # OverflowError: Python int too large to convert to C ssize_t
```

**Not:** Range'ler, concatenation ve repetition dışında tüm [common sequence operation'ları](https://docs.python.org/3/library/stdtypes.html?highlight=range#typesseq-common "https://docs.python.org/3/library/stdtypes.html?highlight=range#typesseq-common") uygular (implement). Çünkü range obje'leri yalnızca strict bir pattern'i takip eden sequence'ları takip edebilir. Concatenation ve repetition genellikle bu pattern'leri ihlal eder (violate). Burası baya ayrıntı. Merak ettiyseniz terimleri kendiniz araştırabilirsiniz.

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
r = range(0, 20, 2)
print(r) # Output: range(0, 20, 2)

print(10 in r) # Output: True
print(11 in r) # Output: False

print(r[5]) # Output: 10
print(r[:5]) # Output: range(0, 10, 2)
print(r[-1]) # Output: 18

print(list(r)) # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(tuple(r)) # Output: (0, 2, 4, 6, 8, 10, 12, 14, 16, 18)
```

**Not:** İki `range` objesinin üzerinde `==` ve `!=` işlemleri yapabiliriz. Bu işlemler, bu iki `range` objesinin içeriği aynı ya da farklı olmasına göre sonuçlar verir. Örnekler:
```py
print(range(0) == range(2,1,3) or range(0,3,2) == range(0,4,2)) # Output: True (Çünkü hepsi hiçbir değer içermiyor)

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