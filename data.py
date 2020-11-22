import os, json

def store_data(file_name, title, author, year, isbn, description):
    print(f'DATA FILE working ok    ----- Data: {file_name} {title} {author} {year} {isbn} {description}')
    file = file_name[2:-3]
    if os.path.isfile(f'{file}.json'):
        print('already have the data file')
        fh = open(f'{file}.json', 'r')
        data = fh.read()
        fh.close()
        return data
    else:
        print(file)
        fh = open(f'{file}.json', 'a')
        pre_json = {
            "file": f"{file}",
            "title": f"{title}", 
            "author": f"{author}", 
            "year": f"{year}",
            "isbn": f"{isbn}", 
            "description": f"{description}"
            }
        json_data = json.dumps(pre_json, indent=4)
        fh.write(json_data)
        fh.close()

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

