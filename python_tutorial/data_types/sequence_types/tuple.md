# İçindekiler

- [# Demet (Tuple)](#1)
    - [Tuple'larda İşlemler](#1.1)
    - [Tuple Üreteçleri (Tuple Comprehensions)](#1.2)
    - [Tuple Methodları](#1.3)
        - [`index(value, start, stop)` Methodu](#1.3.1)
        - [`count(value)` Methodu](#1.3.2)

<h1 id="1">Demetler (Tuples)</h1>

Tuple'lar değiştirilemez (immutable) data type'dır. Bu yüzden bir Tuple'ı değiştirmek için onu yeniden tanımlamak (redefinition) gerekir. Tuple'lar genellikle değiştirilmesini istemediğiniz verileri saklarken kullanılır. `tuple(iterable)` build'in fonksiyonu ile tuple oluşturabilirsiniz veya uygun objeleri tuple'a dönüştürebilirsiniz. Listeler normal parantez (`()`) ile ifade edilir. Örnek:
```py
t1 = ()
t2 = tuple()
t3 = ("string",
	  1, 1.5, 15+5j,
	  ("tuple", "Tuple"),
	  ["liste", "Liste"],
	  {"set", "Set"},
	  {"Sözlük": "dictionary"})
      
print(t1,t2,t3,sep="\n")
```
**Output:**
```
()
()
('string', 1, 1.5, (15+5j), ('tuple', 'Tuple'), ['liste', 'Liste'], {'set', 'Set'}, {'Sözlük': 'dictionary'})
```
Python'da parantez operator'ı, içine aldığı şeyin öncelliğini arttırmak için kullanıldığı için tek öğeli tuple tanımlarken sorun yaşayabilirsiniz. Örnek:
```py
t1 = ("item 1")
print(type(t1)) # Output: <class 'str'>
```
Gördüğünüz gibi burada bir tuple değil bir string objesi tanımlamış olduk. String yerine herhangi bir şey olsa da aynı durumla karşılaşacaktınız. Çözümü:
```py
t1 = ("item 1",)
t2 = "item 1",
t3 = tuple("item 1")
print(type(t1), type(t2), type(t3)) # Output: <class 'tuple'> <class 'tuple'> <class 'tuple'>
```
Gördüğünüz gibi öğeden sonra bir adet virgül operator'ı koyarak tuple belirtmiş olduk. Bunun yerine yukarıdaki gibi `tuple(iterable)` build'in fonksiyonunu da kullanabilirsiniz.

<h2 id="1.1">Tuple'larda İşlemler</h2>

Bir tuple'ı dilimlerken `tuple_exp[Başlama index'i : bitiş index'i : atlama değeri]` syntax'ı kullanılır. Örnekler:
```py
a = (0,1,2,3,4,5,6,7,8,9)

# 4. index'ten başlar, (9. index'i dahil etmeden) 9. index'e kadar tuple'i yazdırır.
print(a[4:9]) # Output: (4, 5, 6, 7, 8)

# Başlangıç index'i belirtilmediği için en baştan (0. index'ten) başlar, (9. index'i dahil etmeden) 9. index'e kadar tuple'i yazdırır.
print(a[:9]) # Output: (0, 1, 2, 3, 4, 5, 6, 7, 8)

# Bitiş index'i belirtilmediği için 4. indexten başlar, en son index'e kadar tuple'i yazdırır.
print(a[4:]) # Output: (4, 5, 6, 7, 8, 9)

# Başlangıç ve bitiş intex'i belirtilmediği için tüm tuple'i yazdırır.
print(a[:]) # Output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Başlangıç index'i belirtilmediği için en baştan (0. index'ten) başlar, (-1. index'i dahil etmeden) -1. index'e kadar (sonran bir önceki index) tuple'i yazdırır.
print(a[:-1])# Output: (0, 1, 2, 3, 4, 5, 6, 7, 8)

# Baştan sona index atlamadan tuple'i yazdırır.
print(a[::1]) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Baştan sona 1 index atlaya atlaya tuple'i yazdırır.
print(a[::2]) # Output: (0, 2, 4, 6, 8)

# 4. index'ten başlar, (9. index'i dahil etmeden) 9. index'e kadar 2 index atlaya atlaya tuple'i yazdırır.
print(a[0:9:3]) # Output: (0, 3, 6)

# Sondan başa index atlamadan tuple'i yazdırır. (tuple'i ters çevirme)
print(a[::-1]) # Output: (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
```

Tuple'ların öğe sayısına `len()` fonksiyonuyla ulaşılabilir. Örnek:
```py
t1 = (1,2,3,4,5)
print(len(t1)) # Output: 5
```

Tuple'larda aritmetik (sayısal) işlemler yapılabilir. Örnek:
```py
print((1,2,3) + (4,5,6)) # Output: (1, 2, 3, 4, 5, 6)
print((1,2,3) * 2) # Output: (1, 2, 3, 1, 2, 3)
```
Bir Tuple'a öğe eklemek için addition (toplama `+`) operator'ını kullanarak öğe ekleyebilirsiniz. Bu durum yeniden tanımlama (redefinition) işlemi olduğu için ve tuple değiştirilemez (immutable) data type olduğu için bu işlemden sonra eski tuple ile yeni tuple birbirinden farklı (ID'leri farklı) iki obje olacaktır. Örnek:
```py
t1 = ("item 1", "item 2")
id_1 = id(t1)
t1 += ("item 2",)
id_2 = id(t1)
print((id_1 == id_2)) # Output: False
```

Diğer iterable objeleri `tuple()` fonksiyonu ile tuple type'a dönüştürebilirsiniz. Örnek:
```py
print(tuple(range(0,4))) # Output: (0, 1, 2, 3)
print(tuple([0,1,2,3])) # Output: (0, 1, 2, 3)
print(tuple({0,1,2,3})) # Output: (0, 1, 2, 3)
print(tuple("0123")) # Output: ('0', '1', '2', '3')
```

Öğe sayısını bilmediğiniz tuple'ların son öğesine ulaşmak için iki yöntem:
```py
t1 = (0,1,2,3,4)
print(t1[len(t1)-1]) # Output: 4
print(t1[-1]) # Output: 4
```

Tuple objesini tamamen silmek:
```py
t1 = (1,2,3,4)
del t1
print(t1) # NameError: name 't1' is not defined
```

Bir listeyi kopyalamak ve sonuçları:
```py
t1 = (1,2,3,4)
t2 = t1
print(t1) # Output: (1, 2, 3, 4)
print(t2) # Output: (1, 2, 3, 4)
print(id(t1) == id(t2)) # Output: True
```

Bir tuple içine tanımlanmış diğer index'lenebilir iterable objelerin index'lerine de erişebiliriz. Örnek:
```py
t1 = ("string",
	  ("tuple", "Tuple"),
	  ["liste", "Liste"],
	  {"Sözlük": "dictionary"})

print(t1[0][3])        # Output: i
print(t1[1][0])        # Output: tuple
print(t1[2][1])        # Output: Liste
print(t1[3]["Sözlük"]) # Output: dictionary
```
`obje[index][index]` yapısını çalışma mantığını daha önce anlattığım için bildiğiniz yerleri atlayabilirsiniz:
- Python `a[b][c]` yapısını soldan sağa okumaya başladığı için önce `a[b]` kısmını okur ve `a` objesinin `b` index'ine gider ve böylece `a[b]` kodu, `a` objesinin `b` index'indeki objeye atıfta bulunmuş olur. Bu objeye `x` diyelim.
- Bu işlemden sonra `a[b][c]` kodu Python'un gözünde `x[c]` koduna dönüşür. Python `x[c]` kodu içinde aynı işlemleri yapar.
- Python'u LEGO gibi düşünün. Kodları bütün olarak değil, parça parça yorumlayın. Böylelikle Python'un çalışma mantığını anlarsınız. Örneğin aşağıdaki iki kod tamamen aynı işi yapmaktadır:
    ```py
    t1 = ((((1,2), (3,4)), ((5,6), (7,8))), (((9,10), (11,12)), ((13,14), (15,16))))

    a1 = t1[0]
    a2 = a1[0]
    a3 = a2[0]
    a4 = a3[0]
    print(a4) # Output: 1

    print(t1[0][0][0][0]) # Output: 1
    ```

**Tuple'ların listelerden bazı farkları:** Bir tuple'ın herhangi bir index'indeki öğesini başka bir şeyler değiştiremezsin veya silemezsin çünkü tuple'lar değiştirilemez (immutable) bir data type olduğu için listelerdeki gibi parça ekleme/çıkarma/silme işlemlerini desteklemez. Aşağıdaki örneklerdeki hata mesajlarında bu duruma vurgu yapılmış zaten:
```py
t1 = (1,2,3,4)
print(t1)
t1[1] = 0 # TypeError: 'tuple' object does not support item assignment
print(t1)

t1 = (1,2,3,4)
print(t1)
t1[:] = 5,6,7,8 # TypeError: 'tuple' object does not support item assignment
print(t1)

t1 = (1,2,3,4)
del t1[:]
print(t1) # TypeError: 'tuple' object does not support item deletion

t1 = (1,2,3,4)
del t1[0] # TypeError: 'tuple' object doesn't support item deletion
print(t1)
```


<h2 id="1.2">Tuple Üreteçleri (Tuple Comprehensions)</h2>

**Comprehension**, tek satırda oluşturduğumuz **Generator** (daha sonra anlatılacak) yapısına verilen isimdir. `(expression for item in iterable)` syntax'ına sahiptir (parantezler dahil). Bu generator yapısı (**Generator Comprehension**) bir generator objesi oluşturmakta kullanılır. Daha sonra bu generator objesini tuple type'a dönüştürerek Tuple Comprehension oluşturabiliriz. Örnek:
```py
tuple_exp = tuple(i for i in range(1,4))
print(tuple_exp) # Output: (1, 2, 3)
```
Burada `(i for i in range(1,4))` yerine `tuple(i for i in range(1,4))` kullanmamızın nedenini daha önce tek öğeli tuple oluşturma kısmında anlattım. Bu konu daha sonra comprehension başlığı altında daha detaylı anlatılacak.

<h2 id="1.3">Tuple Methodları</h2>

<h3 id="1.3.1"><code>index(value, start, stop)</code> Methodu</h3>

`value` parametresine argüman olarak girdiğiniz value'nun, uygulandığı tuple içinde ilk kaçıncı index'de bulunduğunu söyler. `start` ve `stop` parametrelerine gireceğiniz integer argümanlarla, `index` methodunun hangi index'ler arasında arama yaparcağını belirleyebilirsiniz. Örnek:
```py
t1 = ("a", ("b", "c"), "a")
print(t1) # Output: ('a', ('b', 'c'), 'a')
print(t1.index("a")) # Output: 0
print(t1.index("a", 2)) # Output: 2
print(t1.index(("b", "c"))) # Output: 1
```

<h3 id="1.3.2"><code>count(value)</code> Methodu</h3>

`value` parametresine argüman olarak girdiğiniz value'nun, uygulandığı tuple içinde kaç kere geçtiğini söyler. Nested tuple'larda eksik sonuç verebilir çünkü nested tuple'ı görmez. Örnek:
```py
t1 = ("a","b",("a",),"c")
print(t1.count("a")) # Output: 1
```