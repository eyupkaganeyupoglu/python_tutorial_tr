# Keywords
Keyword, anahtar kelime anlamına gelmektedir. Python'da özel anlamlara gelen ayrışmış (reserved) bazı kelimeler vardır. Bu kelimeleri identifier olarak kullanamazsınız. Bütün keyword'ler: `False`, `await`, `else`, `import`, `pass`, `None`, `break`, `except`, `in`, `raise`, `True`, `class`, `finally`, `is`, `return`, `and`, `continue`, `for`, `lambda`, `try`, `as`, `def`, `from`, `nonlocal`, `while`, `assert`, `del`, `global`, `not`, `with`, `async`, `elif`, `if`, `or`, `yield`.

Daha fazla bilgi için [tıklayınız](https://www.programiz.com/python-programming/keyword-list)

# Expression (İfadeler)
İngilizcede **expression** denen **ifadeler**, bir value üretmek için kullanılan kod parçalarıdır. Karakter dizileri, sayılar, operatörler, öteki veri tipleri, liste comprehensions, sözlük comprehensions, küme comprehensions, `fonksiyon()` şeklinde çağırdığırılan fonksiyonlar hep birer **expression**'dır Örneğin:
```py
5
23 + 4
[i for i in range(10)]
len([1,2,3])
```

# Statement (Deyimler)
İngilizcede **statement** olarak adlandırılan **deyimler** ise ifadeleri de kapsayan daha geniş bir kavramdır. Buna göre bütün expression'lar aynı zamanda birer statement'dir. Daha doğrusu, expression'ların bir araya gelmesi ile statement'lar oluşturulabilir. Python'da her line bir statement'dir. Örneğin:
```py
a = 5 (Python’da bütün değer atama işlemleri birer deyimdir.)

if a:
    print(a)

for i in range(10):
    print(i)

while True:
    print(1)
    break
```
**Not:** **C** programlama dilinde, ';' işareti **statement terminator** olarak adlandırılır.

## Multi-line Statements
Backslash `\` ile, tek satırda yazmamız gereken statement'leri birçok satıra bölerek yazabiliriz. Örnek:
```py
sayilar = 1+2+3+\
          4+5+6+\
          7+8
print(sayilar) # Output: 36
```
**Not:** Parantezlerde `(), [], {}` backslash `\` kullanmak ya da kullanmamak bir farklılığa sebep olmaz.
```py
sayilar1 = (1+2+3+
            4+5+6+
            7+8)
sayilar2 = [1+2+3+
            4+5+6+
            7+8]
sayilar3 = {1+2+3+
            4+5+6+
            7+8}
print(sayilar1) # Output: 36
print(sayilar2) # Output: [36]
print(sayilar3) # Output: {36}
```
**Not:** Birden fazla statement'i tek satırda tanımlamak için `;` işaretinden yararlanılır.
```py
a = 1 ; b = 2
print(a+b) # Output: 3
```

## Simple Statements

### Expression Statement
```py
i = int("10")
sum = 1+2+3
```
Önce `int("10")` ve `1+2+3` expression'ları değerlendirilip `sum` ve `i` variable'larına atanır.

### Assignment Statement
Assignment, atama yapmak, değer vermek anlamına gelmektedir. 
```py
count = 10
message = "Hi"
```

### `assert` Statement
```py
assert 5 < 10
assert (True or False)
```

### `pass` Statement
```py
def foo():
    pass  # pass statement
```

### `del` Statement
`del`, Python'da herhangi bir objeyi silmek için kullanılan keyword'dür. `del object_name` şeklinde kullanıldığında statement olarak isimlendirilir.
```py
a = 1
del a
```

### `return` Statement
```py
def return_statement():
    return 10
```

### `yield` Statement
```py
def yield_statement():
    yield 'Statement 1'
```

### `raise` Statement
```py
def raise_statement():
    raise TypeError('Exception Example')
```

### `break` Statement
```py
for num in range(0,4):
    if num > 2:
        break
```

### `continue` Statement
```py
for num in range(0,4):
    if num > 2:
        continue
    print(num)
```

### `import` Statement
```py
import os
from random import radint
```

### `global` Statement
```py
name = "Python"

def global_example():
    global name # global statement
    name = "Flask"

print(name)  # Output: Python
global_example()
print(name)  # Output: Flask
```

### `nonlocal` Statement
```py
def enclosing_function():
    scope = "local"

    def nested_function():
        nonlocal scope  # nonlocal statement
        scope = "nonlocal"
        print(scope)

    nested_function() # Output: nonlocal
    print(scope)

enclosing_function() # Output: nonlocal
```

## Compound Statements

### `if` Statement
```py
if 5 < 10:
    print("This will always print")
else:
    print("Unreachable Code")
```

### `for` Statement
```py
for n in range(0,4):
    print(n)
```

### `while` Statement
```py
count = 5
while count > 0:
    print(count)
    count -= 1
```

### `try` Statement
```py
try:
    print("try")
except ValueError as ve:
    print(ve)
```

### `with` Statement
```py
with open('deneme.txt') as file:
    file.read()
```

### Function Definition (`def`) Statement
```py
def useless():
    pass
```

### Class Definition (`class`) Statement
```py
class Data:
    id = 0
```

### Coroutines Function Definition Statement
```py
import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())
```
**Output:**
```
hello
world
```
Coroutines function definition statement ile ilgili daha fazla bilgi için [tıklayınız](https://docs.python.org/3/reference/compound_stmts.html#coroutines).