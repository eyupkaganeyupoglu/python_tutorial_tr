# İçindekiler

- [`ndarray` Object](#1)

<h1 id="1"><code>ndarray</code> Object</h1>

NumPy'da tanımlanan en önemli obje, `ndarray` adı verilen N boyutlu bir array türüdür. `ndarray`, aynı type itemlerin toplandığı bir koleksiyonudur (grid of value, collection). Bu itemlara erişmek için zero-based index'leme kullanılır (yani ilk item'in index'i `0` olarak ifade edilir). Bir `ndarray`'deki her bir item bellekte aynı boyutta yer kaplar ve `data-type` objesinin bir objesidir (`data-type` = `dtype`).

Bir ndarray'i slicing yoluyla (daha sonra anlatılacak) parçalarsan bir array scalar elde edersin.

![](./pics/1.jpg)

Görseldeki ndarray diyagramı, dtype ve array scalar arasındaki ilişkiyi gösteriyor. Örnek:
```py
import numpy as np

a = np.array([1,2,3,4,5])
b = a[0:2]
c = a[4]
print(type(b), b.dtype, b) # Output: <class 'numpy.ndarray'> int32 [1 2]
print(type(c), c.dtype, c) # Output: <class 'numpy.int32'> int32 5
```
Yani yukarıda anlattığım bütün olay, `c`'nin `'numpy.int32'` type bir obje olması için yaptığımız şeyin açıklaması.

**Not:** The ndarray object consists of contiguous one-dimensional segment of computer memory, combined with an indexing scheme that maps each item to a location in the memory block. The memory block holds the elements in a row-major order (C style) or a column-major order (FORTRAN or MatLab style).

<h2 id="1.1">Array'lerde Boyut (Dimension) ve Indexing</h2>

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
**Not:** Farklı array'ler aynı verileri içeriyor olabilir. Bu durumda array'lerin birinde yaptığınız değişiklikler diğer array'i de etkiler.

[Array attributes](https://numpy.org/doc/stable/reference/arrays.ndarray.html#arrays-ndarray) ve [array object](https://numpy.org/doc/stable/reference/arrays.html#arrays) hakkında daha fazla bilgi tıklayınız.

<h2 id="1.2">NumPy'ın Desteklediği Veri Türleri (<code>dtype</code>)</h2>

Bir `dtype`,
- Data'nın type'ına (integer, float ya da Python object),
- Data'nın size'ına,
- Byte order (little-endian or big-endian),
- Structured type olması durumunda, field'lerin adları (name), her field'ın data type'ı ve her filed tarafından alınan memory block parçasına ()part of memory block),
- Data dype bir subarray ise, shape ve data type'ına

bağlı olarak bir array'e karşılık gelen sabit bellek bloğunun (fixed block of memory) yorumlanmasını (interpretation) açıklar.

**Not:** Byte order'a data type'a prefix olarak `<` ya da `>` eklenerek karar verilir. `<` encoding'in little-endian olduğu anlamına gelir (en önemsizi (least significant) en küçük adreste saklanır). `>` encoding'in big-endian olduğu anlamına gelir (en önemli (most significant) byte en küçük adreste saklanır).

|     Type     | Description                                                                                                         |
| :----------: | :------------------------------------------------------------------------------------------------------------------ |
|   `bool_`    | Byte olarak depolanan boolean (`True` ya da `False`)                                                                |
|    `int_`    | Default integer type (C'deki `long` ile neredeyse aynı (same as), normalde ya `int32` ya da `int64`)                |
|    `intc`    | C'deki `int` ile birebir aynı (identical)(normalde ya `int32` ya da `int64`)                                        |
|    `intp`    | Indexing için kullanılan integer (C'deki `ssize_t` ile neredeyse aynı (same as), normalde ya `int32` ya da `int64`) |
|    `int8`    | Byte (-128 to 127)                                                                                                  |
|   `int16`    | Integer (-32768 to 32767)                                                                                           |
|   `int32`    | Integer (-2147483648 to 2147483647)                                                                                 |
|   `int64`    | Integer (-9223372036854775808 to 9223372036854775807)                                                               |
|   `uint8`    | Unsigned integer (0 to 255)                                                                                         |
|   `uint16`   | Unsigned integer (0 to 65535)                                                                                       |
|   `uint32`   | Unsigned integer (0 to 4294967295)                                                                                  |
|   `uint64`   | Unsigned integer (0 to 18446744073709551615)                                                                        |
|   `float_`   | `float64` için kısaltma (shorthand)                                                                                 |
|  `float16`   | Half precision float: sign bit, 5 bits exponent, 10 bits mantissa                                                   |
|  `float32`   | Single precision float: sign bit, 8 bits exponent, 23 bits mantissa                                                 |
|  `float64`   | Double precision float: sign bit, 11 bits exponent, 52 bits mantissa                                                |
|  `complex_`  | `complex128` için kısaltma (shorthand)                                                                              |
| `complex64`  | İki 32-bit ile temsil edilen complex sayı (real and imaginary components)                                           |
| `complex128` | İki 64-bit ile temsil edilen complex sayı (real and imaginary components)                                           |

Bir `dtype` objesi oluşturmak için `dtype(object, align, copy)` methodu kullanılır.
- **`object`**: Argüman olarak bir data type objesine dönüştürülecek objeyi kabul eder.
- **`align:bool` (optional)**: Bilgi için [tıklayın](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html?highlight=numpy%20dtype#numpy.dtype).
- **`copy:bool` (optional)**: Bilgi için [tıklayın](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html?highlight=numpy%20dtype#numpy.dtype).

`dtype` ile ilgili daha fazla bilgi ve kullanımıyla ilgili örnekler için [tıklayınız](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html?highlight=numpy%20dtype#numpy.dtype).

<h2 id="1.3">Array Attribute'ları</h2>

<h3 id="1.3.1"><code>shape(a)</code> Attribute'u</h3>

`a` parametresine argüman olarak girilen array'in dimension ve her dimension'ındaki item sayısı bilgisini içeren bir tuple döndürür. Örnek:
```py
import numpy as np

a = np.ones((4))
b = np.ones((4, 3))
c = np.ones((4, 3, 2))

print(a, np.shape(a), end="\n\n")
print(b, np.shape(b), end="\n\n")
print(c, np.shape(c))
```
**Output:**
```
[1. 1. 1. 1.] (4,)

[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]] (4, 3)

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

print(a, np.shape(a), end="\n\n")
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

[[1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1.]] (4, 6) (4, 6)
```
Gördüğünüz gibi `np.shape(a)` ile `a.shape` arasında bir fark yoktur. İkisi de aynı bilgiyi verir.

**Not:** Bu işlemin yapılabilmesi için ilgili array'in eski ve yeni shape'i aynı sayıda item'a sahip olmalıdır aksi halde `ValueError: cannot reshape array of size 24 into shape (4,5)` örneğindeki gibi bir hata döndürür.

<h3 id="1.3.2"><code>reshape(a, newshape, order='C')</code> Attribute'u</h3>

`a` parametresine argüman olarak girilen array'i `newshape` parametresine girilen tuple'da belirtilene göre yeniden boyutlandırdığı bir array öbjesi döndürür (yani `a` parametresine argüman olarak girilen array'i etkilemez). Örnek:
```py
import numpy as np

a = np.ones((4, 3, 2))

print(a, np.shape(a), end="\n\n")
b = a.reshape((4, 6))
print(a, np.shape(a), end="\n\n")
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

[[1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1.]] (4, 6)
```

<h3 id="1.3.3"><code>ndim(a)</code> Attribute'u</h3>

`a` parametresine argüman olarak girilen array'in dimension sayısını döndürür. Örnek:
```py
import numpy as np

a = np.ones((4, 3, 2))

print(np.ndim(a)) # Output: 3
a.shape = (4, 6)
print(np.ndim(a),a.ndim) # Output: 2 2
```
gördüğünüz gibi np.ndim(a) ile a.ndim arasında bir fark yoktur. İkisi de aynı bilgiyi verir.

<h3 id="1.3.4"><code>itemsize</code> Attribute'u</h3>

Bir array'in her item'ının bellekte kapladığı alanı byte cinsinden döndürür. Örnek:
```py
import numpy as np

a1 = np.ones((5,), dtype=np.int8)
a2 = np.ones((5,), dtype=np.int32)
a3 = np.ones((5,), dtype=np.float16)

print(a1.itemsize) # Output: 1
print(a2.itemsize) # Output: 4
print(a3.itemsize) # Output: 2
```

<h3 id="1.3.1"><code>shape(a)</code> Attribute'u</h3>

<h3 id="1.3.1"><code>shape(a)</code> Attribute'u</h3>

<h3 id="1.3.1"><code>shape(a)</code> Attribute'u</h3>

<h2 id="1.?">Array Oluşturmak</h2>

<h3 id="1.?.1"><code>array</code> Methodu</h3>

Bir array oluşturmak için en temel yöntem `array` methodunu kullanmaktır. Örnek:
```py
import numpy as np
print(type(np.array([1,2,3]))) # Output: <class 'numpy.ndarray'>
```

`array` methodu `numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)` parametrelerine sahiptir.
- **`object:array_like`**: Bu parametreye argüman olarak sequence, nested sequence, scalar bir değer (integer, float vs.), array döndüren `__array__` methoduna sahip bir şey... kısaca array interface ortaya çıkarabilecek (exposing) herhangi bir obje verilebilir.
- **`dtype:data-type` (optional)**: Bu parametreye argüman olarak C-like veri türleri girilebilir. Böylece array'in öğeleri belirttiğiniz veri türünde olacaktır. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).
- **`copy:bool` (optional)**: Parametre olarak boolean değerleri kabul eder. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).
- **`order:{'K','A','C','F'}` (optional)**: Bu parametre argüman olarak K, A, C, F harflarinden birini kabul eder. Array'in memory layout'unu belirtmek için kullanılır. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).
- **`subok:bool` (optional)**: Parametre olarak boolean değerleri kabul eder. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).
- **`ndmin:int` (optional)**: İlgili array'in sahip olması gereken minimum dimension sayısını belirtebildiğiniz parametredir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).
- **`like:array_like` (optional)**: NumPy array objesi olmayan array'ler oluşturmanız gerektiğinde `array` methodunun referans alacağı objesini belirttiğiniz parametredir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).

<h3 id="1.?.2"><code>zeros</code> Methodu</h3>

<h3 id="1.?.3"><code>array</code> Methodu</h3>

<h3 id="1.?.4"><code>array</code> Methodu</h3>

<h3 id="1.?.5"><code>array</code> Methodu</h3>

<h3 id="1.?.6"><code>array</code> Methodu</h3>

<h3 id="1.?.7"><code>array</code> Methodu</h3>