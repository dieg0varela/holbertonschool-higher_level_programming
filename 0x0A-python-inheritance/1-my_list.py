#!/usr/bin/python3
'''MyList Module'''


class MyList(list):
    '''MyList Class'''
    def print_sorted(self):
        '''Print Sorted List'''
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
