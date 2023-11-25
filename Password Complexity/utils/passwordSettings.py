from password_strength import PasswordPolicy
import json

def getUsernameFromUser():
    '''Returns user input as username. '''
    while True:
        try:
            username = input("Enter username: ")
            return username
        except:
            print("Not a valid username or password.")

def getPasswordFromUser():
    '''Returns user input as password '''
    while True:
        try:
            password = input("Enter password: ")
            return password
        except:
            print("Not a valid username or password.")

def getPassPolicy():
    '''Gets then sets password settings '''
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

def printPolicy(policy_details):
    '''Takes a policy object and prints its details'''
    policy, length, uppercase, numbers, special, nonletters = policy_details  # unpack the tuple

    print("\nYour password policy is set as follows:")
    print(f"Minimum Length: {length}")
    print(f"Minimum Uppercase Letters: {uppercase}")
    print(f"Minimum Numbers: {numbers}")
    print(f"Minimum Special Characters: {special}")
    print(f"Minimum Non-Letter Characters: {nonletters}\n")

def checkPassword(password, policy):
    '''Check to make sure the password meets the policy criteria'''
    pwCheck = policy[0].test(password)
    if pwCheck == []:
        print("Password meets the requirements.")
        return True
    else:
        print("Password doesn't meet the requirements.")
        return False

'''
def writeToJson(userPass, jsonFile):
    with open(jsonFile, 'w') as file:
        json.dump(userPass, file, indent=4)

def readFromJson(jsonFile):
    with open(jsonFile, 'r') as file:
        password = json.load(file)
    return password

def randomGenPassword():
    #Randomly generate password 
    pass

def checkPasswordEntropyBits():
    #Check pw based on entropy bits
    pass

'''