def get_email(entered_name , entered_family):
    myfilehandler = open('information.txt' , 'r')
    mylines = myfilehandler.readlines()
    print(mylines)
    for line in mylines:
        spllited = line.split(' ')
        if spllited[0] == entered_name and spllited[1] == entered_family:
            return spllited[8]



entered_family = input('enter family:')
entered_name = input('enter name:')

email = get_email(entered_name , entered_family)
if email != 'not found':
    print(email)
else:
    print(f"couldn't Find person {entered_name}{entered_family}")






