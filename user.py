import re

def get_user_input():
    print('Add a Book (a)\nDelete a Book (d)\nView Book Summary (s)\nSearch Book by Title (t)\nSearch Book by Author (u)\nSearch by Keyword (k)\nQuit (q)')
    user_input = input()
    return user_input


def user_actions(user_input):
    prem = False
    perm2 = True
    while perm2:
        if user_input == 'a':
            print('Adding a book...\n')
            return user_input 
        elif user_input == 'd':
            print('Deleting book...\n') 
            return user_input 
        elif user_input == 's':
            print('Book Summary...\n') 
            return user_input 
        elif user_input == 't':
            print('Searching by Title...\n')
            return user_input 
        elif user_input == 'u':
            print('Searching by Author...\n') 
            return user_input 
        elif user_input == 'k':
            print('Searching by Keyword...\n') 
            return user_input 
        elif user_input == 'q':
            print('quitting')
            exit()
        else:
            print('Please enter a valid argument')
            user_input = input()
