#1: SET UP CONNECTON THRU SQLITE
import sqlite3
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

#CLOSE CONNECTION
conn.close()