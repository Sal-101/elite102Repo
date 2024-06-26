import unittest #importing the unittest module for usage at the bottom
import sqlite3
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()



##ADD USER ACC
def add_user():
  user_name = input("Input your prefered name: ")
  user_password = input("Input a strong password: ")
  user_email = input("Input your email: ")
  user_init_balance = input("What will be your initial balance? ")
  
  #add user to database
  cursor.execute(f'''INSERT INTO bank(name, password, email, balance) VALUES('{user_name}', '{user_password}', '{user_email}', {user_init_balance})''')
  #show updates
  cursor.execute('''SELECT * FROM bank''')
  update = cursor.fetchall()
  print(update)
  print("Your account has been added!")


##DELETE USER ACC
def delete_user():
  test_username = input("Enter the username of the account you want to delete: ")
  test_password = input("Input the corresponding password. ")
  
  #go into data base and compare user input to table values. if they match, delete the row!
  if cursor.execute(f'''SELECT * FROM bank WHERE name = '{test_username}' AND password = '{test_password}' '''):
    cursor.execute(f'''DELETE FROM bank WHERE name = '{test_username}' AND password = '{test_password}' ''')
  else:
    print("Account not found. Username and/or password may be incorrect!")

  #show updates
  cursor.execute('''SELECT * FROM bank''')
  update = cursor.fetchall()
  print(update)
  print("Your account has been deleted!")


#MODIFY ACC
def modify_user():
  test_username = input("Enter the username of the account you want to modify: ")
  test_password = input("Input the corresponding password. ")
  
  #go into data base and compare user input to table values. if they match, allow user to modify data
  if cursor.execute(f'''SELECT * FROM bank WHERE name = '{test_username}' AND password = '{test_password}' '''):
    new_name = input("Enter new name. If you don't want to change it, re-enter the old one. ")
    new_password = input("Enter new password. If you don't want to change it, re-enter the old one. ")
    new_email = input("Enter new email. If you don't want to change it, re-enter the old one. ")
    
    #update account accordingly
    cursor.execute(f'''UPDATE bank SET name = '{new_name}', password = '{new_password}', email = '{new_email}' WHERE name = '{test_username}' AND password = '{test_password}' ''')
    print("Account updated! To update balance, check DEPOSIT or WITHDRAWAL!")
  else:
    print("Account not found. Username and/or password may be incorrect!")

  #show updates
  cursor.execute('''SELECT * FROM bank''')
  update = cursor.fetchall()
  print(update)
  print("Your account has been updated!")


##DEPOSIT
def deposit():
  test_username = input("Enter the username of the account you want to deposit to: ")
  test_password = input("Input the corresponding password. ")

  #go into data base and compare user input to table values. if they match, allow user to deposit
  if cursor.execute(f'''SELECT * FROM bank WHERE name = '{test_username}' AND password = '{test_password}' '''):
    deposit_amount = input("How much would you like to deposit? ")
    cursor.execute(f'''UPDATE bank SET balance = balance + {deposit_amount} WHERE name = '{test_username}' AND password = '{test_password}' ''')
    print("Deposit completed! Check your balance!")
  else:
    print("Account not found. Username and/or password may be incorrect!")

  #show updates
  cursor.execute('''SELECT * FROM bank''')
  update = cursor.fetchall()
  print(update)


##WITHDRAW
def withdrawal():  #set up similar to deposit(), except subtract from balance!
  test_username = input("Enter the username of the account you want to withdrawal from: ")
  test_password = input("Input the corresponding password. ")

  #go into data base and compare user input to table values. if they match, allow user to withdrawal
  if cursor.execute(f'''SELECT * FROM bank WHERE name = '{test_username}' AND password = '{test_password}' '''):
    withdrawal_amount = input("How much would you like to withdraw? ")
    cursor.execute(f'''UPDATE bank SET balance = balance - {withdrawal_amount} WHERE name = '{test_username}' AND password = '{test_password}' ''')
    print("Withdrawal completed! Check your balance!")
  else:
    print("Account not found. Username and/or password may be incorrect!")

  #show updates
  cursor.execute('''SELECT * FROM bank''')
  update = cursor.fetchall()
  print(update)
  

##CHECK BALANCE
def check_user_balance():
  test_username = input("Enter the username of the account you want to withdrawal from: ")
  test_password = input("Input the corresponding password. ")

  #go into data base and compare user input to table values. if they match, print balance
  if cursor.execute(f'''SELECT * FROM bank WHERE name = '{test_username}' AND password = '{test_password}' '''):
    print(f"Your balance is {cursor.execute(f'''SELECT balance FROM bank WHERE name = '{test_username}' AND password = '{test_password}' ''')}")
  else:
    print("Account not found. Username and/or password may be incorrect!")







###(an attempt at) TESTS
class Test(unittest.TestCase):
  def test_add_user(self):
    self.assertEqual(add_user(), "Account added!") 
  def test_modify_user(self):
    self.assertTrue(modify_user(), "Account updated!")
  def test_deposit(self):
    self.assertTrue(deposit(), "Deposit completed!")
