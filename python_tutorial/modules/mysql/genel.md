# SQL Komutları

## DLL (Data Definition Language (Veri Tanımlama Dili))

### CREATE

Database veya table oluşturmak için kullanılır.

### ALTER

Database veya table üzerinde değişiklik yapmak için kullanılır.

### DROP

Database veya table silmek için kullanılır.

### TRUNCATE

Database veya table içeriğini silmek için kullanılır.

### RENAME

Database veya table adını değiştirmek için kullanılır.

## DML Data Manipulation Language (Veri İşleme Dili)

### SELECT

Database'den veri seçmek için kullanılır.

### INSERT

Database'e veri eklemek için kullanılır.

### UPDATE

Database'deki verileri güncellemek için kullanılır.

### DELETE

Database'den veri silmek için kullanılır.

## UNIQUE

Veri tabanında aynı değeri birden fazla kez kullanmamak için kullanılır. Bir tabloda birden fazla UNIQUE olabilir. Bir UNIQUE sütununda NULL değerleri olabilir. Bir UNIQUE sütununda herhangi bir sütun değeri birden fazla kez tekrar edilemez. Bir UNIQUE sütununda herhangi bir sütun değeri boş olabilir. Bir UNIQUE sütununda herhangi bir sütun değeri değiştirilebilir veya silinebilir.

## PRIMARY KEY

Veri tabanında bir tablonun anahtarını belirtmek için kullanılır. Anahtar, tablodaki her satırın benzersiz bir değere sahip olmasını sağlar. Bir tabloda sadece bir PRIMARY KEY olabilir. Bir PRIMARY KEY sütununda NULL değerleri olamaz. Bir PRIMARY KEY sütununda herhangi bir sütun değeri birden fazla kez tekrar edilemez. Bir PRIMARY KEY sütununda herhangi bir sütun değeri boş olamaz. Bir PRIMARY KEY sütununda herhangi bir sütun değeri değiştirilemez veya silinemez.

## FOREIGN KEY

Bir tablodaki bir sütunun başka bir tablodaki bir sütunla ilişkilendirilmesini sağlar.

## INDEX

Veri tabanında bir tablonun sütunlarını hızlı bir şekilde aramak için kullanılır. `INDEX`'i bir kitabın içindekiler kısmı olarak düşünebilirsiniz. Database'e yapılan her ekleme, güncelleme ve silme işleminden sonra index yeniden inşa edileceğinden fazla kullanılmayan sütunlar için index oluşturmak veya gereğinden fazla index oluşturmak performans düşürür.

## JOIN

Birden fazla tablodaki verileri birleştirmek için kullanılır. JOIN'lerin 4 türü vardır:
- `INNER JOIN`: İki tablodaki ortak değerleri birleştirir.
    ```sql
    SELECT * FROM table_A INNER JOIN table_B ON table_A.column_name = table_B.column_name;
    ```
- `LEFT JOIN`: Sol tablodaki tüm değerleri birleştirir.
    ```sql
    SELECT * FROM table_A LEFT JOIN table_B ON table_A.column_name = table_B.column_name;
    ```
- `RIGHT JOIN`: Sağ tablodaki tüm değerleri birleştirir.
    ```sql
    SELECT * FROM table_A RIGHT JOIN table_B ON table_A.column_name = table_B.column_name;
    ```
- `FULL JOIN`: İki tablodaki tüm değerleri birleştirir.
    ```sql
    SELECT * FROM table_A FULL JOIN table_B ON table_A.column_name = table_B.column_name;
    ```

`WHERE` ile `JOIN` beraber kullanılarak belli bir koşula göre veriler birleştirilebilir. Örnek:
```sql
SELECT * FROM kategoriler, urunler WHERE urunler.kat_id = kategoriler.kat_id;
```


## DCL Data Control Language (Veri Kontrol Dili)

### GRANT

Kullanıcıya yetki vermek için kullanılır.

### REVOKE

Kullanıcıdan yetki almak için kullanılır.

# SQL İşlemleri

## Database Oluşturma
```sql
CREATE DATABASE database_name;
```

## Tablo Oluşturma
```sql
CREATE TABLE table_name (
    column_name1 data_type Kısaltma,
    column_name2 data_type Kısaltma,
    column_name3 data_type Kısaltma,
   ....
);
```
`column_name1` sütunun adıdır. `data_type` sütunun veri tipidir. `Kısaltma` sütuna girilecek veri için sınır veya kural belirtmek için kullanılır. Örnek:
```sql
CREATE TABLE kisiler (
    kisi_sira INT,
    kisi_adi VARCHAR(20),
    kisi_soyadi VARCHAR(30),
    kisi_eposta VARCHAR(50)
);
```

## Tablo Kopyalama
```sql
CREATE TABLE new_table_name AS
    SELECT column_name1, column_name2, ...
    FROM existing_table_name
    WHERE ....;
```
```sql
CREATE TABLE kisi_adi_soyadi AS
  SELECT kisi_adi, kisi_soyadi
  FROM kisiler;
```

## Veri tekrarını önleme

Bunu gerçekleştirmek için `UNIQUE` veya `PRIMARY KEY` anahtar kelimesi kullanılır. Örnek:
```sql
CREATE TABLE kisiler (
  kisi_sira INT PRIMARY KEY,
  kisi_adi VARCHAR(20) UNIQUE,
  kisi_soyadi VARCHAR(30),
  kisi_eposta VARCHAR(50) UNIQUE
);
```

## İki tabloyu ilişkilendirme

Foreign key ile iki tabloyu ilişkilendirebiliriz. Örnek:
```sql
CREATE TABLE table_name (
    column_name1 data_type Kısaltma,
    ...
    FOREIGN KEY (column_name) REFERENCES other_table_name(other_column_name)
        ON UPDATE <EYLEM>
        ON DELETE <EYLEM>
);
```
`ON UPDATE` ve `ON DELETE` eylemleri optional'dır. Bu eylemler `other_table_name` içersindeki `other_column_name` sütununda bir değişiklik olduğunda veya silindiğinde `table_name` tablosunda ne yapılacağını belirtir. Eylemler şunlardır:

- `CASCADE`: `other_column_name`'de bir eylem (UPDATE, DELETE) gerçekleştiğinde `column_name`'de de aynı eylem gerçekleşir.
- `NO ACTION`: `other_column_name`'de bir eylem (UPDATE, DELETE) gerçekleştiğinde `column_name`'de bir eylem gerçekleşmez.
- `SET NULL`: `other_column_name`'de bir eylem (UPDATE, DELETE) gerçekleştiğinde `column_name`'deki değer NULL olur.
- `NOT`: `column_name`'de `NOT NULL` kısıtlaması varsa hata verir.
- `SET DEFAULT`: `other_column_name`'de bir eylem (UPDATE, DELETE) gerçekleştiğinde `column_name`'deki değer `DEFAULT` değerine eşitlenir. `column_name`de `DEFAULT` kısıtlaması yoksa hata verir.
- `RESTRICT`: MySQL VTYS içerisinde bulunan bu eylem NO ACTION ile aynı işleve sahiptir.

## Index Oluşturma

```sql
CREATE INDEX index_name
    ON table_name (column_name);
```

## Değişken Tanımlama ve kullanımı

MySQL VTY sisteminde değişken tanımlamak için `SET` veya `SELECT` anahtar kelimesi kullanılır.
```sql
SET @variable_name = value;
SELECT @variable_name = value;
SET @variable_name := value;
SELECT @variable_name := value;
```
Variable'lar küçük-büyük harfe duyarlı değildir.

MySQL, integer, float, string, NULL data type'ları destekler ve bu veriler sadece geçerli kullanıcı ve oturumda kulanılır. Bu variable'ları çeşitli fonksiyonlarla kullanabilirsiniz. Örnek:
```sql
SET @adi:="Yusuf SEFA SEZER";
SELECT LENGTH(@adi);
SELECT @enyuksek:=MAX(urun_fiyat) FROM urunler;
SELECT * FROM urunler WHERE urun_fiyat=@enyuksek;
```
