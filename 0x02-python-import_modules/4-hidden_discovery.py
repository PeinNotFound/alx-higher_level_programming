#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    for test in dir(hidden_4):
        if test[0] != '_':
            print(test)
