from random import randint
import sys

# creating variables for the path to text files and random email domains
path_to_supporting_files = "PATH TO TXT FILE WITH NAMES: First Last"
email_domains = [
        "@aol.com", "@gmail.com", "@yahoo.com",
        "@outlook.com", "@hotmail.com", "@icloud.com",
        "@yandex.ru", "@mail.me", "@protonmail.com" 
        ]

user_input = input("Enter how many user names you want to generate: ")
random_num = int(user_input)

# opening file and concating a name, a random number and email domains.
with open(path_to_supporting_files, 'r') as names_file:
    names_file = str(names_file.read())
    usernames = []

    for name in names_file.split():
        usernames.append(name)

    for i in range(0, random_num):
        print(usernames[randint(0,len(usernames)- 1)].lower() + str(randint(0,999)) + email_domains[randint(0, len(email_domains) - 1)])
