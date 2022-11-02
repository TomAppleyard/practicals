email = input("email: ")
while email != '':
    email = email.split('@')
    email_name = email[0].split('.')
    email_name = ' '.join(email_name).title()
    print(f"Is this your name ---> {email_name}\n\t")
    response = input("(Y/N): ").upper()
    if response == 'N':
        input_name = input("What is your name then: ")
    break

#  thomas.appleyard@my.jcu.edu.au
