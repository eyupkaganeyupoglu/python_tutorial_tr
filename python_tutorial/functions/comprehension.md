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
Generator Comprehension yapısı `<genexpr>` adında bir obje döndürür. `def` statement ile tanımladığımız fonksiyondan istediğimiz kadar, generator comprehension yapısı ile sadece bir tane generator objesi oluşturabiliriz.

**Not:** Comprehension'larda `(expression for item in iterable)` syntax'ındaki `expression` kısmı, `yield (expression)` anlamına gelmektedir.

<h2 id="1.1">Sequence Comprehension</h2>

Bir generator comprehension objesini sequence type'lara dönüştürebiliriz. `list`/`tuple` gibi type'lara dönüştürülen generator comprehension objelerinden dümdüz `list`/`tuple` vb. olarak bahsedilse bile literatürde List Comprehension, Tuple Comprehension vb. olarak bahsedilir.

List comprehension `[expression for item in iterable]` syntax yapısı ile veya `list(expression for item in iterable)` type dönüşümü yapılarak oluşturulur (parantezler dahil). Örnek:
```py
a = list((i**2) for i in range(1,4))
b = [(i**2) for i in range(1,4)]
print(a) # Output: [1, 4, 9]
print(b) # Output: [1, 4, 9]
```

**Not:** Yukarıdaki yöntemler arasında `[expression for item in iterable]` syntax yapısını kullanmak en sağlıklısıdır.

**Not:** Tuple için durum farklıdır. `((i**2) for i in range(1,4))` yapısı generator comprehension oluşturduğu için `tuple` comprehension oluşturmak için type dönüşümü (`tuple((i**2) for i in range(1,4))`) yapmanız gerekmektedir.

Comprehension yapısını tek satırda tanımlanan `if` - `else` ile birlikte kullanabilirsin. `if` - `else` yapısını Comprehension yapısını içinde (`[(Expression if condition else Expression) for item in iterable]`) kullanmaya örnek:
```py
generator_exp1 = [i*10 if i%2==0 else i*100 for i in range(10)]
print(generator_exp1) # Output: [0, 100, 20, 300, 40, 500, 60, 700, 80, 900]

def generator_exp2():
    for i in range(10):
        if i%2==0:
            yield i*10
        else:
            yield i*100

print(list(generator_exp2())) # Output: [0, 100, 20, 300, 40, 500, 60, 700, 80, 900]
```
`generator_exp1` ile `generator_exp2` aynıdır. `[i*10 if i%2==0 else i*100 for i in range(10)]` yapısını `[(i*10 if i%2==0 else i*100) for i in range(10)]` şeklinde düşünürsek, list comprehension (`[expression for item in iterable]`) syntax'ının `expression` kısmına `if` - `else` yapısı tanımlanıyor diyebiliriz.

Comprehension yapısını `if` - `else` yapısı içinde `[expression for item in iterable if condition]` kullanmaya örnek:
```py
generator_exp1 = [i*10 for i in range(10) if i%2==0]
print(generator_exp1) # Output: [0, 20, 40, 60, 80]

def generator_exp2():
    for i in range(10):
        if i%2 == 0:
            yield i*10

print(list(generator_exp2())) # Output: [0, 20, 40, 60, 80]
```
**Not:** `[expression for item in iterable if condition]` syntax'ındaki `expression for item in iterable` kısmını `[(Expression if condition else Expression) for item in iterable]` syntax'ındaki `Expression if condition else Expression` kısmındaki gibi kullanıcının kodu anlamasını kolaylaştırmak için parantez içine alamazsınız çünkü bazı karışık sebeplerden dolayı bu bir syntax hatasıdır. Bu karışık sebepleri boşverin, bu yapıları syntax'ına uygun kullanın yeterli.

`[(Expression if condition else Expression) for item in iterable]` ve `[expression for item in iterable if conditional]` yapılarının birlikte kullanılmasına örnek:
```py
generator_exp1 = [(i*50 if i == 4 else i*2) for i in range(10) if i%2 == 0]
print(generator_exp1) # Output: [0, 4, 200, 12, 16]

def generator_exp2():
    for i in range(10):
        if i%2==0:
            if i==4:
                yield i*50
            else:
                yield i*2

print(list(generator_exp2())) # Output: [0, 4, 200, 12, 16]
```

Comprehension yapısını nested olarak da kullanabilirsiniz. Örnek:
```py
liste = [[i for i in range(3)] for i in range(3)]
print(liste) # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

def generator1():
    for i in range(3):
        def generator2():
            for j in range(3):
                yield j
        yield list(generator2())

print(list(generator1())) # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
```
```py
liste = [[i for j in range(3)] for i in range(3)]
print(liste) # Output: [[0, 0, 0], [1, 1, 1], [2, 2, 2]]

def generator1():
    for i in range(3):
        def generator2():
            for j in range(3):
                yield i
        yield list(generator2())

print(list(generator1())) # Output: [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
```

Comprehension yapısındaki for loop'lar birbiri ardına eklenince ortaya başka bir özellik çıkıyor. Örnek:
```py
main_list = [[[1,2], [3,4,5], [6]], [[7,8,9,10], [11,12]], [[13,14,15], [16], [17,18],[19,20]]]

generator1 = [k for i in main_list for j in i for k in j]
print(generator1) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def generator2(p1):
    for i in p1:
        for j in i:
            for k in j:
                yield k

print(list(generator2(main_list))) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
```
Buradaki `[k for i in main_list for j in i for k in j]` yapısını nested comprehension değildir. Bu yapıyı anlamak için:
- Bu yapıyı `[(k) (for i in main_list) (for j in i) (for k in j)]` olarak düşünürsek, `for i in main_list` enclosing, diğerleri soldan sağa doğru nested `for` loop oluyor. Yani soldan sağa doğru nested'lık artıyor.

- En sağdaki for loop'un item'ı (`[expression for item in iterable]`), en baştaki expression'ı temsil eder. Örneğin en sağdaki `for k in j` loop'un `k` item'i, en soldaki `k`'yı temsil eder.

Bu yapıyı `[expression for item in iterable if condition]` veya `[(Expression if condition else Expression) for item in iterable]` yapılarıyla beraber kullanabilirsiniz.
- `[expression for item in iterable if condition]` yapısı ile birlikte kullanmaya örnek:
    ```py
    main_list = [[[1,2], [3,4,5], [6]], [[7,8,9,10], [11,12]], [[13,14,15], [16], [17,18],[19,20]]]

    generator1 = [k for i in main_list for j in i for k in j if k%2==0]
    print(generator1) # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    def generator2(p1):
        for i in p1:
            for j in i:
                for k in j:
                    if k%2==0:
                        yield k

    print(list(generator2(main_list))) # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    ```
    Bu kodu `[(k) (for i in main_list) (for j in i) (for k in j if k%2==0)]` şeklinde düşünürseniz işiniz kolaylaşır.

- `[(Expression if condition else Expression) for item in iterable]` yapısı ile birlikte kullanmaya örnek:
    ```py
    main_list = [[[1,2], [3,4,5], [6]], [[7,8,9,10], [11,12]], [[13,14,15], [16], [17,18],[19,20]]]

    generator1 = [k*10 if k%2==0 else k for i in main_list for j in i for k in j]
    print(generator1) # Output: [1, 20, 3, 40, 5, 60, 7, 80, 9, 100, 11, 120, 13, 140, 15, 160, 17, 180, 19, 200]

    def generator2(p1):
        for i in p1:
            for j in i:
                for k in j:
                    if k%2==0:
                        yield k*10
                    else:
                        yield k

    print(list(generator2(main_list))) # Output: [1, 20, 3, 40, 5, 60, 7, 80, 9, 100, 11, 120, 13, 140, 15, 160, 17, 180, 19, 200]
    ```
    Bu kodu `[(k*10 if k%2==0 else k) (for i in main_list) (for j in i) (for k in j)]` şeklinde düşünürseniz işiniz kolaylaşır.

- `[expression for item in iterable if condition]` ve `[(Expression if condition else Expression) for item in iterable]` yapılarıyla birlikte kullanmaya örnek:
    ```py
    main_list = [[[1,2], [3,4,5], [6]], [[7,8,9,10], [11,12]], [[13,14,15], [16], [17,18],[19,20]]]

    generator1 = [k*10 if k==10 else k for i in main_list for j in i for k in j if k%2==0]
    print(generator1) # Output: [2, 4, 6, 8, 100, 12, 14, 16, 18, 20]

    def generator2(p1):
        for i in p1:
            for j in i:
                for k in j:
                    if k%2==0:
                        if k==10:
                            yield k*10
                        else:
                            yield k

    print(list(generator2(main_list))) # Output: [2, 4, 6, 8, 100, 12, 14, 16, 18, 20]
    ```
    Bu kodu `[(k*10 if k==10 else k) (for i in main_list) (for j in i) (for k in j if k%2==0)]` şeklinde düşünürseniz işiniz kolaylaşır.

**Not:** Liste objelerinde nested'lik ile bu listeye erişen list comprehension objelerindeki `for` loop sayısı doğru orantılıdır. Yani bir liste objesi 2 katman (Oreneğin `[[1,2], [3,4]]`) nested ise, bu listeye erişen list comprehension objelerindeki `for` loop (Örneğin `j for i in liste for j in i`) sayısı da 2 olmalıdır. Bunu [`while`-`for` Döngüleri (Loops)](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/while-for_loops.md "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/while-for_loops.md") bölümünde anlatmıştım. `[0, [1, 2, 3], [4, 5], [6, 7, 8, 9]]` gibi listeler üzerinde `[j for i in liste for j in i]` işlemi yapamazsınız çünkü `0` öğesi nested'lığı bozuyor.

Python'ın dinamik yapısı sayesinde comprehension yapısını kullanarak çeşit çeşit algoritmalar uydurabilirsiniz. Örnek:
```py
# Nested bir listeden başka bir nested liste yaratmak

def generator1(p1):
    for i in range(len(p1[0])):
        def generator2():
            for j in p1:
                yield j[i]
        yield list(generator2())

main_list = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(list(generator1(main_list))) # Output: [[1, 5], [2, 6], [3, 7], [4, 8]]
liste = [[j[i] for j in main_list] for i in range(len(main_list[0]))]
print(liste) # Output: [[1, 5], [2, 6], [3, 7], [4, 8]]

main_list = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(list(generator1(main_list))) # Output: [[1, 3, 5, 7], [2, 4, 6, 8]]
liste = [[j[i] for j in main_list] for i in range(len(main_list[0]))]
print(liste) # Output: [[1, 3, 5, 7], [2, 4, 6, 8]]
```

<h2 id="1.2">Dictionary Comprehension</h2>

Bir generator comprehension objesini dictionary type'lara dönüştürebiliriz. `dict` type'a dönüştürülen generator comprehension objelerinden dümdüz `dict` olarak bahsedilse bile literatürde Dictionary Comprehension olarak bahsedilir.

Dictionary comprehension `{key:value for item in iterable}` veya `dict((key,value) for item in iterable)` type dönüşümü yapılarak oluşturulur (parantezler dahil). Örnek:
```py
dict_generator_exp1 = {i:i**2 for i in range(1,4)}
print(dict_generator_exp1) # Output: {1: 1, 2: 4, 3: 9}

dict_generator_exp2 = dict((i,i**2) for i in range(1,4))
print(dict_generator_exp2) # Output: {1: 1, 2: 4, 3: 9}

def dict_generator():
    for i in range(1,4):
        yield (i,i**2)

print(dict(dict_generator())) # Output: {1: 1, 2: 4, 3: 9}
```

**Not:** Yukarıdaki yöntemler arasında `{key:value for item in iterable}` syntax yapısını kullanmak en sağlıklısıdır.

Comprehension yapısını tek satırda tanımlanan `if` - `else` ile birlikte kullanabilirsin. `if` - `else` yapısını Comprehension yapısını içinde (`{key:value if condition else value for item in iterable}`) kullanmaya örnek:
```py
generator_exp1 = {i:i*10 if i%2==0 else i*100 for i in range(6)}
print(generator_exp1) # Output: {0: 0, 1: 100, 2: 20, 3: 300, 4: 40, 5: 500}

def generator_exp2():
    for i in range(6):
        if i%2==0:
            yield (i,i*10)
        else:
            yield (i,i*100)

print(dict(generator_exp2())) # Output: {0: 0, 1: 100, 2: 20, 3: 300, 4: 40, 5: 500}
```
`generator_exp1` ile `generator_exp2` aynıdır. `{i:i*10 if i%2==0 else i*100 for i in range(6)}` yapısını `{i:(i*10 if i%2==0 else i*100) for i in range(6)}` şeklinde düşürseniz anlamanız kolaylaşır. Type dönüşümlü örnek:
```py
generator_exp = dict((i,(i*10 if i%2==0 else i*100)) for i in range(6))
print(generator_exp) # Output: {0: 0, 1: 100, 2: 20, 3: 300, 4: 40, 5: 500}
```
`(i,(i*10 if i%2==0 else i*100)) for i in range(6)` kodundaki `(i,(i*10 if i%2==0 else i*100))` kısmı `(key,value) for item in iterable)` syntax'ındaki `(key,value)` kısmına karşılık gelir. Parantezleri kullanma zorunluluğunuz buradan geliyor. Aksi halde syntax hatası olur.

Comprehension yapısını `if` - `else` yapısı içinde `{key:value for item in iterable if conditional}` kullanmaya örnek:
```py
generator_exp1 = {i:i**2 for i in range(10) if i%2==0}
print(generator_exp1) # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

def generator_exp2():
    for i in range(10):
        if i%2 == 0:
            yield (i,i**2)

print(dict(generator_exp2())) # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```
`{key:value for item in iterable if conditional}` yapısındaki `key:value for item in iterable` kısmını parantez içine alamazsınız. `{key:value for item in iterable if conditional}` syntax'ını direkt kullanmalısınız.

`{key:value for item in iterable if conditional}` yapısı ile `{key:value if condition else value for item in iterable}` yapısı birlikte kullanılabilir. örnek:
```py
generator_exp = {i:i*50 if i == 4 else i*2 for i in range(10) if i%2 == 0}
print(generator_exp) # Output: {0: 0, 2: 4, 4: 200, 6: 12, 8: 16}

def generator_exp2():
    for i in range(10):
        if i%2 == 0:
            if i==4:
                yield (i,i*50)
            else:
                yield (i,i*2)

print(dict(generator_exp2())) # Output: {0: 0, 2: 4, 4: 200, 6: 12, 8: 16}
```

Comprehension yapısını nested olarak da kullanabilirsiniz. Örnek:
```py
dict1 = {i:{j:j**2 for j in range(3)} for i in range(3)}
print(dict1) # Output: {0: {0: 0, 1: 1, 2: 4}, 1: {0: 0, 1: 1, 2: 4}, 2: {0: 0, 1: 1, 2: 4}}

def generator1():
    for i in range(3):
        def generator2():
            for j in range(3):
                yield (j,j**2)
        yield (i,dict(generator2()))

print(dict(generator1())) # Output: {0: {0: 0, 1: 1, 2: 4}, 1: {0: 0, 1: 1, 2: 4}, 2: {0: 0, 1: 1, 2: 4}}
```
```py
dict1 = {i:{i:i**2 for j in range(3)} for i in range(3)}
print(dict1) # Output: {0: {0: 0}, 1: {1: 1}, 2: {2: 4}}

def generator1():
    for i in range(3):
        def generator2():
            for j in range(3):
                yield (i,i**2)
        yield (i,dict(generator2()))
        
print(dict(generator1())) # Output: {0: {0: 0}, 1: {1: 1}, 2: {2: 4}}
```

Comprehension yapısındaki for loop'lar birbiri ardına eklenince ortaya başka bir özellik çıkıyor. Örnek:
```py
main_dict = {"1 key":{"1x nested 1.1 key":{"2x nested 1.1.1 key":"2x nested 1.1.1 value",
                                           "2x nested 1.1.2 key":"2x nested 1.1.2 value"},
                      "1x nested 1.2 key":{"2x nested 1.2.1 key":"2x nested 1.2.1 value"},
                      "1x nested 1.3 key":{"2x nested 1.3.1 key":"2x nested 1.3.1 value",
                                           "2x nested 1.3.2 key":"2x nested 1.3.2 value",
                                           "2x nested 1.3.3 key":"2x nested 1.3.3 value"}},
             "2 key":{"1x nested 2.1 key":{"2x nested 2.1.1 key":"2x nested 2.1.1 value",
                                           "2x nested 2.1.2 key":"2x nested 2.1.2 value",
                                           "2x nested 2.1.3 key":"2x nested 2.1.3 value"}},
             "3 key":{"1x nested 3.1 key":{"2x nested 3.1.1 key":"2x nested 3.1.1 value",
                                           "2x nested 3.1.2 key":"2x nested 3.1.2 value"},
                      "1x nested 3.2 key":{"2x nested 3.2.1 key":"2x nested 3.2.1 value"}}}

dict_generator_exp = {k:main_dict[i][j][k] for i in main_dict for j in main_dict[i] for k in main_dict[i][j]}

def generator1(p1):
    for i in p1:
        for j in p1[i]:
            for k in p1[i][j]:
                yield (k,p1[i][j][k])

print(dict(generator1(main_dict))==dict_generator_exp) # Output: True
```
`dict_generator_exp` ve `dict(generator1(main_dict))` içeriği:
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

- En sağdaki for loop'un item'ı (`{key:value for item in iterable}`), en baştaki key'i temsil eder. Örneğin en sağdaki `for k in main_dict[i][j])` loop'un `k` item'i, en soldaki `k`'yı temsil eder.

Bu yapıylı `{key:value for item in iterable if conditional}` veya `{key:value if condition else value for item in iterable}` yapılarıyla beraber kullanabilirsiniz.

- `{key:value for item in iterable if conditional}` yapısı ile birlikte kullanmaya örnek:
    ```py
    main_dict = {"1 key":{"1x nested 1.1 key":{"2x nested 1.1.1 key":"2x nested 1.1.1 value",
                                            "2x nested 1.1.2 key":"2x nested 1.1.2 value"},
                        "1x nested 1.2 key":{"2x nested 1.2.1 key":"2x nested 1.2.1 value"},
                        "1x nested 1.3 key":{"2x nested 1.3.1 key":"2x nested 1.3.1 value",
                                            "2x nested 1.3.2 key":"2x nested 1.3.2 value",
                                            "2x nested 1.3.3 key":"2x nested 1.3.3 value"}},
                "2 key":{"1x nested 2.1 key":{"2x nested 2.1.1 key":"2x nested 2.1.1 value",
                                            "2x nested 2.1.2 key":"2x nested 2.1.2 value",
                                            "2x nested 2.1.3 key":"2x nested 2.1.3 value"}},
                "3 key":{"1x nested 3.1 key":{"2x nested 3.1.1 key":"2x nested 3.1.1 value",
                                            "2x nested 3.1.2 key":"2x nested 3.1.2 value"},
                        "1x nested 3.2 key":{"2x nested 3.2.1 key":"2x nested 3.2.1 value"}}}

    dict_comprehension_exp = {k:main_dict[i][j][k] for i in main_dict for j in main_dict[i] for k in main_dict[i][j] if "2x nested 1.1." in k}
    print(dict_comprehension_exp)
    # Output:
    # {'2x nested 1.1.1 key': '2x nested 1.1.1 value',
    #  '2x nested 1.1.2 key': '2x nested 1.1.2 value'}
    ```
    Bu kodu `{(k:main_dict[i][j][k]) (for i in main_dict) (for j in main_dict[i]) (for k in main_dict[i][j] if "2x nested 1.1." in k)}` şeklinde düşünürseniz işiniz kolaylaşır.

- `{key:value if condition else value for item in iterable}` yapısı ile birlikte kullanmaya örnek:
    ```py
    dict_comprehension_exp = {k:main_dict[i][j][k]+" |xxx|" if "2x nested 1.1." in k else main_dict[i][j][k] for i in main_dict for j in main_dict[i] for k in main_dict[i][j]}
    print(dict_comprehension_exp)
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
    ```
    Bu kodu `{(k:(main_dict[i][j][k]+" |xxx|" if "2x nested 1.1." in k else main_dict[i][j][k]) for i in main_dict) (for j in main_dict[i]) (for k in main_dict[i][j])}` şeklinde düşünürseniz işiniz kolaylaşır.

- `{key:value for item in iterable if conditional}` ve `{key:value if condition else value for item in iterable}` yapılarıyla birlikte kullanmaya örnek:
    ```py
    dict_comprehension_exp = {k:main_dict[i][j][k]+" |xxx|" if "2x nested 1.1." in k else main_dict[i][j][k] for i in main_dict for j in main_dict[i] for k in main_dict[i][j] if "2x nested 1." in k} # `if` ve `if - else` birlikte
    print(dict_comprehension_exp)
    # Output:
    # {'2x nested 1.1.1 key': '2x nested 1.1.1 value |xxx|',
    #  '2x nested 1.1.2 key': '2x nested 1.1.2 value |xxx|',
    #  '2x nested 1.2.1 key': '2x nested 1.2.1 value',
    #  '2x nested 1.3.1 key': '2x nested 1.3.1 value',
    #  '2x nested 1.3.2 key': '2x nested 1.3.2 value',
    #  '2x nested 1.3.3 key': '2x nested 1.3.3 value'}
    ```
    Bu kodu `{(k:(main_dict[i][j][k]+" |xxx|" if "2x nested 1.1." in k else main_dict[i][j][k]) for i in main_dict) (for j in main_dict[i]) (for k in main_dict[i][j] if "2x nested 1." in k)}` şeklinde düşünürseniz işiniz kolaylaşır.

**Not:** Dictionary objelerinde nested'lik ile bu dictionary'e erişen dictionary comprehension objelerindeki `for` loop sayısı doğru orantılıdır. Yani bir dictionary objesi 2 katman (öreneğin `{1:{1:1, 2:2}, 2:{1:1, 2:2}}`) nested ise, bu dictionary'e erişen dictionary comprehension objelerindeki `for` loop (Örneğin `{j:j for i in p1 for j in p1[i]}`) sayısı da 2 olmalıdır. Bunu [`while`-`for` Döngüleri (Loops)](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/while-for_loops.md "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/while-for_loops.md") bölümünde anlatmıştım. `{1:{1:1, 2:2}, 2:{1:1, 2:2}, 3:3}` gibi listeler üzerinde `{j:j for i in p1 for j in p1[i]}` işlemi yapamazsınız çünkü `3:3` item'ı nested'lığı bozuyor.