import random


def password_generator():
    upper_letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lower_letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    symbols = ["!", "#", "$", "&", "/", "(", ")", "-", "=", "?", "¡", "@"]
    numbers = ["1", "2", "3", "4,", "5", "6", "7", "8", "9", "0"]

    character = upper_letter + lower_letter + symbols + numbers

    password = []

    for i in range(15):
        character_random = random.choice(character)
        password.append(character_random)

    password = "".join(password)
    return password

def run():
    password = password_generator()
    print("Your new password is: " + password)


if __name__ == "__main__":
    run()