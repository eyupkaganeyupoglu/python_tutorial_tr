# İçindekiler

-[Binary Functions](#1)
    -[`bitwise_and` Methodu](#1.1)
    -[`bitwise_or` Methodu](#1.2)
    -[`bitwise_xor` Methodu](#1.3)
    -[`invert` Methodu](#1.4)
    -[`left_shift` Methodu](#1.5)
    -[`right_shift` Methodu](#1.6)
- [Byte Swapping](#2)
    - [`ndarray.byteswap` Attribute'u](#2.1)

<h1 id="1">Binary Functions</h1>

<h2 id="1.1"><code>bitwise_and(x1, x2, /, out=None, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x1` ve `x2` parametrelerine girilen array'lerin bitleri arasında `and` işlemi yapar. Örnek:
```py
import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([5,4,3,2,1])

print(np.bitwise_and(a,b))
```
**Output:**
```
[1 0 3 0 1]
```

<h2 id="1.2"><code>bitwise_or(x1, x2, /, out=None, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x1` ve `x2` parametrelerine girilen array'lerin bitleri arasında `or` işlemi yapar. Örnek:
```py
import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([5,4,3,2,1])

print(np.bitwise_or(a,b))
```
**Output:**
```
[5 6 3 6 5]
```

<h2 id="1.3"><code>bitwise_xor(x1, x2, /, out=None, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x1` ve `x2` parametrelerine girilen array'lerin bitleri arasında `xor` işlemi yapar. Örnek:
```py
import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([5,4,3,2,1])

print(np.bitwise_xor(a,b))
```
**Output:**
```
[4 6 0 6 4]
```

<h2 id="1.4"><code>invert(x, /, out=None, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x` parametresine girilen array'in bitleri arasında `not` işlemi yapar. Örnek:
```py
import numpy as np

a = np.array([1,2,3,4,5])

print(np.invert(a))
```
**Output:**
```
[-2 -3 -4 -5 -6]
```

<h2 id="1.5"><code>left_shift(x1, x2, /, out=None, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x1` parametresine girilen array'in bitleri arasında `x2` parametresine girilen değer kadar sola kaydırma işlemi yapar. Örnek:
```py
import numpy as np

a = np.array([1,2,3,4,5])

print(np.left_shift(a,2))
```
**Output:**
```
[4 8 12 16 20]
```

<h2 id="1.6"><code>right_shift(x1, x2, /, out=None, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x1` parametresine girilen array'in bitleri arasında `x2` parametresine girilen değer kadar sağa kaydırma işlemi yapar. Örnek:
```py
import numpy as np

a = np.array([1,2,3,4,5])

print(np.right_shift(a,2))
```
**Output:**
```
[0 0 0 1 1]
```

<h1 id="2">Byte Swapping</h1>

<h2 id="2.1"><code>ndarray.byteswap(inplace=False)</code> Methodu</h2>

`ndarray`'in byte'larını değiştirir. Örnek:
  ```py
  import numpy as np

  x = np.array([1, 256, 8755], dtype=np.int16)

  print(x.byteswap(True))
  ```
  **Output:**
  ```
  [  256     1 22124]
  ```