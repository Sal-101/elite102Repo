#IMPORT FUNCS + SQLITE
import sqlite3
import functions as func



#1: SET UP CONNECTON THRU SQLITE
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

#2: CREATE TABLE
cursor.execute('''create table if not exists bank.accounts(name text, password text, email text, balance real)''')


#CLOSE CONNECTION
conn.close()