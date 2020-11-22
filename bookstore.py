import user, console_io, data, sys, re


def main():
    perm = True
    while perm:
        if len(sys.argv) != 6:
            print ('Must pass in 6 system arguments')
            break
        else:
            print('***ARGV PASS***')
            file_name = sys.argv[0]
            title = sys.argv[1]
            author = sys.argv[2]
            year = sys.argv[3]
            isbn = sys.argv[4]
            description = sys.argv[5]
            book_data = data.store_data(file_name, title, author, year, isbn, description)
            print(book_data)
            user_input = user.get_user_input()
            action = user.user_actions(user_input)
            if action == "a":
                new_title = input('Title: ')
                new_author = input('Author: ')
                new_year = input('Year: ')
                new_isbn = input('ISBN: ')
                new_description = input('Description: ')
                console_io.check_data(file_name, new_title, new_author, new_year, new_isbn, new_description)

            




if __name__ == "__main__":
    main()
    