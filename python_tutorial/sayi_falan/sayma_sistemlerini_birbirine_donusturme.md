# Sayı Sistemi Fonksiyonları

## `bin(integer)`
Bir integer sayının binary karşılığını döndürür. Output'u string data type'ında verir. Bu sayede index işlemleri yapabiliriz. `integer` parametresinde bir integer belirtilmemişse `TypeError` hatası döndürür.
```py
print(bin(10)) # Output: 0b1010
print(bin(10[2:])) # Output: 1010
```

## `oct(integer)`
Bir integer sayının octal karşılığını döndürür. Output'u string data type'ında verir. Bu sayede index işlemleri yapabiliriz. `integer` parametresinde bir integer belirtilmemişse `TypeError` hatası döndürür.
```py
print(oct(10)) # Output: 0o12
print(oct(10[2:])) # Output: 12
```

## `int(integer)`
bir integer sayının binary karşılığını döndürür. Output'u string data type'ında verir. Bu sayede index işlemleri yapabiliriz.
```py
print(int(0b1010)) # Output: 10
print(int(0o12)) # Output: 10
print(int(0xa)) # Output: 10
```

## `hex(integer)`
bir integer sayının binary karşılığını döndürür. Output'u string data type'ında verir. Bu sayede index işlemleri yapabiliriz.
```py
print(hex(10)) # Output: 0xa
print(hex(10[2:])) # Output: a
```

# Bişimlendirme Yolları
`string` data type'ının bir methodu olan `format` methodunun daha spesifik biçimlendirme yapabilmesi için kullandığı bazı harfler vardır. `bin()`, `oct()`, `int()` ve `hex()` fonksiyonlarını kullanmadan, `format` methodundaki ilgili harfleri kullanarak da dönüşüm işlemleri yapabiliriz. Bu herflere ulaşmak için [tıklayınız](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/.md/karakter_dizileri/karakter_dizileri.md#bi%C3%A7imlendirme-harfleri).
