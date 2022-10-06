# İçindekiler
- [`bool(x)` Fonksiyonu](#1)
    - [Boolean Type Fonksiyonları](#1.1)
        - [`as_integer_ratio()` Methodu](#1.1.1)
        - [`bit_length()` Methodu](#1.1.2)
        - [`to_bytes(length, byteorder, signed=False)` Methodu](#1.1.3)
        - [`from_bytes(bytes, byteorder, signed=False)` Methodu](#1.1.4)
        - [`conjugate()` Methodu](#1.1.5)
        - [`denominator` Methodu](#1.1.6)
        - [`numerator` Methodu](#1.1.7)
        - [`imag()` Methodu](#1.1.8)
        - [`real()` Methodu](#1.1.9)

<h1 id="1"><code>bool(x)</code> Fonksiyonu</h1>

`x` parametresine girilen argümanın boolean karşılığınız verir. Bu argüman [truth testing procedure](https://docs.python.org/3/library/stdtypes.html#truth "https://docs.python.org/3/library/stdtypes.html#truth")'e göre dönüştürülür. Eğer `x` parametresine `False` ya da `False` değerine karşılık gelen bir ifade (`""`, 0 vs.) girilmişse ya da bir değer girilmemişse (**omitted**, yani ihmal etmek) `False`; aksi taktirde `True` döndürür. `bool` class'ı, `int` class'ının subclass'ıdır. Bu yüzden daha fazla subclass'landırılamaz. Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#bool "https://docs.python.org/3/library/functions.html#bool").

<h2 id="1.1">Boolean Type Methodları</h2>

<h3 id="1.1.1"><code>as_integer_ratio()</code> Methodu</h3>

Birbirine bölündüğünde uygulandığı boolean değeri veren iki sayı döndürür. Bu iki sayı `tuple` içinde döndürülür. Örnek:
```py
print(True.as_integer_ratio()) # Output: (1, 1)
print(False.as_integer_ratio()) # Output: (0, 1)
```

<h3 id="1.1.2"><code>bit_length()</code> Methodu</h3>

`bit_length()` methodu, uygulandığı boolean değerin bit uzunluğunu döndürür. `bin()` fonksiyonu, kendisine argüman olarak verilen integer'ın bit karşılığını döndürür (Örnek: `print(bin(True))`: `0b1`). `len(bin()[2:])` kodu ile `bit_length()` methodunun yaptığı iş benzer gibi gözüksede kesinlikle birbiri yerine kullanılamaz. Örnek:
```py
print(True.bit_length()) # Output: 1 (`1` 1 birim uzunluğundadır)
print(False.bit_length()) # Output: 0 (`0` 0 birim uzunluğundadır)
print(len(bin(True)[2:])) # Output: 1 (`1` 1 birim uzunluğundadır)
print(len(bin(False)[2:])) # Output: 1 (`1` 1 birim uzunluğundadır)
print(len(bin(True))) # Output: 3 (`0b1` 1 birim uzunluğundadır)
print(len(bin(False))) # Output: 3 (`0b0` 1 birim uzunluğundadır)
```
`False` değerinin binary değeri `0b0`'dır. Bu değer yokluğu temsil ettiği için `bit_length` methodu doğru sonuç olan `0`'ı döndürür. Ama `len(bin()[2:])` kodu sadece `0b`'dan sonra bir şey olup olmadığına baktığı için istenilen sonucu vermez.

<h3 id="1.1.3"><code>to_bytes(length, byteorder, signed=False)</code> Methodu</h3>

Uygulandığı boolean değeri temsil eden byte array döndürür. Örnek:
```py
print(True.to_bytes(1, byteorder='big')) # Output: b'\x01'
print(False.to_bytes(1, byteorder='big')) # Output: b'\x00'
```
Boolean değerler length bytes kullanılarak temsil edilir. `to_bytes` methodunun uygulandığı boolean değer, en az `length` parametresinde argüman olarak girilen integer'ın belirttiği uzunluk kadar olmalı. `length` parametresinde argüman olarak girilen boolean değerden daha uzun olursa, fazlalıklar null (`b'\x00'`) ile doldurur; kısa olursa, `OverflowError: int too big to convert` hatası yükseltilir. Zaten boolean değerler maksimum 1, minimum 0 uzunluğunda olabilir. Örnek:
```py
print(True.to_bytes(1, byteorder='big')) # Output: b'\x01'
print(True.to_bytes(0, byteorder='big')) # OverflowError: int too big to convert
print(False.to_bytes(1, byteorder='big')) # Output: b'\x00'
print(False.to_bytes(0, byteorder='big')) # Output: b''
```
`False` değeri yokluğu ifade ettiği için `length` parametresinde argüman olarak `0` integer'ını girmemiz bir soruna neden olmaz ve boşluklar null `\x00` ile doldurulur.

`byteorder` parametresine girilen argüman ile `to_bytes` methodunun uygulandığı boolean değeri temsil etmek için kullanılan bayt sırasını (order) belirlenir. `byteorder` parametresine argüman olarak `"big"` girilirse, en önemli byte (the most significant byte) byte array'ın başında, `"little"` girilirse, en önemli byte (the most significant byte) byte array'ın sonunda olur. `big` ve `little` bir nevi birbirinin aynalanmış halidir. Örnek:
```py
print(True.to_bytes(10, byteorder='big')) # Output: b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
print(True.to_bytes(10, byteorder='little')) # Output: b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'
print(False.to_bytes(10, byteorder='big')) # Output: b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
print(False.to_bytes(10, byteorder='little')) # Output: b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
```
`signed` parametresine girilen argüman ile, `to_bytes` methodunun uygulandığı boolean değerin negatif mi pozitif mi olduğunu belirtirsiniz. Default değeri `False`'dır ve pozitif sayıları ifade eder. `True` ise negatif sayıları temsil eder. `signed` parametresine argüman olarak `True` verip, bu methodu pozitif bir sayıya uygularsınız `OverflowError` hatası alırsınız. Örnek:
```py
print(True.to_bytes(1, byteorder='big', signed=False)) # Output: b'\x01'
print(False.to_bytes(1, byteorder='big', signed=True)) # Output: b'\x00'
print(False.to_bytes(1, byteorder='big', signed=False)) # Output: b'\x00'
```
Boolean değerler sadece `True` ve `False`'dan ibarettir. Bu yüzden `signed` parametresi herhangi bir şeye etki etmez çünkü etki edecek karmaşıklıkta bir şey yok ortada. Sadece `True` ve `False` var.

<h3 id="1.1.4"><code>from_bytes(bytes, byteorder, signed=False)</code> Methodu</h3>

`bytes` parametresine argüman olarak girilen byte array'ı temsil eden boolean değeri döndürür. `from_bytes` methodu bir class method olduğu için direkt `bool` class'ına veya boolean type bir objeye uygulanabilir. Örnek:
```py
print(bool.from_bytes(b'\x01', byteorder='big')) # Output: True
print(bool.from_bytes(b'\x00', byteorder='big')) # Output: False
```
`bytes` parametresine girilen argüman [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object "https://docs.python.org/3/glossary.html#term-bytes-like-object") veya bir iterable producing bytes olabilir. Örnek:
```py
print(bool.from_bytes(b'\x04\x00', byteorder='big')) # Output: True
print(bool.from_bytes([255, 0, 0], byteorder='big')) # Output: True

print(bool.from_bytes(b'\x00', byteorder='big')) # Output: False
print(bool.from_bytes([0, 0, 0], byteorder='big')) # Output: False
```
`byteorder` parametresine girilen argüman ile, `bytes` parametresine argüman olarak girilen bytes objesinin bayt sırasını (order) belirler. `byteorder` parametresine argüman olarak `"big"` girilirse, en önemli byte (the most significant byte) byte array'ın başında, `"little"` girilirse, en önemli byte (the most significant byte) byte array'ın sonunda olur. `big` ve `little` bir nevi birbirinin aynalanmış halidir. Örnek:
```py
print(bool.from_bytes(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01', byteorder='big')) # Output: True
print(bool.from_bytes(b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00', byteorder='little')) # Output: True
```
`signed` parametresine girilen argüman ile, `to_bytes` methodunun uygulandığı integer'ın negatif mi pozitif mi olduğunu belirtirsiniz. Default değeri `False`'dır ve pozitif sayıları ifade eder. `True` ise negatif sayıları temsil eder ama boolean değerler için buna gerek yoktur çünkü sadece `True` ve `False` vardır. Örnek:
```py
print(bool.from_bytes(b'\x01', byteorder='big', signed=True)) # Output: True
print(bool.from_bytes(b'\x01', byteorder='big', signed=False)) # Output: True
print(bool.from_bytes(b'\x00', byteorder='big', signed=True)) # Output: False
print(bool.from_bytes(b'\x00', byteorder='big', signed=False)) # Output: False
```

<h3 id="1.1.5"><code>conjugate()</code> Methodu</h3>

Herhangi bir float'ın complex eşleniği (conjugate) olan `self`'i (yani uygulandığı boolean değeri) döndürür. Örnek:
```py
print(True.conjugate()) # Output: 1
print(False.conjugate()) # Output: 0
```

<h3 id="1.1.6"><code>denominator</code> Methodu</h3>

Uygulandığı boolean değerin en küçük terimli paydasını içeren property'dir (ne olduğu class'lar konusunda anlatılacak. şimdilik bir değeri tutan variable olarak düşünün). Boolean değerlerin paydası 1 olduğu için her zaman 1 döndürür. Örnek:
```py
print(True.denominator) # Output: 1
print(False.denominator) # Output: 1
```

<h3 id="1.1.7"><code>numerator</code> Methodu</h3>

Uygulandığı boolean değerin en küçük terimli payını içeren property'dir (ne olduğu class'lar konusunda anlatılacak. şimdilik bir değeri tutan variable olarak düşünün). Uygulandığı boolean değerin paydası kendisi olduğu için uygulandığı boolean değerin döndürür. Örnek:
```py
print(True.numerator) # Output: 1
print(False.numerator) # Output: 0
```

<h3 id="1.1.8"><code>imag()</code> Methodu</h3>

Uygulandığı boolean değerin `imag` (sanal) kısmını içeren bir property'dir (ne olduğu class'lar konusunda anlatılacak. şimdilik bir değeri tutan variable olarak düşünün). Örnek:
```py
print(complex(True)) # Output: (1+0j)
print(True.imag) # Output: 0

print(complex(False)) # Output: 0j
print(False.imag) # Output: 0
```

<h3 id="1.1.9"><code>real()</code> Methodu</h3>

Uygulandığı boolean değerin `real` (gerçek) kısmını içeren bir property'dir (ne olduğu class'lar konusunda anlatılacak. şimdilik bir değeri tutan variable olarak düşünün). Örnek:
```py
print(complex(True)) # Output: (1+0j)
print(True.real) # Output: 1

print(complex(False)) # Output: 0j
print(False.real) # Output: 0
```
