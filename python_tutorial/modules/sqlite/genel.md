- `import sqlite3` şeklinde import edilir.
- `conn = sqlite3.connect('database_name.db')` şeklinde bir database dosyası yaratılır ve bağlantısı oluşturulur.
- `c = conn.cursor()` şeklinde bir cursor oluşturulur. Cursor ile database üzerinde işlemler yapılır.
- SQLite'da data type'lar, bir column'un tutacağı data'ların veri turunu ifade eder. Data type'lar:
  - INTEGER: Signed integer'ları tutar.
  - REAL: Floating point sayıları tutar.
  - TEXT: String'leri tutar.
  - BLOB: Binary data'ları tutar.
  - NULL: Null değer tutar.
- Create a database connection:
  ```py
  import sqlite3

  # Create a database connection
  conn = sqlite3.connect('customer.db')
  ```
- Create a cursor:
  ```py
  import sqlite3

  # Create a database connection
  conn = sqlite3.connect('customer.db')

  # Create a cursor
  c = conn.cursor()
  ```
- Create a table:
  ```py
  import sqlite3

  # Create a database connection
  conn = sqlite3.connect('customer.db')

  # Create a cursor
  c = conn.cursor()

  # Create a table
  c.execute("""CREATE TABLE table_name (
      column_name datatype,
      column_name datatype,
      column_name datatype,
      ...
  )""")
  ```
- Commit our command:
  ```py
  import sqlite3

  # Create a database connection
  conn = sqlite3.connect('customer.db')

  # Create a cursor
  c = conn.cursor()

  # Create a table
  c.execute("""CREATE TABLE table_name (
      column_name datatype,
      column_name datatype,
      column_name datatype,
      ...
  )""")

  # Commit our command
  conn.commit()
  ```
- Close our connection:
  ```py
  import sqlite3

  # Create a database connection
  conn = sqlite3.connect('customer.db')

  # Create a cursor
  c = conn.cursor()

  # Create a table
  c.execute("""CREATE TABLE table_name (
      column_name datatype,
      column_name datatype,
      column_name datatype,
      ...
  )""")

  # Commit our command
  conn.commit()

  # Close our connection
  conn.close()
  ```
- Insert One Record Into The Table:
  ```py
  import sqlite3

  # Create a database connection
  conn = sqlite3.connect('customer.db')

  # Create a cursor
  c = conn.cursor()

  # Insert One Record Into The Table
  c.execute("""INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com')""")
  ```
- Insert Many Records Into The Table:
  ```py
  import sqlite3

  # Create a database connection
  conn = sqlite3.connect('customer.db')

  # Create a cursor
  c = conn.cursor()

  # Insert Many Records Into The Table
  many_customers = [
      ('Wes', 'Brown', 'was@codemy.com'),
      ('Steph', 'Kuewa', 'steph@codemy.com'),
      ('Dan', 'Pas', 'dan@codemy.com')
  ]
  c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
  ```
- Query the database:
  ```py
  import sqlite3

  # Create a database connection
  conn = sqlite3.connect('customer.db')

  # Create a cursor
  c = conn.cursor()

  # Query the database
  c.execute("SELECT * FROM customers")
  print(c.fetchone()) # Tablodaki ilk veriyi getirir.
  print(c.fetchmany(3)) # Tablodaki ilk 3 veriyi getirir.
  print(c.fetchall()) # Tablodaki tüm verileri getirir.
  ```
- rowid:
  ```py
  import sqlite3

  # Create a database connection
  conn = sqlite3.connect('customer.db')

  # Create a cursor
  c = conn.cursor()

  # rowid
  c.execute("SELECT rowid, * FROM customers") # rowid, her bir satıra otomatik olarak verilen id'dir. Bir sayıdır 
  print(c.fetchall())
  print(type(c.fetchall()))
  print("Command executed successfully...")
  ```








- `/d/my_folder/education/solfware/python/python_tutorial/main/.md/main/python_tutorial/modules/sqlite` sqlite klasörüne girilir.