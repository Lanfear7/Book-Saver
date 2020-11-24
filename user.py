import re

def get_user_input():
    print('Add a Book (a)\nDelete a Book (d)\nView Book Summary (s)\nSearch Book by Title (t)\nSearch Book by Author (u)\nSearch by Keyword (k)\nQuit (q)')
    user_input = input()
    return user_input
