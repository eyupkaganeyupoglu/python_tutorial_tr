# İçindekiler

-[String Functions](#1)
  -[`add` Methodu](#1.1)
  -[`multiply` Methodu](#1.2)
  -[`center` Methodu](#1.3)
  -[`capitalize` Methodu](#1.4)
  -[`title` Methodu](#1.5)
  -[`lower` Methodu](#1.6)
  -[`upper` Methodu](#1.7)
  -[`split` Methodu](#1.8)
  -[`splitlines` Methodu](#1.9)
  -[`strip` Methodu](#1.10)
  -[`join` Methodu](#1.11)
  -[`replace` Methodu](#1.12)
  -[`decode` Methodu](#1.13)
  -[`encode` Methodu](#1.14)

<h1 id="1">String Functions</h1>

<h2 id="1.1"><code>add(x1, x2, /[, out, casting, order, dtype, subok])</code> Methodu</h2>

`x1` ve `x2` parametrelerine girilen array'lerin string değerlerini birleştirir. Örnek:
```py
import numpy as np

a = np.array(['a','b','c'])
b = np.array(['d','e','f'])

print(np.add(a,b))
```
**Output:**
```
['ad' 'be' 'cf']
```

<h2 id="1.2"><code>multiply(x1, x2, /[, out, casting, order, dtype, subok])</code> Methodu</h2>

`x1` parametresine girilen array'in string değerlerini `x2` parametresine girilen değer kadar tekrar eder. Örnek:
```py
import numpy as np

a = np.array(['a','b','c'])

print(np.multiply(a,3))
```
**Output:**
```
['aaa' 'bbb' 'ccc']
```

<h2 id="1.3"><code>center(a, width, fillchar=' ', /)</code> Methodu</h2>

`a` parametresine girilen array'in string değerlerini `width` parametresine girilen değer kadar ortalar. `fillchar` parametresine girilen değer ile boşlukları doldurur. Örnek:
```py
import numpy as np

a = np.array(['a','b','c'])

print(np.center(a,10,'-'))
```
**Output:**
```
['---a----' '---b----' '---c----']
```

<h2 id="1.4"><code>capitalize(a, /)</code> Methodu</h2>

`a` parametresine girilen array'in string değerlerinin ilk harflerini büyük yapar. Örnek:
```py
import numpy as np

a = np.array(['a','b','c'])

print(np.capitalize(a))
```
**Output:**
```
['A' 'B' 'C']
```

<h2 id="1.5"><code>title(a, /)</code> Methodu</h2>

`a` parametresine girilen array'in string değerlerinin tüm harflerini büyük yapar. Örnek:
```py
import numpy as np

a = np.array(['a','b','c'])

print(np.title(a))
```
**Output:**
```
['A' 'B' 'C']
```

<h2 id="1.6"><code>lower(a, /)</code> Methodu</h2>

`a` parametresine girilen array'in string değerlerinin tüm harflerini küçük yapar. Örnek:
```py
import numpy as np

a = np.array(['A','B','C'])

print(np.lower(a))
```
**Output:**
```
['a' 'b' 'c']
```

<h2 id="1.7"><code>upper(a, /)</code> Methodu</h2>

`a` parametresine girilen array'in string değerlerinin tüm harflerini büyük yapar. Örnek:
```py
import numpy as np

a = np.array(['a','b','c'])

print(np.upper(a))
```
**Output:**
```
['A' 'B' 'C']
```

<h2 id="1.8"><code>split(a, /[, sep, maxsplit])</code> Methodu</h2>

`a` parametresine girilen array'in string değerlerini `sep` parametresine girilen değer ile ayırır. `maxsplit` parametresine girilen değer kadar ayırma işlemi yapar. Örnek:
```py
import numpy as np

a = np.array(['a b c','d e f','g h i'])

print(np.split(a,' '))
```
**Output:**
```
[array(['a', 'b', 'c'], dtype='<U1')
  array(['d', 'e', 'f'], dtype='<U1')
  array(['g', 'h', 'i'], dtype='<U1')]
```

<h2 id="1.9"><code>splitlines(a, /[, keepends])</code> Methodu</h2>

`a` parametresine girilen array'in string değerlerini satır sonlarına göre ayırır. `keepends` parametresine `True` girilirse satır sonlarını da ayırır. Örnek:
```py
import numpy as np

a = np.array(['a\nb\nc','d\ne\nf','g\nh\ni'])

print(np.splitlines(a))
```
**Output:**
```
[array(['a', 'b', 'c'], dtype='<U1')
  array(['d', 'e', 'f'], dtype='<U1')
  array(['g', 'h', 'i'], dtype='<U1')]
```

<h2 id="1.10"><code>strip(a, /[, chars])</code> Methodu</h2>

`a` parametresine girilen array'in string değerlerinin başındaki ve sonundaki boşlukları siler. `chars` parametresine girilen değerlerin başındaki ve sonundaki boşlukları siler. Örnek:
```py
import numpy as np

a = np.array([' a ',' b ',' c '])

print(np.strip(a))
```
**Output:**
```
['a' 'b' 'c']
```

<h2 id="1.11"><code>join(a, sep, /)</code> Methodu</h2>

`a` parametresine girilen array'in string değerlerini `sep` parametresine girilen değer ile birleştirir. Örnek:
```py
import numpy as np

a = np.array(['a','b','c'])

print(np.join(a,'-'))
```
**Output:**
```
a-b-c
```

<h2 id="1.12"><code>replace(a, old, new, /[, count])</code> Methodu</h2>

`a` parametresine girilen array'in string değerlerinde `old` parametresine girilen değeri `new` parametresine girilen değer ile değiştirir. `count` parametresine girilen değer kadar değiştirme işlemi yapar. Örnek:
```py
import numpy as np

a = np.array(['a','b','c'])

print(np.replace(a,'a','d'))
```
**Output:**
```
['d' 'b' 'c']
```

<h2 id="1.13"><code>decode(a, /[, encoding, errors])</code> Methodu</h2>

`a` parametresine girilen array'in string değerlerini `encoding` parametresine girilen değer ile kodlar. `errors` parametresine girilen değer ile hata ayıklaması yapar. Örnek:
```py
import numpy as np

a = np.array(['a','b','c'])

print(np.decode(a,'utf-8'))
```
**Output:**
```
[b'a' b'b' b'c']
```

<h2 id="1.14"><code>encode(a, /[, encoding, errors])</code> Methodu</h2>

`a` parametresine girilen array'in string değerlerini `encoding` parametresine girilen değer ile kodlar. `errors` parametresine girilen değer ile hata ayıklaması yapar. Örnek:
```py
import numpy as np

a = np.array([b'a',b'b',b'c'])

print(np.encode(a,'utf-8'))
```
**Output:**
```
['a' 'b' 'c']
```