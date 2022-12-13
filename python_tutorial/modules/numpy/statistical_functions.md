# İçindekiler

- [Statistical Functions](#1)
  - [`amin` Methodu](#1.1)
  - [`amax` Methodu](#1.2)
  - [`ptp` Methodu](#1.3)
  - [`percentile` Methodu](#1.4)
  - [`median` Methodu](#1.5)
  - [`mean` Methodu](#1.6)
  - [`average` Methodu](#1.7)
  - [`std` Methodu](#1.8)
  - [`var` Methodu](#1.9)

<h1 id="1">Statistical Functions</h1>

<h2 id="1.1"><code>amin</code> Methodu</h2>

`amin(a, /, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=True)` syntax'ına sahiptir. `a` parametresine girilen array'in tüm değerlerinin en küçüğünü alır. Örnek:
```py
import numpy as np

a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])

print(np.amin(a))
```
**Output:**
```
2
```

<h2 id="1.2"><code>amax</code> Methodu</h2>

`amax(a, /, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=True)` syntax'ına sahiptir. `a` parametresine girilen array'in tüm değerlerinin en büyüğünü alır. Örnek:
```py
import numpy as np

a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])

print(np.amax(a))
```
**Output:**
```
9
```

<h2 id="1.3"><code>ptp</code> Methodu</h2>

`ptp(a, /, axis=None, out=None, keepdims=<no value>)` syntax'ına sahiptir. `a` parametresine girilen array'in tüm değerlerinin en büyük ve en küçük farkını alır. Örnek:
```py
import numpy as np

a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])

print(np.ptp(a))
```
**Output:**
```
7
```

<h2 id="1.4"><code>percentile(a, q, /, axis=None, out=None, overwrite_input=False, interpolation='linear', keepdims=False)</code> Methodu</h2>

`a` parametresine girilen array'in tüm değerlerinin `q` parametresine girilen yüzdelik değerine göre yüzdelik değerini alır. Örnek:
```py
import numpy as np

a = np.array([[10, 7, 4], [3, 2, 1]])

print(np.percentile(a, 50))
```
**Output:**
```
3.5
```

<h2 id="1.5"><code>median(a, /, axis=None, out=None, overwrite_input=False, keepdims=False)</code> Methodu</h2>

`a` parametresine girilen array'in tüm değerlerinin ortalamasını alır. Örnek:
```py
import numpy as np

a = np.array([[30, 65, 70], [80, 95, 10], [50, 90, 60]])

print(np.median(a))
```
**Output:**
```
65.0
```

<h2 id="1.6"><code>mean</code> Methodu</h2>

`mean(a, /, axis=None, dtype=None, out=None, keepdims=<no value>)` syntax'ına sahiptir. `a` parametresine girilen array'in tüm değerlerinin ortalamasını alır. Örnek:
```py
import numpy as np

a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])

print(np.mean(a))
```
**Output:**
```
3.6666666666666665
```

<h2 id="1.7"><code>average(a, /, axis=None, weights=None, returned=False)</code> Methodu</h2>

`a` parametresine girilen array'in tüm değerlerinin ağırlıklı ortalamasını alır. Örnek:
```py
import numpy as np

a = np.array([1, 2, 3, 4])

print(np.average(a))
```
**Output:**
```
2.5
```

<h2 id="1.8"><code>std</code> Methodu</h2>

`std(a, /, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>)` syntax'ına sahiptir. `a` parametresine girilen array'in tüm değerlerinin standart sapmasını alır. Örnek:
```py
import numpy as np

a = np.array([1, 2, 3, 4])

print(np.std(a))
```
**Output:**
```
1.118033988749895
```

<h2 id="1.9"><code>var</code> Methodu</h2>

`var(a, /, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>)` syntax'ına sahiptir. `a` parametresine girilen array'in tüm değerlerinin varyansını alır. Örnek:
```py
import numpy as np

a = np.array([1, 2, 3, 4])

print(np.var(a))
```
**Output:**
```
1.25
```