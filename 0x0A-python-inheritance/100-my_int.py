#!/usr/bin/python3
'''MyInt Module'''


class MyInt(int):
    '''MyInt Class'''
    def __eq__(self, other):
        '''EQ function'''
        return (super().__ne__(other))

    def __ne__(self, other):
        '''Ne function'''
        return (super().__eq__(other))
