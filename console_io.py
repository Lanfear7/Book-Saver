import bookstore, re

def check_data(file_name, new_title, new_author, new_year, new_isbn, new_description):
    file = file_name[2:-3]
    regex_title = "/^[a-zA-Z]+[0-9]* /"
    regex_author ="/^[a-zA-Z]+ /"
    if len(new_year) < 4 or int(new_year) < 1900:
        print('ERROR')
        error = True
        while error:
            print ('Input a valid year after 1900')
            y = input()
            if len(y) >= 4 and int(y) > 1900:
                error = False 


    regex_isbn = "/^[0-9]{4}$/"
    regex_description = "/^[a-zA-Z]{0,256}/"
    print('working')