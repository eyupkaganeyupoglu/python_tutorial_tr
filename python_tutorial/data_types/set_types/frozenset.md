# Dondurulmuş Kümeler (Frozenset)
`tuple`, `list`'in değiştirilemez versiyonu olduğu gibi, `frozenset`'de `frozenset`'in değiştirilemez versiyonudur. Yani `frozenset`'de kullanılan, içeriği değiştirmeye yönelik methodlar `frozenset`'de kullanılamaz. `frozenset`'de kullanılabilen `frozenset` methodları:

## `copy()` Methodu
Uygulandığı `frozenset`'in farklı ID'ye sahip bir kopyasını oluşturur. Bu sayede yeni `frozenset` ile eski `frozenset` birbirinden bağımsız olur. `frozenset` kopyalama işlemi `frozenset1 = frozenset2` şeklinde yapılırsa, `frozenset1` ve `frozenset2` objelerinin ID'leri aynı olacağı için listelerde olduğu gibi, birinde yapılan işlem diğerini de etkiler. Bu yüzden `copy()` methodu kullanılır.
```py
frozenset_exp = frozenset(["bir", "iki", "üç"])
frozenset_exp_2 = frozenset_exp.copy()
print(frozenset_exp_2) # Output: {"bir", "iki", "üç"}
```

## `difference(frozenset)` Methodu
İki frozenset'in farkını almamızı sağlar.
```py
k1 = frozenset([1, 2, 3, 5])
k2 = frozenset([3, 4, 2, 10])

k1.difference(k2) # {1, 5} # k1 - k2
print(k1 - k2) # Output: {1, 5}

k2.difference(k1) # {4, 10} # k2 - k1
print(k2 - k1) # Output: {4, 10}

print(k1) # Output: {1, 2, 3, 5}
print(k2) # Output: {3, 4, 2, 10}
```
`k1.difference(k2)` anlamı, `k1`'de olup `k2`'de olmayan; `k2.difference(k1)` anlamı, `k2`'de olup `k1`'de olmayan anlamına gelmektedir. Bu methodlar kullanıldığında, ana frozenset'leri etkilemez, yani değiştirmez.

## `intersection(frozenset)` Methodu
İki frozenset'in kesişimini verir. `&` operatörü de kullanılabilir.
```py
k1 = frozenset([1, 2, 3, 5])
k2 = frozenset([3, 4, 2, 10])

print(k1.intersection(k2)) # Output: {2, 3}
print(k1 & k2) # Output: {2, 3}
```

## `union(frozenset)` Methodu
İki frozenset'in birleşimini verir. `|` operatörü de kullanılabilir.
```py
k1 = frozenset([1, 2, 3, 5])
k2 = frozenset([3, 4, 2, 10])

print(k1.union(k2)) # Output: {1, 2, 3, 4, 5, 10}
print(k1 | k2) # Output: {1, 2, 3, 4, 5, 10}
```

## `isdisjoint(frozenset)` Methodu
İki frozenset'in kesişiminin boş olup olmadığı sorgular. Boşsa `True`, değilse `False` döndürür.
```py
k1 = frozenset([1, 2, 3, 5])
k2 = frozenset([3, 4, 2, 10])

print(k1.isdisjoint(k2)) # Output: False
```

## `issubset(frozenset)` Methodu
Uygulandığı frozenset'in, `frozenset` parametresine belirtilen frozenset'in alt kümesi olup olmadığını sorgular.

**Alt Küme:** **A** kümesinin bütün elemanları **B** kümesinde varsa, **A** kümesi **B** kümesinin **alt kümesidir.**
```py
k1 = frozenset([1, 2, 3, 5])
k2 = frozenset([1, 7, 2, 9, 3, 5])
print(k1.issubset(k2)) # Output: True
```
Yukarıdaki kod `True` sonucunu verir çünkü `k1` kümesi `k2` kümesinin alt kümesidir.

## `issuperset(frozenset)` Methodu
`issubset()` methodunun tam tersi işi yapar. Yani bir kümenin başka bir kümeyi kapsayıp kapsamadığını sorgular.

**Kapsama:** **A** kümesinin bütün elemanları **B** kümesinde varsa, **B** kümesi **A** kümesini **kapsar.**
```py
k1 = frozenset([1, 2, 3, 5])
k2 = frozenset([1, 7, 2, 9, 3, 5])
print(k2.issuperset(k1)) # Output: True
```

## `symmetric_difference()` Methodu
İki frozenset'in birleşiminden kesişiminin farkını verir. Yani `k1.difference(k2) | k2.difference(k1)` işleminin sonucunu verir. Daha matematiksel açıklamak gerekirse: `(k1 - k2) | (k2 - k1)` işleminin sonucunu verir. Görsel açıklamak gerekirse de:
<img src="https://i.ibb.co/WsKyjcX/symmetric-56a8fa9f5f9b58b7d0f6ea14.jpg" alt="symmetric-56a8fa9f5f9b58b7d0f6ea14" border="0">

Mavi bölgeler `symmetric_difference()` işleminin sonucudur.
```py
k1 = frozenset([1, 2, 3, 5])
k2 = frozenset([3, 4, 2, 10])

print(k1.symmetric_difference(k2)) # Output: {1, 4, 5, 10}
print(k1.difference(k2) | k2.difference(k1)) # Output: {1, 4, 5, 10}
print((k1-k2)|(k2-k1)) # Output: {1, 4, 5, 10}
```