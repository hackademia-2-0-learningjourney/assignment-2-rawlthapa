# Student-name: Rahul Thapa

import json

# file to store user data
Data_File="info.json"
def load_user_data():
    try:
        with open(Data_File,'r') as f: 
            return json.load(f)

    except FileNotFoundError:
        return{}
    
def save_user_data(user_data):
    with open(Data_File,"w") as f:
        json.dump(user_data,f, indent=4)


def sign_up():
    user_data=load_user_data()

    username=input("Enter Username: ")
    if username in user_data:
        print("Uname already exist, try another one")
        return
    
    password=input("Enter password: ")
    mob_number=input("Enter ur mobile number: ")

    user_data[username]={
        "password": password,
        "mobile_number": mob_number
    }

    save_user_data(user_data)
    print("Sign up Successful")

def sign_in():
    user_data=load_user_data()
    username=input("Enter username: ")
    password=input("Enter password: ")

    if username in user_data and user_data[username]['password'] == password:
        print(f"Welcome to the device, {username}")
        print(f"Phone number is {user_data[username]['mobile_number']}")  
    else:
        print("Incorrect credentials")


def main():
    while True:
        print("\nSign up-1")
        print("Sign-in-2")
        print("Exit-3")

        ch=input("Enter your choice: ")
        if ch=="1":
            sign_up()
        elif ch=="2":
            sign_in()
        elif ch=="3":
            print("Exiting program") 
            break
        else:
            print("Invalid Option, try again")

if __name__=="__main__":
    main()

    


