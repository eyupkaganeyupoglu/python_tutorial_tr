# İçindekiler

-[Trigonometric Functions](#1)
    -[`sin` Methodu](#1.1)
    -[`cos` Methodu](#1.2)
    -[`tan` Methodu](#1.3)
    -[`arcsin` Methodu](#1.4)
    -[`arccos` Methodu](#1.5)
    -[`arctan` Methodu](#1.6)
    -[`degrees` Methodu](#1.7)
    -[`radians` Methodu](#1.8)
    -[`deg2rad` Methodu](#1.9)
    -[`rad2deg` Methodu](#1.10)
    -[`unwrap` Methodu](#1.11)

<h1 id="1">Trigonometric Functions</h1>

<h2 id="1.1"><code>sin(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x` parametresine girilen array'in tüm değerlerinin sinüsünü alır ve radians cinsinden döndürür. Örnek:
```py
import numpy as np

x = np.array([0, np.pi/2, np.pi])

print(np.sin(x))
```
**Output:**
```
[0.0000000e+00 1.0000000e+00 1.2246468e-16]
```

<h2 id="1.2"><code>cos(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x` parametresine girilen array'in tüm değerlerinin kosinüsünü alır ve radians cinsinden döndürür. Örnek:
```py
import numpy as np

x = np.array([0, np.pi/2, np.pi])

print(np.cos(x))
```
**Output:**
```
[ 1.0000000e+00  6.1232340e-17 -1.0000000e+00]
```

<h2 id="1.3"><code>tan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x` parametresine girilen array'in tüm değerlerinin tanjantını alır ve radians cinsinden döndürür. Örnek:
```py
import numpy as np

x = np.array([0, np.pi/2, np.pi])

print(np.tan(x))
```
**Output:**
```
[ 0.0000000e+00  1.6331239e+16 -1.2246468e-16]
```

<h2 id="1.4"><code>arcsin(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x` parametresine girilen array'in tüm değerlerinin ters sinüsünü alır ve radians cinsinden döndürür. Örnek:
```py
import numpy as np

x = np.array([0, 1, -1])

print(np.arcsin(x))
```
**Output:**
```
[0.         1.57079633 1.57079633]
```

<h2 id="1.5"><code>arccos(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x` parametresine girilen array'in tüm değerlerinin ters kosinüsünü alır ve radians cinsinden döndürür. Örnek:
```py
import numpy as np

x = np.array([0, 1, -1])

print(np.arccos(x))
```
**Output:**
```
[1.57079633 0.         3.14159265]
```

<h2 id="1.6"><code>arctan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x` parametresine girilen array'in tüm değerlerinin ters tanjantını alır ve radians cinsinden döndürür. Örnek:
```py
import numpy as np

x = np.array([0, 1, -1])

print(np.arctan(x))
```
**Output:**
```
[0.         0.78539816 0.78539816]
```

<h2 id="1.7"><code>degrees(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x` parametresine girilen array'in tüm değerlerinin derece cinsinden karşılığını alır. Örnek:
```py
import numpy as np

x = np.array([0, np.pi/2, np.pi])

print(np.degrees(x))
```
**Output:**
```
[ 0. 90. 180.]
```

<h2 id="1.8"><code>radians(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x` parametresine girilen array'in tüm değerlerinin radyan cinsinden karşılığını alır. Örnek:
```py
import numpy as np

x = np.array([0, 90, 180])

print(np.radians(x))
```
**Output:**
```
[0.         1.57079633 3.14159265]
```

<h2 id="1.9"><code>deg2rad(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x` parametresine girilen array'in tüm değerlerinin radyan cinsinden karşılığını alır. Örnek:
```py
import numpy as np

x = np.array([0, 90, 180])

print(np.deg2rad(x))
```
**Output:**
```
[0.         1.57079633 3.14159265]
```

<h2 id="1.10"><code>rad2deg(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x` parametresine girilen array'in tüm değerlerinin derece cinsinden karşılığını alır. Örnek:
```py
import numpy as np

x = np.array([0, np.pi/2, np.pi])

print(np.rad2deg(x))
```
**Output:**
```
[ 0. 90. 180.]
```

<h2 id="1.11"><code>unwrap(p, discont=None, axis=- 1, *, period=6.283185307179586)</code> Methodu</h2>

`p` parametresine girilen array'in tüm değerlerinin ters sinüsünü alır ve radians cinsinden döndürür. Örnek:
```py
import numpy as np

x = np.array([0, 1, -1])

print(np.unwrap(x))
```
**Output:**
```
[0.         1.57079633 1.57079633]
```