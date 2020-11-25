import bookstore, re, json

def check_data(file_name, new_title, new_author, new_year, new_isbn, new_description):
    ''' Gets data for a new book and will validate the user data '''
    file = file_name[2:-3]
    if re.search("[a-zA-Z0-9]+[ ]*", new_title) is None:
        raise ValueError("Invalid Title Name")
    if re.search("[a-zA-Z0-9]+[ ]*", new_author) is None:
        raise ValueError("Invalid Author Name")
    
    if len(new_year) < 4 or int(new_year) < 1900:
        print('ERROR')
        error = True
        while error:
            print ('Input a valid year after 1900')
            y = input()
            if len(y) >= 4 and int(y) > 1900:
                error = False 

    if re.search("^[0-9]{4}$", new_isbn) is None:
        raise ValueError("Invalid ISBN Number")
    if re.search("^[a-zA-Z]{0,256}", new_description) is None:
        raise ValueError("Invalid Description") 

    return new_title, new_author, new_year, new_isbn, new_description

