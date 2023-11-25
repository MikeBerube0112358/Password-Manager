from utils import passwordSettings, database 
    
def main():
    policy = passwordSettings.getPassPolicy()
    passwordSettings.printPolicy(policy) 
    while True: 
        menu(policy)

def menu(policy):
    admin_operation = input("To add a user enter a.\n"
                            "To get info on user enter u.\n"
                            "To delete user enter d.\n"
                            "To get all user info enter i.\n"
                            "To quit app enter q.\n\n"
                            "Enter your choice: ")
    if admin_operation == 'a':
        username = passwordSettings.getUsernameFromUser()
        password = passwordSettings.getPasswordFromUser()
        while True:
            if passwordSettings.checkPassword(password, policy) == True:
                break
            else: 
                password = passwordSettings.getPasswordFromUser()
        database.create_username_pwd_table() 
        database.add_user(username, password)
    elif admin_operation == 'u':
        print(database.get_userinfo(int(input("Enter user ID: "))))
    elif admin_operation == 'd':
        #add error handling for this input#######
        database.delete_user(int(input("Enter user ID that you want to delete: ")))
    elif admin_operation == 'i':
        for user in database.get_all_userinfo():
            print(user)
    elif admin_operation == 'q':
        quit()

if __name__ == "__main__":
    main()


    '''
    userInfo = {
        "username": username,
        "password": password
    }
    '''