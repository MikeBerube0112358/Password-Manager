from utils import password_settings, database

def main():
    policy = password_settings.get_pass_policy()
    password_settings.print_policy(policy) 
    while True: 
        menu(policy)

def menu(policy):
    admin_operation = input("To add a user enter a.\n"
                            "To get info on user enter u.\n"
                            "To validate a password enter v.\n"
                            "To delete user enter d.\n"
                            "To get all user info enter i.\n"
                            "To quit app enter q.\n\n"
                            "Enter your choice: ")
    if admin_operation == 'a':
        username = password_settings.getUsernameFromUser()
        #Unpacks 'policy' tuple to be passed into get_password_from_user()
        length, uppercase, numbers, special = policy[1:5]
        password = password_settings.get_password_from_user(length, uppercase, numbers, special)
        while True:
            if password_settings.checkPassword(password, policy) == True:
                break
            else: 
                password = password_settings.get_password_from_user(length, uppercase, numbers, special)
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