#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    diccionario = {}
    anagrams = 0
    index = 0
    letters = 1
    
    while index + letters < len(s):
        key = Counter(s[index:index+letters])

        index2 = index + 1

        while index2 + letters - 1 < len(s):
            compared = Counter(s[index2:index2+letters])
            dic_key = key

            index2 = index2 + 1
            if dic_key not in diccionario:
                diccionario[dic_key] = (key - compared) == {}
            
            if diccionario[dic_key]:
                    anagrams = anagrams + 1

        if index + letters == len(s) - 1:
            index = index + 1
            letters = 1
        else:
            letters = letters + 1
    
    return anagrams

def allPossibleSubStrings(s):
    substrings = []

    for i, val in enumerate(s):
        for j, val2 in enumerate(s):
            substring = s[i:j+1]
            if substring not in substrings:
                substrings.append(substring)

    substrings.sort(key=lambda x: len(x))

    return substrings

def sherlockAndAnagrams2(s):
    dictionary = dict({})

    for i in range(len(s)):
        for j in range(1, len(s) - i + 1):
            sub = s[i:i+j]
            key = sum([ord(char) for char in sub])

            if key not in dictionary:
                dictionary[key] = [0, 0, sub]
            else:
                for sub2 in map(lambda x: x[2], dictionary.values()):
                    if((Counter(sub) - Counter(sub2)) == {}):
                        dictionary[key][0] += 1
                        dictionary[key][1] += dictionary[key][0]
                        break
    
    return sum(map(lambda x: x[1], dictionary.values()))


if __name__ == '__main__':
    s = 'abba'

    print(sherlockAndAnagrams2(s))