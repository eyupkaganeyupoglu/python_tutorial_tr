# İçindekiler

- [Linear Algebra](#1)
  - [`linalg.dot(a, b, out=None)`](#1)
  - [`linalg.vdot(a, b)`](#1)
  - [`linalg.inner(a, b)`](#1)
  - [`linalg.matmul(x1, x2, *args, **kwargs)`](#1)
  - [`linalg.determinant(a)`](#1)
  - [`linalg.solve(a, b)`](#1)
  - [`linalg.inv(a)`](#1)

<h1 id="1">Linear Algebra</h1>

NumPy paketi bir Lineer Cebir kitaplığı (`numpy.linalg`) içerir. Bu modül, matrisler üzerinde çeşitli matematiksel işlemler yapmamızı sağlar.

<h2 id="1.1"><code>linalg.dot(a, b, out=None)</code> Methodu</h2>

`a` ve `b` parametrelerine girilen matrisleri çarpar. Örnek:
  ```py
  import numpy as np

  a = np.array([[1, 0], [0, 1]])
  b = np.array([[4, 1], [2, 2]])

  print(np.dot(a, b))
  ```
  **Output:**
  ```
  [[4 1]
  [2 2]]
  ```

<h2 id="1.2"><code>linalg.vdot(a, b)</code> Methodu</h2>

`a` ve `b` parametrelerine girilen vektörleri çarpar. Örnek:
  ```py
  import numpy as np

  a = np.array([1, 4, 5])
  b = np.array([7, 2, 12])

  print(np.vdot(a, b))
  ```
  **Output:**
  ```
  61
  ```

<h2 id="1.3"><code>linalg.inner(a, b)</code> Methodu</h2>

`a` ve `b` parametrelerine girilen matrisleri iç çarpımı yapar. Örnek:
  ```py
  import numpy as np

  a = np.array([[1, 0], [0, 1]])
  b = np.array([[4, 1], [2, 2]])

  print(np.inner(a, b))
  ```
  **Output:**
  ```
  [[4 1]
  [2 2]]
  ```

<h2 id="1.4"><code>linalg.matmul(x1, x2, *args, **kwargs)</code> Methodu</h2>

`x1` ve `x2` parametrelerine girilen matrisleri çarpar. Örnek:
  ```py
  import numpy as np

  a = np.array([[1, 0], [0, 1]])
  b = np.array([[4, 1], [2, 2]])

  print(np.matmul(a, b))
  ```
  **Output:**
  ```
  [[4 1]
  [2 2]]
  ```

<h2 id="1.5"><code>linalg.determinant(a)</code> Methodu</h2>

`a` parametresine girilen matrisin determinantını hesaplar. Örnek:
  ```py
  import numpy as np

  a = np.array([[1, 2], [3, 4]])

  print(np.linalg.det(a))
  ```
  **Output:**
  ```
  -2.0000000000000004
  ```

<h2 id="1.6"><code>linalg.solve(a, b)</code> Methodu</h2>

`a` parametresine girilen matrisin `b` parametresine girilen vektörü çözmesini sağlar. Örnek:
  ```py
  import numpy as np

  a = np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]])
  b = np.array([6, -4, 27])

  print(np.linalg.solve(a, b))
  ```
  **Output:**
  ```
  [ 5.  3. -2.]
  ```

<h2 id="1.7"><code>linalg.inv(a)</code> Methodu</h2>

`a` parametresine girilen matrisin tersini hesaplar. Örnek:
  ```py
  import numpy as np

  a = np.array([[1, 2], [3, 4]])

  print(np.linalg.inv(a))
  ```
  **Output:**
  ```
  [[-2.   1. ]
  [ 1.5 -0.5]]
  ```