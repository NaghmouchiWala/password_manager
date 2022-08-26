from posixpath import split
from cryptography.fernet import Fernet


pwd = input("what is the master password ? : ")

def write_key():
    key = Fernet.generate_key()
    with open("keypass.key", "wb" ) as key_file:
        key_file.write(key)

write_key()        

def view():
     with open('password_manager.txt', 'r') as f :
        for lines in f.readlines():
          data = lines.rstrip()
          user, passw= data.split("|")
        
        print("username : ", user , "pasword : ", passw)


def add():
    name = input("username : ")
    password = input("user's pawd : ")

    with open('password_manager.txt', 'a') as f :
        f.write(name + '|' + password + "\n")


while True:
    mode = input("add or view password ? (add , view) , press q if u want to quit :  ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode!")
        continue
