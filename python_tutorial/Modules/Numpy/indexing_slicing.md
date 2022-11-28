# İçindekiler

- [Indexing ve Slicing](#1)

<h1 id="1">Indexing ve Slicing</h1>

Array'in elementlerine aynı Python'ın build-in container objelerindeki gibi index numarası ile erişebilirsiniz. Birden fazla indexleme yöntemi mevcuttur:
- **Integer Indexing**: Array'in elementlerine tek tek index numarası ile erişebilirsiniz. Örnek:
  ```py
  import numpy as np

  a = np.array([1,2,3,4,5])
  print(a[0]) # Output: 1
  print(a[2]) # Output: 3
  ```
  Çok boyutlu array'lerde axis'ler dıştan içe anlamına gelecek şekilde soldan sağa doğru dolayı integer indexlemeyi buna göre yapmalısınız. Örnek:
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

- **Boolean Indexing**: Array'in elementlerine tek tek boolean değerler ile erişebilirsiniz. Örnek:
  ```py
  import numpy as np

  a = np.array([1,2,3,4,5])
  print(a[[True,False,True,False,True]]) # Output: [1 3 5]

  a = np.array([[1,2,3],[4,5,6]])
  print(a[[[True,False,True],[False,True,True]]]) # Output: [1 3 5 6]
  ```

- **Filter Indexing**: Array'in elementlerine filtreleme yaparak erişebilirsiniz. Örnek:
  ```py
  import numpy as np

  a = np.array([1,2,3,4,5])
  print(a[a > 3]) # Output: [4 5]
  print(a[(a > 3) & (a < 5)]) # Output: [4]
  ```

- **Fancy Indexing**: Array'in elementlerine tek tek index numarası ile erişebilirsiniz. Örnek:
  ```py
  import numpy as np

  a = np.array([1,2,3,4,5])
  print(a[[0,2,4]]) # Output: [1 3 5]
  ```

- **Field Indexing**: Array'in elementlerine tek tek field ismi ile erişebilirsiniz. Örnek:
  ```py
  import numpy as np

  a = np.array([(1,2,3),(4,5,6)],dtype=[('a','i4'),('b','i4'),('c','i4')])
  print(a['a']) # Output: [1 4]
  print(a['b']) # Output: [2 5]
  print(a['c']) # Output: [3 6]
  ```

- **Ellipsis Indexing**: Array'in birden fazla boyutlu olduğu durumlarda, array'in istenilen boyutlarına tek seferde erişmek için kullanılır. Örnek:
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