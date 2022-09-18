def password_check(password):
    SpecialSym = ['$', '@', '#', '%','*','&']
    check = True
    score = int(0)
    while score!=30:
        if len(password) < 8:
            print('length should be at least 6')
            check = False
        else:
            score = (score+5)



        if not any(char.isdigit() for char in password):
            print('Password should have at least one digit')
            check = False
        else:
            score =score+10


        if not any(char.isupper() for char in password):
             print('Password should have at least one uppercase letter')
             check = False
        else:
             score = score+5


        if not any(char.islower() for char in password):
             print('Password should have at least one lowercase letter')
             check = False
        else:
             score = score+5


        if not any(char in SpecialSym for char in password):
            print('Password should have at least one of the symbols $@#')
            check = False
        else:
            score = score+5

        if score:
             return print("All your score = ",score)
        if check:
             return check


def main():
    password = input("Enter the password : ")
    x = "Password is valid"
    y = "Invalid Password !"
    password
    if (password_check(password)):
        print("")
        print(x)
    else:
        print("")
        print(y)


main()