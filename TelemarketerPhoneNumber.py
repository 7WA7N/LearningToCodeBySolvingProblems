phonenumber = (input('Enter Phone # '))
if len(phonenumber) == 4:
    if phonenumber[0] and phonenumber[3] == '8' or '9':
        if phonenumber[1] == phonenumber[2]:
            print("This is a Telemarketer's Phone Number")
        else:
            print("This is not a Telemarketer's Phone Number") 
elif len(phonenumber) > 4: 
    print('Error101: Enter 4-digit Phone')

