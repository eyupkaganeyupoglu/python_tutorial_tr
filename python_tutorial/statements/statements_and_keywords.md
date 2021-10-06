# İçindekiler
- [Keywords (Anahtar Kelimeler)](#1)
- [Expressions (İfadeler)](#2)
- [Statements (Deyimler)](#3)
    - [Multi-line Statements](#3.1)
    - [Simple Statements](#3.2)
        - [Expression Statement](#3.2.1)
        - [Assignment Statement](#3.2.2)
        - [`assert` Statement](#3.2.3)
        - [`pass` Statement](#3.2.4)
        - [`del` Statement](#3.2.5)
        - [`return` Statement](#3.2.6)
        - [`yield` Statement](#3.2.7)
        - [`raise` Statement](#3.2.8)
        - [`break` Statement](#3.2.9)
        - [`continue` Statement](#3.2.10)
        - [`import` Statement](#3.2.11)
        - [`global` Statement](#3.2.12)
        - [`nonlocal` Statement](#3.2.13)
    - [Compound (Bileşik) Statements](#3.3)
        - [`if` - `elif` - `else` Statement](#3.3.1)
        - [`for` Statement](#3.3.2)
        - [`while` Statement](#3.3.3)
        - [`try` Statement](#3.3.4)
        - [`with` Statement](#3.3.5)
        - [Function Definition (`def`) Statement](#3.3.6)
        - [Class Definition (`class`) Statement](#3.3.7)
        - [Coroutines Function Definition Statement](#3.3.8)

<h1 id="1">Keywords (Anahtar Kelimeler)</h1>

Keyword, anahtar kelime anlamına gelmektedir. Python'da özel anlamlara gelen ayrışmış (reserved) bazı kelimeler vardır.Bu kelimelerin her birine **keyword** denilir. Keyword'leri identifier olarak kullanamazsınız.

**Bütün keyword'ler:** `False`, `await`, `else`, `import`, `pass`, `None`, `break`, `except`, `in`, `raise`, `True`, `class`, `finally`, `is`, `return`, `and`, `continue`, `for`, `lambda`, `try`, `as`, `def`, `from`, `nonlocal`, `while`, `assert`, `del`, `global`, `not`, `with`, `async`, `elif`, `if`, `or`, `yield`.

Daha fazla bilgi için [tıklayınız](https://www.programiz.com/python-programming/keyword-list "https://www.programiz.com/python-programming/keyword-list")

<h1 id="2">Expressions (İfadeler)</h1>

Expression, ifade anlamına gelmektedir. Bir value üretmek için kullanılan kod parçalarıdır. strings, integers, operators ... (other data types), list comprehensions, dictionary comprehensions, set comprehensions, çağırılabilir (callable) objeler hep birer **expression**'dır Örneğin:
```py
5
23 + 4
[i for i in range(10)]
len([1,2,3])
```

<h1 id="3">Statements (Deyimler)</h1>

Statement, deyim anlamına gelmektedir. Statement, expression'ları da kapsayan daha geniş kavramdır. Python yorumlayıcısının çalıştırdığı (execute) her bir talimat (instruction), statement olarak isimlendirilir. Bu statement'lar, her bir line'di (satır) instruction da olabilir, tek line'daki **statement terminator** (`;`) ile ayrılmış birden fazla instruction'ın her biri de. Python'da bütün print ve assignment işlemleri birer statement'dır. Örnek:
```py
a = 5 # assignment statement

if a: # `if` statement
    print(a) # print statement

for i in range(10): # `for` statement
    print(i) # print statement

while True: # `while` statement
    print(1) # print statement
    break # break keyword statement
```

**Not:** **C** programlama dilinde `;` işareti **statement terminator** olarak adlandırılır.

<h2 id="3.1">Multi-line Statements</h2>

Backslash (`\`) ile, tek satırda yazılan statement'ları birçok satıra bölerek yazabiliriz. Örnek:
```py
sayilar = 1+2+3+\
          4+5+6+\
          7+8
print(sayilar) # Output: 36
```

**Not:** Parantezlerin (`(), [], {}`) içindeki elemanları bölmek için backslash (`\`) kullanmak ya da kullanmamak bir farklılığa sebep olmaz.
```py
var1 = (1,2,3,\
            4,5,6,\
            7,8)
var2 = [1,2,3,\
        4,5,6,\
        7,8]
var3 = {1,2,3,\
        4,5,6,\
        7,8}
var4 = (1+2+3+
        4+5+6+
        7+8)
var5 = (1+2+3+\
        4+5+6+\
        7+8)
print(var1) # Output: (1, 2, 3, 4, 5, 6, 7, 8)
print(var2) # Output: [1, 2, 3, 4, 5, 6, 7, 8]
print(var3) # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(var4) # Output: 36
print(var5) # Output: 36
```
**Not:** Birden fazla statement'i tek line'da tanımlamak için **statement terminator**'den (`;`) yararlanılır.
```py
a = 1 ; b = 2
print(a+b) # Output: 3
```

<h2 id="3.2">Simple Statements</h2>

Aşağıda gösterilecek statementlerin çoğunu ileriki bölümlerde öğreneceksiniz. Bu bölümde sadece neyin statement, neyin expression, neyin keyword olarak isimlendirildiğini öğrenmeniz yeterli. Bu isimlendirmeleri (aynı zamanda assignment, definition gibi kavramları) bilmeniz önemli çünkü stack overflow'da "This ifade" diye cümleye başlayamazsınız.


<h3 id="3.2.1">Expression Statement</h3>

Expression'ların bir variable'a atanması (assignment) veya yazdırılması (print) Expression Statement'lara örnek gösterilebilir.
```py
a = 1+2+3
b = int("100")
print(1+2+3) # Output: 6
print(int(100)) # Output: 100
```

<h3 id="3.2.2">Assignment Statement</h3>

Bir variable'a value atadığın (assignment) instruction'a Assignment Statement denir.
```py
a = 10
b = "Hi"
```

<h3 id="3.2.3"><code>assert</code> Statement</h3>

```py
assert 5 < 10 # `assert` Statement
assert (True or False) # `assert` Statement
```

<h3 id="3.2.4"><code>pass</code> Statement</h3>

```py
def func(): # Function Definition (`def`) Statement
    pass # `pass` Statement
```

<h3 id="3.2.5"><code>del</code> Statement</h3>

`del`, Python'da herhangi bir objeyi silmek için kullanılan keyword'dür. `del object_name` şeklinde kullanıldığında statement olarak isimlendirilir.
```py
a = 1 # Assignment Statement
del a # `del` statement
```

<h3 id="3.2.6"><code>return</code> Statement</h3>

```py
def func(): # Function Definition (`def`) Statement
    return 10 # `return` Statement
```

<h3 id="3.2.7"><code>yield</code> Statement</h3>

```py
def func(): # Function Definition (`def`) Statement
    yield 'Statement 1' # `yield` Statement
```

<h3 id="3.2.8"><code>raise</code> Statement</h3>

```py
def func(): # Function Definition (`def`) Statement
    raise TypeError('Exception Example') # `raise` Statement
```

<h3 id="3.2.9"><code>break</code> Statement</h3>

```py
for num in range(0,4): # `for` Statement
    if num > 2: # `if` Statement
        break # `break` Statement
```

<h3 id="3.2.10"><code>continue</code> Statement</h3>

```py
for num in range(0,4): # `for` Statement
    if num > 2: # `if` Statement
        continue # `continue` Statement
    print(num) # Expression Statement
```

<h3 id="3.2.11"><code>import</code> Statement</h3>

```py
import os # `import` Statement
from random import randint # `import` Statement
```

<h3 id="3.2.12"><code>global</code> Statement</h3>

```py
name = "Python" # Assignment Statement

def func(): # Function Definition (`def`) Statement
    global name # global statement
    name = "Flask" # Assignment Statement

print(name) # Expression Statement
global_example() # Expression Statement
print(name) # Expression Statement
```

<h3 id="3.2.13"><code>nonlocal</code> Statement</h3>

```py
def enclosing_func(): # Function Definition (`def`) Statement
    scope = "local" # Assignment Statement

    def nested_func(): # Function Definition (`def`) Statement
        nonlocal scope  # nonlocal statement
        scope = "nonlocal" # Assignment Statement
        print(scope) # Expression Statement

    nested_func() # Output: nonlocal
    print(scope) # Expression Statement

enclosing_func() # Expression Statement
```

<h2 id="3.3">Compound (Bileşik) Statements</h2>

<h3 id="3.3.1"><code>if</code> - <code>elif</code> - <code>else</code> Statement</h3>

```py
a = int(input("Sayı girin: "))
if a < 21 and a > 10: #  `if` Statement
    print("10 < a < 21") # Expression Statement
elif a < 11 and a > 0:  # `elif` Statement
    print("0 < a < 11") # Expression Statement
else: # `else` Statement
    print("Bilmiyorum.") # Expression Statement
```

<h3 id="3.3.2"><code>for</code> Statement</h3>

```py
for n in range(0,4): # `for` Statement
    print(n) # Expression Statement
```

<h3 id="3.3.3"><code>while</code> Statement</h3>

```py
count = 5 # Assignment Statement
while count > 0: # `while` Statement
    print(count) # 
    count -= 1 # Assignment Statement
```

<h3 id="3.3.4"><code>try</code> Statement</h3>

```py
try: #  `try` Statement
    a = int(input("Sayı gir: ")) # Expression Statement
    print(a) # Expression Statement
except ValueError as ve: #  `except` Statement
    print(ve) # Expression Statement
```

<h3 id="3.3.5"><code>with</code> Statement</h3>

```py
with open('deneme.txt') as file: # `with` Statement
    pass
```

<h3 id="3.3.6">Function Definition (<code>def</code>) Statement</h3>

```py
def func(): # Function Definition (`def`) Statement
    pass # `pass` statement
```

<h3 id="3.3.7">Class Definition (<code>class</code>) Statement</h3>

```py
class A: # Class Definition (`class`) Statement
    pass # `pass` statement
```

<h3 id="3.3.8">Coroutines Function Definition Statement</h3>

```py
import asyncio

async def main(): # Coroutines Function Definition Statement
    print('hello') # Expression Statement
    await asyncio.sleep(1) # Expression Statement
    print('world') # Expression Statement

asyncio.run(main()) # Expression Statement
```
**Output:**
```
hello
world
```
Coroutines function definition statement ile ilgili daha fazla bilgi için [tıklayınız](https://docs.python.org/3/reference/compound_stmts.html#coroutines "https://docs.python.org/3/reference/compound_stmts.html#coroutines").

Variable'lar, expression'lar ve statement'lar hakkında daha fazla bilgi içib [tıklayınız](https://www.greenteapress.com/thinkpython/thinkCSpy/html/chap02.html "https://www.greenteapress.com/thinkpython/thinkCSpy/html/chap02.html").