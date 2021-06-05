password = 'bbbbb'
mystring = 'abcdefghijklmnopqrstuvwxyz0123456789'
my_guess = ''
password_found = False
if my_guess == password:
    password_found = True


# chekin one character passwords
if not password_found:
    for i in mystring:
        my_guess = i
        if my_guess == password:
            password_found = True
            break
    if password_found == True:
        print(my_guess)


# chekin two character passwords
if not password_found:
    for i1 in mystring:
        for i2 in mystring:
            my_guess = i1 + i2
            if my_guess == password:
                password_found = True
                break
        if password_found == True:
            break

# checkin three character passwords
if not password_found:
    for i3 in mystring:
        for i4 in mystring:
            for i5 in mystring:
                my_guess = i3 + i4 + i5
                if my_guess == password:
                    password_found = True
                    break
            if password_found == True:
                break
        if password_found == True:
            break
     



# checkin four character passwords
if not password_found:
    for i1 in mystring:
        for i2 in mystring:
            for i3 in mystring:
                for i4 in mystring:
                    my_guess = i1 + i2 + i3 + i4
                    if my_guess == password:
                        password_found = True
                        break
                if password_found == True:
                    break
            if password_found == True:
                break
        if password_found == True:
            break


# checkin five character passwords
if not password_found:
    for i1 in mystring:
        for i2 in mystring:
            for i3 in mystring:
                for i4 in mystring:
                    for i5 in mystring:
                        my_guess = i1 + i2 + i3 + i4 + i5
                        if my_guess == password:
                            password_found = True
                            break
                    if password_found == True:
                        break
                if password_found == True:
                    break
            if password_found == True:
                break
        if password_found == True:
            break


if password_found == True:
    print(my_guess)
else:
    print("Couldn't find password!")



