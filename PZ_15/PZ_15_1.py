import sqlite3 as sql
from data import data

with sql.connect('expenses.txt') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS chancellery (employee_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                'name TEXT NOT NULL,'
                'department TEXT NOT NULL,'
                'expense_type TEXT NOT NULL,'
                'cost INTEGER NOT NULL'
                ')')
    
    cur.executemany('INSERT INTO chancellery VALUES (?, ?, ?, ?, ?)', data)
    cur.execute('SELECT * FROM chancellery')
    print('Изначальная база данных:')
    for i in cur:
        print(i)

    cur.execute('SELECT * FROM chancellery WHERE cost > 400')
    print('Поиск записей, где сумма больше 400:')
    for i in cur:
        print(i)
    cur.execute('SELECT * FROM chancellery WHERE department = "Бухгалтерия"')
    print('Поиск записей, где отдел - бухгалтерия:')
    for i in cur:
        print(i)
    cur.execute('SELECT * FROM chancellery WHERE cost < 400')
    print('Поиск записей, где сумма меньше 400:')
    for i in cur:
        print(i)

    cur.execute('DELETE FROM chancellery WHERE cost > 1000')
    cur.execute('DELETE FROM chancellery WHERE department = "Маркетинг"')
    cur.execute('DELETE FROM chancellery WHERE name LIKE "В%"')

    cur.execute('UPDATE chancellery SET cost = 800 WHERE expense_type = "Дырокол"')
    cur.execute('UPDATE chancellery SET expense_type = "Папки" WHERE expense_type = "Папки-регистраторы"')
    cur.execute('UPDATE chancellery SET cost = cost + 50 WHERE cost > 500')

    cur.execute('SELECT * FROM chancellery')
    print('Конечная база данных:')
    for i in cur:
        print(i)