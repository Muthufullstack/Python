import mysql.connector
connection = mysql.connector.connect(host="localhost",user="root",password="arun@2006sql",database="python_db")
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
        Password = int(input("Enter your Password "))
        sql="INSERT INTO user (Username,Email,Password) VALUE (%s,%s,%s)"
        user=(Username,Email,Password)
        res.execute(sql,user)
        connection.commit()
        print("Account created successfully")
def Log_in():
    Username=input("Enter your username : ")
    Password=int(input("Enter your Password :"))
    res=connection.cursor()
    sql = "SELECT * FROM user WHERE Username = %s AND Password = %s"
    params = (Username,Password)
    res.execute(sql, params)
    check=res.fetchone()
    if check:
        print("Successfully logged in ")
    else:
        print("You don't have any account in this website ")
def change_password():
    username = input("Enter your username: ")
    old_password = input("Enter your old password: ")
    res = connection.cursor()
    sql = "SELECT * FROM user WHERE Username = %s AND Password = %s"
    user = (username, old_password)
    res.execute(sql, user)
    check = res.fetchone()
    if check:
        new_password = input("Enter your new password: ")
        sql = "UPDATE user SET Password = %s WHERE Username = %s"
        user = (new_password, username)
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
            user = (username, old_password)
            res.execute(sql, user)
            check = res.fetchone()
            if check:
               new_password = input("Enter your new password: ")
               sql = "UPDATE user SET Password = %s WHERE Username = %s"
               user = (new_password, username)
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
    Password=input("Enter your Password ")
    res=connection.cursor()
    sql = "SELECT * FROM user WHERE Username = %s AND Password = %s"
    user = (Username, Password)
    res.execute(sql, user)
    check = res.fetchone()
    if check:
       sql ="delete from user where Username = %s And Password = %s"
       user = (Username,Password)
       res.execute(sql,user)
       connection.commit()
       print("Account deleted successfully ")
    else:
        print("You don't have any account in this website")
#Main Program
print("1.Create Account ")
print("2.Login")
print("3.Change Password ")
print("4.Delete Account ")
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