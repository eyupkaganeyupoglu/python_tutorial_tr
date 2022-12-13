# İçindekiler

- [Functions for Rounding`](#1)
  - [`around` Methodu](#1.1)
  - [`floor` Methodu](#1.2)
  - [`ceil` Methodu](#1.3)


<h1 id="1">Functions for Rounding</h1>

<h2 id="1.1"><code>around(a, decimals=0, out=None)</code> Methodu</h2>

`a` parametresine girilen array'in tüm değerlerinin belirtilen `decimals` parametresine göre yuvarlanmasını sağlar. Örnek:
```py
import numpy as np

x = np.array([1.0, 5.55, 123, 0.567, 25.532])

print(np.around(x))
print(np.around(x, decimals=1))
print(np.around(x, decimals=-1))
```
**Output:**
```
[  1.   6. 123.   1.  26.]
[  1.    5.6 123.    0.6  25.5]
[  0.  10. 120.   0.  30.]
```

<h2 id="1.2"><code>floor(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x` parametresine girilen array'in tüm değerlerinin alt değerini alır. Örnek:
```py
import numpy as np

x = np.array([-1.7, 1.5, -0.2, 0.6, 10])

print(np.floor(x))
```
**Output:**
```
[-2.  1. -1.  0. 10.]
```

<h2 id="1.3"><code>ceil(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x` parametresine girilen array'in tüm değerlerinin üst değerini alır. Örnek:
```py
import numpy as np

x = np.array([-1.7, 1.5, -0.2, 0.6, 10])

print(np.ceil(x))
```
**Output:**
```
[-1.  2. -0.  1. 10.]
```