# Dictionary Tanımlamak
Dictionary (sözlük), `key` ve `value` ile çalışan bir data type'dır. Her key'in bir value'si, her value'nin de bir ya da birden fazla key'i vardır. Örnek:
```py
s1 = {}
s2 = dict()
s3 = {"key": "value"}
s4 = {"key1": "value", "key2": "value"}
s5 = dict(key1="value", key2 = "value")
print(s1, s2, s3, s4, s5, sep="\n", end="\n\n")
print(type(s1), type(s2), type(s3), type(s4), type(s5), sep="\n")
```
**Output:**
```
{}
{}
{'key': 'value'}
{'key1': 'value', 'key2': 'value'}
{'key1': 'value', 'key2': 'value'}

<class 'dict'>
<class 'dict'>
<class 'dict'>
<class 'dict'>
<class 'dict'>
```
Dictionary'lere `string`, `int`, `float`, `complex`, `list`, `dict`, `tuple`, `set` gibi bir çok data type'ı `value` olarak ekleyebilirsiniz. `tuple`, `str`, ve *numeric* (`int`, `float`, `complex`) data type değiştirilemez (immutable) data type'lar olduğu için sözlüklere `key` olara eklenebilir. `list` ve `dict` değiştirilebilir (mutable) veri tipi olduğu için sözlüklere `key` olarak girilemez. Girilmeye çalışılırsa `TypeError: unhashable type: 'list'` ve `TypeError: unhashable type: 'dict'` hatalarından birisini alırsınız. Sözlüklere girilebilecek veri tiplerine örnek:
```py
sözlük_düzeni = {1                  : "int",
				 2.5                : "float",
				 3 + 6j             : "complex",
				 "string"           : "str",
				 "int"              : 1,
				 "float"            : 2.5,
				 "complex"          : 3 + 6j,
				 "liste"            : ["l1", "l2", "l3"],
				 "tuple"            : ("l1", "l2", "l3"),
				 ("Tuple",)         : "tuple",
				 "set"              : {"l1", "l2", "l3"},
				 "dict"             : {"k1" : "v1",
									   "k2" : "v2",
									   "k3" : "v3"}}
```

## Sözlük Üreteçleri (Dictionary Comprehensions)
Sözlük tanımlamak için üreteçlerden yararlanılabilir. Listelerde de gösterildiği gibi, tek satırda sözlük tanımlamamıza yarar. Örnek:
```py
# Harflere numara vermek
harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
  
harfli_sözlük = dict()
for i in harfler:
	harfli_sözlük[i] = harfler.index(i)
print(harfli_sözlük)

           ### YA DA ###
  
harfli_sözlük = dict()
for i in  range(len(harfler)):
	harfli_sözlük[harfler[i]] = i
print(harfli_sözlük)
```
**Output:**
```
{'a': 0, 'b': 1, 'c': 2, 'ç': 3, 'd': 4, 'e': 5,
 'f': 6, 'g': 7, 'ğ': 8, 'h': 9, 'ı': 10, 'i': 11,
 'j': 12, 'k': 13, 'l': 14, 'm': 15, 'n': 16,
 'o': 17, 'ö': 18, 'p': 19, 'r': 20, 's': 21,
 'ş': 22, 't': 23, 'u': 24, 'ü': 25, 'v': 26,
 'y': 27, 'z': 28}

{'a': 0, 'b': 1, 'c': 2, 'ç': 3, 'd': 4, 'e': 5,
 'f': 6, 'g': 7, 'ğ': 8, 'h': 9, 'ı': 10, 'i': 11,
 'j': 12, 'k': 13, 'l': 14, 'm': 15, 'n': 16,
 'o': 17, 'ö': 18, 'p': 19, 'r': 20, 's': 21,
 'ş': 22, 't': 23, 'u': 24, 'ü': 25, 'v': 26,
 'y': 27, 'z': 28}
```
Üreteç versiyonu:
```py
harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
harfli_sözlük = {i: harfler.index(i) for i in harfler}
print(harfli_sözlük)
```
**Output:**
```
{'a': 0, 'b': 1, 'c': 2, 'ç': 3, 'd': 4, 'e': 5,
 'f': 6, 'g': 7, 'ğ': 8, 'h': 9, 'ı': 10, 'i': 11,
 'j': 12, 'k': 13, 'l': 14, 'm': 15, 'n': 16,
 'o': 17, 'ö': 18, 'p': 19, 'r': 20, 's': 21,
 'ş': 22, 't': 23, 'u': 24, 'ü': 25, 'v': 26,
 'y': 27, 'z': 28}
```

**Not:** `[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]` bunun gibi bir yapıyı `{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}` bunun gibi bir sözlüğe doğrudan dönüştürülerbilir. Örnek:
```py
a = [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]
b = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
c = dict(a)

print(b, c, sep="\n")
```
**Output:**
```
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

# Dictionary'lerde İşlemler
Bir diçtionary'nin bir öğesine erişmek için index kullanamazsınız çünkü dictionary'lerde *sıra* denen kavram yoktur. Bir diçtionary'nin bir öğesine erişmek için aşağıdaki syntax'ı kullanabilirsiniz:
```py
d1 = {'ahmet': 5, 'mehmet': 6, 'fırat': 5}
print(d1["ahmet"]) # Output: 5
```
İç içe sözlüklerde de aşağıdaki syntax kullanılır:
```py
d1 = {'ahmet': {"yas": 30, "boy": 180}, 'mehmet': {"yas": 40, "boy": 140}}
print(d1["ahmet"]["yas"]) # Output: 30
```
Bir sözlük üzerinde `for` loop kullandığınızda, `for` loop, sözlüğün `key` kısmını alır. Örnek:
```py
d1 = {'ahmet': 5, 'mehmet': 6}
for i in d1:
	print(f"key: {i}", f"value: {d1[i]}", sep="\n", end="\n\n")
```
**Output:**
```
key: ahmet
value: 5

key: mehmet
value: 6
```
**Not: ** Sözlük içinde bulunmayan bir öğreye erişmek istediğinizde, Python, `KeyError` hatası verir.

Bir dictionary'ye öğe eklemek için aşağıdaki işlemi kullanabilirsiniz:
```py
sözlük = {"bir": 1, "iki": 2}
sözlük["üç"] = 3
print(sözlük)
# Output: {'bir': 1, 'iki': 2, 'üç': 3}
```
**Not:** Bu yöntemle bir sözlüğe yeni bir öğe eklemek istediğinizde, eğer o öğe zaten sözlükte mevcutsa, o öğenin value'sini değiştirir, yeni bir öğe olarak eklemez. Benzer şekilde, bir sözlük oluştururken aynı key'i iki kere tanımlarsanız, en son tanımladığınız değer dikkate alınır. Yani:
```py
sözlük = {"bir":"1", "bir":5, "iki":"2", "üç": "3"}
print(sözlük) # Output: {'bir': 5, 'iki': '2', 'üç': '3'}
```
Gördüğünüz gibi `"bir"`'in değeri en son `5` olarak tanımlandığu için Python bu değeri dikkate aldı.

**Not:** Belli değerleri bir liste içinde (örneğin `[20, 175, "eyüp"]` gibi) depolayıp, sonradan bu değerlere ihtiyacınız olduğunda listeden çekip kullanmak yerine, bu değerleri, ne olduklarıyla birlikte (`["yaş":20, "boy":175, "isim":"eyüp"]` gibi) bir dictionary'de depolarsanız, daha pratik ve kullanışlı olur.

- Belli bir yapıda sıralanmış bilgileri bir listede [20, 175, "eyüp"] gibi tutup sonradan bu listeden çekip kullanmak yerine, ["yaş":20, "boy":175, "isim":"eyüp"] gibi dict'lerde depolayın. Böylece daha kolay çekip kullanabilirsiniz.

# Dictionary Methodları

## `keys()` Methodu
Sözlüklerde `{key: value}` syntax'ındaki `key` kısmını temsil eder. Bir sözlüğün sadece `key` kısmını almak istenildiğinde kullanılan bir methoddur. Bu method kullanıldığında bir `dict_keys` nesnesi verir. Bu nesneyi kullanabilmek için `list`, `tuple` veya `join()` methoduyla `str`'ye dönüştürüp bir değişkene atayabilirsiniz. Ama `join()` methodunu kullanırken, bütün `key`'lerin aynı string data type'ına sahip olduğundan emin olun.

**Not:** `str()` fonksiyonu, `list()` veya `tuple()` fonksiyonlarının aksine sözlükteki key'lerin nasıl bir ölçüte göre karakter dizisine çevrileceğine dair bir kural içermez. Bu yüzden direkt `str()` fonksiyonunu değil, `join()` methodunu kullanmaya özen gösterin. Eğer `str()` fonksiyonunu kullanırsanız, `print(sözlük.keys())` ile aynı outputu alırsınız.
```py
harfler = "abcde"
sözlük = {i: harfler.index(i) for i in harfler}
print("native keys: ", sözlük.keys())
print("str: ", str(sözlük.keys()))

print("list: ", list(sözlük.keys()))
print("tuple: ", tuple(sözlük.keys()))
```
**Output:**
```
native keys :  dict_keys(['a', 'b', 'c', 'd', 'e'])
str         :  dict_keys(['a', 'b', 'c', 'd', 'e'])
list        :  ['a', 'b', 'c', 'd', 'e']
tuple       :  ('a', 'b', 'c', 'd', 'e')
```

## `values()` Methodu
Sözlüklerde `{key: value}` syntax'ındaki `value` kısmını temsil eder. Bir sözlüğün sadece `value` kısmını almak istenildiğinde kullanılan bir methoddur. Bu method kullanıldığında bir `dict_values` nesnesi verir. Bu nesneyi kullanabilmek için `list`, `tuple` veya `join()` methoduyla `str`'ye dönüştürüp bir değişkene atayabilirsiniz. Ama `join()` methodunu kullanırken, bütün `key`'lerin aynı string data type'ına sahip olduğundan emin olun.

**Not:** `str()` fonksiyonu, `list()` veya `tuple()` fonksiyonlarının aksine sözlükteki value'larin nasıl bir ölçüte göre karakter dizisine çevrileceğine dair bir kural içermez. Bu yüzden direkt `str()` fonksiyonunu değil, `join()` methodunu kullanmaya özen gösterin. Eğer `str()` fonksiyonunu kullanırsanız, `print(sözlük.values())` ile aynı outputu alırsınız.
```py
harfler = "abcde"
sözlük = {i: harfler.index(i) for i in harfler}
print("native values: ", sözlük.value())
print("str: ", str(sözlük.value()))

print("list: ", list(sözlük.value()))
print("tuple: ", tuple(sözlük.value()))
```
**Output:**
```
native values :  dict_values(['0', '1', '2', '3', '4'])
str			  :  dict_values(['0', '1', '2', '3', '4'])
list		  :  ['0', '1', '2', '3', '4']
tuple		  :  ('0', '1', '2', '3', '4')
```

## `items()` Methodu
Sözlüklerde `{key: value}` syntax'ındaki `key` ve `value` kısmını temsil eder. Bir sözlüğün sadece hem `key` hem `value` kısmını almak istenildiğinde kullanılan bir methoddur. Bu method kullanıldığında bir `dict_items` nesnesi verir. Bu nesneyi kullanabilmek için `list` ya da `tuple` fonksiyonlarını kullanabilirsiniz. Her bir item bir tuple içinde saklanır. Örnek:
```py
harfler = "abc"
sözlük = {i: harfler.index(i) for i in harfler}
print("native values: ", sözlük.values())
print("str: ", str(sözlük.values()))

print("list: ", list(sözlük.values()))
print("tuple: ", tuple(sözlük.values()))
```
**Output:**
```
native values :  dict_items([('a', 0), ('b', 1), ('c', 2)])
str			  :  dict_items([('a', 0), ('b', 1), ('c', 2)])
list		  :  [('a', 0), ('b', 1), ('c', 2)]
tuple		  :  (('a', 0), ('b', 1), ('c', 2))
```

## `get(key, "string")` Methodu
Bir sözlükte `key` parametresine girilen değerin sözlük içinde bulunan `key`'lerden biri olup olmadığını sorgular. `key`'e girilen değer dözlükte varsa, o `key`'e karşılık gelen `value`'yi döndürür, yoksa `"string"`'i döndürür.
```py
sözlük = {'a': 0, 'b': 1, 'c': 2}
print(sözlük.get("a", "yok")) # Output: 0
print(sözlük.get("d", "yok")) # Output: yok
```

## `clear()` Methodu
Kullanıldığı sözlüğün içini boşaltır. `del` kullanarak da silinebilir ama `del` kullanılırsa sözlük objesi de silinir ama `clear()` methodu kullanılırsa sözlük objesi silinmeden içi boşaltılır.
```py
sözlük = {'a': 0, 'b': 1, 'c': 2}
sözlük.clear()
print(sözlük) # Output: {}
```

## `copy()` Methodu
Uygulandığı sözlüğün farklı ID'ye sahip bir kopyasını oluşturur. Bu sayede yeni sözlük ile eski sözlük birbirinden bağımsız olur. Sözlük kopyalama işlemi `sözlük1 = sözlük2` şeklinde yapılırsa, `sözlük1` ve `sözlük2` objelerinin ID'leri aynı olacağı için listelerde olduğu gibi, birinde yapılan işlem diğerini de etkiler. Bu yüzden `copy()` methodu kullanılır.
```py
sözlük1 = {'a': 0, 'b': 1, 'c': 2}
sözlük2.copy(sözlük1)
print(f"sözlük2: {sözlük2}", f"sözlük1 ID: {id(sözlük1)}", f"sözlük2 ID: {id(sözlük2)}", sep="\n")
```
**Output:**
```
sözlük2: {'a': 0, 'b': 1, 'c': 2}
sözlük1 ID: 2271871328320
sözlük2 ID: 2271871311296
```
## `fromkeys(key, value = "None")` Methodu
Yeni bir sözlük oluşturmak için kullanılır. `key` parametresine aldığı `list`, `tuple`, `set`, `string` ya da `dictionary` kullanarak, oluşturacağı listenin `keys` kısmını belirler. `string` değer kullanılırsa, string'in her bir index'i bir key'e dönüştürülür. `value` kısmı isteğe bağlıdır (optional). Default değeri `None`'dır. Buraya girilen herhangi bir data type' bütün key'lerin value'si olur.
```py
sözlük = dict()

key1 = "abc"
key2 = ["a","b","c"]
key3 = ("a","b","c")
key4 = {"a","b","c"}
key5 = {"a": None,"b": None,"c": None}

value1 = "abc"
value2 = ["a","b","c"]
value3 = ("a","b","c")
value4 = {"a","b","c"}
value5 = {"a": None,"b": None,"c": None}
print(sözlük.fromkeys(key1,value1),
	  sözlük.fromkeys(key2,value2),
	  sözlük.fromkeys(key3,value3),
	  sözlük.fromkeys(key4,value4),
	  sözlük.fromkeys(key5,value5),
	  sep="\n")
```
**Output:**
```
{'a': 'abc', 'b': 'abc', 'c': 'abc'}
{'a': ['a', 'b', 'c'], 'b': ['a', 'b', 'c'], 'c': ['a', 'b', 'c']}
{'a': ('a', 'b', 'c'), 'b': ('a', 'b', 'c'), 'c': ('a', 'b', 'c')}
{'b': {'b', 'a', 'c'}, 'a': {'b', 'a', 'c'}, 'c': {'b', 'a', 'c'}}
{'a': {'a': None, 'b': None, 'c': None}, 'b': {'a': None, 'b': None, 'c': None}, 'c': {'a': None, 'b': None, 'c': None}}
```

## `pop(key, "string")` Methodu
Sözlükten eleman silmek için kullanılır. Silinen key'in value'sini döndürür. Silmek istenilen eleman, `key` parametresine girilir.
```py
sözlük = {'a': 0, 'b': 1, 'c': 2}
print(sözlük.pop("a")) # Output: 0
```
`key`'e girilen eleman sözlükte yoksa ve `"string"` parametresi tanımlanmamışsa, `KeyError: 'key'` hatası yükseltir.
```py
sözlük = {'a': 0, 'b': 1, 'c': 2}
print(sözlük.pop("d")) # Output: KeyError: 'd'
```
`key`'e girilen eleman sözlükte yoksa ve `"string"` parametresi tanımlanmışsa, `"string"` parametresine tanımlanan değer döndürülür.
```py
sözlük = {'a': 0, 'b': 1, 'c': 2}
print(sözlük.pop("d", "yok")) # Output: yok
```

## `popitem()` Methodu
`pop()` methodunun benzer çalışır. Parametresiz kullanılır. **Last In, First Out** (LIFO) mantığıyla çalışır. Bu mantığa dayanarak, sözlüğe en son eklenen `item`'i döndürür ve döndürülen `item`'i sözlükten kaldırır. Eğer sözlük boşsa, `KeyError` hatası verir. Python 3.7'den önce bu döndürme ve kaldırma işlemini rastgele yapardı.
```py
sözlük = {'a': 0, 'b': 1, 'c': 2}
print(sözlük.popitem(), sözlük, sep="\n")
```
**Output:**
```
('b', 1)
{'a': 0, 'c': 2}
```

## `setdefault(key, value = "None")` Methodu
Sözlük içinde arama yapar. `key` parametresinde belirtilen `key` sözlükte varsa, o `key`'e aite value'yi döndürür. `key` parametresinde belirtilen `key` sözlükte yoksa, o `key`'i sözlüğe ekler. Eklediği key'in value'si default `None` olarak ayarlıdır. `value` parametresi girilirse, değer `None` yerine bu parametreye girilen değer olur.
```py
sözlük = {'a': 0, 'b': 1, 'c': 2}
print(sözlük.setdefault("a"))
print(sözlük.setdefault("d", 3), sözlük, sep="\n")
```
**Output:**
```
0
3
{'a': 0, 'b': 1, 'c': 2, 'd': 3}
```

## `update(dict)` Methodu
`dict1.update(dict2)` syntax'ına sahiptir. Bu syntax'a göre, `dict1`'i, `dict2`'ye göre günceller.
```py
sözlük = {'a': 0, 'b': 1, 'c': 2}
sözlük2 = {'a': 10, 'b': 11, 'c': 12}
sözlük.update(sözlük2)
print(sözlük) # Output: {'a': 10, 'b': 11, 'c': 12}
```