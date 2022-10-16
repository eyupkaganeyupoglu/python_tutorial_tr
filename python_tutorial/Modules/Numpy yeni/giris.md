# İçindekiler

- [Numpy Giriş](#1)

<h1 id="1">Numpy Giriş</h1>

<h2 id="1.1">Numpy Nedir</h2>

Numpy,
- science ve engineering alanlarında sıkça kullanılan open source bir kütüphanedir.
- Numerical data'lar ile çalışmak için evrensel bir standarttır.
- Kendi başına bir işe yaramaz ama Pandas, SciPy, Matplotlib, scikit-learn, scikit-image ve diğer birçok data science ve scientific gibi birçok Python paketinde; veri manipülasyonu, veri bilimi, yapay zeka gibi birçok alanda kullanılmaktadır.
- Multidimensional array ve matrix data structure'ları içerir.
- n-dimensional array object olan `ndarray` ve methodlar barındırır. `ndarray`'ler hem vector'leri (1D array) hem matrix'leri (2D array) hem de tensor'leri (+3D array) temsil etmek için kullanılır.
- Üzerinde verimli çalışabilmek için metotlara sahip olan n-dimensional homojen bir ndarray array object sunar.
- Array ve matrice'lerle verimli hesaplamaları garanti eden güçlü data structure'lar ve array ve matrice'ler üzerinde çeşitli high-level matematiksel işlemler yapabilmenizi sağlayan fonksiyonlar ekler.
- [**vectorization**](https://stackoverflow.com/a/1422181/15170972 "https://stackoverflow.com/a/1422181/15170972")'ı desteklediği için normal python data structure'lardan çok daha hızlı çalışır.
- Python listelerinden farklı olarak homojen bir yapıya sahip olduğu için daha hızlıdır, compact'tır, daha az bellek tüketir, daha optimize ve verimlidir. Örnek:
    ```py
    import numpy as np
    import time

    start_time_1 = time.time()
    A = np.arange(1000000)
    A**2
    time_1 = time.time() - start_time_1

    start_time_2 = time.time()
    B = range(1000000)
    [i**2 for i in B]
    time_2 = time.time() - start_time_2

    print(f"time_1: {time_1}",
        f"time_2: {time_2}",
        f"Bu işlemde arange, range'den {time_2/time_1} kat daha hızlı çalıştı.", sep="\n")
    ```
    **Output:**
    ```
    time_1: 0.0020034313201904297
    time_2: 0.2800407409667969
    Bu işlemde arange, range'den 139.78055456384624 kat daha hızlı çalıştı.
    ```

<h2 id="1.2">Numpy Installing ve Importing</h2>

`pip` kullanıyorsanız CMD'ye `pip install numpy` yazarak Numpy yükleyebilirsiniz.

Python programınızıda Numpy'ı kullanmak için önce import etmelisiniz:
```py
import numpy as np
```
Sürekli numpy yazmak yerine np kullanmak daha pratik olduğu için böyle tercih etmeniz sizin yararınıza olur.

<h2 id="1.3">Array Nedir</h2>

Array, değerler koleksiyonudur (grid of value). Raw data, elementlerin konumu (locate) ve elementlerin nasıl yorumlanacağı (interpret) hakkında bilgiler içeririr. Çeşitli şekillerde indexlenebilir element koleksiyonunda (grid) sahiptir. Elementlerin tümü aynı türdedir (type) ve bu tür `dtype` array olarak adlandırılır. Bir array negatif olmayan integer'lardan oluşan tuble'lar, boolean değerler, diğer arrayler ve integer'lar tarafından indexlenebilir.

Bir array'in **rank**'ı, o dizinin dimension sayısını ifade eden bir integer'dır. İki ya da daha fazla dimension'ı bulunan NumPy array'ler initialize (başlatmak) edebilmek için (kısaca oluşturabilmek için) nested listeler kullanılır. Örnek:
```py
import numpy as np
print(np.array([[1,2,3],[4,5,6],[7,8,9]]))
```
**Output:**
```
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```
Array'leri indexlemek normal python'daki sequence'ları indexlemek gibidir. Örnek:
```py
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a,end="\n\n")
print(a[0],end="\n\n")
print(a[0][0],end="\n\n")
```
**Output:**
```
[[1 2 3]
 [4 5 6]
 [7 8 9]]

[1 2 3]

1
```
NumPy'da dimension'lar **axis** olarak isimlendirilir (birden fazla dimension'dan bahsediyorsak **axes**). 2D array'lerle uğraşırken column ve row kavramlarıyla karşılaşmışsınızdır. Column ve row kavramları sadece 2D array'lerde geçerli olduğu için genel olarak axis (eksen) terimi kullanılır. Çok dimention'lu array'lerde axis'ler soldan sağa doğru dıştan içe olarak sıralanır. Örnek:
```
[[[1 2 3]
  [4 5 6]
  [7 8 9]]

  [[1 2 3]
  [4 5 6]
  [7 8 9]]]

a[first axis, second axis, third axis, ...]
```
```py
import numpy as np
a = np.zeros((2,3,4))
print("1:",a,end="\n\n",sep="\n")
a[:,0,0] = 1
print("2:",a,end="\n\n",sep="\n")
a = np.zeros((2,3,4))
a[0,:,0] = 2
print("3:",a,end="\n\n",sep="\n")
a = np.zeros((2,3,4))
a[0,0,:] = 3
print("4:",a,end="\n\n",sep="\n")
```
**Output:**
```
1:
[[[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]

 [[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]]

2:
[[[1. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]

 [[1. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]]

3:
[[[2. 0. 0. 0.]
  [2. 0. 0. 0.]
  [2. 0. 0. 0.]]

 [[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]]

4:
[[[3. 3. 3. 3.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]

 [[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]]
```

> **Örneği eksik:** Just like in other Python container objects, the contents of an array can be accessed and modified by indexing or slicing the array. Unlike the typical container objects, different arrays can share the same data, so changes made on one array might be visible in another.

[Array attributes](https://numpy.org/doc/stable/reference/arrays.ndarray.html#arrays-ndarray) ve [array object](https://numpy.org/doc/stable/reference/arrays.html#arrays) hakkında daha fazla bilgi tıklayınız.

<h2 id="1.4">Array Oluşturmak</h2>

<h3 id="1.4.1"><code>array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)</code></h3>

`object` parametresine argüman olarak girilen sequence'ı `ndarray`'e dönüştürür. Argüman olarak array, any object exposing the array interface, an object whose `__array__` method returns an array ve nested sequence verilebilir. Argüman olarak scalar bir object verilirse 0 dimension'lı bir array döndürür (kısaca tek integer). Örnek:
```py
import numpy as np
a = np.array(1)
print(a) # Output: 1
```
Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).