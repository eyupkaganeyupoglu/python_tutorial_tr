# İçindekiler

- [Arithmetic Functions](#1)
   - [add](#1.1)
   - [subtract](#1.2)
   - [multiply](#1.3)
   - [divide](#1.4)
   - [power](#1.5)
   - [mod](#1.6)
   - [remainder](#1.7)
   - [fmod](#1.8)
   - [absolute](#1.9)
   - [negative](#1.10)
   - [positive](#1.11)
   - [sign](#1.12)
   - [reciprocal](#1.13)
   - [real](#1.14)
   - [imag](#1.15)
   - [conj](#1.16)
   - [angle](#1.17)

<h1 id="1">Arithmetic Functions</h1>

<h2 id="1.1"><code>add(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x1` ve `x2` parametrelerine girilen array'lerin tüm değerlerinin toplamını alır. Örnek:
```py
import numpy as np

x1 = np.array([10, 20, 30])
x2 = np.array([1, 2, 3])

print(np.add(x1, x2))
```
**Output:**
```
[11 22 33]
```

<h2 id="1.2"><code>subtract(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x1` ve `x2` parametrelerine girilen array'lerin tüm değerlerinin farkını alır. Örnek:
```py
import numpy as np

x1 = np.array([10, 20, 30])
x2 = np.array([1, 2, 3])

print(np.subtract(x1, x2))
```
**Output:**
```
[ 9 18 27]
```

<h2 id="1.3"><code>multiply(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x1` ve `x2` parametrelerine girilen array'lerin tüm değerlerinin çarpımını alır. Örnek:
```py
import numpy as np

x1 = np.array([10, 20, 30])

print(np.multiply(x1, 2))
```
**Output:**
```
[20 40 60]
```

<h2 id="1.4"><code>divide(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x1` ve `x2` parametrelerine girilen array'lerin tüm değerlerinin bölümünü alır. Örnek:
```py
import numpy as np

x1 = np.array([10, 20, 30])

print(np.divide(x1, 2))
```
**Output:**
```
[ 5. 10. 15.]
```

<h2 id="1.5"><code>power(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x1` ve `x2` parametrelerine girilen array'lerin tüm değerlerinin üssünü alır. Örnek:
```py
import numpy as np

x1 = np.array([10, 20, 30])

print(np.power(x1, 2))
```
**Output:**
```
[ 100  400  900]
```

<h2 id="1.6"><code>mod(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x1` ve `x2` parametrelerine girilen array'lerin tüm değerlerinin modunu alır. Örnek:
```py
import numpy as np

x1 = np.array([10, 20, 30])

print(np.mod(x1, 2))
```
**Output:**
```
[0 0 0]
```

<h2 id="1.7"><code>remainder(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x1` ve `x2` parametrelerine girilen array'lerin tüm değerlerinin kalanını alır. Örnek:
```py
import numpy as np

x1 = np.array([10, 20, 30])

print(np.remainder(x1, 2))
```
**Output:**
```
[0 0 0]
```

<h2 id="1.8"><code>fmod(x1, x2, /[, out1, out2, where, casting, order, dtype, subok, signature, extobj])</code> Methodu</h2>

`x1` ve `x2` parametrelerine girilen array'lerin tüm değerlerinin kalanını alır. Örnek:
```py
import numpy as np

x1 = np.array([10, 20, 30])

print(np.fmod(x1, 2))
```
**Output:**
```
[0 0 0]
```

<h2 id="1.9"><code>absolute(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x` parametresine girilen array'in tüm değerlerinin mutlak değerini alır. Örnek:
```py
import numpy as np

x = np.array([-1, 2, -3, 4])

print(np.absolute(x))
```
**Output:**
```
[1 2 3 4]
```

<h2 id="1.10"><code>negative(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x` parametresine girilen array'in tüm değerlerinin negatifini alır. Örnek:
```py
import numpy as np

x = np.array([-1, 2, -3, 4])

print(np.negative(x))
```
**Output:**
```
[ 1 -2  3 -4]
```

<h2 id="1.11"><code>positive(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x` parametresine girilen array'in tüm değerlerinin pozitifini alır. Örnek:
```py
import numpy as np

x = np.array([-1, 2, -3, 4])

print(np.positive(x))
```
**Output:**
```
[-1  2 -3  4]
```

<h2 id="1.12"><code>sign(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x` parametresine girilen array'in tüm değerlerinin işaretini alır. Örnek:
```py
import numpy as np

x = np.array([-1, 2, -3, 4])

print(np.sign(x))
```
**Output:**
```
[-1  1 -1  1]
```

<h2 id="1.13"><code>reciprocal(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x` parametresine girilen array'in tüm değerlerinin tersini alır. Örnek:
```py
import numpy as np

x = np.array([1, 2, 3, 4])

print(np.reciprocal(x))
```
**Output:**
```
[1.         0.5        0.33333333 0.25      ]
```

<h2 id="1.14"><code>real(val)</code> Methodu</h2>

`val` parametresine girilen array'in tüm değerlerinin reel kısmını alır. Örnek:
```py
import numpy as np

val = np.array([1+2j, 3+4j, 5+6*1j])

print(np.real(val))
```
**Output:**
```
[1. 3. 5.]
```

<h2 id="1.15"><code>imag(val)</code> Methodu</h2>

`val` parametresine girilen array'in tüm değerlerinin sanal kısmını alır. Örnek:
```py
import numpy as np

val = np.array([1+2j, 3+4j, 5+6*1j])

print(np.imag(val))
```
**Output:**
```
[2. 4. 6.]
```

<h2 id="1.16"><code>conj(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])</code> Methodu</h2>

`x` parametresine girilen array'in tüm değerlerinin kompleks kongüjünü alır. Örnek:
```py
import numpy as np

x = np.array([1+2j, 3+4j, 5+6j])

print(np.conj(x))
```
**Output:**
```
[1.-2.j 3.-4.j 5.-6.j]
```

<h2 id="1.17"><code>angle(z, /, deg=False)</code> Methodu</h2>

`z` parametresine girilen array'in tüm değerlerinin açısını alır. Örnek:
```py
import numpy as np

z = np.array([1+2j, 3+4j, 5+6j])

print(np.angle(z))
```
**Output:**
```
[1.10714872 0.92729522 0.87605805]
```