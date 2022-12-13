# İçindekiler

- [Broadcasting](#1)

<h1 id="1">Broadcasting</h1>

Array'ler arasında işlem yapma kabiliyetine **broadcasting** denir. Broadcasting'in mümkün olabilmesi için vector ve bir scalar veya uyumlu boyutlardaki arrayler arasında işlem yapılmalıdır. Farklı boyutlardaki arrayler arasında doğrudan işlem yapamazsınız. Farklı boyutlardaki arrayler arasında işlem yapılabilmesi için boyutları uyumlu hale getirilmelidir. Bunun için arraylerin boyutlarından en küçük olanı, diğer arrayin boyutlarına uygun şekilde yayımlanmalıdır (broadcasting). Örnek:
```py
import numpy as np

a = np.array([1,2,3,4,5])
print(a + 1) # Output: [2 3 4 5 6] (vector + scalar)

a = np.array([[1,2,3],[4,5,6]])
b = np.array([1,2,3])
print(a + b) # Output: [[2 4 6] [5 7 9]] (array + vector)

a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
b = np.array([[1,2,3],[4,5,6]])
print(a+b) # Output: [[[ 2  4  6] [ 8 10 12]] [[ 8 10 12] [14 16 18]]] (array + array)
```
Gördüğünüz gibi `a` arrayinin boyutu `(2,3)` iken `b` arrayinin boyutu `(3,)` olduğu için daha küçük bir array olan `b`, uyumlu shape'e sahip olmaları için daha büyük array olan `a` boyutuna yayımlanlanmıştır (broadcast to). Ardından `a` ile `b` arrayleri arasında element-to-element işlemi yapmak mümkün olmuştur. Bu yayımlama (broadcast to) işlemini `broadcast_to` fonksiyonu ile de yapabilirsiniz. Örnek:
```py
import numpy as np

a = np.array([1,2,3])
print(np.broadcast_to(a,(2,3))) # Output: [[1 2 3] [1 2 3]]
```
Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/user/basics.broadcasting.html).