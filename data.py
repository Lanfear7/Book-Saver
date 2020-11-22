import os

def store_data(file_name, title, author, year, isbn, description):
    print(f'working ok\n Data: {file_name} {title} {author} {year} {isbn} {description}')
    file = file_name[2:-3]
    if os.path.isfile(f'{file}.json'):
        print('already have the data file')
        fh = open(f'{file}.json', 'r')
        data = fh.read()
        fh.close()
        print(data)
    else:
        print(file)
        fh = open(f'{file}.json', 'w')
        current_data = f'{file} {title} {author} {year} {isbn} {description}'
        fh.write(current_data)
        fh.close()