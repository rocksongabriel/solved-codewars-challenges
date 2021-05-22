# This is my solution of the detect pangram problem

import string

def is_pangram(s):
    alphas = 'abcdefghijklmnopqrstuvwxyz'
    for alpha in alphas:
        if alpha not in set(s.lower()):
            return False
    return True