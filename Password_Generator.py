import random
choice = str(input("Enter G to generate a password, or L to list/search saved passwords: "))
if choice.upper() == "G":
    site = str(input("Enter the site name for this password: "))
    username = str(input("Enter your username: "))
    password_length = int(input("Enter password length: "))
    symbols = str(input("Include symbols? (y/n): "))
    numbers = str(input("include numbers? (y/n): "))
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

    file = open("passwords.txt", "a")
    file.write(f"Site: {site} | Username: {username} | Password: {password}\n")
    file.close()

elif choice.upper() == "L":
    site_name = input("Enter the site name or enter 'A' to get all the passwords list: ")   
    if site_name.upper() == "A":
        file = open("passwords.txt", "r")
        content = file.read()
        print(content)
        file.close()
    else:
        file = open("passwords.txt", "r") 
        found = False
        for line in file:
            if site_name.lower() in line.lower():
                print(line)
                found = True
        if found == False:
            print("no matching entries found.")
        file.close()




