#IMPORT FUNCS + SQLITE + RUN COMMAND
import sqlite3
import functions as func


#1: SET UP CONNECTON THRU SQLITE
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

#2: CREATE TABLE
cursor.execute('''create table if not exists bank.accounts(name text, password text, email text, balance real)''')

#3: MAIN INTERFACE FUNCS
def main_menu_interface():
  print("WELCOME TO [ THE BANK ]! (yes, that is our name).")
  print()
  print("Our services include the following:")
  print("1) Add An Account")
  print("2) Delete An Account")
  print("3) Modify An Account")
  print("4) Conduct a Deposit")
  print("5) Conduct a Withdrawal")
  print("6) Check Account Balance")
  print()

def user_choice():
  choice = input("What brings you here today? Type the corresponding number! To exit, type 'exit'. ")
  if choice == "1":
    print("---------------------------------------------")
    func.add_user()
  elif choice == "2":
    print("---------------------------------------------")
    func.delete_user()
  elif choice == "3":
    print("---------------------------------------------")
    func.modify_user()
  elif choice == "4":
    print("---------------------------------------------")
    func.deposit()
  elif choice == "5":
    print("---------------------------------------------")
    func.withdrawal
  elif choice == "6":
    print("---------------------------------------------")
    func.check_user_balance()
  elif choice == "Exit" or "exit":
    print("Farewell!")
    conn.close()


#FUNC CALL
def main():
  main_menu_interface()
  user_choice()

main()