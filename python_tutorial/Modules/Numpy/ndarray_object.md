# İçindekiler

- [`ndarray` Object](#1)

<h1 id="1"><code>ndarray</code> Object</h1>

NumPy'da tanımlanan en önemli obje, `ndarray` adı verilen N boyutlu bir array türüdür. `ndarray`, aynı type data'ların (bunlara element veya item denir ama ben element olarak bahsedeceğim) toplandığı bir koleksiyonudur (grid of value, collection). Bu elementlere erişmek için zero-based index'leme kullanılır (yani ilk elementin index'i `0` olarak ifade edilir). Bir `ndarray`'deki her bir element bellekte aynı boyutta yer kaplar ve `data-type` objesinin bir objesidir (`data-type` = `dtype`).

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
print(a,end="\n-------\n")
print(a[0],end="\n-------\n")
print(a[0][0])
```
**Output:**
```
[[1 2 3]
 [4 5 6]
 [7 8 9]]
-------
[1 2 3]
-------
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
NumPy'da dimension'lar **axis** olarak isimlendirilir (birden fazla dimension'dan bahsediyorsak **axes**). 2D array'lerle uğraşırken column ve row kavramlarıyla karşılaşmışsınızdır. Column ve row kavramları sadece 2D array'lerde geçerli olduğu için genel olarak axis (eksen) terimi kullanılır. Çok dimention'lu array'lerde axis'ler dıştan içe anlamına gelecek şekilde soldan sağa doğru sıralanır. Örnek:
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
print(a,end="\n-------\n")
a[:,0,0] = 1
print(a,end="\n-------\n")
a = np.zeros((2,3,4))
a[0,:,0] = 2
print(a,end="\n-------\n")
a = np.zeros((2,3,4))
a[0,0,:] = 3
print(a)
```
**Output:**
```
[[[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]

 [[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]]
-------
[[[1. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]

 [[1. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]]
-------
[[[2. 0. 0. 0.]
  [2. 0. 0. 0.]
  [2. 0. 0. 0.]]

 [[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]]
-------
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

`a` parametresine argüman olarak girilen array'in dimension ve her dimension'ındaki element sayısı bilgisini içeren bir tuple döndürür. Örnek:
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
Gördüğünüz gibi `np.shape(a)` ile `a.shape` arasında bir fark yoktur. İkisi de aynı bilgiyi verir.

**Not:** Bu işlemin yapılabilmesi için ilgili array'in eski ve yeni shape'i aynı sayıda elemente sahip olmalıdır aksi halde `ValueError: cannot reshape array of size 24 into shape (4,5)` örneğindeki gibi bir hata döndürür.

<h3 id="1.3.2"><code>reshape(a, newshape, order='C')</code> Attribute'u</h3>

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

Uygulandığı array'in her elementinin bellekte kapladığı alanı byte cinsinden döndürür. Örnek:
```py
import numpy as np

a1 = np.ones((5,), dtype=np.int8)
a2 = np.ones((5,), dtype=np.int32)
a3 = np.ones((5,), dtype=np.float16)

print(a1.itemsize) # Output: 1
print(a2.itemsize) # Output: 4
print(a3.itemsize) # Output: 2
```

<h3 id="1.3.1"><code>flags</code> Attribute'u</h3>

Bir array'in bellekte nasıl saklandığını gösteren bir özellik öbjesi (`<class 'numpy.core.multiarray.flagsobj'>`) döndürür. Örnek:
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

<h2 id="1.4">Array Oluşturmak</h2>

<h3 id="1.4.1"><code>array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)</code> Methodu</h3>

Bir array oluşturmak için en temel yöntem `array` methodunu kullanmaktır. Örnek:
```py
import numpy as np
print(type(np.array([1,2,3]))) # Output: <class 'numpy.ndarray'>
```
- **`object:array_like`**: Bu parametreye argüman olarak sequence, nested sequence, scalar bir değer (integer, float vs.), array döndüren `__array__` methoduna sahip bir şey... kısaca array interface ortaya çıkarabilecek (exposing) herhangi bir obje verilebilir. Bu parametre zorunludur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).
- **`dtype:data-type` (optional)**: Bu parametreye argüman olarak C-like veri türleri girilebilir. Böylece array'in öğeleri belirttiğiniz veri türünde olacaktır. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).
- **`copy:bool` (optional)**: Bu parametreye argüman olarak `True` veya `False` girilebilir. `True` ise array'in bellekteki verilerini kopyalar, `False` ise kopyalamaz. Default değeri `True`'dur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).
- **`order:{'C', 'F', 'A', 'K'}` (optional)**: Bu parametreye argüman olarak `C`, `F`, `A` veya `K` girilebilir. `C` ise array'in bellekte C dilindeki gibi (row-major) sıralandığı anlamına gelir (C-style contiguous segment), `F` ise array'in bellekte Fortran dilindeki gibi (column-major) sıralandığı anlamına gelir (Fortran-style contiguous segment), `A` ise array'in bellekteki verilerini kopyalamadan sıralamaya çalışır, `K` ise array'in bellekteki verilerini kopyalamadan sıralamaya çalışır. Default değeri `K`'dur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).
- **`subok:bool` (optional)**: Bu parametreye argüman olarak `True` veya `False` girilebilir. `True` ise array'in alt sınıflarını (subclass) döndürür, `False` ise döndürmez. Default değeri `False`'dur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).
- **`ndmin:int` (optional)**: Bu parametreye argüman olarak integer girilebilir. Array'in en az kaç boyutlu (dimension) olacağını belirtir. Default değeri `0`'dır. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).
- **`like:array_like` (optional)**: Bu parametreye argüman olarak array verilebilir. NumPy array objesi olmayan array'ler oluşturmanız gerektiğinde bu parametreye argüman olarak girilen array'in özelliklerini (properties) kullanarak array oluşturur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).

<h3 id="1.4.2"><code>empty(shape, dtype=float, order='C', *, like=None)</code> Methodu</h3>

İstenilen boyutlarda ve veri türünde başlatılmamış (uninitialized) bir array oluşturmak için kullanılır. Örnek:
```py
import numpy as np
print(np.empty((3,2), dtype = int))
```
**Output:**
```
[[1948283503  656434536]
 [1629497131  656434286]
 [1663051567 1634885992]]
```
- **`shape:int or sequence of ints`**: Array'in boyutlarını belirtir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.empty.html?highlight=empty#numpy.empty).
- **`dtype:data-type` (optional)**: Array'in veri türünü belirtir. Default değeri `float`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.empty.html?highlight=empty#numpy.empty).
- **`order:{'C', 'F'}` (optional)**: Array'in bellekteki sıralamasını belirtir. `C` ise C dilindeki gibi (row-major), `F` ise Fortran dilindeki gibi (column-major). Default değeri `C`'dir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.empty.html?highlight=empty#numpy.empty).
- **`like:array_like` (optional)**: Bu parametreye argüman olarak array verilebilir. NumPy array objesi olmayan array'ler oluşturmanız gerektiğinde bu parametreye argüman olarak girilen array'in özelliklerini (properties) kullanarak array oluşturur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.empty.html?highlight=empty#numpy.empty).

<h3 id="1.4.3"><code>zeros(shape, dtype=float, order='C', *, like=None)</code> Methodu</h3>

İstenilen boyutlarda ve veri türünde sıfırlardan oluşan bir array oluşturmak için kullanılır. Örnek:
```py
import numpy as np
print(np.zeros((3,2), dtype = int))
```
**Output:**
```
[[0 0]
 [0 0]
 [0 0]]
```
- **`shape:int or sequence of ints`**: Array'in boyutlarını belirtir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.zeros.html?highlight=zeros#numpy.zeros).
- **`dtype:data-type` (optional):** Array'in veri türünü belirtir. Default değeri `float`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.zeros.html?highlight=zeros#numpy.zeros).
- **`order:{'C', 'F'}` (optional)**: Array'in bellekteki sıralamasını belirtir. `C` ise C dilindeki gibi (row-major), `F` ise Fortran dilindeki gibi (column-major). Default değeri `C`'dir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.zeros.html?highlight=zeros#numpy.zeros).
- **`like:array_like` (optional)**: Bu parametreye argüman olarak array verilebilir. NumPy array objesi olmayan array'ler oluşturmanız gerektiğinde bu parametreye argüman olarak girilen array'in özelliklerini (properties) kullanarak array oluşturur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.zeros.html?highlight=zeros#numpy.zeros).

<h3 id="1.4.4"><code>ones(shape, dtype=None, order='C', *, like=None)</code> Methodu</h3>

İstenilen boyutlarda ve veri türünde birlerden oluşan bir array oluşturmak için kullanılır. Örnek:
```py
import numpy as np
print(np.ones((3,2), dtype = int))
```
**Output:**
```
[[1 1]
 [1 1]
 [1 1]]
```
- **`shape:int or sequence of ints`**: Array'in boyutlarını belirtir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.ones.html?highlight=ones#numpy.ones).
- **`dtype:data-type` (optional)**: Array'in veri türünü belirtir. Default değeri `float`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.ones.html?highlight=ones#numpy.ones).
- **`order:{'C', 'F'}` (optional)**: Array'in bellekteki sıralamasını belirtir. `C` ise C dilindeki gibi (row-major), `F` ise Fortran dilindeki gibi (column-major). Default değeri `C`'dir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.ones.html?highlight=ones#numpy.ones).
- **`like:array_like` (optional)**: Bu parametreye argüman olarak array verilebilir. NumPy array objesi olmayan array'ler oluşturmanız gerektiğinde bu parametreye argüman olarak girilen array'in özelliklerini (properties) kullanarak array oluşturur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.ones.html?highlight=ones#numpy.ones).

<h3 id="1.4.5"><code>asarray(a, dtype=None, order=None, *, like=None)</code> Methodu</h3>

Verilen argümanı array objesine dönüştürür. `array` methodundan farkı, daha az parametre almasıdır. Örnek:
```py
import numpy as np
print(np.asarray([1,2,3])) # Ourput: [1 2 3]
```
- **`a:array_like`**: Array objesine dönüştürülecek argüman. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.asarray.html?highlight=asarray#numpy.asarray).
- **`dtype:data-type` (optional)**: Array'in veri türünü belirtir. Default değeri `float`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.asarray.html?highlight=asarray#numpy.asarray).
- **`order:{'C', 'F'}` (optional)**: Array'in bellekteki sıralamasını belirtir. `C` ise C dilindeki gibi (row-major), `F` ise Fortran dilindeki gibi (column-major). Default değeri `C`'dir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.asarray.html?highlight=asarray#numpy.asarray).
- **`like:array_like` (optional)**: Bu parametreye argüman olarak array verilebilir. NumPy array objesi olmayan array'ler oluşturmanız gerektiğinde bu parametreye argüman olarak girilen array'in özelliklerini (properties) kullanarak array oluşturur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.asarray.html?highlight=asarray#numpy.asarray).

**Not:** `asarray` methodu, `array` methodundan farklı olarak, argüman olarak verilen array'i kopyalamaz. Yani argüman olarak verilen array'i değiştirdiğinizde, `asarray` methodu ile oluşturulan array de değişecektir. Örnek:
```py
import numpy as np

a = np.array([1,2,3,4,5])
array_exp = np.array(a)
asarray_exp = np.asarray(a)
print(a,array_exp,asarray_exp,sep='\n')
a[0] = 10
print(a,array_exp,asarray_exp,sep='\n')
```
**Output:**
```
[1 2 3 4 5]
[1 2 3 4 5]
[1 2 3 4 5]
[10  2  3  4  5]
[1 2 3 4 5]
[10  2  3  4  5]
```

**Not:** `array` ve `asarray` methodları aynı uzunluktaki nested listeleri array'e dönüştürebilir ama farklı uzunluktaki nested listeleri array'e dönüştürürken farklı davranırlar. Örnek:
```py
import numpy as np

a = np.array([[1,2,3],[4,5]])
b = np.asarray([[1,2,3],[4,5]])
print(a) # Output: [list([1, 2, 3]) list([4, 5])]
print(b) # Output: [list([1, 2, 3]) list([4, 5])]
```

<h3 id="1.4.6"><code>frombuffer(buffer, dtype=float, count=- 1, offset=0, *, like=None)</code> Methodu</h3>

Verilen buffer'ı array objesine dönüştürür. Örnek:
```py
import numpy as np

s = b'Hello World'
a = np.frombuffer(s, dtype = 'S1')
print(a) # Output: [b'H' b'e' b'l' b'l' b'o' b' ' b'W' b'o' b'r' b'l' b'd']
```
- **`buffer:object`**: Array objesine dönüştürülecek buffer. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.frombuffer.html?highlight=frombuffer#numpy.frombuffer).
- **`dtype:data-type` (optional)**: Array'in veri türünü belirtir. Default değeri `float`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.frombuffer.html?highlight=frombuffer#numpy.frombuffer).
- **`count:int` (optional)**: Dönüştürülecek buffer'daki byte sayısını belirtir. Default değeri `-1`'dir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.frombuffer.html?highlight=frombuffer#numpy.frombuffer).
- **`offset:int` (optional)**: Dönüştürülecek buffer'daki ilk byte'ın indexini belirtir. Default değeri `0`'dır. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.frombuffer.html?highlight=frombuffer#numpy.frombuffer).
- **`like:array_like` (optional)**: Bu parametreye argüman olarak array verilebilir. NumPy array objesi olmayan array'ler oluşturmanız gerektiğinde bu parametreye argüman olarak girilen array'in özelliklerini (properties) kullanarak array oluşturur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.frombuffer.html?highlight=frombuffer#numpy.frombuffer).

<h3 id="1.4.7"><code>fromiter(iter, dtype, count=- 1, *, like=None)</code> Methodu</h3>

Verilen iterable objeyi array objesine dönüştürür. Örnek:
```py
import numpy as np

a = iter(range(5))
b = np.fromiter(a, dtype = float)
print(b) # Output: [0. 1. 2. 3. 4.]
```
- **`iterable:iterable`**: Array objesine dönüştürülecek iterable obje. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.fromiter.html?highlight=fromiter#numpy.fromiter).
- **`dtype:data-type`**: Array'in veri türünü belirtir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.fromiter.html?highlight=fromiter#numpy.fromiter).
- **`count:int` (optional)**: Dönüştürülecek iterable objedeki eleman sayısını belirtir. Default değeri `-1`'dir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.fromiter.html?highlight=fromiter#numpy.fromiter).
- **`like:array_like` (optional)**: Bu parametreye argüman olarak array verilebilir. NumPy array objesi olmayan array'ler oluşturmanız gerektiğinde bu parametreye argüman olarak girilen array'in özelliklerini (properties) kullanarak array oluşturur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.fromiter.html?highlight=fromiter#numpy.fromiter).

<h3 id="1.4.8"><code>arange(start, stop, step, dtype=None, *, like=None)</code> Methodu</h3>

`start` ve `stop` (`stop` hariç) arasındaki sayıları `step` kadar arttırarak elde edilen sayı dizisini array objesine dönüştürür. Örnek:
```py
import numpy as np

a = np.arange(10)
b = np.arange(1,9,2)
print(a) # Output: [0 1 2 3 4 5 6 7 8 9]
print(b) # Output: [1 3 5 7]
```
- **`start:int` (optional)**: Array'in ilk elemanını belirtir. Default değeri `0`'dır. `range` fonksiyonundaki `start` parametresindeki kurallar geçerlidir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.arange.html?highlight=arange#numpy.arange).
- **`stop:int`**: Array'in son elemanını belirtir. `stop` dahil değildir. `range` fonksiyonundaki `stop` parametresindeki kurallar geçerlidir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.arange.html?highlight=arange#numpy.arange).
- **`step:int` (optional)**: Array'in elemanlarının arasındaki farkı belirtir. Default değeri `1`'dir. `range` fonksiyonundaki `step` parametresindeki kurallar geçerlidir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.arange.html?highlight=arange#numpy.arange).
- **`dtype:data-type` (optional)**: Array'in veri türünü belirtir. Default değeri `float`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.arange.html?highlight=arange#numpy.arange).
- **`like:array_like` (optional)**: Bu parametreye argüman olarak array verilebilir. NumPy array objesi olmayan array'ler oluşturmanız gerektiğinde bu parametreye argüman olarak girilen array'in özelliklerini (properties) kullanarak array oluşturur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.arange.html?highlight=arange#numpy.arange).

<h3 id="1.4.9"><code>linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)</code> Methodu</h3>

`start` ve `stop` arasındaki `num` kadar birbirine eşit uzaklıkta olan sayıları içeren bir array objesi döndürür. Örnek:
```py
import numpy as np

a = np.linspace(10,20,5)
print(a) # Output: [10.  12.5 15.  17.5 20. ]
```
- **`start:int`**: Array'in ilk elemanını belirtir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.linspace.html?highlight=linspace#numpy.linspace).
- **`stop:int`**: Array'in son elemanını belirtir. Dahil edilip edilmeyeceğini `endpoint` parametresi belirler. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.linspace.html?highlight=linspace#numpy.linspace).
- **`num:int`**: Array'in eleman sayısını belirtir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.linspace.html?highlight=linspace#numpy.linspace).
- **`endpoint:bool` (optional)**: `stop` değerinin dahil edilip edilmeyeceğini belirtir. Default değeri `True`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.linspace.html?highlight=linspace#numpy.linspace).
- **`retstep:bool` (optional)**: Array'in elemanlarının arasındaki farkı döndürüp döndürmeyeceğini belirtir. Default değeri `False`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.linspace.html?highlight=linspace#numpy.linspace). Örnek:
  ```py
  import numpy as np

  a = np.linspace(10,20,5,retstep=True)
  print(a) # Output: (array([10. , 12.5, 15. , 17.5, 20. ]), 2.5)
  ```
  Buradaki `2.5` array'in elemanlarının arasındaki farktır.
- **`dtype:data-type` (optional)**: Array'in veri türünü belirtir. Default değeri `float`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.linspace.html?highlight=linspace#numpy.linspace).
- **`axis:int` (optional)**: Array'in boyutunu belirtir. Default değeri `0`'dır. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.linspace.html?highlight=linspace#numpy.linspace).

<h3 id="1.4.10"><code>logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)</code> Methodu</h3>

`start` ve `stop` arasındaki `num` kadar birbirine eşit uzaklıkta olan sayıların `base` parametresinde belirtilen taban üzerindeki logaritmasını içeren bir array objesi döndürür. Yani `base ** start` ile `base ** stop` arasındaki `num` kadar birbirine eşit uzaklıkta olan sayıları içeren bir array objesi döndürür. Örnek:
```py
import numpy as np

a = np.logspace(1,10,10,base=2)
print(a) # Output: [   2.    4.    8.   16.   32.   64.  128.  256.  512. 1024.]
```
- **`start:int`**: Array'in ilk elemanının logaritmasını alınacak sayıyı belirtir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.logspace.html?highlight=logspace#numpy.logspace).
- **`stop:int`**: Array'in son elemanının logaritmasını alınacak sayıyı belirtir. Dahil edilip edilmeyeceğini `endpoint` parametresi belirler. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.logspace.html?highlight=logspace#numpy.logspace).
- **`num:int`**: Array'in eleman sayısını belirtir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.logspace.html?highlight=logspace#numpy.logspace).
- **`endpoint:bool` (optional)**: `stop` değerinin dahil edilip edilmeyeceğini belirtir. Default değeri `True`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.logspace.html?highlight=logspace#numpy.logspace).
- **`base:float` (optional)**: Array'in elemanlarının logaritmasını alınacak sayıyı belirtir. Default değeri `10.0`'dur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.logspace.html?highlight=logspace#numpy.logspace).
- **`dtype:data-type` (optional)**: Array'in veri türünü belirtir. Default değeri `float`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.logspace.html?highlight=logspace#numpy.logspace).
- **`axis:int` (optional)**: Array'in boyutunu belirtir. Default değeri `0`'dır. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.logspace.html?highlight=logspace#numpy.logspace).

<h2 id="1.5">Indexing ve Slicing</h2>

Array'in elemanlarına aynı Python'ın build-in container objelerindeki gibi index numarası ile erişebilirsiniz. Birden fazla indexleme yöntemi mevcuttur:
- **Integer Indexing**: Array'in elemanlarına tek tek index numarası ile erişebilirsiniz. Örnek:
  ```py
  import numpy as np

  a = np.array([1,2,3,4,5])
  print(a[0]) # Output: 1
  print(a[2]) # Output: 3
  ```
  Çok boyutlu array'lerde axis'ler dıştan içe anlamına gelecek şekilde soldan sağa doğru sıraladığından integer indexlemeyi buna göre yapmalısınız. Örnek:
  ```py
  import numpy as np

  a = np.array([[[1,2,3],[4,5,6],[7,8,9]],
              [[10,11,12],[13,14,15],[16,17,18]],
              [[19,20,21],[22,23,24],[25,26,27]]])
  print(a, end='\n--------\n')
  print(a[0], end='\n--------\n')
  print(a[0,], end='\n--------\n')
  print(a[0][0], end='\n--------\n')
  print(a[0,0], end='\n--------\n')
  print(a[0][0][0], end='\n--------\n')
  print(a[0,0,0])
  ```
  Output:
  ```py
  [[[ 1  2  3]
    [ 4  5  6]
    [ 7  8  9]]

  [[10 11 12]
    [13 14 15]
    [16 17 18]]

  [[19 20 21]
    [22 23 24]
    [25 26 27]]]
  --------
  [[1 2 3]
  [4 5 6]
  [7 8 9]]
  --------
  [[1 2 3]
  [4 5 6]
  [7 8 9]]
  --------
  [1 2 3]
  --------
  [1 2 3]
  --------
  1
  --------
  1
  ```

- **Boolean Indexing**: Array'in elemanlarına tek tek boolean değerler ile erişebilirsiniz. Örnek:
  ```py
  import numpy as np

  a = np.array([1,2,3,4,5])
  print(a[[True,False,True,False,True]]) # Output: [1 3 5]

  a = np.array([[1,2,3],[4,5,6]])
  print(a[[[True,False,True],[False,True,True]]]) # Output: [1 3 5 6]
  ```

- **Filter Indexing**: Array'in elemanlarına filtreleme yaparak erişebilirsiniz. Örnek:
  ```py
  import numpy as np

  a = np.array([1,2,3,4,5])
  print(a[a > 3]) # Output: [4 5]
  print(a[(a > 3) & (a < 5)]) # Output: [4]
  ```

- **Fancy Indexing**: Array'in elemanlarına tek tek index numarası ile erişebilirsiniz. Örnek:
  ```py
  import numpy as np

  a = np.array([1,2,3,4,5])
  print(a[[0,2,4]]) # Output: [1 3 5]
  ```

- **Field Indexing**: Array'in elemanlarına tek tek field ismi ile erişebilirsiniz. Örnek:
  ```py
  import numpy as np

  a = np.array([(1,2,3),(4,5,6)],dtype=[('a','i4'),('b','i4'),('c','i4')])
  print(a['a']) # Output: [1 4]
  print(a['b']) # Output: [2 5]
  print(a['c']) # Output: [3 6]
  ```

- **Ellipsis Indexing**: Array'in birden fazla boyutlu olduğu durumlarda, array'in tüm boyutlarını tek seferde erişmek için kullanılır. Örnek:
  ```py
  import numpy as np

  a = np.ones((2,2,2,2))
  print(a[:,:,:,0], end='\n----------------\n')
  print(a[...,0])
  ```
  Output:
  ```py
  [[[1. 1.]
    [1. 1.]]

   [[1. 1.]
    [1. 1.]]]
  ----------------
  [[[1. 1.]
    [1. 1.]]

   [[1. 1.]
    [1. 1.]]]
  ```
Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/arrays.indexing.html#basic-slicing-and-indexing).

<h2 id="1.6">Broadcasting</h2>

Bir vector ve bir scalar veya uyumlu boyutlardaki array'ler arasında yapılan işlemlere **broadcasting** denir. NumPy bu işlemlerin/işlemin her hücrede olması gerektiğini anlar.