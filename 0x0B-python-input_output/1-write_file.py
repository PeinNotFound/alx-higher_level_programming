#!/usr/bin/python3

def write_file(filename="", text=""):
    try:
        ''' Open the file in write mode ('w') with UTF-8 encoding'''
        with open(filename, 'w', encoding='utf-8') as file:
             
            '''Write the text to the file'''
            file.write(text)
             
            '''Return the number of characters written'''
            return len(text)
    except Exception as e:

        ''' Handle any exceptions (e.g., file not found, permission issues)'''

        print(f"Error writing to file: {e}")
        return 0
