import secrets
import string

def generate_random_password(length=16, num_uppercase_letters=2, num_numbers=2, num_special_chars=2):
    """
    Generate a random password with specified numbers of uppercase letters, digits, and special characters.

    Parameters:
    total_length (int): Total length of the password.
    num_uppercase (int): Number of uppercase letters in the password.
    num_digits (int): Number of digits in the password.
    num_special_chars (int): Number of special characters in the password.

    Returns:
    str: A randomly generated password.

    Raises:
    ValueError: If the total length is not sufficient to include the specified numbers of each character type.
    """
    #Generate a specified num of random chars
    uppercase_letters = [secrets.choice(string.ascii_uppercase) for _ in range(num_uppercase_letters)]
    numbers = [secrets.choice(string.digits) for _ in range(num_numbers)]
    special_chars = [secrets.choice(string.punctuation) for _ in range(num_special_chars)]
    all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    #Fill remaining length with random chars
    remaining_chars = length - (num_uppercase_letters + num_numbers + num_special_chars)
    all_ran_chars = [secrets.choice(all_chars) for _ in range(remaining_chars)]
    ran_gen_password = uppercase_letters + numbers + special_chars + all_ran_chars
    #Shuffle list of chars
    secrets.SystemRandom().shuffle(ran_gen_password)
    #Join list of chars to a string
    ran_gen_password = ''.join(ran_gen_password)
    return ran_gen_password

#print(generate_random_password(12, 1, 2, 1))
