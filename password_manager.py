from posixpath import split
from cryptography.fernet import Fernet



'''
def write_key():
    key = Fernet.generate_key()
    with open("keypass.key", "wb" ) as key_file:
        key_file.write(key)'''

def load_key():
     file =open("keypass.key", "rb")
     key = file.read()
     file.close()
     return key

pwd = input("what is the master password ? : ")     
key = load_key() + pwd.encode()
fer = Fernet(key)



def view():
     with open('password_manager.txt', 'r') as f :
        for lines in f.readlines():
          data = lines.rstrip()
          user, passw= data.split("|")
        
        print("username : ", user , "password : ",    fer.decrypt(passw.encode()).decode())


def add():
    name = input("username : ")
    password = input("user's pawd : ")

    with open('password_manager.txt', 'a') as f :
       f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


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
