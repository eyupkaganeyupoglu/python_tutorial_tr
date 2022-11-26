# İçindekiler

- [`ndarray` Attribute'ları](#1)
  - [`shape` Attribute'u](#1.1)
  - [`ndim` Attribute'u](#1.2)
  - [`itemsize` Attribute'u](#1.3)
  - [`size` Attribute'u](#1.4)
  - [`dtype` Attribute'u](#1.5)
  - [`flags` Attribute'u](#1.6)

<h1 id="1"><code>ndarray</code> Attribute'ları</h1>

<h2 id="1.1"><code>shape</code> Attribute'u</h2>

`ndarray.shape` ya da `numpy.shape(a)` şeklinde kullanılabilir. Uygulandığı/`a` parametresine argüman olarak girilen array'in dimension ve her dimension'ındaki element sayısı bilgisini içeren bir tuple döndürür. Örnek:
```py
import numpy as np

a = np.ones((4))
b = np.ones((4, 3))
c = np.ones((4, 3, 2))

print(a, np.shape(a), end="\n-------\n")
print(b, np.shape(b), end="\n-------\n")
print(c, np.shape(c))
```
**Output:**
```
[1. 1. 1. 1.] (4,)
-------
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]] (4, 3)
-------
[[[1. 1.]
  [1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]
  [1. 1.]]] (4, 3, 2)
```
`shape` attribute'u ilgili array'i yeniden şekillendirmek (reshape) için de kullanılabilir. Örnek:
```py
import numpy as np

a = np.ones((4, 3, 2))

print(a, np.shape(a), end="\n-------\n")
a.shape = (4, 6)
print(a, np.shape(a), a.shape)
```
**Output:**
```
[[[1. 1.]
  [1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]
  [1. 1.]]] (4, 3, 2)
-------
[[1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1.]] (4, 6) (4, 6)
```
**Not:** Bu işlemin yapılabilmesi için ilgili array'in eski ve yeni shape'i aynı sayıda elemente sahip olmalıdır aksi halde `ValueError: cannot reshape array of size 24 into shape (4,5)` örneğindeki gibi bir hata döndürür.

<h2 id="1.2"><code>ndim</code> Attribute'u</h2>

`ndarray.ndim` ya da `numpy.ndim(a)` şeklinde kullanılabilir. Uygulandığı/`a` parametresine argüman olarak girilen array'in dimension sayısını döndürür. Örnek:
```py
import numpy as np

a = np.ones((4, 3, 2))

print(np.ndim(a)) # Output: 3
a.shape = (4, 6)
print(np.ndim(a),a.ndim) # Output: 2 2
```

<h2 id="1.3"><code>itemsize</code> Attribute'u</h2>

`ndarray.itemsize` şeklinde kullanılabilir. Uygulandığı array'in her elementinin bellekte kapladığı alanı byte cinsinden döndürür. Örnek:
```py
import numpy as np

a1 = np.ones((5,), dtype=np.int8)
a2 = np.ones((5,), dtype=np.int32)
a3 = np.ones((5,), dtype=np.float16)

print(a1.itemsize) # Output: 1
print(a2.itemsize) # Output: 4
print(a3.itemsize) # Output: 2
```

<h2 id="1.4"><code>size</code> Attribute'u</h2>

`ndarray.size` ya da `numpy.size(a)` şeklinde kullanılabilir. Uygulandığı/`a` parametresine argüman olarak girilen array'in toplam element sayısını döndürür. Örnek:
```py
import numpy as np
a = np.array([[4,2,3,1],[8,5,7,6]])
b = np.array([11,9,12,10])
print(np.size(a)) # Output: 8
print(np.size(b)) # Output: 4
```

<h2 id="1.5"><code>dtype</code> Attribute'u</h2>

`ndarray.dtype` ya da `numpy.dtype(a)` şeklinde kullanılabilir. Uygulandığı/`a` parametresine argüman olarak girilen array'in elementlerinin veri tipini döndürür. Örnek:
```py
import numpy as np

a1 = np.ones((5,), dtype=np.int8)
a2 = np.ones((5,), dtype=np.int32)
a3 = np.ones((5,), dtype=np.float16)

print(a1.dtype) # Output: int8
print(a2.dtype) # Output: int32
print(a3.dtype) # Output: float16
```

<h2 id="1.6"><code>flags</code> Attribute'u</h2>

Bir array'in bellekte nasıl saklandığını gösteren bir özellik objesi (`<class 'numpy.core.multiarray.flagsobj'>`) döndürür. Örnek:
```py
import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a.flags)
```
**Output:**
```
  C_CONTIGUOUS : True
  F_CONTIGUOUS : True
  OWNDATA : True
  WRITEABLE : True
  ALIGNED : True
  WRITEBACKIFCOPY : False
```
Buradaki özelliklerin anlamları şu şekildedir:
- `C_CONTIGUOUS` (C): True ise array'in bellekte C dilindeki gibi sıralandığı anlamına gelir (C-style contiguous segment).
- `F_CONTIGUOUS` (F): True ise array'in bellekte Fortran dilindeki gibi sıralandığı anlamına gelir (Fortran-style contiguous segment).
- `OWNDATA` (O): True ise array'in bellekteki verilerini kendi sakladığı (yani dizi, kullandığı belleğin sahibi) ya da başka bir objeden ödünç aldığı anlamına gelir.
- `WRITEABLE` (W): True ise array'in bellekteki verilerini değiştirebilir (yani array'in immutable olmadığı) anlamına gelir. Bunu False olarak ayarlamak verileri kilitler ve salt okunur (read-only) yapar.
- `ALIGNED` (A): True ise array'in verilerini ve tüm elementleri, donanım için uygun şekilde hizalanmış anlamına gelir.
- `UPDATEIFCOPY` (U): True ise array'in bellekteki verilerini değiştirdiğinizde, değişikliklerin başka bir array'e yazılacağı (yani temel dizi bu dizinin içeriğiyle güncelleneceği) anlamına gelir. Bu özellik, array'in bellekteki verilerini kopyaladığından dolayı performansı düşürür.