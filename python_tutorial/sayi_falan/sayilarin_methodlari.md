# Integer Number Methodları

## `bit_length()`
Uygulandığı integer sayının kaç bit yer kapladığını söyler. `bin()` fonksiyonu, herhangi bir integer sayıyı binary'e dönüştürüp döndürür. Örneğin `10` integer sayısının binary karşılığı `0b1010`'dır. Bu binary sayının ilk iki index'inden sonrası, bu integer sayının bir uzunluğu (bit length) oluyor. `len(bin())` komutunu `len(bin()[2:])` şeklinde kullanırsak istediğimiz sonucu elde ederiz. `len(bin()[2:])` komutuyla `bit_length()` methodunun yaptığı iş aynıdır. Örnek:
```py
print((10).bit_length()) # Output: 4
print(len(bin(10)[2:])) # Output: 4
``` 

# Floating Point Number Methodları

## `as_integer_ratio()`
Birbirine bölündüğünde uygulandığı `float` sayıyı veren en küçük iki tane integer sayı döndürür. Döndürdüğü output'u `tuple` içindedir.
```py
print((4.5).as_integer_ratio()) # Output: (9, 2)
print((4.1).as_integer_ratio()) # Output: (2308094809027379, 562949953421312)
print((5).as_integer_ratio()) # Output: (5, 1)
print((9.3).as_integer_ratio()) # Output: (2617717283409101, 281474976710656)
print((6.125).as_integer_ratio()) # Output: (49, 8)
print((9.337).as_integer_ratio()) # Output: (2628131857547395, 281474976710656)
```

## `is_integer()`
Bir `float` sayının, tam olmayan kısmında (noktanın sağındaki, ondalık olmayan) sıfır harici bir sayı olup olmadığını kontrol eder. Yani bu methodla, bir sayının integer'mı floating point'mi olduğunu sorgulayabilirsiniz.

# Complex Number Methodları
## `imag`
Bir complex number'ın **imag** kısmını döndürür.
```py
print((12+5j).imag) # Output: 5.0
```

## `real`
Bir complex number'ın **real** kısmını döndürür.
```py
print((12+5j).real) # Output: 12.0
```
