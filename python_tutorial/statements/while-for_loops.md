# `while` Loop
`while` kelimesi türkçede *"... Olduğu sürece"* anlamına gelmektedir. `while loops`, belirli bir koşul sağlandığı sürece tekrar eden döngülerdir. Syntax'ı:
```py
while (Koşul):
	# Kodlar
```
Şeklindedir. Buradaki `(Koşul)` kısmı `True` sonucunu verdiği sürece loop devam eder ama `(Koşul)` `False` olursa loop durur. Örnek:
```py
# Sayı Sayma
max_number = int(input("Kaça kadar sayalım?: "))
min_number = 1
while (min_number != max_number):
	print(min_number, end=", ")
	min_number += 1
print(max_number)
```
**Output:**
```
Kaça kadar sayalım?: 10
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```
Liste elemanlarını `len()` fonksiyonu yardımıyla while loop kullanarak bastırabilirsiniz.
```py
liste = [12,15,18,26,38]
index = 0
while (index != (len(liste)-1)):
	print(liste[index], end=", ")
	index += 1
print(liste[index])
```
**Output: ** `12, 15, 18, 26, 38`

**Not:** Sonsuz döngüye giren programlarınızı sonlandırmak için `CTRL + C` tuş kombinasyonunu kullanabilirsiniz. Bu tuş kombinasyonu, terminalde ya da cmd'de sonsüz döngüye girmiş programlarınızı sonlandırır.

## `while true` Loop
`while` loop, koşul durumu `True` olduğu sürece çalışır demiştik. Buna göre, `while` loop'un koşul durumuna `true` value'sini verirsek `while (true)` şeklinde bir yapı elde etmiş oluruz ve bu loop'u çalıştırırsak kendini sonsuz kere tekrarlar. Bu yapıyı kullanışlı hale getirmek için ileride bahsedeceğimiz `break` deyimini kullanacağız.

# `for` Loop
`for` loop `for` loop'un `while` loop'dan farkı, tekrar sayısını manuel olarak ayarlayabilmemizdir. `for` loop, kendisine verilen **Iterable** objeden, loop içinde kullanmak için bir **Iterator** oluşturuyor. Bu aşama arka planda gerçekleşen bir işlem olduğu için kullanıcılar tarafından direkt göslemlenemez. Daha sonra bu **Iterator**, `StopIteration` hatası döndürene kadar yenilenmeye (next) devam eder. Aşağıdaki `for` ve `while` loop kodları biribiryle tamamen aynı çalışır:
```py
a = [1,2,3,4,5]
for i in a:
	print(i)
```
```py
a = [1,2,3,4,5]
b = iter(a) # Iterator oluşturmak için kullanılan bir fonksiyon.
while True:
	try:
		i = next(b)
	except StopIteration:
		break
	print(i)
```
`for` loop'un syntax'ı
```py
for <var> in <iterable>:
	# Kodlar
```
Buradaki `<var>`, `for` loop'un scope'unda kullanılabilen bir local variable; `<iterable>` ise üzerinde gezinilebilen objedir. `<iterable>`'ı daha ayrıntılı açıklamak gerekirse:

**Ön bilgi:** *Iterate* ile *Iterate over* kelimelerinin farkı şudur:
- **Iterate**, bir şeyi bir kere tekrarlamak anlamında kullanılan bir fiildir (repeat).
-  **Iterate over**, bir şeyi sürekli tekrarlamak anlamında kullanılır (repeatedly).

**Iterator** ile **Iterable** İki farklı kavramdır. Defalarca tekrarlanabilir (can iterate over) herhangi bir şey, **Iterable** (tekrarlanabilir) bir objedir. `str`, `list`, `tuple`, `set`, `frozenset`, `dict` gibi data type'lar **Iterable**'dir. Collection type'lar (arrays) genellikle **iterable**'dir.
- **List**, indexlenebilir (yani sıralı) ve değiştirilebilir (mutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin verir.

- **Tuple**, indexlenebilir (yani sıralı) ve değiştirilemez (immutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin verir.

- **Set**, indexlenemez (yani sırasız) ve değiştirilebilir (mutable) bir collection'dır. Duplicate members'a (Bir öğeden birden fazla olması) izin vermez.

- **Dictionary**, indexlenebilir (yani sıralı) ve değiştirilebilir (mutable) bir collection'dır. Python 3.6'dan önce indexlenemezken (yani sırasız),  Python 3.7'den itibaren indexlenebilir (yani sıralı) olmuştur. Duplicate members'a (Bir öğeden birden fazla olması) izin vermez.
Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#next).

[`iter()`](asd) fonksiyonu kullanarak, **Iterable** (tekrarlanabilir) bir objeden, **Iterator** objesi oluşturulabilir. Bunu mümkün kılmak için **Iterable** (tekrarlanabilir) bir objenin class'ının, **Iterator** döndüren bir `__iter__` ya da `0` ile başlayan sıralı (sequential) index'lere sahip `__getitem__` methoduna ihtiyacı vardır. `iter()` fonksiyonuna **Iterable** (tekrarlanabilir) olmayan bir obje verilirse, `TypeError` hatası döndürülür. **Iterator**'ler, objenin bir sonraki item'ına geçmeye yarayan `__next__()` methoduna sahiptir. **Iterator**'ler, `__next__()` methodu kullanarak, **Iterable** bir obje üzerinde iterate (yenileme) yapmak için kullanılan objelerdir.
```py
liste = ["l", "i", "s", "t", "e"]
liste_iter1 = iter(liste)
liste_iter2 = iter(liste)
  
print(next(liste_iter1)) # Output: l
print(next(liste_iter1)) # Output: i
print(next(liste_iter1)) # Output: s
print(next(liste_iter1)) # Output: t
print(next(liste_iter1)) # Output: e
  
print(liste_iter2.__next__()) # Output: l
print(liste_iter2.__next__()) # Output: i
print(liste_iter2.__next__()) # Output: s
print(liste_iter2.__next__()) # Output: t
print(liste_iter2.__next__()) # Output: e
```
**Not:** Bütün **Iterator**'ler **Iterable**'dir ama her **Iterable** obje, **Iterator** değildir. Örneğin bir `list` **Iterable** bir objedir ama **Iterator** değildir.

**Not:** Bir **Iterator**, barındırdığı öğe sayısından fazla `next` methodu ya da fonksiyonu kullanılırsa, başka kullanılabilir öğe bulamadığı için `StopIteration` hatası döndürülür. Örnek:
```py
iterable_item = ["selam", "merhaba"]
iterator = iter(iterable_item)

print(next(iterator)) # Output: selam
print(next(iterator)) # Output: merhaba
print(next(iterator)) # Output: StopIteration
```

Python'daki `for` loop, mantığı, diğer low level dillerdeki **for-each** loop mantığına dayanır. for-each loop ile ilgili bilgi için [**buraya**](https://en.wikipedia.org/wiki/Foreach_loop), for loop'un çalışma mantığıyla ilgili ayrıntılı bilgi için de [**buraya**](https://towardsdatascience.com/python-basics-iteration-and-looping-6ca63b30835c) tıklayınız.

Örnek:
```py
for i in  range(5): # range(), daha sonra anlatılacak.
	print("|", i, end=" | ")

# Output: | 0 | | 1 | | 2 | | 3 | | 4 | 
```
## Listelerin İçinde Gezinmek
```py
liste = ["Selam","Merhaba","Hello"]
for i in liste:
	print("|", i, end=" | ")

# Output: | Selam | | Merhaba | | Hello | 
```
`for` loop'lara birden fazla sequence eklenebilir. Ama `for` bu sequence'ların her birine tek bir value gibi davranacaktır. Örneklerde daha kolay farkedeceksiniz:

### String'lere Davranışı
```py
a1 = "Selam"
for i in a1:
	print("|", i, end=" | ")
	
# Output: | S | | e | | l | | a | | m | 
```
Python, birden fazla string değere böyle davranır:
```py
a1 = "Selam"
a2 = "Ola"
a3 = "Hello"
for i in a1,a2,a3:
	print("|", i, end=" | ")

# Output: | Selam | | Ola | | Hello |
```
**Örnek Program:**
Aşağıdaki programda, `cumle` variable'sine girdiğiniz input değerindeki boşluk `" "` karakterlerini, underscore `"_"` karakteri ile değiştirip, son durumu ekrana basar.
```py
# Stringi editemek
cumle=input("Bir cümle yazınız: ")

release,l1,index="", [], 0

for i in cumle:
	l1.append(i)
	
for j in l1:
	if j == " ":
		l1[index] = "_"
	release += l1[index]
	index += 1
	
print(release)
```
**Output:**
```
Bir cümle yazınız: python tutorial klasörü.md
python_tutorial_klasörü.md
```
**Örnek Program:**
```py
# İki string arasındaki farkları bulmak
ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"
fark = ""
  
for s in ikinci_metin:      # ikinci_metin'de 's' dediğimiz bütün öğeler için
	if  not s in ilk_metin: # eğer 's' ilk_metin'de yoksa
		if  not s in fark:  # eğer 's' fark'ta da yoksa
			fark += s       # bu öğeyi fark değişkenine ekle
			
print(fark)                 # fark değişkenini ekrana bas
```
**Output:**
```
uıorye
```

### Listelere Davranışı
```py
liste = ["Selam","Merhaba","Hello"]
for i in liste:
	print("|", i, end=" | ")

# Output: | Selam | | Merhaba | | Hello | 
```
Python, birden fazla list değere böyle davranır:
```py
a1 = [1,2,3]
a2 = [4,5,6]
a3 = [7,8,9]
for i in a1,a2,a3:
	print("|", i, end=" | ")

# Output: | [1, 2, 3] | | [4, 5, 6] | | [7, 8, 9] |
```
İki boyutlu listeler üzerinde gezinmek için nasted (iç içe) `for` kullanılabilir. Aşağıdaki örnekte, ilk for `a1` listesinin ikili elemanlarını alır ve içteki (*nasted*) for ise bu ikili elemanları teker teker alır.
```py
a1 = [(1,2),(3,4),(5,6),(7,8)]
for i in a1:
	print("|", i, end=" | ")
	for j in i:
		print("|", j, end=" | ")

# Output:
| (1, 2) | | (3, 4) | | (5, 6) | | (7, 8) | 
| 1 | | 2 | | 3 | | 4 | | 5 | | 6 | | 7 | | 8 |
```
Başka bir yöntem:
```py
a1 = [(1,2),(3,4),(5,6),(7,8)]
l1, l2 = list(), list()
for i,j in a1:
	l1.append(i)
	l2.append(j)
	
print(l1,l2, sep="\n")

# Output:
[1, 3, 5, 7]
[2, 4, 6, 8]
```
Buradaki `i,j`, `a1` listesindeki ikili elemanlardan ilki `i`, ikincisi `l` local variable'ına atansın anlamına gelir. Daha iyi anlamak için bir de üçlü versiyonuna bakalım:
```py
a1 = [(1,2,3),(4,5,6),(7,8,9)]
l1, l2, l3 = list(), list(), list()
for i,j,k in a1:
	l1.append(i)
	l2.append(j)
	l3.append(k)
	
print(l1,l2,l3, sep="\n")

# Output:
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
```
Gördüğünüz gibi `for i,j,k` yapısı böyle kullanılıyor. Aşağıdaki gibi bir listenin elemanlarını `for i,j,k` yapısını kullanarak teker teker ekrana bastıramayız. Bunun için nasted `for` loop kullanabiliriz.
```py
a6 = [( (1,2) , (3,4) ) , ( (7,8) , (9,10) )]
for (x,y,z) in a6:
print("x: {} y: {} z: {}" .format(x,y,z))
```
Yukarıdaki kod çalışmayacaktır çünkü `for i,j,k` yapısının parantezlerle alakası yoktur, aynı alanda bulunan value'larla alakası vardır. Ama aşağıdaki kod çalışır.
```py
a6 = [( (1,2) , (3,4) ) , ( (7,8) , (9,10) )]
l1, l2, l3 = list(), list(), list()
for i in a6:
	l1.append(i)
	for j in i:
		l2.append(j)
		for k in j:
			l3.append(k)
  
print(l1,l2,l3, sep="\n")
```
**Output:**
```
[((1, 2), (3, 4)), ((7, 8), (9, 10))]
[(1, 2), (3, 4), (7, 8), (9, 10)]
[1, 2, 3, 4, 7, 8, 9, 10]
```
## Dictionary'lerin İçinde Gezinmek
Dictionary'lerin de içinde `for` loop kullanarak gezinebilirsiniz.
```py
dict_exp = {"bir": 1,"iki": 2,"üç": 3,"dört": 4}
  
for i in dict_exp:
	print(f"| {i}", end=" | ")
```
**Output:**
```
| bir | | iki | | üç | | dört | 
```
Yukarıdaki kodda, `dict_exp` sözlüğüne hiçbir method uygulamazsanız, `for` loop sadece `key`'leri alır.
```py
dict_exp = {"bir": 1,"iki": 2,"üç": 3,"dört": 4}
  
for i in dict_exp.keys():
	print(f"| {i}", end=" | ")
```
**Output:**
```
| bir | | iki | | üç | | dört | 
```
Yukarıdaki kodda, `dict_exp` sözlüğüne `keys()` methodunu uygularsanız, `for` loop`dict_keys` nesnesi içinde gezinir.
```py
dict_exp = {"bir": 1,"iki": 2,"üç": 3,"dört": 4}
  
for i in dict_exp.values():
	print(f"| {i}", end=" | ")
```
**Output:**
```
| 1 | | 2 | | 3 | | 4 | 
```
Yukarıdaki kodda, `dict_exp` sözlüğüne `values()` methodunu uygularsanız, `for` loop`dict_values` nesnesi içinde gezinir.
```py
dict_exp = {"bir": 1,"iki": 2,"üç": 3,"dört": 4}

for i,j in dict_exp.items():
	print("Key: {} | Value: {}" .format(i, j))```
```
**Output:**
```
Key: bir | Value: 1
Key: iki | Value: 2
Key: üç | Value: 3
Key: dört | Value: 4
```
Yukarıdaki kodda, `dict_exp` sözlüğüne `items()` methodunu uygularsanız, `for` loop`dict_items` nesnesi içinde gezinir. Bu nesnenin içindeki her ikili tuple öğesinin içindeki iki öğeyi `i` ve `j` local variable'lerine atar. Bu işlemin mantığını [burada](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/.md/donguler/donguler.md#listelere-davranışı) anlattım.

# `else`'nin Loop'larda Kullanımı
`while` loop, kendisine tanımlanan işlem `True` sonuç verdiği sürece kendi bloğunu çalıştırıyordu. Bu değer `False` olduğunda da çalışmayı durduruyordu. Benzer durum `for` loop'da, `<iterable>`'a tanımlanan objenin sınırına gelince ortaya çıkıyor. Yani `for` loop, `<iterable>`'a tanımlanan objenin sınırına gelince çalışmayı durduruyor. `else` deyimi, `while` ya da `for` loop'dan sonra kullanılırsa,  `while` ya da `for` loop'un bu *"çalışmayı durdurma"* olayını fark edip çalışır. Örnekler:

**`while` loop örneği:**
```py
a = 1
while a < 10: # a, 10'dan küçük olduğu sürece
	a += 1    # a, 1 arttırılır.
else:         # Ama a, 10'dan küçük olmazsa
	print(a)  # a'nın değeri ekrana yazdırılır.
```
**`for` loop örneği:**
```py
for i in  range(11): # 0'dan 10'a kadar (10 dahil) olan her bir `i` sayısı için
	pass             # pass komutu çalıştırılır. Yani hiçbir işlem yapılmaz.
else:                # range(11) objesinin sonuna ulaşılınca
	print(i)         # `i` değerinin aldığı son değer ekrana yazdırılır.
```
**Örnek program:**
```py
veri_girisi = input("Sayı gir: ")     # Kullanıcıdan değer girmesi istenir.
while  not veri_girisi.isnumeric():   # Kullanıcının girdiği değer sayı olmadığı müddetçe
	print("Bu bir sayı değil.")       # "Bu bir sayı değil." ekrana bastır.
	veri_girisi = input("Sayı gir: ") # Kullanıcıdan tekrar değer girmesi istenir.
else: 								  # Ama kullanıcının girdiği değer sayı ise
	print(veri_girisi)				  # Bu değer ekrana yazdırılır.
```

# İlgi Araçları

## `break` Deyimi
Bir loop, kendi kapsamı (scope) içinde herhangi bir `break` deyimiyle karşılaştığı zaman, bir anda sonlanır. Böylelikle döngü hiçbir koşula bağlı kalmadan sonlanmış olur. Örnek:
```py
i = 0
while (i < 10):
	if a == 4:
		break
	i += 1
```
**Output:**
```
0 1 2 3
```
`break` deyimi, sadece kapsamında bulunduğu ilk loop'u sonlandırır. Yani iç içe döngülerde, `break` deyimini kapsayan en içteki loop sonlanır. Örnek:
```py
i = 1
j = 0
while (i < 10):
	if i == 5:
		break
	print(f"\n{i}. Loop")
	i += 1
	while (j < 10):
		if j == 3:
			break
		print(f"J: {j}", end=" ")
		j += 1
	j = 0
```
**Output:**
```
1. Loop
J: 0 J: 1 J: 2
2. Loop
J: 0 J: 1 J: 2
3. Loop
J: 0 J: 1 J: 2
4. Loop
J: 0 J: 1 J: 2
```
Yukarıdaki durumlar `for` loop için de geçerlidir.

## `continue` Deyimi
Bir loop, kendi kapsamı (scope) içinde herhangi bir `break` deyimiyle karşılaştığı zaman, kendinden sonraki işlemleri yapmadan loop'u başa sarar. Örnek:
```py
liste = [1,2,3,4,5]
for i in liste:
	if i == 2:
		continue
	print(i, end=" ")
```
**Output:**
```
1 3 4 5
```

## `pass` Deyimi
`pass` deyimi, *"hiçbir şey yapma, geç"* anlamına gelmektedir. Python, program içinde herhangi bir yerde bu deyimle karşılaşırsa, hiçbir şey yapmaz ve sonraki koda geçer.
```py
while True:
	parola = input("parola belirleyin: ")

	if not parola: # `parola` boşsa boolean değeri `False` olur.
		pass
	elif len(parola) in range(3, 8): # len(parola), range(3,8) objesinin içindeki herhangi bir değeri içeriyorsa çalışır.
		print("Yeni parolanız", parola)
		break
	else:
		print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")
```
