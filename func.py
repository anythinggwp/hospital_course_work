import sqlite3
import re
# Создание таблицы с медкартами


def sql_table_creat_medicalcard(db,name):
    con = sqlite3.connect(db)
    cursor_obj = con.cursor()
    cursor_obj.execute('''CREATE TABLE if not exists ''' + name
                       + ''' (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT,
                          surname TEXT,
                          age INTEGER NOT NULL,
                          count INTEGER)''')

    con.commit()
    con.close()
# Создание таблицы c  расписанием в базе


def sql_table_creat_timetable(db, name):
    con = sqlite3.connect(db)
    cursor_obj = con.cursor()
    cursor_obj.execute('''CREATE TABLE if not exists ''' + name
                       + ''' (
                       name TEXT,
                       spec TEXT,
                       '8:00' INTEGER,
                       '9:00' INTEGER,
                       '10:00' INTEGER,
                       '11:00' INTEGER)''')

    con.commit()
    con.close()
# Создание ведомости за месяц


def sql_table_creat_monthly(db,name):
    con = sqlite3.connect(db)
    cursor_obj = con.cursor()
    cursor_obj.execute('''CREATE TABLE if not exists ''' + name
                       + ''' (
                          name TEXT,
                          spec TEXT,
                          '8:00' TEXT,
                          '9:00' INTEGER,
                          '10:00' INTEGER,
                          '11:00' INTEGER)''')

    con.commit()
    con.close()
def statement_of_cab(num):
    con = sqlite3.connect('test.db')
    cursor_obj = con.cursor()
    cursor_obj.execute('''UPDATE medical_card SET count = :Num WHERE id LIKE '1' ''', {'Num': num})
    con.commit()
    con.close()
def test(date):
    con = sqlite3.connect('test.db')
    cursor_obj = con.cursor()
    cursor_obj.execute('''SELECT name, "8:00", "9:00", "10:00", "11:00" FROM time_table''' + date)
    rows = cursor_obj.fetchall()
    cursor_obj.execute('''SELECT id, count FROM medical_card''')
    rows2 = cursor_obj.fetchall()
    id_list = []
    if len(rows) != False:
        for i in range(len(rows2)):
            id_list.append(rows2[i][0])
        for y in sorted(id_list):
            num1 = rows2[y - 1][1]
            for x in range(0,len(rows)):
                for i in range(1,len(rows[0])):
                    print(i)
                    if rows[x][i] == int(y):
                        num1 += 1
                        cursor_obj.execute('''UPDATE medical_card SET count = :Num WHERE id LIKE :Num2 ''', {'Num': num1,'Num2': y})
    con.commit()
    con.close()
def doctor_statement(name):
    con = sqlite3.connect('test.db')
    cursor_obj = con.cursor()
    cursor_obj.execute('''CREATE TABLE IF NOT EXISTS ''' + name
                       + '''(
                       date TEXT,
                       "8:00" INTEGER,
                       "9:00" INTEGER,
                       "10:00" INTEGER,
                       "11:00" INTEGER,
                       sum INTEGER)''')
    con.commit()
    con.close()
def test2(textt):
    s = re.sub("[\W_]+", "", textt)
    text = '"{}"'.format(s)
if __name__ == '__main__':
    #statement_of_cab()
    #test('2000_01_01')
    test2('jopa')
    #doctor_statement('Igor')
