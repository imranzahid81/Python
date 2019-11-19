import sqlite3
from employeeSqlite import Employee

conn = sqlite3.connect('sqliteDemoEmp.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employees(
#             first text,
#             last text,
#             pay integer
#             )""")

# c.execute("INSERT INTO employees VALUES ('Urooj', 'Zahid', 90000)")

# conn.commit()

c.execute("SELECT * FROM employees WHERE last='Zahid'")

print(c.fetchall())

conn.commit()

conn.close()