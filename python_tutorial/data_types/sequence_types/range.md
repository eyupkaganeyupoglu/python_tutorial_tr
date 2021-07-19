# range(start, stop, step)
`range()` fonksiyonuna girilen argümanlar integer type olmalıdır (direkt integer data type ya da `__index__` methodu uygulanmış obje argüman olarak kullanılabilir).
- `start`, başlangıç değerini ifade eder. Dahildir. Örnek `list(range(2,5)) == [2,3,4]`. `start` parametresi girilmezse (omitted, ihmal etmek) default olarak 0 kabul edilir.
- `stop` bitiş değerini ifade eder. Dahil değildir. Örnek `list(range(2,5)) == [2,3,4]`
- `step` atlama değerini ifade eder. `step` parametresi girilmezse (omitted, ihmal etmek) default olarak 1 kabul edilir. Bu parametre `0` olarak girilirse `ValueError` hatası alırsınız.
    - `step` pozitif bir değer olursa, bir `r` varaible'sine atanmış `range()`'in içeriği `i >= 0` ve `r[i] < stop` olmak üzere, `r[i] = start + step*i` formülü ile hesaplanır.
    - `step` negatif bir değer olursa, bir `r` varaible'sine atanmış `range()`'in içeriği yine `i >= 0` ve `r[i] < stop` olmak üzere, `r[i] = start + step*i` formülü ile hesaplanır.
    - `list(range(0,10,-1))` ya da `list(range(10,0,1))` gibi bir durumda boş liste döndürür çünkü `i >= 0` ve `r[i] < stop` olmak üzere, `r[i] = start + step*i` formülü sağlanmadığı için loop sona erer ve hiçbir işlem yapılmadığından elimize boş liste geçer.

Örnekler:
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

**Not:** `sys.maxsize` (`Py_ssize_t` type bir variable'ın alabileceği max sayı. 32 bir sistemlerde `2**31 - 1`, 64 bir sistemlerde `2**63 - 1` kadardır.) değerinden daha büyük büyük sayılara izin verilir ama `len()` gibi bazı özellikler (features) `OverflowError` hatasına neden olabilir.

**Not:** Range'ler, concatenation ve repetition dışında tüm [common sequence operation'ları](https://docs.python.org/3/library/stdtypes.html?highlight=range#typesseq-common) uygular (implement). Çünkü range obje'leri yalnızca strict bir pattern'i takip eden sequence'ları takip edebilir. Concatenation ve repetition genellikle bu pattern'leri ihlal eder (violate).

**Not:** `range` type'ın `list` ya da `tuple` type'dan avantajlı olmasının sebebi, `range` type sadece `start`, `stop` ve `step` verilerini tuttuğu için `range(0,1,1)` objesi ile `range(0,255,1)` objesinin bellek boyutu aynıdır ama `list(range(0,1,1))` ile `list(range(0,255,1))`'in boyutu aynı değildir.
```py
print(list(range(0,1,1)).__sizeof__()) # Output: 48
print(list(range(0,9999,1)).__sizeof__()) # Output: 80048
print(range(0,1,1).__sizeof__()) # Output: 48
print(range(0,9999,1).__sizeof__()) # Output: 48E
```

**Not:** Range objelerini diğer [Sequence Types](https://docs.python.org/3/library/stdtypes.html?highlight=range#typesseq) objelere dönüştürebilir, membership (`in`) operator'ı ile içeriğine erişebilir ve indexleyebilirsin (negatif index'lemeyi destekler). Daha fazla bilgi için [tıklayınız](https://newbedev.com/does-range-really-create-lists).
```py
r = range(0, 20, 2)
print(r) # Output: range(0, 20, 2)
print(11 in r) # Output: False
print(10 in r) # Output: True
print(r.index(10)) # Output: 5
print(r[5]) # Output: 10
print(r[:5]) # Output: range(0, 10, 2)
print(r[-1]) # Output: 18
print(list(r)) # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(tuple(r)) # Output: (0, 2, 4, 6, 8, 10, 12, 14, 16, 18)
```

**Not:** İki `range` objesinin üzerinde `==` ve `!=` işlemleri yapabiliriz. Bu işlemler, bu iki `range` objesinin içeriği aynı ya da farklı olmasına göre sonuçlar verir. Örnekler:
```py
print(range(0) == range(2,1,3) or range(0,3,2) == range(0,4,2)) # Output: True (Çünkü hepsi [])

a = range(0,2,1)
b = range(1,-1,-1)
print(list(a),list(b),a==b,sep=" | ") # Output: [0, 1] | [1, 0] | False
print(range(0,2,1) == range(0,2,1)) # Output: True
print(range(0,2,1) != range(0,2,1)) # Output: False

print(range(0,2,1) == range(2,4,1)) # Output: False
print(range(0,2,1) != range(2,4,1)) # Output: True
```

**Not:** [linspace recipe](https://code.activestate.com/recipes/579000/), floating point application'larda uygun lazy version bir range'in nasıl uygulanacağını (implement) gösterir.