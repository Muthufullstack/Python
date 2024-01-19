#Simple authentication using python and mysql
import mysql.connector
from getpass import getpass
import hashlib
from tabulate import tabulate
connection = mysql.connector.connect(host="localhost",user="root",password="arun@2006sql",database="python_dbs")
def Signup(): 
    Username=input("Enter your username : ")
    Email=input("Enter your email : ")
    res=connection.cursor()
    sqlc = "SELECT * FROM user WHERE Username = %s Or Email = %s"
    use = (Username,Email)
    res.execute(sqlc,use)
    check = res.fetchone()
    if check:
        print("You already have an account in this website")
    else:
        Password = getpass("Enter your Password ")
        hashed_password = hashlib.sha256(Password.encode()).hexdigest()
        sql="INSERT INTO user (Username,Email,Password) VALUE (%s,%s,%s)"
        user=(Username,Email,hashed_password)
        res.execute(sql,user)
        connection.commit()
        print("Account created successfully")
def Log_in():
    Username=input("Enter your username : ")
    Password=getpass("Enter your Password :")
    res=connection.cursor()
    sql = "SELECT * FROM user WHERE Username = %s AND Password = %s"
    hashed_password = hashlib.sha256(Password.encode()).hexdigest()
    params = (Username,hashed_password)
    res.execute(sql, params)
    check=res.fetchone()
    if check:
        print("Successfully logged in ")
    else:
        print("You don't have any account in this website ")
def change_password():
    username = input("Enter your username: ")
    old_password = getpass("Enter your old password: ")
    res = connection.cursor()
    sql = "SELECT * FROM user WHERE Username = %s AND Password = %s"
    hashed_password = hashlib.sha256(old_password.encode()).hexdigest()
    user = (username,hashed_password)
    res.execute(sql, user)
    check = res.fetchone()
    if check:
        new_password = getpass("Enter your new password: ")
        sql = "UPDATE user SET Password = %s WHERE Username = %s"
        hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
        user = (hashed_password, username)
        res.execute(sql, user)
        connection.commit()
        print("Password changed successfully!")
    else:
        print("Enter your old password correctly.")
        chance = 0
        con =True
        while con and chance <= 3:
            old_password = input("Enter your old password: ")
            res = connection.cursor()
            sql = "SELECT * FROM user WHERE Username = %s AND Password = %s"
            hashed_password = hashlib.sha256(old_password.encode()).hexdigest()
            user = (username, hashed_password)
            res.execute(sql, user)
            check = res.fetchone()
            if check:
               new_password = input("Enter your new password: ")
               sql = "UPDATE user SET Password = %s WHERE Username = %s"
               hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
               user = (hashed_password, username)
               res.execute(sql, user)
               connection.commit()
               print("Password changed successfully!")
               break
            elif chance == 2:
               print("You lost your all chances.Try again after 2 minutes")
               break
            else:
               print("Enter your old password correctly.")
               chance+=1
def Delete_Account():
    Username=input("Enter your username : ")
    Password=getpass("Enter your Password ")
    res=connection.cursor()
    sql = "SELECT * FROM user WHERE Username = %s AND Password = %s"
    hashed_password = hashlib.sha256(Password.encode()).hexdigest()
    user = (Username, hashed_password)
    res.execute(sql, user)
    check = res.fetchone()
    if check:
       sql ="delete from user where Username = %s And Password = %s"
       user = (Username,hashed_password)
       res.execute(sql,user)
       connection.commit()
       print("Account deleted successfully ")
    else:
        print("You don't have any account in this website")
#Main Program
o=[(1," Create Account "),(2,"Login"),(3,"Change Password"),(4,"Delete Account")]
print(tabulate(o,headers=["Option","Functions"]))
opt=int(input("Enter your option:"))
if(opt == 1):
    Signup()
elif(opt == 2):
    Log_in()
elif(opt == 3):
    change_password()
elif(opt == 4):
    Delete_Account()
connection.close()