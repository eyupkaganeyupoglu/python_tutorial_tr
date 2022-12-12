# İçindekiler

- [İçindekiler](#i̇çindekiler)

<h1 id="1">JSON Nedir?</h1>

Structured data'ları temsil etmek için kullanılan bir veri formatıdır. JSON, **J**ava**S**cript **O**bject **N**otation olarak da bilinir. JSON dosyaları, `.json` uzantılıdır. Python, JSON dosyalarıyla çalışmak için `json` modülüne sahiptir. JSON, JSON stringleriyle çalışır. JSON stringleri, Python dict yapısının tırnak içinde yazılarak yazılarak oluşturulan `str` type objelerdir. JSON stringleri üzerinde işlem yapabilmek için JSON to dict/dict to JSON string işlemleri yapmamız gerekiyor.

<h1 id="2">JSON to Dict</h1>

JSON stringlerini Python dict yapısına çevirmek için `json.loads()` fonksiyonunu kullanırız. Syntax:
```py
import json

json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
```
- `s` parametresi, JSON stringi olmalıdır.
- `cls` parametresi, JSON stringini dict yapısına çevirmek için kullanılacak class'ı temsil eder.
- `object_hook` parametresi, JSON stringini dict yapısına çevirmek için kullanılacak fonksiyonu temsil eder.
- `parse_float` parametresi, JSON stringindeki float değerleri çevirmek için kullanılacak fonksiyonu temsil eder.
- `parse_int` parametresi, JSON stringindeki int değerleri çevirmek için kullanılacak fonksiyonu temsil eder.
- `parse_constant` parametresi, JSON stringindeki sabit değerleri çevirmek için kullanılacak fonksiyonu temsil eder.
- `object_pairs_hook` parametresi, JSON stringini dict yapısına çevirmek için kullanılacak fonksiyonu temsil eder.
```py
import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'
python_dict = json.loads(json_string)
print(python_dict, type(python_dict))
```
**Output:**
```
{'name': 'John', 'age': 30, 'city': 'New York'} <class 'dict'>
```

<h1 id="3">Dict to JSON</h1>

Python dict yapısını JSON stringine çevirmek için `json.dumps()` fonksiyonunu kullanırız. Syntax:
```py
import json

json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
```
- `obj` parametresi, dict yapısı olmalıdır.
- `skipkeys` parametresi, dict yapısındaki key'lerin JSON stringine çevrilip çevrilmediğini belirler.
- `ensure_ascii` parametresi, JSON stringindeki karakterlerin ASCII karakterlerine çevrilip çevrilmediğini belirler.
- `check_circular` parametresi, dict yapısındaki circular referansları kontrol edip edilmeyeceğini belirler.
- `allow_nan` parametresi, JSON stringindeki `NaN` ve `Infinity` değerlerinin çevrilip çevrilmediğini belirler.
- `cls` parametresi, JSON stringini dict yapısına çevirmek için kullanılacak class'ı temsil eder.
- `indent` parametresi, JSON stringindeki boşluk sayısını belirler.
- `separators` parametresi, JSON stringindeki key-value ve eleman arasındaki ayırıcıyı belirler.
- `default` parametresi, JSON stringini dict yapısına çevirmek için kullanılacak fonksiyonu temsil eder.
- `sort_keys` parametresi, JSON stringindeki key'lerin sıralanıp sıralanmayacağını belirler.
```py
import json

python_dict = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(python_dict)
print(json_string, type(json_string))
```
**Output:**
```json
{"name": "John", "age": 30, "city": "New York"} <class 'str'>
```

<h1 id="4">Python read JSON file</h1>

JSON dosyalarını okumak için `json.load()` fonksiyonunu kullanırız. Syntax:
```py
import json

json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
```
- `fp` parametresi, JSON dosyasının bulunduğu dosya objesidir.
- `cls` parametresi, JSON stringini dict yapısına çevirmek için kullanılacak class'ı temsil eder.
- `object_hook` parametresi, JSON stringini dict yapısına çevirmek için kullanılacak fonksiyonu temsil eder.
- `parse_float` parametresi, JSON stringindeki float değerleri çevirmek için kullanılacak fonksiyonu temsil eder.
- `parse_int` parametresi, JSON stringindeki int değerleri çevirmek için kullanılacak fonksiyonu temsil eder.
- `parse_constant` parametresi, JSON stringindeki sabit değerleri çevirmek için kullanılacak fonksiyonu temsil eder.
- `object_pairs_hook` parametresi, JSON stringini dict yapısına çevirmek için kullanılacak fonksiyonu temsil eder.
```py
import json

with open("data.json", "r") as f:
    python_dict = json.load(f)
    print(python_dict, type(python_dict))
```
**Output:**
```
{'name': 'John', 'age': 30, 'city': 'New York'} <class 'dict'>
```

<h1 id="5">Python write JSON file</h1>

Python dict yapısını JSON dosyasına yazmak için `json.dump()` fonksiyonunu kullanırız. Syntax:
```py
import json

json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
```
- `obj` parametresi, dict yapısı olmalıdır.
- `fp` parametresi, JSON dosyasının bulunduğu dosya objesidir.
- `skipkeys` parametresi, dict yapısındaki key'lerin JSON stringine çevrilip çevrilmediğini belirler.
- `ensure_ascii` parametresi, JSON stringindeki karakterlerin ASCII karakterlerine çevrilip çevrilmediğini belirler.
- `check_circular` parametresi, dict yapısındaki circular referansları kontrol edip edilmeyeceğini belirler.
- `allow_nan` parametresi, JSON stringindeki `NaN` ve `Infinity` değerlerinin çevrilip çevrilmediğini belirler.
- `cls` parametresi, JSON stringini dict yapısına çevirmek için kullanılacak class'ı temsil eder.
- `indent` parametresi, JSON stringindeki boşluk sayısını belirler.
- `separators` parametresi, JSON stringindeki key-value ve eleman arasındaki ayırıcıyı belirler.
- `default` parametresi, JSON stringini dict yapısına çevirmek için kullanılacak fonksiyonu temsil eder.
- `sort_keys` parametresi, JSON stringindeki key'lerin sıralanıp sıralanmayacağını belirler.
```py
import json

python_dict = {"name": "John", "age": 30, "city": "New York"}
with open("data.json", "w") as f:
    json.dump(python_dict, f)
```