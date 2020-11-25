import user, sys, os, re, data, console_io, json
def main():
    
    if len(sys.argv) != 6:
        print ('Must pass in 6 system arguments')
    else:
        file_name = sys.argv[0]
        file = file_name[2:-3]
        title = sys.argv[1]
        author = sys.argv[2]
        year = sys.argv[3]
        isbn = sys.argv[4]
        description = sys.argv[5]
    quit = False
    if os.path.isfile(f"{file}.json"):
        book_file = open(f"{file}.json")
        book_data = book_file.read()
        book_file.close()
        book_list = json.loads(book_data)
    else:
        book_list = []
        book = {"title": title, "author": author, "year": int(year), "isbn": isbn, "description": description}
        book_list.append(book)
    while not quit:
        user_choice = user.get_user_input() #get the user choice
        try:
            if user_choice == "a":
                print('Add a Book')
                new_title = input('Enter Title: ')
                new_author = input('Enter Author: ')
                new_year = input('Enter Year: ')
                new_isbn = input('Enter ISBN: ')
                new_description = input('Enter Description: ')
                console_io.check_data(file_name, new_title, new_author, new_year, new_isbn, new_description)
                book = {"title": new_title, "author": new_author, "year": int(new_year), "isbn": new_isbn, "description": new_description}
                book_list.append(book)
                
                

            elif user_choice == "d":
                print('Delete book')

                delete = input("Enter ISBN: ")

                if re.search("^[0-9]{4}$", delete) is None:
                    raise ValueError("Invalid title Search Term")

                found_match = False

                new_list = []
                for book in book_list:  # incase you remove multiple [:]
                    if delete == book['isbn']:
                        print(book)
                        book_list.remove(book)
                        found_match = True

                if not found_match:
                    print("ISBN does not exists try a diffrent one")
                        

            elif user_choice == "s":
                print('Summary List')
                if len(book_list) > 0:
                    for book in book_list:
                        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, ISBN: {book['isbn']}, Description: {book['description']}")

                else:
                    print("No books yet")

            elif user_choice == "t":
                print('Search Book')

                title = input("Enter title: ")

                if re.search("[a-zA-Z0-9]+[ ]*", title) is None:
                    raise ValueError("Invalid title Search Term")

                found_match = False
                for book in book_list:

                    if title.lower() in book["title"].lower():
                        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, ISBN: {book['isbn']}, Description: {book['description']}")
                        found_match = True

                if not found_match:
                    print("No matches found")

            elif user_choice == "u":
                print('Search by Author')

                author = input("Enter author: ")

                if re.search("[a-zA-Z0-9]+[ ]*", title) is None:
                    raise ValueError("Invalid title Search Term")

                found_match = False
                for book in book_list:

                    if author in book["author"]:
                        print(f"Title: {book['title']}, Author {book['author']}, Year: {book['year']}, ISBN: {book['isbn']}, Description: {book['description']}")
                        found_match = True

                if not found_match:
                    print("No matches found")

            elif user_choice == "k":

                if len(book_list) > 0:
                    for book in book_list:
                        print("%s %s %d" % (book["title"], book["author"], book["year"]))

                else:
                    print("No books yet")

            elif user_choice == "q":
                print("Quitting Program")

                data.save_book_list(book_list, f"{file}.json")

                quit = True

            else:
                print("Invalid Selection. Try Again.")

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()