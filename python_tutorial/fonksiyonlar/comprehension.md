# İçindekiler

- [Comprehension](#1)
    - [Sequence Comprehension](#1.1)
    - [Dictionary Comprehension](#1.1)

<h1 id="1">Comprehension</h1>

**Comprehension**, tek satırda oluşturduğumuz generator objesine verilen isimdir.
- Sequence (list, tuple vb.) Comprehension
- Dictionary Comprehension

gibi çeşit çeşit comprehension vardır. Generator comprehension bunların en temelidir. Diğer bütün comprehension'lar, generator comprehension objesinin type'ının değiştirilmesi sonucu oluşturulmuştur. Örnek:
```py
var1 = (i for i in range(1,4)) # Generator Comprehension
var2 = list(i for i in range(1,4)) # List Comprehension
var3 = tuple(i for i in range(1,4)) # Tuple Comprehension
var4 = {(i):(i**2) for i in range(1,4)} # Dict Comprehension
print(var1,var2,var3,var4,sep="\n")
```
**Output:**
```
<generator object <genexpr> at 0x0000021160412120>
[1, 2, 3]
(1, 2, 3)
{1: 1, 2: 4, 3: 9}
```

Generator comprehension `(expression for item in iterable)` syntax yapısı ile oluşturulur (parantezler dahil). Örnek:
```py
generator_exp1 = (i for i in range(1,4))

def generator_exp2():
    for i in range(1,4):
        yield i

print(generator_exp1) # Output: <generator object <genexpr> at 0x000001B1B59B2120>
print(generator_exp2()) # Output: <generator object generator_exp2 at 0x000001B1B59D6D60>

for i in generator_exp1:
    print(i, end=" ") # Output: 1 2 3

for i in generator_exp2():
    print(i, end=" ") # Output: 1 2 3
```
Generator Comprehension yapısı `<genexpr>` adında bir obje döndürür. `def` statement ile tanımladığımız fonksiyondan istediğimiz kadar generator objesi oluşturabildiğimiz gibi generator comprehension yapısı ile istediğimiz kadar generator objesi oluşturamayız. generator comprehension yapısı ile sadece 1 tane generator objesi oluşturabiliriz. Bu yüzden bu `<genexpr>` objesini bir kere kullanıp yineleyebiliriz.

**Not:** Comprehension'larda `(expression for item in iterable)` syntax'ındaki `expression` kısmı, `yield` statement'a karşılık gelmektedir.

<h2 id="1.1">Sequence Comprehension</h2>

Bir generator comprehension objesini sequence type'lara dönüştürebiliriz. Bu işlem sonucunda sequence type (`list`, `tuple` vb.) bir obje oluşur. Bu yöntemle üretilen sequence objeleri `list`, `tuple` vb. type objeler (örnek: `[1,2,3]`, `(1,2,3)`) olarak karşımıza çıksa bile literatürde List Comprehension, Tuple Comprehension vb. olarak bahsedilir. `list` ve `tuple` comprehension benzer oldukları için bu kısımda bütün örnekleri list comprehension üzerinden vereceğim.

List comprehension `[expression for item in iterable]` syntax yapısı ile veya `list(expression for item in iterable)` type dönüşümü yapılarak oluşturulur (parantezler dahil). Örnek:
```py
a = list((i**2) for i in range(1,4))
b = [(i**2) for i in range(1,4)]
print(a) # Output: [1, 4, 9]
print(b) # Output: [1, 4, 9]
```

**Not:** Yukarıdaki yöntemler arasında `[expression for item in iterable]` syntax yapısını kullanmak en sağlıklısıdır.

**Not:** `((i**2) for i in range(1,4))` yapısı generator comprehension oluşturduğu için `tuple` comprehension oluşturmak için type dönüşümü (`tuple((i**2) for i in range(1,4))`) yapmanız gerekmektedir.

Comprehension yapısını tek satırda tanımlanan `if` - `else` ile birlikte kullanabilirsin. Ama bu yapıyı oluştururken dikkatli olmalısınız. Kolayca hata yapılabilir. Hatalı örnek:
```py
generator_exp = [i*10 for i in range(10) if i%2==0 else i*100 for i in range(10)]
```
Bu yapıda `else` kısmı `SyntaxError: invalid syntax` hatası döndürür. Doğrusu:
```py
generator_exp = [i*10 if i%2==0 else i*100 for i in range(10)]
print(generator_exp) # Output: [0, 100, 20, 300, 40, 500, 60, 700, 80, 900]
```
Bu yapıyı `[(i*10 if i%2==0 else i*100) for i in range(10)]` şeklinde düşünün. `[expression for item in iterable]` yapısındaki `expression` kısmına `if` - `else` yapısı tanımlanıyor.

Comprehension yapısı bir koşula göre oluşsun (sadece `if` statement kullanmaktan bahsediyorum) diyorsanız `[expression for item in iterable if conditional]` syntax yapısını kullanabilirsiniz. Örnek:
```py
generator_exp = [i*10 for i in range(10) if i%2==0]
print(generator_exp) # Output: [0, 20, 40, 60, 80]
```
Yukarıdaki comprehension yapısı aşağıdaki anlama gelmektedir:
```py
def generator():
    for i in range(10):
        if i%2 == 0:
            yield i*10

generator_exp = list(generator())
print(generator_exp) # Output: [0, 20, 40, 60, 80]
```
`[(if - else) for item in iterable]` yapısı ile `[expression for item in iterable if conditional]` yapısı birlikte kullanılabilir. Örnek:
```py
generator_exp = [i*50 if i == 4 else i*2 for i in range(10) if i%2 == 0]
print(generator_exp) # Output: [0, 4, 200, 12, 16]
```

Comprehension yapısını nested olarak da kullanabilirsiniz. Örnek:
```py
# Nested liste objesi oluşturma (`def` statement ile)

def generator1():
    for i in range(3):
        def generator2():
            for j in range(3):
                yield j
        yield list(generator2())

liste1 = list(generator1())
print(liste1) # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

def generator3():
    for i in range(3):
        def generator4():
            for j in range(3):
                yield i
        yield list(generator4())

liste2 = list(generator3())
print(liste2) # Output: [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
```
```py
# Nested liste objesi oluşturma (nested comprehension ile)

liste1 = [[j for j in range(3)] for i in range(3)]
print(liste1) # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

liste2 = [[i for j in range(3)] for i in range(3)]
print(liste2) # Output: [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
```
`[expression for item in iterable]` yapısının bir comprehension yapısı olduğunu biliyorsunuz. Bu yapı iç içe `[[expression for item in iterable] for item in iterable]` örneğindeki gibi kullanılırsa nested comprehension oluyor çünkü gördüğünüz gibi biri birinin kod block'una tanımlanmış iki list comprehension var.

Comprehension yapısındaki for loop'lar birbiri ardına eklenince ortaya başka bir özellik çıkıyor. Örnek:
```py
# Nested bir listeyi ayrıştırmak (`def` statement ile)

def generator(p1):
    for i in p1:
        for j in i:
            for k in j:
                yield k

main_list = [[[1,2], [3,4,5], [6]], [[7,8,9,10], [11,12]], [[13,14,15], [16], [17,18],[19,20]]]
flatten_list = list(generator(main_list))
print(flatten_list) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
```
```py
# Nested bir listeyi ayrıştırmak (comprehension ile)

main_list = [[[1,2], [3,4,5], [6]], [[7,8,9,10], [11,12]], [[13,14,15], [16], [17,18],[19,20]]]

flatten_list = [k for i in main_list for j in i for k in j]
print(flatten_list) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
```
Buradaki `[k for i in main_list for j in i for k in j]` yapısını nested comprehension değildir. Bu yapıyı anlamak için:
- Bu yapıyı `[(k) (for i in main_list) (for j in i) (for k in j)]` olarak düşünürsek, `for i in main_list` enclosing, diğerleri soldan sağa doğru nested `for` loop oluyor. Yani soldan sağa doğru nested'lık artıyor.

- En sağdaki for loop'un item'ı (`[expression for item in iterable]`), en baştaki expression'ı temsil eder. Örneğin en sağdaki `for k in j` loop'un `k` item'i, en soldaki `k`'yı temsil eder.

- Bu yapıyla `if` - `else` veya sadece `if` veya ikisini birden kullanabilirsiniz. Örnek:
    ```py
    main_list = [[[1,2], [3,4,5], [6]], [[7,8,9,10], [11,12]], [[13,14,15], [16], [17,18],[19,20]]]

    flatten_list1 = [k for i in main_list for j in i for k in j if k%2==0] # sadece `if`
    print(flatten_list1) # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    flatten_list2 = [k*10 if k%2==0 else k for i in main_list for j in i for k in j] # sadece `if - else`
    print(flatten_list2) # Output: [1, 20, 3, 40, 5, 60, 7, 80, 9, 100, 11, 120, 13, 140, 15, 160, 17, 180, 19, 200]

    flatten_list = [k*10 if k==10 else k for i in main_list for j in i for k in j if k%2==0] # `if` ve `if - else` birlikte
    print(flatten_list) # Output: [2, 4, 6, 8, 100, 12, 14, 16, 18, 20]
    ```

**Not:** Liste objelerinde nested'lik ile bu listeye erişen list comprehension objelerindeki `for` loop sayısı doğru orantılıdır. Yani bir liste objesi 2 katman (Oreneğin `[[1,2], [3,4]]`) nested ise, bu listeye erişen list comprehension objelerindeki `for` loop (Örneğin `j for i in liste for j in i`) sayısı da 2 olmalıdır. Bunu [`while`-`for` Döngüleri (Loops)](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/statements/while-for_loops.md "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/statements/while-for_loops.md") bölümünde anlatmıştım. `[0, [1, 2, 3], [4, 5], [6, 7, 8, 9]]` gibi listeler üzerinde `[j for i in liste for j in i]` işlemi yapamazsınız çünkü `0` öğesi nested'lığı bozuyor.

Python'ın dinamik yapısı sayesinde comprehension yapısını kullanarak çeşit çeşit algoritmalar uydurabilirsiniz. Örnek:
```py
# Nested bir listeden başka bir nested liste yaratmak (`def` statement ile)

def generator1(p1):
    for i in range(len(p1[0])):
        def generator2():
            for j in p1:
                yield j[i]
        yield list(generator2())

main_list = [[1, 2, 3, 4], [5, 6, 7, 8]]
liste = list(generator1(main_list))
print(liste) # Output: [[1, 5], [2, 6], [3, 7], [4, 8]]

main_list = [[1, 2], [3, 4], [5, 6], [7, 8]]
liste = list(generator1(main_list))
print(liste) # Output: [[1, 3, 5, 7], [2, 4, 6, 8]]
```
```py
# Nested bir listeden başka bir nested liste yaratmak (comprehension ile)

main_list = [[1, 2, 3, 4], [5, 6, 7, 8]]
liste = [[j[i] for j in main_list] for i in range(len(main_list[0]))]
print(liste) # Output: [[1, 5], [2, 6], [3, 7], [4, 8]]

main_list = [[1, 2], [3, 4], [5, 6], [7, 8]]
liste = [[j[i] for j in main_list] for i in range(len(main_list[0]))]
print(liste) # Output: [[1, 3, 5, 7], [2, 4, 6, 8]]
```

<h2 id="1.2">Dictionary Comprehension</h2>

Bir generator comprehension objesini dictionary type'a dönüştürebiliriz. Bu işlem sonucunda dictionary type bir obje oluşur. Bu yöntemle üretilen dictionary objeleri `dict` type objeler (örnek: `{1:1, 2:2, 3:3}` olarak karşımıza çıksa bile literatürde Dictionary Comprehension olarak bahsedilir.

Dictionary comprehension `{item:item for item in iterable}` veya `dict((item,item) for item in iterable)` type dönüşümü yapılarak oluşturulur (parantezler dahil). Örnek:
```py
dict_generator_exp = {i:i**2 for i in range(1,4)}
print(dict_generator_exp) # Output: {1: 1, 2: 4, 3: 9}

dict_generator_exp = dict((i,i**2) for i in range(1,4))
print(dict_generator_exp) # Output: {1: 1, 2: 4, 3: 9}
```
Yukarıdaki `(i,i**2) for i in range(1,4)` kodunun `def` statement ile tanımlanmış versiyonu:
```py
def generator():
    for i in range(1,4):
        yield (i,i**2)

dict_generator_exp = dict(generator())
print(dict_generator_exp) # Output: {1: 1, 2: 4, 3: 9}
```
`{i:i**2 for i in range(1,4)}` kodunun `def` statement ile tanımlanmış versiyonu yok. Varsa da ben bilmiyorum.

**Not:** Yukarıdaki yöntemler arasında `{item:item for item in iterable}` syntax yapısını kullanmak en sağlıklısıdır.

Comprehension yapısını tek satırda tanımlanan `if` - `else` ile birlikte kullanabilirsin. Ama bu yapıyı oluştururken dikkatli olmalısınız. Kolayca hata yapılabilir. Hatalı örnek:
```py
generator_exp = {i:i*10 for i in range(10) if i%2==0 else i*100 for i in range(10)}
```
Bu yapıda `else` kısmı `SyntaxError: invalid syntax` hatası döndürür. Doğrusu:
```py
generator_exp = {i:i*10 if i%2==0 else i*100 for i in range(10)}
print(generator_exp) # Output: {0: 0, 1: 100, 2: 20, 3: 300, 4: 40, 5: 500, 6: 60, 7: 700, 8: 80, 9: 900}
```
Bu yapıyı `{(i:(i*10 if i%2==0 else i*100)) for i in range(10)]` şeklinde düşünün. `{item:item for item in iterable}` yapısındaki `item:item` kısmındaki sağdaki `item` kısmına `if` - `else` yapısı tanımlanıyor. Type dönüşümlü örnek:
```py
generator_exp = dict((i,(i*10 if i%2==0 else i*100)) for i in range(10))
print(generator_exp) # Output: {0: 0, 1: 100, 2: 20, 3: 300, 4: 40, 5: 500, 6: 60, 7: 700, 8: 80, 9: 900}
```

Comprehension yapısı bir koşula göre oluşsun (sadece `if` statement kullanmaktan bahsediyorum) diyorsanız `{item:item for item in iterable if conditional}` syntax yapısını kullanabilirsiniz. Örnek:
```py
generator_exp = {i:i**2 for i in range(10) if i%2==0}
print(generator_exp) # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```
Yukarıdaki comprehension yapısı aşağıdaki anlama gelmektedir:
```py
def generator():
    for i in range(10):
        if i%2 == 0:
            yield (i,i**2)

generator_exp = dict(generator())
print(generator_exp) # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

`{item:(if - else) for item in iterable}` yapısı ile `{item:item for item in iterable if conditional}` yapısı birlikte kullanılabilir. Örnek:
```py
generator_exp = {i:i*50 if i == 4 else i*2 for i in range(10) if i%2 == 0}
print(generator_exp) # Output: {0: 0, 2: 4, 4: 200, 6: 12, 8: 16}
```

Comprehension yapısını nested olarak da kullanabilirsiniz. Örnek:
```py
# Nested dictionary objesi oluşturma (`def` statement ile)

def generator1():
    for i in range(3):
        def generator2():
            for j in range(3):
                yield (j,j**2)
        yield (i,dict(generator2()))

dict1 = dict(generator1())
print(dict1) # Output: {0: {0: 0, 1: 1, 2: 4}, 1: {0: 0, 1: 1, 2: 4}, 2: {0: 0, 1: 1, 2: 4}}

def generator3():
    for i in range(3):
        def generator4():
            for j in range(3):
                yield (i,i**2)
        yield (i,dict(generator4()))

dict2 = dict(generator3())
print(dict2) # Output: [{0: {0: 0}, 1: {1: 1}, 2: {2: 4}}
```
```py
# Nested dictionary objesi oluşturma (nested comprehension ile)

dict1 = {i:{j:j**2 for j in range(3)} for i in range(3)}
print(dict1) # Output: {0: {0: 0, 1: 1, 2: 4}, 1: {0: 0, 1: 1, 2: 4}, 2: {0: 0, 1: 1, 2: 4}}

dict2 = {i:{i:i**2 for j in range(3)} for i in range(3)}
print(dict2) # Output: {0: {0: 0}, 1: {1: 1}, 2: {2: 4}}
```
`{item:item for item in iterable}` yapısının bir comprehension yapısı olduğunu biliyorsunuz. Bu yapı iç içe `{item:{item:item for item in iterable} for item in iterable}]` örneğindeki gibi kullanılırsa nested comprehension oluyor çünkü gördüğünüz gibi biri birinin kod block'una tanımlanmış iki dictionary comprehension var.

Comprehension yapısındaki for loop'lar birbiri ardına eklenince ortaya başka bir özellik çıkıyor. Örnek:
```py
# Nested bir listeyi ayrıştırmak (`def` statement ile)

main_dict = {"1 key":{"nested 1.1 key":{"2x nested 1.1.1 key":"2x nested 1.1.1 value",
                                        "2x nested 1.1.2 key":"2x nested 1.1.2 value"},
                      "nested 1.2 key":{"2x nested 1.2.1 key":"2x nested 1.2.1 value"},
                      "nested 1.3 key":{"2x nested 1.3.1 key":"2x nested 1.3.1 value",
                                        "2x nested 1.3.2 key":"2x nested 1.3.2 value",
                                        "2x nested 1.3.3 key":"2x nested 1.3.3 value"}},
             "2 key":{"nested 2.1 key":{"2x nested 2.1.1 key":"2x nested 2.1.1 value",
                                        "2x nested 2.1.2 key":"2x nested 2.1.2 value",
                                        "2x nested 2.1.3 key":"2x nested 2.1.3 value"}},
             "3 key":{"nested 3.1 key":{"2x nested 3.1.1 key":"2x nested 3.1.1 value",
                                        "2x nested 3.1.2 key":"2x nested 3.1.2 value"},
                      "nested 3.2 key":{"2x nested 3.2.1 key":"2x nested 3.2.1 value"}}}

def generator(p1):
    for i in p1:
        for j in p1[i]:
            for k in p1[i][j]:
                yield (k,p1[i][j][k])

flatten_dict = dict(generator(main_dict))
print(flatten_dict)
```
**Output:**
```
{'2x nested 1.1.1 key': '2x nested 1.1.1 value',
 '2x nested 1.1.2 key': '2x nested 1.1.2 value',
 '2x nested 1.2.1 key': '2x nested 1.2.1 value',
 '2x nested 1.3.1 key': '2x nested 1.3.1 value',
 '2x nested 1.3.2 key': '2x nested 1.3.2 value',
 '2x nested 1.3.3 key': '2x nested 1.3.3 value',
 '2x nested 2.1.1 key': '2x nested 2.1.1 value',
 '2x nested 2.1.2 key': '2x nested 2.1.2 value',
 '2x nested 2.1.3 key': '2x nested 2.1.3 value',
 '2x nested 3.1.1 key': '2x nested 3.1.1 value',
 '2x nested 3.1.2 key': '2x nested 3.1.2 value',
 '2x nested 3.2.1 key': '2x nested 3.2.1 value'}
```

<hr>

```py
# Nested bir listeyi ayrıştırmak (comprehension ile)

main_dict = {"1 key":{"nested 1.1 key":{"2x nested 1.1.1 key":"2x nested 1.1.1 value",
                                        "2x nested 1.1.2 key":"2x nested 1.1.2 value"},
                      "nested 1.2 key":{"2x nested 1.2.1 key":"2x nested 1.2.1 value"},
                      "nested 1.3 key":{"2x nested 1.3.1 key":"2x nested 1.3.1 value",
                                        "2x nested 1.3.2 key":"2x nested 1.3.2 value",
                                        "2x nested 1.3.3 key":"2x nested 1.3.3 value"}},
             "2 key":{"nested 2.1 key":{"2x nested 2.1.1 key":"2x nested 2.1.1 value",
                                        "2x nested 2.1.2 key":"2x nested 2.1.2 value",
                                        "2x nested 2.1.3 key":"2x nested 2.1.3 value"}},
             "3 key":{"nested 3.1 key":{"2x nested 3.1.1 key":"2x nested 3.1.1 value",
                                        "2x nested 3.1.2 key":"2x nested 3.1.2 value"},
                      "nested 3.2 key":{"2x nested 3.2.1 key":"2x nested 3.2.1 value"}}}

flatten_dict = {k:main_dict[i][j][k] for i in main_dict for j in main_dict[i] for k in main_dict[i][j]}
print(flatten_dict)
```
**Output:**
```
{'2x nested 1.1.1 key': '2x nested 1.1.1 value',
 '2x nested 1.1.2 key': '2x nested 1.1.2 value',
 '2x nested 1.2.1 key': '2x nested 1.2.1 value',
 '2x nested 1.3.1 key': '2x nested 1.3.1 value',
 '2x nested 1.3.2 key': '2x nested 1.3.2 value',
 '2x nested 1.3.3 key': '2x nested 1.3.3 value',
 '2x nested 2.1.1 key': '2x nested 2.1.1 value',
 '2x nested 2.1.2 key': '2x nested 2.1.2 value',
 '2x nested 2.1.3 key': '2x nested 2.1.3 value',
 '2x nested 3.1.1 key': '2x nested 3.1.1 value',
 '2x nested 3.1.2 key': '2x nested 3.1.2 value',
 '2x nested 3.2.1 key': '2x nested 3.2.1 value'}
```
Buradaki `{k:main_dict[i][j][k] for i in main_dict for j in main_dict[i] for k in main_dict[i][j]}` yapısını nested comprehension değildir. Bu yapıyı anlamak için:
- Bu yapıyı `{(k:main_dict[i][j][k]) (for i in main_dict) (for j in main_dict[i]) (for k in main_dict[i][j])}` olarak düşünürsek, `for i in main_dict` enclosing, diğerleri soldan sağa doğru nested `for` loop oluyor. Yani soldan sağa doğru nested'lık artıyor.

- En sağdaki for loop'un item'ı (`{item:item for -> item <- in iterable}`), en baştaki item'ı temsil eder. Örneğin en sağdaki `for k in main_dict[i][j])` loop'un `k` item'i, en soldaki `k`'yı temsil eder.

- Bu yapıyla `if` - `else` veya sadece `if` veya ikisini birden kullanabilirsiniz. Örnek:
    ```py
    main_dict = {"1 key":{"nested 1.1 key":{"2x nested 1.1.1 key":"2x nested 1.1.1 value",
                                            "2x nested 1.1.2 key":"2x nested 1.1.2 value"},
                        "nested 1.2 key":{"2x nested 1.2.1 key":"2x nested 1.2.1 value"},
                        "nested 1.3 key":{"2x nested 1.3.1 key":"2x nested 1.3.1 value",
                                            "2x nested 1.3.2 key":"2x nested 1.3.2 value",
                                            "2x nested 1.3.3 key":"2x nested 1.3.3 value"}},
                "2 key":{"nested 2.1 key":{"2x nested 2.1.1 key":"2x nested 2.1.1 value",
                                            "2x nested 2.1.2 key":"2x nested 2.1.2 value",
                                            "2x nested 2.1.3 key":"2x nested 2.1.3 value"}},
                "3 key":{"nested 3.1 key":{"2x nested 3.1.1 key":"2x nested 3.1.1 value",
                                            "2x nested 3.1.2 key":"2x nested 3.1.2 value"},
                        "nested 3.2 key":{"2x nested 3.2.1 key":"2x nested 3.2.1 value"}}}

    flatten_dict1 = {k:main_dict[i][j][k] for i in main_dict for j in main_dict[i] for k in main_dict[i][j] if "2x nested 1.1." in k} # sadece `if`
    print(flatten_dict1)
    # Output:
    # {'2x nested 1.1.1 key': '2x nested 1.1.1 value',
    #  '2x nested 1.1.2 key': '2x nested 1.1.2 value'}

    flatten_dict2 = {k:main_dict[i][j][k]+" |xxx|" if "2x nested 1.1." in k else main_dict[i][j][k] for i in main_dict for j in main_dict[i] for k in main_dict[i][j]} # sadece `if - else`
    print(flatten_dict2)
    # Output:
    # {'2x nested 1.1.1 key': '2x nested 1.1.1 value |xxx|',
    #  '2x nested 1.1.2 key': '2x nested 1.1.2 value |xxx|',
    #  '2x nested 1.2.1 key': '2x nested 1.2.1 value',
    #  '2x nested 1.3.1 key': '2x nested 1.3.1 value',
    #  '2x nested 1.3.2 key': '2x nested 1.3.2 value',
    #  '2x nested 1.3.3 key': '2x nested 1.3.3 value',
    #  '2x nested 2.1.1 key': '2x nested 2.1.1 value',
    #  '2x nested 2.1.2 key': '2x nested 2.1.2 value',
    #  '2x nested 2.1.3 key': '2x nested 2.1.3 value',
    #  '2x nested 3.1.1 key': '2x nested 3.1.1 value',
    #  '2x nested 3.1.2 key': '2x nested 3.1.2 value',
    #  '2x nested 3.2.1 key': '2x nested 3.2.1 value'}

    flatten_dict = {k:main_dict[i][j][k]+" |xxx|" if "2x nested 1.1." in k else main_dict[i][j][k] for i in main_dict for j in main_dict[i] for k in main_dict[i][j] if "2x nested 1." in k} # `if` ve `if - else` birlikte
    print(flatten_dict)
    # Output:
    # {'2x nested 1.1.1 key': '2x nested 1.1.1 value |xxx|',
    #  '2x nested 1.1.2 key': '2x nested 1.1.2 value |xxx|',
    #  '2x nested 1.2.1 key': '2x nested 1.2.1 value',
    #  '2x nested 1.3.1 key': '2x nested 1.3.1 value',
    #  '2x nested 1.3.2 key': '2x nested 1.3.2 value',
    #  '2x nested 1.3.3 key': '2x nested 1.3.3 value'}
    ```

**Not:** Dictionary objelerinde nested'lık ile bu dictionary'e erişen dictionary comprehension objelerindeki `for` loop sayısı doğru orantılıdır. Yani bir dictionary objesi 2 katman (Oreneğin `{1:{1:1, 2:2}, 2:{1:1, 2:2}}`) nested ise, bu dictionary'e erişen dictionary comprehension objelerindeki `for` loop (Örneğin `{j:j for i in p1 for j in p1[i]}`) sayısı da 2 olmalıdır. Bunu [`while`-`for` Döngüleri (Loops)](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/statements/while-for_loops.md "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/statements/while-for_loops.md") bölümünde anlatmıştım. `{1:{1:1, 2:2}, 2:{1:1, 2:2}, 3:3}` gibi dictionary'ler üzerinde `{j:j for i in p1 for j in p1[i]}` işlemi yapamazsınız çünkü `3:3` item'ı nested'lığı bozuyor.