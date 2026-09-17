import random

password_length = int(input("Enter password length:"))
symbols = str(input("Include symbols? (y/n):"))
numbers = str(input("include numbers? (y/n):"))
password = ""

if symbols == "y" and numbers == "n":
    character_pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*"
elif symbols == "n" and numbers == "n":
    character_pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
elif symbols == "n" and numbers == "y":  
    character_pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
else:
    character_pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*"    

for i in range(password_length):
    password += random.choice(character_pool)
print(password)    

