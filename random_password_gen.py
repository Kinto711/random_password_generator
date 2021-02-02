import random, string

pass_length = input("What is the desired length of the password: ")
pass_length = int(pass_length)

password_characters = string.ascii_letters + string.digits + string.punctuation

password = []
for x in range(pass_length):
    password.append(random.choice(password_characters))

print(''.join(password))