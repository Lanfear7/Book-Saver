import os, json

def save_book_list(book_list, book_file):
    """ Save the book_list as json in the json file """
    book_file = open(book_file, "w")
    book_json = json.dumps(book_list, indent=4)
    book_file.write(book_json)
    book_file.close()

