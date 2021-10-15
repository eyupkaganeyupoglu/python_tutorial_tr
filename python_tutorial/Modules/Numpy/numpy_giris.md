# Numpy Giriş

Numpy, normal Python ile yapacağınız işlemlerden çok daha hızlı çalışır çünkü çekirdeğinde **C** dili ile yazılmış bir kütüphanedir. Numpy [**vectorization**](https://stackoverflow.com/a/1422181/15170972 "https://stackoverflow.com/a/1422181/15170972")'ı desteklediği için bu kadar hızlı çalışır. Normal Python vectorization'ı desteklemediği için hızlı değildir. Örnek:
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

Numpy [**vectorization**](https://stackoverflow.com/a/1422181/15170972 "https://stackoverflow.com/a/1422181/15170972")'ı desteklediği için bu kadar hızlı çalışır. Normal Python vectorization'ı desteklemediği için hızlı değildir.

Numpy kendi başına pek bir işe yaramaz. Veri manipülasyonu, veri bilimi, yapay zeka gibi alanlarda kullanılır. Gelen büyük verileri işlemek için Numpy kullanılır.