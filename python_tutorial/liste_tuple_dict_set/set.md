# Set Oluşturmak
`set`, bildiğimiz matematikteki kümeler gibidir. Her öğeden bir tane bulundurur ve bu öğeler sıralı değildir. Dictionary'lerdeki gibi öğeleri sıralı olmadığı için index kavramı yoktur. Bir `set`'i `print()` fonksiyonu ile ekrana bastırmaya çalışırsanız, öğeleri sıralı olmadığı için programı her çalıştırdığınızda farklı sırada ekrana basılabilir. Örnek:
```py
set_exp = {"bir", "iki", "üç"}
print(set_exp)
# Output: {"bir", "iki", "üç"}
```
```py
set_exp = {"bir", "iki", "üç"}
print(set_exp)
# Output: {"bir", "üç", "iki"}
```
```py
set_exp = {"bir", "iki", "üç"}
print(set_exp)
# Output: { "iki","bir", "üç"}
```
**Not:** Aynı şey `set_exp = {1, 2, 3}` kümesinde geçerli değil. Çünkü `string` değerlerin hash'leri her program çalıştığında değişirken, numeric (`int` `float` `complex`) type'ların değişmez. Bu yüzden `set_exp = {"bir", "iki", "üç"}` kodunun outputu program her çalıştığında farklı sırada olabilirken, `set_exp = {1, 2, 3}` kodunun outputunun sırası değişmez.
```py
print(hash("bir"))
```

`set` data type'ına öğe olarak `list`, `set`, `dict` data type'ları eklenemez, `tuple`, `string` ve numeric type'lar gibi değiştirilemez (immutable) veri tipleri eklenebilir. Hatta `None` değerini bile ekleyebilirsiniz.

Diğer data type'ları `set`'e dönüştürebilirsiniz. Örnekler:
```py
k1 = set(["A", "B", "C"])
k2 = set(("A", "B", "C"))
k3 = set("ABC")
k4 = set({"A": "a", "B": "b", "C": "c"})
k5 = {"A", "B", "C"}
print(k1,k2,k3,k4,k5, sep="\n")
```
**Output:**
```
{'A', 'B', 'C'}
{'A', 'B', 'C'}
{'A', 'B', 'C'}
{'A', 'B', 'C'}
{'A', 'B', 'C'}
```
**Dikkat:** Bu sıra her seferinde farklı olabilir.

`set` data type'ının `list`, `tuple`, `dict` gibi spesifik bir işareti yoktur. Bu yüzden özellikle boş `set` tanımlarken `set()` kullanmalıyız. `{}` kullanırsanız boş `dict` tanımlamış olursunuz.

## Küme Üreteçleri (Set Comprehensions)
Kısa yoldan küme oluşturmak için kullanılabilir. Genellikle `list`, `tuple`, `dict` gibi diğer data type'ları `str`'e dönüştürme mantığına dayanır. Örnek:
```py
list_exp = [*range(1,11)]
set_Exp = {i for i in liste}
print(set_Exp , type(set_Exp ), sep="\n")
```
**Output:**
```
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
<class 'set'>
```

# Set Methodları

## `clear()` Methodu
`del` deyiminden farklı olarak, `set` objesini silmeden sadece içini temizler.
```py
set_exp = {"bir", "iki", "üç"}
set_exp.clear()
print(set_exp) # Output: set()
```

## `copy()` Methodu
Uygulandığı `set`'in farklı ID'ye sahip bir kopyasını oluşturur. Bu sayede yeni `set` ile eski `set` birbirinden bağımsız olur. `set` kopyalama işlemi `set1 = set2` şeklinde yapılırsa, `set1` ve `set2` objelerinin ID'leri aynı olacağı için listelerde olduğu gibi, birinde yapılan işlem diğerini de etkiler. Bu yüzden `copy()` methodu kullanılır.
```py
set_exp = {"bir", "iki", "üç"}
set_exp_2 = set_exp.copy()
print(set_exp_2) # Output: {"bir", "iki", "üç"}
```

## `add(item)` Methodu
Kümeye eleman eklemeye yarar. Öğenin listeye eklenebilmesi için `tuple`, `string` ve numeric type'lar gibi değiştirilemez (immutable) veri tipleri olması gerekiyor. Listede zaten varolan bir öğe eklenmek istenirse, kümede bir değişiklik olmaz çünkü kümelerde her elemandan bir tane olabilir.
```py
set_exp = {"bir", "iki", "üç"}
set_exp.add("dört")
print(set_exp) # Output: {"bir", "iki", "üç", "dört"}
```
## `difference(set)` Methodu
İki kümenin farkını almamızı sağlar.
```py
k1 = set([1, 2, 3, 5])
k2 = set([3, 4, 2, 10])

k1.difference(k2) # {1, 5} # k1 - k2
print(k1 - k2) # Output: {1, 5}

k2.difference(k1) # {4, 10} # k2 - k1
print(k2 - k1) # Output: {4, 10}

print(k1) # Output: {1, 2, 3, 5}
print(k2) # Output: {3, 4, 2, 10}
```
`k1.difference(k2)` anlamı, `k1`'de olup `k2`'de olmayan; `k2.difference(k1)` anlamı, `k2`'de olup `k1`'de olmayan anlamına gelmektedir. Bu methodlar kullanıldığında, ana set'leri etkilemez, yani değiştirmez.

## `difference_update(set)` Methodu
`difference()`'nin yaptığı işi yapar. Tek farkı, uygulandığı set'i değiştirir. Örnek:
```py
k1 = set([1, 2, 3, 5])
k2 = set([3, 4, 2, 10])

k1.difference_update(k2) # {1, 5} # k1 - k2

print(k1) # Output: {1, 5}
```

## `discard(item)` Methodu
`add()` methodunun yaptığı işin zıttını yapar. Yani `item` parametresine girilen elemanı kümeden siler. `item`'de belirtilen değer kümede yoksa, hiçbir şey olmaz.
```py
k1 = {1, 2, 3, 4, 5}
k1.discard(1)
k1.discard(6)
print(k1) # Output: {2, 3, 4, 5}
```

## `remove(item)` Methodu
`discard()` ile aynı şeyi yapar. Tek farkı, `item` parametresine set'de bulunmayan bir öğe girildiğinde `KeyError` hatası döndürür.
```py
k1 = {1, 2, 3, 4, 5}
k1.remove(1)
k1.remove(6) # KeyError: 6
print(k1) # Output: {2, 3, 4, 5}
```

## `intersection(set)` Methodu
İki kümenin kesişimini verir. `&` operatörü de kullanılabilir.
```py
k1 = {1, 2, 3, 5}
k2 = {3, 4, 2, 10}

print(k1.intersection(k2)) # Output: {2, 3}
print(k1 & k2) # Output: {2, 3}
```

## `intersection_update(set)` Methodu
`intersection()` yaptığı şeyi yapar. Tek farkı, uygulandığı set'i değiştirir. Örnek:
```py
k1 = {1, 2, 3, 5}
k2 = {3, 4, 2, 10}

print(k1.intersection_update(k2)) # Output: None
print(k1) # Output: {2, 3}
```

## `isdisjoint(set)` Methodu
İki kümenin kesişim kümesinin boş olup olmadığı sorgular. Boşsa `True`, değilse `False` döndürür.
```py
k1 = {1, 2, 3, 5}
k2 = {3, 4, 2, 10}

print(k1.isdisjoint(k2)) # Output: False
```

## `issubset(set)` Methodu
Uygulandığı kümenin, `set` parametresine belirtilen kümenin alt kümesi olup olmadığını sorgular.

**Alt Küme:** **A** kümesinin bütün elemanları **B** kümesinde varsa, **A** kümesi **B** kümesinin **alt kümesidir.**
```py
k1 = {1, 2, 3, 5}
k2 = {1, 7, 2, 9, 3, 5}
print(k1.issubset(k2)) # Output: True
```
Yukarıdaki kod `True` sonucunu verir çünkü `k1` kümesi `k2` kümesinin alt kümesidir.

## `issuperset(set)` Methodu
`issubset()` methodunun tam tersi işi yapar. Yani bir kümenin başka bir kümeyi kapsayıp kapsamadığını sorgular.
```py
k1 = {1, 2, 3, 5}
k2 = {1, 7, 2, 9, 3, 5}
print(k2.issuperset(k1)) # Output: True
```

## `union(set)` Methodu
İki kümenin birleşimini verir. `|` operatörü de kullanılabilir.
```py
k1 = {1, 2, 3, 5}
k2 = {3, 4, 2, 10}

print(k1.union(k2)) # Output: {1, 2, 3, 4, 5, 10}
print(k1 | k2) # Output: {1, 2, 3, 4, 5, 10}
```

## `update(item)` Methodu
Bir `list`, `tuple`, `set` ya da `dict` elemanlarını bir `set`'e eklemek için `for` döngüsü kullanılır.
```py
l1 = ["bir", "iki", "üç"]
s1 = set()
for i in l1:
	s1.add(i)
print(s1) # Output: ["bir", "iki", "üç"]
```
Bunun işlemi böyle yapmak yerine kısaca `update()` methodunu kullanabiliriz. Örnek:
```py
l1 = ["bir", "iki", "üç"]
s1 = set()
s1.update(l1)
print(s1)
```

## `symmetric_difference()` Methodu
İki kümenin birleşiminden kesişiminin farkını verir. Yani `k1.difference(k2) | k2.difference(k1)` işleminin sonucunu verir. Daha matematiksel açıklamak gerekirse: `(k1 - k2) | (k2 - k1)` işleminin sonucunu verir. Görsel açıklamak gerekirse de:
<img src="https://i.ibb.co/WsKyjcX/symmetric-56a8fa9f5f9b58b7d0f6ea14.jpg" alt="symmetric-56a8fa9f5f9b58b7d0f6ea14" border="0">
Mavi bölgeler `symmetric_difference()` işleminin sonucudur.
```py
k1 = {1, 2, 3, 5}
k2 = {3, 4, 2, 10}

print(k1.symmetric_difference(k2)) # Output: {1, 4, 5, 10}
print(k1.difference(k2) | k2.difference(k1)) # Output: {1, 4, 5, 10}
print((k1-k2)|(k2-k1)) # Output: {1, 4, 5, 10}
```

## `symmetric_difference_update()` Methodu
`symmetric_difference()` methodunun yaptığı işi yapar. Tek farkı, uygulandığı set'in değerini değiştirir.
```py
k1 = {1, 2, 3, 5}
k2 = {3, 4, 2, 10}

print(k1.symmetric_difference(k2)) # Output: None
print(k1) # Output: {2, 3}
```

## `pop()` Methodu
Kümenin rastgele bir elemanını siler ve sildiği elemanı döndürür.
```py
k1 = {1, 2, 3, 4, 5}
print(k1.pop()) # Output: 1
print(k1) # Output: {2, 3, 4, 5}
```

# Dondurulmuş Kümeler (Frozenset)
`tuple`, `list`'in değiştirilemez versiyonu olduğu gibi, `frozenset`'de `set`'in değiştirilemez versiyonudur. Yani `set`'de kullanılan, içeriği değiştirmeye yönelik methodlar `frozenset`'de kullanılamaz. `frozenset`'de kullanılabilen `set` methodları:
1) copy
2) difference
3) intersection
4) isdisjoint
5) issubset
6) issuperset
7) union
