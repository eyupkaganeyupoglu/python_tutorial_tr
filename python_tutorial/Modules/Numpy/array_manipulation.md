# İçindekiler

-[Changing Shape](#1)
-[](#)
-[](#)
-[](#)
-[](#)
-[](#)
-[](#)
-[](#)
-[](#)
-[](#)
-[](#)
-[](#)

<h1 id="1">Changing Shape</h1>

<h2 id="1.1"><code>reshape(a, newshape, order='C')</code> Methodu</h2>

`a` parametresine argüman olarak girilen array'i `newshape` parametresine girilen tuple'da belirtilene göre yeniden boyutlandırdığı bir array öbjesi döndürür (yani `a` parametresine argüman olarak girilen array'i etkilemez). Örnek:
```py
import numpy as np

a = np.ones((4, 3, 2))

print(a, np.shape(a), end="\n-------\n")
b = a.reshape((4, 6))
print(a, np.shape(a), end="\n-------\n")
print(b, np.shape(b))
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
[1. 1. 1. 1. 1. 1.]] (4, 6)
```

<h2 id="1.2"><code>ndarray.flat</code> Methodu</h2>

Uygulandığı `ndarray` objesinin içindeki elemetleri tek bir boyutta döndürür. Örnek:
```py
import numpy as np

a = np.arange(8).reshape(2,4)
print(a, end="\n-------\n")
for i in a.flat:
    print(i, end=", ")
```
**Output:**
```
[[0 1 2 3]
[4 5 6 7]]
-------
0, 1, 2, 3, 4, 5, 6, 7,
```

<h2 id="1.3"><code>ndarray.flatten(order='C')</code> Methodu</h2>

Uygulandığı `ndarray` objesini tek boyutlu bir array'e dönüştürür. Örnek:
```py
import numpy as np

a = np.arange(8).reshape(2,4)
print(a, end="\n-------\n")
print(a.flatten(), end="\n-------\n")
print(a.flatten(order='F'))
```
**Output:**
```
[[0 1 2 3]
[4 5 6 7]]
-------
[0 1 2 3 4 5 6 7]
-------
[0 4 1 5 2 6 3 7]
```

<h2 id="1.4"><code>ndarray.ravel(order='C')</code> Methodu</h2>

`a` parametresine argüman olarak girilen array'i tek boyutlu bir array'e dönüştürür. Örnek:
```py
import numpy as np

a = np.arange(8).reshape(2,4)
print(a, end="\n-------\n")
print(np.ravel(a))
print(a.ravel(), end="\n-------\n")
print(np.ravel(a, order='F'))
print(a.ravel(order='F'))
```
**Output:**
```
[[0 1 2 3]
[4 5 6 7]]
-------
[0 1 2 3 4 5 6 7]
[0 1 2 3 4 5 6 7]
-------
[0 4 1 5 2 6 3 7]
[0 4 1 5 2 6 3 7]
```

<h1 id="2">Transposing Arrays</h1>

<h2 id="2.1"><code>transpose</code> Methodu</h2>

`numpy.transpose(a, axes=None)` ya da `ndarray.transpose(axes=None)` ya da `ndarray.T` methodları ile `ndarray` şeklinde kullanılabilir. İstenilen array'in transpozesini döndürür. Örnek:
```py
import numpy as np

a = np.arange(12).reshape(3,4)
print(a, end="\n-------\n")
print(np.transpose(a))
print(a.transpose())
print(a.T)
```
**Output:**
```
[[ 0  1  2  3]
[ 4  5  6  7]
[ 8  9 10 11]]
-------
[[ 0  4  8]
[ 1  5  9]
[ 2  6 10]
[ 3  7 11]]
[[ 0  4  8]
[ 1  5  9]
[ 2  6 10]
[ 3  7 11]]
[[ 0  4  8]
[ 1  5  9]
[ 2  6 10]
[ 3  7 11]]
```

<h2 id="2.2"><code>rollaxis(a, axis, start=0)</code> Methodu</h2>

`a` parametresine argüman olarak girilen array'in `axis` parametresine girilen ekseni `start` parametresine girilen konuma taşır. Örnek:
```py
import numpy as np

a = np.arange(8).reshape(2,2,2)
print(a, end="\n-------\n")
print(np.rollaxis(a, 2))
print(np.rollaxis(a, 2, 1))
```
**Output:**
```
[[[0 1]
  [2 3]]

[[4 5]
  [6 7]]]
-------
[[[0 2]
  [4 6]]

[[1 3]
  [5 7]]]
-------
[[[0 2]
  [1 3]]

[[4 6]
  [5 7]]]
```

<h2 id="2.3"><code>swapaxes(a, axis1, axis2)</code> Methodu</h2>

`a` parametresine argüman olarak girilen array'in `axis1` ve `axis2` parametrelerine girilen eksenleri yer değiştirir. Örnek:
```py
import numpy as np

a = np.arange(8).reshape(2,2,2)
print(a, end="\n-------\n")
print(np.swapaxes(a, 2, 0), end="\n-------\n")
print(np.swapaxes(a, 1, 0))
```
**Output:**
```
[[[0 1]
  [2 3]]

[[4 5]
  [6 7]]]
-------
[[[0 4]
  [2 6]]

[[1 5]
  [3 7]]]
-------
[[[0 1]
  [4 5]]

[[2 3]
  [6 7]]]
```

<h1 id="3">Changing Dimensions</h1>

<h2 id="3.1"><code>broadcast(a, b)</code> Methodu</h2>

Parametre olarak array_like objeler kabul eder. Verilen argümanları birbirine karşı yayımlar (broadcast) ve sonucu kapsayan bir broadcast objesi döndürür. Örnek:
```py
import numpy as np

a = np.arange(4).reshape(1,4)
b = np.arange(8).reshape(2,4)
c = np.broadcast(a, b)
print(a, end="\n-------\n")
print(b, end="\n-------\n")
print(c, c.index, c.shape, c.size, c.ndim, c.iters, sep="\n")
```
**Output:**
```
[[0 1 2 3]]
-------
[[0 1 2 3]
[4 5 6 7]]
-------
<numpy.broadcast object at 0x00000220CADF8710>
0
(2, 4)
8
2
(<numpy.flatiter object at 0x00000220CAC968C0>, <numpy.flatiter object at 0x00000220CAC97310>)
```

<h2 id="3.2"><code>broadcast_to(array, shape, subok=False)</code> Methodu</h2>

`array` parametresine argüman olarak girilen array'i `shape` parametresine girilen şekle yayımlar (broadcast). Örnek:
```py
import numpy as np

a = np.arange(4).reshape(1,4)
print(a, end="\n-------\n")
print(np.broadcast_to(a, (4,4)))
```
**Output:**
```
[[0 1 2 3]]
-------
[[0 1 2 3]
  [0 1 2 3]
  [0 1 2 3]
  [0 1 2 3]]
```

<h2 id="3.3"><code>expand_dims(a, axis)</code> Methodu</h2>

`a` parametresine argüman olarak girilen array'in `axis` parametresine girilen ekseninin genişletildiği bir array döndürür (yani asıl array'i değiştirmez). Örnek:
```py
import numpy as np

a = np.arange(1,5).reshape(2,2)

print("a:\n", a, "\nShape:", a.shape, "\nndim:", a.ndim, end="\n-------\n")
b = np.expand_dims(a, axis = 0)
print("b = np.expand_dims(x, axis = 0):\n", b, "\nShape:", b.shape, "\nndim:", b.ndim, end="\n-------\n")
c = np.expand_dims(a, axis = 1)
print("c = np.expand_dims(x, axis = 1):\n", c, "\nShape:", c.shape, "\nndim:", c.ndim)
```
**Output:**
```
a:
[[1 2]
  [3 4]]
Shape: (2, 2)
ndim: 2
-------
b = np.expand_dims(x, axis = 0):
[[[1 2]
  [3 4]]]
Shape: (1, 2, 2)
ndim: 3
-------
c = np.expand_dims(x, axis = 1):
[[[1 2]]
[[3 4]]]
Shape: (2, 1, 2)
ndim: 3
```

<h2 id="3.4"><code>squeeze(a, axis=None)</code> Methodu</h2>

 `a` parametresine argüman olarak girilen array'den `axis` parametresine girilen eksenleri kaldırır. Örnek:
```py
import numpy as np

a = np.arange(9).reshape(1,3,3)

print("a:\n", a, "\nShape:", a.shape, "\nndim:", a.ndim, end="\n-------\n")
b = np.squeeze(a, axis = 0)
print("b = np.squeeze(x, axis = 0):\n", b, "\nShape:", b.shape, "\nndim:", b.ndim)
```
**Output:**
```
a:
[[[0 1 2]
  [3 4 5]
  [6 7 8]]]
Shape: (1, 3, 3)
ndim: 3
-------
b = np.squeeze(x, axis = 0):
[[0 1 2]
[3 4 5]
[6 7 8]]
Shape: (3, 3)
ndim: 2
```

<h1 id="4">Joining Arrays</h1>

<h2 id="4.1"><code>concatenate((a1, a2, ...), axis=0, out=None)</code> Methodu</h2>

`(a1, a2, ...)` parametrelerine argüman olarak girilen array'leri `axis` parametresine girilen **mevcut** eksen üzerinde birleştirir. Örnek:
```py
import numpy as np

a = np.arange(4).reshape(1,4)
b = np.arange(4,8).reshape(1,4)
print(a, end="\n-------\n")
print(b, end="\n-------\n")
print(np.concatenate((a,b), axis=0), "\nShape:", a.shape, "\nndim:", a.ndim, end="\n-------\n")
print(np.concatenate((a,b), axis=1), "\nShape:", a.shape, "\nndim:", a.ndim)
```
**Output:**
```
[[0 1 2 3]]
-------
[[4 5 6 7]]
-------
[[0 1 2 3]
[4 5 6 7]]
Shape: (1, 4)
ndim: 2
-------
[[0 1 2 3 4 5 6 7]]
Shape: (1, 4)
ndim: 2
```

<h2 id="4.2"><code>stack(arrays, axis=0, out=None)</code> Methodu</h2>

`arrays` parametresine argüman olarak girilen array'leri `axis` parametresine girilen **yeni** eksen üzerinde birleştirir. Örnek:
```py
import numpy as np

a = np.arange(4).reshape(1,4)
b = np.arange(4,8).reshape(1,4)
print(a, end="\n-------\n")
print(b, end="\n-------\n")
print(np.stack((a,b), axis=0), "\nShape:", a.shape, "\nndim:", a.ndim, end="\n-------\n")
print(np.stack((a,b), axis=1), "\nShape:", a.shape, "\nndim:", a.ndim, end="\n-------\n")
print(np.stack((a,b), axis=2), "\nShape:", a.shape, "\nndim:", a.ndim)
```
**Output:**
```
[[0 1 2 3]]
-------
[[4 5 6 7]]
-------
[[[0 1 2 3]]

[[4 5 6 7]]]
Shape: (1, 4)
ndim: 2
-------
[[[0 1 2 3]
  [4 5 6 7]]]
Shape: (1, 4)
ndim: 2
-------
[[[0 4]
  [1 5]
  [2 6]
  [3 7]]]
Shape: (1, 4)
ndim: 2
```

<h2 id="4.3"><code>hstack(tup)</code> Methodu</h2>

`tup` parametresine argüman olarak girilen tuple'ı yatay olarak birleştirir. Örnek:
```py
import numpy as np

a = np.arange(4).reshape(1,4)
b = np.arange(4,8).reshape(1,4)
print(a, end="\n-------\n")
print(b, end="\n-------\n")
print(np.hstack((a,b)))
```
**Output:**
```
[[0 1 2 3]]
-------
[[4 5 6 7]]
-------
[[0 1 2 3 4 5 6 7]]
```

<h2 id="4.4"><code>vstack(tup)</code> Methodu</h2>

`tup` parametresine argüman olarak girilen tuple'ı dikey olarak birleştirir. Örnek:
```py
import numpy as np

a = np.arange(4).reshape(1,4)
b = np.arange(4,8).reshape(1,4)
print(a, end="\n-------\n")
print(b, end="\n-------\n")
print(np.vstack((a,b)))
```
**Output:**
```
[[0 1 2 3]]
-------
[[4 5 6 7]]
-------
[[0 1 2 3]
[4 5 6 7]]
```

<h2 id="4.5"><code>dstack(tup)</code> Methodu</h2>

`tup` parametresine argüman olarak girilen tuple'ı derinlik olarak birleştirir. Örnek:
```py
import numpy as np

a = np.arange(4).reshape(1,1,4)
b = np.arange(4,8).reshape(1,1,4)
print(a, end="\n-------\n")
print(b, end="\n-------\n")
print(np.dstack((a,b)))
```
**Output:**
```
[[[0 1 2 3]]]
-------
[[[4 5 6 7]]]
-------
[[[0 1 2 3 4 5 6 7]]]
```

<h1 id="5">Splitting Arrays</h1>

<h2 id="5.1"><code>split(ary, indices_or_sections, axis=0)</code> Methodu</h2>

`ary` parametresine argüman olarak girilen array'i `indices_or_sections` parametresine girilen değerlere göre bölerek tuple olarak döndürür. Örnek:
```py
import numpy as np

a = np.arange(8).reshape(2,4)
print(a, end="\n-------\n")
print(np.split(a, 2, axis=0), end="\n-------\n") # 2 parçaya böl
print(np.split(a, 2, axis=1), end="\n-------\n") # 2 parçaya böl
print(np.split(a, [1,3], axis=1)) # 1. ve 3. index'e kadar olanları birleştir
```
**Output:**
```
[[0 1 2 3]
  [4 5 6 7]]
-------
[array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]])]
-------
[array([[0, 1], [4, 5]]), array([[2, 3], [6, 7]])]
-------
[array([[0, 1]]), array([[2, 3], [4, 5]]), array([[6, 7]])]
```

<h2 id="5.2"><code>hsplit(ary, indices_or_sections)</code> Methodu</h2>

`ary` parametresine argüman olarak girilen array'i `indices_or_sections` parametresine girilen değerlere göre yatay olarak bölerek tuple olarak döndürür. Örnek:
```py
import numpy as np

a = np.arange(8).reshape(2,4)
print(a, end="\n-------\n")
print(np.hsplit(a, 2), end="\n-------\n") # 2 parçaya böl
print(np.hsplit(a, [1,3])) # 1. ve 3. index'e kadar olanları birleştir
```
**Output:**
```
[[0 1 2 3]
  [4 5 6 7]]
-------
[array([[0, 1], [4, 5]]), array([[2, 3], [6, 7]])]
-------
[array([[0], [4]]), array([[1, 2], [5, 6]]), array([[3], [7]])]
```

<h2 id="5.3"><code>vsplit(ary, indices_or_sections)</code> Methodu</h2>

`ary` parametresine argüman olarak girilen array'i `indices_or_sections` parametresine girilen değerlere göre dikey olarak bölerek tuple olarak döndürür. Örnek:
```py
import numpy as np

a = np.arange(8).reshape(2,4)
print(a, end="\n-------\n")
print(np.vsplit(a, 2), end="\n-------\n")
print(np.vsplit(a, [1,3]))
```
**Output:**
```
[[0 1 2 3]
  [4 5 6 7]]
-------
[array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]])]
-------
[array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([], shape=(0, 4), dtype=int32)]
```

<h2 id="5.4"><code>dsplit(ary, indices_or_sections)</code> Methodu</h2>

`ary` parametresine argüman olarak girilen array'i `indices_or_sections` parametresine girilen değerlere göre derinlik olarak bölerek tuple olarak döndürür. Örnek:
```py
import numpy as np

a = np.arange(8).reshape(2,2,2)
print(a, end="\n-------\n")
print(np.dsplit(a, 2), end="\n-------\n")
print(np.dsplit(a, [1,3]))
```
**Output:**
```
[[[0 1]
  [2 3]]

  [[4 5]
  [6 7]]]
-------
[array([[[0], [2]], [[4], [6]]]), array([[[1], [3]], [[5], [7]]])]
-------
[array([[[0]], [[4]]]), array([[[1]], [[5]]]), array([[[2]], [[6]]]), array([[[3]], [[7]]])]
```

<h2 id="5.5"><code>array_split(ary, indices_or_sections, axis=0)</code> Methodu</h2>

`ary` parametresine argüman olarak girilen array'i `indices_or_sections` parametresine girilen değerlere göre bölerek tuple olarak döndürür. `split()` fonksiyonu ile aynı işlevi görür, fakat `split()` fonksiyonunda bölme işlemi sabit bir şekilde yapılırken, `array_split()` fonksiyonunda bölme işlemi farklılık gösterebilir. Örnek:
```py
import numpy as np

a = np.arange(8).reshape(2,4)
print(a, end="\n-------\n")
print(np.array_split(a, 3, axis=1), end="\n-------\n")
print(np.array_split(a, 3, axis=0))
```
**Output:**
```
[[0 1 2 3]
  [4 5 6 7]]
-------
[array([[0, 1], [4, 5]]), array([[2, 3], [6, 7]]), array([], shape=(2, 0), dtype=int32)]
-------
[array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([], shape=(0, 4), dtype=int32)]
```

<h1 id="6">Adding/Removing Elements</h1>

<h2 id="6.1"><code>resize(a, new_shape)</code> Methodu</h2>

`a` parametresine argüman olarak girilen array'in boyutunu `new_shape` parametresine girilen boyuta çevirir. Örnek:
```py
import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a, end="\n-------\n")
print(np.resize(a, (3,2)), end="\n-------\n")
print(np.resize(a, (3,3)))
```
**Output:**
```
[[1 2 3]
  [4 5 6]]
-------
[[1 2]
  [3 4]
  [5 6]]
-------
[[1 2 3]
  [4 5 6]
  [1 2 3]]
```

<h2 id="6.2"><code>append(arr, values, axis=None)</code> Methodu</h2>

`arr` parametresine argüman olarak girilen array'in sonuna `values` parametresine girilen değeri ekler. `axis` parametresi girilirse, `values` parametresine girilen değerler `axis` parametresine girilen değere göre eklenir. Örnek:
```py
import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a, end="\n-------\n")
print(np.append(a, [7,8,9]), end="\n-------\n")
print(np.append(a, [[7,8,9]], axis=0), end="\n-------\n")
print(np.append(a, [[5,5,5],[7,8,9]], axis=1))
```
**Output:**
```
[[1 2 3]
  [4 5 6]]
-------
[1 2 3 4 5 6 7 8 9]
-------
[[1 2 3]
  [4 5 6]
  [7 8 9]]
-------
[[1 2 3 5 5 5]
  [4 5 6 7 8 9]]
```

<h2 id="6.3"><code>insert(arr, obj, values, axis=None)</code> Methodu</h2>

`arr` parametresine argüman olarak girilen array'in `obj` parametresine girilen değerlerin yerine (yani bulunduğu index'e) `values` parametresine girilen değerleri ekler. `axis` parametresi girilirse, `values` parametresine girilen değerler `axis` parametresine girilen değere göre eklenir. Örnek:
```py
import numpy as np

a = np.array([[1,2],[3,4],[5,6]])
print(a, end="\n-------\n")
print(np.insert(a, 3, [11,12]), end="\n-------\n")
print(np.insert(a, 1, [11], axis=0), end="\n-------\n")
print(np.insert(a, 1, 11, axis=1))
```
**Output:**
```
[[1 2]
  [3 4]
  [5 6]]
-------
[ 1  2  3 11 12  4  5  6]
-------
[[ 1  2]
  [11 11]
  [ 3  4]
  [ 5  6]]
-------
[[ 1 11  2]
  [ 3 11  4]
  [ 5 11  6]]
```

<h2 id="6.4"><code>delete(arr, obj, axis=None)</code> Methodu</h2>

`arr` parametresine argüman olarak girilen array'in `obj` parametresine girilen değerlerin yerindeki (yani bulunduğu index'deki) değerleri siler. `axis` parametresi girilirse, `obj` parametresine girilen değerler `axis` parametresine girilen değere göre silinir. Örnek:
```py
import numpy as np

a = np.arange(12).reshape(3,4)
print(a, end="\n-------\n")
print(np.delete(a, 5), end="\n-------\n")
print(np.delete(a, 1, axis=0), end="\n-------\n")
print(np.delete(a, [1,3], axis=1))
```
**Output:**
```
[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]
-------
[ 0  1  2  3  4  6  7  8  9 10 11]
-------
[[0 1 2 3]
  [8 9 10 11]]
-------
[[ 0  2]
  [ 4  6]
  [ 8 10]]
```

<h2 id="6.5"><code>unique(arr, return_index=False, return_inverse=False, return_counts=False, axis=None)</code> Methodu</h2>

`arr` parametresine argüman olarak girilen array'deki tekrar eden değerlerinden bir tane bulunan sorted bir array döndürür.
```py
import numpy as np

a = np.array([5,2,6,2,7,5,6,8,2,9])
print("a:\n", a)
arr_rtn = np.unique(a)
print("arr_rtn:\n", arr_rtn)
```
**Output:**
```
a:
 [5 2 6 2 7 5 6 8 2 9]
arr_rtn:
 [2 5 6 7 8 9]
```
- `return_index` parametresi `True` olarak girilirse, `arr_rtn` array'inin elementlerinin `a` array'inde ilk bulunduğu index değerlerini içeren bir array döndürür. Örnek:
  ```py
  import numpy as np

  a = np.array([5,2,6,2,7,5,6,8,2,9])
  print("a:\n", a)
  ar, return_index_rtn = np.unique(a, return_index=True)
  print("ar:\n", ar)
  print("return_index_rtn:\n", return_index_rtn)
  ```
  **Output:**
  ```
  a:
  [5 2 6 2 7 5 6 8 2 9]
  arr_rtn:
  [2 5 6 7 8 9]
  return_index_rtn:
  [1 0 2 4 7 9]
  ```
  Örneğin `arr_rtn` array'indeki `2` değeri `a` array'inde ilk olarak 1. index'de bulunduğu için `return_index_rtn` array'inin 0. index'inin değeri `1`'dir.

- `return_inverse` parametresi `True` olarak girilirse, `a` array'indeki elementlerin `arr_rtn` array'indeki karşılıklarının index değerlerini içeren bir array döndürür. Örnek:
  ```py
  import numpy as np

  a = np.array([5,2,6,2,7,5,6,8,2,9])
  print("a:\n", a)
  arr_rtn, return_inverse_rtn = np.unique(a, return_inverse=True)
  print("arr_rtn:\n", arr_rtn)
  print("return_inverse_rtn:\n", return_inverse_rtn)
  ```
  **Output:**
  ```
  a:
  [5 2 6 2 7 5 6 8 2 9]
  arr_rtn:
  [2 5 6 7 8 9]
  return_inverse_rtn:
  [1 0 2 0 3 1 2 4 0 5]
  ```
  Örneğin `a` array'inin 4. index'indeki `7` elementinin `return_inverse_rtn` array'inde aynı indexdeki karşılığının `3` olması, `arr_rtn` array'inde `7` elementinin 3. index'de bulunmasından dolayıdır.

- `return_counts` parametresi `True` olarak girilirse, `arr_rtn` array'inin elementlerinin `a` array'inde kaç defa tekrar ettiği bilgisini içeren bir array döndürür. Örnek:  
  ```py
  import numpy as np

  a = np.array([5,2,6,2,7,5,6,8,2,9])
  print("a:\n", a)
  arr_rtn, return_counts_rtn = np.unique(a, return_counts=True)
  print("arr_rtn:\n", arr_rtn)
  print("return_counts_rtn:\n", return_counts_rtn)
  ```
  **Output:**
  ```
  a:
  [5 2 6 2 7 5 6 8 2 9]
  arr_rtn:
  [2 5 6 7 8 9]
  return_counts_rtn:
  [3 2 2 1 1 1]
  ```
  Örneğin `arr_rtn` array'indeki 0. indexinde bulunan `2` elementinin `a` array'inde 3 defa tekrar ettiği için `return_counts_rtn` array'indeki 0. index'inin değeri `3`'tür.

**Not:** `axis` parametresi ile istenilen boyutta `unique` işlemi yapılabilir/sınırlandırılabilir.