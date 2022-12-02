# İçindekiler

- [](#1)
  - [`` Methodu](#1.1)
  - [`` Methodu](#1.2)
  - [`` Methodu](#1.3)

<h1 id="1">I/O with NumPy</h1>

`ndarray` objeleri disk üzerinde saklanabilir ve tekrar yüklenerek kullanılabilir. Bunun için kullanılan fonksiyonlar şunlardır:
- `save(file, arr, allow_pickle=True, fix_imports=True)`: `arr` parametresine girilen `ndarray` objesini `file` parametresinde belirtilen dosyaya kaydeder. Oluşturulan dosya `.npy` uzantılıdır.
- `savez(file, *args, **kwds)`: `save()` fonksiyonu ile aynı işlevi görür, fakat birden fazla `ndarray` objesi kaydedilebilir. Oluşturulan dosya `.npz` uzantılıdır.
- `savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='', header='', footer='', comments='# ', encoding=None)`: `X` parametresine girilen `ndarray` objesini `fname` parametresinde belirtilen dosyaya kaydeder. Oluşturulan dosya `.csv` ya da `.txt` uzantılıdır.
- `load(file, mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII')`: `file` parametresinde belirtilen dosyayı yükler ve `ndarray` objesi olarak döndürür.
- `loadtxt(fname, dtype=<class 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0, encoding='bytes', max_rows=None)`: `fname` parametresinde belirtilen dosyayı yükler ve `ndarray` objesi olarak döndürür.

```py
import numpy as np

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
a3 = np.array([7, 8, 9])
np.save("file1", a1)
np.savez("file2",a2,a3)
b1 = np.load("file1.npy")
b2 = np.load("file2.npz")
print(b1) # Output: [1 2 3]
print(b2) # Output: <numpy.lib.npyio.NpzFile object at 0x000002C67FE61DC0>
```
```py
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
np.savetxt('new_file.csv', a)
np.savetxt('new_file.txt', a)
b1 = np.loadtxt('new_file.csv')
b2 = np.loadtxt('new_file.txt')
print(b1) # Output: [1. 2. 3. 4. 5. 6. 7. 8.]
print(b2) # Output: [1. 2. 3. 4. 5. 6. 7. 8.]
```

**Not:** Metin dosyaları ile uğraşmak ve paylaşmak daha kolay olsa bile `.npy` ve `.npz` dosyaları daha küçük boyuttadır ve daha hızlı okunur.