import sqlite3

banco = sqlite3.connect('teste.db')
cursor = banco.cursor()

#cursor.execute("CREATE TABLE employees(id integer PRYMARI KEY,name text, salary real, department text, position text, hireDate text)")
cont = 0
while cont == 10:
    cursor.execute("INSERT INTO employees (id ,name,salary, department,position,hireDate)VALUES(1,'John', 700, 'HR', 'Manager', '2022-02-4')")
    cont += 1
banco.commit()

