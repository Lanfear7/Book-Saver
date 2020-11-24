import os, json

def save_book_list(book_list, book_file):
    """ Save the cars_list as json in the car_file """
    book_file = open(book_file, "w")
    book_json = json.dumps(book_list, indent=4)
    book_file.write(book_json)
    book_file.close()

def add_data(file_name, title, author, year, isbn, description):
    print("*****GOT THE DATA******")
    file = file_name[2:-3]
    pre_json = {
            "file": f"{file}",
            "title": f"{title}", 
            "author": f"{author}", 
            "year": f"{year}",
            "isbn": f"{isbn}", 
            "description": f"{description}"
            }
    fh = open(f'{file}.json', 'a')
    json_data = json.dumps(pre_json, indent=4)
    fh.write(f',\n{json_data}')
    fh.close

