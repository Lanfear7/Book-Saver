import bookstore, re

def check_data(file_name, new_title, new_author, new_year, new_isbn, new_description):

    file = file_name[2:-3]
    regex_title = "[a-zA-Z0-9]+[ ]*"
    regex_author ="^[a-zA-Z]+[ ]*"


    if len(new_year) < 4 or int(new_year) < 1900:
        print('ERROR')
        error = True
        while error:
            print ('Input a valid year after 1900')
            y = input()
            if len(y) >= 4 and int(y) > 1900:
                error = False 

    regex_isbn = "^[0-9]{4}$"
    regex_description = "^[a-zA-Z]{0,256}"
    
    print('working')
    regex(regex_title, new_title, 'title')
    regex(regex_author, new_author, 'author')
    regex(regex_isbn, new_isbn, 'isbn')
    regex(regex_description, new_description, 'description')


def regex(regex, value, of):
    print('**** IN REGEX *****')
    if re.search(regex, value):
        print (f'{value} passed')
        return
    else:
        error = True
        while error:
            print(f'Please input a valid valuse for the books {of}')
            new_value = input()
            print(new_value)
            if re.search(regex, new_value):
                print('pass')
                error = False
