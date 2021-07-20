**Ön Bilgi:** Operand, işlenen; operator, işleç/işlemci anlamlarına gelmektedir. `2 + 2` işlemindeki ikiler operand, artı işaret operator'dır.

# Arithmetic Operators

## Addition (Toplama) (`+`) Operatörü
Addition operatörü, iki operand'ı birbiriyle toplar / birbirine ekler. Numeric type'larda toplama işlemi, text type'larda ekleme işlemi için kullanılır.
```py
print(5 + 10)
# Output: 15

print("Python" + " " + "C++")
# Output: Python C++
```

## Subtraction (Çıkarma) (`-`) Operatörü
Subtraction operatörü, iki operandı birbirinden çıkarır. Numenic type'larda kullanılır.
```py
print(10 - 2)
# Output: 8
```

## Multiplication (Çarpma) (`*`) Operatörü
Multiplication operatörü, iki operandı birbiriyle çarpar. Numenic type'larda çarpma işlemi, text type'larda ise çoklu yazdırma işlemleri için kullanılır.
```py
print(5 * 10)
# Output: 50

print("Beş " * 5)
# Output: Beş Beş Beş Beş Beş 
```

## Division (Bölme) (`/`) Operatörü
Division operatörü, iki operandı birbirinden çıkarır. Numenic type'larda kullanılır.
```py
print(5 + 10)
# Output: 15
```

## Exponentiation (Üs Alma) (`**`) Operatörü
Exponentiation operatörü, ilk operand'ın ikince operand'a göre üssünü alır. Numenic type'larda kullanılır.
```py
print(5 + 10)
# Output: 15
```

## Floor division (Taban Bölme) (`//`) Operatörü
Floor division operatörü, iki operand'ı birbirine bölüp, bölüm kısmını döndürür. Numenic type'larda kullanılır.
```py
print(5 + 10)
# Output: 15
```

## Modulus (Modül) (`%`) Operatörü
Modulus operatörü, iki operand'ı birbirine bölüp, kalan kısmını döndürür. Numenic type'larda kullanılır.
```py
print(5 + 10)
# Output: 15
```
# Comparison Operators

## `==` Operatörü
İki operand birbirine eşitse `True`, değilse `False` döndürür.
```py
print(1 == 1) # Output: True
print(1 == 2) # Output: False
```

## `!=` Operatörü
İki operand birbirine eşitse `False`, değilse `True` döndürür.
```py
print(1 != 2) # Output: True
print(1 != 1) # Output: False
```

## `>` Operatörü
Soldaki operand sağdaki operand'dan büyükse `True`, değilse `False` döndürür.
```py
print(2 > 1) # Output: True
print(1 > 2) # Output: False
```

## `<` Operatörü
Sağdaki operand soldaki operand'dan büyükse `True`, değilse `False` döndürür.
```py
print(1 < 2) # Output: True
print(2 < 1) # Output: False
```

## `>=` Operatörü
Soldaki operand sağdaki operan'dan büyükse ya da eşitse `True`, değilse `False` döndürür.
```py
print(2 >= 1) # Output: True
print(2 >= 2) # Output: True
print(1 >= 2) # Output: False
```

## `<=` Operatörü
Sağdaki operand soldaki operan'dan büyükse ya da eşitse `True`, değilse `False` döndürür.
```py
print(1 <= 2) # Output: True
print(1 <= 1) # Output: True
print(2 <= 1) # Output: False
```

# Logical Operators

## `and` Operatörü
Bu mantıksal bağlaç, bütün karşılaştırma işlemlerinin sonucunun `True` olmasına bakar. Bağlanan karşılaştırma işlemlerinin **hepsinin** kendi içinde sonucu `True` ise genel sonuç `True` , diğer durumlarda ise sonuç `False` çıkar.
```py
print(1 == 1 and 2 == 2 and 3 == 3) # Output: True
print(1 == 1 and 2 == 2 and 3 != 3) # Output: False
```
Python bu işlemi **soldan sağa** okumaya başlar. Bir tane `False`'a denk gelirse sonuç `False` olur.

## `or` Operatörü
Bu mantıksal bağlaç, en az bir karşılaştırma işlemlerinin sonucunun `True` olmasına bakar. Bağlanan karşılaştırma işlemlerinin **en az bir tanesinin** kendi içinde sonucu `True` ise genel sonuç `True` , hepsi `False` ise sonuç `False` çıkar.
```py
print(1 == 1 and 2 != 2 and 3 != 3) # Output: True
print(1 != 1 and 2 != 2 and 3 != 3) # Output: False
```

## `not` Operatörü
`not` operatörü mantıksal bir bağlaç değildir. Mantıksal bağlaç veya logic ifadeleri tersine çevirir. Yani `True`'yu `False`, `False`'ı `True` yapar.
```py
print(not (1 != 1)) # Output: True
```

# Bitwise operators

## Bitwise AND (`&`) Operator
Bitsel AND `&` operatörü, her iki işlenen de 1 ise 1 döndürür. Aksi halde, 0 döndürür. Mantıktaki **"ve"** bağlacına benzer.
| `A` | `B` | `A & B` |
|--|--|--|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |
```
12 = 00001100 (In Binary)
25 = 00011001 (In Binary)

00001100 & 00011001 = 00001000

8 = 00001000 (In Binary)
```
Yukarıdaki işlemin Python'da karşılığı:
```py
bao_1 = 12 # bao_1: bitsel_and_operatoru_1
bao_2 = 25 # bao_2: bitsel_and_operatoru_2
print(bao_1, bao_2, bao_1 & bao_2, sep="\n")
```

## Bitwise OR (`|`) Operator
Bitsel OR `|` işlenenlerden en az biri 1 ise operatör 1 döndürür. Aksi halde 0 döndürür. Mantıktaki **"veya"** bağlacına benzer.
| `A` | `B` | `A OR B` |
|--|--|--|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |
```
12 = 00001100 (In Binary)
25 = 00011001 (In Binary)

00001100 | 00011001 = 00011101

29 = 00011101 (In Binary)
```
Yukarıdaki işlemin Python'da karşılığı:
```py
bao_1 = 12 # bao_1: bitsel_and_operatoru_1
bao_2 = 25 # bao_2: bitsel_and_operatoru_2
print(bao_1, bao_2, bao_1 | bao_2, sep="\n")
```

## Bitwise XOR (`^`) Operator:
Bitsel XOR `^` operatörü, işlenenler birbirinden farklıysa 1, aynıysa 0 döndürür. Mantıktaki **"ya da"** bağlacına benzer.
| `A` | `B` | `A ^ B` |
|--|--|--|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |
```
12 = 00001100 (In Binary)
25 = 00011001 (In Binary)

00001100 ^ 00011001 = 00010101

21 = 00010101 (In Binary)
```
Yukarıdaki işlemin Python'da karşılığı:
```py
bao_1 = 12 # bao_1: bitsel_and_operatoru_1
bao_2 = 25 # bao_2: bitsel_and_operatoru_2
print(bao_1, bao_2, bao_1 ^ bao_2, sep="\n")
```

## Bitwise Complement (`~`) Operator
Bu operatör sadece bir operand üzerinde çalışır. `~` tanımlayıcısına sahiptir. 1'i 0'a, 0'ı 1'e dönüştürür. `N` adında bir operant olsun. `N` operantı *bitwise complement operatörü*nden etkilenirse `-(N + 1)` değerine dönüşür Örneğin:
```
-36 = -(35+1)

35 = 00100011 (In Binary)
~ 00100011 = 11011100
-36 = 11011100 (In Binary)
```
Yukarıdaki işlemin Python'da karşılığı:
```py
bao_1 = 35 # bao_1: bitsel_and_operatoru_1
print(~ bao_1)
```

## Binary Left Shift Operator
Basitçe, bir binary sayıyı sola kaydırır. Kaydırma işlemi sırasında boşluklar `0` ile tamamlanır. Teknik açıklamak gerekirse; 22 decimal sayısının binary versiyonu `00010110`, 88 decimal sayısının binary versiyonu `01011000`'dir. `22 << 2` işleminden sonra 22 (`N`),  88'e (`N` * (2^2^)) dönüşür.
```
22 = 00010110 (In Binary)

00010110 << 2 = 01011000

88 = 01011000 (In Binary)
```
Yukarıdaki işlemin Python'da karşılığı:
```py
bao_1 = 22 # bao_1: bitsel_and_operatoru_1
print(bao_1 << 2)
```

## Binary Right Shift Operator
Basitçe, bir binary sayıyı sağa kaydırır. Kaydırma işlemi sırasında boşluklar `0` ile tamamlanır. Teknik açıklamak gerekirse; 32 decimal sayısının binary versiyonu `00100000`, 8 decimal sayısının binary versiyonu `00001000`'dir. `32 >> 2` işleminden sonra 32 (`N`),  8'e (`N` / (2^2^)) dönüşür.
```
32 = 00100000 (In Binary)

00100000 >> 2 = 00001000

8 = 00001000 (In Binary)
```
Yukarıdaki işlemin Python'da karşılığı:
```py
bao_1 = 32 # bao_1: bitsel_and_operatoru_1
print(bao_1 >> 2)
```

**Not:** Bir decimal sayı üzerinde binary shift operatör kullanırsanız, işlemler binary form'da yapılsa bile output decimal formda verilir.

**Not:** C++ gibi low level dillerde shift operator'ları kullanırken negatif sayılarla ve data type'ın tutabileceği data boyutundan daha büyük sayılarla işlemler yapılması sıkıntıydı. Bu kısıtlama, gözlemlediğim kadarıyla Python'da yok.

# Assignment Operators

## Assignment `=` Operatörü
Sağdaki operand'ı soldaki opranda **atamak** için kullanılır. Örneğin bir value'yu bir variable'a atamanızı sağlar. Ornek:
```py
a = 15
b = 30
# etc.
```

## `+=` Operatörü
`a += 5` işlemi `a = a + 5` anlamına gelmektedir.
```py
a = 5
print(a) # Output: 5
a += 5
print(a) # Output: 10
```

## `-=` Operatörü
`a -= 5` işlemi `a = a - 5` anlamına gelmektedir.
```py
a = 5
print(a) # Output: 5
a -= 5
print(a) # Output: 0
```

## `*=` Operatörü
`a *= 5` işlemi `a = a * 5` anlamına gelmektedir.
```py
a = 5
print(a) # Output: 5
a *= 5
print(a) # Output: 25
```

## `/=` Operatörü
`a +/= 5` işlemi `a = a / 5` anlamına gelmektedir.
```py
a = 5
print(a) # Output: 5
a /= 5
print(a) # Output: 1
```

## `**=` Operatörü
`a **= 5` işlemi `a = a ** 5` anlamına gelmektedir.
```py
a = 5
print(a) # Output: 5
a **= 5
print(a) # Output: 3125
```

## `//=` Operatörü
`a //= 5` işlemi `a = a // 5` anlamına gelmektedir.
```py
a = 5
print(a) # Output: 5
a //= 2
print(a) # Output: 2
```

## `%=` Operatörü
`a %= 5` işlemi `a = a % 5` anlamına gelmektedir.
```py
a = 5
print(a) # Output: 5
a %= 2
print(a) # Output: 1
```

## `&=` Operatörü
`a &= 25` işlemi `a = a & 25` anlamına gelmektedir.
```py
a = 12
print(a) # Output: 12
a &= 25
print(a) # Output: 8
```

## `|=` Operatörü
`a |= 5` işlemi `a = a | 25` anlamına gelmektedir.
```py
a = 12
print(a) # Output: 12
a |= 25
print(a) # Output: 29
```

## `^=` Operatörü
`a ^= 5` işlemi `a = a ^ 25` anlamına gelmektedir.
```py
a = 12
print(a) # Output: 12
a ^= 25
print(a) # Output: 21
```

## `<<=` Operatörü
`a <<= 5` işlemi `a = a << 2` anlamına gelmektedir.
```py
a = 22
print(a) # Output: 22
a <<= 2
print(a) # Output: 88
```

## `>>=` Operatörü
`a >>= 5` işlemi `a = a >> 2` anlamına gelmektedir.
```py
a = 32
print(a) # Output: 32
a >>= 2
print(a) # Output: 8
```

# Identity operators
Python’da her nesnenin, o nesneyi işaret eden geçici bir kimlik numarası ***(identity)*** vardır. Identity'e kısaca **ID** denilir.
```py
a = "Benim id'm ne?"
print(id(a)) # Output: 2048499024880
```

**`is` operatörü**, kıyaslanan iki objenin id'lerinin aynı olma durumunu kontrol eder. **`is not` operatörü** ise,kıyaslanan iki objenin id'lerinin aynı olmama durumunu kontrol eder. Örnek:
```py
a="Python"
print("Önceki a: ", id(a))   # Output: Önceki a:  1747376761776
b="Pytho"
print("Önceki  b: ", id(b))  # Output: Önceki b:  1747376833520
b+="n"
print("Sonraki b: ", id(b))  # Output: Sonraki b:  1747377137584

print(a,b, sep=", ")         # Output: Python, Python
print(a is b)                # Output: False
print(a is not b)            # Output: True
print("Önceki a: ", id(a))   # Output: Önceki a:  1747376761776
print("Sonraki b: ", id(b))  # Output: Sonraki b:  1747377137584
```
Buradaki olaya **String Concatenation** denir. Daha fazla bilgi için [tıklayınız](https://medium.datadriveninvestor.com/how-does-memory-allocation-work-in-python-and-other-languages-d2d8a9398543#:~:text=Each%20string%20in%20python%20needs,and%20needs%20to%20be%20reallocated.&text=Instead%20of%20“%2B”%20for%20string%20concatenation%2C%20USE%20%27%27.).
Buradaki olayı açıklamadan önce **id** ile **bellek adresi** kavramlarını açıklayalım.

**Bellek adresi** kavramını anlamak için **pointer** kavramını anlamak gerekiyor. **Pointer** kavramı, **C** dil ailesini alakadar eden bir kavram. Kısaca bellek adresi, bir variable veya objenin bellekte depolandığı alanın adresidir.

**ID** kavramı, bellek adresinden farklı bir kavramdır. Bellek adresi fiziksel bir belleği işaret ettiği için eşsizdir. Ama id eşsiz değildir. Farklı objeler aynı id'ye sahip olabilirler. Örneğin iki liste objesini birbirine `liste1 = liste2` şeklinde eşitlerseniz, `print(id(liste1))` ve `print(id(liste2))` şeklinde sorguladığınızda, ID'lerinin aynı olduğunu görürsünüz. Çünkü Python'da, aynı value için farklı id'ler **oluşturulmaz.** Aynı value'yi barındıran objeler aynı id'de atanır. Örnek:
```py
b1 = 1000
b2 = 1000
  
print(id(b1))   # Output: 2254419109904
print(id(b2))   # Output: 2254419109904
print(id(1000)) # Output: 2254419109904
```
`liste1` ve `liste2` artık aynı value'ya sahip oldukları için ID'leri aynıdır. Bu yüzden id'yi, python'un bir obje veya value'yu işaret etmek için oluşturduğu geçici kimlik gibi düşünebilirsiniz. Program sonlandığında bu id'ler silinir ve tekrar çalıştırıldığında, her obje'ye yeni id'ler atanır.

`a` ve `b` son durumda `Python`'a eşit olmasına rağmen farklı id'lere sahiptirler. Bunun nedeni basitçe, `a` variable'ı `1747376761776` id'sinde `Python` olarak saklanırken, `b` variable'ı `1747376833520` id'sinde  `Pytho` olarak saklanır ve yapılan ekleme işleminin ardından `1747377137584`  id'sinde `Python` olarak saklanır. Sonuç olarak value'lar aynı olsa bile en başta farklı value'lara sahip iki variable söz konusu olduğu için bellek adresleri farklıdır. Bunu şöyle kanıtlayabilirim:
```py
a="Python"
print(id(a))         # Output: 2578477444016
b="Python"
print(id(b))         # Output: 2578477444016
  
print(a,b, sep=", ") # Output: Python, Python
print(a is b) 		 # Output: True
```
Görüldüğü gibi `a` ve `b` variable'ları en başta aynı value'ya sahip oldukları için bellek adresleri aynıdır. Bu farklılık büyük alan kaplayan her value'de görülür. Yani Python, küçük değerli önbellekte saklarken, büyük değerler için her defasında yeni bir depolama işlemi yapar. Bu nedenle:
```py
a=10
b=9
b+=1
  
print(a,b, sep=", ") # Output: 10, 10
print(a is b) # Output: True
print(id(a)) # Output: 1491813100112
print(id(b)) # Output: 1491813100112
```
Yukarıdaki gibi küçük value'lerle işlem yaparken son durumda `a` ve `b`'nin id'leri aynı olur ama,
```py
a=36893488147419103232
print("Önceki a: ", id(a)) # Output: Önceki a: 2152492817552
b=36893488147419103231
print("Önceki b: ", id(b)) # Output: Önceki b: 2152492905648
b+=1
print("Sonraki b: ", id(b)) # Output: Sonraki b: 2152492908432
  
print(a,b, sep=", ") # Output: Python, Python
print(a is b) # Output: False
print("Önceki a: ", id(a)) # Output: Önceki a: 2152492817552
print("Sonraki b: ", id(b)) # Output: Sonraki b: 2152492908432
```
Yukarıdaki gibi Büyük value'lerle işlem yaparken son durumda `a` ve `b`'nin id'leri farklı olur.

**Not:** `is` operator'ı, iki operand'ın aynı obje olup olmadığını kontrol eder. `==` operator'ı, iki operand'ın value'larının aynı olup olmadığını kontrol eder. Örnek:
```py
a = "Python"
b = "ython"
b = "P" + b

print(a is b) # Output: False
print(a == b) # Output: True
```

# Membership (`in`) operators
Sağdaki operand, soldaki operandı içeriyorsa (Yani soldaki operand, sağdaki operand'ın içinde varsa) `True`, içermiyorsa `False` döndürür. `not in` kullanarak bunun tam tersi durumları sorgulayabilirsiniz. Örnek:
```py
isim="Python"
harf="P"

print(harf in isim) # Output: True
print(harf not in isim) # Output: False
```

## Assignment expressions (`:=`)
Bir değişkene değer atama işlemini bir koşul durumunun içinde yapmamıza olanak sağlayarak fazladan bir satır kod yazmaktan bizi kurtarır.

**`:=` kullanmadan:**
```py
giriş = len(input("Adın ne? "))
  
if giriş < 4:
	print("Adın kısaymış.")
elif giriş < 6:
	print("Adın biraz uzunmuş.")
else:
	print("Çok uzun bir adın var.")
```
**`:=` kullanarak:**
```py
if ( giriş := len(input("Adın ne? ")) ) < 4:
	print("Adın kısaymış.")
elif giriş < 6:
	print("Adın biraz uzunmuş.")
else:
	print("Çok uzun bir adın var.")
```
**Not:**  `giriş := len(input("Adın ne? "))` kodunu parantez içinde (Yani `(giriş := len(input("Adın ne? ")))` şeklinde) yazmazsan, hata ile karşılaşabilirsin ya da `if` yanlış çalışır ve istenilen sonucu vermez. Bu yüzden bu operatörü kullanırken kodu parantez içine yazmalısın.

## Operatörleri Beraber Kullanmak
```py
print( not( ((1 == 1)  and  (2 == 2)) or ((3 == 3) and (4 == 4)) ) )
# Output: False
```
## Boolean Type'ın Diğer Type'larla ilişkisi
Data type'ların duruma göre boolean değerleri `True` ya da `False` olabilir. Örnek:
```py
a1 = ""
a2 = 0
a3 = 0.0
a4 = 0 + 0j
a5 = False
a6 = None

b1 = " " # Boşluk karakteri
b2 = 1
b3 = 1.1
b4 = 1 + 1j
b5 = True

print(bool(a1), bool(a2), bool(a3), bool(a4), bool(a5), bool(a6), sep=", ")
# Output: False, False, False, False, False, False

print(bool(b1), bool(b2), bool(b3), bool(b4), bool(b5), sep=", ") # Output: True, True, True, True, True
```
**Not: ** `b1 = " "` kodundaki boşluk karakteri de bir varlığı ifade eder. İlla bir şeyler yazmak zorunda değilsiniz.

**Not: ** `a1 = ""` kodundaki `False` değerini, kullanıcı register veya login olurken, kullanıcının doldurması gereken yerleri boş bırakmaması için yapılmış bir kontrol mekanizmasında kullanılabilir. Örnek:
```py
kullanıcı = input("Kullanıcı adınız: ")
  
if bool(kullanıcı) == True:
	print("Kullanıcı adınızı:", kullanıcı, "olarak seçtiniz.")
else:
	print("Kullanıcı adı alanı boş bırakılamaz!")
```
**Output:**
```
Kullanıcı adınız: 
Kullanıcı adı alanı boş bırakılamaz!
```
```
Kullanıcı adınız: Eyüp
Kullanıcı adınızı Eyüp olarak seçtiniz.
```
**Not:** `None` değeri, boş value anlamına gelir. Yani bir variable'ı `None` değerine eşitlerseniz, python bunu "Bu variable herhangi bir data type'ı içermiyor, boş bir value." olarak yorumlar ama yine de bellekte o variable için **16 byte** boyutunda yer açar. Çünkü sonuç olarak bir variable bildirmiş (declaration) oluyorsunuz ve python bu variable'ı daha sonra kullanma ihtimaliniz olduğu için bellekte 16 byte yer açar. `None`, genellikle bir variable'ın data type'ını daha sonra belirlemek istediğinizde kullanılır.

# Operatör Önceliği
Bir operatörün önceliğini arttırmak için o operatörün bulunduğu işlemi parantez `()` içine alabilirsiniz. Örneğin `2 + 2 * 2` işlemindeki `+` operatörünün önceliğini arttırmak için bu işlemi `(2 + 2) * 2` şeklinde yazabilirsiniz. Aşağıdaki operatörler, en öncelikliden son öncelikliye doğru olmak üzere yukarıdan aşağıya sıralanmıştır.
| Operator | Description |
|----------|-------------|
| `()` | Parentheses |
| `**` | Exponent |
| `+x`, `-x`, `~x` | Unary plus, Unary minus, Bitwise NOT |
| `*`, `/`, `//`, `%` | Multiplication, Division, Floor division, Modulus |
| `+`, `-` | Addition, Subtraction |
| `<<`, `>>` | Bitwise shift operators |
| `&` | Bitwise AND |
| `^` | Bitwise XOR |
| `|` | Bitwise OR |
|  `==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in` | Comparisons, Identity, Membership operators |
| `not` | Logical NOT |
| `and` | Logical AND |
| `or` | Logical OR |

Daha ayrıntılı bilgi için [tıklayınız](https://docs.python.org/3/reference/expressions.html#operator-precedence).

**Not:** Yukarıdaki linkte ilk sırada olan Binding'in ne olduğunu öğrenmek için [tıklayınız](https://mathieularose.com/python-variables).