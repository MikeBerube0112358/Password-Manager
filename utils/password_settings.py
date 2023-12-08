from password_strength import PasswordPolicy
from utils.random_pass_gen import generate_random_password

def get_username_from_user() -> str:
    '''Returns user input as username. '''
    while True:
        try:
            username = input("Enter username: ")
            return username
        except:
            print("Not a valid username or password.")

def get_password_from_user(length, uppercase, numbers, special) -> str:
    '''Returns user input as password '''
    pw_option = input(  
                        "Choose a password option:\n\n" 
                        "For a randomly generated 16 character password enter d (recommended!): \n"   
                        "For a manual password enter m: \n"
                        "For a minimum length randomly generated password based on password policy enter p: "
                    )
    if pw_option == 'd':
        return generate_random_password()
    elif pw_option == 'm':
        while True:
            try:
                password = input("Please enter password: ")
                return password
            except:
                print("Not a valid username or password.")
    elif pw_option == 'p':
        password = generate_random_password(length, uppercase, numbers, special)
        return password
    else:
        generate_random_password()

def get_pass_policy():
    """
    Prompts the user to input password policy requirements and creates a password policy object using PasswordPolicy package .
    Returns: A tuple containing the password policy object and min: length, number of uppercase letters, number of numbers, 
    number of special characters, and minimum number of non-letter characters.
    """
    while True:
        try:
            length = int(input("Enter minimum password length: "))  # min length
            uppercase = int(input("Enter minimum number of uppercase letters: "))  # need min. 2 uppercase letters
            numbers = int(input("Enter minimum number of numbers: "))  # need min. 2 digits
            special = int(input("Enter minimum number of special characters: "))  # need min. 2 special characters
            nonletters = int(input("Enter minimum number of non letter characters (digits, specials, anything): "))  # need min. 2 non-letter characters (digits, specials, anything)
                
            policy = PasswordPolicy.from_names(
                length=length,
                uppercase=uppercase,
                numbers=numbers,
                special=special,
                nonletters=nonletters
            )
            return policy, length, uppercase, numbers, special, nonletters
        except ValueError:
            print("Invalid input try again.")

def print_policy(policy_details):
    '''Takes a policy object and prints its details'''
    policy, length, uppercase, numbers, special, nonletters = policy_details  # unpack the tuple

    print("\nYour password policy is set as follows:")
    print(f"Minimum Length: {length}")
    print(f"Minimum Uppercase Letters: {uppercase}")
    print(f"Minimum Numbers: {numbers}")
    print(f"Minimum Special Characters: {special}")
    print(f"Minimum Non-Letter Characters: {nonletters}\n")

def checkPassword(password, policy) -> bool:
    '''Check to make sure the password meets the policy criteria'''
    pwCheck = policy[0].test(password)
    if pwCheck == []:
        print("Password meets the requirements.")
        return True
    else:
        print("Password doesn't meet the requirements.")
        return False
