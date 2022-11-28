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