# İçindekiler

- [Sözlükler (Dictionaries)](#1)
    - [Sözlük'de İşlemler](#1.1)
    - [Sözlük Üreteçleri (Dictionary Comprehensions)](#1.2)
    - [Sözlük Methodları](#1.3)
        - [<code>keys()</code> Methodu](#1.3.1)
        - [<code>values()</code> Methodu](#1.3.2)
        - [<code>items()</code> Methodu](#1.3.3)
        - [<code>get(key, default)</code> Methodu](#1.3.4)
        - [<code>clear()</code> Methodu](#1.3.5)
        - [<code>copy()</code> Methodu](#1.3.6)
        - [<code>fromkeys(iterable, value = "None")</code> Methodu](#1.3.7)
        - [<code>pop(key, default)</code> Methodu](#1.3.8)
        - [<code>popitem()</code> Methodu](#1.3.9)
        - [<code>setdefault(key, default = "None")</code> Methodu](#1.3.10)
        - [<code>update(m)</code> Methodu](#1.3.11)

<h1 id="1">Sözlükler (Dictionaries)</h1>

Dictionary'ler, içinde objeleri depolayabilen, sıralı, değiştirilebilir data type'lardır. `dict(object)` build'in fonksiyonu ile liste oluşturabilirsiniz veya uygun objeleri liste'ye dönüştürebilirsiniz. Listeler süslü parantez (`{}`) ve mapping (`key:value`) ile ifade edilir. Örnek:
```py
print({}, type({}))
print(dict(), type(dict()))
print({"key": "value"}, type({"key": "value"}))
print({"key1": "value", "key2": "value"}, type({"key1": "value", "key2": "value"}))
print(dict(key1="value", key2 = "value"), type(dict(key1="value", key2 = "value")))
```
**Output:**
```
{} <class 'dict'>
{} <class 'dict'>
{'key': 'value'} <class 'dict'>
{'key1': 'value', 'key2': 'value'} <class 'dict'>
{'key1': 'value', 'key2': 'value'} <class 'dict'>
```
Dictionary'lere `str`, `int`, `float`, `complex`, `list`, `dict`, `tuple`, `set` gibi birçok data type'ı `value` olarak; `tuple`, `str`, `int`, `float`, `complex` gibi değiştirilemez (immutable) data type'ları `key` olara ekleyebilirsiniz. `list` ve `dict` değiştirilebilir (mutable) data type olduğu için sözlüklere `key` olarak girilemez. Bunlar dışındaki data type'lar `key` olarak kullanılmaya çalışırsanız `TypeError: unhashable type: 'data type'ın ismi'` gibi hatalar yükseltilir. Sözlüklere girilebilecek veri tiplerine örnek:
```py
sözlük_düzeni = {1          : "int",
				 2.5        : "float",
				 3 + 6j     : "complex",
				 "string"   : "str",
				 "int"      : 1,
				 "float"    : 2.5,
				 "complex"  : 3 + 6j,
				 "liste"    : ["l1", "l2", "l3"],
				 "tuple"    : ("t1", "t2", "t3"),
				 ("Tuple",) : "tuple",
				 "set"      : {"s1", "s2", "s3"},
				 "dict"     : {"k1" : "v1",
							   "k2" : "v2",
							   "k3" : "v3"}}

print(sözlük_düzeni) # Output: {1: 'int', 2.5: 'float', (3+6j): 'complex', 'string': 'str', 'int': 1, 'float': 2.5, 'complex': (3+6j), 'liste': ['l1', 'l2', 'l3'], 'tuple': ('l1', 'l2', 'l3'), ('Tuple',): 'tuple', 'set': {'l2', 'l3', 'l1'}, 'dict': {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}}
print(sözlük_düzeni["string"][1]) # Output: t
print(sözlük_düzeni["liste"][1]) # Output: l2
print(sözlük_düzeni["tuple"][1]) # Output: t2
print(sözlük_düzeni["dict"]["k1"]) # Output: v1
```
Gördüğünüz gibi dictionary içine tanımlanmış `list`, `tuple`, `str` gibi type'ların index'lerine ve nested dictionary'lerin içeriğine erişebiliyoruz.

**Not:** Aşağıdaki gibi tanımlanmış list, tuple ve set objeleri direkt olarak dictionary'e dönüştürülebilir:
```py
s1 = {"a":1, "b":2, "c":3}     # Dictionary
s2 = [("a",1),("b",2),("c",3)] # List
s3 = (("a",1),("b",2),("c",3)) # Tuple
s4 = {("a",1),("b",2),("c",3)} # Set
print(dict(s1), dict(s2), dict(s3), dict(s4),sep="\n")
```
**Output:**
```
{'a': 1, 'b': 2, 'c': 3}
{'a': 1, 'b': 2, 'c': 3}
{'a': 1, 'b': 2, 'c': 3}
{'a': 1, 'c': 3, 'b': 2}
```
**Not:** Set sırasız bir type olduğu için set to dict (kümeden sözlüğe) işlemi diğer işlemlerden farklı bir output verdi. Nedenini set type'ı öğrendiğinizde anlayacaksınız.

<h2 id="1.1">Sözlük'de İşlemler</h2>

Dictionary'ler `str`, `list` ve `tuple` gibi indexlenemez. Bunun yerine `key`'den `value` elde ettiğiniz mapping adlı bir yöntem kullanılır. Örnek:
```py
d1 = {'Bir': 1, 'İki': 2, 'Üç': 3}
print(d1["İki"]) # Output: 2
```
İç içe (nested) dictionary'lerde:
```py
d1 = {"Bir Basamaklı": {'Bir': 1, 'İki': 2, 'Üç': 3},
      "İki Basamaklı": {'On': 10, 'Yirmi': 20, 'Otuz': 30},
      "Üç Basamaklı": {'Yüz': 100, 'İki Yüz': 200, 'Üç Yüz': 300},}

print(d1["İki Basamaklı"]["Otuz"]) # Output: 30
```
`dictionary[key1][key2]` yapısını çalışma mantığı:
- Python `dictionary[key1][key2]` yapısını soldan sağa okumaya başladığı için önce `dictionary[key1]` kısmını okur. Bu dictionary'ye `x` diyelim.
- Bu işlemden sonra `dictionary[key1][key2]` kodu Python'un gözünde `x[key2]` koduna dönüşür. Python `x[key2]` kodu içinde aynı işlemleri yapar.
- Python'u LEGO gibi düşünün. Kodları bütün olarak değil, parça parça yorumlayın. Böylelikle Python'un çalışma mantığını anlarsınız. Örneğin aşağıdaki iki kod tamamen aynı işi yapmaktadır:
    ```py
    dictionary = {"1":
                      {"1.1":
                              {"1.1.1":
                                       {'sıfır': 0, 'bir': 1},
                              "1.1.2":
                                       {'iki': 2, 'üç': 3}},
                      "1.2":
                              {"1.2.1":
                                       {'dört': 4, 'beş': 5},
                              "1.2.2":
                                      {'altı': 6, 'yedi': 7}}},
                  "2":
                      {"2.1":
                              {"2.1.1":
                                       {'sekiz': 8, 'dokuz': 9},
                              "2.1.2":
                                       {'on': 10, 'on bir': 11}},
                      "2.2":
                              {"2.2.1":
                                       {'on iki': 12, 'on üç': 13},
                              "2.2.2":
                                       {'on dört': 14, 'on beş': 15}}}}
    
    a1 = dictionary["1"]
    a2 = a1["1.1"]
    a3 = a2["1.1.1"]
    a4 = a3["bir"]
    print(a4) # Output: 1
    
    print(dictionary["1"]["1.1"]["1.1.1"]["bir"]) # Output: 1
    ```

`for` loop'un loop control variable'ı dictionary'nin `key`'leri üzerinde gezinir. Örnek:
```py
d1 = {'Bir': 1, 'İki': 2, 'Üç': 3}

for i in d1:
    print(i,end=", ")
```
**Output:**
```py
Bir, İki, Üç, 
```

**Not:** Sözlükte bulunmayan bir `key`'e erişmeye çalıştığınızda `KeyError` hatası yükseltilir. Örnek:
```py
d1 = {'Bir': 1, 'İki': 2, 'Üç': 3}
print(d1["Dört"]) # KeyError: 'Dört'
```

Bir diçtionary'e öğe eklemek için mapping yöntemini kullanabilirsiniz. Örnek:
```py
d1 = {'Bir': 1, 'İki': 2, 'Üç': 3}
id1 = id(d1)
d1["Dört"] = 4
id2 = id(d1)
print(d1["Dört"]) # Output: 4
print(id1 == id2) # Output: True
```
Bu işlem sonucunda oluşan yeni dictionary ile eski dictionary aynı objedir (id'leri aynıdır).

Bir dictionary'de her `key`'den en fazla 1 tane olabilir. Bir dictionary'e eklemeyek istediğiniz `key` zaten mevcutsa, mevcut `key`'in value'su yerine eklemek istediğiniz `key`'in value'su geçer. Örnek:
```py
d1 = {'Bir': 1, 'İki': 2, 'Üç': 3}
print(d1) # Output: {'Bir': 1, 'İki': 2, 'Üç': 3}

id1 = id(d1)
d1["Bir"] = 4
id2 = id(d1)

print(d1) # Output: {'Bir': 4, 'İki': 2, 'Üç': 3}
print(id1 == id2) # Output: True
```
Sıfırdan bir dictionary yazarken aynı keyden birden fazla yazarsanız, en son yazdığınız key'in value'su geçerli olur. Çünkü Python kodları soldan sağa doğru okuyor. Bu yüzden en son tanımlanan `key` en sağda, dolayısıyla en sağdaki en son okunan olacağı için Python bunu geçerli sayacak. Örnek:
```py
d1 = {'Bir': 1, 'İki': 2, 'Üç': 3, 'Bir': 4}
print(d1) # Output: {'Bir': 4, 'İki': 2, 'Üç': 3}
```
Bu durum birbiri ardına tanımlanan aynı isimdeki variable'lar arasından en son tanımlananın value'sunun geçerli olmasına benziyor.  

**Not:** Dictionary, indexlenebilir (yani sıralı) ve değiştirilebilir (mutable) bir collection'dır. Python 3.6'dan önce indexlenemezken (yani sırasız),  Python 3.7'den itibaren indexlenebilir (yani sıralı) olmuştur. Örnek:
```py
d1 = {"a":1, "b":2, "c":3}
d2 = {"c":3, "a":1, "b":2}
print(d1, d2, sep="\n")
```
**Output:**
```
{'a': 1, 'b': 2, 'c': 3}
{'c': 3, 'a': 1, 'b': 2}
```
Gördüğünüz gibi item'ları dictionary'e hangi sırayla tanımladıysanız, o sırayla dictionary'de bulunur.

**Not:** Dictionary'ler, belli bir yapıda sıralanmış verileri saklamak konusunda çok yararlıdır çünkü verileri `"yaş":20, "boy":175, "isim":"Alex"` gibi isimlendirebiliyorsunuz.

Dictionary'lerin `key` sayısına `len()` fonksiyonuyla ulaşılabilir. Örnek:
```py
d1 = {'Bir': 1, 'İki': 2, 'Üç': 3}
print(len(d1)) # Output: 3
```

Dictionary type, aritmetik (sayısal) işlemleri desteklemez. Örnek:
```py
d1 = {'Bir': 1, 'İki': 2, 'Üç': 3}
d2 = {'Dört': 4, 'Beş': 5, 'Altı': 6}
print(d1+d2) # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
print(d1*2) # TypeError: unsupported operand type(s) for *: 'dict' and 'int'
```

Dictionary'de belli bir `key`'i tamamen silmek:
```py
d1 = {'Bir': 1, 'İki': 2, 'Üç': 3}
print(d1) # Output: {'Bir': 1, 'İki': 2, 'Üç': 3}
del d1["Bir"]
print(d1) # Output: {'İki': 2, 'Üç': 3}
```

Dictionary objesini tamamen silmek:
```py
d1 = {'Bir': 1, 'İki': 2, 'Üç': 3}
print(d1) # Output: {'Bir': 1, 'İki': 2, 'Üç': 3}
del d1
print(d1) # NameError: name 'd1' is not defined
```

Bir Dictionary'i kopyalamak ve sonuçları:
```py
d1 = {'Bir': 1, 'İki': 2, 'Üç': 3}
d2 = d1
print(d1) # Output: {'Bir': 1, 'İki': 2, 'Üç': 3}
print(d2) # Output: {'Bir': 1, 'İki': 2, 'Üç': 3}
print(id(d1) == id(d2)) # Output: True

d1["Bir"] = 4
print(d1) # Output: {'Bir': 4, 'İki': 2, 'Üç': 
print(d2) # Output: {'Bir': 4, 'İki': 2, 'Üç': 
```
Dictionary, değiştirilebilir (mutable) bir data type olduğu için assignment operator (`=`) kullanılarak bir dictionary objesini yukarıdaki gibi farklı bir variable'a atarsanız, son durumda oluşan objeler aynı dictionary objesine atıfta bulunacağı (refers to) için birinde yapılan değişiklikler diğerini de etkiler. Bu durum değiştirilemez (immutable) data type'lar için geçerli değildir çünkü değiştirilemez (immutable) data type'ları değiştirmek için yeniden tanımlama (redefinition) işlemi yaptığımız için birbirinden bağımsız objeler elde ediyoruz.

<h2 id="1.2">Sözlük Üreteçleri (Dictionary Comprehensions)</h2>

**Comprehension**, tek satırda oluşturduğumuz **Generator** (daha sonra anlatılacak) yapısına verilen isimdir. `(expression for item in iterable)` syntax'ına sahiptir (parantezler dahil). Bu generator yapısı (**Generator Comprehension**) bir generator objesi oluşturmakta kullanılır. Daha sonra bu generator objesini dictionary type'a dönüştürerek Dictionary Comprehension oluşturabiliriz. Örnek:
```py
dict_exp = {i:i**2 for i in range(1,4)}
print(dict_exp) # Output: {1: 1, 2: 4, 3: 9}
```
Bu konu daha sonra comprehension başlığı altında daha detaylı anlatılacak. Türkçe alfabe yapmak:
```py
harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
harfli_sözlük = {i: harfler.index(i) for i in harfler}
print(harfli_sözlük)
```
**Output:**
```
{'a': 0, 'b': 1, 'c': 2, 'ç': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'ğ': 8, 'h': 9, 'ı': 10, 'i': 11, 'j': 12, 'k': 13, 'l': 14, 'm': 15, 'n': 16, 'o': 17, 'ö': 18, 'p': 19, 'r': 20, 's': 21, 'ş': 22, 't': 23, 'u': 24, 'ü': 25, 'v': 26, 'y': 27, 'z': 28}
```

<h2 id="1.3">Sözlük Methodları</h2>

<h3 id="1.3.1"><code>keys()</code> Methodu</h3>

Bir dictionary'nin sadece `key` kısmını içeren `dict_keys` objesi döndürür. `dict_keys` objesini diğer iterable objelere dönüştürebilirsiniz. Örnek:
```py
sözlük = {'a': "0", 'b': "1", 'c': "2", 'ç': "3", 'd': "4"}
print("native keys: ", sözlük.keys()) # Output: native keys: dict_keys(['a', 'b', 'c', 'ç', 'd'])
print("str:", str().join(sözlük.keys())) # Output: str: abcçd
print("list:", list(sözlük.keys())) # Output: list: ['a', 'b', 'c', 'ç', 'd']
print("tuple:", tuple(sözlük.keys())) # Output: tuple: ('a', 'b', 'c', 'ç', 'd')
print("set:", set(sözlük.keys())) # Output: tuple: {'d', 'a', 'b', 'ç', 'c'}
```
Bu dönüşümü string'lerde yaparken `join` methodunun kullanmanız gerekmektedir. `str(sözlük.keys())` şeklinde kullanılırsa `sözlük.keys()` ile aynı output'u verir.

<h3 id="1.3.2"><code>values()</code> Methodu</h3>

Bir dictionary'nin sadece `value` kısmını içeren `dict_values` objesi döndürür. `dict_values` objesini diğer iterable objelere dönüştürebilirsiniz. Örnek:
```py
sözlük = {'a': "0", 'b': "1", 'c': "2", 'ç': "3", 'd': "4"}
print("native keys:", sözlük.values()) # Output: native keys: dict_values(['0', '1', '2', '3', '4'])
print("str:", str().join(sözlük.values())) # Output: str: 01234
print("list:", list(sözlük.values())) # Output: list: ['0', '1', '2', '3', '4']
print("tuple:", tuple(sözlük.values())) # Output: tuple: ('0', '1', '2', '3', '4')
print("set:", set(sözlük.values())) # Output: set: {'4', '0', '3', '1', '2'}
```
Bu dönüşümü string'lerde yaparken `join` methodunun kullanmanız gerekmektedir. `str(sözlük.values())` şeklinde kullanılırsa `sözlük.values()` ile aynı output'u verir.

<h3 id="1.3.3"><code>items()</code> Methodu</h3>

Bir dictionary'nin hem `key` hem de `value` kısmını içeren `dict_items` objesi döndürür. `dict_items` objesini diğer iterable objelere dönüştürebilirsiniz. Örnek:
```py
sözlük = {'a': "0", 'b': "1", 'c': "2", 'ç': "3", 'd': "4"}
print("native keys:", sözlük.items()) # Output: native keys: dict_items([('a', '0'), ('b', '1'), ('c', '2'), ('ç', '3'), ('d', '4')])
print("list:", list(sözlük.items())) # Output: list: [('a', '0'), ('b', '1'), ('c', '2'), ('ç', '3'), ('d', '4')]
print("tuple:", tuple(sözlük.items())) # Output: tuple: (('a', '0'), ('b', '1'), ('c', '2'), ('ç', '3'), ('d', '4'))
print("set:", set(sözlük.items())) # Output: set: {('ç', '3'), ('a', '0'), ('b', '1'), ('c', '2'), ('d', '4')}
```
`dict_items` objesi oluşturulduğu format (formattan kastım `('a', '0'), ('b', '1'), ...` bu) yüzünden string type'a dönüştürülemez.

<h3 id="1.3.4"><code>get(key, default)</code> Methodu</h3>

Uygulandığı dictionary'de `key` parametresine argüman olarak girilen değerin bulunup bulunmadığını kontrol eder. Bulursa o `key`'e karşılık gelen `value`'yu, bulamazsa `default` parametresine tanımlanan değeri döndürür. Örnek:
```py
sözlük = {'a': "0", 'b': "1", 'c': "2", 'ç': "3", 'd': "4"}
print(sözlük.get("a", "'a' yok")) # Output: 0
print(sözlük.get("z", "'z' yok")) # Output: 'z' yok
```

<h3 id="1.3.5"><code>clear()</code> Methodu</h3>

Uygulandığı dictionary'nin içeriğini tamamen siler. `del` statement'dan farkı, dictionary objesini silmemesi. Örnek:
```py
sözlük = {'a': "0", 'b': "1", 'c': "2", 'ç': "3", 'd': "4"}
sözlük.clear()
print(sözlük) # Output: {}

sözlük = {'a': "0", 'b': "1", 'c': "2", 'ç': "3", 'd': "4"}
del sözlük
print(sözlük) # Output: NameError: name 'sözlük' is not defined
```

<h3 id="1.3.6"><code>copy()</code> Methodu</h3>

Uygulandığı dictionary'nin bir kopyasını oluşturur. `sözlük1 = sözlük2` gibi assignment operator kullanarak dictionary kopyalama yönteminden farkı, yeni dictionary ile eski dictionary'nin birbirinden bağımsız, farklı (farklı ID'lere sahip) objeler olmasıdır. Böylece birinde yapılan değişikli diğerini etkilemez. Örnek:
```py
sözlük = {'a': "0", 'b': "1", 'c': "2", 'ç': "3", 'd': "4"}
sözlük_copy1 = sözlük
print(sözlük) # Output: {'a': '0', 'b': '1', 'c': '2', 'ç': '3', 'd': '4'}
print(sözlük_copy1) # Output: {'a': '0', 'b': '1', 'c': '2', 'ç': '3', 'd': '4'}

sözlük_copy1["a"] = "Sıfır"
print(sözlük) # Output: {'a': 'Sıfır', 'b': '1', 'c': '2', 'ç': '3', 'd': '4'}
print(sözlük_copy1) # Output: {'a': 'Sıfır', 'b': '1', 'c': '2', 'ç': '3', 'd': '4'}

sözlük_copy2 = sözlük.copy()
print(id(sözlük) == id(sözlük_copy2)) # Output: False
print(sözlük) # Output: {'a': 'Sıfır', 'b': '1', 'c': '2', 'ç': '3', 'd': '4'}
print(sözlük_copy2) # Output: {'a': 'Sıfır', 'b': '1', 'c': '2', 'ç': '3', 'd': '4'}

sözlük_copy2["b"] = "Bir"
print(sözlük) # Output: {'a': 'Sıfır', 'b': '1', 'c': '2', 'ç': '3', 'd': '4'}
print(sözlük_copy2) # Output: {'a': 'Sıfır', 'b': 'Bir', 'c': '2', 'ç': '3', 'd': '4'}
```

<h3 id="1.3.7"><code>fromkeys(iterable, value = "None")</code> Methodu</h3>

Yeni bir sözlük oluşturmak için kullanılır. `iterable` parametresine argüman olarak girilen iterable objenin öğelerini `key` olarak kullanır ve bütün bu `key`'lere `value` parametresinde argüman olarak belirtilen objeyi `value` olarak atar. Örnek:
```py
string_key = "123"
list_key = [1,2,3]
tuple_key = (1,2,3)
set_key = {1,2,3}
dictionary_key = {1: None, 2: None, 3: None}

string_value = "123"
list_value = [1,2,3]
tuple_value = (1,2,3)
set_value = {1,2,3}
dictionary_value = {1: None, 2: None, 3: None}
print({}.fromkeys(string_key,string_value), # Output: {'1': '123', '2': '123', '3': '123'}
	  {}.fromkeys(list_key,list_value), # Output: {1: [1, 2, 3], 2: [1, 2, 3], 3: [1, 2, 3]}
	  {}.fromkeys(tuple_key,tuple_value), # Output: {1: (1, 2, 3), 2: (1, 2, 3), 3: (1, 2, 3)}
	  {}.fromkeys(set_key,set_value), # Output: {1: {1, 2, 3}, 2: {1, 2, 3}, 3: {1, 2, 3}}
	  {}.fromkeys(dictionary_key,dictionary_value)) # Output: {1: {1: None, 2: None, 3: None}, 2: {1: None, 2: None, 3: None}, 3: {1: None, 2: None, 3: None}}
```

**Not:** `fromkeys` methodunu yaptığı iş bakımından değerlendirdiğinizde aslında bu method'un bir build-in fonksiyon olması gerektiği aklınıza gelmiş olabilir. Çünkü tek işlevi, parametrelerine girilen argümanları kullanarak yeni bir sözlük yaratmak. String'lerdeki `join` methodu da buna benzerdir ama en azından uygulandığı string'i de işleme katıyor (`print("--".join(m1)) # Output: 1--2--3`). Bu methodu önemli bir amaç uğruna kullanan görmedim şahsen.

<h3 id="1.3.8"><code>pop(key, default)</code> Methodu</h3>

`key` parametresine argüman olarak girilen obje, `pop` methodunun uygulandığı dictionary içinde varsa o `key`'i siler ve `value`'sunu, yoksa `default` parametresinde belirtilen değeri döndürür. Örnek:
```py
sözlük = {'a': "0", 'b': "1", 'c': "2", 'ç': "3", 'd': "4"}
print(sözlük.pop("a", "'a' yok")) # Output: 0
print(sözlük) # Output: {'b': '1', 'c': '2', 'ç': '3', 'd': '4'}
print(sözlük.pop("a", "'a' yok")) # Output: 'a' yok
print(sözlük.pop("a")) # Output: KeyError: 'a'
```

<h3 id="1.3.9"><code>popitem()</code> Methodu</h3>

`pop()` methoduna benzer çalışan ve parametresi bulunmayan bir methoddur. **Last In, First Out (LIFO)** mantığıyla çalışır. Yani sözlüğe en son eklenen (en son sıradaki, yani en sağdaki) `item`'i döndürür ve döndürülen `item`'i dictionary'den kaldırır. Eğer dictionary boşsa `KeyError` hatası yükseltir. `popitem` methodu bu işlemi Python 3.7'den önce rastgele yapardı çünkü 3.7 sürümünden önce dictionary'ler sırasızdı (`set` type gibiydi). Örnek:
```py
sözlük = {'a': 0, 'b': 1, 'c': 2}
print(sözlük.popitem()) # Output: ('c', 2)
print(sözlük) # Output: {'a': 0, 'b': 1}
```

<h3 id="1.3.10"><code>setdefault(key, default = "None")</code> Methodu</h3>

`key` parametresinde belirtilen `key`'i dictionary içinde arar. Varsa `key`'e ait `value`'yu döndürür, yoksa o `key`'i sözlüğe ekler ve `value`'sunu `default` parametresine argüman olarak girilen değer olarak ayarlar, en son olarak da `value`'sunu döndürür. `default` parametresi default olarak `None` değerine ayarlıdır. Örnek:
```py
sözlük = {'a': 0, 'b': 1, 'c': 2}
print(sözlük.setdefault("a","'a' harfi")) # Output: 0
print(sözlük) # Output: {'a': 0, 'b': 1, 'c': 2}
print(sözlük.setdefault("d","'d' harfi")) # Output: 'd' harfi
print(sözlük) # Output: {'a': 0, 'b': 1, 'c': 2, 'd': "'d' harfi"}
```

<h3 id="1.3.11"><code>update(m)</code> Methodu</h3>

`dict1.update(dict2)` formatında kullanılır. `dict1`'i, `dict2`'ye göre günceller. Örnek:
```py
sözlük1 = {'a': 0, 'b': 1, 'c': 2}
sözlük2 = {'a': 9, 'b': 4, 'c': 2}
sözlük3 = {'d': 13, 'e': 15}

print(sözlük1) # Output: {'a': 0, 'b': 1, 'c': 2}
sözlük1.update(sözlük2)
print(sözlük1) # Output: {'a': 9, 'b': 4, 'c': 2}

print(sözlük1) # Output: {'a': 9, 'b': 4, 'c': 2}
sözlük1.update(sözlük3)
print(sözlük1) # Output: {'a': 9, 'b': 4, 'c': 2, 'd': 13, 'e': 15}
```