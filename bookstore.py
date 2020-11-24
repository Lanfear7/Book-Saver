import user, sys, os, re, data, console_io
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
        book_data = books_file.read()
        book_file.close()
        book_list = json.loads(book_data)
    else:
        book_list = []
    while not quit:
        user_choice = user.get_user_input()
        try:
            if user_choice == "a":
                console_io.check_data(title, author, year)
                book = {"title": new_title, "author": new_author, "year": int(new_year), "isbn": new_isbn, "description": new_description}
                book_list.append(book)
                data.save_book_list(book_list, f"{file}.json")

            elif user_choice == "d":
                if len(book_list) > 0:
                    for book in book_list:
                        print("%s %s %d" % (book["title"], book["author"], book["year"]))

                else:
                    print("No books yet")


            elif user_choice == "s":
                if len(book_list) > 0:
                    for book in book_list:
                        print("%s %s %d" % (book["title"], book["author"], book["year"]))

                else:
                    print("No books yet")


            elif user_choice == "t":
                title = input("Enter title: ")

                if re.search("[a-zA-Z0-9]+[ ]*", title) is None:
                    raise ValueError("Invalid title Search Term")

                found_match = False
                for book in book_list:

                    if title.lower() in book["title"].lower():
                        print(f"Match: {book.title} {book.author} {book.year} {book.isbn} {book.description}")
                        found_match = True

                if not found_match:
                    print("No matches found")

            elif user_choice == "u":

                if len(book_list) > 0:
                    for book in book_list:
                        print("%s %s %d" % (book["title"], book["author"], book["year"]))

                else:
                    print("No books yet")

            elif user_choice == "k":

                if len(book_list) > 0:
                    for book in book_list:
                        print("%s %s %d" % (book["title"], book["author"], book["year"]))

                else:
                    print("No books yet")

            elif user_choice == "q":
                print("Quitting Program")
                quit = True

            else:
                print("Invalid Selection. Try Again.")

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()