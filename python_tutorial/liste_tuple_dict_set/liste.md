# Liste İşlemleri ve Özellikleri

## Liste tanımlamak
Köşeli parantez `[]` listeyi temsil eder.
```py
# Boş Liste Tanımlamak
l1 = []
l2 = list()
```
Listelere her türlü data type'ı eleman olarak ekleyebilirsiniz. Örnek:
```py
l1 = ["string",
	  1, 1.5, 15+5j,
	  ("tuple", "Tuple"),
	  ["liste", "Liste"],
	  {"set", "Set"},
	  {"Sözlük": "dictionary"}]
```
Bir liste içine tekrardan `list`, `tuple`, `dictionary` ve `set` tanımayabilir ve bunların içine erişim sağlayabilirsiniz.  Tanımlama ile ilgili örnek:
```py
l1 = ["string",
	  1, 1.5, 15+5j,
	  ("tuple", "Tuple"),
	  ["liste", "Liste"],
	  {"set", "Set"},
	  {"Sözlük": "dictionary"}]
```

## Listelerde İşlemler
Listelerin eleman sayısına `len()` fonksiyonuyla ulaşılabilir.
```py
l1 = [1,2,3,4,5]
print(len(l1)) # Output: 5
```
Listelerde toplama ve çarpma işlemi yapabilirsin.
```py
d1 = [1,2,3]
d2 = [4,5,6]
l2 = d1 + d2
l3 = d1 * 2
print(l2, l3, sep="\n")
```
**Output:**
```
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 1, 2, 3]
```
Toplama işlemini kullanarak listeye eleman da ekleyebilirsiniz:
```py
d1 = [1,2,3]
d1 = d1 + [4]
print(d1) # Output: [1, 2, 3, 4]
```
Uygun olan herhangi bir değeri `list()` fonksiyonu ile liste türüne dönüştürebilirsiniz. Örneğin:
```py
print(list(range(0,10)))
print(list((0,1,2,3,4,5,6,7,8,9)))
print(list({0,1,2,3,4,5,6,7,8,9}))
print(list("0123456789"))
```
**Output:**
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```
Bir listenin son öğresine ulamak için:
```py
c = [0,1,2,3,4]
print(c[len(c)-1]) # Output: 4
```
Bir listenin herhangi bir öğesindeki değiştirmek için:
```py
c = [1,2,3,4]
c[1] = 0
print(c) # Output: [1, 0, 3, 4]
```
Bir listenin bütün öğelerini değiştirmek için:
```py
c = [1,2,3,4]
c[:len(c)] = 5,6,7,8
print(c) # Output: [5, 6, 7, 8]
```
Listeden bir öğe silmek için:
```py
c = [1,2,3,4]
del c[0]
print(c) # Output: [2, 3, 4]
```
Direkt listeyi silmek için:
```py
c = [1,2,3,4]
del c
print(c) # Output: NameError: name 'c' is not defined
```
Bir listeyi kopyalamak için basitçe o listeyi bir variableye eşitleyebilirsiniz:
```py
c = [1,2,3,4]
c_copy = c
print(c) # Output: [1, 2, 3, 4]
```
**Not:** Normal şartlarda bir variable'yi başka bir variable'ye eşitlerlerseniz, farklı ID'lere sahip olurlar. Ama aynı durum listeler için geçerli değildir. Bir listeyi başka bir listeye eşitlerseniz, aynı ID'lere sahip olurlar. Çünkü ikinci liste, ilk listenin pointer'ı olur. Bu yüzden birbiriyle eşitlenmiş iki listeyle çalışırken, birinide yaptığınız değişiklik diğerini de etkiler. Örnek:
```py
c = [1,2,3,4]
c_copy = c
print(id(c) == id(c_copy)) # Output: True
c.append(2)
print(c, c_copy, sep="\n")
```
**Output:**
```
True
[1, 2, 3, 4, 2]
[1, 2, 3, 4, 2]
```
Bunu önlemek için şöyle bir eşitleme yöntemi uygulayabilirsiniz:
```py
c = [1,2,3,4]
c_copy = c[:]
print(id(c) == id(c_copy)) # Output: True
c.append(2)
print(c, c_copy, sep="\n")
```
**Output:**
```
False
[1, 2, 3, 4, 2]
[1, 2, 3, 4]
```
Gördüğünüz gibi bu yöntemle listeler hem farklı id'lere sahip oldu, hem de farklı id'lere sahip oldukları için birinde yapılan değişiklik diğerini etkilemedi.

## Listeleri Indeksleme
Listelerin elemanlarına ulaşabilmek için index'ler kullanılır. Daha önce [string dilimleme](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/.md/karakter_dizileri/karakter_dizileri.md#string-dilimleme) kısmından aşına olabilirsiniz.


Dördüncü indeksten başlar 10. indeksi dahil etmeden 10. indekse kadar alır.
```py
c = [1,2,3,4,5,6,7,8,9,10]
print(c[4:10])

# Output: [5, 6, 7, 8, 9]
```
Başlangıç değeri belirtilmemişse en baştan başlayarak alır.
```py
c = [1,2,3,4,5,6,7,8,9,10]
print(c[:10])

# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
Bitiş değeri belirtilmemişse en sonuna kadar alır.
```py
c = [1,2,3,4,5,6,7,8,9,10]
print(c[4:])

# Output: [5, 6, 7, 8, 9, 10]
```
İki değer de belirtilmemişse tüm listeyi alır.
```py
c = [1,2,3,4,5,6,7,8,9,10]
print(c[:])

# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
Son liste elemanına kadar alır.
```py
c = [1,2,3,4,5,6,7,8,9,10]
print(c[:-1])

# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
Baştan sona 2 değer atlaya atlaya listeyi alır.
```py
c = [1,2,3,4,5,6,7,8,9,10]
print(c[::2])

# Output: [1, 3, 5, 7, 9]
```
Dördüncü indeksten 12'nci indekse 3'er atlayarak listeyi alır.
```py
c = [1,2,3,4,5,6,7,8,9,10]
print(c[4:12:3])

# Output: [5, 8]
```
Baştan sona -1 atlayarak listeyi alır. (listeyi ters çevirme)
```py
c = [1,2,3,4,5,6,7,8,9,10]
print(c[::-1])

# Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

Bir liste içinde tanımlanmış `string`, `list`, `tuple`, `dictionary` gibi farklı data type'ların indexlerine ulaşabilirsiniz. Örnek:
```py
l1 = ["string",
	  1, 1.5, 15+5j,
	  ("tuple", "Tuple"),
	  ["liste", "Liste"],
	  {"set", "Set"},
	  {"Sözlük": "dictionary"}]
print(l1[0][3])        # Output: i
print(l1[4][0])        # Output: tuple
print(l1[5][1])        # Output: Liste
print(l1[6][0])        # Output: TypeError: 'set' object is not subscriptable
print(l1[7]["Sözlük"]) # Output: dictionary
```
`set` data type'ının neden `TypeError` verdiğini [şuradan](set) öğrenebilirsiniz. Dictionary'nin indeksine nasıl ulaşmak ilgili daha ayrıntılı bilgi için [tıklayınız](asdasd).

# Liste Üreteçleri (List Comprehensions)
Kısa yoldan liste üretmek için kullanılır. Küçük çaplı programlarda tercih edilir. Örnek:
```py
# 1. Yöntem
c1 = list()
for i in range(10):
	c1 += [i]
print(c1)
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. Yöntem (Üreteç)
c2 = [i for i in range(10)]
print(c2)
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Yöntem
c3 = list(range(10))
print(c3)
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
Başka bir örnek:
```py
# 1. Yöntem
liste1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
tümü1 = []
for i in liste1:
	for z in i:
		tümü1 += [z]
print(tümü1)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# 2. Yöntem (Üreteç)
liste2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
tümü2 = [z for i in liste2 for z in i]

print(tümü2)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

# Liste Methodları

## `append(item)` Methodu
Bir listeye öğe eklemek için kullanılır. Öğeyi, listenin en sonuna (yani en sağına) ekler.
```py
liste = ["Elma", "Armut", "Kiraz"]
liste.append("Çilek")
print(liste) # Output: ['Elma', 'Armut', 'Kiraz', 'Çilek']
```
Eklenen type string ile sınırlı değildir. `list`, `tuple`, `set`, `dict` de eklenebilir.
```py
liste = []
liste.append(["Elma", "Armut"]) # list
liste.append(("Elma", "Armut")) # tuple
liste.append({"Elma", "Armut"}) # set
liste.append({"Elma": "Armut"}) # dict
print(liste)
# Output: [['Elma', 'Armut'], ('Elma', 'Armut'), {'Armut', 'Elma'}, {'Elma': 'Armut'}]
```

## `extend(item)` Methodu
Bir listenin elemanlarını başka bir listeye ekler. `append()`'den farkı budur. Örnek:
```py
liste = ["Elma", "Armut", "Kiraz"]
liste.append(["Çilek", "Şeftali"])
print(liste) # Output: ['Elma', 'Armut', 'Kiraz', ['Çilek', 'Şeftali']]

liste = ["Elma", "Armut", "Kiraz"]
liste.extend(["Çilek", "Şeftali"])
print(liste) # Output: ['Elma', 'Armut', 'Kiraz', 'Çilek', 'Şeftali']

```

## `insert(index, item)` Methodu
Bir öğeyi, listenin istenilen yerine yerleştirir. Yeni öğe, yerini aldığı öğenin bir sağa kaymasına neden olur.
```py
liste = ["Elma", "Armut", "Kiraz"]
liste.insert(1, "Çilek")
print(liste) # Output: ['Elma', 'Çilek', 'Armut', 'Kiraz']
```

## `remove(item)` Methodu
Listeden öğe silmek için kullanılır. `item` parametresine, silmek istediğiniz öğeyi yazmalısınız.
```py
liste = ["Elma", "Armut", "Kiraz"]
liste.remove("Elma")
print(liste) # Output: ['Armut', 'Kiraz']
```

## `reverse()` Methodu
Listeleri ters çevirmek için kullanılır.
```py
liste = ["Elma", "Armut", "Kiraz"]
liste.reverse()
print(liste) # Output: ['Kiraz', 'Armut', 'Elma']
```

## `pop(index)` Methodu
`remove()` gibi, bir listeden bir öğeyi silmek için kullanılır. `index` parametresine silmek istediğiniz öğeyi değil, o öğenin bulunduğu index'i yazmalısınız. `remove()`'dan farklı, sildiği öğeyi ekrana bastırmak için kullanılabilir.
```py
liste = ["Elma", "Armut", "Kiraz"]
print(liste.pop(0)) # Output: Elma
print(liste) # Output: ['Armut', 'Kiraz']
```

## `sort(key = ..., reverse = False)` Methodu
Listenin öğelerini UNICODE'a göre küçükten büyüğe sıralar. `key` parametresi, sıralama ölçütü için referansın girildiği parametredir. `reverse` parametresi, öğelerin küçükten büyüğe mi, büyükten küçüğe mi sıralanacağını belirlediğimiz parametredir ve default değeri `False`'dır.
```py
liste = ['Ahmet', 'Mehmet', 'Ceylan', 'Seyhan', 'Mahmut', 'Zeynep', 'Şule', 'İsmail']
liste.sort()
print(liste)
# Output: ['Ahmet', 'Ceylan', 'Mahmut', 'Mehmet', 'Seyhan', 'Zeynep', 'İsmail', 'Şule']

liste.sort(reverse = True)
print(liste)
# Output: ['Şule', 'İsmail', 'Zeynep', 'Seyhan', 'Mehmet', 'Mahmut', 'Ceylan', 'Ahmet']
```
Türkçe karakterlerde sıkıntı çıkabiliyor. Buna alternatif çözüm:
```py
???
```

## `sorted(list, key = ..., reverse = False)` Fonksiyonu
Liste methodu olan `sort()` ile aynı mantıkta çalışır. `sort()` methodu, uygulandığı listeyi değiştirirken, `sorted()` methodu uygulandığı listeyi değiştirmez.
```py
liste = ['Ahmet', 'Mehmet', 'Ceylan', 'Seyhan', 'Mahmut', 'Zeynep', 'Şule', 'İsmail']
print(sorted(liste))
# Output: ['Ahmet', 'Ceylan', 'Mahmut', 'Mehmet', 'Seyhan', 'Zeynep', 'İsmail', 'Şule']

print(sorted(liste, reverse = True))
# Output: ['Şule', 'İsmail', 'Zeynep', 'Seyhan', 'Mehmet', 'Mahmut', 'Ceylan', 'Ahmet']
```
```
Türkçe karakterlerde sıkıntı çıkabiliyor. Buna alternatif çözüm:
```py
???
```

## `index(item)` Methodu
`item` parametresine tanımlanan değerin, liste içinde kaçıncı index'te olduğunu söyler. İç içe listelerde çalışmaz ve `ValueError: 'item' is not in list` hatası verir.
```py
liste_index = ['Ahmet', 'Mehmet', 'Ceylan', 'Seyhan', 'Mahmut', 'Zeynep', 'Şule', 'İsmail']
print(liste_index.index("Ahmet")) # Output: 0
```

## `count(item)` Methodu
`item` parametresine tanımlanan değerin, liste içinde kaç kez geçtiğini söyler. İç içe listelerde, iç listedeki değerleri görmez ve eksik sonuç verebilir.
```py
liste = ["a","b",["a"],"c"]
print(liste.count("a")) # Output: 1
```

## `copy()` Methodu
Uygulandığı listenin farklı ID'ye sahip bir kopyasını oluşturur. Bu sayede yeni liste ile eski liste birbirinden bağımsız olur. Liste kopyalama işlemi `liste1 = liste2` şeklinde yapılırsa, `liste1` ve `liste2` objelerinin ID'leri aynı olacağı için listelerde olduğu gibi, birinde yapılan işlem diğerini de etkiler. Bu yüzden `copy()` methodu kullanılır.
```py
liste1 = ['Ahmet', 'Mehmet', 'Ceylan']
liste2 = liste1.copy()
print(id(liste1), id(liste2), sep="\n")
# Output: 
```

## `clear()` Methodu
Uygulandığı listenin içeriğini siler. Listenin içini boşaltmak için kullanılabilir.
```py
liste = ['Ahmet', 'Mehmet', 'Ceylan']
liste.clear()
print(liste) # Output: []
```
