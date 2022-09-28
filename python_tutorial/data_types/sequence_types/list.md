# İçindekiler

- [Listeler (Lists)](#1)
    - [Listeler'de İşlemler](#1.1)
    - [Liste Üreteçleri (List Comprehensions)](#1.2)
    - [Liste Methodları](#1.3)
        - [`append(object)` Methodu](#1.3.1)
        - [`extend(iterable)` Methodu](#1.3.2)
        - [`insert(index, object)` Methodu](#1.3.3)
        - [`remove(value)` Methodu](#1.3.4)
        - [`reverse()` Methodu](#1.3.5)
        - [`pop(index)` Methodu](#1.3.6)
        - [`sort(key=None, reverse=False)` Methodu](#1.3.7)
        - [`sorted(iterable, key=None, reverse=False)` Fonksiyonu](#1.3.8)
        - [`index(value, start, stop)` Methodu](#1.3.9)
        - [`count(value)` Methodu](#1.3.10)
        - [`copy()` Methodu](#1.3.11)
        - [`clear()` Methodu](#1.3.12)

<h1 id="1">Listeler (Lists)</h1>

Listeler, içinde objeleri depolayabilen, sıralı, değiştirilebilir data type'lardır. `list(iterable)` build'in fonksiyonu ile liste oluşturabilirsiniz veya uygun objeleri liste'ye dönüştürebilirsiniz. Listeler köşeli parantez (`[]`) ile ifade edilir. Örnek:
```py
# Boş Liste Tanımlamak
l1 = []
l2 = list()
l3 = ["string",
	  1, 1.5, 15+5j,
	  ("tuple", "Tuple"),
	  ["liste", "Liste"],
	  {"set", "Set"},
	  {"Sözlük": "dictionary"}]
      
print(l1,l2,l3,sep="\n")
```
**Output:**
```
[]
[]
['string', 1, 1.5, (15+5j), ('tuple', 'Tuple'), ['liste', 'Liste'], {'set', 'Set'}, {'Sözlük': 'dictionary'}]
```

<h2 id="1.1">Listeler'de İşlemler</h2>

Bir listeyi dilimlerken `list_exp[Başlama index'i : bitiş index'i : atlama değeri]` syntax'ı kullanılır. Örnekler:
```py
a = [0,1,2,3,4,5,6,7,8,9]

# 4. index'ten başlar, (9. index'i dahil etmeden) 9. index'e kadar list'i yazdırır.
print(a[4:9]) # Output: [4, 5, 6, 7, 8]

# Başlangıç index'i belirtilmediği için en baştan (0. index'ten) başlar, (9. index'i dahil etmeden) 9. index'e kadar list'i yazdırır.
print(a[:9]) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Bitiş index'i belirtilmediği için 4. indexten başlar, en son index'e kadar list'i yazdırır.
print(a[4:]) # Output: [4, 5, 6, 7, 8, 9]

# Başlangıç ve bitiş intex'i belirtilmediği için tüm list'i yazdırır.
print(a[:]) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Başlangıç index'i belirtilmediği için en baştan (0. index'ten) başlar, (-1. index'i dahil etmeden) -1. index'e kadar (sonran bir önceki index) list'i yazdırır.
print(a[:-1])# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Baştan sona index atlamadan list'i yazdırır.
print(a[::1]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Baştan sona 1 index atlaya atlaya list'i yazdırır.
print(a[::2]) # Output: [0, 2, 4, 6, 8]

# 4. index'ten başlar, (9. index'i dahil etmeden) 9. index'e kadar 2 index atlaya atlaya list'i yazdırır.
print(a[0:9:3]) # Output: [0, 3, 6]

# Sondan başa index atlamadan list'i yazdırır. (list'i ters çevirme)
print(a[::-1]) # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

Listelerin öğe sayısına `len()` fonksiyonuyla ulaşılabilir. Örnek:
```py
l1 = [1,2,3,4,5]
print(len(l1)) # Output: 5
```

Listelerde aritmetik (sayısal) işlemler yapılabilir. Örnek:
```py
print([1,2,3] + [4,5,6]) # Output: [1, 2, 3, 4, 5, 6]
print([1,2,3] * 2) # Output: [1, 2, 3, 1, 2, 3]
```
Bir listeye öğe eklemek için addition (toplama `+`) operator'ını kullanarak öğe ekleyebilirsiniz. Bu durum yeniden tanımlama (redefinition) işlemi olsa bile list, değiştirilebilir (mutable) bir type olduğu için ID'si değişmez, yani farklı bir obje olmaz. Örnek:
```py
l1 = [1,2]
id_1 = id(l1)
print(l1) # Output:[1, 2]
l1 += [3,4]
id_2 = id(l1)
print(l1) # Output:[1, 2, 3, 4]
print((id_1 == id_2)) # Output: True
```

Diğer iterable objeleri `list()` fonksiyonu ile list type bir objeye dönüştürebilirsiniz. Örnek:
```py
print(list(range(0,4))) # Output: [0, 1, 2, 3]
print(list((0,1,2,3))) # Output: [0, 1, 2, 3]
print(list({0,1,2,3})) # Output: [0, 1, 2, 3]
print(list("0123")) # Output: ['0', '1', '2', '3']
```

Öğe sayısını bilmediğiniz listelerin son öğesine ulaşmak için iki yöntem:
```py
l1 = [0,1,2,3,4]
print(l1[len(l1)-1]) # Output: 4
print(l1[-1]) # Output: 4
```

Bir listenin herhangi bir index'indeki öğesini başka bir şeyler değiştirmek:
```py
l1 = [1,2,3,4]
print(l1) # Output: [1, 2, 3, 4]
l1[1] = 0
print(l1) # Output: [1, 0, 3, 4]
```

Bir listenin bütün öğelerini değiştirmek:
```py
l1 = [1,2,3,4]
print(l1) # Output: [1, 2, 3, 4]
l1[:] = 5,6,7,8
print(l1) # Output: [5, 6, 7, 8]
```

Listede belli bir index'deki öğeyi silmek:
```py
l1 = [1,2,3,4]
del l1[0]
print(l1) # Output: [2, 3, 4]
```

Listede bütün öğeleri silmek:
```py
l1 = [1,2,3,4]
del l1[:]
print(l1) # Output: []
```

Liste objesini tamamen silmek:
```py
l1 = [1,2,3,4]
del l1
print(l1) # NameError: name 'l1' is not defined
```

Bir listeyi kopyalamak ve sonuçları:
```py
l1 = [1,2,3,4]
l2 = l1
print(l1) # Output: [1, 2, 3, 4]
print(l2) # Output: [1, 2, 3, 4]
print(id(l1) == id(l2)) # Output: True

l1[0] = 5
print(l1) # Output: [5, 2, 3, 4]
print(l2) # Output: [5, 2, 3, 4]
```
List, değiştirilebilir (mutable) bir data type olduğu için assignment operator (`=`) kullanılarak bir liste objesini yukarıdaki gibi farklı bir variable'a atarsanız, son durumda oluşan objeler aynı liste objesine atıfta bulunacağı (refers to) için birinde yapılan değişiklikler diğerini de etkiler. Bu durum değiştirilemez (immutable) data type'lar için geçerli değildir çünkü değiştirilemez (immutable) data type'ları değiştirmek için yeniden tanımlama (redefinition) işlemi yapıyoruz ve sonuçta birbirinden farklı iki obje elde ediyoruz. Yeniden tanımlama (redefinition) işlemi sonucunda da mevcut obje farklı bir objeye dönüştüğü için birbirine atıfta bulunma durumu ortadan kalkacak ve bu objeler birbirini etkilemeyecek.

Bir listeyi yukarıda anlattığım sorunu yaşamadan kopyalamak istiyorsanız aşağıdaki yöntemi kullanabilirsiniz:
```py
l1 = [1,2,3,4]
l2 = l1[:]
print(id(l1) == id(l2)) # Output: False
print(l1) # Output: [1, 2, 3, 4]
print(l2) # Output: [1, 2, 3, 4]
```
Gördüğünüz gibi bu yöntemle içerikleri aynı ama birbirinden bağımsız liste objeleri elde ettik.

Bir liste içine tanımlanmış diğer index'lenebilir iterable objelerin index'lerine de erişebiliriz. Örnek:
```py
l1 = ["string",
	  ("tuple", "Tuple"),
	  ["liste", "Liste"],
	  {"Sözlük": "dictionary"}]
print(l1[0][3])        # Output: i
print(l1[1][0])        # Output: tuple
print(l1[2][1])        # Output: Liste
print(l1[3]["Sözlük"]) # Output: dictionary
```
`obje[index][index]` yapısını çalışma mantığı:
- Python `a[b][c]` yapısını soldan sağa okumaya başladığı için önce `a[b]` kısmını okur ve `a` objesinin `b` index'ine gider ve böylece `a[b]` kodu, `a` objesinin `b` index'indeki objeye atıfta bulunmuş olur. Bu objeye `x` diyelim.
- Bu işlemden sonra `a[b][c]` kodu Python'un gözünde `x[c]` koduna dönüşür. Python `x[c]` kodu için de aynı işlemleri yapar.
- Python'u LEGO gibi düşünün. Kodları bütün olarak değil, parça parça yorumlayın. Böylelikle Python'un çalışma mantığını anlarsınız. Örneğin aşağıdaki iki kod tamamen aynı işi yapmaktadır:
    ```py
    l1 = [[[[1,2], [3,4]], [[5,6], [7,8]]], [[[9,10], [11,12]], [[13,14], [15,16]]]]

    a1 = l1[0]
    a2 = a1[0]
    a3 = a2[0]
    a4 = a3[0]
    print(a4) # Output: 1

    print(l1[0][0][0][0]) # Output: 1
    ```

<h2 id="1.2">Liste Üreteçleri (List Comprehensions)</h2>

**Comprehension**, tek satırda oluşturduğumuz **Generator** (daha sonra anlatılacak) yapısına verilen isimdir. `(expression for item in iterable)` syntax'ına sahiptir (parantezler dahil). Bu generator yapısı (**Generator Comprehension**) bir generator objesi oluşturmakta kullanılır. Daha sonra bu generator objesini list type'a dönüştürerek List Comprehension oluşturabiliriz. Örnek:
```py
list_exp = [i for i in range(1,4)]
print(list_exp) # Output: [1, 2, 3]
```
Bu konu daha sonra comprehension başlığı altında daha detaylı anlatılacak.

<h2 id="1.3">Liste Methodları</h2>

<h3 id="1.3.1"><code>append(object)</code> Methodu</h3>

`object` parametresinde argüman olarak girdiğiniz objeyi, uygulandığı listeye eklemek için kullanılır. Objeyi listenin en sonuna (yani en sağına) ekler. Örnek:
```py
liste = []
liste.append("Elma, Armut")     # string
liste.append(1)                 # integer
liste.append(1.1)               # float
liste.append(1+1j)              # complex
liste.append(["Elma", "Armut"]) # list
liste.append(("Elma", "Armut")) # tuple
liste.append({"Elma", "Armut"}) # set
liste.append({"Elma": "Armut"}) # dict
print(liste) # Output: ['Elma, Armut', 1, 1.1, (1+1j), ['Elma', 'Armut'], ('Elma', 'Armut'), {'Armut', 'Elma'}, {'Elma': 'Armut'}]
```

<h3 id="1.3.2"><code>extend(iterable)</code> Methodu</h3>

`iterable` parametresinde argüman olarak girdiğiniz iterable objenin öğelerini, uygulandığı listeye eklemek için kullanılır. `append` methodundan bu yönüyle farklıdır. Öğeyi listenin en sonuna (yani en sağına) ekler. Örnek:
```py
liste = ["Elma", "Armut", "Kiraz"]
liste.append(["Çilek", "Şeftali"])
print(liste) # Output: ['Elma', 'Armut', 'Kiraz', ['Çilek', 'Şeftali']]

liste = ["Elma", "Armut", "Kiraz"]
liste.extend(["Çilek", "Şeftali"])
print(liste) # Output: ['Elma', 'Armut', 'Kiraz', 'Çilek', 'Şeftali']
```

<h3 id="1.3.3"><code>insert(index, object)</code> Methodu</h3>

`object` parametresinde argüman olarak girdiğiniz objeyi, uygulandığı listede, `index` parametresinde belirtilen index'e yerleştirir. Yeni öğe, yerini aldığı öğenin ve sonraki öğelerin bir sağa kaymasına neden olur. Örnek:
```py
liste = ["Elma", "Armut", "Kiraz"]
print(liste) # Output: ['Elma', 'Armut', 'Kiraz']
liste.insert(1, "Çilek")
print(liste) # Output: ['Elma', 'Çilek', 'Armut', 'Kiraz']
```
Burada dikkat edilmesi gereken şey `liste = ["Elma", "Armut", "Kiraz"].insert(1, "Çilek")` tuzağıdır. Fonksiyonların yaptıkları şey ile döndürdükleri her zaman birbirini tutmuyor. Örneğin `insert` methodu uygulandığı listenin herhangi bir index'ine bir öğe eklememize yarar ama döndürdüğü şey `None`'dur. Yani `liste = ["Elma", "Armut", "Kiraz"].insert(1, "Çilek")` yaparsanız `Liste == None` olur. Lego oynar gibi python kodlamak bazen böyle istenmeyen sonuçlara sebep oluyor.

<h3 id="1.3.4"><code>remove(value)</code> Methodu</h3>

Uygulandığı listeden `value` parametresinde belirtilen değeri siler. Örnek:
```py
liste = ["Elma", "Armut", "Kiraz"]
liste.remove("Elma")
print(liste) # Output: ['Armut', 'Kiraz']

l1 = ['a', 'b', ['c', 'd']]
l1.remove(['c', 'd'])
print(l1) # Output: ['a', 'b']
```

<h3 id="1.3.5"><code>reverse()</code> Methodu</h3>

Uygulandığı listeyi ters çevirmek için kullanılır.
```py
liste = ["Elma", "Armut", "Kiraz"]
liste.reverse()
print(liste) # Output: ['Kiraz', 'Armut', 'Elma']
```

<h3 id="1.3.6"><code>pop(index)</code> Methodu</h3>

`index` parametresinde belirtilen index'deki öğreyi önce döndürür sonra uygulandığı listeden siler. Örnek:
```py
liste = ["Elma", "Armut", "Kiraz"]
print(liste.pop(0)) # Output: Elma
print(liste) # Output: ['Armut', 'Kiraz']
```

<h3 id="1.3.7"><code>sort(key=None, reverse=False)</code> Methodu</h3>

Listenin öğelerini UNICODE'a göre küçükten büyüğe sıralar. `key` parametresi, sıralama ölçütü için referansın girildiği parametredir. `reverse` parametresi, öğelerin küçükten büyüğe mi, büyükten küçüğe mi sıralanacağını belirlediğimiz parametredir ve default değeri `False`'dır.
```py
liste = ['Ahmet', 'Mehmet', 'Ceylan', 'Seyhan', 'Mahmut', 'Zeynep', 'Şule', 'İsmail']
liste.sort()
print(liste) # Output: ['Ahmet', 'Ceylan', 'Mahmut', 'Mehmet', 'Seyhan', 'Zeynep', 'İsmail', 'Şule']

liste = ['Ahmet', 'Mehmet', 'Ceylan', 'Seyhan', 'Mahmut', 'Zeynep', 'Şule', 'İsmail']
liste.sort(reverse = True)
print(liste) # Output: ['Şule', 'İsmail', 'Zeynep', 'Seyhan', 'Mehmet', 'Mahmut', 'Ceylan', 'Ahmet']
```
Türkçe karakterlerde sıkıntı çıkabiliyor. Buna alternatif çözüm:
```py
import locale
locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254') 

liste = ['Ahmet', 'Mehmet', 'Ceylan', 'Seyhan', 'Mahmut', 'Zeynep', 'Şule', 'İsmail']
liste.sort(key=locale.strxfrm)
print(liste) # Output: ['Ahmet', 'Ceylan', 'İsmail', 'Mahmut', 'Mehmet', 'Seyhan', 'Şule', 'Zeynep']
```

<h3 id="1.3.8"><code>sorted(iterable, key=None, reverse=False)</code> Fonksiyonu</h3>

`iterable` parametresine argüman olarak girilen iterable objeyi `key` parametresinde belirtilen ölçüte göre sıralar. `reverse` parametresine bağlı olarak da bu sıralamanın normal mi yoksa ters mi olacağına karar verebilirsiniz. Bu fonksiyon, output'u `list` type'dır. Örnek:
```py
liste = ['Ahmet', 'Mehmet', 'Ceylan', 'Seyhan', 'Mahmut', 'Zeynep', 'Şule', 'İsmail']
print(sorted(liste)) # Output: ['Ahmet', 'Ceylan', 'Mahmut', 'Mehmet', 'Seyhan', 'Zeynep', 'İsmail', 'Şule']
print(sorted(liste, reverse = True)) # Output: ['Şule', 'İsmail', 'Zeynep', 'Seyhan', 'Mehmet', 'Mahmut', 'Ceylan', 'Ahmet']
```
Türkçe karakterlerde sıkıntı çıkabiliyor. Buna alternatif çözüm:
```py
import locale
locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254') 

liste = ['Ahmet', 'Mehmet', 'Ceylan', 'Seyhan', 'Mahmut', 'Zeynep', 'Şule', 'İsmail']
print(sorted(liste, key=locale.strxfrm)) # Output: ['Ahmet', 'Ceylan', 'İsmail', 'Mahmut', 'Mehmet', 'Seyhan', 'Şule', 'Zeynep']
```

<h3 id="1.3.9"><code>index(value, start, stop)</code> Methodu</h3>

`value` parametresine argüman olarak girdiğiniz value'nun, uygulandığı liste içinde ilk kaçıncı index'de bulunduğunu söyler. `start` ve `stop` parametrelerine gireceğiniz integer argümanlarla, `index` methodunun hangi index'ler arasında arama yaparcağını belirleyebilirsiniz. Örnek:
```py
l1 = ["a", ["b", "c"], "a"]
print(l1) # Output: ['a', ['b', 'c'], 'a']
print(l1.index("a")) # Output: 0
print(l1.index("a", 2)) # Output: 2
print(l1.index(["b", "c"])) # Output: 1
```

<h3 id="1.3.10"><code>count(value)</code> Methodu</h3>

`value` parametresine argüman olarak girdiğiniz value'nun, uygulandığı liste içinde kaç kere geçtiğini söyler. Nested listelerde eksik sonuç verebilir çünkü nested listeyi görmez. Örnek:
```py
liste = ["a","b",["a"],"c"]
print(liste.count("a")) # Output: 1
```

<h3 id="1.3.11"><code>copy()</code> Methodu</h3>

Uygulandığı listenin bir kopyasını oluşturur. `liste1 = liste2` gibi assignment operator kullanarak liste kopyalama yönteminden farkı, yeni liste ile eski liste birbirinden bağımsız, farklı (farklı ID'lere sahip) objeler olmasıdır. Böylece birinde yapılan değişikli diğerini etkilemez. Örnek:
```py
liste = [1,2,3,4,5]
liste_copy1 = liste
print(liste) # Output: [1, 2, 3, 4, 5]
print(liste_copy1) # Output: [1, 2, 3, 4, 5]

liste_copy1[0] = "Bir"
print(liste) # Output: ['Bir', 2, 3, 4, 5]
print(liste_copy1) # Output: ['Bir', 2, 3, 4, 5]

liste_copy2 = liste.copy()
print(id(liste) == id(liste_copy2)) # Output: False
print(liste) # Output: ['Bir', 2, 3, 4, 5]
print(liste_copy2) # Output: ['Bir', 2, 3, 4, 5]

liste_copy2[1] = "İki"
print(liste) # Output: ['Bir', 2, 3, 4, 5]
print(liste_copy2) # Output: ['Bir', 'İki', 3, 4, 5]
```

<h3 id="1.3.12"><code>clear()</code> Methodu</h3>

Uygulandığı listenin içeriğini siler. `del` statement ile liste objesini tamamen silmeden sadece listenin içini boşaltmak isteyenler için uygun bir tercihtir.
```py
liste = ['Ahmet', 'Mehmet', 'Ceylan']
liste.clear()
print(liste) # Output: []
```