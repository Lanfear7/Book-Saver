import user, data, sys, re


def main():
    if len(sys.argv) != 6:
        print ('Must pass in 6 system arguments')
    else:
        print('***ARGV PASS***')
        file_name = sys.argv[0]
        title = sys.argv[1]
        author = sys.argv[2]
        year = sys.argv[3]
        isbn = sys.argv[4]
        description = sys.argv[5]
        data.store_data(file_name, title, author, year, isbn, description)



if __name__ == "__main__":
    main()
    