# Tuple (`tuple(iterable)`) Tanımlamak
Tuple'lar listeler gibi değildir. Listeler değiştirilebilir (mutable) bir data type'dır ama Tuple'lar değiştirilemez (immutable) data type'dır. Bir Tuple'ı değiştirmek için onu yeniden tanımlamak gerekir. Bunu yaparsan demetin ID'si değişir ve eski tuple ile yeni tuple birbirinden bağımsız olur yani yeni tuple ile eski tuple hafızada iki farklı yerde saklanır. Bu da daha fazla memory işgaline yol açar. Tuple'ları, değiştirilmesini istemediğiniz verileri saklarken kullanabilirsiniz. Örneğin değiştirilmemesi gereken bir path'ı saklamak için biçilmiş kaptandır.

Tuple tanımlarken parantez `()` kullanılır.
```py
tuple_exp = (1,2,3,4)
tuple_exp_2 = tuple([1,2,3,4]) 
print(type(tuple_exp), type(tuple_exp_2))
# Output: <class 'tuple'> <class 'tuple'>
```
Burada dikkat edilmesi gereken şey, tuple tanımlayayım derken string tanımlamamanız. Bu durum özellikle tek öğeli tuple'larda görülür. Örnek:
```py
m1 = ("selam")
m2 = "selam"
m3 = ("selam",)
m4 = "selam",
print(type(m1), type(m2), type(m3), type(m4), sep="\n")
```
**Output:**
```
<class 'str'>
<class 'str'>
<class 'tuple'>
<class 'tuple'>
```
Gördüğünüz gibi, string tanımlamakla tuple tanımlamak arasındaki ince çizgiyi `,` belirliyor.

# Tuple Indeksleme
Listelerin elemanlarına ulaşabilmek için index'ler kullanılır.

Dördüncü indeksten başlar 10. indeksi dahil etmeden 10. indekse kadar alır.
```py
c = (1,2,3,4,5,6,7,8,9,10)
print(c[4:10])
  
# Output: (5, 6, 7, 8, 9)
```
Başlangıç değeri belirtilmemişse en baştan başlayarak alır.
```py
c = (1,2,3,4,5,6,7,8,9,10)
print(c[:10])
  
# Output: (1, 2, 3, 4, 5, 6, 7, 8, 9)
```
Bitiş değeri belirtilmemişse en sonuna kadar alır.
```py
c = (1,2,3,4,5,6,7,8,9,10)
print(c[4:])
  
# Output: (5, 6, 7, 8, 9, 10)
```
İki değer de belirtilmemişse tüm listeyi alır.
```py
c = (1,2,3,4,5,6,7,8,9,10)
print(c[:])
  
# Output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
```
Son liste elemanına kadar alır.
```py
c = (1,2,3,4,5,6,7,8,9,10)
print(c[:-1])
  
# Output: (1, 2, 3, 4, 5, 6, 7, 8, 9)
```
Baştan sona 2 değer atlaya atlaya listeyi alır.
```py
c = (1,2,3,4,5,6,7,8,9,10)
print(c[::2])
  
# Output: (1, 3, 5, 7, 9)
```
Dördüncü indeksten 12'nci indekse 3'er atlayarak listeyi alır.
```py
c = (1,2,3,4,5,6,7,8,9,10)
print(c[4:12:3])
  
# Output: (5, 8)
```
Baştan sona -1 atlayarak listeyi alır. (listeyi ters çevirme)
```py
c = (1,2,3,4,5,6,7,8,9,10)
print(c[::-1])
  
# Output: (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
```
Bir tuple içinde tanımlanmış `string`, `list`, `tuple`, `dictionary` gibi farklı data type'ların indexlerine ulaşabilirsiniz. Örnek:
```py
t1 = ("string",
	  1, 1.5, 15+5j,
	  ("tuple", "Tuple"),
	  ["liste", "Liste"],
	  {"set", "Set"},
	  {"Sözlük": "dictionary"})
print(t1[0][3]) # Output: i
print(t1[4][0]) # Output: tuple
print(t1[5][1]) # Output: Liste
print(t1[6][0]) # Output: TypeError: 'set' object is not subscriptable
print(t1[7]["Sözlük"]) # Output: dictionary
```
`set` data type'ının neden `TypeError` verdiğini [şuradan](set) öğrenebilirsiniz. Dictionary'nin indeksine nasıl ulaşmak ilgili daha ayrıntılı bilgi için [tıklayınız](asdasd).

# Demet Üreteçleri (Tuple Comprehensions)
Kısa yoldan tuple üretmek için kullanılır. Küçük çaplı programlarda tercih edilir. Örnek:
```py
# 1. Yöntem
c1 = list()
for i in range(10):
	c1 += [i]
c1 = tuple(c1)
print(c1) # Output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(type(c1)) # Output: <class 'tuple'>

# 2. Yöntem (Üreteç)
c2 = tuple(i for i in range(10))
print(c2) # Output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(type(c2)) # Output: <class 'tuple'>

# 3. Yöntem
c3 = tuple(range(10))
print(c3) # Output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(type(c3)) # Output: <class 'tuple'>
```
Başka bir örnek:
```py
# 1. Yöntem
liste1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
tümü1 = []
for i in liste1:
	for z in i:
		tümü1 += [z]
tümü1 = tuple(tümü1)
print(tümü1) # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
print(type(tümü1)) # Output: <class 'tuple'>

# 2. Yöntem (Üreteç)
liste2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
tümü2 = tuple(z for i in liste2 for z in i)
print(tümü2) # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
print(type(tümü2)) # Output: <class 'tuple'>
```

# Tuple Methodları

## `index(item)` Methodu
`item` parametresine tanımlanan değerin, tuple içinde kaçıncı index'te olduğunu söyler. İç içe tuple'larda çalışmaz ve `ValueError: tuple.index(x): x not in tuple` hatası verir.
```py
m1 = ("1","2",("3",),"4")
print(m1.index("2")) # Output: 1
print(m1.index("3")) # Output: `ValueError: tuple.index(x): x not in tuple`
```

## `count(item)` Methodu
`item` parametresine tanımlanan değerin, tuple içinde kaç kez geçtiğini söyler. İç içe tuple'larda , iç tuple'daki değerleri görmez ve eksik sonuç verebilir.
```py
tuple_exp = ("a","b",("a",),"c")
print(tuple_exp.count("a")) # Output: 1

```
