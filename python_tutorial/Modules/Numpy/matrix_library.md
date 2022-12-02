# İçindekiler

- [Matrix Library](#1)
  - [`matlib.empty`](#1.1)
  - [`matlib.zeros`](#1.2)
  - [`matlib.ones`](#1.3)
  - [`matlib.eye`](#1.4)
  - [`matlib.identity`](#1.5)
  - [`matlib.rand`](#1.6)

<h1 id="1">Matrix Library</h1>

<h2 id="1.1"><code>matlib.empty(shape, dtype=float, order='C')</code> Methodu</h2>

`shape` parametresine girilen boyutta boş bir array oluşturur. Örnek:
  ```py
  import numpy.matlib

  print(numpy.matlib.empty((2, 2)))
  ```
  **Output:**
  ```
  [[1.36162415e-311 1.36162415e-311]
  [1.36162415e-311 1.36162415e-311]]
  ```

<h2 id="1.2"><code>matlib.zeros(shape, dtype=float, order='C')</code> Methodu</h2>

`shape` parametresine girilen boyutta sıfırlardan oluşan bir array oluşturur. Örnek:
  ```py
  import numpy.matlib

  print(numpy.matlib.zeros((2, 2)))
  ```
  **Output:**
  ```
  [[0. 0.]
  [0. 0.]]
  ```

<h2 id="1.3"><code>matlib.ones(shape, dtype=None, order='C')</code> Methodu</h2>

`shape` parametresine girilen boyutta birlerden oluşan bir array oluşturur. Örnek:
  ```py
  import numpy.matlib

  print(numpy.matlib.ones((2, 2)))
  ```
  **Output:**
  ```
  [[1. 1.]
  [1. 1.]]
  ```

<h2 id="1.4"><code>matlib.eye(n, M=None, k=0, dtype=float, order='C')</code> Methodu</h2>

`n` parametresine girilen boyutta birim matris oluşturur. `M` parametresi girilmezse `n` parametresi ile aynı değer alır (yani kare matris olur). `k` parametresi ise birim matrisin ana köşegeninin sağa veya sola kaydırılmasını sağlar. Örnek:
  ```py
  import numpy.matlib

  print(numpy.matlib.eye(n=3, M=4, k=0, dtype=float))
  ```
  **Output:**
  ```
  [[1. 0. 0. 0.]
  [0. 1. 0. 0.]
  [0. 0. 1. 0.]]
  ```

<h2 id="1.5"><code>matlib.identity(n, dtype=None)</code> Methodu</h2>

`n` parametresine girilen boyutta birim matris oluşturur. Örnek:
  ```py
  import numpy.matlib

  print(numpy.matlib.identity(5, dtype=float))
  ```
  **Output:**
  ```
  [[1. 0. 0. 0. 0.]
  [0. 1. 0. 0. 0.]
  [0. 0. 1. 0. 0.]
  [0. 0. 0. 1. 0.]
  [0. 0. 0. 0. 1.]]
  ```

<h2 id="1.6"><code>matlib.rand(*args, **kwargs)</code> Methodu</h2>

`matlib.rand(d0, d1, ..., dn)` şek `d0`, `d1`, ..., `dn` parametrelerine girilen boyutta rastgele değerlerden oluşan bir array oluşturur. Örnek:
```py
import numpy.matlib

print(numpy.matlib.rand(3, 3))
```
**Output:**
```
[[0.59066705 0.50517741 0.55721634]
[0.82512513 0.54510793 0.6141953 ]
[0.18272202 0.66594261 0.66823337]]
```