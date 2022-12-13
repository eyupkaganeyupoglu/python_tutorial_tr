# İçindekiler

- [Sort, Search & Counting Functions](#1)
   - [sort](#1.1)
   - [argsort](#1.2)
   - [lexsort](#1.3)
   - [argmax](#1.4)
   - [argmin](#1.5)
   - [nonzero](#1.6)
   - [where](#1.7)
   - [extract](#1.8)

<h1 id="1">Sort, Search & Counting Functions</h1>

NumPy'da çeşitli sorting fonksiyonları bulunmaktadır. Bu fonksiyonlar speed of execution, worst case performance, workspace required, stability of algorithms ile karakterize edilen farklı sorting algoritmaları uygular. 4 sıralama algoritması bulunmaktadır:
|   **kind**    | **speed** | **worst case** | **work space** | **stable** |
| :-----------: | :-------: | :------------: | :------------: | :--------: |
| `'quicksort'` |     1     |     O(n^2)     |       0        |     no     |
| `'mergesort'` |     2     |  O(n*log(n))   |      ~n/2      |    yes     |
|  `'timsort'`  |     2     |  O(n*log(n))   |      ~n/2      |    yes     |
| `'heapsort'`  |     3     |  O(n*log(n))   |       0        |     no     |

<h2 id="1.1"><code>sort(a, /, axis=-1, kind='quicksort', order=None)</code> Methodu</h2>

`a` parametresine girilen array'i sıralar. Örnek:
```py
import numpy as np

a = np.array([[3, 7], [9, 1]])

print(np.sort(a))
```
**Output:**
```
[[3 7]
  [1 9]]
```

<h2 id="1.2"><code>argsort(a, /, axis=-1, kind='quicksort', order=None)</code> Methodu</h2>

`a` parametresine girilen array'in sıralanmış haliyle aynı boyutlu bir array döndürür. Örnek:
```py
import numpy as np

a = np.array([[3, 7], [9, 1]])

print(np.argsort(a))
```
**Output:**
```
[[0 1]
  [1 0]]
```

<h2 id="1.3"><code>lexsort(keys, /, axis=-1)</code> Methodu</h2>

`keys` parametresine girilen array'in sıralanmış haliyle aynı boyutlu bir array döndürür. Örnek:
```py
import numpy as np

x = np.array([3, 1, 2])
y = np.array([2, 3, 1])

print(np.lexsort((x, y)))
```
**Output:**
```
[1 2 0]
```

<h2 id="1.4"><code>argmax(a, /, axis=None, out=None)</code> Methodu</h2>

`a` parametresine girilen array'in en büyük değerini döndürür. Örnek:
```py
import numpy as np

a = np.array([1, 2, 3, 4])

print(np.argmax(a))
```
**Output:**
```
3
```

<h2 id="1.5"><code>argmin(a, /, axis=None, out=None)</code> Methodu</h2>

`a` parametresine girilen array'in en küçük değerini döndürür. Örnek:
```py
import numpy as np

a = np.array([1, 2, 3, 4])

print(np.argmin(a))
```
**Output:**
```
0
```

<h2 id="1.6"><code>nonzero(a)</code> Methodu</h2>

`a` parametresine girilen array'de 0 olmayan değerlerin indexlerini döndürür. Örnek:
```py
import numpy as np

a = np.array([[1, 2, 3], [0, 0, 0], [4, 5, 6]])

print(np.nonzero(a))
```
**Output:**
```
(array([0, 0, 0, 2, 2, 2]), array([0, 1, 2, 0, 1, 2]))
```

<h2 id="1.7"><code>where(condition, /, x=None, y=None)</code> Methodu</h2>

`condition` parametresine girilen array'de `True` olan (yani `0` olmayan) değerlerin indexlerini döndürür. Örnek:
```py
import numpy as np

a = np.array([[1, 2, 3], [0, 0, 0], [4, 5, 6]])

print(np.where(a > 2))
```
**Output:**
```
(array([0, 2, 2, 2]), array([2, 0, 1, 2]))
```

<h2 id="1.8"><code>extract(condition, arr)</code> Methodu</h2>

`condition` parametresine girilen array'de 0 olmayan değerlerin indexlerini `arr` parametresine girilen array'den alır. Örnek:
```py
import numpy as np

a = np.array([[1, 2, 3], [0, 0, 0], [4, 5, 6]])

print(np.extract(a > 2, a))
```
**Output:**
```
[3 4 5 6]
```