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
`dtype` parametresine argüman olarak C-like veri türleri girilebilir. Böylece array'in öğeleri belirttiğiniz veri türünde olacaktır. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).

<h3 id="1.4.2"><code>zeros(shape, dtype=float, order='C', *, like=None)</code></h3>

`shape` parametresine verilen integer ya da pozitif integer'lardan oluşan bir tuple argümanda bahsedilen şekilde, sıfırlarla dolu bir array döndürür. Örnek:
```py
import numpy as np
a = np.zeros(4)
b = np.zeros((2,3))
c = np.zeros((2,3,4))
print(a,b,c,sep="\n----------------\n")
```
**Output:**
```
[0. 0. 0. 0.]
----------------
[[0. 0. 0.]
 [0. 0. 0.]]
----------------
[[[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]

 [[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]]
```
`dtype` parametresine argüman olarak C-like veri türleri girilebilir. Böylece array'in öğeleri belirttiğiniz veri türünde olacaktır. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.zeros.html).

<h3 id="1.4.3"><code>ones(shape, dtype=None, order='C', *, like=None)</code></h3>

`shape` parametresine verilen integer ya da pozitif integer'lardan oluşan bir sequence argümanda bahsedilen şekilde, sıfırlarla dolu bir array döndürür. Örnek:
```py
import numpy as np
a = np.ones(4)
b = np.ones((2,3))
c = np.ones((2,3,4))
print(a,b,c,sep="\n----------------\n")
```
**Output:**
```
[1. 1. 1. 1.]
----------------
[[1. 1. 1.]
 [1. 1. 1.]]
----------------
[[[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]

 [[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]]
```
`dtype` parametresine argüman olarak C-like veri türleri girilebilir. Böylece array'in öğeleri belirttiğiniz veri türünde olacaktır. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.ones.html).

<h3 id="1.4.4"><code>empty(shape, dtype=float, order='C', *, like=None)</code></h3>

`shape` parametresine verilen integer ya da pozitif integer'lardan oluşan bir tuple argümanda bahsedilen şekilde, belleğin durumuna göre seçilen rastgele sayıların atandığı bir array döndürür. Örnek:
```py
import numpy as np
a = np.empty(4)
b = np.empty((2,3))
c = np.empty((2,3,4))
print(a,b,c,sep=f"\n{'-'*67}\n")
```
**Output:**
```
[8.90070286e-308 8.90070286e-308 1.33508506e-307 0.00000000e+000]
-------------------------------------------------------------------
[[ 0.0000000e+000 -5.1390467e-311  0.0000000e+000]
 [ 0.0000000e+000  0.0000000e+000  0.0000000e+000]]
-------------------------------------------------------------------
[[[6.23042070e-307 4.67296746e-307 1.69121096e-306 1.86922637e-306]
  [1.89146896e-307 7.56571288e-307 3.11525958e-307 1.24610723e-306]
  [1.37962320e-306 1.29060871e-306 2.22518251e-306 1.33511969e-306]]

 [[1.78022342e-306 1.05700345e-307 1.11261027e-306 1.11261502e-306]
  [1.42410839e-306 7.56597770e-307 6.23059726e-307 1.42419530e-306]
  [7.56599128e-307 1.78022206e-306 8.34451503e-308 8.34402698e-308]]]
```
`dtype` parametresine argüman olarak C-like veri türleri girilebilir. Böylece array'in öğeleri belirttiğiniz veri türünde olacaktır. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.empty.html).

<h3 id="1.4.5"><code>arange([start, ]stop, [step, ]dtype=None, *, like=None)</code></h3>

`start` parametresine argüman olarak başlama değeri, `stop` parametresine argüman olarak biriş değeri, `step` parametresine argüman olarak adım değeri integer type olarak verilir. Verilen değerlere uygun bir boyutlu bir array döndürür. `start` dahil edilir, `stop` dahil edilmez. Örnek:
```py
import numpy as np
a = np.arange(10)
b = np.arange(4,10)
c = np.arange(4,10,2)
print(a,b,c,sep=f"\n{'-'*21}\n")
```
**Output:**
```
[0 1 2 3 4 5 6 7 8 9]
---------------------
[4 5 6 7 8 9]
---------------------
[4 6 8]
```
`dtype` parametresine argüman olarak C-like veri türleri girilebilir. Böylece array'in öğeleri belirttiğiniz veri türünde olacaktır. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.arange.html).

<h3 id="1.4.6"><code>linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)</code></h3>

`start` parametresine argüman olarak başlama değeri, `stop` parametresine argüman olarak biriş değeri, `num` parametresine argüman olarak üretilecek öğe sayısı integer type olarak verilir. Verilen değerlere uygun eşit aralıklı öğelerden oluşan bir boyutlu bir array döndürür. `start` dahil edilir, `stop` dahil edilmez. Örnek:
```py
import numpy as np
a = np.linspace(0,10,num=2)
b = np.linspace(0,10,num=3)
c = np.linspace(0,10,num=5)
print(a,b,c,sep=f"\n{'-'*26}\n")
```
**Output:**
```
[ 0. 10.]
--------------------------
[ 0.  5. 10.]
--------------------------
[ 0.   2.5  5.   7.5 10. ]
```
`dtype` parametresine argüman olarak C-like veri türleri girilebilir. Böylece array'in öğeleri belirttiğiniz veri türünde olacaktır. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.linspace.html).

<h3 id="1.4.6">RNG Modülü</h3>

RNG modülündeki `random`, `integers` gibi methodları kullanarak istediğiniz boyutta random array'ler oluşturabilirsiniz.

<h2 id="1.5">Adding, Removing, Sorting Elements</h2>

<h3 id="1.5.1"><code>sort(a, axis= -1, kind=None, order=None)</code></h3>

Array üzerinde sorting (sıralama) işlemi yapar. Asıl array objesini değiştirmez, sorting işlemi yapılmış halini döndürür. Örnek:
```py
import numpy as np
a = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(a) # Output: [2 1 5 3 7 4 6 8]
print(np.sort(a)) # Output: [1 2 3 4 5 6 7 8]
```
Daha fazla bilgi için [tıklayın](https://numpy.org/doc/stable/reference/generated/numpy.sort.html?highlight=sort#numpy.sort).

<h3 id="1.5.2"><code>concatenate((a1, a2, ...), axis=0, out=None, dtype=None, casting="same_kind")</code></h3>

Argüman olarak verilen bir tuple içindeki array'leri ya da array_like sequence'ları birleştirir. Birleştirme işlemini gerçekleştirebilrmek için argüman olarak verilen array'lerin ya da array_like sequence'ların boyutları aynı olmalı. Örnek:
```py
import numpy as np
a = np.array([2, 1, 5, 3])
b = np.array([7, 4, 6, 8])
c = [2, 1, 5, 3]
d = [7, 4, 6, 8]
print(np.concatenate((a,b))) # Output: [2 1 5 3 7 4 6 8]
print(np.concatenate((c,d))) # Output: [2 1 5 3 7 4 6 8]
```
Daha fazla bilgi için [tıklayın](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html?highlight=concatenate#numpy.concatenate).

<h2 id="1.6">Shape ve Size</h2>

<h3 id="1.6.1"><code>ndim(a)</code></h3>

Argüman olarak girilen array'in boyut (dimension) bilgisini döndürür. Örnek:
```py
import numpy as np
a = np.array([[4,2,3,1],[8,5,7,6]])
b = np.array([11,9,12,10])
print(np.ndim(a)) # Output: 2
print(np.ndim(b)) # Output: 1
```

<h3 id="1.6.2"><code>size(a, axis=None)</code></h3>

Argüman olarak girilen array'in toplam element sayısının (size) bilgisini döndürür. Örnek:
```py
import numpy as np
a = np.array([[4,2,3,1],[8,5,7,6]])
b = np.array([11,9,12,10])
print(np.size(a)) # Output: 8
print(np.size(b)) # Output: 4
```

<h3 id="1.6.3"><code>shape(a)</code></h3>

Argüman olarak girilen array'in her boyutundaki element sayısını bilgisini (shape) bir tuple içinde döndürür. Örnek:
```py
import numpy as np
a = np.array([0,0,0,0])
b = np.array([[0,0,0,0],[0,0,0,0]])
c = np.array([[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]]])
print(np.shape(a)) # Output: (4,)
print(np.shape(b)) # Output: (2, 4)
print(np.shape(c)) # Output: (2, 2, 4)
```

<h2 id="1.7">Reshape Array</h2>

<h3 id="1.7.1"><code>reshape(a, newshape, order='C')</code></h3>

Argüman olarak girilen array üzerinde `newshape` parametresinde belirttiğiniz shape'e göre reshape işlemi yapar. Reshape işleminin gerçekleşebilmesi için ilgili array ve reshape'e göre oluşturulacak yeni array'ın size'i (yani toplam element sayısı) aynı olmalı. Örnek:
```py
import numpy as np
a = np.array([[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]]])
print("1.\n",np.reshape(a,(2,8)))
print("2.\n",np.reshape(a,(2,2,2,2)))
```
**Output:**
```
1.
 [[0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]]
2.
 [[[[0 0]
   [0 0]]

  [[0 0]
   [0 0]]]


 [[[0 0]
   [0 0]]

  [[0 0]
   [0 0]]]]
```

<h2 id="1.8">Array'e Yeni Boyut Eklemek</h2>

<h3 id="1.8.1"><code>newaxis</code></h3>

Bir array'e boyut eklemek için kullanılır. Örnek:
```py
import numpy as np
a = np.array([0,0,0,0])
print(a)
a1_1 = a[np.newaxis,:]
a1_2 = a[:,np.newaxis]
print(a1_1,a1_2,sep="\n")
print(np.shape(a1_1),np.shape(a1_2))
```
**Output:**
```
[0 0 0 0]
[[0 0 0 0]]
[[0]
 [0]
 [0]
 [0]]
(1, 4) (4, 1)
```

<h3 id="1.8.2"><code>expand_dims(a, axis)</code></h3>

`a` parametresine argüman olarak girilen array'in `axis` parametresinde belirtilen axis'ine yeni boyut ekler. Örnek:
```py
import numpy as np
a = np.array([0,0,0,0])
print(a)
print(np.expand_dims(a,axis=0))
print(np.expand_dims(a,axis=1))
print(np.shape(np.expand_dims(a,axis=0)),np.shape(np.expand_dims(a,axis=1)))
```
**Output:**
```
[0 0 0 0]
[[0 0 0 0]]
[[0]
 [0]
 [0]
 [0]]
(1, 4) (4, 1)
```

<h2 id="1.9">Indexing ve Slicing</h2>

Indexing bildiğimiz python'daki gibi.

![](https://numpy.org/doc/stable/_images/np_indexing.png)

Belli koşulları sağlayan değerleri istiyorsanız:
```py
import numpy as np

# 7'den küçük değerleri yazdırmak
print(a[a<7]) # Output: [1 2 3 4 5 6]
print(a[(a > 2) & (a < 11)]) # Output: [ 3  4  5  6  7  8  9 10]
koşul1 = (a<7)
koşul2 = (a > 5) | (a == 5)
print(a[koşul1]) # Output: [1 2 3 4 5 6]
print(a[koşul2]) # Output: [ 5  6  7  8  9 10 11 12]
```
Buradaki `koşul` numpy'a özel bir şeydir. Normal python'da böyle bir şey denemeye kalkarsanız olası seneryolarda `TypeError: '<' not supported between instances of 'list' and 'int'` gibi çeşitli hatalarla karşılaşabilirsiniz.

<h3 id="1.9.1"><code>nonzero(a)</code></h3>

Bir array'in her axis'i için sıfır olmayan elementlerin konumlarını içeren array'leri bir tuple içinde döndürür. Bu tuple objesini kullanarak ilgili array'in sıfır olmayan elemanlarına ulaşabilirsiniz. Örnek:
```py
import numpy as np
a = np.array([[0, 8, 0], [7, 0, 0], [-5, 0, 1]])
print(np.nonzero(a)) # Output: (array([0, 1, 2, 2], dtype=int64), array([1, 0, 0, 2], dtype=int64))
print(a[np.nonzero(a)]) # Output: [ 8  7 -5  1]
```
Bu methodu belli bir koşula uyacak şekilde de kullanabilirsiniz. Örnek:
```py
import numpy as np
a = np.array([[0, 8, 0], [7, 0, 0], [-5, 0, 1]])
print(np.nonzero(a>5)) # Output: (array([0, 1], dtype=int64), array([1, 0], dtype=int64))
print(a[np.nonzero(a>5)]) # Output: [8  7]
```

<h2 id="1.10">How to create an array from existing data</h2>

<h3 id="1.10.1"><code>vstack(tup)</code></h3>

İki array'i diket (vertical) olarak birleştirmek için kullanılır. `tup` parametresine argüman olarak bu iki array'i içeren bir tuple objesi verilmelidir. Örnek:
```py
import numpy as np
a = np.array([[1,1],[2,2]])
b = np.array([[3,3],[4,4]])
print(np.vstack((a,b)))
```
**Output:**
```
[[1 1]
 [2 2]
 [3 3]
 [4 4]]
```

<h3 id="1.10.2"><code>hstack(tup)</code></h3>

İki array'i yatay (horizontal) olarak birleştirmek için kullanılır. `tup` parametresine argüman olarak bu iki array'i içeren bir tuple objesi verilmelidir. Örnek:
```py
import numpy as np
a = np.array([[1,1],[2,2]])
b = np.array([[3,3],[4,4]])
print(np.hstack((a,b)))
```
**Output:**
```
[[1 1 3 3]
 [2 2 4 4]]
```

<h3 id="1.10.3"><code>copy()</code></h3>

Bir array'in kopyasını oluşturmaya yarar. Oluşturulan kopya ana array'den bağımsızdır. Örnek:
```py
import numpy as np
a = np.array(range(10))
b = a.copy()
print(a) # Output: [0 1 2 3 4 5 6 7 8 9]
print(b) # Output: [0 1 2 3 4 5 6 7 8 9]
a[0]=99
print(a) # Output: [99 1 2 3 4 5 6 7 8 9]
print(b) # Output: [0 1 2 3 4 5 6 7 8 9]
```
**Output:**
```
[[1 1 3 3]
 [2 2 4 4]]
```

<h2 id="1.11">Basic Array Operations</h2>

<h3 id="1.11.1">Operations</h3>

Array'ler arasında Çeşitli matematiksel işlemler yapabilirsiniz. Örnek:
```py
import numpy as np
a = np.array([1,2])
b = np.ones(2,dtype=int)
print(a) # Output: [1 2]
print(b) # Output: [1 1]
print(a+b) # Output: [2 3]
```
```py
import numpy as np
a = np.array([1,2])
b = np.ones(2,dtype=int)
print(a) # Output: [1 2]
print(b) # Output: [1 1]
print(a+b) # Output: [2 3]
```
**Output:**
```
[[1 2]
 [3 4]]
[1 1]
[[2 3]
 [4 5]]
```

<h3 id="1.11.2">Broadcasting</h3>

Bir vector ve bir scalar veya uyumlu boyutlardaki array'ler arasında yapılan işlemlere **broadcasting** denir. NumPy bu işlemlerin/işlemin her hücrede olması gerektiğini anlar.
```py
import numpy as np
a = np.array([[[1,1,1],[2,2,2]],[[3,3,3],[4,4,4]]])
b = np.array(range(1,13)).reshape((2,2,3))
print(a+b,end="\n-------------------n")
print(b+2.5)
```
**Output:**
```
[[[ 2  3  4]
  [ 6  7  8]]

 [[10 11 12]
  [14 15 16]]]
-------------------
[[[ 3.5  4.5  5.5]
  [ 6.5  7.5  8.5]]

 [[ 9.5 10.5 11.5]
  [12.5 13.5 14.5]]]
```

<h3 id="1.11.3"><code>sum(a, axis=None, dtype=None, ...)</code></h3>

Uygulandığı array'in elementlerinin toplamını döndürür. Örnek:

```py
import numpy as np
a = np.array([[1,2],[3,4]])
print(a.sum()) # Output: 10
```
`axis` parametresinde belirttiğiniz axis'e göre farklı axisler arasında toplama işlemi yapar. Örnek:
```py
import numpy as np
a = np.array([[[1,1,1],[2,2,2]],[[3,3,3],[4,4,4]]])
print(a,end="\n-----------\n")
print(a.sum(axis=0),end="\n-----------\n")
print(a.sum(axis=1),end="\n-----------\n")
print(a.sum(axis=2))
```
**Output:**
```
[[[1 1 1]
  [2 2 2]]

 [[3 3 3]
  [4 4 4]]]
-----------
[[4 4 4]
 [6 6 6]]
-----------
[[3 3 3]
 [7 7 7]]
-----------
[[ 3  6]
 [ 9 12]]
```

<h3 id="1.11.4"><code>min(axis=None)</code></h3>

Uygulandığı array'in elementleri arasından en küçüğünü döndürür. `axis` parametresinde belirtilen axis'lere göre minimum değeri bulur ve döndürür. Örnek:
```py
import numpy as np
b = np.array(range(1,13)).reshape((2,2,3))
print(b,end="\n----------------\n")

print(b.min(),end="\n----------------\n")
print(b.min(axis=0),end="\n----------------\n")
print(b.min(axis=1),end="\n----------------\n")
print(b.min(axis=2))
```
**Output:**
```
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
----------------
1
----------------
[[1 2 3]
 [4 5 6]]
----------------
[[1 2 3]
 [7 8 9]]
----------------
[[ 1  4]
 [ 7 10]]
```

<h3 id="1.11.4"><code>max(axis=None)</code></h3>

Uygulandığı array'in elementleri arasından en büyüğünü döndürür. `axis` parametresinde belirtilen axis'lere göre maxsimum değeri bulur ve döndürür. Örnek:
```py
import numpy as np
b = np.array(range(1,13)).reshape((2,2,3))
print(b,end="\n----------------\n")

print(b.max(),end="\n----------------\n")
print(b.max(axis=0),end="\n----------------\n")
print(b.max(axis=1),end="\n----------------\n")
print(b.max(axis=2))
```
**Output:**
```
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
----------------
12
----------------
[[ 7  8  9]
 [10 11 12]]
----------------
[[ 4  5  6]
 [10 11 12]]
----------------
[[ 3  6]
 [ 9 12]]
```

<h3 id="1.11.5"><code>std()</code></h3>

Uygulandığı array'in strandart sapmasını döndürür. Örnek:
```py
import numpy as np
b = np.array([0,10,20,30,40])
print(b.std()) # Output: 14.142135623730951
b = np.array([0,0,0,0,0])
print(b.std()) # Output: 0
```

<h2 id="1.12">How to get unique items and counts</h2>

<h3 id="1.12.1"><code>unique(ar)</code></h3>

`ar` parametresine argüman olarak girilen array'in elementlerini kullanarak benzersiz elementlerden oluşan bir array objesi döndürür. Benzersiz elementler demek, tekrar eden elementlerden sadece bir tane kullanılması anlamına gelir. Örnek:
```py
import numpy as np
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
print(a) # Output: [11 11 12 13 14 15 16 17 12 13 11 14 18 19 20]
print(np.unique(a)) # Output: [11 12 13 14 15 16 17 18 19 20]
```
Unique element'lerin tekrar etme sayısını istiyorsanız `return_count` parametresine `True` argümanını verin. Örnek:
```py
import numpy as np
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
print(a) # Output: [11 11 12 13 14 15 16 17 12 13 11 14 18 19 20]
print(np.unique(a)) # Output: [11 12 13 14 15 16 17 18 19 20]
print(np.unique(a, return_counts=True)) # Output: (array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), array([3, 2, 2, 2, 1, 1, 1, 1, 1, 1], dtype=int64))    
print(np.unique(a, return_counts=True)[1]) # Output: [3 2 2 2 1 1 1 1 1 1]
```
Unique element'lerin bulundukları indexleri istiyorsanız `return_index` parametresine `True` argümanını verin. Örnek:
```py
import numpy as np
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
print(a)
print(np.unique(a))
print(np.unique(a, return_index=True))
print(np.unique(a, return_index=True)[1])
print(np.unique(a, return_index=True, axis=1)[1])
```
**Output:**
```
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [ 1  2  3  4]]
[ 1  2  3  4  5  6  7  8  9 10 11 12]
(array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]), array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11], dtype=int64))
[ 0  1  2  3  4  5  6  7  8  9 10 11]
[0 1 2]
```
Başka bir örnek:
```py
import numpy as np
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
print(a,end="\n-------------------\n")
unique_rows, indices, occurrence_count = np.unique(a, axis=0, return_counts=True, return_index=True)
print(unique_rows,indices,occurrence_count,sep="\n-------------------\n")
```
**Output:**
```
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [ 1  2  3  4]]
-------------------
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
-------------------
[0 1 2]
-------------------
[2 1 1]
```

<h2 id="1.13">Transposing ve Reshaping</h2>

**Transposing:**

![](../Numpy/g%C3%B6rseller/1.PNG)

```py
import numpy as np
a = np.array([[1,2],[3,4],[5,6],[7,8]])
print(a,end="\n---------------\n")
print(np.transpose(a))
```
**Output:**
```
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
---------------
[[1 3 5 7]
 [2 4 6 8]]
```

**Reshaping:**

![](../Numpy/g%C3%B6rseller/2.PNG)

```py
import numpy as np
a = np.array([[1,2],[3,4],[5,6],[7,8]])
print(a,end="\n---------------\n")
print(np.reshape(a,newshape=(2,4)),end="\n---------------\n")
print(np.reshape(a,newshape=(8,)))
```
**Output:**
```
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
---------------
[[1 2 3 4]
 [5 6 7 8]]
---------------
[1 2 3 4 5 6 7 8]
```

<h2 id="1.13">How to reverse an array</h2>

<h3 id="1.13.1"><code>flip(m,axis)</code></h3>

`m` parametresine argüman olarak girilen array üzerinde reverse işlemi uygular. Örnek:
```py
import numpy as np
a = np.array(range(1,11))
print(a) # Output: [ 1  2  3  4  5  6  7  8  9 10]
print(np.flip(a)) # Output: [10  9  8  7  6  5  4  3  2  1]
```
`axis` parametresinde belirtilen axis düzeyinde reverse işlemi yapmasını istiyorsanız:
```py
import numpy as np
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a,end="\n-----------------\n")
print(np.flip(a),end="\n-----------------\n")
print(np.flip(a,axis=0),end="\n-----------------\n")
print(np.flip(a,axis=1))
```
**Output:**
```
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
-----------------
[[12 11 10  9]
 [ 8  7  6  5]
 [ 4  3  2  1]]
-----------------
[[ 9 10 11 12]
 [ 5  6  7  8]
 [ 1  2  3  4]]
-----------------
[[ 4  3  2  1]
 [ 8  7  6  5]
 [12 11 10  9]]
```

<h2 id="1.14">Flattening Multidimensional Arrays</h2>

<h3 id="1.14.1"><code>flatten</code></h3>

Uygulandığı array'i düzlediği farklı bir array objesi döndürür. Örnek:

```py
import numpy as np
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a1 = a.flatten()
print(a,end="\n-------------\n")
a1[0] = 99
print(a1,end="\n-------------\n")
print(a,end="\n-------------\n")
```
**Output:**
```
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
-------------
[99  2  3  4  5  6  7  8  9 10 11 12]
-------------
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
-------------
```

<h3 id="1.14.2"><code>ravel</code></h3>

Uygulandığı array'i düzlediği farklı bir array objesi döndürür ama bu düzlenmiş array objesinin elementleri referans alınan array objesinin elementleriyle bağlantılıdır. Örnek:

```py
import numpy as np
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a1 = a.ravel()
print(a1,end="\n-------------\n")
a1[0] = 99
print(a,end="\n-------------\n")
print(a1,end="\n-------------\n")
```
**Output:**
```
[ 1  2  3  4  5  6  7  8  9 10 11 12]
-------------
[[99  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
-------------
[99  2  3  4  5  6  7  8  9 10 11 12]
-------------
```