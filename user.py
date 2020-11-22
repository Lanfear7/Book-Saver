def user_actions(user_input):
    if user_input == 'a':
        print('Adding a book...\n') 
    elif user_input == 'd':
        print('Deleting book...\n') 
    elif user_input == 's':
        print('Book Summary...\n') 
    elif user_input == 't':
        print('Searching by Title...\n')
    elif user_input == 'u':
        print('Searching by Author...\n') 
    elif user_input == 'k':
        print('Searching by Keyword...\n') 
    elif user_input == 'q':
        print('quitting')
    else:
        print('Please enter a valid argument')
