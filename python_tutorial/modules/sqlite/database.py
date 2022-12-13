import sqlite3

conn = sqlite3.connect('my_database.sqlite')
c = conn.cursor()

# c.execute("""DELETE FROM sqlite_sequence""")
# c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")

# for table_name in c:
#     print(table_name)

c.execute("""CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_full_name TEXT,
    customer_social_status TEXT,
    customer_order_history TEXT,
    customer_spending_potential TEXT,
    customer_table_history TEXT
)""")

c.execute("""CREATE TABLE Tables (
    table_id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_customers_contained TEXT,
    table_max_capacity INTEGER,
    table_sitting_datetime TEXT,
    table_leaving_datetime TEXT,
    table_total_spending INTEGER,
    table_customer_surveys_result_point INTEGER
)""")

c.execute("""CREATE TABLE Products (
    product_name TEXT,
    pruduct_purchase_price INTEGER,
    product_selling_price INTEGER,
    product_sales_amount INTEGER,
    product_profitability_rate INTEGER
)""")

c.execute("""CREATE TABLE Orders (
    employee_id_selling_product INTEGER,
    product_order_datetime TEXT,
    product_order_table_id INTEGER,
    product_arrive_table_datetime TEXT,
    product_spesiific_order_code TEXT
)""")

c.execute("""CREATE TABLE Employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_full_name TEXT,
    employee_position TEXT,
    employee_salary INTEGER
)""")

c.execute("""CREATE TABLE Customer_Satisfaction_Survey (
    survey_id INTEGER PRIMARY KEY AUTOINCREMENT,
    answered_survey_customer_id INTEGER,
    question_1_score INTEGER,
    question_2_score INTEGER,
    question_3_score INTEGER
)""")

conn.commit()
conn.close()