## `pow(sayı_1, sayı_2, sayı_3)`
Bir sayının kuvvetini almak için kullanılır. `sayı_2`, `sayı_1`'in üssüdür. `sayı_3` sonucun modulus'ünü `%` alır.
```py
print(pow(2,3,2)) # (2 ** 3) % 2
# Output: 0
```

## `abs(sayı)`
`abs()` fonksiyonunun ismi, mutlak anlamına gelen **absolute** kelimesinden gelmektedir. Bir sayının mutlak değerini almakta kullanılır. Mutlak değer, bir sayının sıfıra olan uzaklığıdır.
```py
print(abs(-15)) ; print(abs(15)) # Output: 15
print(abs(-15.18)) ; print(abs(15.18)) # Output: 15.18
print(abs(-15+3j)) ; print(abs(15+3j)) # Output: 15.297058540778355
```

## `round(sayı, basamak)`
Bir sayısal değeri belirli ölçülere göre yuvarlamamızı sağlar. `sayı` parametresine girilen sayının, virgülden sonra `basamak` parametresinde belirtilen basamak kadar kısmını referans alarak yuvarlama işlemi yapar. Örnek:
```py
print(round(3.6)) # Output: 4
print(round(3.5)) # Output: 4
print(round(3.4)) # Output: 3
  
print(round(22/7)) # Output: 3
  
print(round(3.142857142857143, 3)) # Output: 3.1428 -> 3.143
```

## `divmod(bölünen, bölen)`
`bölünen` parametresinde belirtilen sayının `bölen` parametresinde belirtilen sayıya bölünmesi sonucunda `bölüm` ve `kalan` kısımlarını bir `tuple` içinde döndürür. Örnek:
```py
divmod(10, 2)
# Output: (5, 0)
# Bölüm: 5
# Kalan: 0
```

## `max(item, *items, key, default)`
`item` parametresine girilen `list`, `tuple` ya da `set` objesinin içerdiği en büyük öğeyi ya da bir `dict` objesinin içerdiği en büyük `key`'i döndürür. Ayrıca `*items` yıldızlı parametresi sayesinde, birden fazla `item` girmemize izin verir. `*items` parametresine girilen itemlerin data type'ları farklı olursa sorun çıkabilir. Örnek:
```py
# 1. Kod
print(max([1,2],"sel",(1,2,3,4)))
# Output: TypeError: '>' not supported between instances of 'str' and 'list'
```
Ama aynı kodu şöyle yazarsak sorun çıkmaz:
```py
# 2. Kod
print(max([1,2],"sel",(1,2,3,4), key=len))
# Output: (1, 2, 3, 4)
```
`key` parametresi, kendisine verilen ölçüte göre `item` ya da `*items` parametresine girilen itemleri sıralar. Yukarıdaki kodlarda, `1. kod`'da sıkıntı çıkmasının sebebi: `1. kod`'da sıralama ölçütü belirtilmediği için `>` operatörüyle itemleri birbiriyle karşılaştırması ve farklı data type'lar arasında bu operatörle karşılaştırma işlemi yapılamamasıdır.  `2. kod`'da çıkmamasının sebebi: Sıralama ölçütünü `key` parametresinde belirttikten sonra bütün itemlerin `key`'de belirtilen sıralama ölçütünü desteklemesidir. Örnek:
```py
print(max([1,2],"sel", 12, key=len))
# Output: TypeError: object of type 'int' has no len()
```
Gördüğünüz gibi bu kodda `key` parametresinde `len` belirtilen sıralama ölçütünü `int` data type'ı desteklemediği için kod hata verdi.

## `min(item, *items, key, default)`
`item` parametresine girilen `list`, `tuple` ya da `set` objesinin içerdiği en küçük öğeyi ya da bir `dict` objesinin içerdiği en küçük `key`'i döndürür. Ayrıca `*items` yıldızlı parametresi sayesinde, birden fazla `item` girmemize izin verir. `*items` parametresine girilen itemlerin data type'ları farklı olursa sorun çıkabilir. Örnek:
```py
# 1. Kod
print(min([1,2],"sel",(1,2,3,4)))
# Output: TypeError: '>' not supported between instances of 'str' and 'list'
```
Ama aynı kodu şöyle yazarsak sorun çıkmaz:
```py
# 2. Kod
print(max([1,2],"sel",(1,2,3,4), key=len))
# Output: [1,2]
```
`key` parametresi, kendisine verilen ölçüte göre `item` ya da `*items` parametresine girilen itemleri sıralar. Yukarıdaki kodlarda, `1. kod`'da sıkıntı çıkmasının sebebi: `1. kod`'da sıralama ölçütü belirtilmediği için `<` operatörüyle itemleri birbiriyle karşılaştırması ve farklı data type'lar arasında bu operatörle karşılaştırma işlemi yapılamamasıdır.  `2. kod`'da çıkmamasının sebebi: Sıralama ölçütünü `key` parametresinde belirttikten sonra bütün itemlerin `key`'de belirtilen sıralama ölçütünü desteklemesidir. Örnek:
```py
print(min([1,2],"sel", 12, key=len))
# Output: TypeError: object of type 'int' has no len()
```
Gördüğünüz gibi bu kodda `key` parametresinde `len` belirtilen sıralama ölçütünü `int` data type'ı desteklemediği için kod hata verdi.

## `sum(item, sayı)`
`item` parametresine girilen `list`, `tuple` ya da `set` objesinin içerdiği öğelerin ya da bir `dict` objesinin içerdiği `key`'lerin toplamını döndürür.  Bu toplama işlemi matematiksel düzeydedir. Yani sadece numeric type'ları kabul eder. Örnek:
```py
print(sum([1, 2.6, 3+4j]))
# Output: (6.6+4j)
```
`sum()` fonksiyonunun `sayı` parametresine bir numeric type girilirse, bu fonksiyon, `item` parametresinin sonucu, `sayı` parametresiyle toplar ve sonucu döndürür. Örnek:
```py
print(sum([1, 2.6, 3+4j], 5))
# Output: (11.6+4j)
```
