#!/usr/bin/python3
'''Creates class that inherits from list builtin functions'''


class MyList(list):
    '''Class that inherits from list'''


    def print_sorted(self):
        '''Prints the list in ascending order'''
        print(sorted(self))
